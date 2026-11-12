# Case Deck: Modeling Syntax (Abacum)

**Figma:** https://www.figma.com/slides/mOXQnVxL9e6XBo8jthv6zB/Modeling-syntax (built 2026-11-09 in the Abacum DS v2 layout; 10 slides plus skipped backup B1). Images: slide 6 from "Abacum | Syntax - Implementation" `550:15424` (clause-style formula, 2023); slide 9 from the same file `1635:26903` (function help popover, January 2024); B1 from "Abacum | Syntax - Exploration (current)" `288:25346` (Future of Syntax prototype, March 2024). Nothing taken from the team workshop page.
**Best for:** Fintech and data-heavy product roles, initiative across scope, "influence without authority" and "decision with no clear answer" questions.
**Duration:** walk-through 10 to 12 minutes; leave the rest for questions. If time runs short, cut slides 2 (Context) and 7 (Engineering) to one sentence each before touching the proof slides (5, 6, 9).
**Lead framing:** I spotted the syntax inconsistencies, took them to the head of design and wrote the Improve Syntax Usability initiative; I traced them to the functions themselves, made the case to fix the grammar before adding more UI on top, and chose a direction the evidence supported but didn't settle on its own.
**Effects:** none planned. Candidate build: slide 5, benchmark first, then the customer call.

Every claim is checked against [evidence/experience-facts.md](../evidence/experience-facts.md) ("Modeling language", including the Notion entries of 2026-11-09) and [context/portfolio.md](../context/portfolio.md) (Modeling Syntax). Sources for the benchmark, the customer call and the function audit: Notion "Consolidate Abacum functions" ([evidence/notion/deck-and-case-updates.md](../evidence/notion/deck-and-case-updates.md)). "Days instead of weeks" and fewer formula support requests are recollections confirmed 2026-06-12, with no recoverable numbers. Speaker notes are beats, not a script.

---

## 1. Cover

**Headline:** One formula syntax across Abacum's modeling layer
**Sub:** Abacum, 2023 to 2024 · B2B financial planning platform

**Notes:** Result first: I standardised the formula syntax, the rules went into the Abacum Script, and the consistent structure made editor suggestions possible. The customer team's recollection: new users wrote their first useful formula in days instead of weeks.

---

## 2. Context

**Label:** Context
**Headline:** Finance teams build their models in formulas
**Visual:** Abacum's layers (data, modeling, reporting, UI), modeling highlighted.

**Notes:** Power users spend most of their time here. I moved to the Engine squad after Dataset Manager.

---

## 3. The problem

**Label:** Problem
**Headline:** The same concept had different syntax in different places
**Visual:** three real functions from the audit, annotated "parameters outside", "clause style", "parameters inside":
- `DISTRIBUTE_MONTHLY (dimension, start, end, measure) FROM DATASET`
- `JOIN other_dataset_column FROM OTHER_DATASET ON dataset_column = other_dataset_column`
- `TEXTSPLIT (text_column, delimiter, position_to_keep)`

**Notes:** Excel conventions, SQL-style clauses and custom syntax, built by different engineers over time. Syntax usability was already an Engine initiative; I audited the functions underneath it. 15 of the 37 functions broke the pattern.

---

## 4. Making the case

**Label:** Making the case
**Headline:** Fix the grammar before adding more UI on top
**Visual:** the squad's risk rating: function consolidation "no usability risk", syntax filters "high risk". Line below: fifth of seven frustrations in the April 2023 survey (4 of 15 respondents).

**Notes:** Syntax wasn't users' top complaint: fifth of seven in the April 2023 survey. So the case rested on cost and on what it unblocked. Every new function built on the old pattern extended it. One parameter structure would let filters combine and let the editor show parameter previews and a filter popover. The squad rated the consolidation low risk, so it went first. I got the head of design's support before starting.

---

## 5. Investigation (candidate build: benchmark, then customer call)

**Label:** Research
**Headline:** Every competitor put parameters inside parentheses
**Visual:** benchmark table (8 January 2024), Abacum as the outlier; customer-call fragments beside it.

| | Excel | GSheets | Pigment | Causal | Abacum |
|---|---|---|---|---|---|
| Case | Upper | Upper | Upper | Lower | Upper |
| Parameters | Inside () | Inside () | Inside () | Inside () | Outside |
| Word separator | None, "." for sub-functions | Mostly none, "." | Mostly none | Mixed | Mixed "_" |

Quote fragments: "several months with your implementation team" · "if it look more like excel"

**Notes:** Abacum was the outlier on parentheses and on underscores in names. In a December 2023 call, a customer said he only got used to the formulas after several months with our implementation team, and asked for them to feel more like Excel. I also audited every inconsistent function.

---

## 6. Decision

**Label:** Decision
**Headline:** Excel conventions for a finance audience
**Visual:** a 2023 formula in the product with FROM and WHERE outside the function; FX before and after; the Abacum Script rules card.

**Notes:** SQL-style clauses already existed in parts of the product. Cost named: users with a SQL background would find it less natural at first. Rules: parameters inside the parentheses, no underscores, "." for sub-functions, FROM sources moved into the parameters, Excel or Google Sheets names where the function exists there. They went into the Abacum Script.

---

## 7. Engineering

**Label:** Collaboration
**Headline:** I worked through the syntax with one engineer
**Visual:** none needed.

**Notes:** Two working sessions in January 2024. The calls needed the design framing and the technical knowledge in the same conversation. Example: JOIN became three parameters (the other dataset, its column, your column). The work went into 13 tickets for the first iteration and 15 for the second.

---

## 8. What changed

**Label:** Result
**Headline:** One way to write each concept
**Visual:** before and after for DISTRIBUTE_MONTHLY and FX, from the Abacum Script (January 2024).

**Notes:** Parameters inside parentheses, dataset references as explicit inputs, standard function names.

---

## 9. Outcome

**Label:** Outcome
**Headline:** Consistent syntax made editor suggestions possible
**Stats:** Editor suggestions and parameter preview followed · First useful formula in days instead of weeks (customer team's recollection) · Fewer formula support requests in the following quarters (recollection) · New functions follow the Abacum Script
**Next time:** write down the reasoning behind each rule as well as the rule.
**Visual:** the January 2024 function help popover, captioned as predating the renaming (it still shows DISTRIBUTE_YEARLY).

**Notes:** Say "recollection, no numbers" before they ask.

---

## B1. Backup: what came next (skipped slide)

**Headline:** A vision prototype for the next formula editor
**Visual:** Future of Syntax prototype screen: `SUM ( Dataset, measure )` with parameter chips and a dataset preview.
**Body:** March 2024, Maker Days. Type a dot to filter by dimension, period or version. Parameters become chips, with a preview of the dataset you pick. Keyboard users get an expert mode. A vision piece, not shipped. Parameter preview later shipped.

---

## 10. Close

**Headline:** What would be most useful to go deeper on?

**Notes:** Stop talking.

---

## Speaker notes

The Figma deck has no build steps, so slide numbers match Figma positions (checked 2026-11-12). Paste these by hand. Actions sit on their own line, starting with ▶ and in [brackets]. Don't read those lines aloud.

**Slide 1 (Cover)**
At Abacum I standardised the formula syntax across the modeling layer. The rules went into the Abacum Script, and the consistent structure made the editor suggestions project possible. The customer team's recollection was that new users wrote their first useful formula in days instead of weeks.
Nobody had ticketed this problem. I spotted the inconsistencies, took them to the head of design and wrote the initiative to fix them. The evidence didn't settle the direction, so this case is mostly about how I decided.

**Slide 2 (Context)**
Abacum is financial planning software. In the modeling layer, finance teams write the formulas that define their models and plans. Power users spend most of their time there. I moved to the Engine squad, which owned it, after Dataset Manager.
▶ [Short on time: one sentence.]

**Slide 3 (The problem)**
The same concept, like referencing a period or another model, was written differently in different parts of the product. The formulas mixed Excel conventions, SQL-style clauses and custom syntax, because different engineers had built each part at different times.
I wrote the Improve Syntax Usability initiative for the Engine squad. Later I audited the functions underneath, and 15 of the 37 broke the pattern: some put parameters inside the parentheses, some outside, some used SQL-style clauses.
▶ [Point at the three examples.]

**Slide 4 (Making the case)**
Syntax wasn't users' biggest complaint. In our April 2023 survey it came fifth of seven; error messages came first. So I couldn't argue from user pain alone.
I argued from cost and from what it unblocked. Every new function built on the old pattern would extend it. With one parameter structure, filters could combine, and the editor could show parameter previews and a filter popover. The squad's risk review rated the consolidation low risk and syntax filters high risk, so the foundation went first. I got the head of design's support before starting.

**Slide 5 (Investigation)**
I benchmarked Excel, Google Sheets, Pigment and Causal to see whether there was a convention. There was: all of them put parameters inside parentheses and avoided underscores in function names. Abacum was the outlier on both.
▶ [Click, if built.]
Then the customer calls. In December 2023 one customer told us he only got used to our formulas after several months with our implementation team, and asked for them to feel more like Excel. He already knew how a formula should work, and ours didn't match it.
▶ [Never name the customer.]

**Slide 6 (Decision)**
There were two directions. We could keep the SQL style that parts of the product already used, with FROM and WHERE clauses outside the function. Or we could follow Excel: every parameter inside the parentheses, function names as single capitalised words.
Our users were finance teams, and every competitor followed Excel, so I chose Excel. The cost was real: users with a SQL background would find it less natural at first.
The rules went into the Abacum Script: parameters inside the parentheses, no underscores in names, a dot for sub-functions, and Excel or Google Sheets names wherever the function already existed there. New functions could follow them without a design review each time.

**Slide 7 (Engineering)**
I worked through the syntax with one engineer, in two sessions in January 2024. Each call needed the design framing and the technical knowledge in the same conversation, because we had to know what a piece of syntax would produce in the model. JOIN, for example, became three parameters: the other dataset, its column, and your column. The work went into 13 tickets for the first iteration and 15 for the second.
▶ [Short on time: one sentence.]

**Slide 8 (What changed)**
Each concept now had one way to be written. Parameters went inside the parentheses, dataset references became explicit inputs, and function names followed one standard. Heavy users no longer had to remember two ways of writing the same thing.

**Slide 9 (Outcome)**
The clearest outcome was the editor suggestions project, and later parameter preview, which shipped after I handed the work over. With every parameter in a predictable position, the editor could map parts of a formula to inputs and suggestions. With clauses outside the function, it couldn't.
The customer team remembers new users writing their first useful formula in days instead of weeks, and fewer formula support requests in the following quarters. Those are recollections. There are no numbers.
New functions followed the Abacum Script after that.
If I did it again, I'd write down the reasoning behind each rule as well. The reasons, like why we dropped the SQL style, stayed in meeting notes, so the next engineer to extend the syntax had only the rules.
▶ [Say "recollection, no numbers" before they ask.]

**Slide 10 (Close)**
What would be most useful to go deeper on?
▶ [Stop talking.]

---

## Q&A preparation

**"How did you decide what the right syntax was?"** The benchmark and the customer calls pointed the same way: Excel conventions. Where they didn't settle a detail, I picked what a new user would find most predictable.

**"How did this get onto the roadmap?"** I wrote the Improve Syntax Usability initiative myself. The function-level fix came later, once the audit showed the cause. I got the head of design's support first, kept the investigation small enough to fit around roadmap work, and reported progress as I went.

**"How did you prioritise?"** I scored ten syntax problems with ICE, with impact defined as adoption by finance users who didn't model yet. The top two were understanding which variables a formula uses and understanding and fixing syntax errors. The consolidation came first because the squad rated it low risk and the later UI depended on it.

**"What came next?"** In March 2024 I built a vision prototype for the future of the syntax: dot-triggered dimension, period and version filters, parameter preview and a keyboard-first expert mode. It was a vision piece, not shipped.

**"What would you do differently?"** Write down the reasoning with the rules. The Abacum Script had the conventions; the reasons stayed in meeting notes.

**"How did this connect to business outcomes?"** Power users spend the most time in formulas, so friction there costs the most. The more concrete signal is the editor suggestions project, which needed this work done first.

**Don't claim:** a number for the onboarding time or the support drop; that you built the editor suggestions; that a PM ran this; that syntax was users' top frustration; that you oversaw the release after the handover. Never name the customer or the engineer.
