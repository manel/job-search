# Case Deck: Dataset Manager (Abacum)

**Figma:** https://www.figma.com/slides/ufLGMlcTQvBxZrHT2dS1eh/Dataset-manager (v2 built 2026-11-09 in the top row; v1 kept below it, skipped). Image sources: [evidence/abacum-figma-index.md](../evidence/abacum-figma-index.md).
**Best for:** Product design roles, research that changed a direction, complex B2B configuration, cross-functional decisions, staged delivery.
**Duration:** walk-through 10 to 12 minutes; leave the rest for questions. If time runs short, cut slides 3 (Framing) and 6 (Diagnosis) to one sentence each before touching the proof slides (5, 7, 8, 10).
**Lead framing:** testing showed the product's language was the blocker, and I got Product and Engineering to change the language in two steps.
**Effects:** slide 5 is a build: duplicate slides with identical layer names, Smart Animate 0.3s ease-out, one finding per click.

Every claim is checked against [evidence/experience-facts.md](../evidence/experience-facts.md) (Dataset Manager entries; chronology and the time-saving attribution confirmed 2026-11-09). Speaker notes are beats, not a script.

Version history: v1 (October 2026) said "SQL shipped first" and credited the time saving to an implementation team. v2 corrects both: customers got SQL-like formulas, and the estimate came from the Integrations squad's engineers. v2.1 (2026-11-09, from the Notion export): the first three testers were Abacum's FP&A specialists, then customer users; "Next time" now names the autonomy metric the squad defined. v2.2 (2026-11-14, Manel): slide 2 and Figma 2 credit both teams with dataset setup (our FP&A team, with help from the squad's engineers); Figma on-slide text updated the same day.

---

## 1. Cover

**Headline:** From JSON files to self-serve data setup
**Sub:** Customers reached a working dataset in their first session
**Small:** Dataset Manager · Abacum · 2022 to 2023
**Visual:** formula box with the formula library open, right half.

**Notes:** Result first: customers set up their own datasets and reached a working configuration in their first session. The squad's engineers estimated standard setup took about half the time. My role: designer on the Integrations squad, design and customer testing.

---

## 2. Context

**Label:** Context
**Headline:** Customers couldn't set up their own data
**Visual:** back-office JSON schema, cropped large. Caption: "The dataset definition, early 2022. Our FP&A team set it up for each customer, with help from the squad's engineers."

**Notes:** A dataset turns ERP or spreadsheet data into dimensions and measures. In early 2022 it was a JSON file customers couldn't touch.

---

## 3. Framing

**Label:** Framing
**Headline:** Three jobs: set up, enrich, cleanse
**Visual:** my four "How might we" notes, with "Self-service means activation" pulled out. Caption: "My notes, January 2022."

**Notes:** The request was a better JSON editor. I framed the work around what users had to do instead.

---

## 4. Sequencing

**Label:** What came first
**Headline:** Mapping now, transforming later
**Visual:** architecture board (Mapping "Now", Transforming "Later") and the first-release scope list with items struck out.

**Notes:** Mapping happens on every dataset; transformations were sequential and rare. Biggest scope cut: transformations waited. The scope crop hides a colleague's name; check it before presenting.

---

## 5. Testing (build: language, vocabulary, dependencies)

**Label:** Research
**Headline:** Users could write the logic in Excel, not in SQL
**Visual:** early-flow screenshot with three pins revealed one per click:
- Language: all three described the logic with Excel functions. None could write it in SQL.
- Vocabulary: they looked for dimensions and mappings. The screen showed schema properties.
- Dependencies: they changed dimensions without seeing what used them.
**Footer:** Our FP&A specialists first, then customer users. Real configuration tasks on the early flows.

**Notes:** The first three testers set up datasets for customers every day, and the most experienced of them got stuck in the same places as the others, so product experience didn't close the gap. Customer users then hit the same language problems.

---

## 6. Diagnosis

**Label:** Diagnosis
**Headline:** Column settings in the words finance teams use
**Visual:** vocabulary map (exposed structure → guided configuration: schema configuration → dataset setup, nested properties → dimensions and mappings, raw format settings → column formats, transformation syntax → familiar formulas) next to the column settings screen.

**Notes:** Answers the Vocabulary finding. Pick a column type, map it to a dimension, let auto-map fill the values.

---

## 7. Language decision

**Label:** Decision
**Headline:** SQL-like formulas first, Abacum formulas next
**Visual:** 2022 transform field with SQL-like formulas; 2023 formula builder on Abacum formulas.

**Notes:** Engineering wanted to extend the back-office SQL approach; I argued for Abacum formulas with the test results. The interim step was easier to build without revamping formulas. Say "SQL-like formulas", never "SQL shipped".

---

## 8. Guardrails

**Label:** Guardrails
**Headline:** Show what a change will affect before saving
**Visual:** "Where a dimension is used" dialog; "Accepting the impact before saving" warning.

**Notes:** Answers the Dependencies finding. Renaming a dimension could delete formulas in the modules that used it. I designed the dependencies view. Whether the impact warning shipped is unknown; present it as the design.

---

## 9. Final product

**Label:** Final product
**Headline:** Creating a calculated column
**Visual:** JSON thumbnail ("Before: JSON") → shipped column builder.

**Notes:** Pick fields, write a formula, check it before saving. Some advanced transformations stayed restricted.

---

## 10. Outcome

**Label:** Outcome
**Headline:** Finance teams set up standard datasets themselves
**Proof lines:** Customers reached a working configuration in their first session (observed after release) · Standard setup took about half the previous time (estimate from the Integrations squad's engineers, not measured)
**Next time:** The squad had defined an autonomy metric. Report it after release, so the result is a number.

**Notes:** Say there's no after-release number before they ask.

---

## 11. Close

**Headline:** What would be most useful to go deeper on?
**Small:** The SQL decision · The testing · The dependencies design

**Notes:** Stop talking.

---

## Speaker notes to paste into Figma

The Figma plugin API can't write Slides speaker notes, so paste these by hand. Each sentence sits on its own line. Actions sit on their own line too, starting with ▶ and in [brackets]. Don't read those lines aloud. "Figma N" is the slide's position in the v2 row (14 slides; the slide 5 build is four slides). Slide text checked against the file on 2026-11-09. Notes rewritten for speech 2026-11-16 (rules in [interviews/playbooks/case-presentation.md](../interviews/playbooks/case-presentation.md#writing-for-speech)); paste them again.

**Figma 1 (Cover)**

Dataset Manager let finance teams at Abacum set up their own data.

After it shipped, customers reached a working configuration in their first session.

The squad's engineers estimated that standard setup took about half the time it used to.

I was the designer on the Integrations squad.

I ran the design and the customer testing, from the first framing to the formula builder.

**Figma 2 (Context)**

Abacum is a financial planning platform.

Customers bring in data from their ERP or from spreadsheets.

A dataset defines how that data becomes dimensions and measures in their models.

In early 2022, the dataset was a JSON file that customers couldn't touch.

Our FP&A specialists set up each customer's connections and datasets in the back office.

The squad's engineers helped with the import, the configuration and the transformations.

So every change waited for one of those two teams.

**Figma 3 (Framing)**

The request was a better interface for editing JSON.

Before I designed that, I split the work into three jobs.

First, set up a dataset and its columns.

Second, enrich it: give each column a type and map it to a dimension.

Third, cleanse it with transformations.

Next to them, I wrote "self-service means activation".

If customers couldn't configure their data, they couldn't get value from the product.

▶ [Short on time: one sentence. "I framed it as three jobs: set up, enrich, cleanse."]

**Figma 4 (What came first)**

Every dataset needs mapping, and in no fixed order.

Transformations happen in sequence, and few customers used them.

So mapping went first, and transformations waited.

With the PM, I cut functions and some mapping cases from the first release.

Transformations were the biggest cut.

▶ [Point at the struck-out list.]

▶ [Never name the PM.]

**Figma 5 (Research)**

I tested the early flows in two rounds.

The first round was three of our FP&A specialists.

They set up datasets for customers every day.

The second round was customer users.

In both rounds, people did real configuration tasks.

▶ [Click.]

**Figma 6**

All three specialists could describe the transformation with Excel functions.

None of them could write it in SQL.

The customer users had trouble with the wording too.

Both of them read IF ... THEN backwards.

▶ [Click.]

**Figma 7**

They also looked for dimensions and mappings.

The screen showed them schema properties.

The most experienced tester led our FP&A team and had used Abacum for over a year.

That tester still got stuck in the same places as the others.

So the gap was in the product's language.

More time with the product wouldn't have closed it.

▶ [Click.]

**Figma 8**

And they changed dimensions without seeing what depended on them.

▶ [If asked about the sample size: see Q&A below.]

**Figma 9 (Diagnosis)**

Users thought in dimensions, mappings and date formats.

The product asked them for schema properties and data types.

So column settings used their words.

You pick a column type and map it to a dimension.

Then auto-map fills in the values.

▶ [Short on time: one sentence.]

**Figma 10 (Decision)**

Engineering wanted to extend the SQL approach they already used in the back office.

I argued for Abacum's own formulas.

Users already knew them from the modeling layer.

I brought the test results back each time it came up.

In the end, we agreed on a step in between.

First, customers got a transform field with SQL-like formulas.

It was quicker to build, because we didn't have to rebuild formulas first.

Then the formula builder replaced it.

It used Abacum formulas, with syntax checks and autocomplete.

The cost was that customers learned an interim syntax for a while.

▶ [Say "SQL-like formulas". Never say SQL shipped.]

**Figma 11 (Guardrails)**

Once customers could change their own data, one change could break models and tables they couldn't see.

For example, renaming a dimension could delete the formulas that used it.

So I designed the dependencies view.

Each column shows which datasets, modules and tables use its dimension.

And if a change removes filters, the user has to accept the impact before saving.

▶ [If asked whether the warning shipped: I don't know. Present it as the design.]

**Figma 12 (Final product)**

This is a calculated column in the shipped builder.

You pick the fields and write a formula, like in a spreadsheet.

Then you check it before you save.

Some advanced transformations stayed restricted.

**Figma 13 (Outcome)**

After release, finance teams set up standard datasets without our FP&A team.

Customers reached a working configuration in their first session.

The squad's engineers estimated that standard setup took about half the previous time.

Customer support also told me they were getting fewer configuration requests.

I checked in with them regularly after release.

The squad had defined an autonomy metric.

It was the share of dimension actions that customers completed without help from our FP&A team.

No after-release number reached me, so I can't give you a percentage.

Next time, I'd make sure we reported it.

▶ [Say "no after-release number" before they ask. Don't quote the metric's baseline or targets.]

**Figma 14 (Close)**

What would be most useful to go deeper on?

▶ [Stop talking. If they hesitate, offer the three options on the slide: the SQL decision, the testing, the dependencies design.]

---

## Backup

- **v1 row (skipped):** the October 2026 deck, kept until v2 is approved. Don't present it: it says SQL shipped.
- **Dimension rename, the follow-up (Engine, January 2024):** I designed renaming dimension items with an impact check, after interviews with four internal implementation and FP&A colleagues. It shipped. If they want a whiteboard problem, use ordering: sorting cities inside countries breaks the country order unless each level stores its own order.
- **Dimension creation inside the dataset:** users left the dataset to create a missing dimension. I proposed creating and editing basic dimensions in place; customers then reported faster configuration and fewer errors. No slide; use it if they ask about friction in the flow.

---

## Q&A preparation

**"What would you do differently?"** Make sure the metric gets reported. The squad defined an autonomy metric in late 2022; with the after-release number, the outcome would be a figure and the next investment easier to justify.

**"Why ship SQL-like formulas if you disagreed?"** It got transformations to customers months earlier without rebuilding formulas first. I agreed to it as a step, with the formula builder as the destination, and the formula builder shipped.

**"Three sessions seems like a small sample."** The first round asked whether experience closed the gap, so I tested with the people who knew the product best: our FP&A specialists. The most experienced hit the same blocks as the others, so it didn't. The customer sessions afterwards showed the same language problems.

**"Who else was involved and what was yours?"** The PM owned the business problem and scope with me. Engineers built it and shaped what was feasible. Mine: the framing, the mapping-first sequencing, the customer tests, the case against SQL, column settings, the dependencies view and the formula builder design.

**"How did you get Product and Engineering to agree?"** I brought the test findings back each time the direction came up, until the interim step and the formula builder were the plan.

**Don't claim:** that the first three testers were customers; that SQL shipped; that the impact warning shipped; a measured time saving or completion rate; "implementation team". Never name the PM or the research participants. The support line is claimable as a recollection: Manel checked with customer support himself after release (confirmed 2026-11-09).
