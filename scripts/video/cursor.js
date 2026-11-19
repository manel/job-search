// Injected by record.js: a drawn pointer (headless screenshots show none) and animation sync.
(() => {
  const el = document.createElement('div');
  el.id = '__cursor';
  el.style.cssText = 'position:fixed;left:0;top:0;width:20px;height:24px;pointer-events:none;z-index:2147483647;display:none;';
  el.innerHTML = '<div id="__ring" style="position:absolute;left:-14px;top:-14px;width:28px;height:28px;border-radius:50%;background:rgba(0,120,178,.18);opacity:0"></div>' +
    '<svg width="20" height="24" viewBox="0 0 20 24" style="position:absolute;left:-2px;top:-1px">' +
    '<path d="M2 1.5v17.2l4.3-4.1 2.9 6.6 3-1.3-2.9-6.5h6z" fill="#111" stroke="#fff" stroke-width="1.4" stroke-linejoin="round"/></svg>';
  document.body.appendChild(el);
  // pressed: 0..1 strength of the click ring
  window.__cursor = (x, y, pressed = 0, visible = true) => {
    el.style.display = visible ? 'block' : 'none';
    el.style.transform = `translate(${x}px, ${y}px)`;
    const ring = document.getElementById('__ring');
    ring.style.opacity = pressed;
    ring.style.transform = `scale(${0.6 + 0.4 * pressed})`;
  };
  // Pause every running animation and set it to the frame time. Finished ones are completed so
  // transitionend handlers run.
  window.__syncAnimations = (now) => {
    for (const a of document.getAnimations()) {
      if (a.__t0 == null) { a.__t0 = now; a.pause(); }
      const d = a.effect.getComputedTiming().endTime;
      const ct = now - a.__t0;
      if (ct >= d) a.finish(); else a.currentTime = ct;
    }
  };
})();
