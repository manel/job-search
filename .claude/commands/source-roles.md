---
description: Weekly sourcing session — batch-assess new roles and clean the pipeline
argument-hint: [paste role URLs or JDs, one or more]
allowed-tools: Read, Write, WebFetch
---

This is the weekly top-of-funnel ritual. Cadence and board list live in `context/job-boards.md`. The boards themselves can't be scanned automatically (documented limitation), so Manel browses and pastes; this command does the assessment and bookkeeping.

Step 1 — Pipeline hygiene first, before any new roles:
- Read `context/applications.md`. List any overdue Next actions and any roles crossing the stale threshold this week. Surface these before assessing anything new; follow-ups on live applications outrank new applications.
- Check the Deferred table: has any revisit condition been met?

Step 2 — Assess what was pasted in $ARGUMENTS:
- Run each role through the /assess-fit framework (read that command for the full checklist, including the DS-maturity check for DS-titled roles).
- For URLs, fetch the JD if the ATS allows it; if it doesn't, ask Manel to paste the text.
- One verdict per role: Proceed / Defer / Skip, two or three sentences each. Don't soften skips.
- For every Proceed: check for a warm path (`context/outreach.md`) before suggesting a cold apply.

Step 3 — Bookkeeping:
- Record every assessed role in `context/applications.md` (Deferred or Assessed and skipped table; Proceeds get flagged for /new-application).
- If a board produced nothing useful for the third week running, note it in `context/job-boards.md`.

Step 4 — Close with a one-paragraph funnel summary: active count, overdue actions, what was added this week, and whether the pipeline is thin (under ~5 active applications means sourcing needs more volume next week).
