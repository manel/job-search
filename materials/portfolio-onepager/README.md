# Portfolio one-pager

One-page A4 PDF with three case cards (design systems, Remuner design system from scratch, Dataset Manager) and clickable links. Built 2026-10-19 for Flodesk's upload-only portfolio field; reusable for any form that requires a portfolio file.

- `portfolio.html`: source. Thumbnails come from `portfolio/public/assets/thumbnails/` (copy them next to the HTML before rendering).
- Render: Playwright's Chromium, `--headless=new --no-pdf-header-footer --virtual-time-budget=8000 --print-to-pdf=...`.
- Follows `context/brand.md` (Plus Jakarta Sans, teal-700 accent, white background).
- The full multi-page portfolio PDF is a separate TODO.
