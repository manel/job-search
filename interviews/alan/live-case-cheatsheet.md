# Live case cheat sheet (Alan, Fri 2026-10-16, 14:00)

One page to keep open next to the board. Built 2026-10-15 from mocks 1 (Juniper clinics) and 2 (Spendly). Full prep and mock results: [alan-technical-interview.md](alan-technical-interview.md).

## First minute

- Share the board link. Say which tool you're using, and whether you used AI offline (what for, and that the decisions are yours).
- Say the plan out loud: "About 20 minutes of questions, 3 minutes to synthesise, then two or three directions, the flow, and how we'd measure it."

## Questions (rewrite them in the brief's words and highlight before the call)

**Core 8, in this order:**

1. Who is the user, and is the person who pays the same as the person who uses it?
2. What happens today, step by step, and where does it break?
3. What does the user see or know at each step?
4. Do we have research, verbatims or support tickets?
5. Why is this a priority now, and which metric is the team accountable for?
6. What are we not allowed to do, legally or by policy? What has to stay with a person?
7. What do we know in numbers, and is anything believed rather than measured?
8. Team, timeline, and what you want to see at the end: app, web or both?

**Backups:**

- What triggers the journey, and what is the user trying to get done at that moment?
- Is this mainly a growth, retention, cost or support-load problem?
- Does the buyer care about this, or only the user?
- One market or several?
- Is a human in the loop (support, experts), and what does that cost?
- Existing patterns in the app we should reuse?

**Domain you don't know:** you're scored on asking, not knowing. If the answer is "you decide", say the assumption out loud and write it down: "I'll assume a clinician has to approve anything clinical."

## Synthesis

1. Map the journey. Put each pain point on a sticky under its step, including the steps before and after the one you suspect.
2. Group the stickies into 3–4 named groups. Say the names.
3. Pick one: "I'm going with [group] because [their data]. I'm leaving [other] for later because [reason]."
4. One sentence: for [user], in [situation], the problem is [X], shown by [evidence they gave].

**Check before moving on:**

- The problem is the user's, not a fact ("they don't need to come in") and not a solution ("they approve manually").
- "Shown by" is a number or a quote they gave you.
- Your reason holds against your own map. Spendly: "the step that takes longest" was wrong, because submitting took 8 days and the manager 6.
- Never say "we can't control it" about a step that happens in our product.

## Directions

- Two or three options that differ in kind: self-serve, human-assisted, proactive, automated.
- For each: who it helps, where it could break, one line on the business.
- Check out loud that your pick fixes the break point you circled. In mock 1, triage didn't fix the no-shows.
- Justify the pick with a number from their data. Mock 2: "Checking at scan removes the 22% send-back, about 7 days each" beat "it helps more personas".
- Drop an option with their data, not a guess.
- Name what you give up. "I don't give up anything" sounds like you're avoiding the tradeoff.
- Ask her before you decide: "Given what you said about X, I'd go with B. Does that match what you'd expect?"
- When she adds new information, say what it changes: "That changes my assumption about X, so I'd move to Y."

## Flow

- Start it in the last 10–15 minutes, not earlier.
- The user's input decides the path. Ask what they need before you offer a slot or option.
- Under each step: what the user sees, knows or feels.
- Show at least one step where things go wrong (rejected, missing information, no slot), not only the happy path.

## Close

- Each metric is baseline then target, using their numbers: "median 19 days, aim for 12".
- Say one user signal and one business signal out loud, and write them in the boxes. In mock 1 they stayed empty, which is Celine's round-1 gap.
- Optional guardrail: what must not get worse.
- End with what you'd test first and what you'd do next.

## Time

- The offline part is 20 minutes. In mock 2 it ran about an hour.
- Keep stickies to a few words. Say the reasoning out loud instead of writing it.
