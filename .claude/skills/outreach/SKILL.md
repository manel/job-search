---
name: outreach
description: "Draft a warm path referral ask or LinkedIn silent-application message for a specific company and contact, following the rules in context/outreach.md."
---

# Outreach

Drafts a warm path referral ask or LinkedIn follow-up message for a specific company and contact.

## Arguments

`/outreach [company] [type]`

Types:
- `referral` — asking a known contact to refer you or point you to the hiring manager
- `linkedin` — the 3-week silent-application message to a hiring manager or senior designer found on LinkedIn

If type is omitted, read `context/applications.md` to find the role's status and current Next action and infer which type applies.

## What this skill does

1. Read `context/applications.md` for the role's status, applied date, next action, and any known contacts.
2. Read `context/outreach.md` for the applicable message rules.
3. Read `context/positioning.md` for the signal to lead with (DS roles vs. product roles have different leads).
4. Confirm the fit assessment exists in `context/applications.md` before writing anything. If the role hasn't been assessed, stop and run `/assess-fit` first.
5. Ask for any information needed before drafting: who the contact is, how they know Manel, what their role is at the company.
6. Draft the message.
7. Show the draft for confirmation. Do not update anything until confirmed.
8. After confirmation, update `context/applications.md`: add the outreach action to the Notes column with the date, and set the next follow-up date in the Next action column.

## Referral ask

Use when a known contact can refer or introduce.

Three things in the message, nothing else:
- The specific role (title and link from `context/applications.md`)
- One sentence on why the fit is real, taken from the fit assessment notes in `context/applications.md`. Do not invent or paraphrase; pull the language from what was already written.
- The ask: "would you be comfortable referring me, or pointing me at the hiring manager?"

Include the CV and portfolio link (manel-leiva.com) in the same message. Do not make the contact ask for them.

Do not warm up with "do you like working there" before the ask. Either ask that separately or skip it.

If they do not reply in a week: one follow-up message, then stop. Do not contact other people at the same company in parallel.

## LinkedIn message (3-week silent-application)

Use when an application has had no response for approximately 3 weeks and a hiring manager or senior designer on the team has been identified on LinkedIn.

Structure:
- Applied for [role] on [date], still interested
- One concrete line connecting the strongest relevant signal to their product:
  - DS roles: two production design systems and the token pipeline
  - Product roles: the Abacum data-layer work (Dataset Manager or Modeling Syntax depending on what the role emphasizes)
- Ask: "happy to share more if useful"

Constraints:
- Five sentences maximum
- No apology for reaching out
- No attachments; link the portfolio at manel-leiva.com
- One message; if no reply, do not follow up on LinkedIn again

## What not to do

- No outreach for roles that failed the fit assessment. Check before drafting.
- No message that could be pasted to a different company unchanged. Every message is specific to one person at one company.
- No connection requests to strangers without a note.
- Never ask a contact to refer for a role they would be embarrassed to attach their name to. If the fit is marginal, note it and ask whether to proceed.

## Writing rules

Load and apply `principles.md` before drafting.

- No em dashes
- No banned vocabulary (insights, leverage, streamline, enable, journey, and the full list in principles.md)
- Active voice
- No performative enthusiasm
- Read like a calm, direct message from a peer, not a pitch

Referral asks can be up to three short paragraphs if the relationship is close. LinkedIn messages: five sentences hard cap.
