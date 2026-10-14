# Company-led role sourcing

This folder is a discovery layer, not an application tracker.

## Files

- `company-watchlist.csv`: generated, one company per row.
- `company-overrides.csv`: hand-maintained prioritisation and official career-page enrichment.
- `role-leads.csv`: vacancies found but not yet fully assessed.
- `remote-companies.csv`: hand-maintained international companies hiring remotely in Europe, outside the Spanish dataset. Added 2026-10-14 from career-ops.
- `scan/`: configuration and dedup history for the automated scanner. `filters.json` holds the title and location filters; `scan/data/scan-history.tsv` remembers every posting already seen. `portals.yml` is generated on each run.

Do not create application records for companies with no vacancy. Create a file in
`applications/records/` only after an exact live role has been found and an
initial location/relevance check has passed.

## Refresh the company universe

Download the current upstream `companies.csv`, then run:

```sh
python3 scripts/build-company-watchlist.py \
  --input /path/to/companies.csv \
  --overrides sourcing/company-overrides.csv \
  --output sourcing/company-watchlist.csv
```

The upstream compensation figures are reports for software engineers in Spain.
They are retained only as a company-level compensation signal. They are not
Product Designer salary evidence.

## Automated scan

`python3 scripts/scan-roles.py` checks the job boards of every watchlist company (`watch` or `review`) and every remote company with a `careers_url`, filters by title and location, and appends postings it has not seen before to `role-leads.csv` with `next_action: Run /assess-fit`. Use `--dry-run` to preview and `--since 7` to limit to recent postings.

It uses the scanner from the separate career-ops checkout (`~/Dev/career-ops`, or set `CAREER_OPS_DIR`) as an engine only. Everything it reads and writes stays in `sourcing/scan/`; career-ops's own CV, profile and tracker are never used.

Coverage depends on `careers_url`. The scanner reads Greenhouse, Ashby, Lever, Teamtailor, Personio, Workable, SmartRecruiters, Recruitee, Welcome to the Jungle and many other job boards. A company whose careers_url is a custom page, or blank, is skipped. To add one, set its job-board URL and `career_platform` in `company-overrides.csv` (watchlist companies) or in `remote-companies.csv`.

`python3 scripts/check-postings.py` checks whether the `job_url` of each open application record is still live. It only reports; update `posting_status` and `posting_checked_on` in the record yourself.

## Source-checking rule

- Official career page or ATS posting: canonical evidence that a vacancy is open.
- LinkedIn: secondary discovery, duplicate check, and public hiring-contact route.
- Search result snippet: lead only; never evidence that the exact role is open.

Reverify the exact official posting immediately before assessment or application.
