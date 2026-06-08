# Principles

Writing rules and tone standards that apply to every output: CVs, cover letters, case studies, portfolio copy.

---

## Hard rules

- No em dashes. Rewrite every em dash as a comma, period, or new sentence.
- No colon-list stacking. Use prose.
- No bullet points in cover letters or case study body copy.
- Active voice. Address the reader directly where appropriate.
- No "we" without immediately clarifying your specific role.
- No overclaiming. If you didn't own it fully, say what you owned.
- No metrics that aren't real. Own the absence of hard numbers directly.

---

## AI pattern blacklist

These words and phrases make copy sound generated. Never use them.

**Vocabulary:**
insights, leverage, optimize, streamline, unlock, enable, empower, holistic, robust, dynamic, seamless, scalable, nuanced, tapestry, multifaceted, foster, cultivate, facilitate, utilize, comprehensive, superpower, journey, overall, absolutely, typically, various, elevate, essentially, certainly, realm

**Phrases:**
- "not only...but also"
- "here's a breakdown"
- "in the ever-evolving landscape"
- "a testament to"
- "driving impact"
- "laying the groundwork"
- "here's what nobody tells you"
- "the truth is"
- any sentence starting with "Ultimately,"
- any sentence starting with "It's worth noting that"
- "I am excited to"
- "I am passionate about"
- "I would love the opportunity"

**Structural patterns to avoid:**
- Three-part parallel structure ("X, Y, and Z" repeated across multiple sentences)
- Colon-list pattern (heading: then a list)
- Summary closing paragraphs that restate what was already said
- Uniform paragraph length throughout
- Credential stacking openers
- Honesty disclaimers ("To be honest..." / "If I'm being direct...")

---

## Voice

Write like a sharp operator explaining something to a peer. Calm. Specific. Grounded. Mix short sentences with longer ones. Let it feel slightly unpolished but controlled. No punchline energy. No performance.

For cover letters: direct, confident, no performative enthusiasm. State what you did, what you noticed about the role, and why the fit is real. Don't dress up weak fit with strong language.

For case studies: first-person, present tense where possible. Name the decision. Name the constraint. Name the person where it adds credibility. Avoid vague process narration ("I conducted research and synthesized findings").

---

## Humanizer checklist

Run this before outputting any professional written content.

- [ ] No em dashes anywhere
- [ ] No words from the AI vocabulary list
- [ ] No phrases from the AI phrase blacklist
- [ ] No three-part parallel structure repeated more than once
- [ ] Paragraph lengths vary (not all short, not all long)
- [ ] No summary closing that restates the opening
- [ ] No "I am excited / passionate / thrilled"
- [ ] Specific over generic: names, decisions, tradeoffs, not process narration
- [ ] Active voice throughout
- [ ] No overclaiming ownership

---

## Format rules by output type

### CV
- Plain text only. No markdown. No bold. No bullets in the main column.
- Sidebar skills section exists but is not a "core competencies" block.
- Two-column layout implied by section structure (Claude doesn't need to reproduce the layout, just the content hierarchy).
- Experience entries: role title, company, dates, then 3–5 lines of plain prose or tight bullets depending on section.
- No "Cases" section in CV. Portfolio URL handles navigation.

### Cover letter
- Plain text. Three to four paragraphs.
- No subject line unless specifically requested.
- No sign-off flourishes beyond "Best, Manel" or equivalent.
- Salary position confirmed before writing. Stated clearly in the letter if the role asks for it or it's strategically appropriate.

### Case study HTML
- Section structure: h2 headline, lead paragraph with class="lead", body paragraphs, h3 subheadings for subsections.
- No section-label spans unless specifically requested.
- No decorative motion. Screen recordings as evidence of a system working are appropriate.
- Outcomes sections: use named qualitative signals. Own the absence of metrics directly. Don't hedge with "we believe" or "we think."
