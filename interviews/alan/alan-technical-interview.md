# Alan — live technical interview (case round)

Rebuilt 2026-10-14 from Alan's official prep page and its Loom walkthrough. Sources: [canonical record](../../applications/records/alan-product-designer.md), Celine's emails supplied by Manel on 2026-10-14, [Alan prep page](https://alaninsurance.notion.site/Preparing-for-the-technical-product-design-interview-with-Alan-1191426e8be780759a55c5fa836cbf3b) and [Loom walkthrough](https://www.loom.com/share/871febee365a413e88d9d4c9f5d61bd6) (by a member of Alan's design team, dated 8 December 2025), both read 2026-10-14.

## Logistics

- **Date:** Friday 2026-10-16, 14:00–15:30 (Europe/Madrid, confirmed by Manel). Offline block 14:00–14:20, Meet 14:20–15:30.
- **Interviewer:** Christelle Mozzati, Product Designer. Hiring manager: Aiswarya Kolisetty. Recruiter: Celine Brunel. Whether Aiswarya joins is unknown.
- **Format:** 90 min. The brief arrives by email. 20 min offline, then 70 min on Google Meet.
- **Brief timing:** the Loom says the case may land 10–30 min *before* the start. Have your inbox open 30 min early and read it as soon as it arrives.
- **Tools:** Figma is their default; anything else is fine if you say so at the start. AI is allowed if you say when and how you used it (Celine, 2026-10-14). Output does not need to be polished.

**Domain is unknown.** Nothing from Alan says the case will be about health or insurance. Prepare the method, not the domain. The Alan-specific notes below apply only if the brief turns out to be about Alan's own product.

## What they score (official, verbatim categories)

1. **Problem-solving:** clarify the problem, structure the approach, work within the time.
2. **Strategic thinking:** balance assumptions, business constraints and data.
3. **User-centricity:** reason about user needs and turn them into a **user journey, not UI**.
4. **Collaboration:** ask questions, synthesise context, refine ideas in real time.

**The end deliverable is one user flow.** Screens are not expected. The Loom says the flow can wait until the last 10–15 minutes and warns against rushing to it.

## The two things that decide this round

1. **Synthesis.** The Loom names the common pitfall: gathering lots of context without synthesising it. Stop after the questions, take a few minutes to synthesise (you can say "give me three minutes to synthesise"), and write down the problem, assumptions and hypotheses before you ideate.
2. **Celine's gap from round 1:** your answers on direction and impact stayed general. In this round, make it concrete: name the problem you chose, the direction, the tradeoff, and **which user and business signals would show it worked**. Say a metric out loud and put it on the board.

## Time plan (Alan's recommended split)

| Block | Time | What's on the board at the end |
| --- | --- | --- |
| Offline | 20 min | Brief restated in your words · facts vs. assumptions · your question list, ranked · a first guess at the core problem |
| Discovery | ~20 min | Answers captured as stickies under User / Business / Data / Constraints |
| Synthesis | ~5 min inside discovery | Problem statement · 2–3 assumptions · hypothesis · success signals |
| Ideation and flow | ~30 min | 2–3 directions with tradeoffs, one chosen with them, then the flow at the end |
| Discussion | ~20 min | Pros/cons of your choices, what you'd test first, what comes next |

Say at the start how you plan to use the time. Alan's page asks you to arrive with a structure, so stating it scores on its own.

## Figma board: set up before Friday

One Figma file with six labelled frames, left to right. Share the link at the start of the call.

1. **Brief:** paste it, highlight key words, list your assumptions.
2. **Questions:** your ranked list, with answers added as they come.
3. **Synthesis:** use this template:
   > For **[user]** in **[situation]**, the problem is **[X]**, shown by **[evidence they gave]**. If we solve it, members **[outcome]** and Alan **[business outcome]**. We're assuming **[A1, A2]**. We'll know it works if **[signal]**.
4. **North star:** one or two lines on what this experience looks like if Alan gets it fully right. This is the Factorial lesson (2026-07-02): show the full ambition first so your scoping reads as a choice. In Alan's format it stays short.
5. **Directions:** 2–3 options compared on member value, business impact, effort/risk and trust. Mark the one you'd pick.
6. **Flow:** entry trigger → steps → exit, with 2–3 important states (error, not covered, uncertain, human handoff). Annotate the decisions on the flow itself.

## Starter questions (Alan asks you to bring these)

Pick 6–8 once you have the brief. Ask the most useful first, not all of them.

Written generically. If the brief is about Alan's product, swap in the Alan versions in brackets.

**User**
- Who is the user here? Is the person who pays the same as the person who uses it? (Alan: member, employer/HR admin, or clinician? Which country?)
- What triggers this journey? What are they trying to get done at that moment?
- What happens today, and where does it break: drop-off, support contacts, complaints?
- Do we have research, support tickets or member verbatims on this?

**Business**
- Why is this a priority now? Which metric is the team accountable for?
- Is this mainly a growth, retention, cost-of-care or support-load problem?
- Does the buyer care about this, or only the user? (Alan: employer vs. member)

**Data**
- What do we know in numbers: volume, funnel, drop-off, contact reasons?
- Is there anything we believe but haven't measured?

**Constraints**
- Sensitive data or regulation: who is allowed to see what? (Alan: health data, medical confidentiality)
- One market or several? (Alan: France, Spain, Belgium, Canada)
- Is a human in the loop (support, operations, experts), and what does that cost? (Alan: care team, doctors)
- Engineering or timeline limits? Existing patterns in the app we should reuse?

**Scope**
- What would you like to see by the end: one flow on app, web, or both?

If they ask what features you'd add, turn it into a question about which decisions or tasks the user is trying to complete, then work back from that (Factorial lesson, 2026-07-01).

## Alan domain context (only if the case is about Alan's product; external research from round 1, inference flagged)

Alan sells health insurance mainly through employers. Employees become members and get insurance, care access (Alan Clinic: doctors by chat or video), prevention and reimbursements in one app. Operates in France, Belgium, Spain and Canada. **Inference, and only if the case is about Alan's own product:** possible territory includes reimbursements and coverage understanding, getting care quickly, onboarding, prevention engagement, and employer admin tasks. Don't present any Alan metric as known; ask for it.

## Ideation moves that score

- Diverge on purpose. Pick options that differ in kind: self-serve vs. human-assisted vs. proactive/automated. Avoid three versions of the same idea.
- Bring the interviewers into convergence: "Given what you said about [constraint], I'd drop B. Does that match what you'd expect?" The Loom says that involving them makes convergence easier.
- Name the tradeoff in product terms, not as "validate first". If they challenge your scope, name the specific assumption v1 tests and what you'd lose by automating before members trust it (Factorial lesson, 2026-07-01).
- When they add new information, say what it changes: "That changes my assumption about X, so I'd move to Y."

## From the Dashinsky book: what applies to this round

General takeaways are in [prep.md](../prep.md) ("Live design challenge"). These are the ones that change something for this round:

- **Check whether the buyer and the user are different people,** whatever the domain. If the case is Alan's product, they are: employers buy, employees use.
- **Put the user's emotional state in the context notes** (rushed, anxious, money at stake). It justifies choices like reassurance, clear costs and a human fallback. Especially relevant if the case is health-related.
- **Agenda on the board:** write Discovery → Synthesis → Directions → Flow → Measure in the first minute. This is Alan's "come with a structure", made visible.
- **Choosing a direction:** quick reach/value/effort placement of 2–3 options, out loud, then pick. Answers Celine's "how you choose a direction".
- **Metrics:** one member metric, one business metric, one guardrail (e.g. fewer support contacts *without* lower satisfaction, or faster care access *without* more unnecessary visits). Answers Celine's impact gap.
- **Build the flow from a task list,** then add the step before (what triggers it) and the step after (what the member needs next).
- **Ignore the book's time split.** It spends 30 of 60 min on UI. Alan wants a journey, with the flow coming last.

## Close (last ~5 min, or when asked)

Recap in five lines: problem → direction chosen → tradeoff accepted → signals for member and business → what you'd test first and what comes after v1.

## AI use: decide now

Recommendation: **work in Figma by hand during the live part.** They're scoring how you think and collaborate in real time, and an AI step in front of them uses up that time. If you use AI offline (e.g. to restate the brief or check your question list), say so at the start in one sentence: what tool, what for, and that the decisions are yours.

## If the discussion turns to past work

Use Dataset Manager as the direction-setting example, since it's the clearest answer to Celine's gap. Memory chain: UX request → proposed research first → users think in Excel, not SQL → effort objection from Product/Eng → protect existing datasets → shipped, first-session setup (qualitative). No numeric business result; say so. Card A in [battle cards](../behavioral-battle-cards.md) for follow-ups.

Answer drafted 2026-10-13 from Manel's account and the register:

> At Abacum, I was initially asked to improve dataset configuration so customers could move away from editing JSON files. I wasn't convinced that improving the interface alone would solve the problem, so I recommended research before committing to a direction. Testing showed that finance users could explain the transformations they needed using Excel functions, but struggled to express them in SQL. I recommended an ordered list of actions on the dataset, combined with language closer to what users already knew. Product and Engineering were concerned about the development effort; they needed to review the evidence. I advocated the more familiar approach because the goal was customer autonomy. We also had to protect datasets existing customers already had. The guided product shipped, and we had qualitative reports of customers reaching a working configuration in their first session. Reducing dependence on implementation specialists was the intended business benefit; I don't have a measured business result to claim.

Limits: extension of the existing modeling language, not a new one from scratch. No quantified business impact, no zero-loss migration claim.

## Questions for them (end of the session)

1. "How close was this case to a problem the team is actually working on? What did you end up doing?"
2. "In this team, who decides which problem a designer works on, and how early is design involved?"
3. "What separates a strong designer here in their first six months from an average one?"

## Salary

Unlikely in this round. If raised: compensation is tied to assessed level; ask which level they're considering and the matching Spain package. Don't give a number first. Floor guidance is in `context/salary.md` (the 60k gate was relaxed 2026-10-11; no new number set).

## Rehearsal plan

- **Thu 15 morning:** Build the Figma board template, then mock case 1 with Claude playing the interviewer, on the 20/70 timing. Use Dashinsky's primary-care task (book 3.4, don't read the answer first), then compare.
- **Thu 15 afternoon:** Mock case 2 in a domain unrelated to health (e.g. a consumer marketplace or a B2B tool), so you practise the method rather than the domain. Review: was the synthesis explicit, and did a metric get named?
- **Fri 16 morning:** Short retry of the weakest block only. No new mock.
- **Fri 16, 13:30:** Inbox open, Figma file ready, screen share tested.

Mock briefs are made up for rehearsal and labelled as such. They are not predictions of Alan's case.

After the interview: run `/debrief-interview alan case`.
