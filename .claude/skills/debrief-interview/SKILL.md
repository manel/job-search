---
name: debrief-interview
description: "Capture what happened in an interview while it's fresh. Argument: company name and round."
allowed-tools:
  - Read
  - Write
  - Edit
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
- Append a debrief section to `interviews/[company]/[company].md` for that round.
- Update the role's record in `applications/records/` (status, `next_action`, `next_action_on`, a dated `## History` line), then [applications/active.md](../../../applications/active.md).
- If a question exposed a reusable gap or a pattern worth keeping (a question type that keeps appearing, a story that consistently lands or doesn't), add it to [memory.md](../../../memory.md) under the relevant section. One entry per signal, dated.
- If a gap in [interviews/stories.md](../../../interviews/stories.md#gaps) or a [NEEDS YOUR STORY] mark in [interviews/question-bank.md](../../../interviews/question-bank.md) got answered live in the interview, capture the story Manel actually told as a new entry in stories.md (an ID, the four anchors, limits), point the question to it, and add the claimable facts to [evidence/experience-facts.md](../../../evidence/experience-facts.md).

Keep the debrief factual. No coaching commentary unless asked.
