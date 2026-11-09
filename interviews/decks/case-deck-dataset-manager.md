# Case Deck: Dataset Manager (Abacum)

**Best for:** Product design roles, research that changed a direction, complex B2B configuration, cross-functional decisions, staged delivery.
**Duration:** 10 to 12 minutes of walk-through, then the panel steers. 11 slides.
**Figma:** "Dataset manager" (Slides), v2 built 2026-11-09; v1 kept as skipped slides. Image sources: [evidence/abacum-figma-index.md](../../evidence/abacum-figma-index.md).
**Evidence:** [evidence/experience-facts.md](../../evidence/experience-facts.md), "Dataset Manager". Chronology and the time-saving attribution confirmed 2026-11-09.
**Rules:** result first, one line of text per slide, images carry the content ([interviews/prep.md](../prep.md), "Rules for every case deck"; [context/brand.md](../../context/brand.md)).

Version history: v1 (October 2026) said "SQL shipped first" and credited the time saving to an implementation team. Both corrected in v2: customers got SQL-like formulas, and the estimate came from the Integrations engineers.

---

## Slide 1: Cover

**Headline:** From JSON files to self-serve data setup
**Sub:** Customers reached a working dataset in their first session
**Small:** Dataset Manager · Abacum · 2022 to 2023
**Visual:** Formula box with the formula library open (2309, Marketing asset), right half of the slide.

**Speaker notes:** Dataset Manager let finance teams at Abacum set up their own data. Before it, every change to a dataset went through an engineer. After it, customers reached a working configuration in their first session, and the squad's engineers estimated standard setup took about half the time. I was the designer on the Integrations squad and ran the design and customer testing from the first framing to the formula builder.

---

## Slide 2: Before

**Label:** CONTEXT
**Headline:** Every dataset change went through an engineer
**Visual:** The back-office JSON schema (2201 -> Manage), cropped large. One callout: "Edited by the squad's engineers for each customer."

**Speaker notes:** Abacum is a financial planning platform. Customers bring in data from their ERP or spreadsheets, and a dataset defines how that data becomes dimensions and measures in their models. In early 2022 that definition was a JSON file. Customers could not touch it, so the Integrations engineers configured every dataset by hand and every change waited in their queue.

---

## Slide 3: Framing

**Label:** FRAMING
**Headline:** Three jobs: set up, enrich, cleanse
**Visual:** My four "How might we" notes (2201 -> Manage), with the line "Self-service means activation" pulled out.

**Speaker notes:** The request was a better interface for editing JSON. Before designing that, I broke the work into what users needed to do: set up a dataset and its columns, enrich it by typing columns and mapping them to dimensions, and cleanse it with transformations. I wrote "self-service means activation" next to it, because a customer who could not configure data could not get value from the product.

---

## Slide 4: Sequencing

**Label:** WHAT CAME FIRST
**Headline:** Mapping now, transforming later
**Visual:** The architecture board (2201 -> Manage): Mapping "Now", Transforming "Later", with characteristics and actions.

**Speaker notes:** Mapping happens on every dataset and in no fixed order. Transformations are sequential and were rarely used. So mapping came first, and transformations waited. With the PM I cut functions and some mapping cases from the first release; the struck-out list is still in the file. Leaving transformations for later was the biggest scope cut.

---

## Slide 5: Testing

**Label:** RESEARCH
**Headline:** Users could write the logic in Excel, not in SQL
**Visual:** Early-flow screenshot (v1 slide 3), three findings revealed one at a time as pins: Language, Configuration, Dependencies.

**Speaker notes:** I tested the early flows with three customers, doing real configuration tasks. All three could describe the transformation they needed with Excel functions. None could write it in SQL. The most experienced user, who had used Abacum for over a year, got stuck in the same places as the newer ones, so the gap was the language. Testing also showed users changing dimensions without seeing what depended on them.

---

## Slide 6: Diagnosis

**Label:** DIAGNOSIS
**Headline:** Column settings in the words finance teams use
**Visual:** Left: JSON keys (`dimensions`, `property`, `timescale`). Right: Column settings panel with "Column type: Dimension" and auto-map (2207). Four short vocabulary pairs between them.

**Speaker notes:** Users thought in dimensions, mappings and date formats. The product asked for schema properties and data types. Column settings put those choices in their words: pick a column type, map it to a dimension, let auto-map fill the values.

---

## Slide 7: Language decision

**Label:** DECISION
**Headline:** SQL-like formulas first, Abacum formulas next
**Visual:** Two screens. Left: the 2022 transform panel with SQL-like steps (`JOIN RATIO FROM ... ON`, `'Global' if DEPARTMENT:NAME is ...`). Right: the formula builder with chips and the formula library (2023).

**Speaker notes:** Engineering wanted to extend the SQL approach they already used in the back office. I argued for the formulas users knew from Abacum's modeling layer, using the test results. We agreed on a step in between: customers got a transform field with SQL-like formulas, because it was easier to build without revamping formulas. The formula builder on Abacum formulas replaced it, with syntax checks and autocomplete. The cost was that customers learned an interim syntax for a while.

---

## Slide 8: Guardrails

**Label:** GUARDRAILS
**Headline:** Show what a change will affect before saving
**Visual:** The "Dimension 'Suppliers' used in" dialog, then the impact warning with "Accept impact on 3 table filters" (2207).

**Speaker notes:** Once customers could change their own data, a change could break models and tables they could not see. I designed the dependencies view: each column shows which datasets, modules and tables use its dimension, and a change that removes filters asks the user to accept the impact first.

---

## Slide 9: Final product

**Label:** FINAL PRODUCT
**Headline:** Creating a calculated column
**Visual:** JSON thumbnail → shipped column builder (v1 slide 9 images), dark surface.

**Speaker notes:** A calculated column in the shipped builder: pick fields, write a formula users know from spreadsheets, check it before saving. Some advanced transformations stayed restricted.

---

## Slide 10: Outcome

**Label:** OUTCOME
**Headline:** Finance teams set up standard datasets themselves
**Proof lines:**
- Customers reached a working configuration in their first session
- The squad's engineers estimated half the time on standard setup
**Small:** No baseline was measured. Next time I would track completion without help from the start.

**Speaker notes:** These are team reads. We had no instrumented baseline, so I can't give you a percentage. Customer support also reported fewer configuration requests in the following quarters. If I did it again I would measure completion without engineering help from the first test, so the result would be a number.

---

## Slide 11: Close

**Headline:** What would be most useful to go deeper on?

**Speaker notes:** Stop talking. If they hesitate, offer three options: the SQL decision, the testing, or the dependencies design.

---

## Q&A preparation

**"What would you do differently?"**
Measure from the start. With completion rate or time on task from the first sessions, the outcome would be a number and the next investment easier to justify.

**"Why ship SQL-like formulas if you disagreed?"**
It let the squad give customers transformations months earlier, without rebuilding formulas first. I agreed to it as a step, with the formula builder as the destination, and the formula builder shipped.

**"Three sessions seems like a small sample."**
The question was whether experience with the product closed the gap. The most experienced user hit the same blocks as the newer ones, so it did not. More sessions would only have added to the count.

**"Who else was involved and what was yours?"**
The PM owned the business problem and scope with me. Engineers built it and shaped feasibility. Mine: the framing, the mapping-first sequencing, the customer tests, the case against SQL, column settings, the dependencies view and the formula builder design.

**"How did you get Product and Engineering to agree?"**
By bringing the test findings back each time the direction came up, until the interim step and the formula builder were the plan.
