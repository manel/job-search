// Driver for record.js: plays a scripted mouse path over scripts/video/abax-table-selection.html.
// Positions are in table coordinates (0,0 = table top-left, 659x408); 'mDnd' targets the variant button.
// Record with: node scripts/video/record.js scripts/video/abax-table-selection.html <out> --driver <this file>

// [time, action, x, y, moveDuration]
const SCRIPT = [
  [0.0, 'at', 600, 330],
  [1.3, 'move', 180, 100, 0.9],      // hover a cell
  [1.8, 'click'],                    // select it
  [2.9, 'move', 420, 180, 0.7],      // hover another cell while one is selected
  [4.1, 'move', 240, 120, 0.7],      // range handle
  [4.4, 'down'],
  [5.9, 'move', 470, 252, 1.5],      // expand the range
  [6.1, 'up'],
  [6.8, 'move', 60, 22, 0.8],        // header row: the column indicator follows the mouse
  [8.4, 'move', 620, 22, 1.5],
  [9.3, 'move', 438, 0, 0.7],        // column indicator
  [9.7, 'click'],                    // select the column
  [10.7, 'move', 300, 22, 0.6],
  [11.0, 'click'],                   // select the header cell
  [12.0, 'move', 3, 100, 0.8],       // left edge: the row indicator follows the mouse
  [13.4, 'move', 3, 330, 1.3],
  [14.1, 'move', 0, 220, 0.6],       // row indicator
  [14.5, 'click'],                   // select the row
  [15.7, 'move', 'mDnd', 0, 1.0],
  [16.0, 'click'],                   // switch to the drag and drop variant
  [17.2, 'move', 300, 0, 1.0],       // column grip
  [17.7, 'down'],
  [19.1, 'move', 525, 6, 1.3],       // drag the column
  [19.4, 'up'],
  [20.6, 'move', 0, 100, 0.9],       // row grip
  [21.0, 'down'],
  [22.3, 'move', 0, 285, 1.2],       // drag the row
  [22.6, 'up'],
  [23.8, 'move', 760, 330, 0.9],
  [24.1, 'click'],                   // click outside to clear
];
const duration = 25.5;
const ease = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;

async function step(page, t, ctx) {
  if (!ctx.box) {
    ctx.box = await page.$eval('#table', el => { const r = el.getBoundingClientRect(); return { x: r.left, y: r.top, s: r.width / el.offsetWidth }; });
    ctx.mDnd = await page.$eval('#mDnd', el => { const r = el.getBoundingClientRect(); return [r.left + r.width / 2, r.top + r.height / 2]; });
    ctx.done = 0; ctx.pos = null; ctx.lastPress = -9;
  }
  const abs = (x, y) => x === 'mDnd' ? ctx.mDnd : [ctx.box.x + x * ctx.box.s, ctx.box.y + y * ctx.box.s];
  // position at time t
  let pos = null;
  for (const [ts, a, x, y, d] of SCRIPT) {
    if (a === 'at' && ts <= t) pos = abs(x, y);
    if (a === 'move') {
      const t0 = ts - d, to = abs(x, y);
      if (t >= ts) pos = to;
      else if (t >= t0) { const from = pos; const k = ease((t - t0) / d); pos = [from[0] + (to[0] - from[0]) * k, from[1] + (to[1] - from[1]) * k]; break; }
      else break;
    }
  }
  if (!ctx.pos || pos[0] !== ctx.pos[0] || pos[1] !== ctx.pos[1]) { await page.mouse.move(pos[0], pos[1]); ctx.pos = pos; }
  // buttons whose time has come
  while (ctx.done < SCRIPT.length && SCRIPT[ctx.done][0] <= t) {
    const a = SCRIPT[ctx.done][1];
    if (a === 'down' || a === 'click') { await page.mouse.down(); ctx.lastPress = SCRIPT[ctx.done][0]; }
    if (a === 'up' || a === 'click') await page.mouse.up();
    ctx.done++;
  }
  const pressed = Math.max(0, 1 - (t - ctx.lastPress) / 0.35);
  await page.evaluate(([x, y, p]) => window.__cursor(x, y, p), [pos[0], pos[1], pressed]);
}

module.exports = { duration, step, hash: '' };
