---
description: Generate a full application package for a role
argument-hint: [company] [role title] [type: ds|product|fintech|founding]
allowed-tools: Read, Write
---

$ARGUMENTS should contain: company name, role title, and role type (ds / product / fintech / founding).

Before writing anything:
1. Read context/applications.md — check if this role already exists
2. Read context/salary.md — set compensation position now, do not leave it open
3. Read cv/cv-base.md — this is the only source of truth for experience content
4. Read principles.md — apply every rule before outputting anything

Then:
- Generate a role-specific CV using the reorder rules in cv/cv-base.md for the given role type
- Generate a cover letter using the salary position already set
- Save CV to cv/roles/[company-role].md
- Save cover letter to cover-letters/roles/[company-role].md
- Add the role to context/applications.md with status "in progress"

Output format: plain text only. No markdown. No em dashes. Designed for copy-paste into Figma.

Run the humanizer checklist from principles.md before outputting. Flag anything that fails.
