# Alan — live technical interview preparation

Started 2026-10-13. Availability submitted; appointment confirmation pending. Sources: [canonical record](../applications/records/alan-product-designer.md), Celine’s email supplied by Manel, and [experience register](../evidence/experience-facts.md). This is a preparation plan, not Alan’s confirmed assessment rubric.

## Confirmed format

90 minutes: the brief arrives by email at the start; work offline for 20 minutes, then join Google Meet for 70 minutes working on the case with interviewers. Brief topic, deliverables, tool constraints, interviewers and date/time are unknown. Alan asks for disclosure of AI use during hiring; exact limits and procedure are unknown.

Do not assume a healthcare scenario, Figma deliverable, coded prototype or polished presentation. Read the actual brief before choosing the output.

## What Celine’s feedback changes

They already recognised simplifying complex products and AI/code practice. The gap is a clear account of how Manel reframes a problem, chooses a direction, and connects it to user/business results. Do not spend most of preparation demonstrating tools again.

Make the chain explicit: **initial request → evidence → reframed problem → alternatives → recommendation and tradeoff → what changed → evidence of impact**.

A user improvement can support a business rationale without proving a business result. Say what was intended, what was observed, and what you could not measure separately.

## Direction-setting stories — evidence audit

| Story | Confirmed contribution and outcome | Detail to recover |
| --- | --- | --- |
| Dataset Manager | Led design/testing; user difficulty with SQL despite familiar Excel logic; team moved toward familiar modeling language and guided configuration; shipped self-service; first-session setup qualitative/recollection | Initial request, recommendations, effort objection and dataset compatibility constraint confirmed; numeric business outcomes remain unverified |
| IC dashboard | Turned vague feedback into calculation/metric/payment-timing problems through interviews; personally designed all changes; shipped; testing showed users understood missing information | One concrete severity/prioritisation choice; what you deferred; any observed business effect, or acknowledge none measured |
| Abax Maker Days | Co-led business case; capacity tradeoff; focused week put tokens and first Button in production | Your recommendation, why small proof was valuable, what decision it unlocked; no measured ROI |

Start with Dataset Manager. Prepare one complete direction-setting episode before collecting more examples. Existing personal accounts and current evidence take precedence over older or inconsistent wording. Do not invent OKR figures, revenue impact or sole roadmap authority.

## Dataset Manager — direction-setting answer

Updated 2026-10-13. Initial request, research proposal, personal recommendation, development objection and compatibility constraint are supported by Manel’s account. Release and qualitative outcome come from the existing register. The statement about the cheaper option missing the goal expresses the rationale; it is not a measured counterfactual.

At Abacum, I was initially asked to improve dataset configuration so customers could move away from editing JSON files. I wasn’t convinced that improving the interface alone would solve the problem, so I recommended research before committing to a direction.

Testing showed that finance users could explain the transformations they needed using Excel functions, but struggled to express them in SQL. I recommended an ordered list of actions on the dataset, such as transformation or aggregation, combined with language closer to what users already knew.

Product and Engineering were concerned about the development effort. SQL was already used for these transformations, so extending Abacum’s modeling language would take more work. They didn’t agree immediately; they needed to review the evidence and make further checks.

I advocated the more familiar approach because the goal was customer autonomy. A solution that was easier for us to build would still miss that goal if customers couldn’t use it. We also had to introduce changes carefully because existing customers already had datasets we needed to protect.

The guided product shipped, and we had qualitative reports of customers reaching a working configuration in their first session. That supports the user outcome. Reducing dependence on implementation specialists was the intended business benefit; I don’t have a measured business result to claim.

**Memory chain:** UX request → propose research → familiar user language → effort objection → protect existing data → self-service result.

**In reserve:** The evidence supports extension of the existing language, not necessarily creating one from scratch. Exact SQL/formula release sequence and migration mechanism are not established here. Do not claim quantified business impact or a zero-loss migration. Keep syntax details for follow-up questions.

## Offline 20 minutes — suggested allocation

This is a flexible practice structure. Follow the actual brief if it requests something different.

| Time | Work | Useful output |
| --- | --- | --- |
| 0–3 min | Read task, requested deliverable and constraints | Brief in your own words; separate facts from assumptions |
| 3–7 min | Identify user, triggering situation, task and problem | One user/task and the consequence of failure |
| 7–11 min | Choose focus and define success | Prioritised problem; why it matters; user/business success signals |
| 11–16 min | Compare a couple of approaches | Recommended direction, rejected alternative and tradeoff |
| 16–20 min | Sketch a focused flow and prepare discussion | Rough flow, important states, open questions |

Avoid polishing before the problem is clear. The useful first artifact is something the interviewers can react to. An outline or rough flow may be more appropriate than screens, depending on the brief.

## Live 70 minutes — practice structure

The interviewers may lead or redirect. Use this as a rehearsal structure, not a schedule to impose.

- **Opening:** Explain what you understand, what you assumed and what you need to clarify. Ask a few high-value questions before committing to a direction.
- **Focus:** Agree the user/problem and success criteria. Make scope choices explicit.
- **Explore:** Compare alternatives and choose a direction. Explain your reasoning, including consequences for users and the business.
- **Develop together:** Sketch or build at the fidelity needed for the requested task. Show the core flow and relevant states/edge cases. Invite critique at decision points.
- **Respond:** Treat new information as a reason to reconsider. Explain what it changes and retain or revise your choice.
- **Close:** Recap problem, recommendation, tradeoff, remaining uncertainty and how you would validate the solution.

## Spoken anchors for a new case

These are optional phrases, not a scripted answer to an unseen brief.

- “The brief asks for X. The user problem I want to clarify first is Y.”
- “I’m assuming X because the brief doesn’t specify it. Is that a reasonable assumption?”
- “I’d prioritise this because … The consequence of leaving it unresolved is …”
- “The alternative is … It gives us … but costs …”
- “For users, success would mean … For the business, I’d look at … I’d also watch …”
- “That new information changes my earlier assumption. I’d adjust …”
- “This is the direction I’d test first, not a claim that we’ve validated it.”

## AI use and logistics

If using AI, disclose actual tools and their role. Example to adapt only if true: “I used [tool] to [specific task]. I reviewed its output and made the design decisions myself.” Do not hide use in the offline portion or imply all tools are approved.

**Tool clarification requested, 2026-10-13:** Manel confirmed sending Celine a reply acknowledging AI disclosure and asking about other tool requirements/restrictions. Employer response remains pending. Availability is submitted; the appointment is not yet confirmed.

**Practice setup:** Figma, with disclosed LLM support as needed. Preparation now focuses on solving an unfamiliar live case; direction-setting stories are supporting material. No mock case has yet been completed.

No need to request the case in advance. The email says it arrives at the start.

## Practice sequence

1. Recover a specific direction-setting episode and write a concise evidence-bounded answer.
2. Practise one question at a time, with follow-up probes on alternatives, ownership and impact.
3. Run an invented practice brief using the 20/70 split. It must be labelled a rehearsal scenario, not a leaked or predicted Alan case.
4. Review whether the problem, recommendation, tradeoff and evidence were clear. Retry the weakest part.

Current state: brief prepared; strategic-story clarification and mock case not yet completed. Technical booking remains unconfirmed.
