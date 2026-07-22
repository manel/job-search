# Factorial Round 3 — 9:55am Cheat Sheet

One page. Read it once before the challenge starts, then close it. Everything here is derivable live; this is just the scaffolding so you don't freeze under the clock.

---

## The shape of the hour

| Time | Do | Hard rule |
|---|---|---|
| 0–8 | Clarifying questions, out loud, before Figma | Even if they say "start working" |
| 8–18 | Problem framing page: who, the one job, success/failure, **business objective (1 line + metric)**, core loop, MVP boundary, real problem | Leave it visible and legible |
| 18–30 | Structure: boxes and arrows, states, no UI | Staff signals live here |
| 30–50 | Design 1–2 screens where the core problem is solved | **One real screen open by min 35** |
| 50–60 | "What I didn't build" page: 5 deferrals + "if I had 2 more hours" | The Staff signal most skip |

Two failure modes: still framing at min 35, open a screen now. Deep in UI and lost, go back and write one sentence on what you're solving.

---

## Clarifying questions: the test + the six forks

**Test:** ask it only if different answers produce different designs. Picture the two designs first. Can't name the fork? Don't ask it.

**Say the fork out loud:** "Who's the primary user? If it's the employee I design X, if it's the manager I design Y." The reasoning behind the question is the signal, not the question.

**The six fork dimensions** (ask the 2–3 that fork *this* brief most, usually WHO + WHICH-PROBLEM + one):
1. **WHO** is the primary user? Three candidate users = three products. Make them pick.
2. **WHICH PROBLEM**, when the term is vague? ("Reviews" = appraisal / continuous / goals. "Track time *and* get to payroll" = two products.)
3. **OPTIMIZE FOR** speed / compliance / error reduction / quality? Can't serve all. Make them name one.
4. **AUTHORITY / VISIBILITY**: who approves, who sees, centralized or delegated?
5. **PLATFORM / CONTEXT**: desktop / mobile / shared kiosk? Wrong guess sinks the UI.
6. **BOUNDARY**: greenfield or extension, and "is X in scope or an input?"

**Time-pressure move:** ask the 1–2 that fork everything, then **state assumptions and invite correction.** "I'll assume manager is the primary user and I'm optimizing for speed. Stop me if that's wrong." Decisive beats exhaustive, and you can't look like you missed something if you're inviting the miss to be caught.

---

## Scoping: the core-loop test + the seven axes

**Core-loop test:** find the one loop the primary user repeats. For everything else ask: does the loop still produce value without this in v1? If yes, defer it. **Assume away hard inputs** (the balance is a number you assume, not an engine you build).

**The seven axes** (walk them out loud to generate the deferral list, no domain knowledge needed):
1. Config / admin (different user, defer)
2. Upstream (what feeds data in)
3. Downstream (reporting, analytics, integrations, exports)
4. Permissions / delegation
5. Compliance / rules engines (calculations, legal logic, defer)
6. Adjacent inputs (other people's contributions)
7. Platform variants (mobile, offline, region, biometric, kiosk)

You can defer something even if you're unsure it's a real feature. No penalty for it. Big penalty for trying to build everything. **Your bigger risk is over-building, not under-knowing.** When in doubt, cut more and name it.

---

## Hour 2: narrate the thinking, not the output

1. "How I read the problem" — user, goal, cost of failure, and the business objective with the metric you'd move (the Jonathan moment)
2. "What I chose to solve" — the real problem, what I deprioritized
3. "The structure before UI" — flows, decision points (Alberto + Marta)
4. "What I designed and why" — choices + what I chose not to build
5. "What's missing" — frame your bet as a hypothesis: the riskiest assumption, how you'd validate it cheaply, and the signal that would prove you wrong

Every tradeoff named out loud is a Staff signal: "X vs Y, I went X because Z." Every assumption owned is design reasoning, not weakness.

**Per panelist:**
- **Marta:** when she pushes, engage don't defend. "Why this MVP?" = three axes: user pain, business risk, learning potential. Never "it felt right."
- **Alberto:** peer-to-peer, skip the basics. "How does it scale?" = state model, reusable patterns, how structure handles exceptions and permissions.
- **Jonathan:** user and business outcomes only, zero design vocab. "How does it help the business?" = fewer delays, fewer errors, less rework, retention.

---

## Salary (level is decided this round)

If asked: "That depends on where this sits in your framework. Senior or Staff?" Then quote. Never volunteer first.
- **Senior:** 80K€. The floor. Do not go lower.
- **Staff:** 93K€ opening. Do not drop to Senior pricing if leveled Staff.

---

## The one line to carry in

Ask what forks the design. Find the loop. Keep only what the loop needs. Defer along the seven axes. Name every tradeoff out loud. Cut more than feels comfortable, and say why.
