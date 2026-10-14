---
name: remember
description: "Capture a dated observation, pattern, or rule from the job search into memory.md. Argument: the observation."
allowed-tools:
  - Read
  - Edit
---

# Remember

$ARGUMENTS contains the observation to capture. If it's ambiguous or missing, ask what happened before writing anything.

1. Read `memory.md`. Check whether an existing entry already covers this. If one does, update that entry (same date convention) instead of adding a duplicate. If the new observation contradicts an existing entry, correct the old one and note the correction, the way the 2026-06-12 Remuner AI agent entry does.
2. Pick the section: Recruiter and process signals / Writing rules / References and departure context / Interview question patterns / Strategic observations. Add a new section only if none fits. A fact about Manel's work (what he did, owned or shipped) goes in `evidence/experience-facts.md` with its source and date, not here. A note about one live role goes in its record in `applications/records/`.
3. Write one dated entry: `**YYYY-MM-DD** — ` followed by the observation. Keep it factual and specific enough to act on months later without this conversation's context. Name companies, people's roles, and dates.
4. If the observation is about a job board or sourcing channel, put it in `context/job-boards.md` instead. If it's about a specific live application, it probably belongs in that role's record in `applications/records/`; put it there and only add to memory.md if it generalizes beyond that one role.

Do not capture things already recorded in CLAUDE.md, principles.md, or the context files. Memory is for what was learned in use, not for restating the setup.
