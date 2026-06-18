# Brand — Manel Leiva Portfolio

Extracted from the live portfolio CSS (`public/css/base.css`, `case.css`, `home.css`). This is the canonical visual language for all generated artifacts: slide decks, case study HTML, CV layout, any other output.

---

## Color

### Core palette

| Token | Value | Use |
|---|---|---|
| `--bg` | `#ffffff` | Page / slide background |
| `--text` | `#1d1d22` | Headings, primary text |
| `--text-muted` | `#3a3a4a` | Body text, supporting copy |
| `--accent` | `hsl(182, 50%, 36%)` ≈ `#2e8a8d` | Labels, links, bullets, dividers, interactive |
| `--border` | `#e5e5e9` | Dividers, card outlines |
| `--card-bg` | `#f7f7f8` | Subtle surface, code blocks |
| `--thumb-bg` | `#ebebef` | Image placeholders, video wrappers |

### Teal scale (brand hue: HSL 182)

| Step | Value | Hex approx |
|---|---|---|
| 50 | `hsl(182, 30%, 96%)` | `#f2f9f9` |
| 100 | `hsl(182, 34%, 91%)` | `#e3f4f4` |
| 200 | `hsl(182, 38%, 85%)` | `#ceedef` |
| 300 | `hsl(182, 41%, 80%)` | `#bce6e8` |
| 400 | `hsl(182, 43%, 76%)` | `#a8dadc` ← brand base |
| 500 | `hsl(182, 46%, 62%)` | `#6fc6c9` |
| 600 | `hsl(182, 48%, 48%)` | `#3ea9ad` |
| **700** | **`hsl(182, 50%, 36%)`** | **`#2e8a8d`** ← **accent (canonical)** |
| 800 | `hsl(182, 48%, 25%)` | `#1f6062` |
| 900 | `hsl(182, 44%, 16%)` | `#153e3f` |

### Presentation dark variant

When a dark background is required (slide decks, dark-mode assets), shift the palette as follows. Do not invent a new hue.

| Token | Light (portfolio) | Dark (slides) |
|---|---|---|
| Background | `#ffffff` | `#111417` |
| Surface | `#f7f7f8` | `#1a1e22` |
| Primary text | `#1d1d22` | `#f2f2f4` |
| Muted text | `#3a3a4a` | `#8a9099` |
| Accent | teal-700 `#2e8a8d` | teal-400 `#a8dadc` |
| Dim / disabled | `#e5e5e9` | `#2e3340` |
| Border | `#e5e5e9` | `#2e3340` |

Teal-400 (`#a8dadc`) is the accent on dark backgrounds. It passes contrast on the dark surface and preserves the brand hue. Do not substitute blue, purple, or any off-brand color as accent.

---

## Typography

**Font family:** Plus Jakarta Sans (Google Fonts)
Weights in use: 300 (light), 400 (regular), 500 (medium), 600 (semibold), 700 (bold)
**Fallback:** `-apple-system, BlinkMacSystemFont, sans-serif`
**Base size:** 16px
**Base line-height:** 1.7
**Rendering:** `-webkit-font-smoothing: antialiased`

### Type scale

| Role | Size | Weight | Line-height | Letter-spacing | Notes |
|---|---|---|---|---|---|
| Display / H1 | `clamp(1.575rem, 0.875rem + 2.1vw, 2.8rem)` | 700 | 1.1 | -0.03em | Hero headlines |
| Case title | `clamp(1.75rem, 3vw, 2.75rem)` | 700 | 1.15 | -0.03em | Case study headers |
| H2 | 1.625rem (26px) | 700 | 1.2 | -0.02em | Section headings |
| H3 / Work title | 1.25rem (20px) | 700 | 1.25 | -0.02em | Card/list titles |
| Lead | 1.3rem (20.8px) | 500 | 1.6 | — | First paragraph of a section |
| Overview lead | 1.1875rem (19px) | 500 | 1.85 | — | Overview section body |
| Body | 1.0625rem (17px) | 300–400 | 1.8 | — | Standard prose |
| Meta value | 0.875rem (14px) | 400 | — | — | Case meta row values |
| Small | 0.9rem (14.4px) | 300 | 1.7 | — | Work descriptions |
| Label / tag | 0.65–0.7rem (10.4–11.2px) | 600 | — | 0.08–0.12em | Uppercase section labels |
| Caption | 0.75rem (12px) | 400 | — | — | Image captions, opacity 0.55 |

**Label pattern:** All section labels and navigation tags are uppercase, weight 600, letter-spacing 0.08–0.12em, color `--text-muted` (or `--accent` for active/highlighted states).

---

## Spacing

Inferred from CSS. Use this scale; do not invent intermediate values.

`2 · 4 · 6 · 8 · 10 · 12 · 14 · 16 · 20 · 24 · 28 · 32 · 40 · 48 · 56 · 64 · 72 · 80 · 96px`

Key layout values:
- Sidebar width: 210px
- Layout gap (sidebar / main): 72px
- Layout max-width: 1280px
- Content max-width (prose): 660px
- Section margin-bottom: 48px
- Outcome block top padding: 40px (with 2px accent top border)
- Hero padding-top: 132px

---

## Border radius

| Size | Value | Use |
|---|---|---|
| XS | 4px | Badges, inline chips |
| S | 6px | Thumbnails, small cards |
| M | 8px | Inputs, code blocks, images |
| L | 10px | Card panels, before/after components |
| XL | 12px | Formula/code containers |

---

## Visual patterns

**Dividers:** 1px solid `#e5e5e9`. Decorative horizontal rule: 40px wide, 1px height, `--border` color.

**Accent divider (outcomes):** 2px solid `--accent` at the top of the outcome block. This is the only use of a thick accent line.

**Bullets:** 5px circle, `--accent` fill. `position: absolute; left: 0; top: 12px`.

**Before/After panels:**
- Container: 1px border, radius 10px, overflow hidden
- Before panel: white background
- After panel: teal-50 (`#f2f9f9`) background
- Label badge: `background: rgba(86, 103, 249, 0.1); color: var(--accent)` — small, uppercase, 0.6rem

**Animation:** `fadeUp` — `opacity: 0; transform: translateY(16px)` → `opacity: 1; transform: translateY(0)`. Duration 0.5–0.6s ease. Staggered on list items.

**Cards/thumbnails:** `aspect-ratio: 16/9`, `background: --thumb-bg`, radius 6px.

---

## Slide deck composition rules

These rules apply to every presentation deck generated in this project. The current decks (Dataset Manager, Design Systems) use Inter + blue accent and must be updated to match.

### Fonts
Use **Plus Jakarta Sans**. Weight 700 for headlines, 500 for labels/sub-copy, 400 for body, 300 for captions.

### Colors (dark deck)
- Background: `#111417` (rgb: 17, 20, 23)
- Surface for notes strip: `#1a1e22`
- Primary text: `#f2f2f4`
- Body/muted text: `#8a9099`
- Accent: teal-400 `#a8dadc` (rgb: 168, 218, 220)
- Dim (notes, placeholders, slide numbers): `#2e3340`
- Separator lines: `#2e3340`

### Layout (1920×1080)
- Left margin: 120px
- Label: y=270, 13px, weight 500, accent, letter-spacing 2.8px, uppercase
- Headline: y=314, 56px, weight 700, primary text, width 1480px, line-height 72px
- Body: y=614, 26px, weight 400, muted text, width 1300px, line-height 42px
- Visual placeholder: y=882, 13px, weight 400, dim, width 1500px
- Notes separator: y=936, 1px, dim
- Notes label: y=946, 10px, weight 500, accent, letter-spacing 2px
- Notes text: y=960, 12px, weight 400, dim, width 1680px, line-height 18px
- Slide number: x=1848, y=1020, 16px, weight 400, dim

### Cover slide
- Accent bar: x=120, y=318, 64×4px, accent teal-400
- Headline: y=346, 76px, weight 700, line-height 92px
- Sub: y=522, 30px, weight 400, muted
- Author credit: y=988, 16px, weight 500, dim

### Accent usage
The teal accent appears in exactly three places per slide:
1. The label (uppercase category tag, top-left)
2. The notes label ("NOTES")
3. The accent bar on the cover slide

Do not use teal for body text, borders, or decorative elements beyond these three roles.

### What the current decks need to update
1. **Font:** Inter → Plus Jakarta Sans
2. **Accent color:** `#4A7AFF` (blue) → `#a8dadc` (teal-400)
3. **Background:** `#0F1115` → `#111417`
4. **Muted text:** `#8A92A6` → `#8a9099`
5. **Dim color:** `#3B4157` → `#2e3340`

---

## What not to do

- Do not use blue, purple, or any non-teal accent. The brand hue is HSL 182.
- Do not mix light and dark backgrounds within a single deck.
- Do not use Inter or any other font. Plus Jakarta Sans only.
- Do not add decorative gradients, shadows, or glows. The visual language is flat and typographic.
- Do not add company logos or external imagery unless explicitly provided.
- Do not change spacing outside the defined scale.
