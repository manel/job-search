#!/usr/bin/env python3
"""Check that relative Markdown links in the repo point at files and headings that exist.

Scans every .md file outside portfolio/ (a submodule with its own repo) and
reports each [text](target) whose file is missing, or whose #anchor matches no
heading in the target file. External links, mailto links and links inside code
are ignored. It also flags a fixed set-piece answer found outside its canonical
file, so pasted copies can't drift from the approved wording. It writes nothing.

Run: python3 scripts/check-links.py [--quiet]
Exit code 1 when something is broken.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "portfolio", "node_modules", ".obsidian"}
LINK = re.compile(r"(?<!!)\[(?:[^\]\[]|\[[^\]]*\])*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`]*`")

# Set-piece answers live in one file. A copy elsewhere drifts (2026-11-12:
# the Textream departure script still had a superseded wording).
SET_PIECES = {
    "departure answer": (
        "design input didn't always have real weight",
        "interviews/answers.md",
    ),
}
# Files allowed to hold a dated copy: briefs record what was prepared for that
# round, archives are frozen.
SET_PIECE_ALLOWED = re.compile(r"^interviews/(archive/|[^/]+/[^/]+\.md$)")


def slugify(text: str) -> str:
    """GitHub-style heading anchor."""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("`", "").lower().strip()
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def md_files() -> list[Path]:
    out = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in SKIP_DIRS:
            continue
        out.append(path)
    return sorted(out)


def anchors_of(path: Path, cache: dict[Path, set[str]]) -> set[str]:
    if path not in cache:
        seen: dict[str, int] = {}
        found = set()
        in_fence = False
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            m = HEADING.match(line)
            if not m:
                continue
            slug = slugify(m.group(2))
            n = seen.get(slug, 0)
            seen[slug] = n + 1
            found.add(slug if n == 0 else f"{slug}-{n}")
        cache[path] = found
    return cache[path]


def links_in(path: Path):
    in_fence = False
    for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for m in LINK.finditer(INLINE_CODE.sub("", line)):
            yield lineno, m.group(1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--quiet", action="store_true", help="print only the totals")
    args = parser.parse_args()

    cache: dict[Path, set[str]] = {}
    broken = []
    checked = 0
    for path in md_files():
        rel = path.relative_to(ROOT).as_posix()
        for lineno, target in links_in(path):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue
            checked += 1
            file_part, _, anchor = target.partition("#")
            dest = path if not file_part else (path.parent / unquote(file_part)).resolve()
            if not dest.exists():
                broken.append((rel, lineno, target, "missing file"))
                continue
            if anchor and dest.suffix == ".md" and slugify(unquote(anchor)) not in anchors_of(dest, cache):
                broken.append((rel, lineno, target, "missing heading"))

    drift = []
    for label, (needle, canonical) in SET_PIECES.items():
        for path in md_files():
            rel = path.relative_to(ROOT).as_posix()
            if rel == canonical or SET_PIECE_ALLOWED.match(rel):
                continue
            if needle in path.read_text(encoding="utf-8", errors="replace"):
                drift.append((rel, label, canonical))

    if not args.quiet:
        for rel, lineno, target, why in broken:
            print(f"{rel}:{lineno}  {target}  ({why})")
        for rel, label, canonical in drift:
            print(f"{rel}  copy of the {label}; link to {canonical} instead")
    print(f"{checked} links checked, {len(broken)} broken, {len(drift)} set-piece copies outside their file")
    return 1 if broken or drift else 0


if __name__ == "__main__":
    sys.exit(main())
