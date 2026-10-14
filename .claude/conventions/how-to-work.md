## How to work

### Before writing anything for a role application

1. Check `applications/records/` (and `applications/archive-2026-07.md` for June–August) to see if the role or company has already been assessed or is in progress.
2. Run a fit assessment using the framework below. No assessment, no writing. This gate has no exceptions.
3. Check `context/outreach.md`: is there a warm path? Warm paths come before or alongside cold applications. `/outreach [company] referral` drafts the ask.
4. Check `context/salary.md` before stating or recommending any salary figure.
5. Read `principles.md` and `context/writing-rules.md` before producing any written output. Check experience claims against `evidence/experience-facts.md`.
6. Run the `no-ai-slop` skill before drafting and the `humanizer` skill on every draft before output. This applies to all recruiter-facing prose (CV, cover letter, outreach, follow-up, LinkedIn) by default, not on request.
7. Respect the length caps in `principles.md` ("Brevity and skimmability"). Recruiters scan; a document that fails the 10-second test fails, no matter how good the writing is.

### CV work

- The working base is `cv/cv-base.md`, grounded in `evidence/experience-facts.md`. Never invent experience that isn't there.
- Role-specific CVs go in `cv/roles/[company-role].md`.
- What leads depends on role type: the canonical mapping is in `context/positioning.md` ("Role-specific lead"). Never change it without being asked.
- Format: follow "Tailored CV format" in `context/writing-rules.md`. The source is designed for copy-paste into Figma; PDF export and QA are separate tasks.
- No em dashes. Ever.

### Cover letter work

- Check `context/salary.md` before writing. Do not state a figure in the letter unless the application requires one.
- Fit assessment must happen before writing. Don't skip it.
- Output format: plain text, same as CV.
- Apply all rules from `principles.md` before outputting.

### Portfolio and case study work

- Case study context and signals live in `context/portfolio.md`.
- Actual case study files are in `portfolio/` (submodule). Read those for current live copy.
- HTML output follows the section structure defined in `context/portfolio.md`.
- Live case copy never names colleagues, research participants, or customers. Roles only: "the head of design", "the CTO". Names in context files are internal reference.
- Run humanizer principles from `principles.md` on all case study copy before outputting.
- `/review-case [case-name]` scores a live case against the evaluation standard. Run it before any application goes out if the case is relevant to the role.

### LinkedIn work

- Profile copy, audit, and rules live in `context/linkedin.md`.
- The live profile and that file change together. If one is edited, update the other.
- Same writing rules as everything else. The headline must carry the design systems signal explicitly.

### Interview work

- Core story library and question maps: `interviews/prep.md`. Stories repeat; the angle changes per role.
- Per-company material lives in `interviews/[company]/`: a main file per process (`[company].md`) with a section per round and the debrief appended after each round, plus any briefs, cheat sheets or challenge material.
- `/prep-interview [company] [round]` builds the one-page brief. `/debrief-interview [company] [round]` captures what happened and feeds reusable signals into `memory.md`.
- `prep.md` has [NEEDS YOUR STORY] gaps. Flag them when relevant; never fill them with invented material.

### Follow-up discipline

- The follow-up policy lives in `applications/README.md`: nudge at ~10 business days, LinkedIn outreach at ~3 weeks (method in `context/outreach.md`), stale at 5 weeks.
- Every open record has a `next_action` and a dated `next_action_on`. When asked about the pipeline, check for overdue actions first and surface them.
- `/follow-up` surfaces overdue next actions and drafts the appropriate message. Run it at the start of any session where the pipeline might have items due.

---