# Build scripts: merged site, 15 Oct 2026

This site = public-education snapshot (13 pages) + counselling page + new
"Counselling & Communication" category. All scripts are idempotent.

Order used to produce Family-Medicine-Guides/:

1. Start from the public-education site; copy counselling.html and downloads/*.pdf from the counselling snapshot.
2. `python3 update_site.py`: wires counselling into the nav, Mental Health and Respiratory, homepage pill, directory, search (edit the SITE path at the top).
3. `python3 public-education-source/apply_updates.py SITE`: credit block, menu rows, wrap fix.
4. `python3 public-education-source/build_pages.py SITE` then `apply_updates.py SITE --entries public-education-source/_out/public_entries.json`: Patients hub now lists the quit-smoking leaflet.
5. `python3 add_counselling_category.py SITE`: new top-level category (homepage card, directory section, menu panel; 22 categories).

On the full 17-page copy from the main PC (counselling.html is already there): run steps 3–5.

## Update, 11 Nov 2026: master instructions v2.1 applied

- **No em dashes.** Every script, content file and page was converted (colon, comma, semicolon or parentheses; `|` in page titles; `-` in empty cells). `npm run check` (`tools/check-style.mjs`) fails if one comes back.
- **Leaflets rebuilt** from these sources so the PDFs and cards carry no em dash:
  - `public-education-source/build_leaflets.py SRC` and `build_peds_leaflets.py SRC`, where `SRC` is the site's `src/` folder.
  - `counselling-source/build_pdfs.py` (quick reference and quit-smoking leaflet). These two now carry the credit and AI-assistance lines in the footer. Note: this script still has fixed working paths at the top (`S`, `OUT`); edit them before running.
- Fonts: `npm pack @fontsource/inter@5.3.0 @fontsource/fraunces@5.3.0 @fontsource/ibm-plex-sans-arabic@5.3.0`, unpack each to a folder named after the tarball, and point `FMG_FONTS` at the parent folder.
- The one-off wiring scripts in this folder (`update_site.py`, `add_counselling_category.py`, `add_peds_er.py`, `add_peds_leaflets_site.py`) were written for earlier layouts. They are kept as a record. Do not re-run them without checking their anchors against the current pages.
