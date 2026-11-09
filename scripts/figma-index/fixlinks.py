import json, re, sys
f, fk = sys.argv[1], sys.argv[2]
D = '/private/tmp/claude-501/-Users-manel-Dev-job-search/91b163b4-5337-49d5-ab76-a35017449750/scratchpad/figma-dump'
P = json.load(open(f'{D}/{fk}/_pages.json'))['pages']
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
L = open(f).read().split('\n'); section = None; out = []; miss = 0
for l in L:
    if l.startswith('## '): section = l.lower()
    if l.startswith('| ') and f'{fk}/)' in l:
        name = norm(l.split('|')[1])
        hits = [p for p in P if norm(p['name']) == name] or [p for p in P if norm(p['name']).startswith(name) or name.startswith(norm(p['name']))]
        if len(hits) > 1:  # handoff vs exploration duplicates: first is handoff
            hits = hits[1:] if section and 'exploration' in section else hits[:1]
        if hits: l = l.replace(f'{fk}/)', f"{fk}/?node-id={hits[0]['id'].replace(':','-')})")
        else: miss += 1; print('nomatch', l[:70])
    out.append(l)
open(f, 'w').write('\n'.join(out)); print('remaining root links', sum(f'{fk}/)' in l for l in out))
