# Job search project

Private repo. Job search operations for Manel Leiva: strategy, claimable evidence, one record per application, materials, and interview preparation.

## Structure

```
job-search/
├── CLAUDE.md                   ← Claude Code reads this first. Start here.
├── memory.md                   ← Dated observations and rules from the search
├── principles.md               ← Writing rules, tone, humanizer checklist
├── TODO.md                     ← Open items
├── applications/
│   ├── active.md               ← Dashboard: the action queue
│   ├── README.md               ← Record format, statuses, follow-up policy
│   ├── records/                ← One file per company and role (source of truth)
│   └── archive-2026-07.md      ← Frozen pre-September pipeline table
├── evidence/                   ← Evidence register and contribution audits
├── context/                    ← Target roles, positioning, salary, pipeline findings,
│                                 writing rules, portfolio, LinkedIn, outreach, brand
├── cv/
│   ├── cv-base.md              ← Working CV base
│   └── roles/                  ← Role-specific CV sources (Figma-ready)
├── cover-letters/roles/        ← One file per cover letter
├── outreach/                   ← Drafted messages to named contacts
├── application-answers/        ← Drafted written answers for application forms
├── cv-pdf-to-send/             ← Final PDFs as sent, one folder per company
├── interviews/
│   ├── prep.md                 ← Core story library, question maps
│   └── [company]/              ← Per-process briefs and debriefs
├── sourcing/                   ← Company watchlists, role leads, scanner config
├── analysis/[date]/            ← Dated audits and funnel snapshots
├── scripts/                    ← Role scan, posting check, PDF merge, funnel audit
└── portfolio/                  ← Git submodule → portfolio repo (manel-leiva.com)
```

The full annotated tree and the rules for each folder are in `.claude/conventions/project-structure.md` and `.claude/conventions/evidence-and-records.md`.

## Setup

Clone with submodule:

```bash
git clone --recurse-submodules git@github.com:manel/job-search.git
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

## Running the role search

The scanner uses the separate career-ops checkout as its engine. Our own config and history stay in `sourcing/scan/`. career-ops's own CV, profile and tracker are never touched.

Requirements: Node, plus a career-ops checkout with its dependencies installed:

```bash
git clone https://github.com/santifer/career-ops.git ~/Dev/career-ops
cd ~/Dev/career-ops && npm install
```

If the checkout lives somewhere else, set `CAREER_OPS_DIR=/path/to/career-ops`.

Commands (run from this repo's root):

```bash
# Scan every watchlist company (watch/review) and every remote company with a careers_url.
# New matching postings are appended to sourcing/role-leads.csv with next_action "Run /assess-fit".
python3 scripts/scan-roles.py

# Preview only, write nothing
python3 scripts/scan-roles.py --dry-run

# Only postings published in the last N days
python3 scripts/scan-roles.py --since 7

# Check whether the job_url of each open application record is still live (report only)
python3 scripts/check-postings.py
python3 scripts/check-postings.py --all      # include closed records too

# Rebuild the company watchlist from an upstream companies.csv
python3 scripts/build-company-watchlist.py \
  --input /path/to/companies.csv \
  --overrides sourcing/company-overrides.csv \
  --output sourcing/company-watchlist.csv
```

Title and location filters live in `sourcing/scan/filters.json`. Seen postings are kept in `sourcing/scan/data/scan-history.tsv`, so a rerun only reports new ones. `sourcing/scan/portals.yml` is regenerated on every run; don't edit it by hand. A company is only scanned if its `careers_url` points at a supported job board (Greenhouse, Ashby, Lever, Teamtailor, Personio, Workable, SmartRecruiters, Recruitee and others). To add one, set `careers_url` and `career_platform` in `sourcing/company-overrides.csv` or `sourcing/remote-companies.csv`.

Don't run `npm run scan` (or the other career-ops npm scripts) inside the career-ops checkout for this search. Those read and write career-ops's own profile and tracker, not this repo.

After a scan, run `/source-roles` or `/assess-fit` on the new rows in `role-leads.csv`. Details and the source-checking rule: `sourcing/README.md`.

## Working with Claude Code

Open this directory in VS Code or the terminal. Run Claude Code here. It reads `CLAUDE.md` automatically. A SessionStart hook (`.claude/hooks/check-overdue.sh`) surfaces overdue `next_action_on` dates from the application records; it is registered in `.claude/settings.json`.

Slash commands (all in `.claude/skills/`):

Application pipeline:
- `/assess-fit` — evaluate a new role before writing anything
- `/new-application` — set up a full application package (requires a fit assessment first)
- `/update-pipeline` — update a role's record and the dashboard after a confirmed change
- `/source-roles` — weekly sourcing session, batch-assess new roles

Follow-up and outreach:
- `/follow-up` — surface overdue next actions and draft the message
- `/outreach [company] [type]` — draft a referral ask or LinkedIn silent-application message

Portfolio:
- `/review-case [case-name]` — score a case study against the evaluation standard

Interviews:
- `/prep-interview [company] [round]` — build a one-page brief for a round
- `/debrief-interview [company] [round]` — capture what happened after a round

## Reading in Obsidian

The repo can be opened as an Obsidian vault. Vault settings in `.obsidian/` are committed; the per-session workspace files are ignored.

## History

From 2026-09-14 to 2026-10-14 the search ran in a separate repo, career-os (built with ChatGPT/Codex), while this repo was read-only. On 2026-10-14 career-os was merged in with its full git history: its `strategy/` became `context/`, its `materials/` became `cv/`, `cover-letters/`, `outreach/` and `application-answers/`, and its playbooks became skill references. Its 2026-10-13 chat audit (`analysis/2026-10-13/`) notes that the original ChatGPT project's 27 chats and their attachments have not been fully preserved; do not delete that project on the strength of this merge.
