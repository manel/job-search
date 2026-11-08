# Case Deck: Design Systems at Abacum (Abax)

**Figma:** https://www.figma.com/slides/ae1SMrxEXfMMdUygkGTMcH/Abacum-DS (rebuilt 2026-11-06 in the "v2" row; the earlier version is kept in the first row, skipped).
**Best for:** DS-titled roles and any round that asks for one project end to end plus collaboration (Perk Depth of Expertise).
**Duration:** walk-through about 12 minutes; leave the rest for questions. If time runs short, cut slides 4 (Investment choice) and 6 (Roadmap) to one sentence each before touching the proof slides (9, 10, 12).
**Lead framing:** how a system nobody asked for got time, got adopted by squads that didn't report to us, and how we measured it honestly.
**Effects:** build sequences copy the Remuner deck: duplicate slides with identical layer names, Smart Animate 0.3s ease-out. Elements fade in one step per click; on the last step earlier elements dim to 40%.

Every claim is checked against `evidence/experience-facts.md` (Abax entries, 2026-11-06). Speaker notes are beats, not a script.

---

## 1. Cover

**Headline:** Why we built Abax across five product squads
**Sub:** Abacum, 2022-2024 · B2B financial planning platform

**Notes:** Result first (rule in `interviews/prep.md`, "Rules for every case deck"): With the head of design, I co-led Abax, a design system that all five product squads used. When I left, about 47% of the component uses we tracked in the code were Abax, against a goal of 80%. Then the context: Abacum is FP&A software for finance teams, and I joined on data integrations.

---

## 2. Context (build: 5 squads, then my role)

**Label:** Context
**Headline:** Five squads and six designers, with no shared components
**Cards:** Integrations, Engine, Reporting, Collaboration, Admin; each "MUI + local components".
**My role:** I co-led the business case with the head of design and worked on the tokens, the Figma library and governance. Engineers built the pipeline and coded the components.
**Footer:** A change to a shared pattern meant a separate fix in each squad.

**Notes:** Every squad had its own buttons, cells and menus on top of MUI. Fixes landed in one squad and not in another. Say "I" for the business case, library and process; "we" for the decision and the migration.

---

## 3. Business case (build: evidence, concern, proposal, question)

**Label:** Business case
**Headline:** We asked engineering for time to test shared components in production
**Cards:** Evidence: buttons, cells and menus built differently in each squad. Concern: a side project competing with squad work. Proposal: shared tokens and one Button, shipped to production. The open question: how do engineers get focused time for this?

**Notes:** We named engineering's objection before they raised it. Presented to engineering leadership and at an all-hands. Battle card C.

---

## 4. Investment choice

**Label:** Investment choice
**Headline:** We chose one dedicated week for Abax
**Cards:** Alongside sprints: 2 front-end engineers and 1 designer, 2 weeks alongside squad work. Maker Days: 4+ front-end engineers and 2+ designers, 1 dedicated week.

**Notes:** Maker Days was Abacum's quarterly slot for non-roadmap work. Getting selected turned a side project into a sanctioned one.

---

## 5. Proof

**Label:** Proof
**Headline:** The first Abax Button shipped in one week
**Body:** It proved the path from Figma to code. An engineer built the original pipeline.

**Notes:** Tokens and the Button reached production in one Maker Days week. After that, each new component was easier to justify.

---

## 6. Roadmap

**Label:** Roadmap
**Headline:** After Maker Days, we planned Abax adoption
**Steps:** Pilot result → set an adoption goal (80% of Abax and MUI uses from Abax) → find gaps → build next → release and migrate.

**Notes:** The 80% goal counts every Abax and MUI use in the codebase, reached through reworks and new features. Never "80% of new UI".

---

## 7. Architecture

**Label:** Architecture
**Headline:** We kept MUI to avoid a five-squad rewrite
**Cards:** Keep MUI as the base. Primitive tokens (raw values). Semantic tokens (names tied to use, `color-text-primary`).
**Pipeline line:** Figma Variables → Token Studio → Style Dictionary → code

**Notes:** All five squads already used MUI; replacing it would have meant rewriting every screen. Squads could adopt Abax gradually. I didn't build the pipeline; I made the token decisions inside it.

---

## 8. Rollout and governance (build: six cards)

**Label:** Rollout
**Headline:** Squads migrated in their own sprints while design ran the library
**Cards:**
- Feature flags: new form elements shipped behind flags.
- Squad backlogs: each squad added its own migration tickets.
- Weekly library sync: every designer attended, for over eight months.
- Two Figma libraries: Exploration for experiments, Implementation for published work.
- Issue reports: broken components, naming, missing variants and detaches, through Notion and Slack.
- Lint rule: engineers got a warning when they imported an MUI component that Abax replaced.
**Footer:** I proposed the two-library split and ran the sync and the issue process. An engineer wrote the lint rule.

**Notes:** The lint rule covered Button, Select, Tab, Tooltip and Chip, as a warning. Don't say it checked tokens or blocked builds.

---

## 9. Measurement (build: code, Figma, ranking)

**Label:** Measurement
**Headline:** We measured adoption in code and in Figma
**Code, monthly:** front-end engineers counted every Abax and MUI component use. About 47% Abax at departure; goal 80% of the same count.
**Figma, every two weeks:** health score = library instances ÷ all UI nodes (library, detached and one-off frames). A ranking of the most-detached components set what to fix first. Thresholds per component, roughly: under 5% fine, 5 to 15% warning, over 15% broken.
**Footer:** I defined the Figma measures and an engineer built the scripts. The 47% comes from the code count only.

**Notes:** Two measures, two denominators; never merge them. No score history survives, so describe the mechanism and don't quote a health score.

---

## 10. Select and Autocomplete (build: problem, fix, guidance, coaching, result)

**Label:** One fix, end to end
**Headline:** The detachment ranking pointed us to Select and Autocomplete
**Steps:**
- Problem: designers detached the menu to add or remove items, because hiding items broke the auto layout. Some weren't sure when to use Select and when Autocomplete.
- Fix: split into Select, Menu and Menu item. A placeholder slot let designers build items locally and swap them in.
- Guidance: when to use each, on the docs page and in the component description.
- Coaching: a session in the weekly design-system meeting, collecting feedback.
- Result: detachments on these components almost stopped. Remaining issues went into later iterations.

**Notes:** This was before Figma's native slots; it was a placeholder component plus instance swap. "Almost stopped" is recollection; no figure.

---

## 11. Coaching

**Label:** Coaching
**Headline:** Most adoption problems came from designers not knowing what existed
**Cards:** Release notes: every Abax release on Slack, to design and engineering. Weekly meeting: some sessions coached new components, variants and practices. One to one: ad hoc sessions for anyone who needed more help.
**Footer:** When the data showed a component going unused, I asked the designers why and fixed the cause in the next iteration.

**Notes:** No squad resisted. Don't invent one. If asked for a single designer's before and after, there isn't one recorded; describe the practice.

---

## 12. Outcome (build: four stats, then why)

**Label:** Outcome
**Headline:** Abax reached five squads, with migration still in progress when I left
**Stats:** 5 squads using Abax · ~47% of tracked component uses (goal 80%) · 2 + 1 squads: form migration done, one underway · 8+ months of weekly library sync
**Why 80% wasn't reached:** squads migrated one by one, through reworks and new features. There was no dedicated clean-up.
**Other signals:** a designer built a new screen quickly from existing variants; customers said the product felt more polished.
**Source line:** The 47% is reconstructed from monthly codebase counts; the raw exports aren't available.

**Notes:** Say the 80% wasn't reached, and why, before they ask. No velocity number exists; don't invent one.

---

## 13. What I took to Remuner

**Label:** Next system
**Headline:** What I changed when I built Remuner's system alone
**Cards:** Smaller token set: build what the product uses, extend when it needs more. Lint rule for token use: strict at first, then failing only new violations. Audit board: each core screen tracked on or off the system, 10 of 18 at departure.

**Notes:** Same principles, one designer instead of six. Bridge to the Remuner deck if they want more.

---

## 14. LLMs today

**Label:** Today, hypothetical
**Headline:** How I would use LLMs on Abax today
**Cards:** Figma context, Tokens, Components and docs, Production code (unchanged from v1).
**Footer:** At Remuner I used the Figma MCP to manage tokens and run contrast checks.

**Notes:** End on a question: "What would be most useful to go deeper on?" Then stop and let them choose. If they ask for the Figma files or a flow, go there straight away.

---

## Speaker notes to paste into Figma

The Figma plugin API can't write Slides speaker notes, so paste these by hand. Actions sit on their own line, starting with ▶ and in [brackets]. Don't read those lines aloud. "Figma N" is the slide's position in the v2 row (34 slides; builds are separate slides). Build steps checked against the file on 2026-11-08.

**Figma 1 (Cover)**
With the head of design, I co-led Abax, a design system that all five product squads used. When I left, about 47% of the component uses we tracked in the code were Abax, against a goal of 80%.
Abacum is FP&A software for finance teams. I joined on data integrations.

**Figma 2 (Context)**
Abacum had five product squads and six designers, and no shared components.
▶ [Click: the five squads appear.]

**Figma 3**
Every squad had its own buttons, cells and menus on top of MUI.
▶ [Click.]

**Figma 4**
A fix landed in one squad and not in the others. A change to a shared pattern meant a separate fix in each squad.
▶ [Click.]

**Figma 5 (My role)**
I co-led the business case with the head of design. I worked on the tokens, the Figma library and governance. Engineers built the pipeline and coded the components.
▶ [Say "I" for the business case, library and process; "we" for the decision and the migration.]
▶ [Click: the squads dim and My role stays lit.]

**Figma 6**
▶ [Nothing new to say. Click to the next slide.]

**Figma 7 (Business case)**
We asked engineering for time to test shared components in production. The evidence: buttons, cells and menus were built differently in each squad.
▶ [Click.]

**Figma 8**
We named engineering's concern before they raised it: a side project competing with squad work.
▶ [Click.]

**Figma 9**
So we kept the proposal small: shared tokens and one Button, shipped to production.
▶ [Click.]

**Figma 10**
That left one open question: how do engineers get focused time for this? We presented it to engineering leadership and at an all-hands.
▶ [If asked about the objection: battle card C.]

**Figma 11 (Investment choice)**
There were two options. Two front-end engineers and a designer for two weeks alongside squad work, or Maker Days: one dedicated week with four or more engineers and two or more designers. We chose Maker Days. It was Abacum's quarterly slot for non-roadmap work, and being selected turned a side project into a sanctioned one.
▶ [Short on time: one sentence. "We got a dedicated Maker Days week."]

**Figma 12 (Proof)**
Tokens and the first Abax Button reached production in that one week. It proved the path from Figma to code. An engineer built the original pipeline. After that, each new component was easier to justify.
▶ [Point at the Storybook screenshot.]

**Figma 13 (Roadmap)**
After Maker Days we planned adoption. The goal was for 80% of all Abax and MUI component uses in the code to come from Abax. Then we found the gaps, built what was missing, and released through feature flags and squad backlogs.
▶ [Never say "80% of new UI".]
▶ [Short on time: one sentence.]

**Figma 14 (Architecture)**
We kept MUI as the base. All five squads used it, and replacing it would have meant rewriting every screen. Abax added primitive tokens for raw values and semantic tokens named by use, like color-text-primary. Tokens went from Figma Variables through Token Studio and Style Dictionary into code. I made the token decisions; I didn't build the pipeline.
▶ [Point at the pipeline line.]

**Figma 15 (Rollout)**
Squads migrated in their own sprints while design ran the library. New form elements shipped behind feature flags, and each squad added its own migration tickets.
▶ [Click.]

**Figma 16**
Every designer came to a weekly library sync, for over eight months. I proposed two Figma libraries: Exploration for experiments, Implementation for published work.
▶ [Click.]

**Figma 17**
Problems came in through issue reports in Notion and Slack: broken components, naming, missing variants and detaches. Engineers got a lint warning when they imported an MUI component that Abax replaced.
▶ [The lint rule covered Button, Select, Tab, Tooltip and Chip, as a warning. Don't say it checked tokens or blocked builds.]
▶ [Click.]

**Figma 18**
I ran the sync and the issue process. An engineer wrote the lint rule.

**Figma 19 (Measurement)**
We measured adoption in two places. In code, every month, front-end engineers counted every Abax and MUI component use. When I left, about 47% were Abax. The goal was 80% of the same count.
▶ [Click.]

**Figma 20**
In Figma, every two weeks, we tracked a health score: library instances divided by all UI nodes, counting detached instances and one-off frames too.
▶ [Click.]

**Figma 21**
A ranking of the most-detached components told us what to fix first. Roughly, under 5% was fine, 5 to 15% a warning, over 15% broken.
▶ [Thresholds are approximate. Don't quote a health score: no history survives.]
▶ [Click.]

**Figma 22**
I defined the Figma measures, and an engineer built the scripts. The 47% comes from the code count only.
▶ [Two measures, two denominators. Never merge them.]

**Figma 23 (Select and Autocomplete)**
One example: the detachment ranking pointed at Select and Autocomplete. Designers detached the menu to add or remove items, because hiding items broke the auto layout. Some weren't sure when to use Select and when to use Autocomplete.
▶ [Click.]

**Figma 24**
We split it into Select, Menu and Menu item. A placeholder slot let designers build their own items locally and swap them in.
▶ [If asked: this was before Figma's native slots. It was a placeholder component plus instance swap.]
▶ [Click.]

**Figma 25**
We wrote down when to use each, on the docs page and in the component description.
▶ [Click.]

**Figma 26**
Then I ran a session in the weekly design-system meeting, walked designers through it and collected feedback.
▶ [Click.]

**Figma 27**
Detachments on these components almost stopped. The remaining issues went into later iterations.
▶ ["Almost stopped" is recollection. No figure.]
▶ [Click: the steps dim and the result stays lit.]

**Figma 28**
▶ [Nothing new to say. Pause on the result, then click to the next slide.]

**Figma 29 (Coaching)**
Most adoption problems came from designers not knowing what existed; no squad resisted Abax. Every release went out on Slack to design and engineering. Some weekly meetings coached new components, variants and practices, and anyone who needed more got a one-to-one session. When the data showed a component going unused, I asked the designers why and fixed the cause in the next iteration.
▶ [Don't invent a resisting squad. No single designer's before and after is recorded; describe the practice.]

**Figma 30 (Outcome)**
Abax reached all five squads. About 47% of tracked component uses were Abax, against an 80% goal. Two squads finished the form migration and a third was underway. We ran the weekly sync for more than eight months.
▶ [Point at the source line if asked: the 47% is reconstructed from monthly counts; the raw exports aren't available.]
▶ [Click.]

**Figma 31**
We didn't reach 80%. Squads migrated one by one, through reworks and new features, and there was no dedicated clean-up.
▶ [Say this before they ask.]
▶ [Click.]

**Figma 32**
A designer also built a new screen quickly from existing variants, and customers said the product felt more polished.
▶ [No velocity number exists. Don't invent one.]

**Figma 33 (What I took to Remuner)**
When I built Remuner's system alone, I changed three things. A smaller token set: build what the product uses, extend when it needs more. A lint rule for token use, strict at first, then failing only new violations. And an audit board tracking each core screen: 10 of 18 were on the system when I left.
▶ [If they want more: bridge to the Remuner deck.]

**Figma 34 (LLMs today)**
Today I'd use LLMs in four places. Connect an agent to Figma to inspect components and spot inconsistent patterns. Agree on token names, then update Figma variables and code tokens together. Draft variants, code, tests and docs from a shared spec. And write and open the code PR myself, with engineers reviewing it before release. At Remuner I already used the Figma MCP to manage tokens and run contrast checks.
What would be most useful to go deeper on?
▶ [Then stop and let them choose. If they ask for the Figma files or a flow, go there straight away.]

---

## Backup

- **B1. The problem:** duplicate components and repeated fixes (v1 slide).
- **B2. Deprecated components:** marked ⛔ DEPRECATED, replacement published under the clean name, old one unpublished after migration (v1 slide).

---

## Q&A preparation

**"What would you do differently?"** Start with a smaller token set and enforce adoption in code earlier. That's what I did at Remuner (slide 13).

**"How did you handle the team dynamics?"** Head of design as co-lead; engineering leadership for the time; squad designers in the weekly sync; squads owned their own migration tickets. Battle card C for the capacity objection.

**"How did system work get prioritised against features?"** Maker Days as a bounded bet, then migration inside squad backlogs and feature work.

**"How did you measure adoption?"** Slide 9. Two measures: the monthly code count (47%, goal 80%) and the Figma health score every two weeks. I defined the Figma measures; an engineer built the scripts. No raw exports survive.

**"What was your contribution vs the team's?"** Co-led the business case. Token decisions, the Figma library, the two-library split, the sync and the issue process, the Figma measures. Engineers built the pipeline, the components in code, the scripts and the lint rule.

**Don't claim:** that the lint rule checked tokens or blocked builds; a health score or trend; a velocity number; "80% of new UI"; that you wrote the pipeline or scripts.
