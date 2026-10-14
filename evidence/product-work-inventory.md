# Product-work inventory — Abacum and Remuner

Verified 2026-10-06 through read-only Figma Desktop Bridge inspection and Manel's direct scope confirmations. Purpose: preserve role breadth and identify representative projects for future CVs and interviews.

## Consolidation follow-up

The [contribution audit](contribution-audit.md) groups the observed work into candidate workstreams and includes design-team contributions and Remuner's design-practice foundations. On 2026-10-06, Manel asked to continue this audit, prioritize portfolio evidence and pause OLX CV reworking. Follow-up now starts with team/foundation examples; the earlier project-achievement questions remain deferred until reviewing the consolidated register.

## Evidence boundaries

- **Confirmed user account:** Abacum work covered Integrations followed by Engine. Remuner involved platform-wide product-design responsibility as sole designer.
- **Initial Abacum review:** Five connected files were enumerated; four are Abacum implementation files and one is Remuner. All page names were read; relevant page/frame structures and selected annotations were examined in the four Abacum files. Six representative screens were visually inspected across the five files. This is a scope inventory, not a complete screen-by-screen audit.
- **Interpretation:** Abacum's work can be grouped around connecting data, preparing and structuring it, and building and understanding financial models. This grouping describes the remit; it does not establish that Manel owned every step of one continuous end-to-end journey.
- **Unknown:** Individual leadership, research, release status, and outcomes for newly identified projects. Checkmarks and page names are file conventions, not independently verified shipment evidence. Screen sample data is not business-impact evidence.
- Some broad recursive annotation reads timed out. Bounded reads recovered selected annotations; exhaustive annotation coverage is not claimed.

## Abacum scope

| Area | Work visible in the artifacts | Basis |
|---|---|---|
| Data connections and updates | Dataset creation, HRIS auto-sync, automatic/manual updates, update history, activity and data loading | Dataset Manager page index; integrations remit confirmed by Manel |
| Data preparation and management | Transformations, previews, transformation-step ordering, manual adjustments, validation and unsaved-change behavior | Dataset Manager pages and annotations; manual-adjustment screen |
| Dimensions and mappings | Dimension/item creation and editing, rename/error flows, mapping templates, mapping status, automatic mapping, column dependencies | Dimensions sections and resource-page screen; Dataset Manager pages and dependency annotations |
| Financial model building | Module management, logic panels, variable relationships, dimension ordering, actual/forecast formula views, concurrency and save behavior | Engine page index and inspected logic/relationship screens |
| Formula-language interfaces | Formula help, autocomplete, aliases, dimension blocks, syntax colors, aggregation context, time ranges and variable highlighting | Syntax page index, selected annotations and formula-relationship screen |
| Design-system infrastructure | Token architecture, component library, governance and engineering pipeline across five squads | Existing experience register; not re-audited in these five files |

These are product areas and recurring workflows. Dataset Manager and modeling syntax remain selected project evidence within this broader remit.

## Remuner scope

**Confirmed user account:** Manel owned product design across the Remuner platform as sole designer. His named remit includes integrations, datasets, rep plans, approval workflows, roles and permissions. The files below corroborate the broader platform scope; individual leadership and outcomes for newly inventoried projects remain to be confirmed later.

### Review coverage — 2026-10-06

- Enumerated all 13 connected files beginning with “Remuner |”. Read their page indexes and selected handoff structures, with 18 representative screens/components visually inspected and selected annotation snippets recovered from every file that contained them in the sampled pages.
- Two files are named Datasets, with different file keys but identical page ID/name indexes at inspection. Their canonical version and lineage are unknown; count the data-management area once. The 399 indexed page entries include both copies, separators, covers, templates, exploration and handoff pages. This is not a count of projects or shipped features.
- The earlier Datasets file was initially connected as “Abacum | Datasets”. Manel confirmed it is Remuner work, corroborated by Remuner branding and its subsequent file name.
- Handoff/exploration labels describe file organization, not verified delivery status. Dates in names are not reliable career chronology: the Roles page is labelled 0124 and one Comp. plans page is labelled 1026, outside the recorded tenure. Do not resolve those discrepancies by inventing dates or ownership.
- The Core review covered foundations and selected typography documentation. It was not a complete component-library, token-pipeline, or accessibility audit.

### User-confirmed organization

On 2026-10-06, Manel explained that he established a role/scope-based organization of design files: Admin, IC/Manager, Core for app-wide projects, and Libraries. Each file separated exploration from implementation, with dated projects and iteration identifiers within both sections. The inspected Handoff sections are the implementation side of this structure. Month/year prefixes are visible in the snapshot; their exact format and occasional inconsistent dates are retained rather than treated as verified chronology. This records Manel’s organizational contribution. He subsequently confirmed use by engineers, the wider team, the Head of Product, and a designer who joined later, as well as himself. Resulting improvements and the later designer’s join date/overlap remain unconfirmed.

### Product areas and relationships

| Area | Artifact evidence | Scope implication |
|---|---|---|
| Data integrations and configuration | Data-source choice, file uploads, dataset fields, nested conditions, processing/error states, archiving, mappings linked to metrics and parameters | Work on the data inputs and configuration used by compensation plans |
| Compensation-plan design | Plan creation, metric configuration, targets, weighted metrics, multipliers, tiers, matrix payouts, payout limits, frequencies, currencies, bulk parameters and true-up/regularisation | Complex rule configuration as well as the user-facing plan experience |
| Rep plans and earnings | My plans, payout breakdowns, metrics and targets, payout frequencies, expired-plan visibility, plan details and responsive cards | Helping reps understand their plans and compensation logic |
| Rep dashboards | Earnings, payments, target progress, metric widgets, tier information and performance/coaching concepts | Reporting and performance information beyond the AI chat surface; visible AI-labelled concepts are not proof of additional shipped AI capabilities |
| Manager/admin dashboards | Widget configuration, dashboard layout, calculated metrics, team comparisons, pending-payment views, export, sharing and permissions | Team reporting and configurable administrative experiences |
| Period closing and approvals | Frozen versus closed periods; approvals from reps, managers and admins; reminders; bulk actions; approver validation | Workflow states and responsibilities across several user roles |
| Access and administration | Users/teams, system/custom roles, resource permissions, plan sharing, restriction communication, settings and SSO configuration | Access rules affect navigation, resource visibility and available actions |
| HR documents | Sales-letter templates, plan-description generation, document previews, sending letters, signing-state warnings and rep/admin document access | Compensation-document workflows; the file title does not establish legal or regulatory compliance |
| Navigation and responsive behavior | Personal/team/admin navigation, expansion/collapse, settings access, mobile navigation and documented breakpoints | Information architecture across roles and screen sizes; this does not establish native mobile design |
| Design-system foundations | Colors, typography, elevation, shadows, spacing, application contexts and token names | Shared foundations serving the wider platform; production pipeline ownership remains governed by the existing register |

### Observed design logic

These are artifact observations, not newly verified personal achievements:

- **Roles and permissions:** annotations define no access, view, edit and full access, along with navigation visibility, read-only dialogs and disabled actions. New custom roles start at the lowest permission level; system roles can be duplicated but not edited/deleted.
- **Closing and approvals:** annotations distinguish frozen periods awaiting approvals, partial approval across a team, and closed periods. They describe role-specific rep, manager and admin flows.
- **Data-source selection:** notes identify the need to choose either a connected CRM source or an Excel upload and to warn when changing a source already active in a plan.
- **Mappings:** notes describe restrictions on deleting mappings in use and connect mapping edit rights to dataset permissions, while distinguishing users with access only to plans or parameters.
- **Conditional fields:** notes identify an earlier limitation around nested conditions and specify a rules table with an Else fallback. Improvement intent is visible; shipment and resulting user benefit are not independently established.
- **Plan setup and payouts:** annotations describe removing an unused role-type question, improving contextual selector descriptions, and exposing cross-plan true-up configuration with corresponding indicators in the plan designer and user views.
- **Dashboards:** notes specify default view-only sharing and raise the breadth of data exposed when sharing. Visible earnings/progress amounts are screen examples, not outcome metrics.

### Remuner sources

| File | Source |
|---|---|
| Datasets | [Figma](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL) |
| Settings | [Figma](https://www.figma.com/design/6ud2wi9O3p82AotF9VHUBn) |
| Roles & permissions | [Figma](https://www.figma.com/design/yuXoXF2i7ugCFHbAJhnoWN) |
| Period Locking & Closing | [Figma](https://www.figma.com/design/Cwzy1PaZXXZmPFblpwvEHU) |
| Navigation | [Figma](https://www.figma.com/design/mndiSWlmvCFcZXugl7qzOG) |
| My plans (IC) | [Figma](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF) |
| Mappings | [Figma](https://www.figma.com/design/ckwN0tSlbE2zrimqSGlvbN) |
| HR Compliance | [Figma](https://www.figma.com/design/TMFqslrpYHy3Fz7E6B7028) |
| Datasets | [Figma](https://www.figma.com/design/VMALBdcCPmY2jhEl4C3tQM) |
| Dashboard (manager / admin) | [Figma](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI) |
| Dashboard (IC) | [Figma](https://www.figma.com/design/ZKUJadWn8AGs81L0V7nUCG) |
| Comp. plans | [Figma](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX) |
| ⚛️ Core | [Figma](https://www.figma.com/design/SmHO5c8ExGDaO6r2hDvbHy) |

The [structured Remuner snapshot](figma-remuner-product-scope-2026-10-06.json) preserves all file keys, page indexes, sampled structures, annotation snippets and the 18 inspected node IDs. The snapshot includes internal artifact text; it is evidence for drafting, not recruiter-facing copy.

### Positioning interpretation

The remit spans the configuration and operation of a sales-compensation platform: data setup, plan and payout rules, role-specific reporting, approvals, access and administration. AI-agent and design-system work are important selected examples within that scope.

**Working CV scope:** Owned product design across Remuner’s sales-compensation platform as its sole designer. Scope spanned data integrations and configuration, compensation plans and payouts, rep and manager experiences, approval workflows, and administration.

**Deferred by Manel on 2026-10-06:** Follow-up on specific project leadership, shipment and outcomes at both employers. Preserve candidate examples and revisit later; no additional achievement claims are approved by this artifact review.


## Sources and inspected examples

| File | Source | Visually inspected nodes |
|---|---|---|
| Abacum — Dimensions | [Figma](https://www.figma.com/design/6c5Iwbr9X5FdhaDj0GD81O) | [Resource page](https://www.figma.com/design/6c5Iwbr9X5FdhaDj0GD81O?node-id=1937-8555) |
| Abacum — Dataset Manager | [Figma](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR) | [Manual adjustments](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR?node-id=6960-18995) |
| Abacum — Syntax | [Figma](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l) | [Formula relationships](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l?node-id=1179-70369) |
| Abacum — Engine | [Figma](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN) | [Relationship panel](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN?node-id=2212-186968), [logic panel](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN?node-id=2085-138213) |
| Remuner — Datasets | [Figma](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL) | [Data sources and errors](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL?node-id=3443-29881) |

The [structured snapshot](figma-product-scope-2026-10-06.json) retains all five file keys, page IDs/names, selected annotation text, and inspected node IDs. Nodes are historical source references; re-resolve them before future MCP use.

## CV use

1. Preserve a role-scope paragraph at both employers.
2. Select achievements by relevance rather than repeating one case in several bullets.
3. Keep the broader inventory here; do not turn the CV into a complete feature list.
4. Abacum's next candidate achievement should come from model logic/relationships or dimension management, once Manel confirms his contribution and a supported outcome. Existing Dataset Manager, syntax and Abax claims remain the established proof.
5. Remuner’s broader configuration, payout, dashboard, approval and access work supplies candidate examples. Individual contributions and outcomes remain deferred alongside the Abacum follow-up.


## Additional Remuner Core archives — 2026-10-06

Read-only inspection of all nine supplied ZIPs recovered their native Figma page/section hierarchy. Sources are under `/Volumes/Documents/Jobs/Remuner/Files (Figma)/Core/`. The [archive snapshot](figma-remuner-archive-scope-2026-10-06.json) records exact paths, hashes, page IDs and comparisons. This was not a full visual or annotation review. All export timestamps are 2026-03-06; these are export dates, not project or release dates.

| Archive | Recovered scope | Treatment |
|---|---|---|
| Emails | Notification-system exploration and handoff; invitations/password reset, assigned/closed plans, closed periods, shared dashboards, letters to sign, target updates, source/plan errors, manager/IC digests and mobile emails | New communications workstream. Newsletter/AI-labelled pages do not establish marketing ownership or shipped AI features |
| Feedback system | Micro-Survey Engine, survey types, persistent feedback widget, custom triggers and IA feedback | New feedback-collection candidate; release, research use and personal decisions unresolved |
| Issues | Manager/IC issues, bidirectional manager claims, labels, bulk actions, CSV/report downloads, autocomplete, issue creation from items and metric/payout contexts, desktop/mobile | New issue/claim-management workstream. Labels span 2024–2026; chronology and release need confirmation |
| Login | SSO login, password recovery and invitations, exploration and handoff | Extends existing access/administration work; not a separate security-specialist claim |
| Currency symbol placement | August/September 2025-labelled currency-position pages | New financial-display consistency candidate |
| Posición del símbolo de la moneda | Single Page 1; different canvas/file hashes and structure from English archive | Retain as related source by title; content relationship unresolved. Do not count as another independent project |
| Navigation | Exact 15-entry page-index match with connected Navigation | Existing workstream; canvas equality not established |
| Roles & permissions | Exact 11-entry page-index match with connected Roles & permissions | Existing workstream; canvas equality not established |
| Settings | Exact 13-entry page-index match with connected Settings | Existing workstream; canvas equality not established |

These extend the broader platform picture to communications, feedback collection, issue handling and financial presentation. They are evidence of saved design work, not proof of individual leadership, shipment or impact.
