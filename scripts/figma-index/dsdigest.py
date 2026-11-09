import json, os, sys, re
D, fk = sys.argv[1], sys.argv[2]
d = os.path.join(D, fk); meta = json.load(open(os.path.join(d, '_pages.json')))
print('#', meta['file'])
def flat(ns):
    for n in ns:
        if n['type'] == 'SECTION' and 'kids' in n: yield from flat(n['kids'])
        else: yield n
for p in meta['pages']:
    f = os.path.join(d, f"p{p['i']:03d}.json")
    if not os.path.exists(f): print(p['i'], p['name'], 'MISSING'); continue
    top = json.load(open(f))['top']
    if not top: continue
    comps, notes, nodes = [], [], 0
    for n in flat(top):
        nodes += 1; comps += n.get('comps', [])
        for s in n.get('notes', []):
            if len(s) > 25 and s not in notes: notes.append(s)
    sets = [c for c in comps if c.get('set')]; singles = [c for c in comps if not c.get('set')]
    var = sum(c['variants'] for c in sets)
    pub = [c for c in comps if not c['name'].startswith(('.', '_'))]
    desc = sum(1 for c in comps if c.get('desc'))
    print(f"\n[{p['i']}] {p['name']} ({p['id']}) nodes={nodes} sets={len(sets)} variants={var} single={len(singles)} public={len(pub)} withDesc={desc}")
    if sets: print('  sets: ' + '; '.join(f"{c['name']}[{c['variants']}v: {','.join(dict.fromkeys(c['props']))[:80]}]" for c in sets)[:700])
    if singles: print('  single: ' + ', '.join(c['name'] for c in singles)[:300])
    ds = [f"{c['name']}: {c['desc'][:120]}" for c in comps if c.get('desc')]
    if ds: print('  desc: ' + ' | '.join(ds)[:500])
    if notes: print('  notes: ' + ' ¶ '.join(notes)[:600])
