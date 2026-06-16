---
name: debrief-interview
description: "Capture what happened in an interview while it's fresh. Argument: company name and round."
allowed-tools:
  - Read
  - Write
---

# Debrief interview

$ARGUMENTS should contain: company name and round.

Ask Manel, one at a time, only what hasn't been volunteered already:
1. What questions came up that the prep didn't cover?
2. Which story did you lead with, and how did it land?
3. Anything you fumbled or would answer differently?
4. What did you learn about the team, the role, or the process?
5. Next step and expected timing?

Then:
- Append a debrief section to `interviews/[company].md` for that round.
- Update the role's row in `context/applications.md` (status, next step, date).
- If a question exposed a reusable gap or a pattern worth keeping (a question type that keeps appearing, a story that consistently lands or doesn't), add it to `memory.md` under the relevant section. One entry per signal, dated.
- If a [NEEDS YOUR STORY] gap in `interviews/prep.md` got answered live in the interview, capture the story Manel actually told and replace the placeholder with it.

Keep the debrief factual. No coaching commentary unless asked.
