# Career operating system

This repository is the durable source of truth for Manel Leiva's Senior, Lead, and Staff IC product-design search. It holds strategy, claimable evidence, application records, materials, and interview preparation. It is designed to work with any agent or no agent.

## Working protocol

Before making a recommendation or drafting application material:

1. Read `strategy/positioning.md` and `strategy/target-roles.md`.
2. Read `strategy/pipeline-findings.md` before recommending application volume, salary changes, or sourcing tactics.
3. Read `evidence/experience-facts.md` before making claims about experience or outcomes.
4. Read the relevant file in `applications/records/` before acting on a live process.
5. Treat dated external research, salary figures, and old application status as stale until checked.
6. Update the relevant durable record after a confirmed change. Do not leave important decisions only in chat.

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
- One application record exists per company and role in `applications/records/`.
- `applications/active.md` is a dashboard, not a second source of truth.
- Tailored CVs, letters, and sent PDFs are historical records. Never overwrite an item after it has been sent.
- `playbooks/` describe portable workflows. Agent-specific shortcuts may live in `agents/`, but they cannot contain unique business rules.

## Current migration state

The scaffold and application-status migration were completed on 2026-09-14. The dashboard contains 32 reconciled records: four active, fifteen rejected, seven stale without a decision, four not submitted, and two vacancies closed. The previous `job-search` repository remains read-only source material.
