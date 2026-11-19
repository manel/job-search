# Interview fix plan: 2026-11-19 to 2026-12-02

Source: [feedback-weaknesses.md](feedback-weaknesses.md).

## Goal

By 2026-12-02, you can do these four things in an interview without help:

1. State what your work changed, with your strongest signal.
2. Lead a live case from the data point to a metric.
3. Answer an unprepared question with a principle and an example.
4. Show a visual craft piece.

## Time and pipeline rules

- Plan for about 2 hours each working day. Change this number if it is not realistic.
- Keep follow-ups and interview tasks on schedule.
- Limit new applications to 3 per week. Interview conversion is the bottleneck, and you already have many open applications.
- Spend under one hour on a role with an unmet stated must-have.
- If an interview gets a date, that interview comes first. Run `/prep-interview`, then practise its stories, facts and likely follow-ups.

## Three findings that change the prep

- **The live-case playbook contradicts the Alan lesson.** [live-challenge.md](../../interviews/playbooks/live-challenge.md) says "The brief gives you a domain. You define the product." After Alan, the rule is that the task and data define the problem.
- **Drill practice stopped.** The [results log](../../interviews/drills/framing-drills.md#results-log) has one scored drill, from 2026-10-16, at 8/12. Drill 2 is unfinished, and drills 3 to 5 are untouched.
- **Most stories have a result, but little measured impact.** The fix cannot be a stronger claim. Each story must state what changed, how you know, and what you would measure now.

## Workstreams

### A. Impact

Cover `abax`, `dataset-manager`, `remuner-ds`, `ai-agent` and `ic-dashboard` in [stories.md](../../interviews/stories.md). Add these four lines to each story:

| Line | Content |
|---|---|
| Changed for | The user, customer or team, and what became different |
| How we know | The measure or signal, with its evidence class |
| If asked | The limit, said in one sentence, only when someone asks |
| Measure now | What you would track if you ran it today |

- Claude asks one recall question at a time. Your honest memory or best estimate is enough, and you need no proof.
- Say "about" or "roughly" for an estimate. Numbers that did not happen stay out.
- New facts go to the register first, then to the story.
- The `abax` session also covers the adoption items in [TODO.md](../../TODO.md#what-to-improve-after-the-perk-feedback-2026-11-18).

### B. Live cases

Use this order, and put each step on the board:

1. **Task:** what they asked for.
2. **Signal:** the number or break point in the brief.
3. **Problem:** a statement that quotes the signal.
4. **Risks:** two or three user challenges that could break the flow.
5. **Direction:** one sentence on what the product should become.
6. **One flow:** the part that attacks the signal.
7. **Metric:** baseline, target and one guardrail.
8. **Beyond the MVP:** what comes next, and why.

If the brief has no data, as in a zero-to-one challenge, start with step 5. State your time plan at the start, and check it at each step.

### C. Unprepared follow-ups

Answer in this shape, in under 60 seconds:

1. The principle.
2. How you would apply it here.
3. One real example, or "I have not done this at that scale".
4. The limit or tradeoff.

"I don't know" is acceptable only when you add how you would find out. Claude builds a bank of about 40 questions from your real interviews. Topics: scale, standards, enforcement, documentation, metrics, AI and visual craft. Claude does not show you the questions before the session.

### D. Fact accuracy

Claude builds a one-page fact card from the register for the five stories. It holds numbers, dates, who did what, and phrases to avoid. Claude checks every rehearsal transcript against it.

### E. Visual craft piece

Version 1 is the table selection work, plus the screens where you did the most visual fine-tuning. Details and limits are in [TODO.md](../../TODO.md#what-to-improve-after-the-perk-feedback-2026-11-18).

- **Remuner before and after: dropped 2026-11-19.** Manel's call: the before looked very poor, so the after was easy and proves little.
- **Your task:** go through the Abacum and Remuner files and list the screens with the most fine-tuning work. Two or three files open at a time.
- Write the visual decisions for each piece: hierarchy, spacing, type and colour.
- The new component exercise comes after version 1 is live.

### F. Honest debriefs

After each real interview or mock, record these before giving a general impression:

- Where did the interviewer have to steer you?
- Which answers had no principle?
- Which impact claims had no evidence?
- Which facts were wrong?

Do not write "likely to advance" unless the record names a specific positive signal from the employer.

## Calendar

| Date | Your work | Claude's work | Fixed dates |
|---|---|---|---|
| Thu 2026-11-19 | Review the [playbook change](../../interviews/playbooks/live-challenge.md#choose-the-opening-from-the-brief-2026-11-18) and [fact card](../../interviews/reference/fact-card.md) (20 min). Impact session: `abax` (45 min). Finish drill 2 (10 min). | Prep done 2026-11-18, including the [question bank](../../interviews/drills/followup-bank.md). Do not open the bank. | |
| Fri 2026-11-20 | Impact session: `dataset-manager`, `remuner-ds` (45 min). Follow-up set 1 (20 min). Go through the files for fine-tuning work (30 min). | Score drill and answers. | Wizeline check-in. Fever test check. Neotalent nudge. |
| Mon 2026-11-23 | Impact session: `ai-agent`, `ic-dashboard` (45 min). Drill 3 (10 min). Visual decisions, first pair (30 min). | Update stories after your approval. | Hublance nudge. |
| Tue 2026-11-24 | Drill 4 (10 min). Follow-up set 2 (20 min). Finish visual decisions (60 min). | Score. Draft piece structure. | |
| Wed 2026-11-25 | Mock live case 1 (90 min). | Play interviewer, using a brief you have not seen. | Spendesk check. |
| Thu 2026-11-26 | Review mock 1 (20 min). Drill 5 (10 min). Record the table selection (45 min). | Debrief against section F. | |
| Fri 2026-11-27 | Publish version 1 of the visual piece. Say all five impact answers aloud (30 min). | **Checkpoint 1.** | |
| Mon 2026-11-30 | Mock live case 2 (90 min). | Play interviewer. Score. | |
| Tue 2026-12-01 | Case presentation with hard follow-ups, Abacum deck (60 min). | Ask follow-ups. Check facts. | |
| Wed 2026-12-02 | Record a full case presentation (30 min). Final follow-up set (20 min). | Run the cold-listener test. **Checkpoint 2.** Update this plan. | |

## Pass criteria

These thresholds are my proposal. They measure readiness in practice, and they do not predict an offer.

| Area | Pass |
|---|---|
| Impact | All five stories said aloud in under 90 seconds, with all four lines |
| Framing drills | Three drills in a row at 10/12 or more, with lines 2 and 4 at 2/2 |
| Live cases | Mock 2 has signal, problem and risks on the board before solution work, no steering needed on them, and a metric with baseline and target |
| Follow-ups | 16 of 20 unseen questions start with a clear principle |
| Facts | Two rehearsals in a row with no wrong number, date or owner |
| Visual craft | Public or unlisted link live, with every claim confirmed |

If an area fails at Checkpoint 1, it gets the free time in week 2. If live cases still fail on 2026-12-02, continue with two mocks per week.

## Limits

- Claude can check structure, content and facts. Claude cannot reliably judge your delivery, pace or how easy you are to follow.
- A spoken rehearsal needs a transcript. Test on 2026-11-19 whether FluidVoice can record a solo rehearsal that Claude can read.
- Manel decided on 2026-11-18 to continue without a human mock. A fresh Claude session reads only the transcript, then repeats back the problem, your role, the key decision and the result.
- This cold-listener test checks whether the words are clear. It does not test delivery, so the Spendesk presentation risk stays partly open.
