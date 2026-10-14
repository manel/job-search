# Application records

Create one file per company and role in `records/`, named `company-role.md`.

Use [the dashboard](active.md) to review the action queue. Keep its sections distinct:

- **Ready to apply:** Proceed with CV/cover-letter sources prepared; export, PDF QA and vacancy checks may remain.
- **Prepare application:** Proceed, with drafting still needed and no recorded prerequisite blocking it.
- **Needs clarification or evidence:** a prerequisite, portfolio gap or user decision remains unresolved. Retain the actual Proceed/Defer/Skip assessment in the summary.
- **Confirmed active:** submission or an ongoing employer process is confirmed.
- **Skipped:** the recorded decision is not to pursue; historical prepared materials do not make it active.
- **Rejected / closed vacancies / unverified provenance:** retain these separately from candidate fit decisions.

Dashboard placement is an action grouping, not a new application status or fit decision. Use the individual record as the source of truth; include the next action and preserve uncertainty. Date vacancy checks so an old assessment is not mistaken for a live opening.

Use this frontmatter:

```yaml
company:
role:
status: prospect
status_verified_on:
status_confidence: unknown # confirmed | inferred | unknown
posting_status: unknown # open | closed | unknown
posting_checked_on:
fit_decision:
role_lane: # product | ai-product | design-systems | mixed
application_channel: # direct | referral | recruiter | internal-contact | unknown
warm_path: # name and relationship, none, or unknown
portfolio_version: # date or commit shown to the employer, if known
applied_on:
last_contact_on:
outcome_stage: # not-submitted | no-response | cv-review | recruiter-screen | design-interview | live-challenge | offer
rejection_reason_class: # none | generic | specific | unknown
next_action:
next_action_on:
salary_stated:
job_url:
source:
```

Then record: fit assessment, contacts and outreach, materials sent, interview notes, decisions, and dated status changes. Update `active.md` only after updating the individual record.

## Status vocabulary

- `prospect`: identified but not assessed
- `assessing`: fit assessment in progress
- `deferred`: fit is plausible; waiting for a stated condition
- `skipped`: assessed and intentionally not pursued
- `in-progress`: application materials are being prepared; not confirmed sent
- `applied`: submission confirmed; no response yet
- `interviewing`: at least one interview scheduled or completed; no final outcome
- `offer`: offer received
- `hired`: offer accepted
- `rejected`: employer closed the process
- `stale`: no response beyond the agreed follow-up window; removed from the active pipeline but not treated as an employer rejection or a closed vacancy
- `withdrawn`: Manel ended the process
- `role-closed`: posting closed or was removed before a decision

## Event log

Do not overwrite history. Append dated events:

```markdown
## History

- 2026-09-14: Status confirmed by Manel. Source: direct confirmation.
```

If materials exist but submission is unconfirmed, use `in-progress`, not `applied`.

Application status and vacancy status are separate. A stale application may point to a vacancy that is still open. Use `posting_status` only after checking the exact job ID or URL.

Record the application channel, warm path, portfolio version, and outcome stage whenever evidence exists. These fields are required for meaningful conversion analysis. Leave them unknown rather than reconstructing them from memory.

## Follow-up policy

- About 10 business days after applying with no response: send a short status nudge through the channel used to apply.
- About 3 weeks with no response: find the hiring manager or a designer on the team on LinkedIn. Method in `context/outreach.md`.
- 5 weeks with no response: set `stale`. Stop investing.
- Every open record carries a dated `next_action` and `next_action_on`. A SessionStart hook (`.claude/hooks/check-overdue.sh`) reads `next_action_on` from each record's frontmatter and surfaces any that are due, except for closed statuses (`rejected`, `skipped`, `stale`, `withdrawn`, `role-closed`, `hired`). Keep `next_action_on` a single `YYYY-MM-DD` date.

## Earlier pipeline (June–August 2026)

[archive-2026-07.md](archive-2026-07.md) is the frozen pre-September pipeline table. Check it for earlier skip reasons, warm paths and ATS notes before assessing a company again. Do not update it.
