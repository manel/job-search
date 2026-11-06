# Case Deck: Design Systems at Abacum (Abax)

**Figma:** https://www.figma.com/slides/ae1SMrxEXfMMdUygkGTMcH/Abacum-DS (rebuilt 2026-11-06 in the "v2" row; the earlier version is kept in the first row, skipped).
**Best for:** DS-titled roles and any round that asks for one project end to end plus collaboration (Perk Depth of Expertise).
**Duration:** walk-through about 12 minutes; leave the rest for questions.
**Lead framing:** how a system nobody asked for got time, got adopted by squads that didn't report to us, and how we measured it honestly.
**Effects:** build sequences copy the Remuner deck: duplicate slides with identical layer names, Smart Animate 0.3s ease-out. Elements fade in one step per click; on the last step earlier elements dim to 40%.

Every claim is checked against `evidence/experience-facts.md` (Abax entries, 2026-11-06). Speaker notes are beats, not a script.

---

## 1. Cover

**Headline:** Why we built Abax across five product squads
**Sub:** Abacum, 2022-2024 · B2B financial planning platform

**Notes:** Abacum is FP&A software for finance teams. I joined on data integrations and ended up co-leading the design system with the head of design.

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
