"""Outline an unzipped .sketch file: pages, artboards, text in reading order, prototype links.

Usage: sketch_outline.py unzipped_dir out.md [page-name-regex]
"""
import glob
import json
import os
import re
import sys

src, out_path = sys.argv[1], sys.argv[2]
page_filter = re.compile(sys.argv[3], re.I) if len(sys.argv) > 3 else None


def texts(layer, acc):
    if layer.get("isVisible") is False:
        return
    if layer.get("_class") == "text":
        s = (layer.get("attributedString") or {}).get("string", "").strip()
        if s:
            f = layer.get("frame", {})
            acc.append((round(f.get("y", 0)), round(f.get("x", 0)), re.sub(r"\s+", " ", s)))
    if layer.get("_class") == "symbolInstance":
        for o in layer.get("overrideValues", []):
            if o.get("overrideName", "").endswith("_stringValue") and isinstance(o.get("value"), str) and o["value"].strip():
                f = layer.get("frame", {})
                acc.append((round(f.get("y", 0)), round(f.get("x", 0)), re.sub(r"\s+", " ", o["value"].strip())))
    for c in layer.get("layers", []) or []:
        texts(c, acc)


def links(layer, acc):
    fl = layer.get("flow")
    if fl and fl.get("destinationArtboardID"):
        acc.add(fl["destinationArtboardID"])
    for c in layer.get("layers", []) or []:
        links(c, acc)


pages = [json.load(open(p, encoding="utf-8")) for p in glob.glob(os.path.join(src, "pages", "*.json"))]
names = {}
for p in pages:
    for a in p.get("layers", []):
        names[a.get("do_objectID")] = a.get("name")

with open(out_path, "w", encoding="utf-8") as out:
    for p in sorted(pages, key=lambda p: p.get("name", "")):
        if page_filter and not page_filter.search(p.get("name", "")):
            continue
        boards = [a for a in p.get("layers", []) if a.get("_class") in ("artboard", "symbolMaster")]
        out.write(f"# {p.get('name')} ({len(boards)} artboards)\n\n")
        for a in sorted(boards, key=lambda a: a.get("name", "")):
            f = a.get("frame", {})
            out.write(f"## {a.get('name')} [{round(f.get('width', 0))}x{round(f.get('height', 0))}]\n")
            dest = set()
            links(a, dest)
            if dest:
                out.write("Links to: " + "; ".join(sorted(str(names.get(d, d)) for d in dest)) + "\n")
            acc = []
            texts(a, acc)
            seen = set()
            for _, _, s in sorted(acc):
                if s not in seen:
                    seen.add(s)
                    out.write(f"- {s[:160]}\n")
            out.write("\n")
print("written", out_path)
