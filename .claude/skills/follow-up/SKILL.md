---
name: follow-up
description: "Surface overdue next actions from the applications pipeline and draft the appropriate follow-up message for a specific role."
---

# Follow-up

Checks the applications pipeline for overdue next actions and drafts the follow-up message.

## What this skill does

1. Read `context/applications.md`. Get today's date from the system context.
2. Scan every row in the Active table. Identify which roles have a Next action date that has passed or is due today.
3. Surface them in order of how overdue they are, most overdue first.
4. If more than one is overdue, ask which role to act on before drafting anything.
5. Determine the message type from the follow-up policy below.
6. Draft the message following the rules in `context/outreach.md`.
7. Show the draft for confirmation. Do not update anything until confirmed.
8. After confirmation, update the Next action field in `context/applications.md` with the new date and what the next step is.

## Follow-up policy

- ~10 business days after applying with no response: short nudge through the channel used to apply.
- ~3 weeks with no response: LinkedIn message to the hiring manager or a senior designer on the team. Method in `context/outreach.md` under "Hiring manager outreach".
- 5 weeks with no response: mark stale. Stop investing. Propose moving the role to the Closed table.

Count business days, not calendar days.

## Message rules

All messages follow `principles.md`. Load and check against those rules before drafting. Invoke the `no-ai-slop` skill before drafting and the `humanizer` skill on the draft before output. Mandatory, not opt-in.

**Nudge (10-day):** One or two sentences. Applied, still interested, checking in. No apology for following up. No attachments; the portfolio link is in the original application.

**LinkedIn outreach (3-week):** Follow the template in `context/outreach.md` exactly:
- Applied for [role] on [date], still interested
- One concrete line connecting the strongest relevant signal to their product. DS roles: two production design systems and the token pipeline. Product roles: the Abacum data-layer work. One line, not a pitch.
- Ask: "happy to share more if useful"
- No apology for reaching out. No more than five sentences total. No attachments; link the portfolio at manel-leiva.com.

**Stale (5 weeks):** No message. Propose updating the status to stale and moving the row to Closed.

## Checking for the contact (LinkedIn outreach only)

Before drafting the LinkedIn message, check `context/applications.md` Notes column and `context/outreach.md` Active warm paths for any known contact at the company. If a contact is already identified, address the message to them. If not, note that the hiring manager or a senior designer on the team needs to be identified on LinkedIn before the message can be sent.

## After confirmation

Update `context/applications.md`:
- Replace the current Next action with what was just done and the date.
- Add the next scheduled action and its date.
- If marking stale: move the row from Active to Closed, set status to stale.
