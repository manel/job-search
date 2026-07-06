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
1. Read `context/applications.md` — confirm the role is in the pipeline and get its current state.
2. Read `interviews/prep.md` — the core story library and question maps.
3. Read `interviews/[company].md` if it exists — prior rounds, interviewer notes, what already landed or didn't.
4. Read `context/positioning.md` — pick the lead story for this role type using the role-type mapping.
5. Read `context/salary.md` — know the agreed position cold. Never walk into a round without it.

Then produce a one-page brief in `interviews/[company].md` (create the file if it's the first round, append a new round section otherwise):

- Round, date, interviewer name and role (ask if unknown)
- The 2–3 things this company most likely cares about, from the JD and prior rounds
- Lead story for this round and why (use the positioning mapping, don't improvise a new one)
- Likely questions for this round type, each mapped to a story from `interviews/prep.md`
- Any [NEEDS YOUR STORY] gaps in `interviews/prep.md` that this round is likely to hit — flag them, don't fill them with invented material
- 2–3 questions to ask them, chosen from `interviews/prep.md` and tailored to what is actually unknown about this company
- Salary position reminder if the round could touch compensation

Do not write scripts or full answers. The goal is knowing which story fits which question, not memorizing text.

After the interview happens, remind Manel to run `/debrief-interview`.
