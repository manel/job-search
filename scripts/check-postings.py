#!/usr/bin/env python3
"""Check whether the job postings of open application records are still live.

Reads job_url from every record in applications/records/ whose status is still
open, runs the career-ops liveness checker on them (job board API first, headless
browser when inconclusive) and prints a verdict per record. It writes nothing:
update a record's posting_status and posting_checked_on yourself, after reading
the verdict.

Run: python3 scripts/check-postings.py [--all]
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAREER_OPS = Path(os.environ.get("CAREER_OPS_DIR", Path.home() / "Dev" / "career-ops"))
OPEN_STATUSES = {"prospect", "assessing", "deferred", "in-progress", "applied", "interviewing", "offer"}


def frontmatter(path: Path) -> dict[str, str]:
    meta: dict[str, str] = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines[1:]:
        if line == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"')
    return meta


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--all", action="store_true", help="include closed records too")
    args = parser.parse_args()
    if not (CAREER_OPS / "check-liveness.mjs").exists():
        sys.exit(f"career-ops not found at {CAREER_OPS}; set CAREER_OPS_DIR")

    targets: dict[str, tuple[str, dict[str, str]]] = {}
    for path in sorted((ROOT / "applications" / "records").glob("*.md")):
        meta = frontmatter(path)
        if (args.all or meta.get("status") in OPEN_STATUSES) and meta.get("job_url", "").startswith("http"):
            targets[meta["job_url"]] = (path.stem, meta)
    if not targets:
        print("No open records with a job_url.")
        return
    print(f"Checking {len(targets)} postings...\n", file=sys.stderr)

    result = subprocess.run(
        ["node", "check-liveness.mjs", "--no-record", *targets],
        cwd=CAREER_OPS, capture_output=True, text=True,
        env={**os.environ, "CAREER_OPS_ROOT": str(ROOT / "sourcing" / "scan")},
    )
    verdicts: dict[str, str] = {}
    for line in result.stdout.splitlines():
        match = re.search(r"(active|expired|uncertain)\s+(?:\([^)]*\)\s+)?(https?://\S+)", line)
        if match:
            verdicts[match.group(2)] = line.strip()

    for url, (stem, meta) in targets.items():
        verdict = verdicts.get(url, "no verdict (see checker output)")
        recorded = meta.get("posting_status") or "unknown"
        checked = meta.get("posting_checked_on") or "never"
        print(f"{stem} [{meta.get('status')}]")
        print(f"  recorded: posting_status {recorded}, checked {checked}")
        print(f"  now:      {verdict}")
    summary = [line for line in result.stdout.splitlines() if line.startswith("Results:")]
    if summary:
        print("\n" + summary[-1])
    if len(verdicts) < len(targets):
        print("\nChecker output:\n" + result.stdout[-3000:] + result.stderr[-1000:])


if __name__ == "__main__":
    main()
