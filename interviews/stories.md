# Story library

One entry per story. Briefs, question maps and decks point here by story ID (`dataset-manager`, `token-file`); they don't retell the story. The [evidence register](../evidence/experience-facts.md) outranks this file: if they disagree, the register wins and this file gets fixed.

Merged 2026-11-12 from three older sets that used clashing labels. Old briefs still use those labels; translate them with the table below.

| ID | Story | Old prep.md | Old battle card | Old STAR bank (Datavant) |
| --- | --- | --- | --- | --- |
| [`dataset-manager`](#dataset-manager) | Dataset Manager: testing changed the direction | Story A | A | 1 |
| [`dimensions`](#dimensions) | Dimensions inside Dataset Manager | | B | 9 |
| [`modeling-language`](#modeling-language) | Modeling language made consistent | Story D | | 2 |
| [`abax`](#abax) | Abax design system, the whole case | Story B | | |
| [`maker-days`](#maker-days) | Maker Days: a bounded production test | Story B (part) | C | 3 |
| [`abax-migration`](#abax-migration) | Abax migration through squad backlogs | Story B (part) | | 4 |
| [`abax-deprecation`](#abax-deprecation) | Deprecated components in Figma search | | | 8 |
| [`remuner-ds`](#remuner-ds) | Remuner design system and the CTO quote | Story C | | 7 (audit) |
| [`manager-view`](#manager-view) | Manager view: disagree, deliver, assess | | D | |
| [`token-file`](#token-file) | Token file outage: a mistake owned | Q6 | E | 6 |
| [`ai-agent`](#ai-agent) | Remuner AI agent: scope and trust | | F | 5 |
| [`ic-dashboard`](#ic-dashboard) | IC dashboard: vague feedback made specific | | G | |
| [`kom-deadline`](#kom-deadline) | Kings of Mambo: a missed deadline | Q2 | | |
| [`kom-lofi-feedback`](#kom-lofi-feedback) | Kings of Mambo: lo-fi before hi-fi | Q24 | | |

Old labels to watch: prep.md "Story C" was the Remuner design system, battle card C was Maker Days, and some briefs (Biorce) used "Story C" for the AI agent. Prep.md "Story E" was the Kings of Mambo gap, now under [Gaps](#gaps).

## Pick a story

| What they ask | Story |
| --- | --- |
| Impact, research changed your mind, a complex problem | `dataset-manager` |
| Customer feedback, a small change with impact, simplifying a workflow | `dimensions` |
| A decision with no clear answer, working directly with Engineering | `modeling-language` |
| Pushback, influence without authority, competing priorities | `maker-days` |
| Adoption, gradual rollout, system stewardship | `abax-migration` |
| A practical fix to user friction, comparing options | `abax-deprecation` |
| Earning trust quickly, building from zero, prioritising with no capacity | `remuner-ds` |
| Disagreement, supporting a decision you challenged | `manager-view` |
| Failure, accountability, what you learned | `token-file` |
| AI, ambiguity, trust, zero to one | `ai-agent` |
| Vague feedback you had to clarify | `ic-dashboard` |
| A missed deadline, bad news to a client | `kom-deadline` |
| Feedback that changed how you work | `kom-lofi-feedback` |
| Mentoring someone | No story yet; see [Gaps](#gaps) |

## Answer shape

Take a breath, choose an episode, then open with why it fits: "A good example is ..., where ...". Give context, then your responsibility, then your actions and why, then the result. Aim for 60 to 90 seconds on the first answer and extend only when asked. Keep context to one or two sentences and spend most of the time on your decisions.

Name the result even when it is mixed. End there and let them ask a follow-up. "I" means your contribution; "we" means a shared decision or delivery.

- If the prompt is unclear: "When you say impact, do you mean the customer outcome or the wider team impact?"
- If you need a moment: "Let me think of a specific example."
- If you lose the thread: "Let me simplify that. The problem was ... My contribution was ... What changed was ..."
- If you have an adjacent story: "I have a related example, although it wasn't feedback from a PM. Would that be useful?"
- If you have no matching incident, say so. For a hypothetical question, explain what you would do; don't turn it into something you did.

---

## Abacum

### dataset-manager

Dataset Manager: testing changed the direction of a self-service data-configuration tool. Deck: [case-deck-dataset-manager.md](decks/case-deck-dataset-manager.md). Evidence: [register, Dataset Manager](../evidence/experience-facts.md#dataset-manager).

**Opener:** "At Abacum, testing changed our direction for a self-service data-configuration tool."

- **Context:** Finance users depended on the implementation team and JSON to configure datasets. Autonomy was the goal.
- **My responsibility:** Led design and customer testing. Took the research finding to the PM and lead engineer.
- **Actions and why:** Tested a simpler UI plus SQL. Users could express the logic with Excel functions but not with SQL. The team extended the familiar modeling language and built guided configuration instead of exposing SQL.
- **Result:** Shipped. Customers reached a working configuration in their first session; the squad's engineers estimated standard setup took roughly half the previous time.

**Limits:** The outcomes are team recollection, not analytics. Never "I reduced time by 50%", and no revenue, support-ticket or user-count claims. The decision and delivery were shared with Product and Engineering, so the "no SQL" call is "we", backed by my research. Don't quote participants or give a test count.
**Probes:** What changed your mind? What did you personally do? How did you know it helped? What did the team choose not to build, and what did that make harder?
**In reserve:** The familiar language was the important change; a simpler visual layer alone wasn't enough. If asked what you'd measure now: completion versus real independence, framed as what you would do, not what you did.

### dimensions

Letting users create a missing dimension without leaving the dataset they were configuring. Evidence: [register, Dataset Manager](../evidence/experience-facts.md#dataset-manager).

**Opener:** "One useful change was letting users create a missing dimension without leaving the dataset they were configuring."

- **Context:** Users had to leave the dataset, create the dimension in a separate area, come back and resume. Customers reported lost time, errors and confusion.
- **My responsibility:** Identified the workflow problem and proposed the change.
- **Actions and why:** Put basic creation and editing inside the open dataset. Product and Engineering agreed to build it. Advanced management stayed separate to keep the first version small.
- **Result:** Shipped. Customers reported faster configuration, fewer errors and less confusion.

**Limits:** Qualitative customer reports; no baseline, sample size or measured reduction. Supports "responding to feedback", not "clarifying vague feedback". Ownership of the later advanced work is not established.
**Probes:** Why not move everything in? What feedback followed? How did you find the problem? Why did the first version stop at basic creation and editing?

### modeling-language

Making Abacum's formula language consistent across functions. Deck: [case-deck-modeling-syntax.md](decks/case-deck-modeling-syntax.md). Evidence: [register, Modeling language](../evidence/experience-facts.md#modeling-language).

- **Context:** The modeling layer used several formula patterns, so users had to learn a different structure for each function.
- **My responsibility:** Led research and design with the head of design: customer-call evidence and competitor benchmarking. Partnered with an engineer on the syntax decisions.
- **Actions and why:** Proposed extending and standardising the existing language instead of introducing a new one. Used customer evidence to show the problem. There was no established pattern to copy, so the decision was a judgment call built on enough evidence to defend.
- **Result:** The consistent structure later supported contextual suggestions in the formula editor (the Dataset Manager autocomplete, November 2023). Faster writing and fewer support questions are qualitative feedback, not measured.

**Limits:** Syntax decisions were shared with Engineering. Syntax usability was already an Engine initiative, so never say nobody had ticketed it. Adoption of the suggestions is not established.
**In reserve:** `SUM(amount) FROM Transactional WHERE accounts_level_2 IS "Workforce"` became `SUM(Transactional.amount, accounts_level_2 = "Workforce")`: parameters inside the function, the dataset an explicit input.
**Probes:** What did retaining the existing language cost? Who decided?

### abax

The Abax design system as one case: co-led with the head of design across five product squads. Use the deck for a full walkthrough and the three episodes below for behavioral questions. Deck: [case-deck-design-systems-abacum.md](decks/case-deck-design-systems-abacum.md). Evidence: [register, Abax design system](../evidence/experience-facts.md#abax-design-system).

**Result line (from the deck):** "With the head of design, I co-led Abax, a design system that all five product squads used. When I left, about 47% of the component uses we tracked in the code were Abax, against a goal of 80%."

**Limits:** Co-led, never sole owner. Engineering built the original token pipeline. MUI stayed underneath to limit scope. The all-hands presentation sought buy-in; don't say it won it. No measured ROI. Name tools (Token Studio, Style Dictionary, the `prefer-abax-component` lint rule) only if asked, and check the register first.

### maker-days

Answering Engineering's capacity concern with a bounded production test. Evidence: [register, Abax design system](../evidence/experience-facts.md#abax-design-system).

**Opener:** "At Abacum, we addressed Engineering's capacity concern with a bounded production test for the design system."

- **Context:** Engineering worried the system would compete with squad work and never reach production.
- **My responsibility:** Co-led the business case with the head of design; contributed the token and library work. Engineering built the original pipeline.
- **Actions and why:** Showed real inconsistencies in the product, compared two staffing approaches, and the team chose one focused Maker Days week: more people away from squad work, for less time.
- **Result:** The tokens and the first Button reached production that week, which proved the design-to-code path worked.

**Limits:** Shared influence and a shared decision. No measured ROI or delivery-speed claim. Don't invent a PM conflict or a sole engineering implementation. Avoid quoting headcounts.
**Probes:** What objection did they raise? Why a week? What did you give up? Why was taking people off delivery worth it then?
**In reserve:** Squad delivery capacity was the cost. It was a small proof before broader adoption, not the end of the migration.

### abax-migration

Getting adoption through squad backlogs instead of a central rollout. Evidence: [register, Abax design system](../evidence/experience-facts.md#abax-design-system).

- **Context:** Five squads already used MUI, and replacing it would have needed broad product work. Shared components still had to fit each squad's delivery plan.
- **My responsibility:** Shared patterns and governance, including the library review and the migration approach. Squads kept their backlogs; Engineering owned implementation.
- **Actions and why:** Kept MUI underneath Abax, released new form elements behind feature flags, and let squads schedule their own migration tickets. Weekly reviews exposed missing states and variants.
- **Result:** When I left, two squads had finished the form migration and a third was in progress. A reconstructed code count put Abax at about 47% of tracked Abax and MUI component uses. Adoption was incomplete.

**Limits:** The migration state is recollection. The 47% is reconstructed and the raw exports are gone. It is a share of component uses, not of screens, users or squads. Don't invent an escalation when a squad delayed.
**Probes:** What did you gain and lose by leaving migration in squad backlogs? Name one missing variant you found.

### abax-deprecation

A smaller workable fix for deprecated components showing up in Figma search. Evidence: [register, Abax design system](../evidence/experience-facts.md#abax-design-system).

- **Context:** Deprecated components still appeared in Figma search, so designers could pick the wrong version during migration.
- **My responsibility:** Diagnosed the problem and proposed three approaches with their tradeoffs.
- **Actions and why:** Marked the old component deprecated and published the replacement under the clean name. Kept the old version during the transition, then unpublished it. That avoided a heavier remove-and-republish process.
- **Result:** Shipped, and the old component was later unpublished. Wrong selections and time saved were not measured.

**Limits:** The records keep only two of the three options; leave the third out.
**Probes:** Why keep the obsolete component available during the transition?

---

## Remuner

### remuner-ds

Building Remuner's design system from scratch as the sole designer. Deck: [case-deck-design-systems-remuner.md](decks/case-deck-design-systems-remuner.md). Evidence: [register, Design system and token pipeline](../evidence/experience-facts.md#design-system-and-token-pipeline).

- **Context:** Sole designer at a startup with no system in place. Each screen had its own Select, with different styles and behaviour.
- **My responsibility:** Built the component library and design system. Owned the brief, decisions and outcome of the token pipeline, which engineers adapted from the Abacum foundation to Remuner's Vuetify and Sass stack.
- **Actions and why:** Started with a deliberately small token set, a lesson from Abacum. Built foundations first, then the most-used form components (TextField, Textarea, Select, then Autocomplete after the Select audit). Ran an ongoing audit: capture every instance of a pattern, define variants, ticket it, review it with front-end engineers in the monthly meeting, and decide fix-now versus defer into an upcoming feature. Fixed part of the hardcoded styles in the app myself with Claude, as PRs the front-end team reviewed and merged.
- **Result:** 10 of 18 screens on the system when I left, tracked from a weekly scan and my review. The CTO, unprompted, described the product's before-and-after as going from a 2010 app to a 2025 app.

**Limits:** Never sole technical implementation or original authorship of the pipeline. The February 2026 pipeline additions (CI and safety checks, drift detection, smoke tests, W3C token format, HTML preview, JSON output) were done with Codex and reviewed and merged by engineers. WCAG AA for in-use colours only, never AAA, no named failing colours. No product metrics. The quote is "2010 app to a 2025 app", never 2020. The CTO can't be offered as a reference.
**Probes:** What did you defer and why? How did you measure adoption? What did the engineers own?
**In reserve:** Trust at a technical company came from shipping something visible and correct early; the visible change is why the CTO had an opinion at all. The audit is a working pattern, not one incident: use it for "how do you prioritise", not for "tell me about a time".

### manager-view

Disagreeing with a full redesign, then delivering it with the research findings kept in. Evidence: [register, Manager-view redesign](../evidence/experience-facts.md#manager-view-redesign).

**Opener:** "At Remuner, I disagreed with a full redesign, but worked to keep the research findings in the direction leadership chose."

- **Context:** Managers lacked an overview by metric, went through too many nested steps, and couldn't easily see previous-period information.
- **My responsibility:** The research and the design recommendation: fix the foundational workflow and architecture first.
- **Actions and why:** Stated the disagreement. The CEO and CTO chose a full redesign. Accepted it and kept the main findings in the metric overview and the navigation changes. Captured feedback afterwards and separated blocking problems from other friction.
- **Result:** Shipped. Positive feedback on the overview and navigation, mixed overall, including difficulty finding information.

**Limits:** Qualitative personal account. Don't say later iterations solved the problems; no later release is confirmed. The disagreement was with leadership, not with a PM.
**Probes:** What was your alternative? How did you act after the decision? What did the negative feedback change?

### token-file

A token file deleted by mistake caused a short production outage. Evidence: [register, Design system and token pipeline](../evidence/experience-facts.md#design-system-and-token-pipeline).

**Opener:** "I deleted a token file I thought was duplicated, and the next deployment caused a short production outage."

- **Context:** The front end still depended on the file; my assumption was wrong.
- **My responsibility:** Own the deletion and the mistaken dependency assumption. Don't shift it to the deployment or an engineer.
- **Actions and why:** Restored the file and pushed the fix. For several days I checked every required file before deployment. The team then added a required-file check until the front-end dependency could be removed.
- **Result:** Service restored, safeguard introduced, process changed.

**Limits:** No exact outage duration or customer count. Whether the check was automated, and whether the dependency cleanup was completed, are not confirmed. Don't merge the separate pipeline hardening into this incident.
**Probes:** Why did you delete it? What would you check before the same kind of change now? What changed afterwards?
**Angle:** The app went down; own it plainly, don't frame it as a near miss. The lesson: when production depends on a file, check what uses it before removing it.

### ai-agent

Designing Remuner's conversational agent for questions about commissions and plans. Deck: [case-deck-ai-agent.md](decks/case-deck-ai-agent.md). Evidence: [register, Conversational AI agent](../evidence/experience-facts.md#conversational-ai-agent).

**Opener:** "At Remuner, I designed a conversational agent for questions about commissions and sales plans."

- **Context:** Reps and managers needed understandable answers about their pay, and different roles had different access.
- **My responsibility:** As sole designer: UX and UI, conversation design, answer formats, role-based context and the design-side boundaries. There was no PM.
- **Actions and why:** Engineering established what data was available. Agreed the scope with the founders and Engineering. Designed supported questions and refusals, and direct answers with context, using tables or lists where useful. Iterated tone, terminology and presentation after launch.
- **Result:** Released to all customers before March 2026. Mixed feedback and continued iteration; no reliable adoption, accuracy or business metrics.

**Limits:** Engineering owned the architecture. The agent could return wrong numbers when customer-specific calculation code was outside its context, and the recorded fix is unclear; don't claim it was solved or that answers were guaranteed correct. Data freshness appeared elsewhere in the app, not in the chat.
**Probes:** What was out of scope? How did you assess accuracy? What did you personally own? How did you tell a useful answer from a correct one?
**In reserve:** No complaint or follow-up was a weak operational signal, not ground truth. For scaling-feedback questions, see [reference/ai-agent-feedback-cheat-sheet.md](reference/ai-agent-feedback-cheat-sheet.md).

### ic-dashboard

Users said the rep dashboard "wasn't intuitive"; interviews showed they meant different things. Evidence: [register, IC dashboard](../evidence/experience-facts.md#ic-dashboard-clarifying-vague-feedback).

**Opener:** "At Remuner, users said the rep dashboard wasn't intuitive, but interviews showed they meant different things."

- **Context:** "Not intuitive" didn't say whether the problem was the UI, missing information, or understanding compensation.
- **My responsibility:** Found who gave the feedback, arranged the interviews, and designed all the changes as sole designer.
- **Actions and why:** Found three problems: understanding the calculation, how metrics related, and quarterly payment timing. The team compared them with existing evidence and prioritised by severity. Added a calculation summary with access to the full detail, and period and payment information. Tested with users.
- **Result:** Shipped. In testing, users understood the information they had been missing. Qualitative, no quantified impact.

**Limits:** Prioritisation and implementation were shared. No specific metric-relationship solution is recorded. Don't merge with the manager-view redesign.
**Probes:** What did you ask? How did you prioritise? What did testing show? Did it ship?

---

## Kings of Mambo

Neither story below is in the evidence register yet. Both are Manel's account as written in the old prep.md; confirm the details before using them in depth.

### kom-deadline

A client e-commerce build (WordPress) where the scope was larger than the timeline could absorb.

- **Context:** During the build it became clear the agreed date wouldn't hold.
- **Actions:** Called the client proactively. They were angry; absorbed it without defensiveness or excuses. Once it settled, proposed shipping on the original date without purchase functionality, with "coming soon" messaging and an email capture form. Decided together with the client.
- **Result:** The client got a live site on time and built an audience before the shop opened.

**Angle:** Proactive communication over a silent overrun. The partial launch was a product call, not a patch. Don't frame it as heroic: it was a miss handled professionally. The lesson was to renegotiate scope at the first sign of slippage, not at the deadline.

### kom-lofi-feedback

A client stopped a review of high-fidelity explorations and asked to go low-fidelity first.

- **Context:** The hi-fi work was done and good. The feedback was about sequencing, not quality: a process mistake, not a skill mistake.
- **Change:** Restructured design phases: low-fi and stakeholder validation before any hi-fi, because being wrong at hi-fi costs much more than being wrong at lo-fi.

**Angle:** The change lasted; it still shows in how you work. Don't frame it as "I was inexperienced": you were confident in the work, and the feedback named something true you hadn't named yet. In a live challenge the vision still comes first ([playbooks/live-challenge.md](playbooks/live-challenge.md)): "validate first" read as conservative at Factorial.

---

## Gaps

Flag these when a round could hit them. Never fill them with invented material.

- **Kings of Mambo incidents.** Eleven years of client work, underused. Pick two or three real incidents usable in a senior IC interview (stakeholders who don't listen, a project that failed) and say which are fine to tell.
- **Disagreement with a manager or a PM.** `manager-view` is a disagreement with leadership, not a manager or PM. The Remuner AI project had no PM. Engineering capacity pushback (`maker-days`) is not a PM conflict.
- **Mentoring someone.** Mentoring is confirmed; an individual episode with a result is still needed.
- **Number of designers and engineers each system served.** Abacum: about six product designers across five squads. Remuner: four people worked from the libraries in the last months. The Kings of Mambo figure Manel gave Perk (about 15 to 16 designers) isn't in the register.
- **A concrete Remuner fix-versus-defer episode** for `remuner-ds`.
- **Accessibility gap found after shipping**, **regulated-industry pattern restrictions**, **research with specialised users**: see the enterprise gaps in [question-bank.md](question-bank.md#gaps-no-direct-material-do-not-invent).
