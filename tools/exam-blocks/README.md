# Exam-oriented blocks: switched off (12 Nov 2026)

The medical editor asked to remove the High-Yield, Trap and Exam Q boxes for now, so the site reads as a plain educational reference.

They are **switched off, not deleted**. One setting controls them all:

`src/_data/site.json` -> `"showExamBlocks": false`

While it is `false`, the build leaves these out of the published pages:

| Page | What is left out |
| --- | --- |
| `geriatrics.html` | 35 High-Yield boxes, 20 Trap boxes, 15 Exam Q boxes, the appendix "Exam bank, traps, the numbers" and its menu link, and three entries in the "How to read this guide" legend |
| `asthma.html` | 8 High-Yield boxes, 6 Trap boxes, 4 Exam Q boxes |
| `counselling.html` | 5 Traps boxes, 2 Board pearl boxes |
| `osce.html` | 1 "High-yield OSCE detail" note |

In the page files each block sits between `{% if site.showExamBlocks %}` and `{% endif %}`.

Left in place on purpose (they are clinical cautions or worked cases, not exam boxes): the warning boxes in Dermatology, Mental Health and the OSCE page, the "pearl" boxes in Pediatric ER Doses, the worked case in Counselling, and the four practice stations in Pediatric Asthma.

## To bring them back

1. Set `"showExamBlocks": true` in `src/_data/site.json`.
2. Add the entries listed under `removed` in `hidden-search-entries.json` back into `src/search-index.js`, and put back the snippet listed under `changed`.
3. `npm run build` and `npm run check`.
