# Career operating system

This repository is the durable source of truth for Manel Leiva's Senior, Lead, and Staff IC product-design search. It holds strategy, claimable evidence, application records, materials, and interview preparation. It is designed to work with any agent or no agent.

## Working protocol

Before making a recommendation or drafting application material:

1. Read `context/positioning.md` and `context/target-roles.md`.
2. Read `context/pipeline-findings.md` before recommending application volume or sourcing tactics.
3. Read `context/salary.md` before recommending a salary figure or interpreting compensation evidence.
4. Read `evidence/experience-facts.md` before making claims about experience or outcomes.
5. Read the relevant file in `applications/records/` before acting on a live process.
6. Treat dated external research, salary figures, and old application status as stale until checked.
7. Update the relevant durable record after a confirmed change. Do not leave important decisions only in chat.

## Evidence classes

Every material claim must be labelled as one of:

- **Confirmed:** directly supported by a current canonical document or explicitly confirmed by Manel.
- **Recollection:** remembered by Manel or a team, but not backed by recoverable measurement.
- **External research:** derived from a third-party source; include the source and date.
- **Inference:** a plausible interpretation that must not be presented as fact.
- **Unknown:** unresolved; do not use externally until confirmed.

For every external claim, record its source and last verification date. A short CV may omit these labels, but the evidence register may not.

## Source-of-truth rules

- Strategy belongs in `strategy/`.
- Claimable work history belongs in `evidence/`.
- The working CV base is `cv/cv-base.md`. Preserve each role's scope paragraph when tailoring; use `context/writing-rules.md` for format and claim discipline.
- One application record exists per company and role in `applications/records/`.
- `applications/active.md` is a dashboard, not a second source of truth.
- Tailored CVs, letters, and sent PDFs are historical records. Never overwrite an item after it has been sent.
- `playbooks/` describe portable workflows. Agent-specific shortcuts may live in `agents/`, but they cannot contain unique business rules.

## Current migration state

The scaffold and initial application-status migration were completed on 2026-09-14. The original 32-record count is a historical snapshot; use [applications/active.md](applications/active.md) for the maintained queue and individual records for status evidence. The previous `job-search` repository remains read-only source material.

The [2026-10-13 chat audit](analysis/2026-10-13/chat-documentation-audit.md) records recovered decisions, evidence and draft copy. Its follow-up reconciles all 54 substantive conversations in the complete local career-project index, including worktrees. Original server-side ChatGPT coverage and attachment preservation remain unverified; the audit does not establish that the old ChatGPT project can be deleted.
