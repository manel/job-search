# Behavioral interview battle cards

Prepared 2026-10-06. English cues for Alan and future interviews. These are retrieval aids, not approved verbatim answers. Sources: [experience register](../evidence/experience-facts.md) and [existing detailed story bank](datavant/datavant-star-examples.md). Current evidence supersedes older wording.

## Keep this selector visible

| What they ask | Choose | Memory chain |
| --- | --- | --- |
| Impact / research changed your mind / complex problem | A · Dataset Manager | Dependence → test → familiar language → working setup |
| Customer feedback / small change with impact / simplify a workflow | B · Dimensions | Leave task → embed basics → keep advanced separate → feedback |
| Pushback / influence / competing priorities | C · Maker Days | Capacity concern → co-led case → bounded week → production Button |
| Disagreement / mixed feedback / support a decision you challenged | D · Manager view | Workflow first → leadership chose redesign → preserve findings → mixed result |
| Failure / accountability / what you learned | E · Token file | Wrong assumption → outage → restore → required-file check |
| AI / ambiguity / trust / zero to one | F · AI agent | Pay questions → roles and limits → structured answers → launch, limits remain |
| Vague feedback you had to clarify | G · IC dashboard | Not intuitive → interview users → different causes → prioritise and test |
| Mentoring someone / helping them improve | Not yet a story | Mentoring confirmed; individual episode and result still needed |

## Answer shape: headline + four anchors

Take a breath, choose an episode, then open with why it fits: “A good example is …, where …”. Give **context → my responsibility → actions and why → result**. Aim for 60–90 seconds for the first answer; extend only when asked. Keep context to one or two sentences and spend most time on your decisions.

Name the result even when it is mixed. End there and let them ask a follow-up. “I” means your contribution; “we” means a shared decision or delivery.

If the prompt is unclear: “When you say impact, do you mean the customer outcome or the wider team impact?”
If you need a moment: “Let me think of a specific example.”
If you lose the thread: “Let me simplify that. The problem was … My contribution was … What changed was …”
If you have an adjacent story: “I have a related example, although it wasn’t feedback from a PM. Would that be useful?”
If you have no matching incident: say so. For a hypothetical question, explain what you would do; do not turn that into something you did.

## A · Dataset Manager — impact and changing direction

**Opener:** “At Abacum, testing changed our direction for a self-service data-configuration tool.”

- **Context:** Finance users depended on specialists and JSON configuration; autonomy was the goal.
- **My responsibility:** Led design and customer testing.
- **Actions / why:** Tested simpler UI plus SQL → users could express the logic in Excel but not SQL → took finding to Product and Engineering → team extended the familiar modeling language and guided configuration.
- **Result:** Shipped. Customers could reach working configuration in their first session; implementation team recalled standard setup taking roughly half the previous time.

**Evidence boundary:** Outcomes are recollection, not analytics. Do not say “I reduced time by 50%” or infer revenue, support-ticket reduction, or numeric user scale.
**Likely probes:** What changed your mind? What did you personally do? How did you know it helped?
**Detail in reserve:** Familiar language was the important change; a simpler visual layer alone was insufficient.
**Reflection prompt:** What would you measure now to distinguish completion from real independence? Frame proposed instrumentation as what you would do, not a historical action.

## B · Dimensions — a specific customer-feedback loop

**Opener:** “One useful change was letting users create a missing dimension without leaving the dataset they were configuring.”

- **Context:** Leave dataset → create dimension elsewhere → return and resume; customers reported friction, errors, confusion.
- **My responsibility:** Identified the workflow problem and proposed the change.
- **Actions / why:** Put basic creation/editing into the current task → Product and Engineering agreed → kept advanced management separate to limit first-version scope.
- **Result:** Shipped; customers reported faster configuration, fewer errors, and less confusion.

**Evidence boundary:** Qualitative customer reports; no baseline, sample size, or measured reduction. This supports responding to feedback, not clarifying vague feedback.
**Likely probes:** Why not move everything? What feedback followed? How did you identify the problem?
**Detail in reserve:** Dimensions subsequently supported aggregation/modeling; ownership of later advanced work is not established.

## C · Maker Days — influence and capacity tradeoff

**Opener:** “At Abacum, we addressed Engineering’s capacity concern with a bounded production test for the design system.”

- **Context:** Engineering worried the system would compete with squad work and never reach production.
- **My responsibility:** Co-led business case with Head of Design; contributed token/library work. Engineering built original pipeline.
- **Actions / why:** Showed inconsistencies → compared staffing approaches → team chose one focused Maker Days week, more concentrated participation for less time.
- **Result:** Tokens and first Button reached production; proved the design-to-code path worked.

**Evidence boundary:** Shared influence and decision. No measured ROI or delivery-speed claim. Do not invent a PM conflict or sole engineering implementation.
**Likely probes:** What objection did they raise? Why a week? What did you give up?
**Detail in reserve:** Squad delivery capacity was the cost. This was a small proof before broader adoption, not completion of the migration.

## D · Manager view — disagree, deliver, assess honestly

**Opener:** “At Remuner, I disagreed with a full redesign, but worked to keep the research findings in the direction leadership chose.”

- **Context:** Managers lacked an overview by metric, navigated too many nested steps, and could not easily see previous-period information.
- **My responsibility:** Research/design recommendation; proposed fixing foundational workflow and architecture first.
- **Actions / why:** Stated disagreement → CEO/CTO chose full redesign → accepted decision and retained the main findings in metric overview and navigation changes → captured feedback and separated blocking problems from other friction.
- **Result:** Shipped; positive feedback on overview/navigation, mixed response overall, including difficulty finding information.

**Evidence boundary:** Qualitative personal account. Do not say later iterations solved the problems; no later release/result confirmed. Leadership disagreement was not a PM disagreement.
**Likely probes:** What was your alternative? How did you act after the decision? What did negative feedback change?
**Detail in reserve:** Analysis informed future iteration priorities; it does not establish that those iterations shipped.

## E · Token file — a mistake you owned

**Opener:** “I deleted a token file I thought was duplicated, and the next deployment caused a short production outage.”

- **Context:** Frontend still depended on the file; my assumption was wrong.
- **My responsibility:** Own deletion and mistaken dependency assumption.
- **Actions / why:** Restored file and pushed fix → manually checked required files for several days → team added required-file presence check pending dependency cleanup.
- **Result:** Service restored; safeguard introduced.

**Evidence boundary:** No exact outage duration or customer count. Automation and completed dependency cleanup are not confirmed. Do not merge separate pipeline hardening into this incident.
**Likely probes:** Why did you delete it? What would you do differently? What changed afterward?
**Reflection prompt:** Explain how you would verify consumers/dependencies before removing a supposedly duplicate file. This is a lesson to articulate, not evidence you performed a particular technical audit then.

## F · AI agent — scope and trust under uncertainty

**Opener:** “At Remuner, I designed a conversational agent for questions about commissions and sales plans.”

- **Context:** Reps and managers needed understandable answers about pay; different roles had different access.
- **My responsibility:** UX/UI, conversation design, answer formats, role-based context and design-side boundaries.
- **Actions / why:** Engineering established available data → agreed scope with founders/Engineering → designed supported questions/refusals and contextual answers, tables/lists where useful → iterated tone, terminology, presentation after launch.
- **Result:** Released to all customers before March 2026; mixed feedback and continued iteration, without reliable adoption/accuracy/business metrics.

**Evidence boundary:** No PM on this project. Engineering owned architecture. Wrong numbers could arise when customer-specific calculation code was outside agent context; recorded resolution is unclear. Do not claim guaranteed correctness or that chat exposed data freshness.
**Likely probes:** What was out of scope? How did you assess accuracy? What did you personally own?
**Detail in reserve:** No complaint/follow-up was a weak operational signal, not ground truth.

## G · IC dashboard — turn vague feedback into specific problems

Updated from Manel’s direct account, 2026-10-09. [Readable answer](textream/07-vague-feedback-ic-dashboard.txt).

**Opener:** “At Remuner, users said the rep dashboard wasn’t intuitive, but interviews showed they meant different things.”

- **Context:** “Not intuitive” did not identify whether the problem was UI, missing information, or understanding compensation.
- **My responsibility:** Identified feedback-givers, arranged interviews, and designed all the changes as sole designer.
- **Actions / why:** Found calculation-understanding, metric-relationship and quarterly-payment timing problems → team compared with existing evidence → prioritised severity and useful changes → added calculation summary/full-detail access and period/payment information → tested with users.
- **Result:** Changes shipped. In testing, users understood the information they had previously been missing; qualitative evidence, without quantified impact.

**Evidence boundary:** Qualitative direct account, no measured effect. Personal research and full design ownership confirmed; prioritisation and implementation were shared. No specific metric-relationship solution recorded. Do not merge with manager-view redesign or assume the same iteration as the earlier progressive-disclosure example.
**Likely probes:** What did you ask? How did you prioritise? What did testing show? Did it ship?
**Memory chain:** Vague complaint → different causes → targeted changes → user testing.

## Rehearsal

Practise the selector, not six memorised speeches. Ask prompts in random order; choose the card within a few seconds and answer without reading it. Start with impact, vague feedback, disagreement, failure, then AI.

After each answer, check: Did I answer the actual question? Can a listener repeat the problem, my contribution, decision and result? Did I explain why? Did I overclaim? Retry only the weak part.

Useful probe rotation: “What did you personally do?” / “What evidence supported that?” / “What was the alternative?” / “What happened next?”

Cards are prepared. Spoken rehearsal and listener comprehension have not yet been verified.
