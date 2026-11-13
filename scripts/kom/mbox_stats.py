"""Aggregate the mbox index: years, senders, sent-to domains, Basecamp projects."""
import collections
import email.utils
import json
import re
import sys

idx_path, out_path = sys.argv[1], sys.argv[2]
GENERIC = {"gmail.com", "hotmail.com", "yahoo.es", "yahoo.com", "hotmail.es", "outlook.com",
           "googlemail.com", "msn.com", "live.com", "icloud.com", "me.com", "mac.com",
           "telefonica.net", "terra.es", "kingsofmambo.com"}


def domains(field):
    return [a.split("@")[-1].lower().strip(">") for _, a in email.utils.getaddresses([field]) if "@" in a]


def year(d):
    m = re.search(r"\b(19|20)\d\d\b", d or "")
    return m.group(0) if m else "?"


by_year = collections.Counter()
sent_year = collections.Counter()
sent_dom = collections.defaultdict(lambda: {"n": 0, "years": collections.Counter(), "subjects": []})
from_addr = collections.Counter()
bc_proj = collections.defaultdict(lambda: {"n": 0, "years": collections.Counter(), "subjects": []})
att_types = collections.Counter()
own = collections.Counter()

for line in open(idx_path, encoding="utf-8"):
    r = json.loads(line)
    if "error" in r:
        continue
    y = year(r["date"])
    by_year[y] += 1
    labels = r["labels"]
    if re.search(r"\b(Spam|Trash)\b", labels):
        continue
    if "Sent" in labels:
        sent_year[y] += 1
        own[r["from"]] += 1
        for d in set(domains(r["to"] + "," + r["cc"])):
            if d in GENERIC:
                continue
            s = sent_dom[d]
            s["n"] += 1
            s["years"][y] += 1
            if len(s["subjects"]) < 15 and r["subject"] not in s["subjects"]:
                s["subjects"].append(r["subject"])
    m = re.search(r"Basecamp/([^,]+)", labels)
    if m or "basecamp" in r["from"].lower():
        p = m.group(1) if m else re.sub(r"^\(?([^)]*)\)?.*", r"\1", r["subject"])[:40]
        p = m.group(1) if m else (re.match(r"\(([^)]+)\)", r["subject"]) or [None, "?"])[1]
        b = bc_proj[p]
        b["n"] += 1
        b["years"][y] += 1
        if len(b["subjects"]) < 10 and r["subject"] not in b["subjects"]:
            b["subjects"].append(r["subject"])
    for a in r["attachments"]:
        ext = a["name"].rsplit(".", 1)[-1].lower() if "." in a["name"] else a["type"]
        att_types[ext] += 1

res = {
    "by_year": dict(sorted(by_year.items())),
    "sent_by_year": dict(sorted(sent_year.items())),
    "own_from": own.most_common(10),
    "sent_domains": sorted(
        ({"domain": d, "n": v["n"], "years": dict(sorted(v["years"].items())), "subjects": v["subjects"]}
         for d, v in sent_dom.items()), key=lambda x: -x["n"])[:120],
    "basecamp_projects": sorted(
        ({"project": p, "n": v["n"], "years": dict(sorted(v["years"].items())), "subjects": v["subjects"]}
         for p, v in bc_proj.items()), key=lambda x: -x["n"])[:80],
    "attachment_types": att_types.most_common(40),
}
json.dump(res, open(out_path, "w"), ensure_ascii=False, indent=1)
