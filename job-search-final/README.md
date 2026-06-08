# job-search

Private repo. Job search operations for Manel Leiva.

## Structure

```
job-search/
├── CLAUDE.md                   ← Claude Code reads this first. Start here.
├── principles.md               ← Writing rules, tone, humanizer checklist
├── context/
│   ├── portfolio.md            ← Case studies, signals, portfolio writing rules
│   ├── applications.md         ← Pipeline state — update this as roles progress
│   ├── positioning.md          ← Differentiation, target persona, what I'm not
│   └── salary.md               ← Compensation positions and negotiation rules
├── cv/
│   ├── cv-base.md              ← Master CV content. Edit here, not in role files.
│   └── roles/                  ← Role-specific CV outputs (plain text, Figma-ready)
├── cover-letters/
│   └── roles/                  ← One file per cover letter
└── portfolio/                  ← Git submodule → portfolio repo (manel-leiva.com)
```

## Setup

Clone with submodule:

```bash
git clone --recurse-submodules git@github.com:yourusername/job-search.git
```

Or if already cloned:

```bash
git submodule update --init --recursive
```

## Portfolio submodule

The `portfolio/` directory points to the portfolio repo. To work on case study copy:

1. Edit files inside `portfolio/`
2. Commit in the portfolio repo: `cd portfolio && git add . && git commit -m "..." && git push`
3. Update the pointer here: `cd .. && git add portfolio && git commit -m "update portfolio submodule"`

## Working with Claude Code

Open this directory in VS Code. Run Claude Code here. It reads `CLAUDE.md` automatically.

Slash commands available in `.claude/commands/`:
- `/assess-fit` — evaluate a new role before writing anything
- `/new-application` — set up a full application package
- `/update-pipeline` — update role status in applications.md
