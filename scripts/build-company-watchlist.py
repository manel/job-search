#!/usr/bin/env python3
"""Build a deduplicated sourcing watchlist from spanish-top-tech-companies.

Since 2026-11 the upstream publishes JSON instead of a per-report CSV. The
input is its `data/` directory: `data.json` (companies and per-company salary
cells), `boards.json` (ATS job boards keyed by Levels.fyi slug). Engineering pay
stays a company-level signal; the designer columns are Product Designer
salaries at that company, usually too few to be a band.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


FIELDS = [
    "company",
    "watch_status",
    "domain_fit",
    "salary_sample_size",
    "engineering_median_base_eur",
    "engineering_at_60k_count",
    "engineering_at_60k_share",
    "designer_sample_size",
    "designer_median_base_eur",
    "latest_salary_report",
    "reported_cities",
    "linkedin_company_url",
    "linkedin_spain_jobs_url",
    "website",
    "careers_url",
    "career_platform",
    "prior_application_records",
    "prior_application_statuses",
    "last_careers_check",
    "last_linkedin_check",
    "notes",
    "source_url",
    "source_snapshot_date",
]


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Upstream data/ directory holding data.json and boards.json.",
    )
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--overrides",
        type=Path,
        help="Optional hand-maintained enrichment keyed by company.",
    )
    parser.add_argument(
        "--records-dir",
        type=Path,
        default=Path("applications/records"),
    )
    parser.add_argument(
        "--source-url",
        default="https://github.com/pugarte7/spanish-top-tech-companies",
    )
    return parser.parse_args()


BOARD_URLS = {
    "greenhouse": "https://job-boards.greenhouse.io/{board}",
    "ashby": "https://jobs.ashbyhq.com/{board}",
    "lever": "https://jobs.lever.co/{board}",
    "smartrecruiters": "https://careers.smartrecruiters.com/{board}",
    "workable": "https://apply.workable.com/{board}",
    "recruitee": "https://{board}.recruitee.com",
}


def board_url(entry: dict[str, str] | None) -> tuple[str, str]:
    if not entry:
        return "", ""
    ats, board = entry["ats"], entry["board"]
    if ats == "workday":
        tenant, instance, site = board.split("/", 2)
        return f"https://{tenant}.{instance}.myworkdayjobs.com/{site}", ats
    if ats == "lever" and entry.get("region") == "eu":
        return f"https://jobs.eu.lever.co/{board}", ats
    template = BOARD_URLS.get(ats)
    return (template.format(board=board), ats) if template else ("", ats)


def company_cell(data: dict, key: str) -> dict[int, dict]:
    return {cell["c"]: cell for cell in data["company_cells"].get(key, [])}


def load_overrides(path: Path | None) -> dict[str, dict[str, str]]:
    if not path or not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as source:
        return {row["company"]: row for row in csv.DictReader(source)}


def application_history(records_dir: Path) -> dict[str, dict[str, object]]:
    history: dict[str, dict[str, object]] = defaultdict(
        lambda: {"count": 0, "statuses": set()}
    )
    if not records_dir.exists():
        return history
    for path in records_dir.glob("*.md"):
        values: dict[str, str] = {}
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0] != "---":
            continue
        for line in lines[1:]:
            if line == "---":
                break
            if ":" in line:
                key, value = line.split(":", 1)
                values[key.strip()] = value.strip().strip('"')
        company = values.get("company", "")
        if not company:
            continue
        history[company]["count"] = int(history[company]["count"]) + 1
        if values.get("status"):
            statuses = history[company]["statuses"]
            assert isinstance(statuses, set)
            statuses.add(values["status"])
    return history


def main() -> None:
    args = arguments()
    data = json.loads((args.input / "data.json").read_text(encoding="utf-8"))
    boards = json.loads((args.input / "boards.json").read_text(encoding="utf-8"))
    engineering = company_cell(data, "software-engineer||")
    designers = company_cell(data, "product-designer||")

    overrides = load_overrides(args.overrides)
    history = application_history(args.records_dir)
    output_rows: list[dict[str, object]] = []

    for index, entry in enumerate(data["companies"]):
        company = entry["name"].strip()
        override = overrides.get(company, {})
        app_history = history.get(company, {"count": 0, "statuses": set()})
        statuses = app_history["statuses"]
        assert isinstance(statuses, set)
        eng = engineering.get(index, {})
        design = designers.get(index, {})
        at_60k = round(eng["n"] * eng["share"]) if eng.get("share") is not None else ""
        board, platform = board_url(boards.get(entry.get("levels", "")))
        linkedin = entry.get("linkedin", "")

        output_rows.append(
            {
                "company": company,
                "watch_status": override.get("watch_status", "review"),
                "domain_fit": override.get("domain_fit", "unreviewed"),
                "salary_sample_size": eng.get("n", ""),
                "engineering_median_base_eur": eng.get("median", ""),
                "engineering_at_60k_count": at_60k,
                "engineering_at_60k_share": f"{eng['share']:.0%}" if eng.get("share") is not None else "",
                "designer_sample_size": design.get("n", ""),
                "designer_median_base_eur": design.get("median", ""),
                "latest_salary_report": "",
                "reported_cities": " | ".join(sorted(entry.get("cities", []))),
                "linkedin_company_url": linkedin,
                "linkedin_spain_jobs_url": linkedin.rstrip("/") + "/jobs/" if linkedin else "",
                "website": override.get("website") or entry.get("web", ""),
                "careers_url": override.get("careers_url") or board,
                "career_platform": override.get("career_platform") or platform or "unknown",
                "prior_application_records": app_history["count"],
                "prior_application_statuses": " | ".join(sorted(statuses)),
                "last_careers_check": override.get("last_careers_check", ""),
                "last_linkedin_check": override.get("last_linkedin_check", ""),
                "notes": override.get("notes", ""),
                "source_url": args.source_url,
                "source_snapshot_date": data.get("data_as_of", ""),
            }
        )

    # Companies dropped upstream stay only if they carry hand enrichment or history.
    listed = {str(row["company"]) for row in output_rows}
    if args.output.exists():
        with args.output.open(newline="", encoding="utf-8") as previous:
            for row in csv.DictReader(previous):
                name = row["company"]
                if name in listed or not (name in overrides or name in history):
                    continue
                row.update({field: "" for field in FIELDS if field not in row})
                row["notes"] = (row["notes"] + "; " if row["notes"] else "") + (
                    f"Not in upstream as of {data.get('data_as_of', '')}"
                )
                output_rows.append(row)

    output_rows.sort(key=lambda row: str(row["company"]).casefold())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(target, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {len(output_rows)} companies to {args.output}")


if __name__ == "__main__":
    main()
