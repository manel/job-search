# Kings of Mambo archive audit

Audit run 2026-11-13 on `/Volumes/Documents/Jobs/KoM` (folders `e-Mail`, `Projects`, `Sites`). Read-only: nothing on the volume was moved, renamed or changed. Nothing from the archive was copied into the repo except these notes.

Internal reference only. Client and person names here are for recall and checking; live case copy never names them ([.claude/conventions/how-to-work.md](../../.claude/conventions/how-to-work.md)).

Status: Step 1 (inventory) and a first pass of Step 4 (email) are done. Steps 2, 3 and 5 are not started. Nothing here has gone into [evidence/experience-facts.md](../experience-facts.md) yet.

## What was skipped

- The KoM root folder holds company closure, tax, bank and payroll documents. Not opened.
- Email: Spam and Trash kept headers only. Subjects with invoice, payment, payroll or tax words were filtered out of the project dumps. Labels `Invoices` and `CVs` were not read.
- No live site was checked.

## Inventory

| Folder | Content | Size | Dates |
|---|---|---|---|
| `e-Mail` | `kom_email.tar.gz`: one Gmail mbox, "All mail Including Spam and Trash" (22 GB uncompressed) | 12 GB | archived 2023-11-06 |
| `e-Mail` | Google Takeout zip: calendars (KoM Projects, KoM calendar, personal) and mail settings; no mail | 424 KB | 2021-10-25 |
| `Projects` | `KYMCO-site.sketch` (Sketch 69.1, 10 pages, 274 artboards) | 1.2 GB | 2021-02-08 |
| `Projects` | `LaBasad.sketch` (12 artboards, 22 symbols), `LaBasad Library.sketch` (8 symbols) | 3 MB | 2020-04/05 |
| `Projects` | KYMCO SEO audit PDF, 31 pages (third party, 2020-12-17) | 1 MB | 2021-01-25 |
| `Sites` | `Sites.tar.gz`: the full local `Sites` folder, 37 folders, about 498,000 files | 15 GB | 2021-10-28 |
| `Sites` | 23 per-site `.tgz` files: a 2023 re-archive of a subset of the same folders | 14 GB | 2023-11-10 |

`KYMCO-site.sketch` pages: Proceso de compra (36 artboards), Proceso de prueba (13), Zonas privadas (14), Header/menú (19), Páginas (43), Landings scooters (90), FAQs (26), Mapa concesionarios (5), Actualización accesorios (5), Symbols (23). The file does not record who made it.

Folders in `Sites.tar.gz` only (not in the 2023 set): blafer, josecamarena, rogerdiaz, manel-leiva (portfolio site, Hugo plus Tailwind, 2021), ux, grades, webpack test projects, two third-party repos.

`Sites/ux/`: a 2019 UX exercise "Coches.net Explore" with wireframes, design and prototype images and a Sketch file. Purpose not known (a hiring exercise?).

## Email at a glance

- 257,759 messages, 2008 to 2021. Busiest years: 2012 (31,234) and 2014 (26,982).
- Account: `manel@kingsofmambo.com`. About 22,000 sent messages; sent volume peaks in 2021 (3,703).
- 149 Basecamp projects appear in notification subjects. Basecamp does not email authors their own posts, so Manel's posts are missing from the mailbox.
- Most active Basecamp posters: Josep Ortega (9,686, KoM), Jordi Galed (1,857), Olivier at Kymco (1,812), Eric Cardona (1,730, KoM).

### Clients by messages Manel sent

Top of the list, from `To` and `Cc` domains on sent mail (generic mail domains removed):

| Client | Sent | Years | Typical threads |
|---|---|---|---|
| Grupo Godó (RAC105, La Vanguardia blogs) | 1,560 + 253 | 2011 to 2021 | staged deploys (test, then production), migrations |
| 8TV, 8 al dia | 1,183 + 219 | 2011 to 2018 | new site, typography, deploys |
| Kymco and its partners (SGA, Disi, Sinergia, CaixaBank P&C) | about 2,000 | 2016 to 2021 | purchase and reservation flows, dealer integration, financing |
| Stan James (desdelabanda) | 294 | 2009 to 2011 | quiniela, hosting |
| Dezero (FUNK3D, Crowdeen) | 277 | 2013 to 2021 | project review, design to-do list |
| Front London | 222 | 2015 to 2018 | site hosting, video issues |
| Profits Online (TROA) | 188 | 2010 to 2013 | templates for schools and parents, audit |
| Adacyte | 133 + 109 (translation agency) | 2020 to 2021 | site in three languages, calculator |
| Celingest, Softonic | 126 + 61 + 48 | 2010 to 2016 | corporate site and migrations |
| vLex | 55 | 2016 to 2019 | IE errors, CDN |
| NoviCap | Basecamp only | 2019 to 2021 | new website |

## Git authorship (from `Sites.tar.gz`)

Only the `.git` folders were extracted, to the session scratchpad. Counts include small commits.

| Repo | Commits | Years | Manel | Others |
|---|---|---|---|---|
| kymco | 1,986 | 2019 to 2021 | about 1,690 | fjgarces 288 |
| kymco-ebikes | 852 | 2018 to 2021 | about 470 | Javier Garcés 352 |
| kymco-old | 608 | 2017 to 2020 | about 458 | Xavi Blanch 55, Cata 48 |
| bit | 633 | 2017 to 2020 | 161 | Jordi 406 |
| opertek | 586 | 2019 to 2021 | 152 | Jordi 302, jotagebe 78 |
| somia | 370 | 2020 to 2021 | 351 | jotagebe 19 |
| inmolovers | 347 | 2018 to 2020 | about 323 | Jordi 17 |
| adacyte | 345 | 2020 to 2021 | 335 | jotagebe 9 |
| vlex | 341 | 2016 to 2020 | about 232 | Cesc Zafra 26, root 36 |
| funk3d | 232 | 2021 | 150 | fabian-dz 54 |
| siquia | 226 | 2020 to 2021 | about 225 | none |
| joinenergy | 127 | 2021 | 3 | jotagebe 93, Jordi 31 |
| chester | 104 | 2021 | 1 | jotagebe 62, Jordi 41 |
| iceberg-design | 82 | 2016 | about 65 | CescZafra 10 |

The kymco numbers match the 2026-10-22 inspection of `~/Dev/kymco` already in the register.

## Findings that matter for positioning

### 1. Kymco was a six-year, multi-system program

Email shows a longer and more operational program than the register describes:

- 2016 to 2017: landing pages, a dealer search by province, a dealer database.
- 2017 to 2018: Kymco eBikes. Wireframes and mobile proposals, an e-commerce build, an integration with an outside system for delivery notes and the assignment of vehicles to dealers ("cesiones"), test-ride booking, a press room, a dealer private area.
- 2019 to 2020: new kymco.es. Purchase process, test-ride process, dealer finder and dealer pages, financing pop-up, measurement project with an analytics agency (2020-04).
- 2020 to 2021: accessories purchase flow, CaixaBank P&C online financing, shipping integration, pre-reservation and reservation flow (2021-01 to 2021-10), dealer landing pages, scheduled vehicle assignments.

The systems around the site: SGA (dealer and vehicle assignment data), Disi (delivery notes), A3 (ERP), CaixaBank P&C (financing), a payment gateway, a shipping provider, and an outside developer (Sinergia) on back-end and API work.

In his own emails, Manel coordinated these integrations, tested full processes (new user, returning user, changes, cancellations), found sync bugs (users with development IDs in production) and added loading states so the process did not look stuck (2018-06). This is evidence of complex B2B2C workflow work: dealers, vehicle assignment states, financing and reservations across several systems.

### 2. Who designed Kymco (resolved 2026-11-13)

In email, many Kymco design deliveries (wireframes and design deliveries, 2019-10; purchase-process revision, 2020-02) were posted in Basecamp by Eric Cardona, a KoM designer. Manel's posts don't appear (see above), so email cannot show his share. Manel, 2026-11-13: both designed, and Manel was the lead designer. Recorded in [evidence/experience-facts.md](../experience-facts.md) under "Named e-commerce projects".

### 3. Other projects with product or workflow content

- vLex App (2016): three design deliveries and a Topics screen. Separate from the vLex design-system work. Email has no trace of the design-system project.
- NoviCap (2019, fintech): website with wireframes, an icon library, forms with a CRM integration, a review with founders and leadership. Mainly a marketing site. One fintech instance, so the finance one-mention rule applies.
- Joinenergy (2021): identity, site architecture, use cases (user registration workflow), a pre-analysis tool, API access, wireframes and a prototype. Manel has 3 of 127 commits there, so his role was not front-end.
- Telemaki (2020): architecture and wireframes, prototypes on InVision, posted by Eric Cardona.
- Mind Analytics (2018 to 2019): content architecture, wireframes, design proposals, a corporate presentation.

### 4. Team signal

Recurring KoM people in Basecamp and git: Josep Ortega (most project posts), Eric Cardona (design deliveries 2019 to 2021), Jordi and jotagebe (development 2017 to 2021), Cata, Cesc Zafra, Xavi Blanch. The team size per year is not recorded.

## Kymco Sketch file (read 2026-11-13)

`Projects/KYMCO-site.sketch` read without Sketch: page JSON unzipped to `~/Dev/kom-audit/sketch/kymco-site/`, full text outline in `~/Dev/kom-audit/sketch/kymco-site-outline.md` (script `sketch_outline.py`). The file records no author. Sample data in the screens is dated September 2019 and uses a 2020 coupon code, so the designs date from 2019 to 2020, matching the new-site emails. Every flow has a desktop (1440) and a mobile (320) version. No prototype links between artboards.

**Test-ride booking ("Proceso de prueba", 13 artboards).** Five steps, with a "your booking" summary panel on every step:

1. Dealer: search by address, province or postcode, or use current location. Dealer cards show distance, opening hours, official dealer and official service badges.
2. Day and time: calendar plus hourly slots.
3. Log in or register.
4. Personal data: name, ID number, phone, email, preferred contact channel, privacy and marketing consent. The copy explains why: so the customer can change the booking and be told of any change.
5. Booking confirmed, with share buttons.

The step bar on these screens still says "Envío, Forma de pago" (shipping, payment): copied from the purchase flow.

**Purchase ("Proceso de compra", 36 artboards).** Eight steps:

1. Product and total price.
2. Accessories offered for the scooter (top case and its options, four states), coupon code entry and applied-coupon state.
3. Pick-up dealer, with the note that the dealer calls when the scooter arrives.
4. Dealer selected. A Canary Islands variant blocks online sale and sends the customer to a point of sale.
5. Register, "to know the status of your order at all times".
6. Customer data. Financing only for individuals and self-employed.
7. Payment: credit card, bank transfer, CaixaBank financing, Plan Dúo. A v2 lists the documents needed to apply for financing, split by CaixaBank customer or not. The copy explains that the dealer completes registration of the vehicle after delivery.
8. Purchase confirmed.

Mobile adds an expandable order summary.

**Customer area ("Zonas privadas", 14 artboards).** My data, My vehicles (with periodic service), My orders (with status), My test rides (change or cancel), Contact.

**Later additions.** "Actualización accesorios" (5): purchase step 3 redesigned, with a home-delivery option. "Mapa concesionarios" (5): dealer map searchable by postcode or province, filter by services.

Other pages: FAQs (26), header and menu (19), scooter landing pages (90), content pages (43), symbols (23).

What the file shows for hiring: the flows handle real business constraints (regional sales block, financing eligibility, dealer pick-up and later vehicle registration, accessory dependencies, coupons) and the customer area closes the loop on bookings and orders. It does not show who drew which screen; Manel was lead designer with Eric also designing.

To see the screens: Figma imports `.sketch` files (no Sketch license needed). Manel runs that import himself; at 1.2 GB it may be slow.

## Targeted email searches (2026-11-13)

Script `mbox_search.py`; results in `~/Dev/kom-audit/searches/` (`ds.tsv`, `incidents-sent.tsv`). Newsletters, promotions and forums were filtered out.

### Design-system work for other clients

No email evidence of client design-system work, for vLex or anyone else. The hits are brand style guides (Stan James 2010, SNTalent 2012, Creditoh! 2017, Godó Strategies 2019, a CaixaBank exhibition site 2019) and one 2021 estimate for "nanoMOOCs" that lists a "UI design system for interactive web pieces" as a deliverable; whether it was sold is unknown. The LaBasad Sketch files (2020) hold a small symbol library (22 symbols, plus an 8-symbol library file).

The mailbox ends in October 2021. The vLex design-system work may have run through another channel or after that date. Either way, the register's vLex entry rests on Manel's statement alone; nothing here contradicts or corroborates it.

### Incidents

Manel's sent mail with apology, delay or complaint words: 200 threads, mostly small (late replies, hosting). The useful ones:

- **Kymco new site, delivery date (2019-05-31 to 2019-07-10).** Manel wrote to Kymco's project manager and the integration partners that the new site was still in design, with screens waiting on Kymco's feedback, and that 30 June was impossible: "we need three more weeks", to the week of 22 July. The client side answered that the commitment was to finish in July and pressed for status; the ERP partner had been ready for weeks and was waiting to test orders. Manel set a meeting with the back-end developer and reported back. Emails from April 2020 (training on the new site, the measurement project) suggest the new site went live around then, well after July 2019. Inference only: the launch date and the reasons for the later slip are not established. Manel does not remember what happened between July 2019 and the launch (asked 2026-11-13), so this is not usable as a story beyond the 2019-05-31 email itself.
- **8TV video players (2013-04).** Players on the 8TV site failed after a change; Manel reported the fix and apologised for the disruption. Small.
- **Kymco coupons (2019-04 to 2019-06).** Manel specified rules for stacking coupons with active campaigns (a per-coupon checkbox to block stacking; showing "-10% applied, -5% extra" in the order summary). Not an incident, but a design decision with business rules.

Also found: in 2019-06 the ERP partner warned that the customer-area vehicle lookup must not let users edit their ID number, or it could be used to pull third parties' data. A privacy constraint the "My vehicles" design had to respect.

## Kymco attachments (extracted 2026-11-13)

Both are in `~/Dev/kom-audit/attachments/`.

- **`kymco-shop-orders.xlsx`** (Manel to Kymco, 2018-11-20): an eBikes order export with three orders only. Columns: customer data, payment mode, delivery mode (dealer or home), assembled or not, status, dealer, prices, up to ten products. It shows the order data model. It gives no volume. It holds customer personal data; do not quote rows.
- **`Analytics Sin IP KYMCO Páginas de destino 20190401-20200331.xlsx`** (analytics agency, 2020-04-30): Google Analytics landing pages for the old kymco.es, 2019-04-01 to 2020-03-31, internal IPs excluded. KoM built and ran that site (repo `kymco-old`, 2017 to 2020).
  - 2,515 landing pages, 2,133,292 sessions in total. The home page had 691,248 sessions.
  - The only goal set up was "dealer page views": 262,871 completions.
  - The daily sheet adds up to 4,308,732 sessions, about twice the landing-page total. The cause is not known (another segment or a different filter).
  - The test-ride landing page `/genius/prueba-de-conduccion.html` had 1,327 sessions. The dealer finder `/concesionarios-servicios-tecnicos/` had 30,386.
  - This is one year of traffic before the new site. It has no before and after comparison and no purchase or booking figures, so it shows scale, not an outcome.

## Not checked

- Message bodies outside the Kymco, NoviCap, Joinenergy, Adacyte, Mind Analytics, Godó, 8TV and Ubiqum projects.
- Attachments: not extracted (about 9,000 PDFs, 400 docx, 73 `.ai` files in email).
- The Sketch files' screens: only page and artboard names were read.
- The site code beyond git authorship. `Sites.tar.gz` has about 3,000 PDFs and docx files, almost all in WordPress uploads.
- The calendar files in the Takeout zip.
- Live sites.

## Working files

Kept outside the repo in `~/Dev/kom-audit/` (6 GB, moved there 2026-11-13). Not in git; it holds client correspondence.

- `kom-email/index.jsonl` (503 MB): one line per message with headers, attachment names and the body capped at 6,000 characters. Spam and Trash have headers only.
- `kom-email/stats.json`: year, label, sent-to domain and Basecamp project counts.
- `kom-email/projects/`: thread timelines (`*-threads.tsv`) and Manel's sent bodies (`*-sent.txt`) for Kymco, NoviCap, Joinenergy, Adacyte, Mind Analytics, Godó, 8TV and Ubiqum.
- `kom-git/Sites/`: the `.git` folders of 32 site repos (5.4 GB). Read with `git --git-dir=<repo>/.git log`.
- `kom-listings/`: file listings of every archive on the volume.
- `attachments/`: attachments pulled from the mailbox on request.
- `scripts/`: `mbox_index.py`, `mbox_stats.py`, `mbox_project.py`, `mbox_attachments.py`. Each reads the mbox from stdin: `tar -xOzf /Volumes/Documents/Jobs/KoM/e-Mail/kom_email.tar.gz | python3 -I scripts/<script> ...`. Nothing is extracted to disk.

## Questions for the recall session

Ask one at a time.

1. ~~Kymco: who designed what?~~ Answered 2026-11-13: both, Manel as lead designer. Still open: which flows did you design yourself (purchase, test ride, reservation, dealer pages)?
2. ~~Kymco "cesiones"?~~ Answered 2026-11-13: a test-ride loan; the customer chose dealer and model. Mailbox details recorded in [evidence/experience-facts.md](../experience-facts.md).
3. ~~Team roles and size?~~ Answered 2026-11-13: Josep co-founder, Eric designer, about six people, stable; periods not recalled.
4. ~~Figures from the 2020 measurement project?~~ Answered 2026-11-13: none recalled. Two attachments in the mailbox may hold figures: `Analytics Sin IP KYMCO Páginas de destino 20190401-20200331.xlsx` (agency email, 2020-04-30) and `kymco-shop-orders.xlsx` (Manel, 2018-11-20, eBikes orders; contains customer data, so read counts only).
5. ~~The vLex App in 2016?~~ Answered 2026-11-13: Manel was part of the design, Josep led; app not remembered. Recorded in [evidence/experience-facts.md](../experience-facts.md).
6. ~~The Coches.net Explore exercise in 2019?~~ Answered 2026-11-13: a hiring exercise. Not client work, so not in the register. Possible reference for live-challenge prep.
