// Render an HTML animation to MP4 and WebM, frame by frame, in headless Chrome.
//
// Usage (playwright-core is not a repo dependency; point NODE_PATH at any install):
//   NODE_PATH=<dir>/node_modules node scripts/video/record.js <page.html> <out-base> [--driver <driver.js>]
//
// A page either exposes window.__seek(t) (seconds) and window.__duration, or a driver module
// exports { duration, async step(page, t, ctx) } and moves the real mouse. CSS transitions and
// Web Animations are paused and seeked to the frame time, so playback is deterministic.
// Output: <out-base>.mp4 (H.264) and <out-base>.webm (VP9), 1920 px wide, 30 fps.

const { chromium } = require('playwright-core');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const [pagePath, outBase] = args;
const driverPath = opt('--driver');
const FPS = +opt('--fps', 30);
const OUT_W = +opt('--width', 1920);
const CHROME = process.env.CHROME || process.env.HOME +
  '/Library/Caches/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-mac-arm64/chrome-headless-shell';

(async () => {
  const driver = driverPath ? require(path.resolve(driverPath)) : null;
  const html = fs.readFileSync(path.resolve(pagePath), 'utf8');
  const vp = (opt('--viewport') || (html.match(/data-viewport="(\d+x\d+)"/) || [])[1] || '1280x800').split('x');
  const [vw, vh] = vp.map(Number);
  const browser = await chromium.launch({ executablePath: CHROME });
  const page = await browser.newPage({ viewport: { width: vw, height: vh }, deviceScaleFactor: OUT_W / vw });
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  await page.goto('file://' + path.resolve(pagePath) + (driver && driver.hash || ''));
  await page.addScriptTag({ path: path.join(__dirname, 'cursor.js') });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);

  const duration = driver ? driver.duration : await page.evaluate(() => window.__duration);
  const frames = Math.round(duration * FPS);
  const tmp = fs.mkdtempSync(path.join(require('os').tmpdir(), 'rec-'));
  const ctx = {};
  for (let f = 0; f < frames; f++) {
    const t = f / FPS;
    if (driver) await driver.step(page, t, ctx);
    else await page.evaluate(t => window.__seek(t), t);
    await page.evaluate(ms => window.__syncAnimations(ms), t * 1000);
    await page.screenshot({ path: path.join(tmp, String(f).padStart(5, '0') + '.png') });
  }
  await browser.close();
  if (errors.length) console.error('page errors:', errors);

  const run = a => new Promise((ok, no) => spawn('ffmpeg', a, { stdio: 'inherit' }).on('exit', c => c ? no(c) : ok()));
  // H.264 and VP9 need even frame sizes
  const input = ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(tmp, '%05d.png'), '-vf', 'crop=trunc(iw/2)*2:trunc(ih/2)*2'];
  await run([...input, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'slow', '-movflags', '+faststart', outBase + '.mp4']);
  await run([...input, '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuv420p', '-crf', '30', '-b:v', '0', '-row-mt', '1', outBase + '.webm']);
  await run(['-y', '-loglevel', 'error', '-i', path.join(tmp, String(frames - 1).padStart(5, '0') + '.png'), '-vf', 'scale=1920:-1', outBase + '-poster.jpg']);
  fs.rmSync(tmp, { recursive: true });
  console.log(`${outBase}: ${frames} frames, ${duration}s`);
})();
