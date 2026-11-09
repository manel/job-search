"""Print compact plain text of Notion HTML pages. Args: root, then title regexes (or --path p)."""
import json, re, sys, os
from html.parser import HTMLParser

ROOT = sys.argv[1]
CAP = int(os.environ.get("CAP", "4000"))
P = json.load(open(os.environ.get("INV", "pages_dedup.json")))


class T(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out, self.skip, self.body = [], 0, False

    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag in ("style", "script"):
            self.skip += 1
        if tag == "div" and "page-body" in (a.get("class") or ""):
            self.body = True
        if tag == "table" and "properties" in (a.get("class") or ""):
            self.out.append("\n[props] ")
        if tag in ("h1", "h2", "h3"):
            self.out.append("\n## ")
        elif tag in ("li", "p", "tr", "summary", "blockquote", "figure"):
            self.out.append("\n- " if tag == "li" else "\n")
        elif tag in ("td", "th"):
            self.out.append(" | ")
        if tag == "a" and a.get("href", "").startswith("http"):
            self.href = a["href"]
        if tag == "img":
            self.out.append("[img]")

    def handle_endtag(self, tag):
        if tag in ("style", "script"):
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip:
            self.out.append(d)


def text(path):
    t = T()
    t.feed(open(os.path.join(ROOT, path), encoding="utf-8", errors="replace").read())
    s = "".join(t.out)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


args = sys.argv[2:]
if args and args[0] == "--path":
    sel = [p for p in P if p["path"] in args[1:]]
else:
    sel = [p for p in P if any(re.search(a, p["title"]) for a in args) and not p.get("md")]
for p in sel:
    s = text(p["path"])
    print(f"\n=================== {p['title']}  [{p['words']}w] {p['path'][:120]}")
    print(s[:CAP] + ("\n…[truncated]" if len(s) > CAP else ""))
