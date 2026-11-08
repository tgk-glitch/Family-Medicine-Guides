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
| `tools/` | Python build scripts for leaflets, About and Patients pages, counselling wiring (not published) |

Every upload to `main` triggers a build (Actions tab), and the site updates about a minute later.

To preview on your own computer (optional): install Node.js 24 LTS, then in this folder run `npm install` once and `npm start`, and open http://localhost:8080

## Security

- **No server, database, login or plugins.** The site is static files served by GitHub Pages.
- **Locked build steps.** `.github/workflows/deploy.yml` uses only GitHub's official actions, each pinned to an exact commit fingerprint. Packages install from `package-lock.json` with `npm ci --ignore-scripts` (exact versions, no install-time scripts).
- **Dependabot** (`.github/dependabot.yml`) checks monthly and opens a pull request when an action or package has an update. Nothing changes until it's approved (merged).
- **Only outside resource on the pages:** Google Fonts.
