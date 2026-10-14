# Kings of Mambo — e-commerce evidence

Evidence updated 2026-10-11. Reusable commerce evidence gathered during PromoFarma preparation. The vacancy closed without submission; the unsent tailored CV was deleted on 2026-10-13.

## Confirmed by Manel

Manel identified four KoM e-commerce projects: FUNK3D (Shopify theme), Somia (WordPress/WooCommerce), Kymco e-bikes (custom commerce), and Kymco bikes (custom commerce).

Follow-up confirmation, 2026-10-11:

- Full design-process and frontend responsibility applies to Kymco, not the other stores. Kymco shopping/checkout flows launched and took real orders.
- Manel remembers designing and implementing modular content blocks so content managers could add, remove and edit blocks on individual bike pages. This is a confirmed account of his contribution and intended usability benefit; no measured editing-time improvement is claimed.
- On the other stores, Manel owned implementation rather than design: frontend and platform configuration. For WordPress work, this included setup, ACF custom fields and connecting the frontend to managed content. Apply WordPress/ACF specifically to the WordPress project, not FUNK3D's Shopify theme.
- “Owner of everything else” is recorded as broad implementation responsibility on those stores. It does not independently establish sole backend/payment engineering, infrastructure, commercial operations or Shopify checkout ownership.

Exact project dates, discovery/research methods, measured results and the other stores' historical launch status remain unknown.

## FUNK3D live-site inspection

External research, verified 2026-10-11: https://funk3d-bcn.com/ shows product categories/collections, product cards and pricing, search, account login, cart, bundles/offers, shipping/returns information and a Kings of Mambo footer credit. Shopify CDN assets corroborate the user-confirmed platform.

The current site supports studio attribution and commerce context. It does not establish that every current screen or feature is Manel's historical work, nor personal responsibility for Shopify's checkout/payment functionality.

## Kymco repository inspection

Read-only static inspection of `/Users/manel/Dev/kymco`, 2026-10-11. October CMS theme and custom `Kymco.Shop` plugin. No application executed, database inspected or live transaction attempted. The repository includes bicycle and motorbike branches; it does not by itself establish separate deployment histories for the two projects.

| Area | Code evidence | Relevant capability |
| --- | --- | --- |
| Product browsing | `themes/kymco/pages/product.htm`, `page-compare.htm`, product partials | Complex product information and comparison |
| Cart | `themes/kymco/partials/carrito1/default.htm`, `kom-dev/js/main.js` cart interactions | Basket and add-to-cart interactions |
| Delivery/dealer | `themes/kymco/pages/checkout-00.htm`, `checkout-01.htm`, `checkout-01-shipping.htm` | Purchase branches by product type, dealer collection and home delivery |
| Identity/billing | `checkout-02.htm`, `checkout-03.htm`, register variants | Account/login, customer data, company billing and validation |
| Payment | `checkout-04.htm` | Card and bank-transfer interfaces; financing/Plan Dúo code and explanatory copy |
| Completion/errors | `checkout-05.htm`, `checkout-success.htm`, `checkout-error.htm` | Confirmation and failure states |
| Reservations | `res-checkout-*.htm` | Separate reservation journey |
| Customer account | `mi-kymco-orders.htm`, `mi-kymco-data.htm`, `mi-kymco-testdrives.htm` | Order history, account information and test-drive area |
| Operations | `plugins/kymco/shop/controllers/Orders.php`, `Products.php`, `Dealers.php`, `Coupons.php`; model field schemas | Order/status/delivery/dealer administration, catalogue and promotion areas |

Important qualification: payment template contains a comment that financing options are temporarily disabled. Manel has confirmed launch and real orders for the shopping/checkout flows; this does not establish historical availability of every payment option. Do not list all backend modules as personal design work: the specifically confirmed admin contribution is modular page-content editing.

## CV implications

This materially strengthens direct commerce relevance. Manel has earlier custom-commerce design and frontend experience at Kymco, plus implementation ownership across Shopify and WooCommerce projects, followed by complex B2B product work. Keep design ownership distinct from implementation ownership. Kymco establishes launched transactional work, not merely a promotional website.

CV-ready wording:

“Designed and implemented the frontend for Kymco's custom e-commerce experiences, including shopping and checkout flows that launched and handled real orders.”

“Designed and implemented modular page-content blocks, enabling content managers to add, remove and edit content for individual bikes.”

“Owned frontend implementation and platform configuration for FUNK3D's Shopify theme and Somia's WooCommerce store, including WordPress setup, ACF fields and frontend integration for Somia.”

Do not claim conversion uplift, AOV/retention gains, A/B testing, multi-market localization or recent high-volume commerce expertise from this evidence.

## Remaining useful detail

### Conversion and experimentation follow-up, 2026-10-11

Manel recalls conversion improvements and A/B testing, without specifics. Recorded as recollection, not verified experiment evidence. Targeted static search of theme pages/partials, main frontend script and shop components found no identifiable A/B-test setup for common experiment tooling. This limited search cannot establish that experiments never occurred or exclude externally configured tooling.

Repository history includes checkout/tablet/mobile fixes, dealer/map changes, postal-code validation and checkout-detail updates (2019–2021). These are useful recovery leads, not proof of conversion optimization intent, personal authorship, test variants or results. GTM/dataLayer artifacts exist, with some commented out; this does not prove active historical tracking or analytics-led decisions.

Use Kymco's verified launched checkout and content-block work as the historical story. Discuss conversion hypotheses and measurement as a proposed approach to PromoFarma, explicitly distinct from past experiments. No invented baseline, uplift, sample size or winning variant.

- One consequential checkout/design decision, its constraint, and any qualitative or measured outcome; exact dates and Somia URL/repository if available. These would improve an interview story but are not prerequisites to using the confirmed responsibilities in the CV.
