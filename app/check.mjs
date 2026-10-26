// Checks the private app build in _site/ before it is published.
// Usage: npm run build:app && npm run app:check   (exits with an error if anything fails)
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const ROOT = "_site";
const problems = [];
const warnings = [];
// Pages that exist only on the main-PC copy (known, tracked in the project notes).
const KNOWN_MISSING = new Set(["ramadan.html"]);
const fail = (msg) => problems.push(msg);
const sha = (s) => "'sha256-" + crypto.createHash("sha256").update(s, "utf8").digest("base64") + "'";

const pages = fs.readdirSync(ROOT).filter((f) => f.endsWith(".html") && f !== "offline.html");
if (pages.length < 10) fail(`only ${pages.length} pages built`);

for (const page of pages) {
  const html = fs.readFileSync(path.join(ROOT, page), "utf8");
  const head = html.slice(0, html.search(/<\/head>/i));
  const csp = (head.match(/<meta http-equiv="Content-Security-Policy" content="([^"]+)"/) || [])[1];
  if (!csp) { fail(`${page}: no Content-Security-Policy`); continue; }
  const firstScript = head.search(/<script/i);
  if (firstScript !== -1 && firstScript < head.indexOf("Content-Security-Policy")) fail(`${page}: a script comes before the policy`);
  for (const m of html.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/gi))
    if (!csp.includes(sha(m[1]))) fail(`${page}: inline script not allowed by policy`);
  if (!/<meta name="robots" content="noindex/.test(head)) fail(`${page}: missing noindex`);
  if (!head.includes('rel="manifest"')) fail(`${page}: missing manifest link`);
  if (!head.includes("/app/app.js")) fail(`${page}: missing app.js`);
  // Nothing may be loaded from another site (plain links to other sites are fine).
  for (const m of html.matchAll(/<(script|link|img|iframe|source|video|audio|embed)\b[^>]*\b(src|href)=["'](https?:)?\/\/[^"']+/gi)) {
    const tag = m[0];
    if (/^<link/i.test(tag) && !/rel=["']?(stylesheet|preload|preconnect|icon|manifest|modulepreload)/i.test(tag)) continue;
    fail(`${page}: loads an outside resource → ${tag.slice(0, 120)}`);
  }
  // Internal links and files must exist.
  for (const m of html.matchAll(/\b(?:href|src)=["']([^"'#?]+)(?:[?#][^"']*)?["']/gi)) {
    const ref = m[1];
    if (/^(https?:|mailto:|tel:|data:|javascript:|\/\/)/i.test(ref) || !ref) continue;
    const target = path.join(ROOT, ref.startsWith("/") ? ref : ref);
    if (!fs.existsSync(target)) (KNOWN_MISSING.has(ref) ? warnings : problems).push(`${page}: broken link → ${ref}`);
  }
}

// Manifest and icons
const manifest = JSON.parse(fs.readFileSync(path.join(ROOT, "manifest.webmanifest"), "utf8"));
for (const icon of manifest.icons) if (!fs.existsSync(path.join(ROOT, icon.src))) fail(`manifest icon missing: ${icon.src}`);
if (!manifest.icons.some((i) => i.purpose === "maskable")) fail("no maskable icon");

// Service worker precache list must match real files
const sw = fs.readFileSync(path.join(ROOT, "sw.js"), "utf8");
const list = JSON.parse(sw.match(/const PRECACHE = (\[[\s\S]*?\]);/)[1]);
for (const f of list) if (!fs.existsSync(path.join(ROOT, f))) fail(`precache file missing: ${f}`);
for (const p of pages) if (!list.includes("/" + p)) fail(`page not saved for offline: ${p}`);
if (!list.includes("/offline.html")) fail("offline page not in precache");

// Host files
for (const f of ["_headers", "robots.txt"]) if (!fs.existsSync(path.join(ROOT, f))) fail(`missing ${f}`);
const headers = fs.readFileSync(path.join(ROOT, "_headers"), "utf8");
for (const h of ["frame-ancestors 'none'", "Strict-Transport-Security", "X-Robots-Tag", "Permissions-Policy", "nosniff"])
  if (!headers.includes(h)) fail(`_headers lacks ${h}`);
if (!/Disallow: \/\s*$/m.test(fs.readFileSync(path.join(ROOT, "robots.txt"), "utf8"))) fail("robots.txt does not block crawlers");

if (warnings.length) console.warn(`! ${[...new Set(warnings)].length} known warning(s):\n  - ` + [...new Set(warnings)].join("\n  - "));
if (problems.length) {
  console.error(`✗ ${problems.length} problem(s):\n  - ` + problems.join("\n  - "));
  process.exit(1);
}
console.log(`✓ app build OK: ${pages.length} pages, ${list.length} files saved for offline, policy and headers in place`);
