# Portfolio Context

Portfolio live at: manel-leiva.com
Stack: Next.js, Vercel (Hobby tier), password protection via cookie-session.
Portfolio repo is linked as a git submodule at `../portfolio/` relative to this file.

To update case study copy: edit files in the `portfolio/` submodule, commit there first, then update the submodule pointer in this repo.

---

## Candidate

Manel Leiva — Senior Product Designer
- Kings of Mambo (UX studio, co-founder, 2010–2021)
- Abacum (Senior Product Designer, Jan 2022–Apr 2024, integrations and engine squads)
- Remuner (Senior Product Designer, May 2024–Mar 2026, sole designer and DS lead)
- Postgraduate teaching: UX and digital design. Framed in portfolio as skills developed (explaining complex systems, depth of craft, mentoring). Not a standalone work entry.

Education: Higher National Diploma in Computing Design and Multimedia from ESI (2002). Vocational qualification (Spanish CFGS equivalent). Not a university degree.

---

## Case studies

### 1. Modeling Syntax (Abacum)
URL: /cases/modeling-syntax
Status: Complete and live

Summary: Standardised formula syntax across Abacum's modeling layer. The problem was identified with Julian (head of design). Ran competitor benchmark, synthesised GONG call evidence from the Swirldlabs call. Cross-squad ownership. Collaborated with Manuel C. (engineer) on syntax decisions. Unlocked the follow-on editor suggestions project.

Key decisions:
- Identified the problem as systemic, not a surface UI issue
- Chose to extend and standardise existing syntax rather than design a new one
- Worked across squad boundaries without formal mandate

Signals:
- Faster formula writing (qualitative, from user feedback)
- Quieter support channel (qualitative)
- Unlocked follow-on project (operational)

No hard metrics. Own this directly.

Colleagues named: Julian (head of design), Manuel C. (engineer collaborator).

---

### 2. Dataset Manager (Abacum)
URL: /cases/dataset-manager
Status: Complete and live

Summary: Introduced a UI abstraction layer over JSON-based dataset configuration, enabling finance teams to manage data autonomously.

Key decisions:
- First dedicated designer on the squad — had to establish the problem space before designing anything
- Ran 3 user tests: Maria, Eduardo, Guillermo, Oriol. Weighted Oriol most heavily (most experienced user)
- Identified language mismatch between product language (data types) and user language (dimensions)
- Decided not to introduce SQL. Extended Modeling Syntax instead (prerequisite work that closed the gap)
- Work was incremental due to technical constraints — this was the right call, not a compromise

Signals:
- Implementation team had less work (operational signal from CS and implementation teams)
- Customer autonomy increased (qualitative, from implementation team feedback)
- Oriol's session: specific moments where the abstraction landed

No hard metrics. Own this directly.

Colleagues / users named: Maria, Eduardo, Guillermo, Oriol (research participants).

---

### 3. Design Systems (Abacum + Remuner)
URL: /cases/design-systems
Status: Complete and live
Title: From scattered components to a production design system

Summary: Promoted, built buy-in for, and implemented production-ready design systems at two companies alongside regular product work.

#### Abacum (Abax)
- Built business case with Julian (head of design). Formal presentation to engineering leadership.
- Maker Days initiative to get engineering buy-in
- Two-tier token architecture
- Token Studio → Style Dictionary → GitHub → npm pipeline (engineer built the original pipeline)
- ESLint rules for adoption enforcement
- Storybook deployed in Chromatic
- Kept MUI as base — deliberate decision to reduce scope and accelerate adoption
- Covered five squads

#### Remuner
- Built component library from scratch. Sole designer.
- Defined the DS roadmap from zero
- Adapted the Abacum pipeline setup using AI assistance (Codex). Engineer approved the implementation.
- Separate icons file and icons repo
- Started with a small token set deliberately — lesson applied from Abacum (bigger token set created drift and maintenance overhead)
- Figma variables used throughout

Key signals:
- CTO at Remuner: "from a 2010 app to a 2020 app" (unprompted, during a review session)
- Storybook screen recording: placed as last item in the case, evidence the system works in production

Stack: Figma variables, Token Studio, Style Dictionary, GitHub submodule, Storybook, ESLint, npm packages, Chromatic

Technical ownership note: Manel adapted the token pipeline at Remuner using AI assistance. An engineer built the original pipeline at Abacum. Do not overstate technical ownership in copy.

Colleagues named: Julian (head of design, Abacum, co-led DS business case).

---

### 4. Rep Letters (Remuner)
URL: /cases/rep-letters
Status: Not started

Topic: AI agent for sales reps and managers — automatically generating compensation letters based on the rep's plan.

What shipped: The rep-facing and manager-facing AI agent.
What didn't ship: Admin natural-language interface (designed as a direction, not shipped). Frame transparently if included.

Open questions before investing time in this case:
- What signal exists on the shipped agent?
- How much of the design did Manel personally own vs. the team?

Do not write this case until these questions are answered.

---

## Portfolio evaluation standard

Cases must show:
- Problem complexity and ambiguity
- Candidate's specific role and decisions (not "we" without context)
- Cross-functional influence
- Measurable or operational impact
- What made it hard

## HTML section structure

Every section follows this pattern:

```html
<section>
  <h2>Section headline</h2>
  <p class="lead">Lead paragraph. One or two sentences. Sets the frame.</p>
  <p>Body paragraph.</p>
  <h3>Subsection if needed</h3>
  <p>Body paragraph.</p>
</section>
```

No section-label spans unless specifically requested. No decorative motion. Screen recordings as evidence of a system working are appropriate and encouraged.

## Outcomes section rules

- Use named qualitative signals. Name the person or team where it adds credibility.
- Own the absence of hard metrics directly. Do not hedge with "we believe" or "we think."
- Anchor outcomes in: named people's reactions, operational changes, follow-on work unlocked.
- Avoid: "the project was well received," "users found it easier to use," any vague positive claim.
