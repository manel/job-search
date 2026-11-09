"""Dedup inventory JSON and write a page catalog TSV (no body text). Args: inv.json out_dedup.json out.tsv"""
import json, os, re, sys
d = json.load(open(sys.argv[1]))
by = {}
for p in d["pages"]:
    k = p["id"] or p["path"]
    if k not in by or (not p.get("md") and p["words"] > by[k]["words"]):
        by[k] = p
P = list(by.values())
json.dump(P, open(sys.argv[2], "w"), ensure_ascii=False)
EXCL = re.compile(r"Design candidates|Design hiring|Potential Participants|Mentors database|Engineers |Design onboarding|Group interview|Yummy|Interview guide|PDP|1-1->|1 1 → Manel|Career levels|Career path|Feedback|Self assessment|Peer feedback")
WHO = ("Owner", "Owner(s)", "Author", "Created by", "Designer", "Researcher", "Reporter", "Built by")
WHEN = ("Date", "Created time", "Created", "Created at", "Last updated", "Maker day", "Period")
clean = lambda s: re.sub(r"\s+", " ", re.sub(r" [0-9a-f]{32}", "", s)).strip()
rows = []
for p in P:
    if EXCL.search(p["path"]) or p.get("md"):
        continue
    pr = p["props"]
    who = next((pr[k] for k in WHO if pr.get(k)), "")
    when = next((pr[k].lstrip("@") for k in WHEN if pr.get(k)), "")
    db = clean(os.path.basename(os.path.dirname(p["path"])))
    rows.append((clean(p["title"]), db, who, when, str(p["words"]), clean(p["path"])))
rows.sort(key=lambda r: (r[5]))
with open(sys.argv[3], "w") as f:
    f.write("title\tparent\towner_or_author\tdate\twords\tpath\n")
    for r in rows:
        f.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
print(len(P), "unique;", len(rows), "catalogued")
