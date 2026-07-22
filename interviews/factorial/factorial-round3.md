# Factorial — Round 3: Live Design Challenge

**Date:** Wednesday 2026-07-01, 10am–12pm CET
**Format:** 2 hours. Hour 1: assignment given, solo work. Hour 2: panel joins, present process, Q&A.

---

## The panel

| Name | Role | Lens |
|---|---|---|
| Marta Serrano | Product Design Director | Judgment, decision quality, product reasoning |
| Alberto Martínez | Design Director (Finance domain) | System thinking, design decisions, DS maturity. Background in DS from Prezi — speaks your language, don't over-explain craft basics |
| Jonathan Centeno Mayado | Director of Growth (2nd employee) | Product outcomes, business impact, user framing. Not a designer. Frame in user and business outcomes |

**Marta's framing from Round 2:** they are looking for product builders — not just designers, not just engineers, not just PMs. Someone who collapses the role boundaries and thinks across the full product. This should be present in how you narrate the work in hour 2, not just in what you design.

**Implication:** This is not a design crit. It's a cross-functional panel. Open with problem and business impact — it works for everyone, not just Jonathan. Then move into structure and decisions. Lead with design vocabulary and you risk losing half the room before you've made your case.

---

## What this round is actually testing

Not whether you can produce a polished design in 60 minutes. They're evaluating:

1. Do you ask clarifying questions before touching Figma, or do you just start?
2. Do you clarify scope aggressively, or do you try to design the full product?
3. Do you identify the real problem beneath the brief's surface problem?
4. Do you name tradeoffs explicitly — not "I chose this" but "I chose this over X because Y"?
5. Do you show system-level structure before going to UI?
6. Do you annotate what you didn't build and why?

**The leveling instrument:** they use this to decide Senior vs. Staff. The output from hour 1 is evidence. The narration in hour 2 is the test.

---

## Known domain pool

The challenge will come from one of Factorial's HRIS verticals. Format confirmed by Marta: build from zero — define the problem and design the core experience. Not a "fix this broken flow" prompt.

- Time & attendance (clock in/out, schedules, overtime)
- Leave management (requests, approvals, balance visibility)
- Payroll (calculation, payslips, corrections)
- Recruitment / ATS (job posting, pipeline, candidate)
- Onboarding (tasks, document signing, progress)
- Performance (reviews, goals, 1:1s)
- Expenses (submission, approval, reporting)
- Org structure / company hierarchy

The spinoff is early-stage. The domain may be less mature — they may be testing whether you can define what the MVP covers, not just design within an established product.

**The trap:** trying to design the full product. Don't. Pick one user, one core job, one core flow. Explicitly name what you're not building.

---

## Hour 1 playbook

Use this order. Do not skip steps.

### 0–8 min — Ask clarifying questions before opening Figma

Before touching any tool, ask 3–5 sharp questions. Even if the brief says "start working."

Good questions:
- "Who is the primary persona — HR manager, employee, or team manager?"
- "Is this greenfield or an extension of the existing Factorial product?"
- "Desktop-first, or multi-platform?"
- "Are we optimizing for speed, compliance, or error reduction?"
- "Any constraints around approvals or permissions I should know about?"

Why this matters: senior candidates solve the prompt. Staff candidates reshape it. Asking sharp questions before designing signals that the problem definition is part of the work — not a given.

Also: the brief may contain deliberate ambiguity. HR and finance workflows naturally expand into permissions, delegated approvals, exceptions, audit history. The panel may probe this on purpose. When you hit one of those hidden branches, name it out loud: "Before I lock this design, I'd clarify whether approval authority is centralized or delegated — that changes the flow significantly." That's the move.

### 8–18 min — Define before designing

Open a Figma page labeled **"Problem framing."** Write answers to these before touching any component:

1. Who is the primary user? (HR manager, employee, team manager — pick one, don't hedge)
2. What is the one job they need to do in this domain that creates the most friction or cost?
3. What does success look like for them? What does failure look like?
4. Business objective (one line): what outcome am I designing toward, and what metric would show I moved it? This is the business's success, not the user's. It is the Jonathan opener and the business-risk axis Marta probes. Keep it to one line, do not build a metrics section.
5. What is the core loop? (What they do every day or every week — not edge cases)
6. What is the MVP boundary? What does v1 include, and what explicitly does it not?
7. What is the real problem here vs. what the brief names?

The directors will read this page. Leave it visible and legible.

### 18–30 min — Structure before screens

Map the primary user journey at conceptual level. No UI yet.

- Entry point: how does the user arrive at this problem?
- Steps: what are the 3–5 decisions they make?
- States: empty, in-progress, complete, error, edge cases
- Outputs: what does the user have at the end that they didn't have at the start?

Boxes and arrows, lo-fi sketches. Staff signals live here, not in the components.

### 30–50 min — Design the core flow

Pick the 1–2 screens where the core problem is solved. Not onboarding, not settings. The screen that carries the most weight.

Scope explicitly: "I'm focusing on X because that's where the core problem lives. Y and Z are real; I'll name them as deferred."

Annotations in the design are better than trying to cover every state. Label clearly: "happy path only — error states deferred" or "mobile not in scope."

**Hard constraint: by minute 35, you must have at least one real screen open, even if rough.** Systems thinking is your comparative advantage and your risk — under time pressure it can become too much framing and not enough artifact. The panel needs something tangible to react to. If you're still in flow diagrams at minute 35, stop and open a screen.

### 50–60 min — Stop and annotate

Add a Figma page labeled **"What I didn't build."**

- List 3–5 things you explicitly scoped out
- One-line reason for each
- Add: "If I had 2 more hours, I'd do X next, because..."

This is the Staff signal most candidates skip. Preempt the obvious scope objections — but leave room for discussion. Q&A is where Staff-level reasoning often becomes most visible; over-annotating everything makes the presentation defensive.

If time is short, inline scope notes beside the flow work equally well. The priority is that the reasoning is visible, not that it lives on a separate page.

---

## Hour 2 playbook — narrating to the panel

**Don't present the output. Present the thinking.**

Walk it in this order:

1. "Here's how I read the problem" — your framing, not the brief's framing. This is the Jonathan moment: user, goal, what failure costs them.
2. "Here's what I chose to solve" — the real problem you identified and why. Name what you deprioritized.
3. "Here's the structure I landed on before going to UI" — flows, decision points. This is for Alberto and Marta.
4. "Here's what I designed and why" — choices and explicitly, what you chose not to build.
5. "Here's what's missing" — what you'd do with more time, what's still risky, what you'd validate before shipping.

**On tradeoffs:** name them out loud even when they feel obvious. "The tradeoff was X vs. Y. I went with X because Z." Every explicit tradeoff is a Staff signal.

**On assumptions:** if you made a judgment call you're not sure about, say so. "I assumed the user would be in this context. If that's wrong, the solution changes in this way." That's not weakness — it's design reasoning.

---

## Staff signals checklist — hit these explicitly

- [ ] Scope clarification before output: "the brief asked for X, I interpreted it as Y, because..."
- [ ] Product outcome framing: "this matters because the user's actual problem is..."
- [ ] What you chose not to build, with stated reason
- [ ] What you'd validate before shipping more
- [ ] The meta-question: what would change if you had 2 weeks instead of 1 hour?

---

## Panel-specific adjustments

**Marta (Design Director):** She's seen you twice. She knows you can design. In hour 2 she's looking for whether the reasoning holds under follow-up. When she probes a decision, don't defend it — engage with the challenge. "That's a fair push. If I'd gone that route the tradeoff would have been..."

Likely question: "Why did you choose this as the MVP?" Answer with three axes: user pain (what friction this removes), business risk (what breaks if you don't solve it), and learning potential (what this reveals for v2). Don't answer with "it felt like the right scope."

**Alberto (Design Director, DS background):** Speak peer-to-peer. Don't over-explain design basics. He'll probe whether you thought about extensibility, states, and system implications beyond the happy path.

Likely question: "How does this scale when complexity grows?" Talk about the state model, reusable patterns, how the structure handles exceptions and permissions without breaking. This is where your DS background is an asset — think in terms of what compounds well.

**Jonathan (Growth, non-designer):** Frame in user outcomes and business terms throughout. "This step eliminates the back-and-forth between employee and manager that delays approval" lands. "I used a single-action pattern" does not.

Likely question: "How does this improve business outcomes?" Avoid design language entirely. Talk about reduced delays, fewer errors, operational efficiency, activation or retention. Connect the design decision to a cost the business is currently paying.

---

## Pre-challenge setup (tonight)

Prepare your Figma workspace before 10am tomorrow:

- Blank file with page labels pre-created:
  - `Problem framing`
  - `Core flow`
  - `Design`
  - `What I didn't build`
- A text block with the 5 clarifying questions pre-written — read them, pick the relevant ones, ask before touching Figma
- A text block with the 7 definition questions pre-written — paste and fill when the assignment lands
- A small component kit ready: form inputs, buttons, table rows, nav shell, status indicators. Don't spend time hunting for primitives under pressure.
- Close all other tabs and apps. One window: Figma. Notifications off.

---

## Salary position

The level is determined by this round.

- **If Senior:** €80K. Do not go lower. That is the Senior ceiling.
- **If Staff:** €93K opening. Do not drop to Senior pricing if they level you Staff.

If they ask about compensation during hour 2: "That depends on where this role sits in your framework — can you tell me whether you're thinking Senior or Staff?" Then quote the number for whatever they answer. Do not volunteer a number before level is clarified.

---

## If hour 1 goes sideways

Two failure modes. Know which one you're in.

**If you're still in framing at minute 35:** stop. Open a screen. A clear problem definition with one rough screen beats a perfect problem definition with no artifact. They need something tangible to discuss in hour 2.

**If you're deep in UI and losing the thread:** stop. Go back to the problem framing page and write one sentence about what you're actually solving and why. Polished screens that solve the wrong problem are worse than rough screens that solve the right one.

---

*After the challenge: run `/debrief-interview Factorial challenge` while it's fresh.*
