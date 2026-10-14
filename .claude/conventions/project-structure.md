## Project structure

```
job-search/
├── CLAUDE.md                   ← you are here
├── TODO.md                     ← consolidated open items, check at session start
├── memory.md                   ← dated observations and rules from the search
├── principles.md               ← writing rules, tone, what never to do
├── applications/
│   ├── active.md               ← dashboard: action queue grouped by next step
│   ├── README.md               ← record format, status vocabulary, follow-up policy
│   ├── records/                ← one file per company and role (source of truth)
│   └── archive-2026-07.md      ← frozen pre-September pipeline table
├── evidence/
│   ├── experience-facts.md     ← evidence register: claimable facts, sources, limits
│   └── ...                     ← contribution audit, product-work inventory, Figma scope
├── context/
│   ├── target-roles.md         ← target, constraints, fit gate (canonical)
│   ├── positioning.md          ← core position, proof themes, role-type mapping (canonical)
│   ├── salary.md               ← compensation evidence and decision rules
│   ├── pipeline-findings.md    ← funnel analysis; read before volume or sourcing advice
│   ├── writing-rules.md        ← claim discipline and tailored-CV format
│   ├── portfolio.md            ← case studies, signals, writing rules
│   ├── linkedin.md             ← profile copy, audit, maintenance checklist
│   ├── outreach.md             ← warm paths, referral asks, silent-application outreach
│   ├── job-boards.md           ← where to search, what works
│   ├── brand.md                ← canonical visual language for any visual artifact
│   └── ...                     ← DS and AI-agent notes, asset rework, story shortlist
├── cv/
│   ├── cv-base.md              ← working CV base
│   └── roles/                  ← role-specific CV sources (Figma-ready)
├── cover-letters/
│   └── roles/                  ← one file per cover letter
├── outreach/                   ← drafted messages to named contacts
├── application-answers/        ← drafted written answers for application forms
├── cv-pdf-to-send/             ← final PDFs as sent, one folder per company
├── interviews/
│   ├── prep.md                 ← core story library, question maps
│   ├── behavioral-battle-cards.md
│   ├── [company]/              ← per-process briefs, debriefs, challenge material
│   ├── decks/                  ← case presentation decks
│   ├── textream/               ← teleprompter scripts
│   └── archive/                ← rehearsal transcripts
├── sourcing/                   ← watchlist, remote companies, role leads, scanner config (discovery, not pipeline)
├── analysis/[date]/            ← dated audits and funnel snapshots
├── scripts/                    ← role scan, posting check, PDF merge, funnel audit, builders
└── portfolio/                  ← git submodule → manel-leiva portfolio repo
```

The portfolio directory is a git submodule pointing to the portfolio repo. To update case study copy: edit files inside `portfolio/` first, commit there, then update the submodule pointer here.

Naming convention for sent PDFs: `cv-pdf-to-send/[Company]/Manel Leiva CV 2026.pdf` and `Manel Leiva CL 2026.pdf`. The folder reflects exactly what was sent; never regenerate a file in it after sending.

Every sent PDF must have its plain-text source saved in `cv/roles/` or `cover-letters/roles/` before export. The sources are the record of what each company was told; without them, claims can't be checked when an interview comes weeks later. Known gap: applications sent before July 2026 have PDFs but no sources. When a company gets a second application, keep both sources and suffix the later one with its month (`-2026-09`).

Any visual artifact (case decks, slides, CV layout, generated images) follows `context/brand.md`. Read it before producing visual output.

---
