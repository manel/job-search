#!/usr/bin/env python3
"""Check that a CV or cover-letter PDF extracts as clean text, the way an ATS reads it.

Figma exports can draw text that looks right on screen but extracts broken:
"wit h", "t he", "mont hly" (seen in October 2026 exports). An ATS or a recruiter
pasting the PDF sees the broken text, and keyword searches miss split words.

For each PDF it reports:
- no extractable text (text exported as outlines, or an image-only PDF)
- split words: two fragments that join into a known word
- missing contact details (email, portfolio domain)
- with --source: words from the plain-text source that never appear in the PDF

Run it before sending, never to re-check or regenerate PDFs that were already sent.
It writes nothing. Exit code 1 when any PDF has issues.

Run: python3 scripts/check-pdf-text.py "cv-pdf-to-send/Perk (DS)"
     python3 scripts/check-pdf-text.py path/to/CV.pdf --source cv/roles/perk-ds.md
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

EMAIL = "maneleiva@gmail.com"
DOMAIN = "manel-leiva.com"
DICT = Path("/usr/share/dict/words")
WORD = re.compile(r"[A-Za-z]+")
SPACED = re.compile(r"^\s*(?:[A-Za-z] ){3,}[A-Za-z]\s*$")
# Short joins ("tot", "han") are dictionary noise; accept them only if common or seen whole.
COMMON = {"the", "that", "this", "with", "then", "than", "them", "they", "both", "into", "from", "what", "when", "each", "only"}

# macOS fallback when pypdf is not installed: a tiny PDFKit extractor, compiled once.
SWIFT_SRC = """import PDFKit
guard let d = PDFDocument(url: URL(fileURLWithPath: CommandLine.arguments[1])) else { exit(2) }
print(d.string ?? "")
"""


def pdfkit_binary() -> Path:
    cache = Path(tempfile.gettempdir()) / "check-pdf-text"
    binary = cache / "pdfkit-extract"
    if not binary.exists():
        cache.mkdir(exist_ok=True)
        src = cache / "extract.swift"
        src.write_text(SWIFT_SRC, encoding="utf-8")
        subprocess.run(["swiftc", "-O", str(src), "-o", str(binary)], check=True, capture_output=True)
    return binary


def extract(pdf: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        result = subprocess.run([str(pdfkit_binary()), str(pdf)], capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"could not open {pdf}")
        return result.stdout
    return "\n".join(page.extract_text() or "" for page in PdfReader(pdf).pages)


def load_vocabulary() -> set[str]:
    return {w.lower() for w in DICT.read_text().split()} if DICT.exists() else set()


def is_word(fragment: str, vocab: set[str]) -> bool:
    if len(fragment) == 1:
        return fragment in {"a", "i"}
    return fragment in vocab


def split_words(text: str, vocab: set[str], seen: set[str]) -> list[str]:
    """Adjacent fragments on one line that join into a word, where one fragment is not a word."""
    def candidate(tokens: list[str], i: int) -> bool:
        if i + 2 >= len(tokens) or tokens[i + 1] != " ":
            return False
        left, right = tokens[i], tokens[i + 2]
        if not WORD.fullmatch(left) or not WORD.fullmatch(right):
            return False
        # "a B2B": the right fragment continues into digits, so it is a real token.
        after = tokens[i + 3] if i + 3 < len(tokens) else ""
        if after[:1].isdigit():
            return False
        l, r = left.lower(), right.lower()
        joined = l + r
        if len(joined) <= 4 and joined not in COMMON and joined not in seen:
            return False
        return joined in vocab and not (is_word(l, vocab) and is_word(r, vocab))

    found = []
    for line in text.splitlines():
        if SPACED.match(line):
            continue
        tokens = re.findall(r"[A-Za-z]+|[^A-Za-z]+", line)
        for i in range(len(tokens)):
            # "to t he": the fragment "t" belongs to the next split, so skip this pair.
            if candidate(tokens, i) and not candidate(tokens, i + 2):
                found.append(f"{tokens[i]} {tokens[i + 2]}")
    return found


def missing_from_source(source: str, extracted: str) -> list[str]:
    in_pdf = {w.lower() for w in WORD.findall(extracted)}
    # Drop Markdown link targets so URLs don't count as prose.
    # Compare only the CV or letter body: source files keep notes above a "---" line.
    head, sep, body = source.partition("\n---\n")
    prose = re.sub(r"\]\([^)]*\)", "]", body if sep else source)
    missing = {w for w in WORD.findall(prose) if len(w) >= 4 and w.lower() not in in_pdf}
    return sorted(missing, key=str.lower)


def check(pdf: Path, source_text: str | None) -> list[str]:
    text = extract(pdf)
    if len(WORD.findall(text)) < 20:
        return ["no extractable text: the PDF may contain outlined text or images only"]

    issues = []
    # Words that appear whole in the PDF or the source also count as known.
    # Fragments like "han" (from "t han") are short, so PDF words count only from five letters.
    seen = {w.lower() for w in WORD.findall(source_text or "") if len(w) > 2}
    seen |= {w.lower() for w in WORD.findall(text) if len(w) >= 5}
    vocab = load_vocabulary() | seen
    spaced = [line.strip() for line in text.splitlines() if SPACED.match(line)]
    if spaced:
        issues.append(f"letter-spaced text extracts as single letters (parsers miss these headings): {', '.join(spaced)}")
    splits = split_words(text, vocab, seen)
    if splits:
        counts: dict[str, int] = {}
        for s in splits:
            counts[s] = counts.get(s, 0) + 1
        listed = ", ".join(f'"{s}"' + (f" x{n}" if n > 1 else "") for s, n in sorted(counts.items(), key=lambda kv: -kv[1]))
        issues.append(f"{len(splits)} split words: {listed}")

    compact = re.sub(r"\s+", "", text)
    for needle in (EMAIL, DOMAIN):
        if needle not in compact:
            issues.append(f"contact detail not found intact: {needle}")
        elif needle not in text:
            issues.append(f"contact detail broken by spaces or line breaks: {needle}")

    if source_text is not None:
        missing = missing_from_source(source_text, text)
        if missing:
            issues.append(f"{len(missing)} source words missing from the PDF: {', '.join(missing[:30])}")
    return issues


def collect(paths: list[str]) -> list[Path]:
    pdfs: list[Path] = []
    for p in map(Path, paths):
        pdfs.extend(sorted(p.glob("*.pdf")) if p.is_dir() else [p])
    return pdfs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("paths", nargs="+", help="PDF files or folders of PDFs")
    parser.add_argument("--source", help="plain-text source (cv/roles/... or cover-letters/roles/...) to compare against")
    args = parser.parse_args()

    source_text = Path(args.source).read_text(encoding="utf-8") if args.source else None
    failed = 0
    for pdf in collect(args.paths):
        try:
            issues = check(pdf, source_text)
        except (RuntimeError, OSError, subprocess.CalledProcessError) as exc:
            issues = [f"error: {exc}"]
        print(f"{'FAIL' if issues else 'OK  '}  {pdf}")
        for issue in issues:
            print(f"      - {issue}")
        failed += bool(issues)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
