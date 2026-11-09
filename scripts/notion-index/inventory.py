"""Inventory a Notion export: pages (HTML/MD) and CSV databases. No full reads."""
import csv, json, os, re, sys
from html.parser import HTMLParser
from html import unescape

ROOT = sys.argv[1]
OUT = sys.argv[2]
ID_RE = re.compile(r"\s?([0-9a-f]{32})(?=\.|$|/)")


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.in_props = 0
        self.in_th = self.in_td = False
        self.props, self.cur_k, self.cur_v = {}, "", ""
        self.in_body = False
        self.text = []
        self.headings, self.in_h = [], False
        self.skip = 0

    def handle_starttag(self, tag, a):
        a = dict(a)
        cls = a.get("class") or ""
        if tag == "title":
            self.in_title = True
        if tag in ("style", "script"):
            self.skip += 1
        if tag == "table" and "properties" in cls:
            self.in_props += 1
        if self.in_props and tag == "th":
            self.in_th, self.cur_k = True, ""
        if self.in_props and tag == "td":
            self.in_td, self.cur_v = True, ""
        if tag == "div" and "page-body" in cls:
            self.in_body = True
        if self.in_body and tag in ("h1", "h2", "h3"):
            self.in_h, self.hbuf = True, ""

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag in ("style", "script"):
            self.skip -= 1
        if self.in_props and tag == "th":
            self.in_th = False
        if self.in_props and tag == "td":
            self.in_td = False
            self.props[self.cur_k.strip()] = re.sub(r"\s+", " ", self.cur_v).strip()
        if tag == "table" and self.in_props:
            self.in_props -= 1
        if self.in_h and tag in ("h1", "h2", "h3"):
            self.in_h = False
            if self.hbuf.strip():
                self.headings.append(self.hbuf.strip()[:80])

    def handle_data(self, d):
        if self.skip:
            return
        if self.in_title:
            self.title += d
        if self.in_th:
            self.cur_k += d
        if self.in_td:
            self.cur_v += d
        if self.in_body:
            self.text.append(d)
        if self.in_h:
            self.hbuf += d


pages, dbs = [], []
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, ROOT)
        m = ID_RE.search(f)
        nid = m.group(1) if m else ""
        if f.endswith(".html"):
            pr = Page()
            try:
                pr.feed(open(p, encoding="utf-8", errors="replace").read())
            except Exception as e:
                pr.title = f"PARSE ERROR {e}"
            body = re.sub(r"\s+", " ", " ".join(pr.text)).strip()
            pages.append({
                "path": rel, "id": nid, "title": unescape(pr.title.strip()),
                "top": rel.split(os.sep)[0], "depth": rel.count(os.sep),
                "props": pr.props, "words": len(body.split()),
                "headings": pr.headings[:8], "snippet": body[:200],
            })
        elif f.endswith(".md"):
            t = open(p, encoding="utf-8", errors="replace").read()
            pages.append({"path": rel, "id": nid, "title": t.split("\n", 1)[0].lstrip("# ").strip(),
                          "top": rel.split(os.sep)[0], "depth": rel.count(os.sep), "props": {},
                          "words": len(t.split()), "headings": [], "snippet": t[:200], "md": True})
        elif f.endswith(".csv"):
            try:
                rows = list(csv.reader(open(p, encoding="utf-8-sig", errors="replace")))
            except Exception:
                rows = []
            dbs.append({"path": rel, "id": nid, "name": ID_RE.sub("", f[:-4]).replace("_all", "").strip(),
                        "all": f.endswith("_all.csv"), "headers": rows[0] if rows else [],
                        "rows": max(len(rows) - 1, 0)})

json.dump({"pages": pages, "dbs": dbs}, open(OUT, "w"), ensure_ascii=False)
print(len(pages), "pages;", len(dbs), "csv")
