"""Search the mbox index bodies and subjects, grouped by thread.

Usage: mbox_search.py index.jsonl out.tsv body_regex [--sent-only] [--subject regex]
Skips Spam, Trash, promotions, forums, updates and social categories.
Writes: first date, last date, messages, sent by Manel, hits, sample hit, subject.
"""
import argparse
import email.utils
import json
import re

ap = argparse.ArgumentParser()
ap.add_argument("index")
ap.add_argument("out")
ap.add_argument("body")
ap.add_argument("--sent-only", action="store_true")
ap.add_argument("--subject")
a = ap.parse_args()
body_re = re.compile(a.body, re.I)
subj_re = re.compile(a.subject, re.I) if a.subject else None
NOISE = re.compile(r"Spam|Trash|Category (promotions|forums|updates|social)")
QUOTE = re.compile(r"\n(El |On |Em ).{5,200}(escribió|va escriure|wrote|escreveu):", re.S)

threads = {}
for line in open(a.index, encoding="utf-8"):
    r = json.loads(line)
    if "error" in r or NOISE.search(r["labels"]):
        continue
    sent = "Sent" in r["labels"] and r["from"].startswith("Manel")
    if a.sent_only and not sent:
        continue
    if subj_re and not subj_re.search(r["subject"]):
        continue
    own = QUOTE.split(r["body"])[0]
    own = "\n".join(l for l in own.splitlines() if not l.startswith(">"))
    m = body_re.search(r["subject"] + "\n" + own)
    if not m:
        continue
    try:
        dt = email.utils.parsedate_to_datetime(r["date"]).strftime("%Y-%m-%d")
    except Exception:
        dt = "????-??-??"
    key = r["thread"] or re.sub(r"^((re|fw|fwd|rv)\s*:\s*)+", "", r["subject"], flags=re.I).lower()
    t = threads.setdefault(key, {"first": dt, "last": dt, "n": 0, "sent": 0, "subject": r["subject"], "sample": ""})
    t["first"], t["last"] = min(t["first"], dt), max(t["last"], dt)
    t["n"] += 1
    t["sent"] += sent
    if not t["sample"]:
        s = own[max(0, m.start() - 120): m.end() + 160]
        t["sample"] = re.sub(r"\s+", " ", s)

with open(a.out, "w", encoding="utf-8") as f:
    for t in sorted(threads.values(), key=lambda t: (-t["n"], t["first"])):
        f.write(f'{t["first"]}\t{t["last"]}\t{t["n"]}\t{t["sent"]}\t{t["subject"][:90]}\t{t["sample"][:300]}\n')
print(len(threads), "threads ->", a.out)
