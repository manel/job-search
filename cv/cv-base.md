# CV Base — Manel Leiva

Single source of truth for all CV content. Do not edit role-specific outputs here. Edit this file, then generate role-specific versions in cv/roles/.

Format contract (from principles.md, "Brevity and skimmability"): each experience entry is 3 to 4 one-line bullets, strongest claim first. Role-specific CVs pick and reorder bullets per `context/positioning.md`; they do not add prose. The "Additional material" line under each entry holds verified detail available for role-specific swaps. It is not CV copy.

---

## Personal

Manel Leiva
Senior Product Designer
Barcelona, Spain
manel-leiva.com
linkedin.com/in/maneleiva

---

## Summary

Senior Product Designer with 15 years designing complex B2B products.
Built two production design systems from scratch, in fintech FP&A and sales compensation SaaS, including the token pipeline from Figma to a published npm package.
Works on data-heavy workflows directly with engineering, product, and business stakeholders.

---

## Experience

### Remuner — Senior Product Designer
May 2024 – March 2026 | Barcelona (Remote)

- Sole designer; owned product design and the design system across the full product surface.
- Built the component library and token pipeline from scratch: Token Studio to Style Dictionary to npm, with CI validation and the W3C token format.
- Designed and shipped an AI agent, a chat panel plus embedded in-app answers where sales reps and managers consult their commission data, sales plans, and team info; GA to all customers.
- Introduced Figma variables and a structured token architecture; the CTO described the change as going from a 2010 app to a 2020 app.

Additional material (verified, for role-specific swaps): deliberately small starting token set based on Abacum lessons; pipeline hardened with AI assistance (drift checks, smoke tests), engineers reviewed and merged the work; separate icons file and repo; ESLint adoption enforcement. Agent detail: Manel owned UX/UI, conversation design (tone, answer formats), capability scoping with PM and engineering, and trust/accuracy patterns; post-GA iteration on tone, response format, and per-customer terminology. Managers confirmed as real users 2026-07-06: most had their own comp plan and could query team info.

Stack: Figma, Token Studio, Style Dictionary, GitHub, npm, Storybook, Chromatic, ESLint.

---

### Abacum — Senior Product Designer
January 2022 – April 2024 | Barcelona (Remote)

- Built the Abax design system alongside product work: two-tier token architecture and a Token Studio to Style Dictionary to npm pipeline, adopted across five squads.
- Designed the Dataset Manager, a UI layer over JSON dataset configuration that let finance teams configure their data without engineering support.
- Standardised formula syntax across the modeling layer from competitor benchmarking and customer call evidence; made the syntax decisions together with an engineer.
- First designer on the integrations squad, then the engine squad; co-led the design system business case with the head of design and presented it to engineering leadership.

Additional material (verified, for role-specific swaps): structured user research on the Dataset Manager surfaced a language mismatch between product terminology and user mental models; made the call not to introduce SQL and extended the modeling syntax instead; the syntax work unlocked a follow-on editor suggestions project; kept MUI as the system base to reduce scope and speed adoption; ESLint adoption enforcement; Storybook in Chromatic.

Stack: Figma, Token Studio, Style Dictionary, GitHub, npm, Storybook, Chromatic, ESLint, MUI.

---

### Kings of Mambo — Co-founder, UX Design Lead
2010 – 2021 | Barcelona

- Co-founded and led a UX studio for 11 years; end-to-end product design for clients in media, retail, finance, legal, and culture, including a legal document management system and design plus front-end work for KYMCO.
- Built much of what I designed: full WordPress themes wired to the CMS, component libraries in Sketch mapped to front-end code, and by 2020 a shared front-end starter kit with a build pipeline and a CSS variables settings layer.
- Taught UX and digital design at postgraduate level, including a course taking a design file to a working CMS-driven site.

Additional material (verified, for role-specific swaps): work spanned research, information architecture, interaction design, and delivery; mentored junior practitioners; Advanced Custom Fields for CMS wiring; linting in the starter kit.

---

## Skills

Design: Figma, Figma Make, Token Studio, Storybook, Chromatic
Systems: Design tokens, Style Dictionary, component architecture, ESLint adoption rules
Research: Structured user testing, synthesis, Jobs to Be Done
Collaboration: Cross-functional facilitation, engineering alignment, stakeholder presentations
Prototyping: Figma Make (Claude-powered), high-fidelity interaction design
Tools: GitHub, npm, VSCode, Vercel

---

## Education

Higher National Diploma in Computing Design and Multimedia
ESI Barcelona, 2002

---

## CV reorder rules (for role-specific outputs)

The role-type → lead-story mapping lives in `context/positioning.md` ("How to position for specific role types"). That file is the canonical source; apply it when generating a role-specific CV in cv/roles/. Do not duplicate the mapping here.

Header title: each sent CV carries a custom title under the name, matched to the open role (established practice, confirmed 2026-07-06). Example: "Product Designer, Design Systems" for a DS role. The custom title applies to the CV header only; experience entry titles stay as they were held and are never inflated.

Output format: plain text only. No markdown formatting beyond line breaks and section headers. Designed for copy-paste into Figma.
