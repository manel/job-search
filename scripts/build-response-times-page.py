#!/usr/bin/env python3
"""Build the standalone response-times page from the analysis CSV.

Reads analysis/<date>/response-times.csv (from analyze-response-times.py) and
the page template scripts/templates/response-times.html, embeds the rows, and
writes analysis/<date>/response-times.html. Open it in a browser; d3 loads
from cdnjs. Colors and type follow context/brand.md.

Run: python3 scripts/build-response-times-page.py analysis/2026-11-03
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "scripts" / "templates" / "response-times.html"


def main() -> None:
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else sys.exit(__doc__)
    with (folder / "response-times.csv").open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    data = json.dumps(rows, ensure_ascii=False).replace("</", "<\\/")
    page = TEMPLATE.read_text(encoding="utf-8").replace("/*__ROWS__*/[]", data)
    out = folder / "response-times.html"
    out.write_text(page, encoding="utf-8")
    print(f"Wrote {out} ({len(rows)} applications)")


if __name__ == "__main__":
    main()
