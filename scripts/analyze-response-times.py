#!/usr/bin/env python3
"""Response-time and ghosting analysis over submitted applications.

Reads frontmatter from applications/records/. A submission counts when
applied_on is set or the record is known to have been submitted (UNDATED).
First employer response comes from FIRST_RESPONSE when a process reached a
conversation (the invite date, sourced from each record's History), otherwise
from last_contact_on for rejections. last_contact_on equal to applied_on on a
record with no decision is the submission itself, not a response.

Run: python3 scripts/analyze-response-times.py [--as-of YYYY-MM-DD] [--csv out.csv]
"""

from __future__ import annotations

import argparse
import csv
import statistics
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# First human contact for processes that reached a conversation: (date, note).
# None means the record confirms a conversation but not the invite date.
FIRST_RESPONSE = {
    "alan-product-designer": ("2026-10-06", "invite from recruiter"),
    "kabilio-senior-ux-ui-designer": ("2026-10-01", "invite same day"),
    "datavant-senior-ux-designer-provider-experience": ("2026-09-23", "recruiter call request"),
    "enginy-product-designer": ("2026-10-21", "invite"),
    "haddock-senior-product-designer-b2b-saas": ("2026-09-29", "invite"),
    "wizeline-senior-product-designer-barcelona-hybrid": ("2026-10-20", "invite"),
    "perk-senior-design-systems-designer": ("2026-10-26", "template rejection, reversed 2026-11-02"),
    "biorce-senior-product-designer": ("2026-07-28", "screen date (invite date not recorded)"),
    "factorial-senior-staff-product-designer-it-spinoff": ("2026-06-22", "talent screen date (invite date not recorded)"),
    "spendesk-confirmed-product-designer": (None, "screen before 2026-09-08"),
    "secfix-senior-product-designer": (None, "screen 2026-09-02, applied date unknown"),
    "valeria-hr-senior-product-designer": ("2026-08-14", "initial response, applied date unknown"),
}

# Reached a human conversation (screen or later).
CONVERSATION = set(FIRST_RESPONSE) - {"perk-senior-design-systems-designer"} | {
    "perk-senior-design-systems-designer"  # TA preliminary booked 2026-11-05 after reversal
}

# Submitted, but applied_on is unknown.
UNDATED = {
    "secfix-senior-product-designer", "valeria-hr-senior-product-designer",
    "tabby-senior-product-designer-b2b-lifecycle", "murphy-ai-founding-product-designer",
    "deel-staff-product-designer", "pilar-unnamed-client-profile-review",
}

CLOSED = {"rejected", "stale", "role-closed", "withdrawn", "hired"}

# Stage at which an ended conversation was lost, from each record's History.
LOST_AT = {
    "biorce-senior-product-designer": "Recruiter screen",
    "secfix-senior-product-designer": "Recruiter screen",
    "kabilio-senior-ux-ui-designer": "First interview",
    "valeria-hr-senior-product-designer": "First interview",
    "datavant-senior-ux-designer-provider-experience": "Hiring manager",
    "spendesk-confirmed-product-designer": "Hiring manager",
    "factorial-senior-staff-product-designer-it-spinoff": "Live challenge",
    "alan-product-designer": "Live challenge",
}


def frontmatter(path: Path) -> dict[str, str]:
    meta: dict[str, str] = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines[1:]:
        if line == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.split(" #")[0].strip().strip('"')
    return meta


def day(value: str | None) -> date | None:
    try:
        return date.fromisoformat(value[:10]) if value else None
    except ValueError:
        return None


def ats(url: str) -> str:
    for key, name in (("ashby", "Ashby"), ("greenhouse", "Greenhouse"), ("gh_jid", "Greenhouse"),
                      ("lever", "Lever"), ("workable", "Workable"), ("teamtailor", "Teamtailor"),
                      ("haddock.app", "Teamtailor"), ("personio", "Personio"), ("linkedin", "LinkedIn"),
                      ("recruitee", "Recruitee"), ("tether.io", "Recruitee")):
        if key in url:
            return name
    return "other/unknown" if url else "unknown"


def channel(meta: dict[str, str]) -> str:
    raw = (meta.get("application_channel", "") + " " + meta.get("warm_path", "")).lower()
    if "referral" in raw or "warm path" in raw:
        return "referral/warm"
    if "recruiter" in raw or "agency" in raw:
        return "recruiter/agency"
    if "direct" in raw:
        return "direct"
    return "unknown"


def load(as_of: date) -> list[dict]:
    rows = []
    for path in sorted((ROOT / "applications" / "records").glob("*.md")):
        meta = frontmatter(path)
        stem = path.stem
        applied = day(meta.get("applied_on"))
        if not applied and stem not in UNDATED:
            continue
        status = meta.get("status", "")
        last = day(meta.get("last_contact_on"))
        if stem in FIRST_RESPONSE:
            first_raw, note = FIRST_RESPONSE[stem]
            first = day(first_raw)
            kind = "rejection" if "rejection" in note else "conversation"
        elif status == "rejected" and last:
            first, note, kind = last, "rejection", "rejection"
        else:
            first, note, kind = None, "", "none"
        rows.append({
            "record": stem,
            "company": meta.get("company", ""),
            "status": status,
            "stage": meta.get("outcome_stage", "") or "",
            "lane": meta.get("role_lane", "") or "unknown",
            "channel": channel(meta),
            "ats": ats(meta.get("job_url", "")),
            "applied": applied,
            "first_response": first,
            "response_kind": kind,
            "response_note": note,
            "days_to_first": (first - applied).days if first and applied else None,
            "conversation": stem in CONVERSATION,
            "last_contact": last,
            "days_open": (as_of - applied).days if applied and status not in CLOSED else None,
            "days_since_applied": (as_of - applied).days if applied else None,
            "posting": meta.get("posting_status", ""),
            "ds_titled": "design-system" in stem,
            "lost_at": LOST_AT.get(stem, ""),
        })
    return rows


def pct(n: int, d: int) -> str:
    return f"{n}/{d} ({n / d:.0%})" if d else "0/0"


def summary(values: list[int]) -> str:
    if not values:
        return "n=0"
    values = sorted(values)
    return (f"n={len(values)}, median {statistics.median(values):g} days, "
            f"range {values[0]}-{values[-1]}")


def report(rows: list[dict], as_of: date) -> None:
    dated = [r for r in rows if r["applied"]]
    print(f"As of {as_of}. Submitted: {len(rows)} ({len(dated)} with applied_on).")
    print("Status:", dict(Counter(r["status"] for r in rows)))

    kinds = Counter(r["response_kind"] for r in rows)
    closed = [r for r in rows if r["status"] in CLOSED or r["response_kind"] != "none"]
    print("\nFirst response kind:", dict(kinds))
    print("Any employer response:", pct(sum(r["response_kind"] != "none" for r in rows), len(rows)))
    print("Reached a conversation:", pct(sum(r["conversation"] for r in rows), len(rows)))

    print("\nDays to first response")
    for kind in ("conversation", "rejection"):
        print(f"  {kind}: {summary([r['days_to_first'] for r in rows if r['response_kind'] == kind and r['days_to_first'] is not None])}")
    by_ats = defaultdict(list)
    for r in rows:
        if r["response_kind"] == "rejection" and r["days_to_first"] is not None and not r["conversation"]:
            by_ats[r["ats"]].append(r["days_to_first"])
    print("  Pre-interview rejections by ATS:")
    for name, values in sorted(by_ats.items()):
        print(f"    {name}: {summary(values)}")

    print("\nSilence (no employer response at all)")
    silent = [r for r in dated if r["response_kind"] == "none"]
    for r in sorted(silent, key=lambda r: r["applied"]):
        age = (as_of - r["applied"]).days
        print(f"  {r['applied']} {age:>3}d {r['status']:<12} posting={r['posting']:<8} {r['record']}")

    def split(label: str, key: str) -> None:
        print(f"\nBy {label}: submitted / any response / conversation")
        groups = defaultdict(list)
        for r in rows:
            groups[r[key]].append(r)
        for name, items in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            resp = sum(i["response_kind"] != "none" for i in items)
            conv = sum(i["conversation"] for i in items)
            print(f"  {name:<18} {len(items):>3}  {pct(resp, len(items)):<12} {pct(conv, len(items))}")

    for r in rows:
        r["period"] = ("unknown" if not r["applied"] else
                       "May-Aug" if r["applied"] < date(2026, 9, 1) else "Sep-Nov")
    split("period", "period")
    split("lane (recorded since September)", "lane")
    split("channel", "channel")
    split("ATS", "ats")
    print("\nRejection stage:", dict(Counter((r["stage"] or "unrecorded") for r in rows if r["status"] == "rejected")))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--as-of", default=date.today().isoformat())
    parser.add_argument("--csv", type=Path)
    args = parser.parse_args()
    as_of = date.fromisoformat(args.as_of)
    rows = load(as_of)
    report(rows, as_of)
    if args.csv:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        with args.csv.open("w", newline="", encoding="utf-8") as target:
            writer = csv.DictWriter(target, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
