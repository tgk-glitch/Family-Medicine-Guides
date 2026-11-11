# Family Medicine Guides

Bilingual (English / العربية) reference site for family physicians in Saudi Arabia, with a public-education section.
Created and medically supervised by **Dr. Albaraa Albawab**, Family Medicine.

Live site: https://tgk-glitch.github.io/Family-Medicine-Guides/

## How this repository works

| Folder / file | What it is |
| --- | --- |
| `src/` | The website's pages (`.html`), leaflets (`downloads/`) and search index |
| `src/_includes/nav.html` | The menu, used by every page. Edit once, and every page updates |
| `src/_includes/credit.html` | The footer credit block, used by every page |
| `eleventy.config.js` | Settings for Eleventy, the tool that assembles the site |
| `.github/workflows/deploy.yml` | Builds and publishes the site automatically after every upload |
| `tools/` | Python build scripts for leaflets, About and Patients pages, counselling wiring, and `check-style.mjs` (not published) |

Every merge to `main` triggers a build (Actions tab), and the site updates about a minute later.

## How changes are made

1. Changes are made on a **new branch**, never directly on `main`.
2. The site is built locally (`npm run build`) and the style check is run (`npm run check`). Both must pass.
3. A summary of every file changed is reviewed and approved by the medical editor.
4. Only then is the branch merged to `main`, which publishes it.

Clinical content (doses, thresholds, recommendations, red flags) is supplied or approved by the medical editor before it goes live.

## Writing rules

- **No em dashes** (the long dash) anywhere: pages, leaflets, scripts. Use a colon, comma, semicolon, full stop or parentheses. In page titles use `|`. In an empty table cell use `-`. En dashes are for ranges only (6–11 years).
- `npm run check` fails if an em dash, a hospital or employer name, or an email address appears in the pages.
- English and Arabic carry the same content. Shared parts (menu, footer credit, search index, directory) are edited once in their shared file.
- Topic counts and live/planned badges are read from `src/categories.html`; the homepage cards must match it.
- Printable leaflets carry no website address.

To preview on your own computer (optional): install Node.js 24 LTS, then in this folder run `npm install` once and `npm start`, and open http://localhost:8080

## Security

- **No server, database, login or plugins.** The site is static files served by GitHub Pages.
- **Locked build steps.** `.github/workflows/deploy.yml` uses only GitHub's official actions, each pinned to an exact commit fingerprint. Packages install from `package-lock.json` with `npm ci --ignore-scripts` (exact versions, no install-time scripts).
- **Dependabot** (`.github/dependabot.yml`) checks monthly and opens a pull request when an action or package has an update. Nothing changes until it's approved (merged).
- **Only outside resource on the pages:** Google Fonts.
