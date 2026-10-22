# Alan — live technical interview (case round)

Rebuilt 2026-10-14 from Alan's official prep page and its Loom walkthrough. Sources: [canonical record](../../applications/records/alan-product-designer.md), Celine's emails supplied by Manel on 2026-10-14, [Alan prep page](https://alaninsurance.notion.site/Preparing-for-the-technical-product-design-interview-with-Alan-1191426e8be780759a55c5fa836cbf3b) and [Loom walkthrough](https://www.loom.com/share/871febee365a413e88d9d4c9f5d61bd6) (by a member of Alan's design team, dated 8 December 2025), both read 2026-10-14.

## Logistics

- **Date:** Friday 2026-10-16, 14:00–15:30 (Europe/Madrid, confirmed by Manel). Offline block 14:00–14:20, Meet 14:20–15:30.
- **Interviewer:** Christelle Mozzati, Product Designer. Hiring manager: Aiswarya Kolisetty. Recruiter: Celine Brunel. Whether Aiswarya joins is unknown.
- **Format:** 90 min. The brief arrives by email. 20 min offline, then 70 min on Google Meet.
- **Brief timing:** the Loom says the case may land 10–30 min *before* the start. Have your inbox open 30 min early and read it as soon as it arrives.
- **Tools:** Figma is their default; anything else is fine if you say so at the start. AI is allowed if you say when and how you used it (Celine, 2026-10-14). Output does not need to be polished.

**Domain is unknown.** Nothing from Alan says the case will be about health or insurance. Prepare the method, not the domain. The Alan-specific notes below apply only if the brief turns out to be about Alan's own product.

## Your interviewer: Christelle Mozzati

External research, checked 2026-10-15. Sources: [personal site](https://christellemozzati.com/), [GitHub profile](https://github.com/cmozzati) (company: Alan, location: Lyon), [getprog.ai profile](https://www.getprog.ai/profile/3350525) (search snippet only), [LinkedIn](https://www.linkedin.com/in/christellemozzati/) (not readable without login), and Alan's [Behind the screens](https://aiswaryak.substack.com/p/alan-design-behind-the-screens-9263628dcbb1) post (Aiswarya Kolisetty, 2022-08-26).

**Who she is**
- Senior Product Designer at Alan since March 2022 (about 4.5 years), based in Lyon. French; the interview is in English.
- Was a **Product Manager** before. At Unow (digital learning) she did design system, product design and product management.
- Earlier work leans on craft: branding, icons, illustration and web design (Mapado ticketing, Trackin delivery app, Copark parking app, WP Rocket, illustrations for Michelin). She has a Noun Project icon set, Dribbble and Behance.
- Taught digital design at Master 2 level (Bellecour École), curated design talks for BlendWebMix 2017, and has spoken on branding and product-centric startup design. Wrote about dark patterns and product management.
- Motto on every profile: "J'aime faire de belles choses avec des gens bien" (make beautiful things with good people).
- **Unknown:** which Alan team or product area she works on now. Don't guess in the room. If it comes up naturally, ask.

**Her on record about Alan (2022 post):**
- On research: "it's SO refreshing to have an in-house research team! We have access to fundamental research... It is a game changer."
- On async: "The no-meeting rule is key to take back control of your time."

**What this means for the session (inference)**
- **PM background:** she'll notice whether you frame the problem before jumping to solutions. Don't play PM to match her: she's a designer now, and this round hires a designer. Lead with the user journey, the break points and what the member sees at each step. Business impact gets one line and one signal (Celine's gap), not a section. Decided with Manel 2026-10-15.
- **She values research:** "What research or member verbatims do we have?" is a natural early question, and she can probably answer it.
- **Craft background:** the flow doesn't need polish, but a tidy, labelled board reads well to someone who taught design. Keep stickies aligned and frames named.
- **Written, async culture:** Alan decides through written GitHub issues (goal, context, proposals, then the author decides). Write your decisions on the board in that shape: goal, context, options, decision. Your board is your written argument.
- **Teacher and collaborator:** treat her like a teammate. Think out loud, ask what she'd expect, adjust when she pushes.
- **Don't** bring up her personal interests or older side projects. Asking about her work at Alan is fine; showing you've read her personal site is not.

## Alan context refresh (external research, checked 2026-10-15)

Only use this if the case is about Alan's product or it comes up in conversation. Never present a figure as something they told you.

- **Funding:** June 2026, €480M round led by Prosus at a €5.5B valuation, for international expansion and AI product development ([Prosus](https://www.prosus.com/news-insights/2026/prosus-leads-euros-480-million-funding-round-in-alan-to-shape-the-future-of-ai-powered-healthcare)). A Canadian outlet reports different dollar figures; use Prosus's.
- **Scale:** about 1.1 to 1.2M members; €800M ARR in Q1 2026, up 53% year on year; profitable in France. Headcount grows slowly relative to revenue, which they credit to AI.
- **Mo (AI health assistant):** available to all members in France. Runs on about 20 AI agents, and worrying conversations are escalated to the medical team within 15 minutes. Planned for Canada in 2027 ([The Logic](https://thelogic.co/news/alan-insurance-expansion-ai/), 2026-07-28).
- **Claims:** AI-assisted. Most reimbursements land within minutes, and rejections come with a plain-language explanation (same source).
- **Canada:** Alan Clinic mental health therapy in-app for Ontario members (February 2026, [Business Wire](https://www.businesswire.com/news/home/20260217347722/en/Alan-Launches-Alan-Clinic-in-Canada-Bringing-Mental-Health-Care-Directly-Into-the-Insurance-App)), licensed in Quebec, about 4,000 Canadian workers covered. Plans for four new countries in the next 18 months.

**If the case touches Alan's product (inference):** the likely ground is AI with a human fallback, trust around health data, explaining a decision to a worried member (rejected claim, not covered), or launching in a new market. Your Remuner AI-agent work (capability boundaries, trust patterns, structured answers) is the relevant past experience. In the flow, always design the moment where the AI hands over to a human and what the member sees while waiting.

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

Our recommendation, not Alan's: neither the prep page nor the Loom mentions preparing a board. Derived from their scoring categories, the "arrive with a structure" ask and the Dashinsky agenda. Optional; keep it to a few minutes of setup.

One Figma file with six labelled frames, left to right. Share the link at the start of the call.

Built 2026-10-15 as a FigJam template: [Live case board (template)](https://www.figma.com/board/Y18T6tOyf2ReDNt804AsEe). Duplicate it for each mock and for Friday; keep the template empty. After mock 1 (2026-10-15) it was trimmed: Directions uses sentence blocks instead of a table, and Facts, User state, North star, Option C, States, Guardrail and the written close are marked optional. During mock 2 Manel removed the agenda strip and North star. Synthesis now runs map → group stickies into 3–4 named groups → pick one out loud → one sentence. The sticky clustering shows the designer process; the sentence is what comes out of it (decided with Manel 2026-10-15).

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
- What does the user see or know at each step today? (Added after mock 2: in the Spendly mock, the app showed only "Submitted" / "Paid" and nobody asked.)
- Do we have research, support tickets or member verbatims on this?

**Business**
- Why is this a priority now? Which metric is the team accountable for?
- Is this mainly a growth, retention, cost-of-care or support-load problem?
- Does the buyer care about this, or only the user? (Alan: employer vs. member)

**Data**
- What do we know in numbers: volume, funnel, drop-off, contact reasons?
- Is there anything we believe but haven't measured?

**Constraints**
- What are we not allowed to do here, legally or by policy? Which decisions must stay with a person, and which can the product make? (Added after mock 1: the domain-agnostic way to find rules you don't know. If the answer is "you decide", state the assumption out loud.)
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
4. Alternative for Christelle: "You've been at Alan since 2022. How has Mo and the AI work changed what a designer actually does on a member journey?"

## Salary

Unlikely in this round. If raised: compensation is tied to assessed level; ask which level they're considering and the matching Spain package. Don't give a number first. Floor guidance is in `context/salary.md` (the 60k gate was relaxed 2026-10-11; no new number set).

## Rehearsal plan

- **Thu 15 morning:** Build the Figma board template, then mock case 1 with Claude playing the interviewer, on the 20/70 timing. Use Dashinsky's primary-care task (book 3.4, don't read the answer first), then compare.
- **Thu 15 afternoon:** Mock case 2 in a domain unrelated to health (e.g. a consumer marketplace or a B2B tool), so you practise the method rather than the domain. Review: was the synthesis explicit, and did a metric get named?
- **Fri 16 morning:** Short retry of the weakest block only. No new mock.
- **Fri 16, 13:30:** Inbox open, Figma file ready, screen share tested.

Mock briefs are made up for rehearsal and labelled as such. They are not predictions of Alan's case.

### Mock 1 result (2026-10-15, Juniper primary-care brief, Claude as Christelle)

Board: [Live case board (Juniper clinics)](https://www.figma.com/board/wxAxvXE8xlnFjWfzQ1NR0P). The session ended before the discussion block; the planned pushback was not delivered.

- **Strong:** opened with research, took the acute-vs-chronic challenge well, corrected own misreading of the 9-day wait, mapped a real break point (cancel only by phone → no-show), reached a flow.
- **Weak:** no time plan stated until asked; no constraint or "why now" questions; problem statement stayed a fact ("they don't need to go to the clinic") instead of a user problem; chosen direction (triage) didn't attack the mapped break point (no-shows); pick justified by assertion, refused to name what was given up; flow puts date picker before visit reason and is happy-path only; metric boxes empty, so Celine's impact gap stayed open.
- **Missed context that would have changed the pick:** software can't make triage decisions (a nurse must review), nurse capacity is limited, a value-based insurer contract makes avoidable visits costly from next year, booking API supports slot types, team is 1 PM + 4 eng for 6 months.
- **Fixes for Friday:** (1) ask constraints and "why now" before synthesising; (2) check that the pick fixes the break point you circled, and say what you give up; (3) say one user signal and one business signal out loud and write them down.

After the interview: run `/debrief-interview alan case`.

## Mock 2 result (2026-10-15/16, Spendly expense reimbursement, made-up case)

Scores (same 0–4 scale as mock 1): Problem-solving 3 · Strategic thinking 2.5 · User-centricity 3 · Collaboration 3.5. Up on every category.

- **Strong:** asked why now, success and constraints; dug into the manager quote (emails, filter, what "business expense" means); took the €50 rule and rebuilt option B; added employee-facing states when pushed; flow branches with two failure paths looping back to the employee, a status under every step, and the manual-correction idea; metrics named the team's baseline (19 days); guardrail included invalid expenses getting through.
- **Weak:** offline ran ~60 min against 20; synthesis picked the manager step with a reason the map contradicted (8 days submit vs 6 manager) and wrote the solution into the problem; A and B were the same kind of option; the third option (better manager notifications) was dropped on a guess, not data; pick justified by "more personas" and "I feel there's capacity"; never claimed the strongest point of B (checking at scan removes the 22% send-back, ~7 days each); flow first drawn from the list screen to "processed", not from paying to money received; manager notification for >€50 left unchanged; metrics had no targets and read the 30% "where is my money" figure as finance time.
- **Fixes for the live round:** (1) justify the pick with a number from their data; (2) metrics as baseline → target, one for the user and one for the business; (3) hard-stop offline at 20 min and draw the flow from the real trigger to the real end.

## Debrief: live technical interview (2026-10-16)

Source: Manel's account on 2026-10-16, plus the board as left in the Figma file "Technical # 1 - Therapist - Manel (Copy)" (read through the Figma bridge the same day). Christelle Mozzati was the only interviewer. Manel's own read: it went well, but not sure.

### The brief (Alan's own product)

"Find the right therapist." Design the experience that improves matching between members and therapists for video consultations in the Alan app. Facts from the brief:
- Four therapists, each with distinct specialisations (anxiety, depression, panic attacks, self-confidence, burn-out, anger management).
- France only; digital mental health is still "new" there compared with the US or UK.
- Initially for a selected group of members. First version to ship in 2–3 weeks, as part of the member coverage plan.
- A therapy session lasts about 45 minutes; a general consultation lasts about 15.
- The biggest drop-off in the current flow is the "Select a therapist" screen.
- Booking and video calls already exist; no third-party solution is needed.
- Deliverable: an overarching concept, distilled into a defined MVP, shown as a low-fidelity user journey map. Rethinking the therapist experience is out of scope.

Alan's board template suggested Discovery (on your own) 20 · Problem definition 20 · Solution exploration 20 · Deliverable 20 · Q&A 10.

### What happened

- **Discovery:** Manel went through the whole question list and Christelle answered each one. Answers captured on the board: there are fewer doctors and more patients, and information is hard to reach. Members are less sensitive to mental health. Mental health issues lead to work problems and sick leave. More members have mental health problems and want therapy. Booking can take 3 to 6 months. The team is 2 engineers, with 2–3 weeks to build.
- **Synthesis on the board:** "For patients being reactive instead of preventative the problem is they are not used to care for mental health and booking times." Evidence cited: low sensitivity to mental health, and booking taking up to 6 months. Member outcome: look after their mental health. Business outcome: fewer sick leaves and absences, and healthier employees who perform better.
- **Exploration:** only Option A is written on the board. It's a mental health awareness section, plus signals throughout the app. Christelle then drove the exploration with direct questions:
  - *How do we make it easier for a member to book a therapist?* Manel proposed a free-text "Please explain what you need" step, where AI reads the described symptoms and points to a recommendation, with "Or pick one" topic triage as the alternative.
  - *How could "Choose your therapist" make it clear what the member is choosing?* Manel proposed expanding the cards with what each therapist does, their methods and a description. Manel drew a "Recommended" / "Other options" list showing availability and language, and a sheet over "Choose your therapist" with the therapist's methods.
- **Edge cases:** Manel raised these unprompted: no therapist available, or the calendar full for a long period so the member has to choose another option. Discussed out loud; not drawn.
- **Flow on the board:** drawn in red over Alan's app screenshots: Clinic → "Please explain what you need" (or topic triage) → recommended therapists → booking → teleconsultation, with a therapist detail sheet.

### Questions the prep didn't cover

- **"How do we know we made a good match between member and therapist?"** Manel's answer: a short follow-up form asking whether the member is satisfied and how to improve the flow.
- **Metrics:** Christelle asked. Manel first went back to awareness: a section explaining mental health and therapies, with entry points across the app, to move members from reactive to preventive. Manel then named the number of consultations, compared with the current number, as the metric. No target was stated, and no metric was written on the board.

### Stories used

None. The session stayed on the case; no past-project story came up.

### What we learned about Alan

- Christelle works on the **insurance** side of the product.
- About **14 designers** and a **research team of 5–6**. Work is organised in groups or pods that coordinate several verticals (Manel's recollection of the wording).
- There is a **design system** in place. A separate team maintains consistency across platforms and markets. Christelle described them as the "guardians" of the design.

### Next step

Christelle will talk to Celine, and Celine will send the decision. If Alan moves forward, Manel understood the next round would be a getting-to-know-you conversation with another person from the design team, or with the head of the design group (unconfirmed). No timing was given.

### Outcome (2026-10-21)

Rejected. Celine's email named strategic awareness (why now for Alan, business case, other countries), honesty about gaps, taking feedback well and adapting when the AI option was ruled out. The reasons given: discovery structure and anticipating key user challenges "required significant guidance", plus a need for more proactive simplification and time management. This matches the debrief above: the synthesis came from the vision paragraph, and Christelle's questions steered the session back to matching. Record: `applications/records/alan-product-designer.md`.
