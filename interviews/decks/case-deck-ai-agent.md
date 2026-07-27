# Case Deck: AI Agent (Remuner)

**Best for:** Roles that name AI-assisted design or shipped AI product work as a qualification. Trust, capability scoping, and judgment-under-ambiguity narratives. Second case to pair with a DS deck when the portfolio needs product/discovery breadth, not just infrastructure.
**Duration:** 20-25 minutes including Q&A. Walk-through aim: 12-15 minutes.
**Lead framing:** Restraint hero. Not "I shipped an AI feature" (capability hero) or "I designed a chat UI" (craft hero). The story is: under competitive pressure to ship an AI feature fast, I made the call to scope it narrow and defend that boundary through launch, then used a real failure (a wrong number reaching a customer) to show what happens at the edge of that boundary and how the team responded.
**Editorial lens:** Every major moment must survive: "What did Manel decide here that a less careful designer would have skipped?" This case has no adoption or satisfaction metrics. Every slide earns its place on judgment, not on outcome.

**Ownership guardrails (do not drift from these in delivery):**
- No PM existed during this project. Never say "with the PM." Scope was decided between the CEO, CTO, engineers, and Manel.
- The agent computed nothing itself; it read the platform's own calculations. Wrong numbers came from custom client code the agent didn't know existed, not from agent reasoning errors.
- The multi-agent orchestrator architecture (one agent per vertical, routed by an orchestrator) was an engineering decision and build. Describe it, never claim authorship.
- No adoption, satisfaction, or accuracy metrics exist. Own this directly in the outcomes slide, do not wait for the question.

---

## Slide 1: Cover

**Headline:** An AI agent for questions about pay

**Subheadline:** AI Agent | Remuner, released before March 2026

**Speaker Notes:** This case is about designing the boundary around an AI feature before designing the feature itself. Remuner had to ship an AI-assisted way for sales reps to ask about their own commissions. The obvious risk: get a number wrong about someone's pay and lose their trust in the tool permanently. Most of the design work was deciding what the agent could answer, how it showed its reasoning, and what happened when a correct answer still confused the person reading it.

---

## Slide 2: Business context

**Headline:** The most sensitive number in the product, buried across screens

**Visual:** Simple flow: Rep question -> plan screen -> calculation screen -> payout screen -> answer. Annotate each hop with "screen the rep had to find."

**Speaker Notes:** Remuner sells sales compensation software. Reps could already see their commissions and plan setup in the platform; the problem was reaching a specific answer, which usually meant knowing which of several screens held it.

The team had been improving those screens step by step. The faster route was letting reps ask in plain language and skip the navigation entirely. Leadership pushed hard for this, and competitors were shipping similar features, so this was a market response as much as a user need. I was sole designer at Remuner throughout, no PM on this project; the CEO and CTO covered that ground alongside engineering and me.

---

## Slide 3: My role

**Headline:** Interface, conversation design, and where the answer stops

**Visual:** Three labeled columns: Interface / Conversation design (tone, formats, vocabulary) / Capability scoping (what it answers, what it refuses).

**Speaker Notes:** I owned the interface, the conversation design, and the design side of capability scoping. Conversation design meant the tone of answers, the formats they rendered in, the vocabulary they used. Scoping meant drawing the boundary of what the agent was allowed to respond to and writing the plan for widening it over time.

This is the frame for the whole case: most of the design work here happened before any chat interface existed, in deciding what the agent was allowed to say.

---

## Slide 4: The scoping decision

**Headline:** Commissions, plans, and what-if scenarios. Nothing else.

**Visual:** Two columns. Left: "Answers" (commissions, compensation plans, what-if payout scenarios via the existing simulator). Right: "Refuses" (everything else, standard refusal naming what it can answer instead).

**Speaker Notes:** The first design decision was which questions the agent would answer and which it would refuse. We scoped it to commissions, compensation plans, and what-if payout scenarios using the earnings simulator reps already had in the product. Nothing else. Any question outside that got a standard refusal telling the rep what the agent could answer, instead of an improvised reply.

The reasoning: a wrong guess about someone's pay costs more trust than any refusal does. So refusing was the default for everything outside the boundary, not an edge case we patched later. The narrow launch scope shipped with a written release path for widening the answerable set over time.

---

## Slide 5: The architecture boundary

**Headline:** The agent read the platform's answers. It never calculated its own.

**Visual:** Reach diagram. Inside the boundary: platform standard calculations, three vertical agents (Plans, Simulator, Items), an orchestrator routing questions to the right one, the chat surface. Outside the boundary, drawn explicitly separate: custom-coded client calculations.

**Speaker Notes:** The second boundary was about what the agent was allowed to compute. It calculated nothing itself; it read results the platform had already computed. Behind the conversation, engineering ran a separate agent per vertical of the app, plans, the simulator, line items, with an orchestrator routing each question to the right one. A single agent had produced inconsistent answers, most likely from the amount of context it had to manage. That architecture was engineering's decision and build; I can describe why it existed, I didn't design it.

The diagram matters for the next slide. The boundary held for every client on the standard configuration. It didn't hold everywhere.

---

## Slide 6: Trust: the anatomy of an answer

**Headline:** The number first. Then how it was built. Then the rules behind it.

**Visual:** Annotated conversation screenshot (rebuilt from the Remu Figma components), three callouts: the answer, the derivation, the plan rules and context.

**Speaker Notes:** Every consequential answer had the same structure. A rep asking how much they're making this quarter got the figure immediately, with the calculation detail and the relevant plan conditions underneath. They could stop at the number or follow it down to the rule that produced it. The answer led; the evidence sat underneath it.

Format followed the question: line items as tables, breakdowns as lists, single figures as a sentence. That wasn't guessed. Lists and tables already outperformed paragraphs elsewhere in the platform, validated with users there, and we tested the same pattern directly with users in the chat prototype before launch.

Vocabulary mattered more than expected. The same object was a "deal" at one customer, a "contract" at another, an "item" at a third. An agent that calls your deal an item reads as a tool that doesn't know your business. Adapting terminology per customer became a standing part of the iteration loop, not a one-time fix.

---

## Slide 7: Where it broke

**Headline:** Three failure modes. None of them were the agent reasoning wrong.

**Visual:** Three-row table.

| Failure | What happened | Where it sat |
|---|---|---|
| Wrong numbers | Custom client code the agent didn't know existed; it answered from the standard calculation path | System boundary |
| Comprehension | Correct number, plan too complex to parse without help | Explanation design |
| Data freshness | Stale ERP sync; last-updated date existed but was global, not shown in the conversation | Never fully solved |

**Speaker Notes:** Feedback after release was mixed, and three problems drove most of the iteration work.

The first: wrong numbers, and most traced back to custom code. Some clients had requirements the product's front end couldn't configure, so engineering had written custom calculations for them. The agent didn't know that code existed and answered from the standard path, so for those clients its numbers could be wrong. Reading the platform's own calculations protected accuracy only as far as the standard configuration reached. That's the honest version of "what happens when the AI is wrong": the agent was blind to a part of the system nobody had told it about.

The second: comprehension. A correct number from a plan with tiers and multipliers can still confuse the person reading it. This drove most of the format and tone work, trying different ways to show the calculation until the explanation landed.

The third: data freshness. When ERP data was hours stale, the agent reported a stale number and the rep saw a mismatch. The platform had a last-updated date, but globally, not inside the conversation where reps actually hit the problem. We never fully solved this inside the chat. If I built this again, answer-level freshness would be in the first release, not an afterthought.

---

## Slide 8: The feedback loop

**Headline:** No ground truth for answer quality, so we instrumented behavior instead

**Visual:** Cycle diagram: every question and answer captured -> thumbs up/down -> thumbs-down opens a text field -> weekly review against the full record -> format and tone changes shipped back in.

**Speaker Notes:** There was no ground truth for whether an answer was good. So the chat captured every question and answer the agents produced, with thumbs up and down on each response. A thumbs-down opened a text field asking what went wrong. All of it, not just flagged answers, was reviewed weekly against the full record. An answer with no follow-up question and no thumbs-down counted as valid.

This is the operational governance layer of the case, the same signal class as a recurring cross-functional review cadence in a mature design system. It shows the team kept steering the agent after launch instead of moving on to the next feature.

---

## Slide 9: Outcomes

**Headline:** No adoption numbers. Here's what I can stand behind.

**Visual:** Four outcome cards, not an artifact list.

- Released to every Remuner customer before March 2026
- Pre-release interviews: reps described it as a genuine tool for their work, not a novelty
- The post-release loop steered format, tone, and per-customer vocabulary from real usage signal, not from opinion
- The agent is now the headline of remuner.com; the team extended it after I left, but the question-answering core is what this case describes

**Speaker Notes:** I can't claim adoption or satisfaction numbers from my tenure at Remuner, there was no instrumentation in place to produce them, and I'm not going to imply otherwise. What I can stand behind: it shipped to every customer, pre-release research backed the concept, the iteration loop was real and ran on captured evidence, and the product it became is now the company's lead marketing surface. That last point is a checkable signal, not a metric, and I phrase it carefully: it evolved after I left.

---

## Slide 10: Closing

**Headline:** Shipping this agent was mostly a sequence of restraint decisions

**Visual:** Single line, no image.

**Speaker Notes:** Shipping an AI feature under competitive pressure came down to a sequence of restraint decisions: what it's allowed to answer, what it admits it can't do, how much of its reasoning it shows before asking for trust. The failure that mattered most, the custom-code blind spot, was a systems-boundary problem: the agent's model of the product didn't cover every client's reality. That's the same kind of thinking I'd use to scope a design system. Here it showed up in a conversation instead of a component library.

---

## Q&A preparation

**"What would you do differently?"**
Answer-level freshness in the first release, not an afterthought. The platform's global last-updated date didn't help a rep looking at a stale number inside the conversation. I'd also push earlier to get the custom-code blind spot mapped, since that's where the real accuracy risk lived, not in the agent's reasoning.

**"How do you know the scoping decision was right?"**
Indirectly. No A/B test on the boundary itself. The signal was structural: launching narrow with a stated release path avoided the failure mode of promising broad capability and patching trust damage after the fact. The alternative, a wrong guess about someone's pay, was the one failure we couldn't recover from cheaply.

**"Who else was involved, what was your specific contribution?"**
No PM on this project. The CEO and CTO acted as product owners; scope was decided between them, engineering, and me. My contribution: the conversation design (tone, formats, vocabulary), the design side of the capability boundary and its refusal pattern, the trust architecture of an answer (number, derivation, context), and running the format/tone iteration off the weekly feedback review. The multi-agent orchestrator was engineering's design and build, not mine; I describe it because it explains the failure mode, not because I claim it.

**"What happened to the wrong-numbers problem after you found the cause?"**
Open. The custom-code blind spot was identified as the cause; what changed operationally after that, whether the agent was made aware of custom logic or affected clients got a disclaimer, wasn't resolved before I left Remuner. Say this plainly if asked, don't guess at a resolution.

**"Isn't 'no metrics' a weak place to end?"**
Reframe: the absence of a false metric is more honest than a decorated one. What's checkable is that it shipped to every customer, that pre-release research backed the concept, and that the product is now the company's flagship page. Those are real, verifiable signals. Inventing a completion rate or satisfaction score would be the actual weak move.
