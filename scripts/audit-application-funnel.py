#!/usr/bin/env python3
"""Read canonical records; print a cycle-level audit. No files are modified.

Manual stage annotations below are sourced from the bodies of the named records.
They are deliberately explicit: absence of an interview field is not rejection
before interview. Datavant's two dated submissions are separate cycles.
Run: python3 scripts/audit-application-funnel.py > analysis/<date>/funnel.json
"""
import hashlib
import json
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AS_OF = date(2026, 9, 23)
CONVERSATIONS = {
    "biorce-senior-product-designer": "recruiter-screen",
    "secfix-senior-product-designer": "recruiter-screen",
    "factorial-senior-staff-product-designer-it-spinoff": "live-challenge",
    "spendesk-confirmed-product-designer": "design-interview",
    "valeria-hr-senior-product-designer": "first-interview",
}
PRE_INTERVIEW = {
    "3commas-senior-product-designer-quantpilot",
    "bitpanda-senior-design-system-designer-july-reapplication",
    "bitpanda-senior-design-system-designer-june",
    "bitpanda-senior-product-designer-advanced-trading",
    "cloudpay-product-designer-uiux", "deel-staff-product-designer",
    "factorial-senior-product-designer-platform-domain",
    "hostaway-staff-product-designer-design-systems",
    "olx-otodom-senior-design-system-designer",
    "perk-staff-product-designer-events",
    "qonto-senior-product-designer-ai-lab",
    "wayflyer-senior-staff-product-designer",
}
SPECIFIC = {"biorce-senior-product-designer",
            "factorial-senior-staff-product-designer-it-spinoff"}

cycles, excluded, recruiter_reviews = [], [], []
for path in sorted((ROOT / "applications/records").glob("*.md")):
    raw = path.read_text()
    front = raw.split("---", 2)[1]
    fields = dict(line.split(":", 1) for line in front.strip().splitlines() if ":" in line)
    fields = {key: value.strip().strip('"') for key, value in fields.items()}
    status = fields["status"]
    if fields.get("submission_kind") == "recruiter-profile-review":
        recruiter_reviews.append({"source": str(path.relative_to(ROOT)),
                                 "company": fields["company"], "status": status,
                                 "stage": fields.get("outcome_stage"),
                                 "last_contact_on": fields.get("last_contact_on"),
                                 "source_sha256": hashlib.sha256(raw.encode()).hexdigest()})
        continue
    submitted = status in {"applied", "interviewing", "rejected", "offer", "hired"} or bool(fields.get("applied_on"))
    if not submitted:
        excluded.append({"record": path.name, "status": status})
        continue
    stem = path.stem
    human = stem in CONVERSATIONS
    if human:
        stage = CONVERSATIONS[stem]
    elif stem in PRE_INTERVIEW:
        stage = "cv-review"
    elif status == "rejected":
        stage = "unknown"
    else:
        stage = fields.get("outcome_stage") or "no-response"
    feedback = "none"
    if status == "rejected":
        feedback = "specific" if stem in SPECIFIC else "hiring-process-context" if stem == "valeria-hr-senior-product-designer" else "vague-context" if stem == "secfix-senior-product-designer" else "generic"
    row = {
        "cycle": stem,
        "company": fields["company"], "role": fields["role"],
        "status": status, "applied_on": fields.get("applied_on") or None,
        "last_status_verified_on": fields.get("status_verified_on"),
        "known_human_conversation": human, "furthest_known_stage": stage,
        "feedback_class_audit": feedback,
        "explicit_design_system_title": "design system" in fields["role"].lower(),
        "application_channel_recorded": fields.get("application_channel") or "unknown",
        "portfolio_version_recorded": fields.get("portfolio_version") or "unknown",
        "source": str(path.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(raw.encode()).hexdigest(),
    }
    cycles.append(row)
    if stem == "datavant-senior-ux-designer-provider-experience":
        assert "2026-07-13: Application submitted" in raw
        assert row["applied_on"] == "2026-09-22"
        cycles.append(dict(row, cycle=stem + "--2026-07", status="role-closed",
                           applied_on="2026-07-13", portfolio_version_recorded="unknown",
                           application_channel_recorded="unknown"))

def cohort(rows):
    return {"n": len(rows), "known_conversations": sum(r["known_human_conversation"] for r in rows),
            "statuses": dict(Counter(r["status"] for r in rows))}

result = {
    "as_of": AS_OF.isoformat(),
    "unit": "confirmed submitted application cycle; not assessed role or company",
    "n_cycles": len(cycles), "n_companies": len({r["company"] for r in cycles}),
    "n_known_conversations": sum(r["known_human_conversation"] for r in cycles),
    "status_counts": dict(Counter(r["status"] for r in cycles)),
    "rejected_stage_counts": dict(Counter(r["furthest_known_stage"] for r in cycles if r["status"] == "rejected")),
    "feedback_counts": dict(Counter(r["feedback_class_audit"] for r in cycles if r["status"] == "rejected")),
    "application_month_counts": dict(Counter((r["applied_on"] or "unknown")[:7] for r in cycles)),
    "cohorts": {
        "before_2026-07-28": cohort([r for r in cycles if r["applied_on"] and r["applied_on"] < "2026-07-28"]),
        "on_or_after_2026-07-28": cohort([r for r in cycles if r["applied_on"] and r["applied_on"] >= "2026-07-28"]),
        "date_unknown": cohort([r for r in cycles if not r["applied_on"]]),
        "explicit_design_system_title": cohort([r for r in cycles if r["explicit_design_system_title"]]),
    },
    "cycles": cycles, "excluded_unsubmitted_records": excluded,
    "separate_recruiter_profile_reviews": recruiter_reviews,
    "inclusive_submissions": len(cycles) + len(recruiter_reviews),
    "limitations": ["Statuses are latest recorded, not newly verified with employers.",
                    "Dates are not proof of the exact portfolio version reviewed.",
                    "Murphy AI interview stage is unknown.",
                    "Manual stage annotations require review when records change.",
                    "Saved PDF existence alone does not establish submission."],
}
assert sum(result["status_counts"].values()) == len(cycles)
assert len({r["cycle"] for r in cycles}) == len(cycles)
print(json.dumps(result, indent=2))
