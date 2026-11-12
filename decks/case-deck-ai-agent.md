# Case Deck: AI Agent (Remuner)

**Figma:** no deck yet. Visuals per slide (flow, reach diagram, annotated conversation rebuilt from the Remu components, cycle diagram, outcome cards) still need building; see [context/ai-agent-notes.md](../context/ai-agent-notes.md). Build it in the Abacum DS v2 layout ([context/brand.md](../context/brand.md)).
**Best for:** Roles that name AI-assisted design or shipped AI product work. Trust, capability scoping and judgment under ambiguity. Pairs with a DS deck when a panel needs product breadth.
**Duration:** walk-through 10 to 12 minutes; leave the rest for questions. If time runs short, cut slides 2 (Context) and 3 (My role) to one sentence each before touching the proof slides (4, 6, 7, 8).
**Lead framing:** under pressure to ship an AI feature fast, I scoped it narrow and held that boundary through launch. Then a real failure, wrong numbers reaching customers, showed where the boundary ended.
**Effects:** candidate build when the deck exists: slide 7, one failure row per click.

Every claim is checked against [evidence/experience-facts.md](../evidence/experience-facts.md) ("Conversational AI agent") and [context/ai-agent-notes.md](../context/ai-agent-notes.md) (corrections 2026-07-14 to 2026-07-21). Speaker notes are beats, not a script.

**Ownership guardrails:**
- No PM on this project. Scope was decided by the CEO, CTO, engineering and me. Never say "with the PM".
- The agent calculated nothing. Wrong numbers came from custom client code it didn't know about.
- The orchestrator with one agent per vertical was engineering's decision and build. Describe it; never claim it.
- No adoption, satisfaction or accuracy metrics exist. Say so on the outcome slide before they ask.

---

## 1. Cover

**Headline:** An AI agent for questions about pay
**Sub:** Remuner · released to every customer before March 2026

**Notes:** Result first: I designed a production AI agent that answers sales reps' questions about their own commissions, and it shipped to every customer. Most of the work was deciding what it could answer.

---

## 2. Context

**Label:** Context
**Headline:** Reps had to find their answer across several screens
**Visual:** rep question → plan screen → calculation screen → payout screen → answer.

**Notes:** Leadership pushed for it and competitors were shipping similar features. Market response as much as user need.

---

## 3. My role

**Label:** My role
**Headline:** Interface, conversation design and what the agent could answer
**Visual:** three columns: Interface · Conversation design (tone, formats, vocabulary) · Capability scoping (answers, refusals).

**Notes:** Sole designer, no PM. I also set up the role-based context: managers saw their own and their team's plans, reps only their own.

---

## 4. Scope

**Label:** Scope
**Headline:** It answered commissions, plans and what-if scenarios only
**Visual:** two columns: Answers (commissions, plans, what-if payouts through the existing simulator) · Refuses (everything else, with a standard reply naming what it can answer).

**Notes:** A wrong guess about someone's pay costs more trust than a refusal. Launched narrow, with a written path for widening it.

---

## 5. Architecture

**Label:** Architecture
**Headline:** The agent read the platform's calculations
**Visual:** reach diagram: standard calculations, three vertical agents (plans, simulator, line items), orchestrator, chat surface. Custom client code drawn outside the boundary.

**Notes:** Engineering's design. A single agent had given inconsistent answers. Set up slide 7: the boundary held on the standard configuration only.

---

## 6. Answer anatomy

**Label:** Trust
**Headline:** The number first, then how it was built, then the plan rules
**Visual:** annotated conversation with three callouts: answer, derivation, plan rules.

**Notes:** Format followed the question: tables for line items, lists for breakdowns, a sentence for one figure. Lists and tables had already beaten paragraphs elsewhere in the platform, and we tested the formats in the prototype. Vocabulary per customer: deal, contract or item.

---

## 7. Where it broke (candidate build: one row per click)

**Label:** Where it broke
**Headline:** Wrong numbers came from code the agent couldn't see

| Failure | What happened | Where it sat |
|---|---|---|
| Wrong numbers | Custom client code the agent didn't know about; it answered from the standard calculation | System boundary |
| Comprehension | Correct number, plan too complex to follow | Explanation design |
| Data freshness | Stale ERP sync; the last-updated date was global and not shown in the chat | Never fully solved |

**Notes:** What changed after we found the custom-code cause is unknown. Don't guess.

---

## 8. Feedback loop

**Label:** After launch
**Headline:** We reviewed every answer each week
**Visual:** cycle: every question and answer captured → thumbs up or down → thumbs-down opens a text field → weekly review of the full record → format and tone changes shipped.

**Notes:** No ground truth for answer quality. An answer with no follow-up question and no thumbs-down counted as valid. That check came after launch; it didn't pick the formats.

---

## 9. Outcome

**Label:** Outcome
**Headline:** Shipped to every customer, with no adoption numbers
**Cards:** Released to every customer before March 2026 · Pre-release interviews: reps called it "a genuine tool to improve their work" · Weekly review steered format, tone and vocabulary · remuner.com/remu now presents the agent (extended after I left)

**Notes:** Say "no metrics" first, then the four cards.

---

## 10. Close

**Headline:** What would be most useful to go deeper on?

**Notes:** One sentence of lesson, then stop: most of the work was restraint.

---

## Speaker notes

No Figma deck exists yet, so these are keyed by slide number. When the deck is built, renumber them by Figma position and paste them by hand. Actions sit on their own line, starting with ▶ and in [brackets]. Don't read those lines aloud.

**Slide 1 (Cover)**
At Remuner I designed an AI agent that answers sales reps' questions about their own commissions. It shipped to every customer before I left in March 2026.
The risk was obvious: get a number wrong about someone's pay and they stop trusting the tool. So most of the design work was deciding what the agent could answer, how it showed its working, and what happened when a correct answer still confused people.

**Slide 2 (Context)**
Remuner sells sales compensation software. Reps could already see their commissions and plans in the platform, but a specific answer usually meant knowing which of several screens held it.
Leadership pushed hard for an agent, and competitors were shipping similar features, so this was a market response as much as a user need.
▶ [Short on time: one sentence.]

**Slide 3 (My role)**
I was the only designer, and there was no PM on this project. The CEO and CTO covered that with engineering and me. I owned the interface, the conversation design, meaning tone, answer formats and vocabulary, and the design side of what the agent could answer.
I also set up the role-based context: managers could ask about their own plans and their team's, and reps only about their own.
▶ [Never say "with the PM".]

**Slide 4 (Scope)**
We scoped the agent to commissions, compensation plans, and what-if payouts through the earnings simulator reps already used. Anything else got a standard reply that said what the agent could answer.
A wrong guess about someone's pay costs more trust than a refusal does, so refusing was the default outside that boundary. We launched narrow, with a written plan for widening it.

**Slide 5 (Architecture)**
The agent calculated nothing itself. It read results the platform had already calculated. Engineering ran a separate agent for each part of the app, plans, the simulator and line items, with an orchestrator routing each question. A single agent had given inconsistent answers, most likely because it had too much context to manage.
That was engineering's design, so I can explain why it existed, but it wasn't mine. Keep the diagram in mind for slide 7: the boundary held for every client on the standard configuration, and only there.

**Slide 6 (Answer anatomy)**
Every consequential answer had the same order. A rep asking what they're making this quarter got the figure first, then how it was calculated, then the plan conditions behind it. They could stop at the number or follow it down to the rule.
Format followed the question: tables for line items, lists for breakdowns, a sentence for a single figure. Lists and tables had already done better than paragraphs elsewhere in the platform, with users, and we tested the chat formats in the prototype before launch.
Vocabulary mattered more than I expected. The same object was a deal at one customer, a contract at another and an item at a third, and an agent that calls your deal an item sounds like it doesn't know your business. Adapting the terms per customer became a regular part of the iteration.

**Slide 7 (Where it broke)**
Feedback after release was mixed, and three problems drove most of the iteration.
▶ [Click, if built.]
First, wrong numbers, and most of them came from custom code. Some clients had requirements the product couldn't configure, so engineering had written custom calculations for them. The agent didn't know that code existed and answered from the standard path, so for those clients its numbers could be wrong.
▶ [Click.]
Second, comprehension. A correct number from a plan with tiers and multipliers can still confuse the person reading it. Most of the format and tone work went here.
▶ [Click.]
Third, freshness. When the ERP sync was hours behind, the agent gave a stale number and the rep saw a mismatch. The platform showed one global last-updated date, and the chat didn't show it at all. We never fully solved this in the chat. If I built it again, each answer would show how fresh its data was from the first release.
▶ [If asked what happened after the custom-code cause was found: it wasn't resolved before I left. Don't guess.]

**Slide 8 (Feedback loop)**
There was no ground truth for whether an answer was good. So the chat captured every question and answer, with thumbs up and down on each response. A thumbs-down opened a text field asking what went wrong. Every week we reviewed all of it, the full record as well as the flagged answers. An answer with no follow-up question and no thumbs-down counted as valid.
▶ [This check ran after launch. It didn't choose the formats.]

**Slide 9 (Outcome)**
I don't have adoption or satisfaction numbers. There was no instrumentation to produce them.
What I can point to: it shipped to every customer before March 2026. In pre-release interviews, reps called it a genuine tool to improve their work. The weekly review kept changing format, tone and vocabulary from real use. And remuner.com now has a page for the agent, though the team extended it after I left.
▶ [Say "no numbers" first.]

**Slide 10 (Close)**
Looking back, most of this work was restraint: what the agent may answer, what it admits it can't do, and how much working it shows before it asks for trust. The failure that hurt most came from a part of the system the agent couldn't see.
What would be most useful to go deeper on?
▶ [Stop talking.]

---

## Q&A preparation

**"What would you do differently?"** Show data freshness in each answer from the first release. And map the custom-code clients earlier, because that's where the accuracy risk was.

**"How do you know the scoping decision was right?"** Indirectly; there was no A/B test on the boundary. A wrong guess about someone's pay was the one failure we couldn't recover from cheaply, and launching narrow with a stated path avoided promising more than it could do.

**"Who else was involved and what was yours?"** No PM. The CEO and CTO acted as product owners; scope was decided between them, engineering and me. Engineering decided what data the agent could reach. Mine: the conversation design, the design side of the boundary and its refusal reply, the order of an answer (number, working, rules), the role-based context, and the format and tone changes from the weekly review. The orchestrator was engineering's.

**"What happened to the wrong-numbers problem?"** We found the cause. What changed after that wasn't settled before I left. Say that plainly.

**"Isn't ending on 'no metrics' weak?"** Each thing I can claim is checkable: it shipped to every customer, pre-release research backed it, the review loop ran on captured conversations, and the product has its own page on remuner.com.

**Don't claim:** adoption, satisfaction or accuracy figures; that you designed the orchestrator; that the follow-up check picked the formats; that the custom-code problem was fixed; a PM. The agent didn't generate rep letters; that was a separate feature.
