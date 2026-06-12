---
description: Generate a full application package for a role
argument-hint: [company] [role title] [type: ds|product|fintech|founding]
allowed-tools: Read, Write
---

$ARGUMENTS should contain: company name, role title, and role type (ds / product / fintech / founding).

Hard gate: read context/applications.md first. If this role has no recorded fit assessment (it isn't in any table, or it's there without an assessment decision), STOP and run the /assess-fit flow before writing anything. Do not skip this even if asked to hurry. Writing before assessing is the failure mode this project is built to prevent.

Then, before writing:
1. Read context/salary.md — set the compensation position now, do not leave it open. If no position exists for this role, set one using the framework in that file and record it there.
2. Read context/positioning.md — use the role-type mapping (canonical source) to pick what leads.
3. Read cv/cv-base.md — the only source of truth for experience content. Never invent experience.
4. Read principles.md — apply every rule before outputting anything.

Then:
- Generate a role-specific CV using the role-type mapping from positioning.md
- Generate a cover letter using the salary position already set
- Save CV to cv/roles/[company-role].md
- Save cover letter to cover-letters/roles/[company-role].md
- Add the role to context/applications.md with status "in-progress"

Output format: plain text only. No markdown. No em dashes. Designed for copy-paste into Figma.

Run the humanizer checklist from principles.md before outputting. Flag anything that fails.

After Manel confirms the application was sent, update the status to "applied" via /update-pipeline so follow-up dates get set.
