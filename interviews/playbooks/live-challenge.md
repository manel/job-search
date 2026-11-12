# Live design challenge

A distinct format from case presentation. You are given a brief in-session and expected to produce work — then present it. Increasingly common at Staff-level hiring.

**What they are actually evaluating:** not the output. The reasoning and judgment visible in the output. A polished design produced the wrong way reads worse than a rough one produced the right way.

Related material:
- Framing practice: [interviews/drills/framing-drills.md](../drills/framing-drills.md) (keys in a separate file; don't open them before answering).
- Live-case rules from Alan (synthesis drift, discovery structure on the board): [memory.md](../../memory.md), "Interview question patterns", 2026-10-16 and 2026-10-22.
- Worked examples from past rounds: the Alan one-page board sheet, [alan/live-case-cheatsheet.md](../alan/live-case-cheatsheet.md), and the Factorial core-loop scoping method, [factorial/factorial-mvp-scoping-method.md](../factorial/factorial-mvp-scoping-method.md).
- Lead with the user journey and what the user sees; business impact gets one line and one signal.

## The gap the Factorial challenge exposed (2026-07-02)

The prep for that round emphasized scoping down, naming what you're not building, and validating before adding complexity. That is correct execution discipline. It is not sufficient on its own.

What the panel needed — and didn't see — was a vision of what the product needs to be to create real value and compete in the market. Not the minimum. The full proposition. Then, from that vision, a disciplined scoping of what this session will address.

The failure mode: presenting a careful, validated, minimal solution when they wanted to see what you'd build if you were right. "Validation thinking" reads as conservative and junior. "Vision thinking" reads as Staff.

**The corrected approach for any "build from zero" challenge:**

**Step 0 — Vision before scoping (5 min)**

Before the problem framing page, answer this in writing:

- What does this product need to be to win in the market?
- What's the full value proposition — not just the MVP, but the thing users would pay for and competitors would fear?
- What does success look like at scale, not just at launch?

This is the vision anchor. Everything else scopes down from here. Without it, you're building from the floor up. With it, you're building from the ceiling down — which reads as a different level of designer.

**Then:** problem framing, core flow, design, "what I didn't build." The rest of the playbook stays.

**In the hour 2 presentation, lead with the vision:**

"Here's what I believe this product needs to be to create real value for this user and compete. Here's the piece I chose to design in this session as the most critical part of that — and here's why."

That structure shows product thinking before craft. It also makes the scoping decision look deliberate rather than conservative.

## What to avoid

- Scoping down without first showing you understand the full scope. Scope decisions only read as judgment if it's clear you could have built more and chose not to.
- "We should validate first before adding automation" in a challenge context. That framing is correct in production. In a challenge it signals you don't know what the product should eventually be.
- Treating the brief as the problem definition. The brief gives you a domain. You define the product.

## Takeaways from Dashinsky, *Solving Product Design Exercises* (2018), read 2026-10-14

External source; the author ran design hiring at WeWork. The book is aimed at entry- to mid-level candidates, and parts of it are dated. Where a company publishes its own format, the company's format wins.

- **Framework (5W1H):** Why (goal and business opportunity) → Who (one audience) → When/Where (context, trigger, emotion) → What (3–4 ideas) → choose → Solve → How (measure). Write the step names on the board at the start as your agenda, so they act as a prompt when you're under pressure.
- **Open with Why:** company mission → benefit to the user → business opportunity. This is the same move as the vision anchor above.
- **User vs. customer:** in B2B2C, the buyer and the user are different people. Say so out loud, even if it doesn't change the solution.
- **Pick one audience, then sub-groups with different needs.** Sub-groups are a quick source of distinct ideas.
- **"You decide" from the interviewer is a test.** It checks how you work with limited information. State the assumption and move on.
- **Diverge on the properties of the solution:** channel, platform, interface type, human vs. automated. This avoids three variations of one idea.
- **Choose with reach × value × revenue vs. effort.** In an exercise, pick an idea with enough substance to design. The cheapest quick win is often too thin.
- **Pros and cons of every option, including the one you chose.** Being critical of your own pick reads as judgment, not weakness.
- **"Defining tasks" is the fastest way to build a flow:** list what the user must be able to do, then sequence it. Check the step before and after the product, because value often sits there.
- **Measure with three kinds of metric:** a user metric (task success, time), a business metric, and a guardrail that must not get worse (e.g. less doctor time per patient while NPS holds). Split short-term from long-term.
- **When stuck, say the step out loud** ("I'm thinking about when and where this happens…"). Either it unblocks you or the interviewer helps. Neither costs points.
- **Expect one deliberate pushback.** The book recommends that interviewers plan one. Engage with it; don't defend reflexively.
- **The interviewer's checklist works as a self-check:** asks questions · takes feedback · follows a process · makes valid assumptions · links to the mission · names the audience · uses context · explains how the best idea was chosen · gives pros and cons · goes beyond the obvious · sets success measures.
- **Where the book conflicts with modern live formats:** it puts 50% of the time into UI ("Solve") and treats the exercise as solo work followed by a presentation. Collaborative, journey-first formats (Alan) reverse both.

## Pre-challenge checklist

1. Write the vision answer before opening any design tool
2. Make the vision visible on a labeled Figma page — the panel will read it
3. When presenting in hour 2: state the vision before the scoping. The scoping is a response to the vision, not a substitute for it.
4. Put the discovery structure on the board in the first minutes (task, signal, problem statement, metric) and check that the problem statement cites the number or break point the brief gave you.
5. Name the two or three user challenges that could break the flow before drawing anything.
