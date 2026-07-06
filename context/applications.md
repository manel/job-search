# Applications

Pipeline state as of 2026-07-02. Update this file whenever a role status changes.

## Status vocabulary

Use these statuses everywhere (this file, /update-pipeline, /new-application):

- **in-progress** — package being written, not yet sent
- **applied** — application sent, no response yet
- **interviewing** — at least one round scheduled or done (track rounds in `interviews/[company].md`)
- **offer** — offer received
- **rejected** — closed by them
- **stale** — no response 5+ weeks after applying, treat as closed
- **deferred** — assessed, fit is real, holding for a stated reason
- **skipped** — assessed, not pursuing

## Follow-up policy

- ~10 business days after applying with no response: send a short status nudge through the channel used to apply.
- ~3 weeks with no response: find the hiring manager or a designer on the team on LinkedIn. Use `context/outreach.md`.
- 5 weeks with no response: mark stale. Stop investing.
- Record every follow-up action in the Next action column with its date.
- Convention: the first date in a Next action cell is its due date. A SessionStart hook (`.claude/hooks/check-overdue.sh`) flags rows whose first date has passed, so lead with the due date and keep other dates out of that cell.

---

## Active

| Role | Company | Status | Applied | Next action | Notes | URL |
|---|---|---|---|---|---|---|
| Senior Product Designer | Spendesk | 🟡 in-progress | — | Due 2026-07-04: set salary position, write package. Use canonical AI agent description (manager claim confirmed safe 2026-07-06, see memory.md); don't gate on the Sasha probe | Fit assessed 2026-06-12: proceed. 2nd-degree paths found 2026-06-12 incl. the Head of Product Design. Barcelona hybrid. No salary in JD; set position before cover letter. Position as product role with DS component: lead with Abacum. De-scoped 2026-07-02: was blocked 3 weeks on the AI agent description | https://career.spendesk.com/jobs/7802636-senior-product-designer |
| Senior Product Designer | Finom | 🟢 applied | 2026-06-02 | Due 2026-07-03: send LinkedIn outreach to a design lead (draft ready). Stale 2026-07-10 if silent | €78K position. 10-day nudge (due 2026-06-16) was never sent; at 4+ weeks the 3-week LinkedIn step applies instead | https://jobs.eu.lever.co/pnlfin/b5a8e88e-ed56-4260-8425-7f7a99ad6fb7 |
| Lead Design Systems | BVNK | 🟢 applied | 2026-06-01 | Due 2026-07-03: send LinkedIn outreach to hiring manager or senior DS designer (draft ready). Stale 2026-07-10 if silent | €90K position. 10-day nudge (due 2026-06-15) was never sent; at 4+ weeks the 3-week LinkedIn step applies instead | https://job-boards.eu.greenhouse.io/bvnk/jobs/4876105101 |

## Closed

| Role | Company | Status | Applied | Closed | Notes |
|---|---|---|---|---|---|
| Senior Product Designer (Integrations) | Typeform | ⚪ stale | 2026-05-26 | 2026-07-02 | Marked stale at 5+ weeks per policy. M. Lynch (Global Hiring) never replied to 2026-06-11 LinkedIn message; the 2026-06-18 follow-up was never sent. Stop investing |
| Senior Product Designer (IT spinoff) | Factorial | 🔴 rejected | 2026-05-26 | 2026-07-02 | 3 rounds incl. live design challenge. Rejection feedback: "stayed close to a manual, minimal solution" — panel wanted vision-first thinking, not validation-first. See `interviews/factorial.md`. |
| Staff Product Designer - Design Systems - 100% Remote - EMEA | Hostaway | 🔴 rejected | 2026-06-04 | 2026-06-29 | Standard form rejection, no feedback. "Closer fit" language only |
| Senior Design System Designer | Bitpanda | 🔴 rejected | 2026-06-01 | 2026-06-08 | Standard form rejection, no feedback |
| Senior Product Designer (Advanced Trading) | Bitpanda | 🔴 rejected | 2026-05-21 | 2026-06-01 | Standard form rejection, no feedback. No salary stated at application |

---

## Deferred

| Role | Company | Reason | Revisit | URL |
|---|---|---|---|---|
| Product Designer | Linear | Strong fit. Needs a few weeks of active product use before applying | When Linear becomes primary tool | |
| Sr Product Designer, Spectrum Design System | Adobe | Domain (creative tools) and genuine interest are marginal. DS scope and location pass. Role posted 2026-06-10. | If domain concern resolves or a warm path appears | https://careers.adobe.com/us/en/job/ADOBUSR169335EXTERNALENUS/Sr-Product-Designer-Spectrum-Design-System |

---

## Assessed and skipped

| Role | Company | Reason | URL |
|---|---|---|---|
| Various | Deel | Figma MCP / Plugin API gaps — domain mismatch | |
| Various | GitLab | Location and domain | |
| Staff Product Designer | Remote.com | Staff level but domain mismatch | |
| Various | Fundraise Up | Language requirement | |
| Product Designer | Perk Flights | Low genuine interest confirmed | |
| Staff Product Designer (Network Features) | Tailscale | US-remote only | |
| Senior Product Designer, Core UX & Mobile | PandaDoc | Domain mismatch (document management), mobile component is a gap, genuine interest fail | https://www.pandadoc.com/careers/senior-product-designer-core-ux-mobile-eu/ |
| Product Designer | Hostinger | Consumer product (website builder), unleveled scope (mid-level), compensation ~€54K well below floor | https://jobs.ashbyhq.com/hostinger/ea9d04c9-c20c-4c20-9a94-19df2e600006 |
| Design System Champion | Merkle (Dentsu) | Pre-sales/sales engineering role disguised as DS work — outputs are demos and RFPs, not shipped product | https://dentsuaegis.wd3.myworkdayjobs.com/DAN_GLOBAL/job/Barcelona/Design-System-Champion_R1118430 |
| Design System Designer | Fluidra | Pool hardware company — digital team is a support function, domain and genuine interest both fail | https://jobs.fluidra.com/job/Sant-Cugat-del-Valles-Design-System-Designer-B/910-es_ES |
| Senior Product Designer (Inbox) | Proton | Consumer email product, visual craft emphasis (icons, illustrations) — wrong work type for the positioning | https://job-boards.eu.greenhouse.io/proton/jobs/4606437101 |
| UX/UI Designer & Researcher | knowmad mood | IT consulting agency — generalist UX production for client accounts, mid-senior leveling, domain and genuine interest fail | https://knowmadmood.teamtailor.com/jobs/7915753-ux-ui-designer-researcher-figma-entorno-internacional |

---

## Warm paths

- Factorial (closed 2026-07-02): Liliana, former Remuner coworker, now at Factorial. Activated 2026-06-11, but the recruiter had already contacted Manel off the application before the referral did anything. The interview process came from the cold application, not the warm path. Liliana remains a contact for any future Factorial role.
- Perk Flights: former Abacum contact potentially available as warm intro. Genuine interest unresolved — do not pursue until that's answered.
- Linear: no warm path identified yet. Worth researching before applying.
- Spendesk: 2nd-degree paths found 2026-06-12. Only real bridge: Sasha Lamachenka (ex-Abacum colleague), but her Spendesk mutuals are non-design (Swann M., support engineer; Cristina Maria, PM). Probe sent/pending: ask Sasha if she knows them or anyone else at Spendesk well. Other bridges (Jakob Fiedler, Jorge Casals → Cyrièle Piancastelli, Head of Product Design; Eugeni Vila d'Abadal, Jens Bringsjord → Lorenzo Selvaggi, Senior PD Barcelona; Sébastien Hézard → Rachel Belkadi, Senior PD AI) are weak relationships, not usable for intros. Fallback after applying: connection request with note to Lorenzo Selvaggi. Don't gate the application on the probe. No parallel outreach.

---

## Notes on specific ATSs

- Factorial uses `careers.factorialhr.com` (proprietary). Automated scanning unreliable. Check manually.
- BVNK uses Greenhouse.
- Hostaway application included custom form answers in addition to CV and cover letter.
