---
name: source-roles
description: "Weekly sourcing session — batch-assess new roles and clean the pipeline. Argument: paste role URLs or JDs, one or more."
allowed-tools:
  - Read
  - Write
  - Edit
  - WebFetch
---

# Source roles

This is the weekly top-of-funnel ritual. Read `context/pipeline-findings.md` before recommending volume or channels. Board list and channel notes live in `context/job-boards.md`. Many boards can't be scanned automatically, so Manel often browses and pastes; this skill does the assessment and bookkeeping.

Two methods, each with a reference:
- **Company watchlist:** `references/company-watchlist.md`. Work through `sourcing/company-watchlist.csv` (`watch` weekly, `review` in batches, `paused` monthly) and record vacancies in `sourcing/role-leads.csv`. See `sourcing/README.md` for refreshing the watchlist.
- **LinkedIn:** `references/linkedin.md` for Open to Work, saved searches, alerts and contact discovery.

Source-checking rule: the official career page or ATS posting is the only evidence that a vacancy is open. LinkedIn and search snippets are leads.

**Step 1 — Pipeline hygiene first, before any new roles:**
Read the frontmatter of `applications/records/`. List overdue `next_action_on` dates and any applied roles crossing the 5-week stale threshold this week. Surface these before assessing anything new; follow-ups on live applications outrank new applications.
Check `deferred` records: has any revisit condition been met?

**Step 2 — Assess what was pasted in $ARGUMENTS (or found in step 1's sources):**
Run each role through the `/assess-fit` framework (read that skill for the full checklist).
For URLs, fetch the JD if the ATS allows it; if it doesn't, ask Manel to paste the text.
One verdict per role: Proceed / Defer / Skip, two or three sentences each. Don't soften skips.
For every Proceed: check for a warm path (`context/outreach.md`) before suggesting a cold apply.

**Step 3 — Bookkeeping:**
Create a record in `applications/records/` for every assessed role with an exact live posting, and place it in `applications/active.md`. Leads not yet assessed stay in `sourcing/role-leads.csv`. Proceeds get flagged for `/new-application`.
Update watchlist check dates even when nothing suitable was found. If a board produced nothing useful for the third week running, note it in `context/job-boards.md`.

**Step 4 — Close with a one-paragraph funnel summary:** active count, overdue actions, what was added this week, and whether the pipeline is thin (under approximately 5 active applications means sourcing needs more volume next week).
