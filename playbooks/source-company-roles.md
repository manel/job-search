# Source roles from a company watchlist

## Purpose

Find live Product Design vacancies from a defined company universe without
mixing unverified leads into the application pipeline.

## Search order

1. Review companies marked `watch` before `review`; skip `paused` companies
   unless the note's reconsideration condition has changed.
2. Check the official career page or ATS board for Product Design vacancies.
3. Check the company's LinkedIn Spain jobs URL for omissions, duplicates, and
   public hiring posts.
4. Treat search snippets and LinkedIn-only vacancies as leads until the exact
   posting is verified.

## Include

- Product Designer, Senior Product Designer, Staff Product Designer, Principal
  Product Designer, or Lead Product Designer with individual-contributor scope.
- UX Designer titles only when the work is product-led rather than a production
  or marketing service.
- Design Systems Designer or a closely related product-infrastructure role.
- Remote roles explicitly open to Spain and hybrid roles based in Barcelona.

## Exclude early

- Explicit people-management accountability or direct reports.
- Roles requiring relocation or attendance outside Barcelona.
- Brand, marketing, graphic, motion, or UI-production roles.
- Consumer-mobile craft roles requiring recent native iOS or Android experience
  unless the evidence register changes.

## Record a lead

Add one row to `sourcing/role-leads.csv` with both URLs when available. Use the
official job ID or URL to distinguish similarly titled vacancies. Record
`posting_status: open` only when the exact official posting was checked.

After initial location and relevance checks pass, follow `playbooks/assess-role.md`
and create the canonical application record before drafting materials.

## Cadence

- `watch`: weekly.
- `review`: assess and classify in batches, then move to `watch` or `paused`.
- `paused`: monthly or when the reconsideration condition changes.

Update the check dates even when no suitable role is found. A company jobs page
being visible does not prove that a specific vacancy is still open.
