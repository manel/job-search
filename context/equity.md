# Equity

How to read an option or ESOP grant, and Manel's existing grant. Moved from the pre-merge `context/salary.md` (commit `83bef9f`) on 2026-10-14.

Use this to read any grant — Factorial ESOP, Abacum NSOs, future offers. Only the numbers change.

**The core objects:**
- **Option** — the right to *buy* a share at a fixed price. Not a share yet. You own nothing until you exercise.
- **Strike / exercise price** — the fixed price you pay per share to exercise. Set at grant, never changes.
- **FMV / 409A price** — the current internal per-share value of a private company, set by the board. This is the "worth," not a market price. No open market exists for private shares.
- **Vesting** — the schedule by which options become yours. Typical: 4 years, 1-year cliff (nothing until month 12, then monthly/quarterly). Leaving stops vesting; unvested options are forfeited.
- **Exercise** — actually paying strike × quantity to convert vested options into shares.
- **Liquidity event** — acquisition, IPO, or tender/secondary sale. The only way private shares become cash.

**In the money vs underwater:** if FMV > strike, exercising has value (the spread). If FMV < strike, the options are worthless to exercise.

**The value formulas:**
- Cost to exercise = strike × number of vested options
- Paper value = FMV × vested options
- Spread (gain) = (FMV − strike) × vested options
- Real cash = spread realized only at a liquidity event, minus tax

**Two things people miss:**
1. FMV is not withdrawable cash. Private shares can't be sold until a liquidity event. Exercising early means cash tied up in an illiquid, high-risk asset for years.
2. Exercising creates a tax event with no sale. For NSOs (and most ESOPs), the spread at exercise is taxed as ordinary income that year even though no cash changed hands. Later gains above FMV are capital gains at sale. Cross-border (US grant, Spain resident) is fiddly — get a Spanish tax advisor before exercising.

**Post-termination exercise (PTE) window:** when you leave, you usually have a limited time to exercise vested options — commonly 90 days, after which they vanish. Some companies extend it (Abacum extended Manel's to the full 10-year term, expiring Feb 2032). Always confirm the PTE deadline in the grant.

**ISO vs NSO/ESOP:** ISOs have better US tax treatment but strict rules; NSOs are simpler and taxed as ordinary income on the spread. ESOP is the umbrella term for the plan; the instrument underneath is usually options.

**Low-risk default play:** for illiquid private grants, waiting until an announced liquidity event and doing exercise-and-sell in one motion avoids years of dead money and premature tax. Check whether the company allows cashless exercise / same-day sale.

**Worked example — Abacum (former grant, ES-87, logged 2026-07-01):** 445 vested NSOs, strike $2.88, FMV $7.24. Cost to exercise $1,281.60; paper value $3,221.80; spread ~$1,940. Terminated April 2024 but exercisable until Feb 2032. In the money, but locked until a liquidity event.

**Open questions before valuing any new ESOP offer** (from the Factorial process): options vs RSUs, strike price, current company valuation and last-round terms, exercise window on leaving, dilution and total share count.
