---
name: new-application
description: "Generate a full application package for a role. Argument: company name, role title, role type (ds|product|fintech|founding)."
allowed-tools:
  - Read
  - Write
  - Edit
  - Skill
---

# New application

$ARGUMENTS should contain: company name, role title, and role type (ds / product / fintech / founding).

Hard gate: read the role's file in `applications/records/` first. If there is no record, or the record has no Proceed decision, STOP and run `/assess-fit` before writing anything. Do not skip this even if asked to hurry. Writing before assessing is the failure mode this project is built to prevent. Recheck that the exact vacancy is still open.

Then, before writing:
1. Read `context/salary.md`. Note the employer range if one is published. Do not put a figure in the letter; if the form forces a number, propose one using the decision rules there and record it in the record's `salary_stated` only once Manel confirms what he entered.
2. Read `context/positioning.md` — use the role-specific lead table (canonical source) to pick what leads.
3. Read `cv/cv-base.md` and `evidence/experience-facts.md`. Never invent experience, metrics or ownership.
4. Read `principles.md` and `context/writing-rules.md` — apply every rule before outputting anything.
5. Reuse the structure of recent files in `cv/roles/` and `cover-letters/roles/`.

Then:
- Generate a role-specific CV following "Tailored CV format" in `context/writing-rules.md`
- Generate a short, role-specific cover letter grounded in the fit assessment
- Save CV to `cv/roles/[company-role].md`
- Save cover letter to `cover-letters/roles/[company-role].md`
- If the company already has sources from an earlier application, never overwrite them: suffix the new files with the month (`-2026-10`)
- Set the record to `status: in-progress`, list the material paths under its materials section, set `next_action`/`next_action_on`, and update `applications/active.md`

Output: a Markdown source ready for copy-paste into Figma. No em dashes. PDF export and QA are separate tasks.

Before drafting, invoke the `no-ai-slop` skill. After drafting, run the `humanizer` skill on both documents before saving. Both are mandatory, not optional.

Enforce the length caps: cover letter under 180 words in three paragraphs max (`principles.md`, "Brevity and skimmability"); CV entries per `context/writing-rules.md`. If a draft exceeds a cap, cut it before outputting; do not ask whether to.

Run the humanizer checklist from `principles.md` before outputting. Flag anything that fails.

After Manel confirms the application was sent, update the status to `applied` via `/update-pipeline` so follow-up dates get set. Save the sent PDFs in `cv-pdf-to-send/[Company]/`.
