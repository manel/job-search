# Spoken stories for Textream

Prepared 2026-10-07. Seven draft English answers converted from the [battle cards](../behavioral-battle-cards.md). These are editable spoken drafts, not user-approved verbatim answers. Facts and ownership were checked against the current experience register; historical detail also comes from the detailed Datavant bank. Existing cues remain available.

Open [alan-first-meeting.textream](alan-first-meeting.textream) in Textream for the introduction, collaboration answer, project walkthrough, and seven behavioral stories as separate pages. Native format verified against Textream’s save/load source on 2026-10-07: a JSON array of page strings. JSON round-trip and all twelve page contents checked; opening in the app has not been tested.

## Choose one answer

| Prompt | Paste this file into a separate Textream page |
| --- | --- |
| Impact / research changed direction | [Dataset Manager](01-impact-dataset-manager.txt) |
| Customer feedback / small improvement | [Dimensions](02-feedback-dimensions.txt) |
| Influence / pushback / capacity tradeoff | [Maker Days](03-influence-maker-days.txt) |
| Disagreement / mixed feedback | [Manager view](04-disagreement-manager-view.txt) |
| Mistake / accountability | [Token file](05-mistake-token-file.txt) |
| AI / scope / trust | [AI agent](06-ai-agent.txt) |
| Clarifying vague feedback | [IC dashboard](07-vague-feedback-ic-dashboard.txt) |

Each answer is roughly a minute at an unhurried pace; timing is an estimate, not a rehearsal result. Bracketed lines are delivery cues, not words to say.

## Recommended use

Paste one story per page using Add Page. Turn Auto Next Page off so finishing one answer doesn't start the next. Put the prompt near the camera and select English as the speech language. Try Word Tracking in rehearsal; pause or stop it when listening, and resume only after selecting the answer that fits. Manual scrolling is a fallback if tracking distracts you or you paraphrase substantially.

Rehearse once by reading, then once using only the original four cues. Record a short practice answer and check whether the problem, your contribution, decision and outcome are clear. Change wording that does not sound like you. Full prose is a safety net; adapting to the actual question still matters. You can stop early when interrupted and answer the follow-up directly.

Textream offers separate pages, bracketed cues, Word Tracking, auto-scroll and manual controls according to its [official documentation](https://textream.net/docs/), checked 2026-10-07. Its Hide from Screen Sharing setting is not guaranteed across capture apps; test with the meeting setup if you plan to share a screen. App behavior and tracking with your voice have not been tested here.

## Details to keep in reserve

- Dataset Manager: familiar modeling language; roughly half the time is team recollection, not a measured 50% gain.
- Dimensions: advanced management stayed separate; qualitative customer reports, no measured reduction.
- Maker Days: shared business case; Engineering built original pipeline; no ROI claim.
- Manager view: a leadership disagreement, not a PM conflict. Mixed feedback is not a vague-feedback episode. No later successful iteration is confirmed.
- Token file: exact duration, customer impact, automated check and completed dependency cleanup remain unknown. Do not combine this with separate pipeline hardening.
- AI: wrong numbers could occur when customer-specific calculation code was outside the agent context; the recorded fix is unclear. Data freshness was elsewhere in the app, not chat. Lack of complaints was not proof of correctness.

The vague-feedback story was added on 2026-10-09 from Manel’s account; design ownership, shipment and qualitative comprehension outcome are confirmed; exact test observations and metrics remain unrecorded. Personal Alan motivation is now included in the spoken prep. Mentoring is generally confirmed, but a specific mentoring story still needs a real episode and outcome.

## Full meeting preparation — in progress

[alan-first-meeting.textream](alan-first-meeting.textream) contains the career introduction, the Product/Engineering collaboration answer, a longer Dataset Manager walkthrough, and the seven story pages. [Introduction text](00-career-introduction.txt) includes Kings of Mambo before Abacum and Remuner. This is the single consolidated Textream file; the duplicate battle-card export was removed after verifying every page was included. Other meeting sections will be added as drafted; mentoring was skipped at Manel’s request.

## Local browser reader

Open [alan-reader.html](../alan-reader.html) in a browser. It includes all Textream answers plus the reference sections from [alan-first-interview.md](../alan-first-interview.md). Use search, text-size controls and left/right arrow keys; load a revised Textream file with the button in the sidebar. To refresh both answers and Markdown reference notes on disk, run `python3 scripts/build-alan-reader.py` from the repository. No server, account, or network connection is required.
