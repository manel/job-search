import json, os, sys, glob, re
D, OUT = sys.argv[1], sys.argv[2]
NOTE_CAP = int(os.environ.get('NOTE_CAP', '600'))
def link(fk, nid): return f"https://www.figma.com/design/{fk}/?node-id={nid.replace(':','-')}"
def clip(s, n):
    s = s.replace('|', '/')
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + ' …'
def flat(nodes, path=()):
    for n in nodes:
        if n['type'] == 'SECTION' and 'kids' in n:
            yield ('section', n, path)
            yield from flat(n['kids'], path + (n['name'],))
        else:
            yield ('node', n, path)
for fd in sorted(glob.glob(os.path.join(D, '*/_pages.json'))):
    d = os.path.dirname(fd); meta = json.load(open(fd)); fk = meta['fileKey']
    if len(sys.argv) > 3 and fk not in sys.argv[3:]: continue
    L = [f"# {meta['file']}", "", f"Raw catalog generated {__import__('datetime').date.today()} from the Figma Desktop Bridge. File: [{fk}](https://www.figma.com/design/{fk}). Every visible top-level node on every page is listed; frames inside sections are listed under the section. \"Notes\" is designer-placed text outside component instances (capped at {NOTE_CAP} characters per frame); \"UI\" counts text strings inside instances; full text is in the JSON dump.", ""]
    tot = {'frames': 0, 'img': 0}
    for p in meta['pages']:
        f = os.path.join(d, f"p{p['i']:03d}.json")
        if not os.path.exists(f):
            err = f[:-5] + '.err'
            L += [f"## {p['name']}", "", f"NOT EXTRACTED{': ' + open(err).read() if os.path.exists(err) else ''}", ""]; continue
        pg = json.load(open(f)); top = pg['top']
        if re.fullmatch(r'[-—·\s]*', p['name']) and not top: continue
        L += [f"## {p['name']}", "", f"[page]({link(fk, p['id'])}) · {len(top)} top-level nodes", ""]
        if not top: L += ["(empty)", ""]; continue
        L += ["| Node | Type | Size | Notes | UI / inst / img | Link |", "|---|---|---|---|---|---|"]
        for kind, n, path in flat(top):
            name = ' / '.join(path + (n['name'],)).replace('|', '/')
            if kind == 'section':
                L.append(f"| **§ {name}** | SECTION | {n['w']}×{n['h']} | {len(n['kids'])} children | | [open]({link(fk, n['id'])}) |"); continue
            tot['frames'] += 1; tot['img'] += n.get('nImages', 0)
            notes = ' · '.join(n.get('notes', []))
            ui = n.get('ui', [])
            if n['type'] == 'INSTANCE' and len(ui) <= 40:
                notes = (notes + ' · ' if notes else '') + ' · '.join(ui)
            elif ui:
                notes = (notes + ' · ' if notes else '') + 'UI: ' + clip(' · '.join(ui[:12]), 220)
            ann = ' · '.join(n.get('ann', []))
            if ann: notes = (notes + ' · ' if notes else '') + 'ANNOTATIONS: ' + ann
            comps = n.get('comps', [])
            if comps:
                cs = '; '.join(f"{c['name']}" + (f" ({c['variants']} var)" if c.get('set') else '') for c in comps[:40])
                notes = (notes + ' · ' if notes else '') + f"COMPONENTS ({len(comps)}): " + cs
            L.append(f"| {clip(name, 120)} | {n['type']} | {n['w']}×{n['h']} | {clip(notes, NOTE_CAP)} | {len(n.get('ui', []))} / {n.get('inst', 0)} / {n.get('nImages', 0)} | [open]({link(fk, n['id'])}) |")
        L.append("")
    L[2] += f" Totals: {len(meta['pages'])} pages, {tot['frames']} frames/nodes, {tot['img']} image fills."
    name = re.sub(r'[^a-z0-9]+', '-', meta['file'].lower()).strip('-')
    open(os.path.join(OUT, f"{name}--{fk[:6]}.md"), 'w').write('\n'.join(L) + '\n')
    print(name, tot)
