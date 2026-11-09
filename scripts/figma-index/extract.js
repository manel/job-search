(async () => {
const FK = figma.fileKey;
const SKIP = (globalThis.__SKIP && globalThis.__SKIP[FK]) || [];
const post = async (p, body) => { for (let i=0;i<3;i++){ try { const r = await fetch('http://localhost:9232/?p='+encodeURIComponent(p), {method:'POST', body}); if (r.status===200) return true; } catch(e){} } return false; };
const T = s => (s||'').replace(/\s+/g,' ').trim().slice(0,2000);
function walk(node, ctx, acc) {
  if (node.visible === false) return;
  const t = node.type;
  if (t === 'TEXT' || t === 'STICKY' || t === 'SHAPE_WITH_TEXT') {
    const s = T(t==='TEXT' ? node.characters : (node.text && node.text.characters));
    if (s) (ctx.inInst ? acc.ui : acc.notes).push(s);
  }
  if (node.annotations && node.annotations.length) for (const a of node.annotations) { const s = T(a.label || a.labelMarkdown); if (s) acc.ann.push(s); }
  if ('fills' in node && Array.isArray(node.fills) && node.fills.some(f => f.type === 'IMAGE' && f.visible !== false)) acc.images.push({id: node.id, name: node.name, w: Math.round(node.width), h: Math.round(node.height)});
  if (t === 'COMPONENT_SET') { let props=[]; try { props = Object.keys(node.componentPropertyDefinitions||{}).map(k=>k.split('#')[0]); } catch(e){} acc.comps.push({id: node.id, name: node.name, set: true, variants: node.children.length, props, desc: T(node.description)}); }
  else if (t === 'COMPONENT' && !(node.parent && node.parent.type === 'COMPONENT_SET')) acc.comps.push({id: node.id, name: node.name, set: false, desc: T(node.description)});
  if (t === 'INSTANCE') { acc.inst++; }
  if ('children' in node) { const c2 = t === 'INSTANCE' ? {inInst: true} : ctx; for (const ch of node.children) walk(ch, c2, acc); }
}
const uniq = a => { const m = new Map(); for (const s of a) m.set(s, (m.get(s)||0)+1); return [...m].map(([s,n]) => n>1 ? s+' ×'+n : s); };
function summarize(n, depth) {
  if (n.type === 'SECTION' && depth < 4) {
    return {id: n.id, name: n.name, type: n.type, x: Math.round(n.x), y: Math.round(n.y), w: Math.round(n.width), h: Math.round(n.height), kids: n.children.filter(c=>c.visible!==false).map(c => summarize(c, depth+1))};
  }
  const acc = {notes: [], ui: [], ann: [], images: [], comps: [], inst: 0};
  walk(n, {inInst: n.type==='INSTANCE'}, acc);
  const o = {id: n.id, name: n.name, type: n.type, x: Math.round(n.x), y: Math.round(n.y), w: Math.round(n.width), h: Math.round(n.height), notes: uniq(acc.notes), ui: uniq(acc.ui), ann: uniq(acc.ann), images: acc.images.slice(0,20), nImages: acc.images.length, comps: acc.comps, inst: acc.inst};
  if (depth === 0 && (n.type === 'FRAME' || n.type === 'GROUP') && 'children' in n && n.children.length <= 80) o.kidNames = n.children.filter(c=>c.visible!==false).map(c => c.id+' '+c.name);
  return o;
}
const pages = figma.root.children;
const status = [];
await post(FK+'/_pages.json', JSON.stringify({file: figma.root.name, fileKey: FK, pages: pages.map((p,i)=>({i, id: p.id, name: p.name}))}));
for (let i = 0; i < pages.length; i++) {
  const p = pages[i];
  if (SKIP.includes(i)) continue;
  try {
    await post(FK+'/_cur.txt', i+' '+p.name);
    await p.loadAsync();
    const top = p.children.filter(c => c.visible !== false).map(c => summarize(c, 0));
    const ok = await post(FK+'/p'+String(i).padStart(3,'0')+'.json', JSON.stringify({i, id: p.id, name: p.name, top}));
    status.push([i, top.length, ok ? 1 : 0]);
  } catch (e) { status.push([i, 'ERR '+(e.message||e)]); await post(FK+'/p'+String(i).padStart(3,'0')+'.err', String(e.message||e)); }
}
await post(FK+'/_done.json', JSON.stringify(status));

})();
return 'started '+figma.fileKey;