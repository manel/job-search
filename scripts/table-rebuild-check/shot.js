const { chromium } = require('playwright-core');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.HOME + '/Library/Caches/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-mac-arm64/chrome-headless-shell' });
  const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
  await p.goto('file:///Users/manel/Dev/job-search/interviews/perk/perk-table-selection-rebuild.html');
  await p.waitForTimeout(800);
  const box = await p.$eval('#table', el => { const r = el.getBoundingClientRect(); return { x: r.left, y: r.top, s: r.width / 702 }; });
  const at = (x, y) => [box.x + x * box.s, box.y + y * box.s];
  const steps = [
    ['01-hover-cell', async () => p.mouse.move(...at(180, 60))],
    ['02-selected', async () => { await p.mouse.down(); await p.mouse.up(); }],
    ['03-hover-other', async () => p.mouse.move(...at(420, 180))],
    ['04-expanded', async () => { await p.mouse.move(...at(240, 80)); await p.mouse.down(); await p.mouse.move(...at(300, 150), {steps:5}); await p.mouse.move(...at(330, 190), {steps:5}); await p.mouse.up(); }],
    ['05-col-zone1', async () => p.mouse.move(...at(170, 30))],
    ['06-col-zone2', async () => p.mouse.move(...at(140, 2))],
    ['07-col-zone3', async () => p.mouse.move(...at(180, 0))],
    ['08-col-selected', async () => { await p.mouse.down(); await p.mouse.up(); }],
    ['09-header-selected', async () => { await p.mouse.move(...at(300, 28)); await p.mouse.down(); await p.mouse.up(); }],
    ['10-row-zone1', async () => p.mouse.move(...at(70, 100))],
    ['11-row-zone2', async () => p.mouse.move(...at(2, 88))],
    ['12-row-zone3', async () => p.mouse.move(...at(0, 100))],
    ['13-row-selected', async () => { await p.mouse.down(); await p.mouse.up(); await p.mouse.move(...at(300, 230)); }],
  ];
  for (const [n, f] of steps) { await f(); await p.waitForTimeout(150); await p.screenshot({ path: `shots/${n}.png` }); }
  await b.close();
})();
