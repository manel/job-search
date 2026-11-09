# Usage: finalize.py FK [FK...]  -> render catalogs, copy catalogs + PNGs to repo, rebuild images/README.md
import json, os, glob, shutil, subprocess, sys, re
S = '/private/tmp/claude-501/-Users-manel-Dev-job-search/91b163b4-5337-49d5-ab76-a35017449750/scratchpad'
D = S + '/figma-dump'; R = '/Users/manel/Dev/job-search/evidence/figma'
fks = sys.argv[1:]
if fks:
    subprocess.run(['python3', '-I', S + '/bin/render.py', D, S + '/catalog'] + fks, check=True)
    for fk in fks:
        for c in glob.glob(f'{S}/catalog/*--{fk[:6]}.md'): shutil.copy(c, f'{R}/catalog/')
names = {}; idx = {}
for pj in glob.glob(f'{D}/*/_pages.json'):
    m = json.load(open(pj)); names[m['fileKey']] = m['file'].replace(' | ', ' / ')
for f in glob.glob(f'{D}/*/p*.json'):
    fk = f.split('/')[-2]
    def fl(ns):
        for n in ns:
            idx[(fk, n['id'])] = (n['name'], f"{n['w']}x{n['h']}")
            for k in n.get('kidNames') or []:
                i, _, nm = k.partition(' '); idx.setdefault((fk, i), (nm, ''))
            if 'kids' in n: fl(n['kids'])
    fl(json.load(open(f))['top'])
rows = []
for d in sorted(glob.glob(f'{D}/images/*/')):
    fk = os.path.basename(d.rstrip('/'))
    if fk == 'VMALBdcCPmY2jhEl4C3tQM': continue
    os.makedirs(f'{R}/images/{fk}', exist_ok=True)
    for f in sorted(glob.glob(d + '*.png')):
        if os.path.getsize(f) < 12000: continue
        dst = f'{R}/images/{fk}/' + os.path.basename(f)
        if not os.path.exists(dst): shutil.copy(f, dst)
        nid = os.path.basename(f)[:-4].replace('-', ':', 1)
        nm, sz = idx.get((fk, nid), ('', ''))
        rows.append((names.get(fk, fk), fk, nid, nm.replace('|', '/')[:60], sz, os.path.basename(f)))
L = ['# Figma image exports', '', 'PNG exports of the image sources named in the per-file indexes, made 2026-11-09 from the Desktop Bridge (longest side capped at 1600px). Oversized sections were exported as their child frames. Files under 12 KB (label bars, blanks) were dropped. Many show real customer data: blur or replace before external use.', '', '| File | Node | Name | Size in Figma | PNG | Open in Figma |', '|---|---|---|---|---|---|']
for fn, fk, nid, nm, sz, png in rows:
    L.append(f"| {fn} | {nid} | {nm} | {sz} | [{png}]({fk}/{png}) | [open](https://www.figma.com/design/{fk}/?node-id={nid.replace(':','-')}) |")
open(f'{R}/images/README.md', 'w').write('\n'.join(L) + '\n')
print(len(rows), 'images indexed')
for fk in fks:
    c = glob.glob(f'{R}/catalog/*--{fk[:6]}.md')
    print(fk, os.path.basename(c[0]) if c else 'NO CATALOG', open(c[0]).read().split('\n')[2].split('Totals:')[-1] if c else '')
