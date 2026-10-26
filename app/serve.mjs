// Local preview server for the private app (Option B: your own computer only).
// Usage:  npm run app          (builds, then serves on http://localhost:8080)
//         npm run app:serve    (serves the existing build)
//
// Security:
//  - Listens on 127.0.0.1 only, so other devices on the network cannot reach it.
//  - Sends the same security headers as the online app (from _site/_headers).
//  - Serves files only from inside _site/ (no path tricks like ../).
// "localhost" counts as a secure origin, so offline mode and "Install app" work.
import http from "node:http";
import fs from "node:fs";
import path from "node:path";

const ROOT = path.resolve("_site");
const PORT = Number(process.env.PORT || 8080);
const HOST = "127.0.0.1";

const TYPES = {
  ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8",
  ".css": "text/css; charset=utf-8", ".json": "application/json; charset=utf-8",
  ".webmanifest": "application/manifest+json; charset=utf-8", ".svg": "image/svg+xml",
  ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp",
  ".pdf": "application/pdf", ".woff2": "font/woff2", ".txt": "text/plain; charset=utf-8",
  ".ico": "image/x-icon",
};

// Minimal reader for the Cloudflare-style _headers file.
function loadHeaderRules() {
  const file = path.join(ROOT, "_headers");
  if (!fs.existsSync(file)) return [];
  const rules = [];
  let current = null;
  for (const raw of fs.readFileSync(file, "utf8").split(/\r?\n/)) {
    if (!raw.trim() || raw.trim().startsWith("#")) continue;
    if (!/^\s/.test(raw)) { current = { pattern: raw.trim(), headers: [] }; rules.push(current); continue; }
    const i = raw.indexOf(":");
    if (current && i > 0) current.headers.push([raw.slice(0, i).trim(), raw.slice(i + 1).trim()]);
  }
  return rules;
}
const RULES = loadHeaderRules();
const matches = (pattern, p) =>
  new RegExp("^" + pattern.replace(/[.+?^${}()|[\]\\]/g, "\\$&").replace(/\*/g, ".*") + "$").test(p);

http.createServer((req, res) => {
  if (req.method !== "GET" && req.method !== "HEAD") { res.writeHead(405).end(); return; }
  let urlPath;
  try { urlPath = decodeURIComponent(new URL(req.url, "http://x").pathname); }
  catch { res.writeHead(400).end(); return; }
  if (urlPath.endsWith("/")) urlPath += "index.html";
  let file = path.resolve(ROOT, "." + urlPath);
  if (!file.startsWith(ROOT + path.sep)) { res.writeHead(403).end(); return; }
  if (!fs.existsSync(file) && fs.existsSync(file + ".html")) file += ".html";
  if (["_headers", "_redirects"].includes(path.basename(file))) { res.writeHead(404).end(); return; }

  for (const rule of RULES) {
    if (matches(rule.pattern, urlPath)) for (const [k, v] of rule.headers) {
      if (k.toLowerCase() === "strict-transport-security") continue; // not for plain http://localhost
      res.setHeader(k, k.toLowerCase() === "content-security-policy" ? v.replace(/;\s*upgrade-insecure-requests/, "") : v);
    }
  }
  fs.stat(file, (err, st) => {
    if (err || !st.isFile()) {
      res.statusCode = 404;
      res.setHeader("Content-Type", "text/html; charset=utf-8");
      fs.createReadStream(path.join(ROOT, "offline.html")).pipe(res);
      return;
    }
    res.setHeader("Content-Type", TYPES[path.extname(file).toLowerCase()] || "application/octet-stream");
    res.setHeader("Content-Length", st.size);
    if (req.method === "HEAD") { res.end(); return; }
    fs.createReadStream(file).pipe(res);
  });
}).listen(PORT, HOST, () => {
  console.log(`Family Medicine Guides (private app) → http://localhost:${PORT}/`);
  console.log("Only this computer can open it. Press Ctrl+C to stop.");
});
