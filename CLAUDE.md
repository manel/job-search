# Job Search — Claude Code Project

## Who I am

Manel Leiva. Senior Product Designer based in Barcelona. Specializing in complex B2B workflows, data-heavy products, design systems, and systems thinking. Active job search targeting Senior, Lead, or Staff IC Product Designer roles. No management. No relocation.

Portfolio: manel-leiva.com
LinkedIn: linkedin.com/in/manelleiva

---

## Project structure

```
job-search/
├── CLAUDE.md                   ← you are here
├── principles.md               ← writing rules, tone, what never to do
├── context/
│   ├── portfolio.md            ← case studies, signals, writing rules
│   ├── applications.md         ← pipeline state, all roles and decisions
│   ├── positioning.md          ← differentiation, target persona, what I'm not
│   └── salary.md               ← agreed positions, benchmarks, negotiation rules
├── cv/
│   ├── cv-base.md              ← master CV content, single source of truth
│   └── roles/                  ← role-specific CV outputs (plain text, Figma-ready)
├── cover-letters/
│   └── roles/                  ← one file per cover letter
└── portfolio/                  ← git submodule → manel-leiva portfolio repo
```

The portfolio directory is a git submodule pointing to the portfolio repo. To update case study copy: edit files inside `portfolio/` first, commit there, then update the submodule pointer here.

---

## How to work

### Before writing anything for a role application

1. Read `context/applications.md` to check if the role has already been assessed or is in progress.
2. Run a fit assessment using the framework in `context/positioning.md`.
3. Check `context/salary.md` for the agreed compensation position before writing any cover letter.
4. Read `principles.md` before producing any written output.

### CV work

- Master content lives in `cv/cv-base.md`. Never invent experience that isn't there.
- Role-specific CVs go in `cv/roles/[company-role].md`.
- Reorder logic: DS roles lead with Remuner DS work. Product roles lead with Abacum integrations. Fintech/trading roles lead with Modeling Syntax. Never change this without being asked.
- Output format: plain text only. No markdown formatting beyond line breaks. Designed for copy-paste into Figma.
- No em dashes. Ever.

### Cover letter work

- Always confirm salary position from `context/salary.md` before writing. Never leave compensation open.
- Fit assessment must happen before writing. Don't skip it.
- Output format: plain text, same as CV.
- Apply all rules from `principles.md` before outputting.

### Portfolio and case study work

- Case study context and signals live in `context/portfolio.md`.
- Actual case study files are in `portfolio/` (submodule). Read those for current live copy.
- HTML output follows the section structure defined in `context/portfolio.md`.
- Run humanizer principles from `principles.md` on all case study copy before outputting.

---

## Target roles

Senior Product Designer, Lead Product Designer (IC), Staff Product Designer.
IC only. No design management.

Target companies: B2B SaaS, fintech, data-heavy platforms, complex workflow software. Series A–C or established product companies.

Location: Remote, or hybrid in Barcelona. No relocation.

---

## Fit assessment framework

Run this before any application. Score each dimension and give a clear proceed / defer / skip decision.

| Dimension | Check |
|---|---|
| Domain | B2B SaaS, fintech, data-heavy, or complex workflow? |
| Scope | Senior, Lead, or Staff IC? Not management, not junior? |
| Work type | Product design and systems thinking? Not pure UI production? |
| Location | Remote or Barcelona hybrid? |
| Genuine interest | Would I actually want this job? |
| Stack signal | Figma, design systems, complex workflows in JD? |

A weak score on Domain or Genuine Interest is a skip, not a defer. Don't write applications for roles you don't want.

---

## Strategic rules

- Never optimize a CV or cover letter without first assessing fit. Writing first wastes time.
- When fit is marginal, say so. Don't dress it up.
- Salary: always open at the top of the range. Never give a range when the ceiling is known. Never share previous salary if asked.
- Warm referrals are higher leverage than cold applications. Flag when a role might have a warm path.
- Don't add case studies or portfolio work that doesn't improve hiring outcomes. Motion as evidence is appropriate. Motion as decoration is not.

---

## Reading order for a new session

1. This file (already done)
2. `memory.md` — observations and rules captured during the search
3. `context/applications.md` — know the pipeline state
4. Task-specific file: `context/portfolio.md` for portfolio work, `context/salary.md` before any cover letter, `context/positioning.md` for strategy
5. `principles.md` before any written output