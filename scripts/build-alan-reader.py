"""Build an offline interview reader from the canonical Textream pages and brief."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
brief = (ROOT / 'interviews/alan-first-interview.md').read_text()
pages = json.loads((ROOT / 'interviews/textream/alan-first-meeting.textream').read_text())
items = []
for page in pages:
    title = page.splitlines()[0].strip('[]')
    content = '\n'.join(page.splitlines()[1:]).strip()
    personal = title in ['Tell me about yourself', 'Why Alan', 'Working with Product and Engineering', 'Why did you leave Remuner?']
    items.append(dict(title=title, group='About me' if personal else 'Project battle cards',
                      kind='answer', battle=not personal, text=content))

for match in re.finditer(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', brief, re.M | re.S):
    title, body = match.groups()
    if title in ['First-call priorities', 'How I work — concrete evidence in reserve',
                 'What Alan does — comparison with Sanitas',
                 'Likely questions — preparation, not a confirmed script',
                 'Questions for Celine', 'Before and after', 'Sources and boundaries']:
        live = title in ['Questions for Celine', 'How I work — concrete evidence in reserve',
                         'Likely questions — preparation, not a confirmed script']
        items.append(dict(title=title, group='Interview' if live else 'Reference',
                          kind='notes', text=body.strip()))
items.append(dict(title='Meeting details', group='Reference', text=brief.split('## First-call priorities')[0].split('Adapted', 1)[-1].split('\n', 1)[-1].strip()))
items.append(dict(title='Evidence and follow-up cues', group='Reference', text=(ROOT / 'interviews/behavioral-battle-cards.md').read_text()))

questions = next(item for item in items if item['title'] == 'Questions for Celine')
items.remove(questions)
items.insert(4, questions)
items = [item for group in ['About me', 'Interview', 'Project battle cards', 'Reference']
         for item in items if item['group'] == group]

template = (ROOT / 'interviews/reader-template.html').read_text()
data = json.dumps(items, ensure_ascii=False).replace('<', '\\u003c')
out = ROOT / 'interviews/alan-reader.html'
out.write_text(template.replace('__READER_DATA__', data))
print(f'{out}: {len(items)} sections')
