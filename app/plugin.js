// Private app layer for Family Medicine Guides.
// Switched on only by FMG_APP=1 (npm run build:app / npm run app).
// The public website build (npm run build) is not affected.
//
// It adds:
//  - install-as-app files (manifest, icons, offline page)
//  - a service worker that saves the whole app for offline use
//  - self-hosted fonts (no Google Fonts requests)
//  - a strict Content-Security-Policy on every page (inline scripts allowed
//    only by exact fingerprint, nothing loaded from other sites)
//  - "do not index" markers and a private-preview badge
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { buildFonts } from "./fonts.mjs";

const sha = (s) => "'sha256-" + crypto.createHash("sha256").update(s, "utf8").digest("base64") + "'";

function cspFor(html) {
  const scriptHashes = new Set();
  // Inline <script> blocks (no src): allow by exact fingerprint.
  for (const m of html.matchAll(/<script(?![^>]*\bsrc=)([^>]*)>([\s\S]*?)<\/script>/gi)) {
    if (/type=["']?application\/(ld\+)?json/i.test(m[1])) continue;
    scriptHashes.add(sha(m[2]));
  }
  // Inline onclick="…" handlers: allowed by fingerprint too ('unsafe-hashes').
  let handlers = false;
  for (const m of html.matchAll(/\son[a-z]+="([^"]*)"/gi)) {
    const value = m[1].replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, "&");
    scriptHashes.add(sha(value));
    handlers = true;
  }
  const script = ["'self'", ...(handlers ? ["'unsafe-hashes'"] : []), ...scriptHashes].join(" ");
  return [
    "default-src 'self'",
    `script-src ${script}`,
    "style-src 'self' 'unsafe-inline'",
    "font-src 'self'",
    "img-src 'self' data: blob:",
    "connect-src 'self'",
    "media-src 'self'",
    "manifest-src 'self'",
    "worker-src 'self'",
    "frame-src 'self'",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
  ].join("; ");
}

const HEAD_ADDITIONS = `
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">
<meta name="referrer" content="no-referrer">
<meta name="theme-color" content="#123C38">
<meta name="application-name" content="FM Guides">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="FM Guides">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="manifest" href="/manifest.webmanifest" crossorigin="use-credentials">
<link rel="icon" href="/icons/icon.svg" type="image/svg+xml">
<link rel="icon" href="/icons/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">
<link rel="stylesheet" href="/fonts/fonts.css">
<link rel="stylesheet" href="/app/app.css">
<script src="/app/app.js" defer></script>`;

function transformPage(html) {
  // 1. Drop Google Fonts (replaced by self-hosted fonts).
  html = html
    .replace(/<link[^>]+rel=["']?preconnect["']?[^>]+fonts\.(googleapis|gstatic)\.com[^>]*>\s*/gi, "")
    .replace(/<link[^>]+href=["']https:\/\/fonts\.googleapis\.com[^>]*>\s*/gi, "");
  // 2. App additions, right after <meta charset>.
  const charset = /<meta\s+charset=["']?[^"'>]+["']?\s*\/?>/i;
  if (charset.test(html)) html = html.replace(charset, (m) => m + HEAD_ADDITIONS);
  else html = html.replace(/<head[^>]*>/i, (m) => m + '\n<meta charset="UTF-8">' + HEAD_ADDITIONS);
  // 3. Content-Security-Policy as the first thing after <meta charset>,
  //    computed from the final page so the fingerprints match exactly.
  const csp = `\n<meta http-equiv="Content-Security-Policy" content="${cspFor(html)}">`;
  html = html.replace(charset, (m) => m + csp);
  return html;
}

function walk(dir, base = dir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, base, out);
    else out.push("/" + path.relative(base, full).split(path.sep).join("/"));
  }
  return out;
}

export default function appPlugin(eleventyConfig) {
  eleventyConfig.addPassthroughCopy({ "app/static": "/" });

  eleventyConfig.addTransform("fmg-app", function (content) {
    const out = this.page.outputPath || "";
    return out.endsWith(".html") ? transformPage(content) : content;
  });

  eleventyConfig.on("eleventy.after", ({ dir }) => {
    const outDir = dir.output;
    buildFonts(outDir);

    // Precache list = every file in the build, except host/crawler files.
    const skip = new Set(["/sw.js", "/_headers", "/_redirects", "/robots.txt"]);
    const files = walk(outDir).filter((f) => !skip.has(f)).sort();
    const hash = crypto.createHash("sha256");
    for (const f of files) hash.update(f).update(fs.readFileSync(path.join(outDir, f)));
    const version = hash.digest("hex").slice(0, 12);

    const tpl = fs.readFileSync("app/sw-template.js", "utf8");
    fs.writeFileSync(
      path.join(outDir, "sw.js"),
      tpl.replace("__VERSION__", version).replace("__PRECACHE__", JSON.stringify(files, null, 0))
    );
    fs.writeFileSync(
      path.join(outDir, "app", "version.json"),
      JSON.stringify({ version, built: new Date().toISOString(), files: files.length, list: files }) + "\n"
    );
    const bytes = files.reduce((n, f) => n + fs.statSync(path.join(outDir, f)).size, 0);
    console.log(`[fmg-app] service worker ${version}: ${files.length} files, ${(bytes / 1048576).toFixed(1)} MB saved for offline`);
  });
}
