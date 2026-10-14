#!/usr/bin/env python3
"""Scan company job boards for matching roles and add new ones to sourcing/role-leads.csv.

Uses the career-ops scanner (a separate checkout, default ~/Dev/career-ops) as an
engine only. Everything it reads and writes lives in sourcing/scan/ in this repo:
the generated company config, the filters and the dedup history. career-ops's own
CV, profile, tracker and history are never read or written.

Companies scanned: sourcing/company-watchlist.csv rows with watch_status watch or
review, plus sourcing/remote-companies.csv rows not paused, in both cases only when
careers_url points to a job board the scanner supports (Greenhouse, Ashby, Lever,
Teamtailor, Personio, Workable, SmartRecruiters, Recruitee and others).

Run: python3 scripts/scan-roles.py [--dry-run] [--since DAYS]
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCING = ROOT / "sourcing"
SCAN = SOURCING / "scan"
CAREER_OPS = Path(os.environ.get("CAREER_OPS_DIR", Path.home() / "Dev" / "career-ops"))
OPEN_STATUSES = {"prospect", "assessing", "deferred", "in-progress", "applied", "interviewing", "offer"}


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--dry-run", action="store_true", help="show what would be found; write nothing")
    parser.add_argument("--since", type=int, help="only postings published in the last N days")
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


def build_portals() -> int:
    companies = []
    for row in read_csv(SOURCING / "company-watchlist.csv"):
        if row["watch_status"] in ("watch", "review") and row["careers_url"].startswith("http"):
            companies.append({"name": row["company"], "careers_url": row["careers_url"], "enabled": True})
    for row in read_csv(SOURCING / "remote-companies.csv"):
        if row["watch_status"] != "paused" and row["careers_url"].startswith("http"):
            entry = {"name": row["company"], "careers_url": row["careers_url"], "enabled": True}
            if row.get("api"):
                entry["api"] = row["api"]
            companies.append(entry)
    config = json.loads((SCAN / "filters.json").read_text(encoding="utf-8"))
    config["tracked_companies"] = companies
    # JSON is valid YAML, which is what the scanner expects.
    (SCAN / "portals.yml").write_text(json.dumps(config, indent=1) + "\n", encoding="utf-8")
    return len(companies)


def known_urls() -> tuple[set[str], dict[str, list[str]]]:
    urls = {row["official_url"].strip() for row in read_csv(SOURCING / "role-leads.csv")}
    by_company: dict[str, list[str]] = {}
    for path in (ROOT / "applications" / "records").glob("*.md"):
        meta: dict[str, str] = {}
        lines = path.read_text(encoding="utf-8").splitlines()
        for line in lines[1:]:
            if line == "---":
                break
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip().strip('"')
        if meta.get("job_url"):
            urls.add(meta["job_url"])
        company = meta.get("company", "").split(" — ")[0].casefold()
        by_company.setdefault(company, []).append(f"{path.stem} ({meta.get('status', '?')})")
    return urls, by_company


def scan_history() -> dict[str, dict[str, str]]:
    path = SCAN / "data" / "scan-history.tsv"
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as source:
        return {row["url"]: row for row in csv.DictReader(source, delimiter="\t")}


def main() -> None:
    args = arguments()
    if not (CAREER_OPS / "scan.mjs").exists():
        sys.exit(f"career-ops not found at {CAREER_OPS}; set CAREER_OPS_DIR")
    count = build_portals()
    print(f"Scanning {count} companies with a careers_url...", file=sys.stderr)

    command = ["node", str(CAREER_OPS / "scan.mjs"), "--json", "--quiet"]
    if args.dry_run:
        command.append("--dry-run")
    if args.since:
        command += ["--since", str(args.since)]
    env = {**os.environ, "CAREER_OPS_ROOT": str(SCAN)}
    result = subprocess.run(command, cwd=CAREER_OPS, env=env, capture_output=True, text=True)
    lines = [line for line in result.stdout.splitlines() if line.startswith("{")]
    if not lines:
        sys.exit(f"Scanner produced no result.\n{result.stderr[-2000:]}")
    receipt = json.loads(lines[-1])

    print(
        f"Scanned {receipt['scanned']} boards, skipped {receipt['skipped']} with no supported job board; "
        f"{receipt['found']} postings, {receipt['added']} matching new.",
    )
    for error in receipt.get("errors", []):
        print(f"  error: {error}")

    known, by_company = known_urls()
    history = scan_history()
    new_rows = []
    for url in receipt.get("added_urls", []):
        if url in known:
            continue
        info = history.get(url, {})
        company = info.get("company", "")
        prior = by_company.get(company.casefold(), [])
        note = "Found by scripts/scan-roles.py from the job board API."
        if prior:
            note += " Earlier records at this company: " + "; ".join(prior) + "."
        new_rows.append({
            "company": company,
            "role": info.get("title", ""),
            "role_lane": "",
            "location": info.get("location", ""),
            "work_mode": "unspecified",
            "official_url": url,
            "linkedin_url": "",
            "discovered_on": date.today().isoformat(),
            "last_verified_on": date.today().isoformat(),
            "posting_status": "open",
            "initial_fit": "not assessed",
            "next_action": "Run /assess-fit",
            "source_notes": note,
        })

    if args.dry_run:
        print("\nDry run: nothing written. Matching postings not already in role-leads or records:")
        for url in receipt.get("added_urls", []):
            if url not in known:
                print(f"  {url}")
        return

    if new_rows:
        leads = SOURCING / "role-leads.csv"
        with leads.open(newline="", encoding="utf-8") as source:
            fields = next(csv.reader(source))
        with leads.open("a", newline="", encoding="utf-8") as target:
            csv.DictWriter(target, fieldnames=fields, lineterminator="\n").writerows(new_rows)
    print(f"\nAdded {len(new_rows)} new leads to sourcing/role-leads.csv:")
    for row in new_rows:
        print(f"  {row['company']} | {row['role']} | {row['location']}")
        if "Earlier records" in row["source_notes"]:
            print(f"    {row['source_notes'].split('Earlier records at this company: ')[1]}")


if __name__ == "__main__":
    main()
