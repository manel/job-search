---
company: Perk (formerly TravelPerk)
role: Senior Design Systems Designer
status: in-progress
status_verified_on: 2026-10-19
status_confidence: confirmed
posting_status: open
posting_checked_on: 2026-10-19
fit_decision: proceed
role_lane: design-systems
application_channel: referral
warm_path: Xavi Francisco, former Abacum colleague at Perk (referred Manel for Staff Events in July)
portfolio_version:
applied_on:
last_contact_on:
outcome_stage: not-submitted
rejection_reason_class: none
next_action: Ask Xavi to submit a referral for this req (a referral usually has to come from him in Perk's system, before or right after the application); export the CV PDF and apply via Ashby. Tell Claude when sent
next_action_on: 2026-10-22
salary_stated: Not stated; no range published
job_url: https://jobs.ashbyhq.com/Perk/78dafbf1-0f6d-46b7-b71a-2c59f7af31cf
source: Perk Ashby job board API, fetched 2026-10-19 (published 2026-10-15; London, with Barcelona as a secondary location; hybrid, three days in office)
---

# Perk — Senior Design Systems Designer (Suitcase)

## Decision

**Proceed, high priority.** This is one of the strongest design-system matches in the search. Suitcase is a named system serving 25+ designers and their engineers on web and mobile. The role owns its visual language, token architecture, roadmap, contribution governance, adoption and parity measures, and AI-readable component specs. It is B2B travel and spend SaaS, Barcelona hybrid, and the posting is four days old.

The Staff Events rejection (CV review, July) does not block this. The role shape is different (design systems, not product), and the strongest evidence matches it directly.

## Fit assessment

| Dimension | Result | Note |
|---|---|---|
| Domain | Pass | B2B travel and spend management, fintech-adjacent SaaS. |
| Scope | Pass | Senior IC owning the system's direction and roadmap with design and engineering leadership; coaching, no reports. |
| Work type | Pass | Systems design, governance, measurement, foundations. |
| Location | Pass | Barcelona hub, three days a week in office. |
| Genuine interest | Likely | Design-system ownership is the stated target. |
| Stack signal | Pass | Tokens, Figma-to-code, Storybook, Code Connect, MCP, AI prototyping, HTML/CSS/JS. |
| DS maturity | Pass | Named system, 25+ designers, roadmap with named resources, adoption and parity metrics, experimental and core layers. Real infrastructure. |

## Level read

Senior, with lead-IC system ownership: set direction, own the roadmap, report progress, push back when the system is bypassed. Consistent with Manel's Abacum co-lead and Remuner ownership.

## Proof case

[Design Systems (Abacum + Remuner)](https://www.manel-leiva.com/cases/design-systems), live 2026-10-19. The rarest requirement is measuring and driving adoption while consolidating systems. Abacum shows a tracked component-usage count (Abax at about 47% of tracked Abax and MUI uses against an 80% target, at departure), migration off MUI across five squads, and the contribution model. Remuner adds ESLint adoption enforcement, feature-flagged rollouts and the token pipeline.

## Evidence map

- **Adoption and health measures:** Abacum tracked count and 80% target. State 47% and the target honestly; 80% was not reached.
- **Consolidating systems:** Abax replacing MUI; migration state per `evidence/experience-facts.md`.
- **Token systems and Figma-to-code:** two-tier tokens, Figma Variables to Token Studio to Style Dictionary (Abacum); Vuetify and Sass adaptation and Codex CI checks (Remuner).
- **Contribution governance:** both cases.
- **HTML, CSS, JavaScript:** Kings of Mambo front-end work (theme and commerce).
- **Storybook:** Abacum.

## Gaps

- **WCAG 2.2 AA with keyboard and screen-reader behaviour:** partly covered since 2026-10-19: accessibility audits through the Figma MCP (colour contrast and component checks), mostly at Remuner. Keyboard and screen-reader behaviour and formal conformance work remain unevidenced; do not claim them.
- **MCP tooling:** confirmed 2026-10-19: Figma MCP with an AI agent to manage design tokens in Remuner's Figma files (and since). **Code Connect:** not confirmed; do not claim.
- **Mobile:** the system covers web and mobile; Manel's mobile evidence is the Remuner webview app.
- **Motion and visual-language ownership:** the case is about architecture more than visual direction.
- **Localisation and content tokens:** Remuner's per-customer terminology in the AI agent is adjacent, not the same thing.
- **Salary:** no range published. Follow `context/salary.md`; Perk is a large, well-funded company.

## Materials

- CV source: `cv/roles/perk-senior-design-systems-designer.md` (prepared 2026-10-19)
- Cover letter source: `cover-letters/roles/perk-senior-design-systems-designer.md` (prepared 2026-10-19, 210 words)
- Checked against the evidence register; no-ai-slop and humanizer applied. Code Connect and accessibility not claimed. Not yet exported or sent.

## Prior applications

- Staff Product Designer, Events: referral via Xavi, rejected at CV review (`perk-staff-product-designer-events.md`). One screen rejection, different role shape.
- Staff Product Designer, Flights: skipped twice in July (archive).

## History

- 2026-10-19: Posting fetched (published 2026-10-15, open). Assessed: Proceed, high priority, with a referral via Xavi. No materials prepared.
- 2026-10-19: Manel confirmed Figma MCP use (Remuner tokens, explorations, presentations); CV and cover letter prepared.
