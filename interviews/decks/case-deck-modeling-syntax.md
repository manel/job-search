# Case Deck: Modeling Syntax (Abacum)

**Figma:** no deck yet. Build it in the Abacum DS v2 layout ([context/brand.md](../../context/brand.md)) when a process reaches a case round.
**Best for:** Fintech and data-heavy product roles, initiative across scope, "influence without authority" and "decision with no clear answer" questions.
**Duration:** walk-through 10 to 12 minutes; leave the rest for questions. If time runs short, cut slides 2 (Context) and 7 (Engineering) to one sentence each before touching the proof slides (5, 6, 9).
**Lead framing:** I found a problem nobody had ticketed, made the case to work on it, and chose a direction the evidence supported but didn't settle on its own.
**Effects:** none planned. Candidate build when the deck exists: slide 5, benchmark first, then the customer call.

Every claim is checked against [evidence/experience-facts.md](../../evidence/experience-facts.md) ("Modeling language") and [context/portfolio.md](../../context/portfolio.md) (Modeling Syntax). "Days instead of weeks" and fewer formula support requests are recollections confirmed 2026-06-12, with no recoverable numbers. Speaker notes are beats, not a script.

---

## 1. Cover

**Headline:** One formula syntax across Abacum's modeling layer
**Sub:** Abacum, 2023 · B2B financial planning platform

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
**Visual:** the same logic written two ways in two parts of the product, annotated.

**Notes:** Excel conventions, SQL-style clauses and custom syntax, built by different engineers over time. No ticket; it showed up in support calls.

---

## 4. Making the case

**Label:** Making the case
**Headline:** I got the head of design's support before starting
**Visual:** none, or the support-call quotes.

**Notes:** Every new function built on the inconsistent syntax made it worse. The cost already showed in support calls and call recordings.
[NEEDS YOUR STORY: was there pushback on the time? If not, say the evidence made it an easy argument.]

---

## 5. Investigation (candidate build: benchmark, then customer call)

**Label:** Research
**Headline:** Every competitor put parameters inside parentheses
**Visual:** benchmark table (Excel, Google Sheets, Pigment, Causal) with Abacum as the outlier; customer-call quote beside it.

**Notes:** Abacum was the outlier on parentheses and on underscores in names. One enterprise customer needed months of onboarding support to write basic formulas and wished it felt like Excel. I also audited every inconsistent function.

---

## 6. Decision

**Label:** Decision
**Headline:** Excel conventions for a finance audience
**Visual:** SQL-style (`FROM dataset WHERE condition`) next to Excel-style (all parameters inside parentheses).

**Notes:** SQL-style clauses already existed in parts of the product. Cost named: users with a SQL background would find it less natural at first. The rules went into the Abacum Script.

---

## 7. Engineering

**Label:** Collaboration
**Headline:** I worked through the syntax with one engineer
**Visual:** none needed.

**Notes:** The calls needed the design framing and the technical knowledge in the same conversation.

---

## 8. What changed

**Label:** Result
**Headline:** One way to write each concept
**Visual:** the slide 3 examples, standardised.

**Notes:** Parameters inside parentheses, dataset references as explicit inputs, standard function names.

---

## 9. Outcome

**Label:** Outcome
**Headline:** Consistent syntax made editor suggestions possible
**Stats:** Editor suggestions project followed · First useful formula in days instead of weeks (customer team's recollection) · Fewer formula support requests in the following quarters (recollection) · New functions follow the Abacum Script
**Next time:** write down the reasoning behind each rule as well as the rule.

**Notes:** Say "recollection, no numbers" before they ask.

---

## 10. Close

**Headline:** What would be most useful to go deeper on?

**Notes:** Stop talking.

---

## Speaker notes

No Figma deck exists yet, so these are keyed by slide number. When the deck is built, renumber them by Figma position and paste them by hand. Actions sit on their own line, starting with ▶ and in [brackets]. Don't read those lines aloud.

**Slide 1 (Cover)**
At Abacum I standardised the formula syntax across the modeling layer. The rules went into the Abacum Script, and the consistent structure made the editor suggestions project possible. The customer team's recollection was that new users wrote their first useful formula in days instead of weeks.
Nobody had ticketed this problem, and the evidence didn't hand me the answer, so this case is mostly about how I decided.

**Slide 2 (Context)**
Abacum is financial planning software. In the modeling layer, finance teams write the formulas that define their models and plans. Power users spend most of their time there. I moved to the Engine squad, which owned it, after Dataset Manager.
▶ [Short on time: one sentence.]

**Slide 3 (The problem)**
The same concept, like referencing a period or another model, was written differently in different parts of the product. The formulas mixed Excel conventions, SQL-style clauses and custom syntax, because different engineers had built each part at different times.
No customer had filed a bug about it and it wasn't on the roadmap. It showed up in support calls, as users asking why something worked one way here and another way there.

**Slide 4 (Making the case)**
The squad had a roadmap, so I needed a reason to spend design time on this. Every new function built on top of the inconsistent syntax would extend it, and the cost was already visible in support calls and call recordings. I got the head of design's support before starting.
▶ [Pushback story goes here once written. Don't invent one.]

**Slide 5 (Investigation)**
I benchmarked Excel, Google Sheets, Pigment and Causal to see whether there was a convention. There was: all of them put parameters inside parentheses and avoided underscores in function names. Abacum was the outlier on both.
▶ [Click, if built.]
Then the customer calls. One enterprise customer described months of onboarding support just to write basic formulas, and said they wished it felt more like Excel. They already knew how a formula should work, and ours didn't match it. I also audited every function that broke the pattern.
▶ [Never name the customer.]

**Slide 6 (Decision)**
There were two directions. We could keep the SQL style that parts of the product already used, with FROM and WHERE clauses outside the function. Or we could follow Excel: every parameter inside the parentheses, function names as single capitalised words.
Our users were finance teams, and every competitor followed Excel, so I chose Excel. The cost was real: users with a SQL background would find it less natural at first.
We wrote the rules down in the Abacum Script, so new functions would follow them without a design review each time.

**Slide 7 (Engineering)**
I worked through the syntax with one engineer. Each call needed the design framing and the technical knowledge in the same conversation: what a piece of syntax would actually produce in the model.
▶ [Short on time: one sentence.]

**Slide 8 (What changed)**
Each concept now had one way to be written. Parameters went inside the parentheses, dataset references became explicit inputs, and function names followed one standard. Heavy users no longer had to remember two ways of writing the same thing.

**Slide 9 (Outcome)**
The clearest outcome was the editor suggestions project. With every parameter in a predictable position, the editor could map parts of a formula to inputs and suggestions. With clauses outside the function, it couldn't.
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

**"How did you manage this when it wasn't on your squad's roadmap?"** I got the head of design's support first, kept the investigation small enough to fit around roadmap work, and reported progress as I went.

**"What would you do differently?"** Write down the reasoning with the rules. The Abacum Script had the conventions; the reasons stayed in meeting notes.

**"How did this connect to business outcomes?"** Power users spend the most time in formulas, so friction there costs the most. The more concrete signal is the editor suggestions project, which needed this work done first.

**Don't claim:** a number for the onboarding time or the support drop; that you built the editor suggestions; that a PM ran this. Never name the customer.
