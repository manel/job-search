import json, os, sys, glob, re
from collections import Counter, OrderedDict
D = sys.argv[1]; fk = sys.argv[2]; CAP = int(sys.argv[3]) if len(sys.argv) > 3 else 2500
d = os.path.join(D, fk); meta = json.load(open(os.path.join(d, '_pages.json')))
print(f"# {meta['file']} ({fk})")
NOISE = re.compile(r'^(Label|Specs|Status|Badge|Cursor|Arrow|Line|Vector|Rectangle|Ellipse|Group|Frame)\b', re.I)
def flat(nodes, path=()):
    for n in nodes:
        if n['type'] == 'SECTION' and 'kids' in n:
            yield ('S', n, path); yield from flat(n['kids'], path + (n['name'],))
        else: yield ('N', n, path)
for p in meta['pages']:
    f = os.path.join(d, f"p{p['i']:03d}.json")
    if not os.path.exists(f): print(f"\n## [{p['i']}] {p['name']} — NOT EXTRACTED"); continue
    top = json.load(open(f))['top']
    if not top: 
        if not re.fullmatch(r'[-—·\s]*', p['name']): print(f"\n## [{p['i']}] {p['name']} — empty")
        continue
    secs, names, notes, imgs, comps, frames = [], Counter(), OrderedDict(), 0, [], 0
    for k, n, path in flat(top):
        if k == 'S': secs.append(' / '.join(path + (n['name'],)) + f" ({n['id']})"); continue
        frames += 1
        names[n['name']] += 1; imgs += n.get('nImages', 0)
        src = list(n.get('notes', [])) + ['ANN: ' + a for a in n.get('ann', [])]
        if n['type'] == 'INSTANCE' and len(n.get('ui', [])) <= 12: src += n.get('ui', [])
        for s in src:
            s = re.sub(r' ×\d+$', '', s)
            if len(s) > 2 and s not in notes: notes[s] = n['id']
        comps += n.get('comps', [])
    print(f"\n## [{p['i']}] {p['name']} — {frames} nodes, {imgs} img")
    if secs: print("Sections: " + '; '.join(secs))
    big = [f"{nm}×{c}" if c > 1 else nm for nm, c in names.most_common() if not NOISE.match(nm)]
    print("Frames: " + clip if False else "Frames: " + ' | '.join(big)[:900])
    if comps: print(f"Components ({len(comps)}): " + '; '.join(c['name'] + (f"[{c['variants']}v]" if c.get('set') else '') + (f" — {c['desc'][:80]}" if c.get('desc') else '') for c in comps)[:1500])
    txt = ' ¶ '.join(f"{s} <{i}>" if len(s) > 40 else s for s, i in notes.items())
    print("Text: " + (txt[:CAP] + (f" …[+{len(txt)-CAP} chars]" if len(txt) > CAP else '')))
