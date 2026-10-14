# Initial company-led sourcing scan

Checked: 2026-09-23

This is a discovery scan, not a completed fit assessment. Official career pages
or ATS feeds are canonical. LinkedIn is a secondary discovery and recency signal.

## Leads ready for assessment

### New Relic — Principal Product Designer

- Official: <https://job-boards.greenhouse.io/newrelic/jobs/5396630008>
- LinkedIn company jobs: <https://www.linkedin.com/jobs/search/?f_C=426253&location=Spain>
- Location: Barcelona.
- Initial read: strong lead. AI-native UX Platform, complex technical products,
  design systems, senior IC influence, and no stated people-management ownership.
- Open question: verify whether the Principal calibration matches the evidence and
  whether the flexible-workforce wording applies to this exact Barcelona role.

### Rover.com — Senior Product Designer

- Official: <https://jobs.lever.co/rover/bf6aa5e2-d5ad-4e10-8257-1990ca2533c2>
- LinkedIn company jobs: <https://www.linkedin.com/jobs/search/?f_C=2686335&location=Spain>
- Location: Barcelona; hybrid with Mondays and Thursdays in the office.
- Initial read: plausible lead. Level and location pass, but a consumer marketplace
  across web, iOS, and Android is weaker than the preferred B2B/data-heavy lane.

## Conflicting or blocked leads

### N26 — Product Designer, Grow & Engage

The official careers index returns one Product Designer result in Berlin and
Barcelona, but the exact detail page returns 404. LinkedIn also carries recent
design listings. Record as `posting_status: unknown`; do not assess or apply
until the exact official page works again.

### Pennylane — Product Designer, Germany

The current official Ashby posting is open to Spain-remote candidates, but it
requires fluent German for user research. Career OS contains no German-language
evidence, so this is not an actionable lead without new evidence.

## No new actionable role found

- Datadog: official Product Design page showed no current opening; the exact
  LinkedIn Product Designer II, Security URL redirected to expired jobs.
- Grafana Labs: no Product Design role in the official 138-job Greenhouse feed;
  LinkedIn still exposed a Staff Product Designer listing absent from that feed.
- Qonto: official Lever board showed no Product Design opening; recent LinkedIn
  AI Lab and Staff Accounting listings were not present on the official board.
- Perk: official board currently lists Staff Product Designer, Events, but the
  same role already has a rejected Career OS record. It is not a fresh lead.

## Source limitation discovered

The upstream CSV snapshot downloaded on 2026-09-23 contained 1,710 salary rows
for 164 unique company names. Only one company had a populated `careers_url`.
Career-page discovery therefore needs a maintained enrichment layer; it cannot
be reliably regenerated from upstream fields alone.
