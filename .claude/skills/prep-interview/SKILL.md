---
name: prep-interview
description: "Prepare for a specific interview round at a company. Argument: company name and round type (screen|hiring-manager|case|behavioral|ways-of-working|final)."
allowed-tools:
  - Read
  - Write
  - Edit
---

# Prep interview

$ARGUMENTS should contain: company name and round type.

Before producing anything:
1. Read the role's file in `applications/records/` — confirm it is in the pipeline and get its current state and history.
2. Read [interviews/prep.md](../../../interviews/prep.md) (the index), then [interviews/stories.md](../../../interviews/stories.md) (stories by ID, with limits), [interviews/question-bank.md](../../../interviews/question-bank.md) (Q1–Q27 mapped to stories), [interviews/answers.md](../../../interviews/answers.md) (set-piece answers) and the playbook for the round type in `interviews/playbooks/` (case, live challenge, ways of working, before the call).
3. Read `interviews/[company]/` if it exists — prior rounds, interviewer notes, what already landed or didn't. Check claims against [evidence/experience-facts.md](../../../evidence/experience-facts.md); it outranks stories.md.
4. Read [context/positioning.md](../../../context/positioning.md) — pick the lead story for this role type using the role-type mapping.
5. Read [context/salary.md](../../../context/salary.md) and the record's `salary_stated` — know what was already said and the decision rules. Never walk into a round without it.

Then produce a one-page brief in `interviews/[company]/[company].md` (create the folder and file if it's the first round, append a new round section otherwise):

- Round, date, interviewer name and role (ask if unknown)
- The 2–3 things this company most likely cares about, from the JD and prior rounds
- Lead story for this round and why (use the positioning mapping, don't improvise a new one)
- Likely questions for this round type, each mapped to a story ID from [interviews/stories.md](../../../interviews/stories.md) (`dataset-manager`, `token-file`), never the old letters (Story A, card D)
- Any gaps in [interviews/stories.md](../../../interviews/stories.md#gaps) or [NEEDS YOUR STORY] marks in [interviews/question-bank.md](../../../interviews/question-bank.md) that this round is likely to hit — flag them, don't fill them with invented material
- 2–3 questions to ask them, chosen from [interviews/playbooks/before-the-call.md](../../../interviews/playbooks/before-the-call.md) and tailored to what is actually unknown about this company
- Salary position reminder if the round could touch compensation

Do not write scripts or full answers. The goal is knowing which story fits which question, not memorizing text. Link to stories and set-piece answers instead of pasting them: a pasted copy drifts from the approved wording. A company-specific variant goes in the brief as the change only ("drop the founder-driven clause"). Run `python3 scripts/check-links.py` after writing the brief.

After the interview happens, remind Manel to run `/debrief-interview`.
