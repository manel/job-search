# Company-led role sourcing

This folder is a discovery layer, not an application tracker.

## Files

- `company-watchlist.csv`: generated, one company per row.
- `company-overrides.csv`: hand-maintained prioritisation and official career-page enrichment.
- `role-leads.csv`: vacancies found but not yet fully assessed.

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

## Source-checking rule

- Official career page or ATS posting: canonical evidence that a vacancy is open.
- LinkedIn: secondary discovery, duplicate check, and public hiring-contact route.
- Search result snippet: lead only; never evidence that the exact role is open.

Reverify the exact official posting immediately before assessment or application.
