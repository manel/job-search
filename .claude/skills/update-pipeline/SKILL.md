---
name: update-pipeline
description: "Update a role's status in the applications pipeline. Argument: company name and new status (in-progress|applied|interviewing|offer|rejected|stale|deferred|skipped)."
allowed-tools:
  - Read
  - Write
---

# Update pipeline

The pipeline lives in `context/applications.md`. Read that file first. The status vocabulary is defined at the top of that file — use it exactly.

$ARGUMENTS should contain: company name and new status.

Valid statuses: in-progress / applied / interviewing / offer / rejected / stale / deferred / skipped

Update the relevant row with the new status and today's date.

**Status-specific handling:**

- **applied:** set the Next action column using the follow-up policy in `context/applications.md` (nudge at ~10 business days, LinkedIn outreach at ~3 weeks, stale at 5 weeks). Compute the actual dates.
- **interviewing:** ask for interviewer name, round type, and date. Then suggest running `/prep-interview` for the round. Move follow-up tracking into `interviews/[company].md`.
- **offer:** check `context/salary.md` for the agreed position before discussing anything.
- **rejected:** ask for any feedback received. Move the row to the Closed table. If the rejection reveals a pattern worth keeping (a recurring objection, a positioning gap), add a dated entry to `memory.md`.
- **stale:** move the row to the Closed table with a stale marker.
- **deferred:** move the row to the Deferred table with a reason and a revisit condition.
- **skipped:** move the row to the Assessed and skipped table with the reason.

Write the updated file back to `context/applications.md`.
