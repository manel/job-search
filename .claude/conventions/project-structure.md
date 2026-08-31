## Project structure

```
job-search/
├── CLAUDE.md                   ← you are here
├── TODO.md                     ← consolidated open items, check at session start
├── memory.md                   ← dated observations and rules from the search
├── principles.md               ← writing rules, tone, what never to do
├── context/
│   ├── portfolio.md            ← case studies, signals, writing rules
│   ├── applications.md         ← pipeline state, statuses, follow-up policy
│   ├── positioning.md          ← differentiation, role-type mapping (canonical)
│   ├── salary.md               ← agreed positions, benchmarks, negotiation rules
│   ├── linkedin.md             ← profile copy, audit, maintenance checklist
│   ├── outreach.md             ← warm paths, referral asks, silent-application outreach
│   ├── job-boards.md           ← where to search, what works
│   ├── brand.md                ← canonical visual language for any visual artifact
│   └── design-systems-notes.md ← raw DS intake archive (distilled into portfolio.md)
├── cv/
│   ├── cv-base.md              ← master CV content, single source of truth
│   └── roles/                  ← role-specific CV outputs (plain text, Figma-ready)
├── cover-letters/
│   └── roles/                  ← one file per cover letter
├── cv-pdf-to-send/             ← final PDFs as sent, one folder per company
├── interviews/
│   ├── prep.md                 ← core story library, question maps
│   ├── [company].md            ← per-process briefs and debriefs
│   └── [company]-*.md          ← supporting artifacts for a process (challenge decks, cheat sheets)
└── portfolio/                  ← git submodule → manel-leiva portfolio repo
```

The portfolio directory is a git submodule pointing to the portfolio repo. To update case study copy: edit files inside `portfolio/` first, commit there, then update the submodule pointer here.

Naming convention for sent PDFs: `cv-pdf-to-send/[Company]/Manel Leiva CV 2026.pdf` and `Manel Leiva CL 2026.pdf`. The folder reflects exactly what was sent; never regenerate a file in it after sending.

Every sent PDF must have its plain-text source saved in `cv/roles/` or `cover-letters/roles/` before export. The sources are the record of what each company was told; without them, claims can't be checked when an interview comes weeks later. Known gap: applications sent before July 2026 have PDFs but no sources.

Any visual artifact (case decks, slides, CV layout, generated images) follows `context/brand.md`. Read it before producing visual output.

---