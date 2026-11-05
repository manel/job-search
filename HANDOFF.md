# Handoff: Perk Suitcase process (session 2026-11-05)

## Goal

Get Manel through the Perk Senior Design Systems Designer (Suitcase) process. The TA screen passed on 2026-11-05. The next round is the hiring-manager session, on site in Barcelona, next week.

## Current status

- **TA Preliminary with Clare Watts held and passed 2026-11-05.** The debrief is the last section of `interviews/perk/perk.md`. Record and dashboard are updated.
- **Waiting on two emails from Clare:** a process confirmation with prep links, and an availability link for the on-site session. Not received as of the end of this session.
- **Process (per Clare):**
  1. Hiring-manager session on site in Barcelona. Tim dials in from London; a local designer or the director is in the room. Exploratory, portfolio-led. Tim is off Tue 10 and Wed 11 Nov.
  2. Online case study on one of Manel's own cases (problem, challenges, success metrics, adoption), plus scenario questions run as a team exercise.
  3. Leadership wrap-up (CPO or another design leader).
  Two to three weeks in total.
- **Salary:** Manel restated EUR 65,000. Clare said the level is "probably closer to seventy", plus benefits and stock options. No full band. Logged in the record and in `context/salary.md` (Employer band evidence).
- **Not working / unresolved:** on the call Manel made claims the evidence register doesn't cover (see Open questions). They are unconfirmed, and Tim may probe them.
- **Nothing is committed.** The working tree also holds changes from before this session (Enginy record, `outreach/enginy-saul-villa-2026-11-05.md`), plus edits to `TODO.md` and `interviews/prep.md` that this session didn't make (made on disk during the session, presumably by Manel).

## Decisions made (with reasons)

- **Brief split into two files.** `interviews/perk/perk.md` keeps the live Suitcase process, because `/debrief-interview` and `/prep-interview` write to `interviews/[company]/[company].md`. The closed July Events brief moved to `interviews/perk/perk-events.md`. It was never used (rejected at CV review).
- **"Likely questions" rewritten as #### headings** (for a table of contents) with first-person spoken answers. `no-ai-slop` and the humanizer were run. The Remuner departure answer was kept word for word from `interviews/prep.md` (Priority zero).
- **Two corrections against the register while writing:**
  - Dropped "KOM component libraries" from the intro: not in the register.
  - Updated the accessibility answer to the current register: focus and error states not relying on colour alone, screen readers "in some cases".
- **Tanna's 2026-11-05 message** (she understood every referral gets at least a first interview) is logged as inference: the 26 Oct rejection was likely an automatic or first-filter cut. It does not mean the hiring team rated the CV highly.

## Tried and rejected

- **Public Suitcase research:** Perk's own Builders blog posts (rebrand, microfrontends) return HTTP 403 to fetches.
  - The Medium RSS feed for builders.perk.com works and gave the May 2026 and Dec 2025 posts.
  - The rebrand and microfrontends details exist only as search summaries and are marked that way in the brief.
- **Willy Fontenelle's "Suitcase design system" Medium article** is about Hurb (a Brazilian travel company), not Perk. Ignore it.
- **Ashby posting page** renders by JavaScript. Use the Ashby API instead (see How to verify).

## Files touched

- `interviews/perk/perk.md`: Suitcase public-research section, Round 1 brief with spoken answers, and the Round 1 debrief appended at the end.
- `interviews/perk/perk-events.md`: new file holding the July Events brief.
- `applications/records/perk-senior-design-systems-designer.md`:
  - Fields changed: posting_checked_on, last_contact_on, status_verified_on, outcome_stage (design-interview), next_action, next_action_on (2026-11-06), salary_stated.
  - History lines added for 2026-11-05: posting check, Tanna's reply, TA screen.
- `applications/records/perk-staff-product-designer-events.md`: link to `perk-events.md`.
- `applications/active.md`: Perk Suitcase dashboard line.
- `context/salary.md`: Perk entry under Employer band evidence.
- `memory.md`: two 2026-11-05 entries.
  - Recruiter and process signals: the form figure sat below Perk's level.
  - Interview question patterns: design system screens ask how many designers you've supported and whether you coached them.

## Next steps

1. **Check for Clare's emails.** When the availability link arrives, submit slots for Mon 9, Thu 12 or Fri 13 Nov (Tim is off 10 and 11). Log the booking in the record History and update `next_action`.
2. **Ask Manel the open question below** (Kings of Mambo client claims). Record the answer in `evidence/experience-facts.md` with class and boundary, or tell him not to repeat the claim.
3. **Prep the on-site session, but only after Clare's process email arrives.** Manel's decision (2026-11-05): wait for it, because Clare said it will carry instructions and prep links (hints and tips). Ask Manel to paste the email, read any links, then run `/prep-interview perk hiring-manager` and append a Round 2 section to `interviews/perk/perk.md`. Points to cover, adjusted to whatever the email says:
   - Portfolio walk-through led by the Design Systems case (manel-leiva.com/cases/design-systems): Abax first, Remuner second.
   - Questions for Tim: mobile and Compose Multiplatform on the same Suitcase foundations; PM coverage; the current vision; what the dedicated person and project team hand over.
   - If Tim is Tim Archer (content design), the content tokens and SimpleLocalize keys point, and Manel's 2026-10-21 comment on his post.
   - The Remuner departure answer word for word, including the CTO line. On the TA call it came out paraphrased and left the CTO line out.
4. **Start preparing round 2 (case deep dive) early.**
   - Success metrics and adoption: 47% of all tracked component uses at departure, goal 80% of the same count (`evidence/experience-facts.md` lines ~502-512).
   - Never say "80% of new UI". The live case still carries that wording; the fix is drafted in `context/abacum-case-additions-2026-10-30.md` and should go live before round 2. Run `/review-case design-systems`.
5. **Commit the session's work** once Manel confirms. The commit includes files from before the session; check with him what goes in.
6. **Remaining overdue pipeline items** (19, surfaced by the SessionStart hook) were not handled. Run `/follow-up`.

## Open questions

- **Kings of Mambo claims made on the call, not in the register:**
  - design system work for clients;
  - a client with about 15-16 designers;
  - coaching them on adoption.
  Ask Manel: which client, what the coaching involved (sessions, docs, reviews), and roughly when.
- **"Push code to production"** (said on the call): the register supports PRs for styles and tokens, reviewed and merged by the front-end team. Keep that wording going forward.
- **Is the hiring manager Tim Archer** (Senior Content Design Manager, who posted the role)? Inference only.
- **Is the one person dedicated to Suitcase Tanna Schumacher?** Inference only.
- **Mobile:** Clare believes Suitcase covers all platforms, including acquired businesses. Unconfirmed; ask Tim.
- **Dedicated PM:** Clare said probably not and that she would check.

## How to verify

- **Posting still open, and the JD text:** fetch the Perk board from the Ashby API, `curl -s "https://api.ashbyhq.com/posting-api/job-board/Perk"`. Look for job IDs `78dafbf1-0f6d-46b7-b71a-2c59f7af31cf` (London, applied) and `3ec33996-74e4-4466-8b88-d9e9dad6e48f` (Barcelona, same text).
- **Record fields:** `grep -n "^next_action\|^outcome_stage\|^salary_stated" applications/records/perk-senior-design-systems-designer.md`
- **Brief structure (TOC):** `grep -n "^#" interviews/perk/perk.md`
- **No dashes in the brief** (one allowed, inside the quoted Medium title): `grep -c "—\|–" interviews/perk/perk.md`
- **Uncommitted work:** `git status --short`
