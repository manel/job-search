# Case Deck: Dataset Manager (Abacum)

**Best for:** Product design roles, research-driven decision-making, cross-functional alignment, decisions without a clear answer, changed approach mid-project.
**Duration:** 25–35 minutes including Q&A. Walk-through aim: 15–18 minutes.
**Lead framing:** Version C — Leadership hero. Not "I discovered the real problem" (research hero) or "I redesigned the abstraction layer" (architecture hero). The story is: I aligned product and engineering around a fundamentally different problem definition and sequenced delivery so we could reduce complexity without breaking what advanced users depended on.
**Editorial lens:** Every major moment must survive — "What specifically did Manel drive here that another senior designer probably would not?"

---

## Slide 1 — Cover

**Headline:** From technical configuration to self-serve onboarding

**Subheadline:** Dataset Manager — Abacum, 2022

**Speaker Notes:** This case is about a platform problem that looked like a UI issue but was actually a product architecture problem. Research changed the diagnosis. The harder work was reframing the scope with PM and engineering, then sequencing delivery so we could reduce complexity for users without breaking what advanced users relied on.

---

## Slide 2 — Business Context

**Headline:** Dataset configuration had become a scaling bottleneck

**Visual:** Dependency loop — Customer → Implementation team → Data setup → Product usage. Annotate the cost at each step: engineer hours, customer wait time, ceiling on how many customers the team could support.

**Speaker Notes:** Dataset Manager is what finance teams use to clean and structure raw data before it lands in a model: aggregate columns, apply lookups, trim values, set types. Every one of those tasks required an implementation engineer.

Abacum is a financial planning platform built on a configurable data layer. Before this project, customers depended heavily on implementation engineers or internal technical teams to configure datasets. Slow onboarding, expensive support, a hard ceiling on how many customers the team could take on.

I joined as the first dedicated designer on the integrations squad. No design context existed for this area. I had to build the problem understanding from scratch while staying on a delivery timeline.

---

## Slide 3 — Initial hypothesis

**Headline:** The assumption: the problem was usability

**Visual:** Screenshot or sketch of the existing dataset configuration interface. Two annotation layers: UI roughness AND conceptual mismatch, where the product exposed technical language finance users shouldn't have needed to see.

**Speaker Notes:** My initial read, before research, was that the interface was the problem. The configuration UI exposed technical concepts in ways that felt wrong. The assumption: fix the rough edges, and users could configure their own datasets.

I brought that hypothesis into the sessions expecting to validate it.

---

## Slide 4 — Research

**Headline:** Even expert users hit the same ceiling

**Visual:** Research participant grid — three participants, their tenure with the product, their technical background. Highlight the most experienced user. Note the specific task that failed and why it was the decisive signal.

**Speaker Notes:** Three task-based sessions, not interviews. Participants completed real configuration tasks; I watched where they got stuck.

The signal that mattered: the most experienced user, someone who had been using Abacum for over a year and was comfortable with the product, struggled with the same conceptual blocks as users who were new to it.

When the most experienced user hits the same wall as new users, the problem is not familiarity. More sessions would have added to the count, not the diagnosis. The question I needed to answer was whether experience with the interface closed the gap. One experienced user failing told me it didn't. The ceiling was in the model, not the interface.

---

## Slide 5 — Diagnosis

**Headline:** The product model didn't match the user's mental model

**Visual:** Two-column vocabulary map with matched pairs.

| Product language | Finance language |
|---|---|
| Schema | Dataset |
| Keys | Dimensions |
| Entities | Categories |
| Types | Metrics |

**Speaker Notes:** Users were being asked to work in the product's terms: data types, source schemas, entity keys. Finance teams thought in dimensions, metrics, cost centers.

That translation burden was the real source of friction, not the UI roughness I'd noticed going in. A better UI in the same model would have made the translation slightly easier. It wouldn't have removed it.

This changed what we needed to build.

---

## Slide 6 — Strategic pivot

**Headline:** A different problem entirely.

**Visual:** Before/after problem framing — left: "Simplify the interface," right: "Redesign the conceptual model." Show the scope difference: what each implies for engineering effort, timeline, and what gets built.

**Speaker Notes:** Every session returned the same finding. Users weren't stuck on the UI; they were stuck on the translation between product language and their own.

I kept naming that out loud every time direction came up. Not a single intervention. Same case, repeated, with new data each time until there was no other reading of it.

PM and engineering arrived at the same place. Scope changed — from a UI cleanup to a product architecture initiative.

---

## Slide 7 — The SQL decision

**Headline:** SQL would have worked. For the wrong users.

**Visual:** Tradeoff matrix.

| Option | Advantage | Risk |
|---|---|---|
| SQL | Fast to ship, familiar to technical users | Excludes core ICP; splits language model long-term |
| Abstraction layer | Scalable self-serve for the finance majority; consistent with modeling vocabulary | Harder to build, longer to ship |

Annotate: "who SQL serves" vs "who this product is for."

**Speaker Notes:** SQL was a reasonable call. Power users could configure datasets with it, and it would have shipped faster.

Two reasons I pushed back. First: it excludes the finance majority, the actual ICP. They don't think in SQL. Second: users already had formula syntax in the modeling layer. Adding SQL would have split the language model across the product — two ways to reach the same data.

We didn't avoid SQL entirely. When the formula-based approach wasn't ready, SQL was the interim step. Sequencing decision, not a change of direction.

The cost was real: power users stayed underserved for longer. That was the deliberate tradeoff. The PM wasn't wrong. He was solving for a different segment.

---

## Slide 8 — Delivery strategy

**Headline:** Progressive abstraction instead of big-bang replacement

**Visual:** Three-phase timeline with annotation under each phase.

Phase 1 — JSON editor: Preserve flexibility, protect advanced users, reduce migration risk
Phase 2 — Structured actions: Remove translation overhead for the finance majority
Phase 3 — Guardrails: Enable safe self-serve for configuration changes with downstream consequences

**Speaker Notes:** A full replacement would have broken workflows advanced users depended on. We also couldn't validate the abstraction without shipping something first.

I worked with the PM and lead engineer on the phased rollout. The sequencing logic was mine.

Phase 1: JSON editing. Preserve flexibility for advanced users, keep migration risk low.

Phase 2: structured actions. Take the translation burden off the finance majority.

Phase 3: guardrails. Some configuration changes have downstream effects. Users needed safety rails before we put those in their hands.

No phase extended until the previous one proved the abstraction worked.

---

## Slide 9 — Final product

**Headline:** Backend complexity abstracted into finance-native workflows

**Visual:** Before/after — raw JSON configuration on the left, Dataset Manager UI on the right. Annotate the vocabulary touchpoints: where "data type" became "dimension," where entity keys disappeared from the UI entirely. Make the abstraction layer visible, not just the aesthetic improvement.

**Speaker Notes:** The Dataset Manager abstracted the underlying configuration into workflows aligned with how finance teams already thought. Technical flexibility remained underneath; advanced users could still reach it. Complexity became optional rather than mandatory.

Not everything landed within the time I owned this squad. The formula-based transformation layer was the long-term direction but remained in progress when I moved to the engine squad after about eighteen months. The foundation was solid enough that work could continue without me.

The Modeling Syntax project I worked on after moving to the engine squad was part of the same thread — getting the language consistent across the product so the datasets layer could eventually build on top of it properly. The Dataset Manager created the need for that work. The two projects were connected, but in sequence, not in parallel.

---

## Slide 10 — Outcome

**Headline:** Self-serve onboarding became viable. A new product surface opened.

**Visual:** Four outcome cards.

- User: Customers completed standard configuration without requiring implementation support
- Operational: Implementation team reported roughly 50% reduction in setup time for common configurations
- Business: Reduced dependency increased onboarding throughput and shortened time to value
- Strategic: Editor suggestions shipped after this project made the configuration layer stable enough to build on.

**Speaker Notes:** No instrumented data. We didn't set a baseline before starting. If I did this again, I'd build a completion rate measurement into the research phase so the outcome was quantifiable.

User box: customers started completing standard configuration in a first session. Before this project, that required multiple handoffs to an implementation engineer.

Operational box: the implementation team's read was roughly half the time for standard setup. CS requests dropped in the following quarters. Their words, not a metric.

Business box: fewer engineering dependencies meant more customers moving through onboarding without a queue. Throughput up, time to value shorter.

Strategic box: this is the one I'd weight most. Intelligent editor suggestions were only viable once the configuration model was consistent enough for the system to reason about. Before this project, the underlying layer was too inconsistent to build on. Once it was clean, engineering had the foundation to ship that feature. That project existed because this one did first.

What made this hard wasn't the research or the vocabulary mapping. It was getting PM and engineering to change their read of the problem, then sequencing delivery so we could reduce complexity without breaking what existing users relied on. That's what I'd want someone to take away.

---

## Q&A preparation

**"What would you do differently?"**
Instrument the flow before starting. We had strong qualitative signals and clear operational outcomes, but no baseline. With a completion rate or time-on-task baseline, the outcome would have been quantifiable and the follow-on investment easier to justify. I'd build that into the research phase next time.

**"How did you validate the direction?"**
Task-based usability sessions with the prototype before finalizing the design. The signal was whether users could configure a dataset without translating into product language. When the most experienced user completed a task in a first session that had previously required implementation support, that was the validation.

**"How did you handle disagreement about SQL?"**
Made the case with evidence, not opinion. The research told us who the users were and how they thought. SQL required a mental model those users didn't have. The PM wasn't wrong to raise it; it just served a different segment than the one we needed to design for. Once that was clear, there wasn't much to disagree about.

**"Who else was involved and what was your specific contribution?"**
PM defined the business problem and held the stakeholder relationship. Engineering implemented and shaped technical feasibility. My contributions: identified the language mismatch through research, made the case against SQL, defined the conceptual model that became the Dataset Manager, co-defined the phased delivery strategy with the PM and lead engineer, ran usability sessions on the prototype.

**"Three sessions seems like a small sample."**
The confidence came from the specific signal, not the count. When the most experienced user struggled with the same conceptual blocks as new users, more sessions would have added to the count, not the diagnosis. The question I needed to answer was whether experience with the interface closed the gap. One experienced user failing told me it didn't.

**"How did you get PM and engineering aligned on the scope change?"**
It wasn't a single conversation. Every time we discussed direction, I connected what research was showing to what it meant for scope. The frame shifted gradually; not because I called a meeting, but because I kept making the same case with new evidence until there was no other reading of it.
