---
name: update-pipeline
description: "Update a role's status in the applications pipeline. Argument: company name and new status (prospect|assessing|deferred|skipped|in-progress|applied|interviewing|offer|hired|rejected|stale|withdrawn|role-closed)."
allowed-tools:
  - Read
  - Write
  - Edit
---

# Update pipeline

The source of truth is one record per company and role in `applications/records/`. Read `applications/README.md` first: it defines the frontmatter, the status vocabulary and the follow-up policy. Use the vocabulary exactly.

$ARGUMENTS should contain: company name and new status. Find the matching record; if more than one role exists at the company, ask which.

Only update after the change is confirmed by Manel or by evidence he supplied (an ATS email, a message). If materials exist but submission is unconfirmed, the status is `in-progress`, not `applied`.

In the record:
- Update `status`, `status_verified_on` (today) and `status_confidence`.
- Update `next_action` and `next_action_on` (a single `YYYY-MM-DD` date; the SessionStart hook reads it).
- Append a dated line to `## History`. Never rewrite earlier history.
- Fill `application_channel`, `warm_path`, `portfolio_version`, `outcome_stage` and `salary_stated` when there is evidence. Leave them unknown rather than reconstructing them from memory.

**Status-specific handling:**

- **applied:** set `applied_on`, and set `next_action_on` from the follow-up policy (nudge at ~10 business days, LinkedIn outreach at ~3 weeks, stale at 5 weeks). Compute the actual dates.
- **interviewing:** ask for interviewer name, round type, and date. Then suggest running `/prep-interview` for the round. Round material lives in `interviews/[company]/`.
- **offer:** read `context/salary.md` before discussing anything.
- **rejected:** ask for any feedback received and set `rejection_reason_class`. Never record salary as the reason unless the employer said so. If the rejection reveals a pattern worth keeping, add a dated entry to `memory.md`.
- **stale / withdrawn / role-closed:** record the reason. A stale application may point to a vacancy that is still open; `posting_status` is separate.
- **deferred:** record the reason and the revisit condition.
- **skipped:** record the reason.

Then update `applications/active.md`: move the role to the section matching its new next step, with a one-line summary. The record comes first; the dashboard follows.

Finally check `TODO.md`: if it references this role, update or remove that item in the same pass.
