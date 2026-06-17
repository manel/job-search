# Case Deck: Dataset Manager (Abacum)

**Best for:** Product design roles, roles that emphasize research-driven decision-making, any interview asking about changed approach mid-project or making decisions without a clear answer.
**Duration:** 25-35 minutes including Q&A. Walk-through aim: 15-18 minutes.
**Lead framing:** Research changed the diagnosis, not just the solution. The interesting decision was recognizing that the original problem statement was wrong, and that the PM's proposed alternative served a different set of users than the ones we needed to serve.

---

## Slide 1 — Cover

**Headline:** When research changes the problem

**Subheadline:** Abacum, 2022 — Dataset Manager, Integrations squad

**Speaker notes:**
This case is about a project where the initial hypothesis was wrong, but not in the obvious way. It only became clear when I sat with real users and watched them work. I'll walk you through how the research changed the direction, the decision about SQL that followed from it, and what we built as a result.

---

## Slide 2 — Context

**Headline:** Finance teams couldn't configure their own data

**Visual:** Before-state diagram: finance user → asks for help → implementation team configures data → result delivered. Dependency loop annotated.

**Speaker notes:**
Abacum is a financial planning product. At the core is a data layer: companies connect their source data, configure how it maps into Abacum's models, and build their financial plans on top of that.

The problem in the integrations squad: finance teams couldn't do that configuration themselves. They had to go through Abacum's implementation team, or their own technical staff, every time they needed to adjust their data setup. For Abacum, that meant a paid implementation engineer's time on every configuration request, a delay to the customer's time-to-value, and a hard ceiling on how many customers the team could support without hiring more people. CS and implementation were handling work that should have been self-serve.

I joined as the first dedicated designer on this squad.

---

## Slide 3 — Initial hypothesis

**Headline:** The product needed a better UI

**Visual:** Screenshot or sketch of the existing dataset configuration interface. Rough edges annotated.

**Speaker notes:**
My initial read, before research, was that the interface was the problem. The configuration UI had rough edges. It exposed technical concepts in ways that didn't feel natural. It seemed like a UX problem: better labels, clearer affordances, a more guided flow, and users could configure their own datasets.

This is the hypothesis I brought into the research sessions.

---

## Slide 4 — Research

**Headline:** Three user sessions. The most experienced user struggled with the same concepts as new users.

**Visual:** Research participant grid: three participants, their tenure with the product, their technical background. Highlight on the most experienced user.

**Speaker notes:**
I ran structured user tests with three participants. Not surveys, not interviews. Task-based sessions where participants tried to configure a dataset and I watched where they got stuck.

The detail that mattered: the most experienced user, someone who had been using Abacum for over a year and was comfortable with the product, struggled with the same conceptual blocks as users who were new to it.

Three sessions is a small sample. What made it defensible: when the most experienced user hits the same wall as new users, it tells you this isn't a familiarity problem. More sessions would have added to the count, not the diagnosis. The signal I needed was whether the ceiling on improvement was the interface or the model underneath it. One experienced user failing told me it was the model.

When an experienced user hits the same wall as a new user, the wall isn't in the UI. It's in the model underneath the UI.

---

## Slide 5 — What the research showed

**Headline:** A language mismatch between how the product thought and how users thought

**Visual:** Two columns: Product language on the left (data types, keys, sources, entities) vs User language on the right (dimensions, metrics, rows, categories). Examples from the sessions.

**Speaker notes:**
The research sessions made the actual problem clear. The product asked users to think in product terms: data types, source schemas, entity keys. Finance teams didn't think that way. They thought in their own vocabulary: dimensions, metrics, revenue lines, cost centers.

Every time a finance user tried to configure a dataset, they were doing a mental translation between their domain language and the product's language. That translation was where they failed. Not because they were unsophisticated. The product was asking them to do a job they shouldn't have to do.

This is not a UI problem. A better UI in the same model makes the translation slightly easier, but it doesn't remove it.

---

## Slide 6 — The turn

**Headline:** The product needed to speak their language, not the other way around

**Speaker notes:**
The conclusion from research: we needed to introduce a conceptual layer that matched how finance teams already thought about data. Not "simplify the technical interface." Restructure the interface around a different, user-native model.

This was a bigger call than a visual redesign. It meant changing the mental model the product offered users, not just the layout of the existing one. That required buy-in from engineering and PM, because the scope was different from what they'd expected.

---

## Slide 7 — The SQL question

**Headline:** SQL would have worked. For the wrong users.

**Visual:** Two user segments: power users (small segment, high technical literacy) vs the majority of finance users (primary segment, non-technical). SQL coverage vs extended syntax coverage diagram. The segments are annotated: "who SQL serves" vs "who this product is for."

**Speaker notes:**
The PM and some stakeholders raised SQL support as a solution. It was a reasonable suggestion: SQL is expressive, power users could use it, it would solve the configuration problem for the technically inclined.

I made the case against it. SQL would have worked for a segment of users who were already finding workarounds with the existing interface. For the majority, the finance professionals who are the actual ICP and don't think in SQL, it would have raised the floor while doing nothing for the ceiling.

The argument was made with the research evidence: here is who the users are, here is how they think about data, here is what SQL requires them to know. Not "SQL is bad," but "SQL is wrong for these users."

The cost of saying no was real: power users stayed underserved for longer. That was a deliberate tradeoff. Building SQL would have served 10% of users while making the core interface harder for the other 90% — because the interface would have had to accommodate both paradigms at once.

The PM's hypothesis wasn't wrong. It was answering a different question.

---

## Slide 8 — What we built

**Headline:** A UI abstraction layer over JSON configuration, using vocabulary finance teams already knew

**Visual:** Before/after: raw JSON configuration on the left, the Dataset Manager UI on the right with finance-native terminology. Key UI patterns annotated.

**Speaker notes:**
We built the Dataset Manager: a UI that abstracted over the underlying JSON configuration and surfaced it through concepts finance teams already used. Dimensions. Metrics. Clear categories. No data types exposed unless the user needed to see them.

The Modeling Syntax work from the engine squad was a prerequisite: before the Dataset Manager could abstract over it cleanly, the syntax underneath needed to be consistent. That dependency shaped the sequencing and required coordination across squads.

The release was incremental, driven by technical constraints. V1 covered the most common configuration patterns. Edge cases — complex source mappings and multi-level hierarchies — were deferred deliberately. We needed to validate that the core abstraction worked before extending it into the harder cases. That was the right call, not a compromise. It let us validate each layer with real users before building the next.

---

## Slide 9 — Outcome

**Headline:** Follow-on work became possible. Configuration became autonomous. Implementation overhead dropped.

**Visual:** Three outcome cards: CS/implementation team signal, onboarding signal, follow-on project (editor suggestions). Editor suggestions card visually emphasized.

**Speaker notes:**
I'll name these as what they are: team reads and recollections, not measured data.

The clearest business outcome was the follow-on: the editor suggestions project came directly from the Dataset Manager. Once the configuration layer was clean enough to work with, building intelligent suggestions on top of it became a viable investment. That project existed because this one had been done. In product terms, the Dataset Manager didn't just solve a problem — it created a surface worth investing in.

The implementation team's read: standard configuration setup took roughly half the time after the Dataset Manager shipped. Their words, not a dashboard.

Onboarding: new customers started completing configuration setup in a first session rather than requiring multiple back-and-forths with the implementation team.

One thing I'd do differently: I'd instrument the configuration flow before starting. We shipped a better product but I can't tell you precisely where the original friction was highest or how much each layer of the abstraction reduced it. Having a baseline would have made the outcome quantifiable, and the business case for any follow-on work more concrete.

---

## Q&A preparation

**"What would you do differently?"**
Instrument the flow before starting. The outcome was real but qualitative. A baseline completion rate, or time-on-task for the configuration steps, would have given us a number to point to after shipping. I'd build that into the research phase next time.

**"How did you validate the direction?"**
Task-based user sessions with the prototype before finalizing the design. The signal was whether users could configure a dataset without needing to translate into product language. When the most experienced user completed a task in a first session that had previously required implementation team support, that was the validation.

**"How did you handle disagreement about SQL?"**
Made the case with evidence, not opinion. The research told us who the users were and how they thought. SQL required a mental model those users didn't have. The PM wasn't wrong to raise it — it just served a different segment than the one we needed to design for. Once that was clear, there wasn't much to disagree about.

**"Who else was involved and what was your specific contribution?"**
PM defined the business problem and held the stakeholder relationship. Engineering implemented and shaped what was technically feasible. My specific contribution: identified the language mismatch through research, made the case against SQL, defined the conceptual model that became the Dataset Manager UI, ran usability sessions on the prototype.

**"Three sessions seems like a small sample — how confident were you in that direction?"**
The confidence came from the specific signal, not the count. When the most experienced user in the cohort struggled with the same conceptual blocks as new users, more sessions would have added to the count without changing the diagnosis. The question I needed to answer was whether experience with the interface closed the gap. One experienced user failing told me it didn't.
