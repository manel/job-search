#!/bin/zsh
# Merge PDFs in the exact order given on the command line.
# Usage: ./scripts/merge-pdf.sh output.pdf page1.pdf page2.pdf [page3.pdf ...]
# Built 2026-07-13 after the Datavant CV went out with pages reversed:
# Finder's "Create PDF" quick action combines files in Finder sort order,
# not selection order, so a page-2 export whose filename sorts first lands first.
# This script has no such opinion. The argument order is the page order.

set -e

if [ $# -lt 3 ]; then
  echo "Usage: $0 output.pdf input1.pdf input2.pdf [...]"
  exit 1
fi

"$HOME/.venvs/pdftools/bin/python" - "$@" <<'EOF'
import sys
from pypdf import PdfWriter

out, *inputs = sys.argv[1:]
writer = PdfWriter()
for path in inputs:
    writer.append(path)
with open(out, "wb") as f:
    writer.write(f)
print(f"Wrote {out}: " + " + ".join(inputs))
EOF
