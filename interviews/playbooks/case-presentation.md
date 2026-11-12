# Case presentation round

This section assumes a 30-45 minute format: walk us through a project, then Q&A. Deck sources are in [decks/](../../decks/); the story behind each deck is in [stories.md](../stories.md).

## Story selection

Lead with the case that matches the company's context. Use the same mapping from [context/positioning.md](../../context/positioning.md):
- DS-first roles: Remuner DS (CTO quote is the credibility anchor), `remuner-ds`
- Product roles with DS: Abacum Dataset Manager, `dataset-manager`
- Fintech: Modeling Syntax, `modeling-language`
- Founding designer: breadth narrative across both companies

Don't try to cover everything. One case, deep, is more effective than three cases shallow.

## Structure that works

1. Context (60 seconds): company, team, my role, the surface problem
2. The real problem (90 seconds): what research or investigation showed the real constraint was
3. The decision (2 minutes): what you chose to do and why. What you chose NOT to do and why. The "why not" is often more interesting than the "why."
4. The work (3-4 minutes): what was actually designed. Show the process, not just the output. Failure states, iterations, constraints.
5. Outcome (90 seconds): what shipped, what changed, what you'd do differently. Own absence of metrics directly.

## Q&A what to expect

- "How did you handle disagreement in the team?"
- "What would you do differently?"
- "How did you validate the direction?"
- "Who else was involved and what was your specific contribution?"
- "How did this connect to business outcomes?"

The last one is the hardest if you don't have hard metrics. Answer: here is the qualitative signal, here is why it mattered, here is why I don't have a number, here is the proxy I would use.

---

## Rules for every case deck

Added 2026-11-08, from Reddit advice on presenting to execs and hiring managers, applied first to the Wizeline client round.

- **Result first.** The first sentence on the cover gives the outcome: what you did and what it reached, using a figure from the register. The outcome slide near the end still closes on it. The listener should know in the first minute what you did and why it mattered.
- **Talk for 10 to 12 minutes, then let them steer.** In a 30 or 60 minute slot, keep the walk-through short and end on a question: "What would be most useful to go deeper on?" Then stop talking. Cut setup slides to one or two sentences before cutting proof.
- **Use their words.** Turn each JD sentence into a "tell me about a time when" prompt and check that a slide or beat answers it. Say the company's own terms (product names, system names, values in the JD) wherever they are true for your work.
- **Follow what they ask for.** If they want a flow, a screen or the Figma file, go there straight away instead of finishing the slides (Wizeline Round 2, 2026-10-30).
- **One source format.** Every deck source in `decks/` follows [decks/case-deck-design-systems-abacum.md](../../decks/case-deck-design-systems-abacum.md) (adopted 2026-11-09): a header block (Figma, Best for, Duration with what to cut first, Lead framing, Effects, evidence line); numbered slides with Label, Headline, Visual and short Notes beats; a full speaker-notes section keyed by Figma position, with ▶ [action] lines; Backup; a short Q&A ending in "Don't claim". Decks with no Figma build key the notes by slide number until they are built.
- **Portfolio on top of the deck.** When a round asks to "show your portfolio" as well, show the curated Figma file "Manel Leiva Portfolio Highlights", not the website or raw working files ([memory.md](../../memory.md), 2026-11-09).

## Staff-level signals checklist

Run this against any deck before a Senior Staff or Staff-level interview. A deck that only passes Senior checks reads as "strong executor." A deck that passes these reads as "strategic operator." The written-case version is in [context/portfolio.md](../../context/portfolio.md).

**1. Opening frame**
The first sentence gives the result (see "Rules for every case deck"). The rest of the first 60 seconds must signal: ambiguity + leverage + strategic allocation. Not domain or craft. The opening is not "here is the design system work I did." It is "here is a case that reflects how I decide where design investment creates the most leverage in an under-resourced environment." If you wouldn't open with those words, rewrite the first slide.

**2. Constraint framing**
Constraints must read as strategic, not operational. "I was the only designer" is a capacity note. "Bandwidth was a strategic allocation problem — every infrastructure investment competed with revenue-generating product work" is a Staff signal. Visualise the tension: product delivery vs. system quality vs. team scalability. Impossible to maximise all three simultaneously. Naming that tension explicitly is what separates a senior who navigated constraints from a Staff who managed them deliberately.

**3. Prioritisation as a section, not an afterthought**
Show the decision framework: what criteria drove what got built, deferred, or escalated. Three-axis model that works: business impact (does this accelerate delivery or reduce repeated engineering effort?), dependency pressure (is complexity compounding? will delay increase cost?), user pain (is inconsistency causing visible friction?). Include a concrete table — at minimum 3–4 decisions with outcomes. This slide alone is the missing Staff signal in most portfolios.

**4. Show restraint explicitly**
"What I chose NOT to build" deserves its own callout — a section header, a table column, or a dedicated annotation. Deferred decisions with stated reasoning are evidence of judgment. Without this, the deck reads as a build log. With it, it reads as a resource allocation record.

**5. Surface PM-like behaviours**
Tickets created, backlog participation, sprint prioritisation discussions, system debt treated as first-class roadmap items alongside product features — these must appear explicitly, not be implied. Make the influence chain visible: observation → framing → ticket → sprint prioritisation → roadmap impact. If you shaped what got built, not just how it looked, that chain must be traceable in the deck.

**6. Outcome buckets over artifact lists**
Replace "here is what I shipped" with four outcome categories:
- Product velocity: what repeated work was eliminated
- Engineering consistency: what previously implicit decisions became enforceable
- Team scalability: what got faster or cheaper to onboard
- Organisational behaviour: what changed in how the team plans, not just what it ships

The last one is the hardest to fill but the strongest Staff signal. "Infrastructure became part of planning, not ad hoc cleanup" is not a technical outcome — it is an organisational outcome. That is what Staff designers produce.

**7. Closing meta-lesson**
End with the underlying tradeoff, not the artifact. Not "I built a design system." Not "adoption was high." Something like: "The biggest lesson wasn't about component architecture — it was learning how to continuously balance short-term delivery against long-term leverage. That tradeoff is, in practice, a core part of this kind of work." The meta-lesson signals you understand what the role actually is.

**8. No hard metrics — own it proactively**
Don't wait to be asked about numbers. Name the proxies confidently in the deck itself: qualitative signals, operational signals (what got unblocked), and the CTO/stakeholder observation if available. If pressed: "I didn't have instrumentation in place to measure it. What I can point to is what the work made possible." Never apologise. Frame it as a startup reality and move on.

**9. Keep a second non-DS story ready**
If the primary case is infrastructure-heavy, a Design Director will probe for product discovery, user research, or ambiguity navigation. Prepare one non-DS case beat — a messy workflow problem, a research-driven direction change, a business tradeoff. This prevents being read as "infrastructure specialist" when the role requires product breadth.
