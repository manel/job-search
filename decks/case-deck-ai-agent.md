# Case Deck: AI Agent (Remuner)

**Figma:** https://www.figma.com/design/hvBKW3kVMBdUB8vVnsNjRU/AI-agent. v2 built 2026-11-16 in the top row (13 slides; the slide 7 build is four slides), in the Abacum DS v2 layout ([context/brand.md](../context/brand.md)), with no on-slide notes. All visuals are native Figma layers: the slide 5 reach diagram follows the portfolio's `ai-agent-reach.svg`, and the slide 6 conversation follows `ai-agent-hero.png`, with the same made-up figures. The July draft sits in the second row, skipped, until v2 is approved. Its headlines don't match this file and its slide 9 card adds "not a novelty" to the quote, so don't present it.
**Best for:** Roles that name AI-assisted design or shipped AI product work. Trust, capability scoping and judgment under ambiguity. Pairs with a DS deck when a panel needs product breadth.
**Duration:** walk-through 10 to 12 minutes; leave the rest for questions. If time runs short, cut slides 2 (Context) and 3 (My role) to one sentence each before touching the proof slides (4, 6, 7, 8).
**Lead framing:** under pressure to ship an AI feature fast, I scoped it narrow and held that boundary through launch. Then a real failure, wrong numbers reaching customers, showed where the boundary ended.
**Effects:** slide 7 is a build: duplicate slides with identical layer names, Smart Animate 0.3s ease-out. The table header shows first, then one failure row per click.

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
**Visual:** a rep's question → plan screen → calculation screen → payout screen → the answer.
**Footer:** The data was already in the platform. Reps had to know which screen held it.

**Notes:** Leadership pushed for it and competitors were shipping similar features. Market response as much as user need.

---

## 3. My role

**Label:** My role
**Headline:** Interface, conversation design and what the agent could answer
**Visual:** three cards. Interface: one global chat panel, not tied to the screen the rep was on. Conversation design: tone, answer formats and vocabulary for each customer. Capability scoping: what the agent answers, what it refuses, and the plan to widen it.
**Footer:** Sole designer. No PM: the CEO and CTO set scope with engineering and me.

**Notes:** Sole designer, no PM. I also set up the role-based context: managers saw their own and their team's plans, reps only their own.

---

## 4. Scope

**Label:** Scope
**Headline:** It answered commissions, plans and what-if scenarios only
**Visual:** two cards. Answers: commissions, compensation plans, what-if payouts through the simulator reps already used. Refuses: everything else, with a standard reply that names what the agent can answer.
**Footer:** Launched narrow, with a written plan for widening it.

**Notes:** A wrong guess about someone's pay costs more trust than a refusal. Launched narrow, with a written path for widening it.

---

## 5. Architecture

**Label:** Architecture
**Headline:** The agent read the platform's calculations
**Visual:** reach diagram. Inside a dashed boundary ("What the agent could read"): chat → orchestrator → plans, simulator and items agents → standard calculations, with the line "The agents calculated nothing. They read results the platform had already calculated." Outside it: custom client code ("Per-client calculations the product couldn't configure").

**Notes:** Engineering's design. A single agent had given inconsistent answers. Set up slide 7: the boundary held on the standard configuration only.

---

## 6. Answer anatomy

**Label:** Trust
**Headline:** The number first, then how it was built, then the plan rules
**Visual:** a Remu chat panel answering "How much am I making this quarter?" (6.360,00 €, a four-line breakdown, then the plan rule), with three callouts: the answer first, how it was built, the plan rules. Caption: "Example conversation. The data is made up."

**Notes:** Format followed the question: tables for line items, lists for breakdowns, a sentence for one figure. Lists and tables had already beaten paragraphs elsewhere in the platform, and we tested the formats in the prototype. Vocabulary per customer: deal, contract or item.

---

## 7. Where it broke (build: header, then one row per click)

**Label:** Where it broke
**Headline:** Wrong numbers came from code the agent couldn't see

| Failure | What happened | Where it sat |
|---|---|---|
| Wrong numbers | Custom client code the agent didn't know about. It answered from the standard calculation. | System boundary |
| Comprehension | The number was correct, but the plan was too complex to follow | Explanation design |
| Data freshness | Stale ERP sync. The last-updated date was global and not shown in the chat. | Never fully solved |

**Notes:** What changed after we found the custom-code cause is unknown. Don't guess.

---

## 8. Feedback loop

**Label:** After launch
**Headline:** We reviewed every answer each week
**Visual:** five numbered steps with a return arrow: every question and answer captured → thumbs up or down on each answer → a thumbs-down opens a text field → weekly review of the full record → format and tone changes shipped.

**Notes:** No ground truth for answer quality. An answer with no follow-up question and no thumbs-down counted as valid. That check came after launch; it didn't pick the formats.

---

## 9. Outcome

**Label:** Outcome
**Headline:** Shipped to every customer, with no adoption numbers
**Cards:** Released to every customer before March 2026 · In pre-release interviews, reps called it "a genuine tool to improve their work" · The weekly review steered format, tone and vocabulary · remuner.com/remu now presents the agent. The team extended it after I left.

**Notes:** Say "no metrics" first, then the four cards.

---

## 10. Close

**Headline:** What would be most useful to go deeper on?

**Notes:** One sentence of lesson, then stop: most of the work was restraint.

---

## Speaker notes

The Figma plugin API can't write Slides speaker notes, so paste these by hand. "Figma N" is the slide's position in the v2 row (13 slides; the slide 7 build is four slides). Rewritten for speech 2026-11-16 ([interviews/playbooks/case-presentation.md](../interviews/playbooks/case-presentation.md#writing-for-speech)). Each sentence sits on its own line. Actions sit on their own line too, starting with ▶ and in [brackets]. Don't read those lines aloud.

**Figma 1 (Cover)**

At Remuner, I designed an AI agent that answers sales reps' questions about their own commissions.

It shipped to every customer before I left in March 2026.

If it got a number about someone's pay wrong, the rep would stop trusting the tool.

So most of the design work was deciding three things.

First, what the agent could answer.

Second, how it showed its working.

Third, what happened when a correct answer still confused people.

**Figma 2 (Context)**

Remuner sells sales compensation software.

Reps could already see their commissions and plans in the platform.

But to get a specific answer, they had to know which of several screens held it.

Leadership pushed hard for an agent, and competitors were shipping similar features.

So this was a market response as much as a user need.

▶ [Short on time: one sentence.]

**Figma 3 (My role)**

I was the only designer, and there was no PM on this project.

The CEO and CTO covered that, together with engineering and me.

I owned the interface and the conversation design: tone, answer formats and vocabulary.

I also owned the design side of what the agent could answer.

And I set up the role-based context.

Managers could ask about their own plans and their team's.

Reps could only ask about their own.

▶ [Never say "with the PM".]

**Figma 4 (Scope)**

We scoped the agent to three topics.

First, commissions.

Second, compensation plans.

Third, what-if payouts through the earnings simulator that reps already used.

Anything else got a standard reply that said what the agent could answer.

A wrong guess about someone's pay costs more trust than a refusal.

So outside those topics, the agent refused by default.

We launched narrow, with a written plan for widening it.

**Figma 5 (Architecture)**

The agent didn't calculate anything itself.

It read results the platform had already calculated.

Engineering ran a separate agent for each part of the app: plans, the simulator and line items.

An orchestrator sent each question to the right one.

They split it up because a single agent had given inconsistent answers.

Most likely, it had too much context to manage.

Keep this diagram in mind for slide 7.

The boundary held for every client on the standard configuration, and only there.

▶ [If asked who designed it: engineering did. I can explain why it existed.]

**Figma 6 (Trust)**

Every important answer had the same order.

Say a rep asks what they're making this quarter.

They get the figure first, then how it was calculated, then the plan conditions behind it.

They can stop at the number, or follow it down to the rule.

The format followed the question.

Line items got a table, breakdowns got a list, and a single figure got a sentence.

Lists and tables had already worked better than paragraphs in other parts of the platform.

And we tested the chat formats in the prototype before launch.

Vocabulary mattered more than I expected.

The same object was a deal at one customer, a contract at another and an item at a third.

If an agent calls your deal an item, it sounds like it doesn't know your business.

So we adapted the terms for each customer, and we kept adjusting them after launch.

**Figma 7 (Where it broke)**

Feedback after release was mixed.

Three problems drove most of the changes.

▶ [Click.]

**Figma 8**

First, wrong numbers, and most of them came from custom code.

Some clients needed things the product couldn't configure.

So engineering had written custom calculations for them.

The agent didn't know that code existed, and it answered from the standard calculation.

So for those clients, its numbers could be wrong.

▶ [Click.]

**Figma 9**

Second, comprehension.

A correct number from a plan with tiers and multipliers can still confuse the person reading it.

Most of the format and tone work went here.

▶ [Click.]

**Figma 10**

Third, freshness.

When the ERP sync was hours behind, the agent gave an old number, and the rep saw a mismatch.

The platform showed one global last-updated date, and the chat didn't show it at all.

We never fully solved this in the chat.

If I built it again, every answer would show how fresh its data is, from the first release.

▶ [If asked what happened after the custom-code cause was found: it wasn't resolved before I left. Don't guess.]

**Figma 11 (After launch)**

We had no ground truth for whether an answer was good.

So the chat saved every question and answer, with a thumbs up and a thumbs down on each one.

A thumbs-down opened a text field that asked what went wrong.

Every week, we reviewed all of it: the full record, and the flagged answers too.

If an answer got no follow-up question and no thumbs-down, we counted it as valid.

▶ [This check ran after launch. It didn't choose the formats.]

**Figma 12 (Outcome)**

I don't have adoption or satisfaction numbers.

There was no instrumentation to produce them.

Here's what I can point to.

First, it shipped to every customer before March 2026.

Second, in pre-release interviews, reps called it "a genuine tool to improve their work".

Third, the weekly review kept changing format, tone and vocabulary, based on real use.

Fourth, remuner.com now has a page for the agent, though the team extended it after I left.

▶ [Say "no numbers" first.]

**Figma 13 (Close)**

Looking back, most of this work was restraint.

I had to decide what the agent may answer, and what it admits it can't do.

I also had to decide how much working it shows before it asks for trust.

And the failure that hurt most came from a part of the system the agent couldn't see.

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
