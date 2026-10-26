# Family Medicine Guides — private app

This repository (`fmg-app`, **private**) is the app version of Family Medicine Guides.
It is visible only to Dr. Albaraa Albawab (and anyone he adds later). The public website
(`tgk-glitch/family-medicine-guides`) stays as it is and is not affected.

## What the app adds to the website

| Feature | What it means for you |
| --- | --- |
| **Install as an app** | Own icon and window on iPhone, iPad, Android, Windows, macOS, Linux and ChromeOS. No app store needed for development |
| **Works offline** | All 14 pages, every leaflet PDF and card (about 6 MB) are saved on the device after the first visit |
| **Updates itself** | When a new version is published, a small "A new version is ready · Update" message appears |
| **Private preview badge** | Shows briefly at the bottom of the screen; stays visible when you are offline ("Offline · saved copy") |
| **Shortcuts** | Long-press (phone) or right-click (desktop) the icon: Search, Urgent care, Peds ER, Patients |

The content is the same as the public site. Pages are not changed; the app layer is added at build time.

## Protections

| Layer | Protection |
| --- | --- |
| Who can open it | **Cloudflare Access** in front of every page and file: sign-in with a one-time code sent to an allowed email. Nobody else gets anything, not even a PDF by guessing its link |
| On your computer (Option B) | The local server listens on `127.0.0.1` only, so other devices on the same Wi-Fi cannot reach it |
| Source code | Private repository; two-factor sign-in on GitHub and Cloudflare (to do — see the setup steps) |
| What the pages may load | **Content-Security-Policy** on every page: scripts only from the app itself, inline scripts allowed only by exact fingerprint, nothing from other sites, no plugins, cannot be embedded in another site |
| Browser headers | HTTPS forced (HSTS), no sniffing, no referrer sent when opening outside links, camera/microphone/location/payment and similar features switched off |
| Search engines and AI crawlers | `noindex` on every page and in the headers, `robots.txt` blocks all crawlers |
| Fonts | Self-hosted (no Google Fonts requests, so no visitor data leaves the app) |
| Offline storage | Saves only the app's own files. No accounts, forms, analytics or patient data — nothing personal is stored or sent |
| Build | Official GitHub actions pinned to exact commits, `npm ci --ignore-scripts`, read-only permissions, Dependabot updates. Every upload is checked (`npm run app:check`) |

## Option B — on your own computer

Needs Node.js 22 or newer (nodejs.org → LTS).

```
git clone https://github.com/tgk-glitch/fmg-app.git
cd fmg-app
npm ci --ignore-scripts
npm run app
```

Open **http://localhost:8080** in Chrome or Edge, then click the install icon in the address bar
(or menu → "Install Family Medicine Guides"). Press Ctrl+C in the terminal to stop the server.
Once installed and opened once, the app keeps working offline even when the server is stopped.

## Option A — on your phone, tablet and other computers

Published by Cloudflare Pages at `https://fmg-app.pages.dev`, locked by Cloudflare Access.
Setup steps are in the project notes ("Private app — setup steps").

| Device | How to install |
| --- | --- |
| iPhone / iPad | Safari → Share → **Add to Home Screen** |
| Android | Chrome → **Install app** (or menu → Add to Home screen) |
| Windows / Linux / ChromeOS | Chrome or Edge → install icon in the address bar |
| Mac | Chrome or Edge → install icon; or Safari → File → **Add to Dock** |

## Commands

| Command | What it does |
| --- | --- |
| `npm run build` | Builds the **public** website (unchanged, no app layer) |
| `npm run build:app` | Builds the **app** into `_site/` |
| `npm run app:check` | Checks the app build (security policy, offline list, links, headers) |
| `npm run app` | Builds the app and serves it on this computer |

## Keeping the app in step with the website

New pages and changes are made in the public repository as usual. To bring them into the app:

```
git remote add upstream https://github.com/tgk-glitch/family-medicine-guides.git   # once
git fetch upstream && git merge upstream/main
```

Files that belong only to the app: `app/`, `.github/workflows/check-app.yml`, `.node-version`,
and the few lines marked "Private app build" in `eleventy.config.js` and `package.json`.

## Files in `app/`

| File | Purpose |
| --- | --- |
| `plugin.js` | Adds the app layer to every page at build time (manifest, icons, fonts, security policy) |
| `sw-template.js` | The offline service worker (the build fills in the file list and version) |
| `fonts.mjs` | Copies the self-hosted fonts |
| `static/` | Manifest, icons, offline page, security headers, robots.txt, the small helper script |
| `serve.mjs` | Local server for Option B |
| `check.mjs` | Pre-publish checks |
| `dev/make-icons.py` | Redraws the app icon |
