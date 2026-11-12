# Ways-of-working round

These questions test how you actually function in a team day-to-day. Interviewers are checking for: process maturity, collaboration patterns, communication, how you handle ambiguity and disagreement. Vocabulary refresher: [reference/business-terms.md](../reference/business-terms.md).

## Common themes

**Handling ambiguity**
What do you do when a brief is underspecified? Answer: distinguish between ambiguity in the problem (explore it) and ambiguity in the scope (clarify it before starting). Don't ship a solution to a problem you haven't confirmed.

**Cross-functional collaboration**
Describe your relationship with engineering. Specific answer from experience: the Modeling Syntax work happened in direct collaboration with one engineer, not through a PM intermediary. The Remuner pipeline had engineer sign-off at each implementation step. The relationship is a partnership, not a handoff.

**Prioritization**
How do you decide what to work on? At a startup: survival first. Does the product work well enough to retain users? At a scale-up: what's the highest-leverage design change given the engineering cost? The framing shifts by company stage.

**Documentation and handoff**
How do you make sure your work doesn't die when you leave? Design system documentation was a solved problem at both Abacum and Remuner. Storybook in Chromatic is the artifact. ESLint adoption rules are the enforcement. The system should work without you explaining it every time.

Evidence check: the register confirms Storybook views generated per component at Remuner, a custom ESLint rule at Abacum (`prefer-abax-component`, severity `warn`) and a token-compliance lint rule at Remuner whose tool isn't known. Chromatic isn't in the register; don't name it until Manel confirms it.

**Receiving feedback and iterating**
You get a critique that's partly right and partly wrong. How do you handle it? Separate the diagnosis from the prescription. The interviewer's diagnosis of what's wrong may be accurate even if their proposed fix is wrong. Engage with the diagnosis.
