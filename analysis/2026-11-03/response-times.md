# Response times, ghosting and conversion (2026-11-03)

Source: frontmatter of every record in `applications/records/` with a submission, plus first-contact dates from each record's History for processes that reached a conversation. Script: `scripts/analyze-response-times.py`. Raw output: `response-times.txt`. Per-application data: `response-times.csv`.

Unit: one submitted application (51 total, 45 with a known `applied_on`). Datavant's July cycle and other applications that predate the records are not included. Small numbers throughout: read percentages as direction, not as rates.

## Headline

| | Count |
|---|---|
| Submitted | 51 |
| Any employer response | 34 (67%) |
| Never heard anything | 17 (33%) |
| Reached a human conversation | 12 (24%) |
| Lost after a conversation | 8 |
| Live conversations | 4 (Wizeline, Perk, Enginy, Haddock on hold) |
| Offers | 0 |

The top of the funnel has improved. Applications sent since September reach a conversation 28% of the time (7/25) against 15% (3/20) for May to August. The pipeline now loses candidates after the first conversation, not only at the CV screen: all 8 conversations that have ended were rejections.

## 1. Good news comes fast; silence past two weeks is a signal

| First response | n | Median | Range |
|---|---|---|---|
| Invite to a conversation | 8 dated | 4.5 days | 0-36 |
| Rejection | 19 dated | 10 days | 0-67 |

- Five of the eight dated invites arrived within 5 days: Kabilio (same day), Datavant (1), Wizeline (1), Biorce (4, screen date), Alan (5).
- Only three came later: Haddock (19), Factorial IT spinoff (27, screen date, so the invite was earlier) and Enginy (36).
- Pre-interview rejections cluster by ATS: Ashby templates at 5 days (3Commas, AIOS, Perk DS), Lever at 10-13 days (Finom, OLX Otodom twice). Workable is slower and wider (12-50).
- Long-tail rejections (25-67 days) are all at the CV screen: Hostaway, CloudTalk, Factorial Platform, RemoFirst (only after a LinkedIn DM), Perk Events.

Inference: an application with no reply after 14 days has a low chance of becoming an interview. The 10-business-day nudge is timed right. Waiting the full five weeks before writing an application off costs nothing, but it should not hold back new applications.

## 2. Ghosting

17 of 51 applications (33%) got no word from the employer at all.

- **Ended in silence (11):** 7 postings closed without a reply (Typeform, BVNK, Finom June, Evinova, Fluidra, eDreams, Moniepoint), and 3 set stale on 2026-11-03 after their postings closed (WhiteTech, Hostinger, Tether). Bunge has been `applied` for 104 days.
- **Still inside the window (6):** Stripe DS (36 days, past the 5-week stale line today), OLX Senior PD (21 days, LinkedIn outreach due), PromoFarma (18), Flodesk (15), LearnWise (15), Nebius (6).
- Posting closure is the clearest ghosting signal on record: 10 of the 11 silent endings had a closed posting by the time they were checked.

## 3. Design-systems-titled roles are the weakest lane

| | Submitted | Conversation | Rejected | Silent |
|---|---|---|---|---|
| DS-titled roles | 11 | 1 (9%) | 5 | 5 |
| Everything else | 40 | 11 (28%) | | 12 |

The one DS conversation (Perk Suitcase) came only after a template rejection was reversed, following a referral. Two Bitpanda DS rejections arrived in 0 and 2 days, which is consistent with an automated or near-automated cut. This matches the `memory.md` entries from 2026-10-26 and 2026-10-29 and supports the DS-lane CV review already in `TODO.md`. Wizeline, the live DS-shaped process, is titled Senior Product Designer.

## 4. Where conversations end

| Stage reached | Lost | Records | Feedback |
|---|---|---|---|
| Recruiter screen | 2 | Biorce, Secfix | Biorce: role was effectively mid-level. Secfix: salary thought high for Spain. |
| First interview | 2 | Kabilio, Valeria | Both: another candidate already in final stages. |
| Hiring manager / design interview | 2 | Datavant, Spendesk | Spendesk: presentation clarity. Datavant: generic. |
| Live challenge | 2 | Factorial IT spinoff, Alan | Factorial: vision and impact. Alan: discovery structure, anticipating key user needs. |

- Three of 12 conversations ended or stalled because the company was further along with someone else: Kabilio, Valeria, and Haddock (on hold since 2026-10-09). Inference: applying in the first days of a posting matters. The scanner's new-postings output is the tool for that.
- The four losses with specific feedback point at interview craft (structure, presentation, vision), not at CV screening. Two of them came from live challenges.

## 5. Channel and ATS (weak evidence)

- Referral or warm path: 2 of 5 reached a conversation (Datavant next day, Perk DS after reversal). Perk Events was rejected at 67 days despite a referral, and PromoFarma has been silent 18 days. Too few to call, but the two best outcomes in the DS lane and the fastest-ever recruiter call both involved a warm contact.
- Recruiter or agency: 2 of 2 answered, 0 of 2 reached a conversation (Babel rejected in 2 days, Pilar declined).
- By ATS, Ashby answers most (6/7) and Greenhouse least (3/8). Lever and Workable answered every time but never with an interview (0/7). This more likely reflects which companies use which ATS than the ATS itself.
- Channel and lane are not recorded for 26-27 applications made before September, so these splits rest on the newer half of the data.

## What to do with this

1. **Nudge at day 10-14, then move on mentally.** Silence after two weeks rarely turns into an interview.
2. **Apply early.** Prioritise postings the scanner flags as new; three conversations were lost to candidates already further along.
3. **Stop sending DS-titled applications cold** until the DS CV review is done. Route DS interest through referrals or through roles titled Product Designer with system scope (the Wizeline shape).
4. **Interview prep matters more than application volume now.** Since September roughly one in four applications reaches a conversation, and every conversation that has ended was a rejection. The fixes on record (structure, vision before validation, concise answers) are where the leverage is.
5. **Record hygiene:** decide on Stripe DS (36 days) and Bunge (104 days, likely stale). Keep logging `application_channel`, `role_lane` and the first-contact date so the next snapshot is stronger.

## Gaps

- Invite dates are missing for Spendesk and Secfix, and applied dates for Secfix, Valeria, Tabby, Murphy, Deel Staff and Pilar.
- Biorce and Factorial IT spinoff use the screen date, not the invite date, so their days-to-invite are upper bounds.
- No offer stage exists yet, so nothing here describes late-stage conversion.
