# Chat documentation audit

Audited 2026-10-13. Scope: recover decisions, evidence and useful draft copy from available project conversations into Career OS.

## Complete local list verified

Follow-up on 2026-10-13: reconciled the full local app thread index, queried read-only, against the source manifest. Included both registered career projects, their roots (including read-only `job-search`), the legacy project directory and Career OS worktrees. The complete matching index contains **79 threads: 54 substantive conversations, 23 internal approval reviews, one empty thread and this audit**. All 54 substantive thread IDs are now covered. The [complete local list](complete-local-chat-list.json) records each thread and its disposition.

The initial exact-workspace filter missed one substantive conversation in `/Users/manel/.codex/worktrees/6fde/career-os`: **Interview storytelling practice**, thread `01a0ce90-e645-7702-8aaa-d213686d968b`. Read its full available transcript and saved it in the [rehearsal archive](../../interviews/archive/dataset-manager-rehearsal-2026-09-23.md). It contains two submitted English practice answers, assistant feedback and three historical story cards. Their underlying project evidence is already represented in current records. The archive flags superseded token-file recovery wording and the existing SQL chronology conflict.

**Result:** no substantive conversation in the complete local career-project index remains unmatched. This verifies local app-list coverage, not every sentence's migration or preservation of chat attachments. After sign-in, verified the complete visible original ChatGPT project list: **27 chats**, with pagination exhausted and URLs deduplicated. The [original project inventory](complete-chatgpt-project-list.md) records every title and link. Full content and attachment preservation for these 27 originals has not been established; local Codex coverage does not prove original-chat coverage. No chats were deleted.

## Coverage

Read local Codex session logs with either `/Users/manel/Dev/career-os` or the older Career Strategy ChatGPT project directory as their recorded workspace. Found 82 files: 56 substantive source files representing 53 unique conversations, after excluding 26 internal approval-review, empty/non-substantive or current-audit files. Three conversations had more than one source file; they were grouped by thread ID.

The [source manifest](chat-audit-manifest.json) records thread IDs, local source paths, hashes, topic cues and existing document references. Document-reference extraction aids navigation; it is not proof that every statement in a chat has been migrated. The semantic findings below identify the material gaps recovered in this pass.

The initial local audit did not cover the original server-side list. The follow-up now records all 27 visible original project chats separately. Older chats referenced within conversations but without recoverable local bodies were not reviewed in full. Some newer work, including PromoFarma, is present in the repository but its original local transcript was not found within this source inventory. Existing saved records were retained. Do not delete the old ChatGPT project on the strength of this audit.

## Recovered material

| Missing material | Durable destination | Evidence boundary |
|---|---|---|
| Preply CRM/lifecycle Skip, 2026-09-22 | [Application record](../../applications/records/preply-global-senior-crm-lifecycle-designer.md) and dashboard | Historical assistant assessment; no employer rejection or submission inferred. Current opening unknown; later income-first priority acknowledged. |
| Factorial reapplication advice, 2026-09-22 | [IT-spinoff record](../../applications/records/factorial-senior-staff-product-designer-it-spinoff.md#reapplication-advice-recovered-from-chat) | January/February 2027 were proposed timing, not company policy or Manel's confirmed decision. |
| Personal LLM use, 2026-09-10 | [Experience register](../../evidence/experience-facts.md#personal-ai-use) | Homelab/network and light coaching/tracking directly confirmed; assistant elaborations excluded from the fact claim. |
| Abax all-hands presentation, target sequencing, denominator and qualitative feedback, 2026-09-17 | [Experience register](../../evidence/experience-facts.md#abax-design-system) | Separate intended buy-in, adoption target, reconstructed counts and perceived improvements. No new quantitative result. |
| Dataset Manager chronology/attribution conflict | [Experience register](../../evidence/experience-facts.md#dataset-manager) | Published interim-SQL account conflicts with older “SQL dropped” wording; estimate attribution also differs. Flagged, not resolved by assumption. |
| Final Jaume outreach with the requested code-experience addition | [Enginy draft](../../outreach/enginy-jaume-puig-2026-09-15.md) | Sending unconfirmed. |
| Aideen feedback request after rejection | [Datavant draft](../../outreach/datavant-aideen-feedback-request-2026-10-04.md) | Sending and any response unconfirmed. |
| User-edited Spendesk survey answers and revised closing | [Survey draft](../../outreach/spendesk-candidate-survey-2026-09-29.md) | Submission unconfirmed; no numeric survey ratings recovered. |
| Original Haddock booking acknowledgement | [Historical draft](../../outreach/haddock-ingrid-booking-2026-09-29.md) | Superseded 2 October appointment; do not send now. |
| eDreams professional/personal AI-use form answer | [Historical draft](../../application-answers/edreams-ai-use-2026-09-10.md) | Actual submitted wording unknown; assistant elaborations labelled. |
| Warm-copy and senior design-system framing preferences | [Writing rules](../../context/writing-rules.md) | Preserve approved copy; foreground scope and stewardship; avoid unsupported Kings of Mambo chronology. |

Each recovered draft is linked from the relevant application record. Preply's record was written before adding its dashboard entry. Existing application outcomes and contact dates were not inferred from draft recovery.

## Already documented

The checked conversations already had durable records for the other role assessments and duplicate routes, WhiteTech/CloudTalk submissions, Alan and Kabilio progression, Haddock's hold, AirHelp/Tabby/Datavant/Spendesk outcomes, and legacy application reconciliation. Later dated record updates take precedence over earlier chat snapshots.

Broader Remuner ownership, Abacum's Integrations-to-Engine scope, mentoring/teaching, design practices, dashboard research, token-file incident, Dimensions integration and modeling-language evidence were already captured in the evidence register and interview materials. Figma coverage is saved in the product inventory and contribution audit. Dataset Manager deck edits have a dated alignment report. LinkedIn sourcing, the company watchlist, external application feedback and the portfolio rework plan also exist.

Saved interview scripts and readers establish prepared materials. The recovered worktree conversation additionally establishes two submitted English practice answers with assistant feedback; independent spoken delivery, timing and improved presentation performance remain unverified. Old vacancy research and market-pay suggestions remain dated historical evidence; this audit did not recheck them online.

## Remaining gaps

- The complete visible server-side project list is verified (27 chats). Full original-chat content and attachment preservation remains unverified. All 54 substantive local career-project threads are matched; these are separate inventories.
- Dataset Manager's exact SQL release sequence and original time-saving source need corroboration. The published account and direct recollection are both retained.
- Sends/submissions for the recovered drafts are unknown. Datavant's planned hiring-manager interview completion remains unconfirmed. Alan technical booking/tool clarification and Kabilio's employer update require new evidence, not inference from elapsed dates.
- Abax has no recoverable raw measurement series, exact script-counting unit, adoption-target deadline or measured customer/time-saving result. Commerce A/B-test specifics and conversion results remain unverified in the existing register.
- Numerous existing files are modified or untracked in Git. Files saved on disk are not necessarily committed or backed up. This audit preserved the existing working tree and did not bulk-commit unrelated work.

## Verification

Checked recovered copy against original message bodies, including reconstruction of Spendesk's three user-edited writing-block fragments. Checked source dates for Abax confirmations and grouped duplicate thread files. Verified the new report/record/draft links and ran `git diff --check` after edits.
