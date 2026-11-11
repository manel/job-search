# Wizeline UX interview: Remuner DS case deck (talk track)

Deck: Figma file "Remuner DS", one slide row (21 Figma slides since 2026-11-07: "What I bring" and "Thank you" added after Handover for the client round; before that 19 Figma slides plus two skipped originals at the end: deck slide 3 is five builds, deck slide 5 is four, deck slide 7 is three; builds use smart animate with earlier items dimmed). Built 2026-10-27; rebuilt the same day for strategy and JD coverage. Slide 5 updated 2026-10-29 with the marketing library.
Slot: 15 minutes per David Ho's email (STAR: situation, task, actions, outcomes; role and team; no long paragraphs, no small assets). The 25-minute whiteboard follows, so don't run over.
Every figure below was checked against the Figma files on 2026-10-27 or against [evidence/experience-facts.md](../../evidence/experience-facts.md).

The slides carry one point each. The detail is here, said aloud.

| #   | Slide                                         | Time | Say                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --- | --------------------------------------------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Cover                                         | 0:20 | I was Remuner's only designer. This is the design system I built while still doing all the product work.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 2   | Situation                                     | 1:15 | Every engineer had their own components, with Vuetify defaults filling the gaps. Point at the audit: text ran from 9px to 25px, and there were values like 22.0099px. There were no Figma components.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 3   | The constraint (5 builds, 4 clicks)           | 1:30 | Click on each need as you name it, then once more for the decision. Three needs competed for my hours: features that couldn't stop, no system, and a team going from 2 to 5 engineers who would copy whatever already existed. My call was to build the system inside feature work. Then the ownership split: I owned the brief, the libraries, the tokens repo and the audit. Engineers adapted the pipeline and built the components in code.                                                                                                                                                                                                                                                                                                                                                                             |
| 4   | Prioritisation                                | 2:00 | Foundations first, because every component depended on them. Then the most-used components, which here were forms: TextField, Textarea, Select. The Select audit showed selects and autocompletes mixed together, so Autocomplete came next. Dark mode and motion were deferred because no screen needed them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 5   | Architecture                                  | 1:55 | One core of 417 primitives in one repo, which I owned. The app has its own semantic layer (189 tokens) and 161 component sets, including a domain layer for ranking, tiers and the IC and manager widgets. The marketing site used the same core with its own semantic layer. I ran the exports, and the agency injected them into WordPress. The marketing site also had its own Figma library on the same core: buttons, form fields, page sections. I designed pages with it for the agency, and they had to use the tokens. I also built LinkedIn templates on it so the marketing team could publish without me. Typography switches by mode for desktop and mobile. This is the bridge to multi-brand: a brand would be another semantic layer or mode over the same core. Both products were one brand, so say that. |
| 6   | Select end to end                             | 2:00 | No standard Select existed. I audited every instance and turned the requirements into one component: 131 variants and 13 props named like the code, covering rest, hover, focus and disabled, plus error and multiple. It went in screen by screen as features reached each screen, for example the permissions screen. I wrote the tickets with the spec and where to apply it. The old one stayed on a "DEPRECATED -> Select" page, marked, so engineers could still find it. Autocomplete shares almost all of Select's props (state, size, orientation, multiple); one name differs, `hasInfo` against `infoVisual`, so don't say "identical".                                                                                                                                                                          |
| 7   | Accessibility                                 | 1:30 | The base colours were inherited and I built the ramps. I normalised them in HSL with the Figma MCP. Text and icon colours meet AA (ratios on the slide, measured 2026-10-29). Where AA and harmony clashed, AA won. Helper text and links were the last ones, darkened before I left. Errors carry a message, not just a red border, and some components were checked with screen readers. Say "AA" and "some", and stop there. The original slide 7 is skipped in Figma (its focus claim was wrong for fields).                                                                                                                                                                                                                                                                                                            |
| 8   | Adoption and governance                       | 2:05 | The loop: audit, ticket, feature work, monthly front-end meeting. A lint rule (loosened to block only new violations) and a weekly component count fed the audit board. Nothing was removed silently: the ranking tokens are still in the file marked "TO DELETE". The mistake: I deleted a token file the app used and caused a short outage. In February 2026 I hardened the repo with Codex, with an engineer reviewing every step. If I did it again, CI on the tokens repo from the first commit.                                                                                                                                                                                                                                                                                                                      |
| 9   | Outcome                                       | 1:30 | 10 of 18 core screens when I left in March 2026, tracked on the audit board. Then the three buckets. Close on the CTO quote.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 10  | Handover                                      | 0:30 | A designer and a PM joined in my last months and worked from the library. I set up a Notion page where engineers and product logged inconsistencies and problems, so the team could keep iterating the components. Client round (10 Nov): go straight to slide 11.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 11  | What I bring (added 2026-11-07, client round) | 1:00 | Three anchors, one example each. Client design systems: several clients, at the studio and outside it (Manel, 2026-11-10); vLex is the named example, coached about 15 of their designers ("about 15"; no dates, metrics or token scope). Abacum: one system across five squads, weekly library sync, migration off MUI run from each squad's backlog (co-led with the head of design if asked; never "led"). Close to the code: Remuner tokens repo, engineer-reviewed PRs, years of own front-end code at the studio. Then the plan line, said as a plan: learn your design system and its contribution rules, check my area against it, bring gaps back as proposals. Changed 2026-11-10: the seat on the Index team is unconfirmed (Forest leads WSJ product design), so the slide and notes say "the team" and "your design system". Name Index only after they do; then say "contribute to", never "manage".                                                                                                                                                                                                   |
| 12  | Thank you                                     | 0:05 | Thank them; open the floor. Contact line on the slide.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

Total: 14:35, which leaves 25 seconds of slack.

Client round (10 Nov, added 2026-11-08): the result goes first on slide 1, slide 8 drops to two sentences, and slides 9 to 12 take about 60 seconds together. With 13b, What I bring and Thank you added, aim for about 12 minutes, then hand the choice to the panel on slide 21. Source of the change: Reddit advice on presenting to execs (result up front, keep it short, let them drive), applied because Forest leads his own cases with numbers.

## JD coverage

| JD | Slide |
|---|---|
| Building and refining components for edge cases, accessibility and multi-brand | 6, 7 |
| Organising Figma libraries for other designers | 5 (marketing library and templates used by the marketing team), plus 10 (a designer and a PM who joined late worked from the library; Notion page for feedback) |
| Tokens and variables for theming and multi-brand | 5 |
| Linking the core system to product-area libraries | 5 (core, then product semantic, then domain components) |
| Documentation | Say it on 6: docs and a Storybook view per component were generated with the Figma MCP. Not on a slide. |
| WCAG in components | 7 |
| Design to code | 3, 5, 6 |
| Versioning and contribution | 8 |
| AI tooling | 7, 8 (one line each) |

## Limits (from the register)

- No npm releases and no ESLint violation trend. "14 reviewed PRs" means PRs to the tokens repo. The number of app PRs isn't recorded.
- Variants: Select has 131 and the library has 1,438 (counted 2026-10-27). The old deck's "around 1,600" isn't supported.
- Screen readers: "in some cases" only. No keyboard or WCAG 2.2 conformance claim.
- Multi-brand: never say you shipped it. The marketing site is the same brand.
- Marketing library (added 2026-10-29): the agency used the tokens because you required it, and built its own components, which weren't a design system. Never say the live site ran on your components. No count of pages, assets or time saved.
- Library users (slide 20 diagram, Manel 2026-11-10): you, the new designer, the PM and the marketing person. She worked in both the app library (assets for the website) and the website library.
- Marketing sync: the marketing Figma file holds its own local copy of the core tokens; it doesn't link to the app library. If asked how core changes reached it: "By hand. Every time a core token changed, I updated the marketing library. Changes came often at first, then the core stabilised." If they push, the better setup is one published core library both files consume; say you'd do that now.
- The faster-shipped feature is still missing (NEEDS YOUR STORY). If they ask for a delivery-speed example, say you don't have a measured one and point to the 10 of 18 screens and the Select rollout.

## Visual sources

- Slide 13b anatomy (added 2026-11-08 after the Round 2 atomic-design feedback): read from the Components file the same day. Select and Autocomplete nest ListPanel > ListContent (single or multiple) > ListItem > .actionListItem, plus Chip, Icon, IconButton, Tooltip and Divider. `.fieldHelperTextContainer` is nested in 8 form components (TextField, Textarea, Select, Autocomplete, DateInput, FileInput, ColorPicker, RadioGroup); `.fieldValidation` only in Select and TextField. `.actionListItem` also feeds ActionMenu. The input box itself is not a shared component: never say Select is built on TextField. The atom/molecule/organism labels are the grouping on the slide, not names in the file.

- Slide 2 audit: Core file, Typography page, "Audit" section.
- Slide 6: Components file, "DEPRECATED -> Select" page (before) and the Select set, top rows (after).
- Slide 7 ramps: Core file, Color page, "Spectrum v2", Brand and UI rows. These are the current ramps, not a before/after. Ratios: tokens bound in Select and TextField, Components file, measured on white 2026-10-29. Error field: TextField hasError="Yes", text filled in for the slide. In that file, helper text (#909DA3, 2.8:1) and links (#1594D1, 3.4:1) still fail; Manel fixed them later, values not remembered, so never quote ratios for them.

## Speaker notes to paste into Figma

The Figma plugin API can't write Slides speaker notes, so paste these by hand. Actions sit on their own line, starting with ▶ and in [brackets]. Don't read those lines aloud.

**Figma 1 (Cover)**
I was Remuner's only designer. I built its design system inside feature work, and when I left in March 2026, 10 of 18 core screens ran on it.

**Figma 2 (Situation)**
Every front-end engineer had built their own components. Vuetify defaults filled the gaps.
▶ [Point at the audit.]
Text ran from 9px to 25px, with values like 22.0099px. There were no components in Figma.

**Figma 3 (Constraint)**
I had three needs and the same hours for all of them.
▶ [Click as you name each one.]

**Figma 4**
First, features couldn't stop.

**Figma 5**
Second, there was no system.

**Figma 6**
Third, the team was growing from 2 to 5 engineers. New people would copy whatever already existed.

**Figma 7**
▶ [Click.]
So I built the system inside feature work. I owned the brief, the Figma libraries, the tokens repo and the audit. Engineers adapted the token pipeline and built the components in code.

**Figma 8 (Prioritisation)**
I started with foundations, because every component depended on them. Then forms, because every screen used them: TextField, Textarea and Select, then Autocomplete.
▶ [Client round: stop there. The longer version, with dark mode and motion left for later, is in the table above if they ask.]

**Figma 9 (Architecture, build 1: core)**
▶ [Client round: slides 9 to 12 together in about 60 seconds. One sentence per build.]
Everything starts from one core: 417 primitives in one repo, which I owned.
▶ [Click.]

**Figma 10 (Architecture, build 2: app)**
The app has its own semantic layer of 189 tokens and 161 component sets. Some of those are domain components, like ranking, tiers and the IC and manager widgets.
▶ [Click.]

**Figma 11 (Architecture, build 3: marketing)**
The marketing website had its own semantic layer on the same core.
▶ [Point at the core.]
I ran the token exports, and the agency put them into WordPress. I also built a Figma library for the website, with buttons, form fields and page sections. I designed pages with it for the agency, and they had to use the tokens. Then I made LinkedIn templates, so the marketing team could publish without me.
▶ [Click.]

**Figma 12 (Architecture, build 4: full picture)**
Typography changes by mode: titles are 32px on desktop and 22px on mobile. A new brand would be one more semantic layer on this core.
▶ [Say clearly that both products were the same brand. Don't call it multi-brand.]

**Figma 13 (Select)**
There was no standard Select. Each screen had its own. I audited every instance and turned what I found into one component: 131 variants and 13 props, named like the code.
▶ [Point at the props panel.]
These are the same names as in the code and in the Storybook view I generated for it. It went in screen by screen, as features reached each screen. The permissions screen is one example. I wrote the tickets with the spec and where to use it. I kept the old one on a page marked "DEPRECATED", so engineers could still find it.
▶ [If asked about Autocomplete: it shares almost all of Select's props. Don't say identical.]
▶ [Click.]

**Figma 13b (Select anatomy, added 2026-11-08; live in the deck as Figma slide 14 since then)**
I built it bottom up, in atomic design layers. Tokens sit at the base, then atoms like Chip, Icon and the base list row. Those make the list items, the list panel and the helper text, and those make the Select. Autocomplete is built from the same parts. So a fix to the list row reached Select, Autocomplete and the action menu at the same time.
▶ [Point at the rows, top to bottom.]
▶ [If they want the real layers: switch to the Components file, Select page, and expand the nested instances. Names starting with a dot are internal parts, not for use on screens.]

**Figma 14 (Accessibility, build 1: ramps)**
The base colours were inherited, and I built the shade ramps. I used the Figma MCP to normalise them in HSL. When AA and visual harmony clashed, I chose AA.
▶ [Click.]

**Figma 15 (Accessibility, build 2: contrast)**
Text and icon colours meet AA.
▶ [Point at the ratios.]
Helper text and links were the last ones. I darkened them to AA before I left.
▶ [Don't quote ratios for helper text or links.]
▶ [Click.]

**Figma 16 (Accessibility, build 3: states)**
Errors don't rely on colour alone.
▶ [Point at the error field.]
They show a message, not just a red border. I checked some components with screen readers.
▶ [If asked about focus: buttons have a focus ring; on fields, focus is a border colour change.]

**Figma 17 (Adoption and governance)**
The system grew through a loop: audit, ticket, feature work, and a monthly meeting with the front-end team. Nothing was removed without warning.
▶ [Point at the "Nothing removed silently" line.]
Old tokens and the old Select stayed in the files, marked, until we agreed to remove them. The old ranking tokens are still in the file, marked "TO DELETE".
Two checks in the code fed the audit board. A lint rule flagged styles that bypassed the tokens, and a script counted the components each template used. I ran it every week. The lint rule started strict, and engineers had to fix old code just to ship a change, so we loosened it to block only new violations.
▶ [Added 2026-10-30. Say "the team built" the rule and script; never name the lint tool; no trend or counts.]
I made one real mistake. I deleted a token file the app still used, and it caused a short outage. In February 2026 I hardened the repo with Codex. An engineer reviewed every step. If I did it again, I'd put CI on the tokens repo from the first commit.

**Figma 18 (Outcome)**
When I left in March 2026, 10 of 18 core screens used system components. I tracked that on the audit board, from the weekly component count and my own review of each screen.
▶ [If asked about speed: not measured. In Figma it was your impression as sole designer.]
▶ [Point at each box, left to right. One sentence each.]
For engineering, hardcoded styles in the app were replaced with tokens through PRs the engineers reviewed, and a lint rule blocks new ones.
For the team, it went from two to five engineers working from one set of components, and the designer who joined late worked from the library.
And the CTO summed it up in a product review: "From a 2010 app to a 2025 app."
▶ [Pause after the quote. Don't read the footer numbers unless asked.]
▶ [Client round, before they ask about metrics: "I didn't measure product impact. Now I'd track how long a new screen takes to ship on the components."]

**Figma 19 (Handover)**
In my last months, a new designer and a PM joined. Both worked from the component library. I set up a Notion page where engineers and the product team logged inconsistencies and problems, so we could keep improving the components.
▶ [Client round: click to slide 20.]

**Figma 20 (What I bring)**
Three things I'd bring to the team.
▶ [Point at each card.]
First, I've built design systems for several clients. One was vLex: I helped them build their system and coached about 15 of their designers on using it. Second, I've worked inside one system shared by many teams. At Abacum it served five squads. We ran a weekly library sync, and each squad moved off MUI from its own backlog. Third, I work close to the code. At Remuner I owned the tokens repo and opened PRs that engineers reviewed, and at the studio I shipped my own front-end code for years.
▶ [Plan line.]
In my first months I'd learn your design system and how people contribute to it, check what my product area uses against it, and bring the gaps back as proposals.
▶ [Don't name Index unless they do. If it fits, ask: "Do you work from Index, or does WSJ have its own library?"]

**Figma 21 (Thank you)**
Thank you. What would be most useful to go deeper on?
▶ [Then stop and let them choose. If they ask for a flow, a screen or the files, go there straight away.]
