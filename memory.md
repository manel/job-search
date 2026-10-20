# Memory

Observations, patterns, and rules captured during the job search. Updated via /remember.

Read this file at the start of every session alongside CLAUDE.md. Claimable facts about Manel's work belong in `evidence/experience-facts.md`, not here; this file holds lessons learned in use.

Cleaned 2026-10-14 during the career-os merge: entries now covered by the evidence register, `context/positioning.md` or `context/writing-rules.md` were removed; the full earlier version is at commit `83bef9f`.

---

## Recruiter and process signals

**2026-10-16** — Kabilio rejected after the first interview: another candidate was already in final stages, remaining interviews were paused, and Manel's profile never reached the hiring manager. Same shape as Valeria HR (filled by a candidate "already far along") and close to Tabby (filled). Applied 2026-10-01, screened 2026-10-05, roughly when the leading candidate was closing. For small Barcelona companies, a late entry loses to timing, not to the package. Rule: when a recruiter screen goes well, ask where the process stands and how many candidates are ahead, and treat "slower than expected due to candidate volume" (Kabilio, 2026-10-08) as an early warning that someone else is ahead.

**2026-06-08** — Bitpanda Design Systems role rejected. Bitpanda Advanced Trading role is a separate application, do not conflate the two.

**2026-06-08** — Factorial uses a proprietary ATS at careers.factorialhr.com. Automated job scanning is unreliable. Always check manually.

**2026-06-08** — Hostaway application required custom form answers in addition to CV and cover letter. If applying to similar Staff-level DS roles, expect additional written questions beyond the standard package.

**2026-06-08** — BVNK uses Greenhouse. Standard application flow.

---

## Writing rules (discovered in use)

**2026-07-15** — Setup-then-reveal sentences are banned in case copy. The pattern: a clever framing sentence that delays the point, then a colon or rhetorical question that reveals it ("The first design decision had no screens in it: what is this agent allowed to talk about?"). Also its cousins: "delivering the number turned out to be the easy half of the job", "the failures were not the ones I had braced for". Manel flagged the pattern in the AI agent case draft. Fix: state the decision or fact directly, one concrete sentence, no windup. Related to the 2026-06-08 aphoristic-contrast ban; both are punchline energy.

**2026-07-09** — No jargon in Manel's voice documents that he wouldn't say unprompted in an interview. "GA" (General Availability) was in the Qonto CV and cover letter and he had to ask what it meant; a recruiter probing that term would have exposed it as ghostwritten. Test for every term of art: would Manel use this word on a call. If not, plain language ("released to all customers").

**2026-06-08** — Em dashes are the single most flagged AI writing pattern in outputs. Check for them explicitly before every output, not as part of a general review. They survive casual passes.

**2026-06-08** — "I am excited to", "I am passionate about", and "I would love the opportunity" are instant rejection signals in cover letters. They appear more often than expected in first drafts. Treat them as hard stops.

**2026-06-08** — Avoid "harder projects" language and any framing that implies difficulty as a credential. The work speaks for itself. Stating that something was hard reads as insecurity.

**2026-06-08** — Avoid "built without a dedicated team" phrasing. It draws attention to resource constraints rather than outcomes and sounds like an excuse dressed as an achievement.

**2026-06-08** — Do not overclaim technical ownership of the token pipeline. Manel adapted the Abacum pipeline at Remuner using AI assistance. An engineer built the original at Abacum. The correct framing is ownership of the brief, decisions, and outcome — not the implementation.

**2026-06-08** — Outcomes sections must use named qualitative signals, not vague positive claims. "The project was well received" is not a signal. "The CTO said unprompted: from a 2010 app to a 2020 app" is a signal. Name the person, name the moment.

**2026-06-08** — Own the absence of hard metrics directly. Do not hedge with "we believe" or "we think the project improved...". Say there are no hard metrics, then anchor to the strongest qualitative signal available.

**2026-06-08** — "We" without immediate clarification of personal role is a red flag in case studies. Every "we" should be followed by what specifically you did within that collective action.

---

## References and departure context

**2026-06-12** — Departure from Remuner (March 2026) was company-initiated. Never propose Remuner-based references or LinkedIn recommendation asks. The CTO quote stays in case studies (it happened and is documented), but it cannot be converted into a public or checkable reference. "Why did you leave Remuner" is a guaranteed interview question and needs a prepared answer before any screen — see interviews/prep.md.

---

## Interview question patterns

**2026-06-29** — "What would you do if you were the CEO?" surfaced at Factorial Round 2 (Design Director). This is a vision and ambition probe, not a process question. It tests whether a candidate thinks at the product/business level or stays inside the design frame. Prepare a clear, opinionated answer about product direction — not about design craft.

**2026-06-29** — "How would you build [project] if you had full resources?" (Factorial Round 2) is a prioritization and scope probe. The expected answer is not "everything" — it's a ranked argument about what matters most and why. Shows product judgment under hypothetical freedom.

**2026-06-29** — AI usage has now come up in both Round 1 (Lucia) and Round 2 (Marta) at Factorial. It is a standing evaluation thread at this company, not an informal question. Have a layered answer: what changed in your workflow, where AI helps, where it doesn't. Don't just list tools.

**2026-06-29** — Factorial is using the Round 3 live challenge as a leveling instrument (Senior vs. Staff). In challenge-format interviews that serve this function, the process narration in the debrief hour carries as much weight as the output. Staff-level signals in a live challenge: clarify scope before starting, name tradeoffs as you go, frame decisions in product outcome terms, show system-level thinking before touching UI. Shipping a polished screen without narrating the reasoning reads as Senior, not Staff.

**2026-07-01** — "What reports can you derive from this system?" (Factorial Round 3) is a product scope trap. The instinct to generate report types on the spot is wrong — the correct answer is to redirect to user needs: "I'd ask what decisions IT and Finance are trying to make, then design reports backward from that." Generating features from a system description is a PM habit, not a design habit. Caught here; correct it in future challenges.

**2026-07-01** — MVP scope disagreements in live challenges: if the panel challenges your MVP boundary, you need a tighter product argument than "validate first, automate later." That argument is defensible in a strategy conversation but reads as risk-avoidance in a fast-moving company. The stronger framing is: "here's the specific assumption we'd be able to validate with v1 that automation would actually mask, and here's what we'd lose if automation failed before trust was established." Name the tradeoff concretely, not abstractly.

**2026-10-16** — "How would we know it worked?" is a standing probe at Alan. Celine flagged impact as too general in round 1, and Christelle asked it twice in the live case: how to know a member–therapist match was good, and which metrics. In live cases, the measurement question gets asked directly, whether or not the board has a metric on it.

**2026-10-16** — In live cases, the synthesis keeps drifting away from the data point the brief hands over. This happened three times in a row:
- **Juniper mock:** picked triage while the mapped break point was no-shows.
- **Spendly mock:** picked the manager step against the map's own numbers.
- **Alan live, "Find the right therapist":** framed the problem from Alan's vision paragraph ("reactive instead of preventive") instead of the task and data (matching, four therapists, biggest drop-off at "Select a therapist", 2–3 weeks). The only written option (awareness) didn't touch the drop-off. Christelle's questions steered the session back to matching.

Rule: the company vision is background. The task, the constraints and the data point given define the problem. The problem statement must cite that data point, the chosen direction must attack it, and the metric must measure it as baseline → target (here: the drop-off at therapist selection). Before ideating, check: "Does my problem statement mention the number or the break point they gave me?"

**2026-07-01** — Factorial culture signal: strong bias toward moving fast and shipping full feature sets early. They placed automation inside the MVP, not phase 2. If this role is offered and accepted, the push/caution tension is a real working dynamic to plan for, not an artifact of the interview format.

---

## Strategic observations

**2026-06-08** — Warm referrals are higher leverage than cold applications. When assessing a new role, always check whether a warm path exists before defaulting to a cold apply.

**2026-07-02** — Factorial process origin, corrected by Manel: the recruiter reached out off the cold application before Liliana's referral ping had any effect. The only screen in the pipeline so far came from a cold application. Do not cite Factorial as warm-path evidence. Note the pattern instead: the one conversion was a Barcelona-local company positioned as founding-designer breadth; the fast form rejections were global-remote DS-titled roles with the largest applicant pools.

**2026-07-08** — Spendesk closed before the application went out. Assessed as a strong fit 2026-06-12 (Barcelona hybrid, the converting segment), then the package sat blocked ~3 weeks on one unresolved claim (the AI agent description) and the role was delisted 2026-07-08. Rule: a fit-assessed role in the converting segment gets its package out within one week. If a claim is unresolved, ship without it and add it later; a blocked application and no application cost the same.

**2026-06-08** — Fit assessment must run before any writing. Writing a CV or cover letter for a role that hasn't been assessed is wasted work. Skipping assessment to save time always costs more time downstream.

**2026-06-08** — Salary positioning must be set before writing a cover letter. Never start writing with compensation open. It creates a decision point mid-draft that contaminates the tone. *Superseded 2026-10-11 by the income-first priority: ask for the range first and don't put a figure in the letter unless the form requires one. See `context/salary.md`.*

**2026-06-08** — Genuine interest is a real criterion, not a soft one. Roles where genuine interest is marginal or absent should be skipped, not dressed up with strong language. The cover letter will show it regardless. *Partly superseded 2026-10-11: under the income-first priority a weak domain or non-ideal product is not a skip on its own; genuine willingness to do the work still matters. See `context/target-roles.md`.*

**2026-06-08** — Motion as evidence (screen recordings showing a system working in production) is appropriate and strengthens the DS case. Motion as decoration undermines systems-thinking credibility. Do not rebuild the portfolio in Framer.

**2026-06-08** — The AI case study (Remuner AI agent) is worth pursuing but has open questions: what signal exists on the shipped agent, and how much of the design Manel personally owned. Do not invest time writing this case until those questions are answered. *Resolved: ownership and evidence were settled in July and the case went live on 2026-07-23. Facts are in `evidence/experience-facts.md`.*

**2026-07-13** — Qonto AI Lab rejected at screen in 2 business days, template rejection, no human contact. This was the strongest-fit assessment in the pipeline with direct evidence for the JD's rarest requirement (shipped AI agent with guardrails/error states). Extends the 2026-07-02 pattern: fast form rejections are a property of the segment (global-remote roles at high-profile companies, largest applicant pools), not of application quality — the best package in the queue died exactly as fast as the weakest. Consequences: (1) don't over-invest polish time in global-remote applications at name-brand companies; ship them fast and cheap, the screen is a volume lottery; (2) Barcelona-local remains the only segment that has ever converted to a human conversation; weight sourcing and effort accordingly; (3) a "strongest fit" label predicts interview performance, not screen survival — stop treating screen outcomes as feedback on positioning.

**2026-07-13** — CloudPay (Product Designer UI/UX, unleveled title) form-rejected in 1 business day: applied Friday 07-10 with €78K stated on the form, template rejection Monday 07-13. The level probe at application had flagged exactly this risk (scope read Senior, title unleveled, exit if band mid-level). A rejection that fast is a screen-level cut, and the stated Senior-band figure is the likely trigger. This validates the leveling skips (Hostinger, Valeria, Bizneo, SocialHub) rather than arguing for hiding the number: stating the figure cost nothing but a fast no on a role whose band would have failed anyway. Rule: unleveled "Product Designer" titles where scope reads Senior are a proceed only with eyes open — expect the salary question to resolve the level question for you, quickly.

**2026-07-14** — Bitpanda DS repost rejected in 1 business day, template, no feedback — the third Bitpanda template rejection (Advanced Trading, DS, DS repost) with zero human contact across all three. The reapplication test has its answer: candor about the prior rejection plus genuinely new evidence (the live DS case) did not survive the screen, and the speed suggests the June rejection on file drove the cut. Two rules: (1) Bitpanda is off the sourcing rotation; (2) reapplying to the same req after a screen rejection is a low-odds play even with new evidence — the prior rejection is visible to them and new evidence only matters if a human looks. A reapplication is worth it after an interview-stage rejection with feedback addressed, not after a screen cut. Consistent with the 2026-07-13 Qonto entry: global-remote name-brand screens are a volume lottery; this one had worse odds from the start.

**2026-07-10** — AI-assisted design tooling is appearing as a named qualification in target-segment JDs, not a nice-to-have. Four in one week: Vista AI Logomaker lists "Claude Code, Figma Make, or Cursor" as a requirement; AirHelp (Lead PD, mobile) asks for prototyping with "Cursor, Claude — building real flows instead of static mocks"; Perk Events requires "AI as a working default" (Claude, Cursor, Bolt, Figma, Git); INFINNI (Senior PD, remote EU) requires "above-average, in-depth skill in Figma, FigJam, and AI tools like Claude". The shipped Remuner agent plus daily AI-assisted practice is direct evidence most Senior candidates can't show. Surface it early in CVs and cover letters for roles that carry this signal, not as a buried differentiator. Complements the 2026-06-29 entry: AI usage is also a standing interview evaluation thread (Factorial, two rounds).

**2026-10-20** — PDF export rule. Featherweight (the Figma plugin used for CV and letter PDFs) embeds real Inter, except for any text layer containing underlined text: that whole layer is drawn as outlined glyphs (`FigmaGlyphs`, Type3), which extracts split ("wit h", "librar y") for ATS parsers. Hyperlinks carry Figma's default underline, so every link-bearing layer broke: LearnWise, Flodesk, OLX Otodom DS and the OLX PD letter went out affected (13 and 19 Oct). Featherweight flags it under "Needs attention: Underline or strikethrough". Rule: remove underlines from linked text (the hyperlink stays clickable), confirm "Needs attention" is empty, export, then run `python3 scripts/check-pdf-text.py <pdf> --source <source.md>` before sending. Also: the Figma frame can drift from the Markdown source (Perk had a stale 80% claim); the `--source` check catches it.
