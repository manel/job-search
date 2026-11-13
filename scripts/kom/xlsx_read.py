"""Read an .xlsx without openpyxl. Prints sheet names, row counts and the first rows.

Usage: xlsx_read.py file.xlsx [rows_to_show]
"""
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
RID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"


def col_index(ref):
    letters = re.match(r"[A-Z]+", ref).group(0)
    n = 0
    for ch in letters:
        n = n * 26 + ord(ch) - 64
    return n - 1


def read(path):
    z = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            shared.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    target = {r.get("Id"): r.get("Target") for r in rels}
    sheets = {}
    for s in wb.find("m:sheets", NS):
        t = target[s.get(RID)].lstrip("/")
        t = t if t.startswith("xl/") else "xl/" + t
        rows = []
        for row in ET.fromstring(z.read(t)).iter("{%s}row" % NS["m"]):
            vals = {}
            for c in row.findall("m:c", NS):
                v = c.find("m:v", NS)
                txt = v.text if v is not None else "".join(x.text or "" for x in c.iter("{%s}t" % NS["m"]))
                if c.get("t") == "s" and txt:
                    txt = shared[int(txt)]
                vals[col_index(c.get("r"))] = txt
            if vals:
                rows.append([vals.get(i, "") for i in range(max(vals) + 1)])
        sheets[s.get("name")] = rows
    return sheets


if __name__ == "__main__":
    show = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    for name, rows in read(sys.argv[1]).items():
        print(f"== sheet {name!r}: {len(rows)} rows")
        for r in rows[:show]:
            print(" | ".join(str(x)[:40] for x in r))
