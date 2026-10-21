# Public education & credits — source scripts

Built 13 Oct 2026 against the 10-page public repo (HEAD 7ebf037).

## What these scripts do

| Script | Does |
|---|---|
| `apply_updates.py SITE` | Adds the bilingual credit block to every page footer, adds "For patients & families" and "About this site" to the shared menu, adds the patient band and pill to the homepage, and adds the `.wrap` phone-width fix (`FMG-WRAP-FIX`) where missing. Idempotent: run it as often as you like. |
| `build_leaflets.py SITE [--final]` | Renders each leaflet to a 2-page A4 PDF and a 1080×1350 summary card (EN + AR) in `SITE/downloads/leaflets/`. Without `--final` they carry a DRAFT stamp. |
| `build_pages.py SITE` | Writes `about.html` and `patients.html`. Links each leaflet to its clinician guide if that page exists (e.g. `ramadan.html`), and lists the quit-smoking leaflet only if its PDFs are in `SITE/downloads/`. |
| `apply_updates.py SITE --entries _out/public_entries.json` | Replaces the public pages' entries in `search-index.js`. |
| `readability.py` | Reading-grade check for the English leaflet text. |

Content lives in `leaflet_content.py` (leaflets) and `build_pages.py` (hub and About text). Shared blocks are in `shared.py`.

## Running it on the full 17-page copy

```
python3 apply_updates.py  /path/to/site
python3 build_leaflets.py /path/to/site
python3 build_pages.py    /path/to/site
python3 apply_updates.py  /path/to/site --entries _out/public_entries.json
```

Fonts for the PDFs: `npm pack @fontsource/inter @fontsource/fraunces @fontsource/ibm-plex-sans-arabic`, unpack each to a folder named after the tarball, and point `FMG_FONTS` at the parent folder.

## Marker blocks

`FMG-CREDIT`, `FMG-NAV-PUBLIC` (inside `FMG-NAV`), `FMG-PUBLIC` (homepage band), `FMG-WRAP-FIX`, `FMG-SEG-FIX` (asthma toggle), plus `FMG-I18N` / `FMG-I18N-JS` on the two new pages.
