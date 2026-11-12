## How to work

### Before writing anything for a role application

1. Check `applications/records/` (and [applications/archive-2026-07.md](../../applications/archive-2026-07.md) for June–August) to see if the role or company has already been assessed or is in progress.
2. Run a fit assessment using the framework below. No assessment, no writing. This gate has no exceptions.
3. Check [context/outreach.md](../../context/outreach.md): is there a warm path? Warm paths come before or alongside cold applications. `/outreach [company] referral` drafts the ask.
4. Check [context/salary.md](../../context/salary.md) before stating or recommending any salary figure.
5. Read [principles.md](../../principles.md) and [context/writing-rules.md](../../context/writing-rules.md) before producing any written output. Check experience claims against [evidence/experience-facts.md](../../evidence/experience-facts.md).
6. Run the `no-ai-slop` skill before drafting and the `anthropic-skills:humanizer` skill on every draft before output. This applies to any text someone other than Manel will read (CV, cover letter, outreach, follow-up, recruiter replies, form answers, LinkedIn, case study copy, decks, scripts) by default, not on request. Full rule in [principles.md](../../principles.md) ("Operating Rules").
7. Respect the length caps in [principles.md](../../principles.md) ("Brevity and skimmability"). Recruiters scan; a document that fails the 10-second test fails, no matter how good the writing is.

### CV work

- The working base is [cv/cv-base.md](../../cv/cv-base.md), grounded in [evidence/experience-facts.md](../../evidence/experience-facts.md). Never invent experience that isn't there.
- Role-specific CVs go in `cv/roles/[company-role].md`.
- What leads depends on role type: the canonical mapping is in [context/positioning.md](../../context/positioning.md) ("Role-specific lead"). Never change it without being asked.
- Format: follow "Tailored CV format" in [context/writing-rules.md](../../context/writing-rules.md). The source is designed for copy-paste into Figma; PDF export and QA are separate tasks.
- No em dashes. Ever.

### Cover letter work

- Check [context/salary.md](../../context/salary.md) before writing. Do not state a figure in the letter unless the application requires one.
- Fit assessment must happen before writing. Don't skip it.
- Output format: plain text, same as CV.
- Apply all rules from [principles.md](../../principles.md) before outputting.

### Portfolio and case study work

- Case study context and signals live in [context/portfolio.md](../../context/portfolio.md).
- Actual case study files are in `portfolio/` (submodule). Read those for current live copy.
- HTML output follows the section structure defined in [context/portfolio.md](../../context/portfolio.md).
- Live case copy never names colleagues, research participants, or customers. Roles only: "the head of design", "the CTO". Names in context files are internal reference.
- Run the `no-ai-slop` and `anthropic-skills:humanizer` skills on all case study copy before outputting.
- `/review-case [case-name]` scores a live case against the evaluation standard. Run it before any application goes out if the case is relevant to the role.

### LinkedIn work

- Profile copy, audit, and rules live in [context/linkedin.md](../../context/linkedin.md).
- The live profile and that file change together. If one is edited, update the other.
- Same writing rules as everything else. The headline must carry the design systems signal explicitly.

### Interview work

- Start at [interviews/prep.md](../../interviews/prep.md), the index. Stories live once in [interviews/stories.md](../../interviews/stories.md) under IDs (`dataset-manager`, `token-file`); set-piece answers once in [interviews/answers.md](../../interviews/answers.md); questions Q1–Q27 in [interviews/question-bank.md](../../interviews/question-bank.md); round formats in `interviews/playbooks/`. Stories repeat; the angle changes per role.
- Briefs link to stories and answers by ID and anchor; they never paste them. A company variant is written as the change only. Run `python3 scripts/check-links.py` after moving or renaming any Markdown file; it also flags a pasted copy of the departure answer.
- Per-company material lives in `interviews/[company]/`, one file per stage (adopted 2026-11-12; Wizeline is the reference, older folders keep their names until their next stage):
  - `[company].md`: the index. Record link, a table of stages (date, panel, file, result) and the claims already made that later stages must stay consistent with.
  - `[company]-stage[N]-[type].md`: the brief for that stage, with the debrief appended after it. N counts stages in the order they happen; a rescheduled stage keeps its number.
  - `[type]` is one of: `screening` (recruiter or TA call), `hiring-manager`, `case` (portfolio or case presentation), `challenge` (live or take-home exercise), `behavioral`, `ways-of-working`, `technical`, `client` (an agency's client), `final`, `offer`. A stage that mixes two takes the one it is mainly judged on.
  - Material for one stage: the stage file name plus what it is (`wizeline-stage3-client-answers.md`, `wizeline-stage1-screening-salary.md`). Material used in several stages: company plus what it is (`wizeline-case-deck.md`).
  - Received documents keep a dated name (`wizeline-candidate-profile-2026-11-10.pdf`). Delete material that went unused once the stage is over; the debrief says what was skipped.
- `/prep-interview [company] [round]` builds the one-page brief. `/debrief-interview [company] [round]` captures what happened and feeds reusable signals into [memory.md](../../memory.md).
- Open gaps are listed in [interviews/stories.md](../../interviews/stories.md#gaps) and marked [NEEDS YOUR STORY] in [interviews/question-bank.md](../../interviews/question-bank.md). Flag them when relevant; never fill them with invented material.

### Follow-up discipline

- The follow-up policy lives in [applications/README.md](../../applications/README.md): nudge at ~10 business days, LinkedIn outreach at ~3 weeks (method in [context/outreach.md](../../context/outreach.md)), stale at 5 weeks.
- Every open record has a `next_action` and a dated `next_action_on`. When asked about the pipeline, check for overdue actions first and surface them.
- `/follow-up` surfaces overdue next actions and drafts the appropriate message. Run it at the start of any session where the pipeline might have items due.

---