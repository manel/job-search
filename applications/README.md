# Application records

Create one file per company and role in `records/`, named `company-role.md`.

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
