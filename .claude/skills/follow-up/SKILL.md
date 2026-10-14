---
name: follow-up
description: "Surface overdue next actions from the applications pipeline and draft the appropriate follow-up message for a specific role."
---

# Follow-up

Checks the applications pipeline for overdue next actions and drafts the follow-up message.

## What this skill does

1. Read the frontmatter of every file in `applications/records/`. Get today's date from the system context.
2. Ignore closed statuses (`rejected`, `skipped`, `stale`, `withdrawn`, `role-closed`, `hired`). Identify records whose `next_action_on` has passed or is due today.
3. Surface them in order of how overdue they are, most overdue first, with the `next_action` text.
4. If more than one is overdue, ask which role to act on before drafting anything.
5. Read that record in full: history, contacts, outreach already sent, and any drafts in `outreach/`.
6. Determine the message type from the follow-up policy below.
7. Draft the message following the rules in `context/outreach.md`.
8. Show the draft for confirmation. Do not update anything until confirmed.
9. After confirmation that it was sent, update the record and `applications/active.md` (see below).

## Follow-up policy

Canonical copy in `applications/README.md`:

- ~10 business days after applying with no response: short nudge through the channel used to apply.
- ~3 weeks with no response: LinkedIn message to the hiring manager or a senior designer on the team. Method in `context/outreach.md` under "Hiring manager outreach".
- 5 weeks with no response: mark stale. Stop investing.

Count business days, not calendar days.

## Message rules

All messages follow `principles.md` and `context/writing-rules.md`. Load and check against those rules before drafting. Invoke the `no-ai-slop` skill before drafting and the `humanizer` skill on the draft before output. Mandatory, not opt-in.

**Nudge (10-day):** One or two sentences. Applied, still interested, checking in. No apology for following up. No attachments; the portfolio link is in the original application.

**LinkedIn outreach (3-week):** Follow the template in `context/outreach.md` exactly:
- Applied for [role] on [date], still interested
- One concrete line connecting the strongest relevant signal to their product, chosen from the role-specific lead in `context/positioning.md`. One line, not a pitch.
- Ask: "happy to share more if useful"
- No apology for reaching out. No more than five sentences total. No attachments; link the portfolio at manel-leiva.com.

**Stale (5 weeks):** No message. Propose setting the status to stale.

Save any drafted message to `outreach/[company]-[contact]-[date].md` and link it from the record.

## Checking for the contact (LinkedIn outreach only)

Before drafting the LinkedIn message, check the record's `warm_path` and contacts, and `context/outreach.md` Active warm paths, for any known contact at the company. If a contact is already identified, address the message to them. If not, note that the hiring manager or a senior designer on the team needs to be identified on LinkedIn before the message can be sent.

## After confirmation

Only once Manel confirms the message was sent:
- Append a dated line to the record's `## History` and update `last_contact_on`.
- Replace `next_action` and `next_action_on` with the next scheduled step.
- If marking stale: set `status: stale` and move the role out of the active sections of `applications/active.md`.
