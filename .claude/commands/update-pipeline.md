---
description: Update a role's status in the applications pipeline
argument-hint: [company] [status: in-progress|sent|interviewing|rejected|deferred|skipped]
allowed-tools: Read, Write
---

$ARGUMENTS should contain: company name and new status.

Valid statuses: in-progress / sent / interviewing / rejected / deferred / skipped

Open context/applications.md and update the relevant row with the new status and today's date.

If status is "interviewing", ask for: interviewer name, round number, and date before updating.
If status is "rejected", ask for: any feedback received before updating.

Keep context/applications.md as the single source of truth. Do not track status anywhere else.
