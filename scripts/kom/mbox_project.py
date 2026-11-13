"""Dump one project's threads from the mbox index: unique subjects by date, plus Manel's sent bodies.

Usage: mbox_project.py index.jsonl out_dir name regex [regex ...]
A message matches when any regex hits subject, labels, from, to or cc.
Spam, Trash, invoice and payroll subjects are skipped.
"""
import email.utils
import json
import re
import sys

idx, out_dir, name = sys.argv[1:4]
pats = [re.compile(p, re.I) for p in sys.argv[4:]]
SKIP = re.compile(r"factur|invoice|n[oó]mina|pagament|pago|IRPF|retenci", re.I)

rows = []
for line in open(idx, encoding="utf-8"):
    r = json.loads(line)
    if "error" in r or re.search(r"\b(Spam|Trash)\b", r["labels"]):
        continue
    hay = " ".join([r["subject"], r["labels"], r["from"], r["to"], r["cc"]])
    if not any(p.search(hay) for p in pats) or SKIP.search(r["subject"]):
        continue
    try:
        dt = email.utils.parsedate_to_datetime(r["date"]).strftime("%Y-%m-%d")
    except Exception:
        dt = "????-??-??"
    rows.append((dt, r))
rows.sort(key=lambda x: x[0])

seen = {}
for dt, r in rows:
    key = re.sub(r"^((re|fw|fwd|rv|tr)\s*:\s*|\[[^\]]*\]\s*)+", "", r["subject"], flags=re.I).strip().lower()
    s = seen.setdefault(key, {"first": dt, "last": dt, "n": 0, "sent": 0, "subject": r["subject"]})
    s["last"] = dt
    s["n"] += 1
    s["sent"] += "Sent" in r["labels"]

with open(f"{out_dir}/{name}-threads.tsv", "w", encoding="utf-8") as f:
    for s in sorted(seen.values(), key=lambda x: x["first"]):
        f.write(f'{s["first"]}\t{s["last"]}\t{s["n"]}\t{s["sent"]}\t{s["subject"][:110]}\n')

with open(f"{out_dir}/{name}-sent.txt", "w", encoding="utf-8") as f:
    for dt, r in rows:
        if "Sent" not in r["labels"] or not r["from"].startswith("Manel"):
            continue
        body = re.split(r"\n(El |On ).{10,200}(escribió|escribi|va escriure|wrote):", r["body"])[0]
        body = "\n".join(l for l in body.splitlines() if not l.startswith(">"))[:1500]
        f.write(f"### {dt} | {r['subject'][:100]} | to {r['to'][:80]}\n{body}\n\n")
print(name, len(rows), "messages", len(seen), "threads")
