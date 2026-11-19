# Follow-up question bank

**Manel: do not open this file before a session.** Claude picks the questions and logs the results. Seeing them first removes the point of the practice.

Built 2026-11-18. Source shows where the question came from. "New" means Claude wrote it for the same weakness.

## Scoring

Each answer gets 0 to 2 on each line:

| Line | 2 points |
|---|---|
| Principle | A clear rule in the first sentence |
| Application | Applies the rule to this situation |
| Evidence | One real example, or says honestly that none exists at that scale |
| Tradeoff | Names a limit or a cost |
| Facts | Nothing conflicts with the [fact card](../reference/fact-card.md) or the [register](../../evidence/experience-facts.md) |

A question passes at 7 of 10 or more, with Principle at 2 and Facts at 2. Mark any answer over 60 seconds. Never accept the Perk claims listed as unconfirmed on the fact card.

## Scale

| # | Question | Source | Strong answer includes |
|---|---|---|---|
| 1 | How would you adapt this for a team of 40 designers? | Perk | 1:1 coaching does not scale. Data picks where to step in, one contact per area, docs as the main layer. Abacum was about six designers |
| 2 | We have 30 designers. What is the largest group you have supported? | Perk | The honest number, then what would change at 30 |
| 3 | You have no dedicated engineer this year. How do you make progress? | Perk context | Squad-owned work, bounded tests, Maker Days and the later core team |
| 4 | A squad builds a good local pattern. How does it enter the system? | Perk context | Clear contribution criteria: reuse, quality, owner, and who decides |
| 5 | You inherit a system nobody trusts. What do you do in the first month? | New | Audit and listen first, then one visible fix. Remuner audit as support |
| 6 | Five teams need different things this quarter. How do you prioritise? | New | Usage and impact as criteria. Abax order by use in screens and code |

## Standards and tradeoffs

| # | Question | Source | Strong answer includes |
|---|---|---|---|
| 7 | Three squads use 16, 12 and 8 px padding on a card. Which is the standard? | Perk | Spacing scale, most-used value from an audit, content density. Design decides and documents why |
| 8 | Two teams forked the data table. How do you unify them? | Wizeline | Compare use cases, keep one API, plan migration through squad work |
| 9 | A team needs custom UI by Friday, and the system cannot do it. What now? | Wizeline | Allow a tracked exception, then decide later if the system absorbs it |
| 10 | Visual quality, WCAG and front-end APIs conflict. Which wins? | Wizeline | Accessibility first. Remuner: AA over visual consistency |
| 11 | When do you deprecate a component? | Perk context | Usage data, replacement ready, transition period. `abax-deprecation` |
| 12 | How do you decide which components to build first? | Perk | Use in screens and code. Abax and Remuner build orders |

## Enforcement and adoption

| # | Question | Source | Strong answer includes |
|---|---|---|---|
| 13 | "Coaching over enforcement" is the diplomatic answer. How do you actually enforce? | Perk | A ladder: measure, find why, fix, then guardrails. `prefer-abax` lint rule, ratchet rule, blocking last |
| 14 | Designers keep detaching one component. What do you do? | Perk | Ask why before acting. Select and Autocomplete example |
| 15 | A new lint rule makes engineers fix old code, and they complain. What do you do? | New | Enforce only new violations. Remuner ratchet, "the team built" |
| 16 | A senior designer refuses to use the system. How do you respond? | New | Find the reason first. Says honestly that Abacum had no real resistance |
| 17 | Adoption has stopped at about half. What is your next move? | New | Segment by squad and component, remove blockers, tie the goal to reworks |

## Documentation

| # | Question | Source | Strong answer includes |
|---|---|---|---|
| 18 | How would you organise documentation across platforms into one source? | Perk | One source next to components, published to Figma, Storybook and AI tools |
| 19 | How do you write docs so AI tools use them correctly? | Perk | Explicit rules, names, examples, do and do not. Test the output |
| 20 | How do you know people read the documentation? | New | Page views plus behaviour: misuse and support questions |
| 21 | Who should own documentation, design or engineering? | New | Single owner per layer, with shared review |

## Metrics and impact

| # | Question | Source | Strong answer includes |
|---|---|---|---|
| 22 | How would we know this worked? | Alan | Baseline, target, guardrail tied to the original problem |
| 23 | 47% adoption. What did that change for users? | Perk | Says the 47% is a system measure. Uses only recorded signals and says what was not measured |
| 24 | You have no metric for this project. Why should I believe it worked? | New | The signal, why it counts, why no number exists, what to track now |
| 25 | How would you justify a design system to a CFO? | New | Cost of duplicated work and defects. Proposes measures and invents no ROI |
| 26 | How would you measure whether a recommendation was good for the user? | Alan | Measures the outcome after the action. Adds a guardrail |
| 27 | Your metric improves, but support complaints rise. What do you do? | New | Guardrail logic, investigate segments, do not celebrate the metric |

## Product judgment

| # | Question | Source | Strong answer includes |
|---|---|---|---|
| 28 | If you were the CEO, what would you do with this product? | Factorial | An opinionated direction with a ranked reason |
| 29 | How would you build this with full resources? | Factorial | A ranked argument, not "everything" |
| 30 | What reports could this system produce? | Factorial | Starts from the decisions users need to make |
| 31 | We think automation belongs in the MVP. Why leave it out? | Factorial | The specific assumption and risk, or changes position with a reason |
| 32 | Your solution is safe. What is the ambitious version? | Factorial | A clear future proposition, then the first step toward it |
| 33 | Leadership chose a direction you disagree with. What do you do? | New | State the disagreement, commit, protect key findings. `manager-view` |

## AI

| # | Question | Source | Strong answer includes |
|---|---|---|---|
| 34 | How do you use AI day to day? | Enginy, Factorial | The three uses in [answers.md](../answers.md), with where it fails |
| 35 | With today's AI, what would you do differently on that project? | Perk | Specific change, and engineers still review |
| 36 | How do you make AI prototypes meet the system's quality bar? | Perk | Readable specs, tokens, automatic checks for drift |
| 37 | How would AI help run a system across a much larger team? | Perk | Separates current practice from proposal. Labels personal work |
| 38 | AI output looks right but breaks the system. How do you catch it? | New | Checks against tokens and components, human review |

## Visual craft

| # | Question | Source | Strong answer includes |
|---|---|---|---|
| 39 | Show me a component you elevated visually. | Perk | A real example with hierarchy, spacing, type and colour decisions |
| 40 | Our B2B product should feel consumer-grade. What does that mean to you? | Perk | Specific qualities, and compares against strong references |
| 41 | What makes a data table feel high quality? | New | Density, alignment, states, clear selection. Table selection is prototyped, not shown as shipped |
| 42 | When does motion add value in a product? | New | Motion that explains change. Claims no unconfirmed motion work |

## Working style and role

| # | Question | Source | Strong answer includes |
|---|---|---|---|
| 43 | A bug reaches you directly. What do you do? | Enginy | Triage by severity, file it clearly, route it. A real Remuner example if one exists |
| 44 | What is your mobile experience? | Mapon, Perk | No native depth, Remuner webview on both stores, Kymco checkout |
| 45 | What would you bring in your first three months? | Wizeline | Concrete deliverables backed by past work |

## Results log

| Date | Question | Score | Over 60 s? | Note |
| --- | --- | --- | --- | --- |
