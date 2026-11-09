import json, sys, glob, os
D, fk = sys.argv[1], sys.argv[2]; pages = [int(x) for x in sys.argv[3:]]
for f in sorted(glob.glob(os.path.join(D, fk, 'p*.json'))):
    d = json.load(open(f))
    if pages and d['i'] not in pages: continue
    print(d['i'], d['name'], d['id'])
    def fl(ns, dep=1):
        for n in ns:
            if n['type'] == 'SECTION' or (n['type'] in ('FRAME','GROUP','RECTANGLE') and n['w'] >= 1000 and not n['name'].lower().startswith(('note','tooltip','jira','label'))):
                print('  '*dep + n['type'][0], n['id'], n['name'][:60], f"{n['w']}x{n['h']}", ('img' if n.get('nImages') else ''))
            if 'kids' in n: fl(n['kids'], dep+1)
    fl(d['top'])
