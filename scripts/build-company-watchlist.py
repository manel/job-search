#!/usr/bin/env python3
"""Build a deduplicated sourcing watchlist from spanish-top-tech-companies.

The upstream CSV has one row per salary report. This script produces one row
per company and keeps salary data explicitly labelled as an engineering-pay
signal, not a Product Design salary estimate.
"""

from __future__ import annotations

import argparse
import csv
import statistics
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote


FIELDS = [
    "company",
    "watch_status",
    "domain_fit",
    "salary_sample_size",
    "engineering_median_base_eur",
    "engineering_at_60k_count",
    "engineering_at_60k_share",
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
    parser.add_argument("--input", required=True, type=Path)
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


def first(rows: list[dict[str, str]], field: str) -> str:
    return next((row[field].strip() for row in rows if row.get(field, "").strip()), "")


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


def linkedin_jobs_url(rows: list[dict[str, str]]) -> str:
    raw_ids = first(rows, "linkedin_ids")
    if raw_ids:
        ids = ",".join(part.strip() for part in raw_ids.split("|") if part.strip())
        return (
            "https://www.linkedin.com/jobs/search/"
            f"?f_C={quote(ids)}&location=Spain"
        )
    company_url = first(rows, "linkedin_url")
    if company_url:
        return company_url.rstrip("/") + "/jobs/"
    return ""


def main() -> None:
    args = arguments()
    with args.input.open(newline="", encoding="utf-8") as source:
        source_rows = list(csv.DictReader(source))

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in source_rows:
        if row.get("company", "").strip():
            grouped[row["company"].strip()].append(row)

    overrides = load_overrides(args.overrides)
    history = application_history(args.records_dir)
    output_rows: list[dict[str, object]] = []

    for company, rows in grouped.items():
        bases = [round(float(row["base"])) for row in rows if row.get("base", "").strip()]
        reports = sorted({row["reported"].strip() for row in rows if row.get("reported", "").strip()})
        cities = sorted({row["city"].strip() for row in rows if row.get("city", "").strip()})
        at_60k = sum(base >= 60_000 for base in bases)
        override = overrides.get(company, {})
        app_history = history.get(company, {"count": 0, "statuses": set()})
        statuses = app_history["statuses"]
        assert isinstance(statuses, set)

        output_rows.append(
            {
                "company": company,
                "watch_status": override.get("watch_status", "review"),
                "domain_fit": override.get("domain_fit", "unreviewed"),
                "salary_sample_size": len(bases),
                "engineering_median_base_eur": round(statistics.median(bases)),
                "engineering_at_60k_count": at_60k,
                "engineering_at_60k_share": f"{at_60k / len(bases):.0%}",
                "latest_salary_report": reports[-1] if reports else "",
                "reported_cities": " | ".join(cities),
                "linkedin_company_url": first(rows, "linkedin_url"),
                "linkedin_spain_jobs_url": linkedin_jobs_url(rows),
                "website": override.get("website") or first(rows, "website"),
                "careers_url": override.get("careers_url") or first(rows, "careers_url"),
                "career_platform": override.get("career_platform", "unknown"),
                "prior_application_records": app_history["count"],
                "prior_application_statuses": " | ".join(sorted(statuses)),
                "last_careers_check": override.get("last_careers_check", ""),
                "last_linkedin_check": override.get("last_linkedin_check", ""),
                "notes": override.get("notes", ""),
                "source_url": args.source_url,
                "source_snapshot_date": first(rows, "date"),
            }
        )

    output_rows.sort(key=lambda row: str(row["company"]).casefold())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(target, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {len(output_rows)} companies to {args.output}")


if __name__ == "__main__":
    main()
