# AI Agent case — raw intake

Status: intake in progress (started 2026-07-14). This file collects the material for the Remuner AI agent case study. Once distilled, the summary moves to `context/portfolio.md` and the case ships as `portfolio/public/cases/ai-agent.html` (or similar). Same pattern as `design-systems-notes.md`.

Strategic frame (2026-07-14): AI-assisted design and shipped AI product work are now named qualifications in target-segment JDs (memory.md 2026-07-10) and a standing interview thread (Factorial, two rounds). This case converts positioning differentiator #4 ("Shipped AI product work") from a bullet into evidence. The case is a judgment record about designing AI-mediated work: intent scoping, trust, error handling. It is NOT written in "future of design" manifesto language.

---

## Facts on record (verified, safe to use)

From memory.md 2026-06-12 / 2026-07-06 and context/portfolio.md:

- A chat panel plus embedded answers inside the app. Sales reps consult their own data: ERP line items, aggregations by period, where to focus, understanding their sales plan and decisions based on it.
- Managers were real users too. Most had a compensation plan of their own and could query team info through the agent.
- Released to all customers before March 2026 (say "released to all customers", not "GA" — jargon rule 2026-07-09).
- Manel owned: full UX/UI, conversation design (tone, answer formats), capability scoping with engineering, trust and accuracy patterns.
- CORRECTION (2026-07-15, Manel): there was NO PM during the agent project. The PM joined later, during the AI admin period (the admin-side plan builder exploration, late 2025 / early 2026). The CEO and CTO were acting as PMs and were involved in scope decisions alongside the engineers and Manel. Precise claim: Manel owned the design side of capability scoping; the boundary was decided between CEO, CTO, engineers, and Manel. Never say "with the PM" about the agent, and never claim scoping was designer-and-engineers only. The canonical description in memory.md 2026-06-12 and context/portfolio.md says "capability scoping with PM/eng"; correct it when propagating.
- Post-release feedback was mixed. Iterated on tone, response format, and per-customer terminology: the same object was a "deal", a "contract", or an "item" depending on the customer.
- Pre-release user interviews showed strong interest ("a genuine tool to improve their work").
- Evidence position: no claimable metrics or named signal. Own the absence in the outcomes section. The post-GA iteration loop is the story.
- SEPARATE project from rep letters / agreement lifecycle. The agent does not generate letters. Never conflate.
- Sole designer at Remuner throughout.

Continuity thread worth using: the per-customer terminology problem rhymes with the Dataset Manager language-mismatch insight (data types vs dimensions). Same pattern, new layer: the gap between system language and user language, and designing the translation.

---

## Proposed case structure (draft, judgment-first)

1. **Overview** — what shipped, who used it, one line on scope ownership.
2. **My role** — sole designer; conversation design, capability scoping, trust patterns. Not just the chat UI.
3. **The problem** — what reps did before the agent existed and why that was worth solving. [NEEDS INTAKE Q3]
4. **Scoping what the agent should answer** — the decision record: what it answers, what it refuses, why. This is the restraint section and the strongest AI-era judgment signal. [NEEDS INTAKE Q2]
5. **Designing for trust** — what a rep sees before believing an answer about their own money. Answer formats, grounding, error and uncertainty states. [NEEDS INTAKE Q1]
6. **When the answer was wrong** — post-release mixed feedback and the iteration loop: tone, response format, per-customer terminology. Partially documented, needs specifics. [NEEDS INTAKE Q4]
7. **Outcomes** — own the absence of metrics directly. Anchor: released to all customers, pre-release interview signal, the iteration loop as evidence the team treated it as a product, not a demo.

---

## Intake questions (answers verbatim from Manel, then distilled)

### Q1 — Trust and answer anatomy (most important)
When the agent answered something consequential ("your Q2 payout is X", "focus on these deals"), what did the rep actually see? Was the answer grounded in visible data (source line items, a calculation breakdown, a link to the plan rule)? What did the agent do when it wasn't confident or couldn't answer?

ANSWER (2026-07-14, verbatim): "The rep saw the answer first and the detail how the answer was built and the rest of the context, plan rules, etc."

Distilled: three-layer answer anatomy. The direct answer leads, the derivation (how the number was built) comes second, the surrounding context and plan rules ground it last. Answer-first with the evidence attached, not evidence-first.

STILL OPEN from Q1:
- What did the derivation layer actually show: line items? a calculation breakdown? Was it expanded by default or behind an interaction?
- What happened when the agent couldn't answer or wasn't confident? Refusal message, fallback to a human, silence?

### Q2 — Capability scoping
What did you, PM, and engineering decide the agent should NOT do, and why? Examples of the kind of thing that matters: could it compare a rep's earnings with teammates (privacy), could it make forward-looking projections, could it take actions or only answer, were any data sources excluded because accuracy couldn't be guaranteed?

ANSWER (2026-07-14, verbatim): "It depended on the type of questions. We gave specific instructions to only answer questions related to comissions and plans. Nothing else. The rest of questions where routed to a default answer, something like 'Sorry, I can only asnwer questions related to your comissions'. That was the answer to 'who's the president of spain?' or similar. Then, on the other side, we defined a release path to bring more available answers. So first we defined what can the agent respond and what not and improve from there."

Distilled:
- Hard scope boundary defined up front: the agent answers questions about commissions and plans, nothing else.
- Off-scope questions routed to an explicit refusal ("Sorry, I can only answer questions related to your commissions"), including general-knowledge bait like "who's the president of Spain?". INTERNAL ONLY (Manel, 2026-07-16): the sample wording and the president-of-Spain example do not appear in live copy; the case states the refusal concept without quoting it. Fine for interview conversation.
- A release path was defined to expand the answerable set deliberately over time. Define what it can answer, refuse the rest, widen from there. The inverse of shipping broad and patching failures.
- This partially answers Q1's open failure-mode item for OFF-scope questions. Still open: IN-scope failures (see below).

STILL OPEN from Q2:
- Who defined the boundary and how was it negotiated with engineering (no PM existed then; see 2026-07-15 correction above)? Was there pressure to launch broader?
- Privacy-type exclusions (teammate comparisons, team data visibility for reps vs managers): explicitly scoped, or never came up?
- What did the release path actually add after launch, if anything, before March 2026?

### Q3 — Problem origin
What triggered the project? What were reps doing before: asking managers, filing support tickets, mistrusting their payout numbers? Was there a business driver (support load, churn signal, sales pitch)?

ANSWER (2026-07-14, verbatim): "So before the agent, reps could see their commissions and plan setup in the platform. It was not easy and were doing steps towards improving it but at some point we saw a fastest way for reps to get all this info in a simple chatting way. In terms of business driver, we wabted to have a sales differentiator, specially the plan builder that came later when we were exploring the admin side. And leadrship was also pushing hard as the rest of the competition was also doing something similar."

Distilled:
- Before: the information existed in the platform (commissions, plan setup) but was hard to reach. The team was already improving those surfaces incrementally.
- The pivot insight: chat was a faster path to the same information than continuing to improve navigation. The agent collapsed a navigation problem, it didn't expose new data.
- Business driver: sales differentiation, plus leadership pushing hard because competitors were shipping similar features.
- The later admin plan builder was part of the same differentiation push. CAREFUL: that is the separate "sales rep plan creation experience for admins" project (designed, partially built, never confirmed shipped). Keep it out of this case's claims.
- Case framing: the honest origin is "AI feature under competitive pressure." The design judgment story is turning that mandate into something scoped and trustworthy rather than a checkbox. Do not dress it up as user-research-led discovery; the pre-release interviews validated interest, they didn't originate the project.

### Q4 — What broke post-release
The feedback was mixed. Concretely, what did users complain about? Wrong numbers, wrong tone, answers too long, terminology mismatch, something else? Pick the 2 or 3 specific complaints that drove the iterations.

ANSWER (2026-07-14, verbatim): "I don't reacall specific moments but I know it happened. There were 2 main problems detected, one the rep don't understand the number because the complex was complex. The other one the rep gets numbers that don't match and that could happen because of not up-to-date data. It was very difficult the agent got it wrong because afaik it was only reading the calculations the platform did."

Distilled:
- Architectural trust fact: the agent did not compute anything itself. It read the calculations the platform had already made. Wrong-math answers were structurally unlikely for standard configurations (Manel's qualifier: "as far as I know", keep the hedge honest, never claim "never got it wrong").
- CORRECTION (2026-07-16, Manel): wrong numbers DID reach users, and most traced to custom code. Clients with requirements that couldn't be achieved through the product's front end had custom-coded calculations, and the agent was not aware of that code. It answered from the standard calculation path, so its numbers could be wrong for exactly those clients. This supersedes the "very difficult the agent got it wrong" framing: the read-only guarantee held only inside the standard configuration. Case framing: this is the system-boundary failure mode (the agent's model of the product didn't cover per-client customization). OPEN: what, if anything, changed once this cause was found (agent made aware of custom results? disclaimer for affected clients? unresolved at departure?).
- Failure mode 1, comprehension: the number was correct but the rep didn't understand it, because the compensation plan itself was complex. The agent's job became explaining a correct number, not just delivering it.
- Failure mode 2, freshness: reps saw numbers that didn't match their expectation or other sources, traced to not-up-to-date data (sync lag), not to the agent's reasoning.
- No specific recallable incidents. Case copy frames these as the two detected problem classes, never as invented anecdotes.
- Framing note for the case: neither failure mode is "the AI was wrong." Both sit around the model: explanation design and data freshness. This is the honest, senior version of "what happens when the AI is wrong."

FOLLOW-UP ANSWER (2026-07-14, verbatim): "There was a constant improvement of the agents involved in the answers. I can remember what were the specific changes but I kown we were trying different ways to show the info and adapt to the questions, so when no follow up questions were made or no thumbs down feedback recorder, we took that as a 'valid' answer. For data recency, we already added a last updated date but it was global, not specific of the chat."

Distilled:
- Multiple agents were involved in assembling answers, and they were continuously improved. Manel's side of the loop: trying different ways to show the information and adapting formats to question types. Specific individual changes not recallable; frame as an ongoing loop, not as named iterations.
- Architecture detail (2026-07-14, Manel: "I was not part of that setup"): the system ran different agents per app vertical (one for the plan, one for integrations and items, etc.) with an orchestrator that routed each question to the corresponding agent. Reason: a single agent produced inconsistent results, most likely from the amount of information and context it had to manage. OWNERSHIP RULE: this was an engineering decision and build. Manel can describe it and why it existed; he never claims he designed or proposed it. Same crediting discipline as the Abacum pipeline ("an engineer built the original pipeline").
- Answer-quality proxy, concrete and case-worthy: no ground truth existed for answer quality, so behavior was the signal. An answer that produced no follow-up question and no thumbs-down was treated as valid.
- EXPANDED (2026-07-16, Manel): the chat had thumbs up AND down buttons. A thumbs-down opened a textarea asking the user to describe the problem. All those interactions were captured and reviewed weekly. All questions and answers the agents produced were also captured, so the review covered the full conversation record, not just flagged answers. This is the operational governance loop of the case (same signal class as the DS monthly FE meetings).
- CORRECTION (2026-07-21, Manel): the case draft had overclaimed the format-selection process, stating "formats that reduced follow-up questions won" as if a formal production A/B on follow-up rate decided the winning format per question type. Not accurate. The real basis for format choice was a mix: (1) prior evidence from elsewhere in the platform, where lists and tables were already known to outperform paragraphs for this kind of data, validated with users there; (2) general design judgment, a table doesn't work rendered as paragraph prose; (3) the chat format choices were tested directly with users in the prototype before launch. The no-follow-up/no-thumbs-down signal (see above) was a post-release answer-validity check, not the mechanism that picked between format variants. Live copy corrected to reflect this.
- Data freshness: the app already had a last-updated date, but it was global, not shown in the chat. Honest limitation: the freshness mismatch was never fully solved inside the conversation. Own this in the case; it reads as maturity, not weakness.

### Q5 — Chat panel vs embedded answers
Why two surfaces? What lived in the chat and what was embedded in the app? Was one of them the original scope and the other added later?

ANSWER (2026-07-14, verbatim): "I don't get this question. There were 2 surfaces. One was the regular app where reps could navigate plans, comissions and periods and then there was the AI chat surface where they could get answers but it was not depending on the section they were in the app. No more surfaces. The answers of the chat were then tailored to show the specific content, tables, lists, etc."

Distilled:
- CORRECTION to the canonical description ("a chat panel plus embedded answers inside the app", memory.md 2026-06-12 and context/portfolio.md). There was ONE AI surface: a global chat panel inside the app, not tied to the section the rep was in. There was no second embedded-AI surface.
- "Embedded answers" actually means the answers themselves rendered as tailored structured content: tables, lists, specific formats per question type. This is the concrete meaning of "answer formats" in Manel's documented conversation-design ownership.
- Propagate this correction to context/portfolio.md and memory.md at distillation time so no CV or interview answer repeats the two-surface phrasing.

### Q6 — Visual evidence
What can be shown? Screenshots, screen recording, redacted conversation examples? The other cases lean on before/after images and video evidence. A case with no artifact is weaker.

ANSWER (2026-07-14): Manel has the Figma file and the Remu components (the Remuner Components library has 6 Remu component sets: saved chats, header, footer, content states). He can rebuild a conversation from them for the case. The public marketing page https://www.remuner.com/remu/ serves as inspiration only; its videos and images will not be reused.

Artifact plan (revised 2026-07-16, refusal image dropped as redundant with the reach diagram):
1. HERO — annotated answer anatomy: a conversation rebuilt from the Remu Figma components with three callout labels (the answer, how it was built, the plan rules behind it). Include a table-formatted answer so the formats point is shown, not told.
2. REACH DIAGRAM — the agent's line of sight: platform standard calculations (readable), orchestrator + per-vertical agents, chat surface; custom-code calculations drawn explicitly OUTSIDE the boundary. Explains scope, architecture, and the custom-code failure mode in one image. Precedent: design-systems-pipeline.svg.
3. FEEDBACK LOOP — cycle diagram: capture every Q&A → thumbs up/down → textarea on thumbs-down → weekly review → format changes shipped.
- Rebuilt artifacts show only capabilities that existed at departure (March 2026), populated with invented-but-realistic data clearly of Manel's making. Never screenshot-style fake real customer data.
- Any diagram follows context/brand.md (read before producing visual output).

What the public page claims today (fetched 2026-07-14), for calibration:
- Remu is now marketed as "your AI Compensation Manager" covering plan design ("Build tiers, multipliers, and simulations in minutes"), instant Q&A for reps/managers/Finance, and payout forecasting ("What if I close this deal?").
- Public example questions match Manel's era and are safe phrasing inspiration: "How much am I making this quarter?", "Which deals matter most for my quota?".
- HARD RULES: the case claims only what existed at Manel's departure. Admin-side plan design (building tiers and multipliers) is post-departure or admin-side scope; do not claim it. The page's metrics (90% admin task reduction, 15% performance increase, +2 daily usages) are the company's current marketing claims; Manel never cites them as outcomes of his work.
- Useful confirmation: the Q&A agent became the company's headline product surface. "The feature I designed is now the company's flagship marketing page" is a legitimate, checkable signal for the outcomes section, phrased carefully (it evolved after his departure).

CORRECTION (2026-07-20, Manel, while reviewing ai-agent-reach.svg): the "Integrations agent" node was wrong, it duplicated the "Items agent" (both read ERP/line items). The real third vertical was a Simulator agent: reps could already simulate earnings in the product with sliders and inputs for the metrics they were measured on, moving them to see possible payouts. The chat agent could answer what-if payout scenarios using that same simulator, and this existed pre-departure. This supersedes the HARD RULE above insofar as it named "simulation" as post-departure-only; what's post-departure is the admin-side plan-building simulation ("Build tiers, multipliers, and simulations in minutes"), not the rep-facing what-if payout scenarios the chat agent already answered. The vertical agent set is: Plans agent (compensation plans), Simulator agent (what-if payout scenarios), Items agent (ERP line items, one agent per vertical). ai-agent-reach.svg and the Scope section of the live case were updated to match.

---

## Rules for this case

- No invented metrics, no invented anecdotes. Gaps stay gaps until answered here.
- No "AI-era UX" editorializing in the live copy. The thinking shows through the decisions, not through claims about the profession.
- No names of colleagues or customers in live copy. Roles only.
- All principles.md rules apply: no em dashes, length caps, outcome-list pattern, humanizer pass before output.
