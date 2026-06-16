---
name: review-case
description: "Review a portfolio case study against the evaluation standard: problem complexity, candidate's specific decisions, cross-functional influence, measurable impact, what made it hard."
---

# Review case study

Reviews a case study in the live portfolio against the evaluation standard in `context/portfolio.md`.

## Arguments

`/review-case [case-name]`

Valid names: `modeling-syntax`, `dataset-manager`, `design-systems`, `design-system-remuner`

If no argument is given, review all four cases in sequence.

## What this skill does

1. Read the HTML file at `portfolio/public/cases/[case-name].html`.
2. Read the evaluation standard and case-specific signals from `context/portfolio.md`.
3. Score the case against the five criteria below.
4. Run the three additional checks below.
5. Report findings: what is working, what is weak, and quote the specific line or section that needs attention.
6. Do not rewrite unless asked. Assessment first.

## Evaluation criteria

Score each on: strong / acceptable / weak / missing.

**1. Problem complexity and ambiguity**
Does the case open on a problem that is genuinely hard? Is the difficulty specific — organizational, technical, political — or vague? A strong opening makes the reader understand why this wasn't just execution work. Flag any opener that describes symptoms without explaining why the situation was structurally difficult.

**2. Candidate's specific role and decisions**
Is it clear what Manel owned vs. what was shared? Does the case name specific decisions and the reasoning behind them, or does it narrate process? Flag: "we" without a role attribution. Flag: process narration without named judgment calls ("I identified", "I decided", "I proposed" should attach to a stated reason, not just an action).

**3. Cross-functional influence**
Does the case show work that moved across function boundaries — design, engineering, product, leadership? Is the influence specific (who, what changed as a result) or implied ("worked closely with engineers")? Implied influence scores acceptable at best.

**4. Measurable or operational impact**
Does the case land on concrete signals? Signals can be qualitative (the CTO's unprompted observation) or operational (Maker Days selected twice, engineers referencing token names). What it cannot be: vague claims without a named before/after. Flag any outcome paragraph that asserts impact without a concrete signal.

**5. What made it hard**
Does the case name a real constraint, tension, or trade-off? Strong cases have at least one moment where something didn't work or where a decision required giving something up. A case with no friction reads as sanitized.

## Additional checks

**Impact-first framing**
Scan every section for explanations of what tokens are, how pipelines work, or what design systems are in general. These read as teaching, not showing. Flag the specific paragraph. The correct fix is to lead with what changed and make the definition subordinate, not to cut the context entirely.

**Governance as prominent as the build**
Count sections that cover advocacy, governance, documentation, and community vs. sections that cover what was designed or built. If governance is one paragraph after three or more pages of component work, flag it.

**One coherent story**
Does the case follow a single thread from problem to decision to outcome? Or does it mix multiple problems, multiple phases, or multiple systems without a unifying frame? Flag where the thread breaks.

## Output format

For each criterion: score, one sentence of evidence quoted from the case, one sentence on what to fix if weak or missing.

For each additional check: pass or flag, with the specific line quoted if flagging.

End with a priority stack: the one or two changes that would most improve how a hiring manager reads this case. Be specific about which section and what the fix is.
