---
description: Update a role's status in the applications pipeline
argument-hint: [company] [status: in-progress|sent|interviewing|rejected|deferred|skipped]
allowed-tools: Read, Write
---

The pipeline lives in context/applications.md. Read that file first.

$ARGUMENTS should contain: company name and new status.

Valid statuses: in-progress / sent / interviewing / rejected / deferred / skipped

Update the relevant row in context/applications.md with the new status and today's date.

If status is "interviewing": ask for interviewer name, round number, and date before updating.
If status is "rejected": ask for any feedback received before updating.
If status is "deferred": move the row from Active to the Deferred table.
If status is "skipped": move the row from Active to the Assessed and skipped table.

Write the updated file back to context/applications.md.
