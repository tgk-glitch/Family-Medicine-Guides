/* Family Medicine Guides — private app service worker.
 * Generated at build time by app/plugin.js. Do not edit _site/sw.js by hand.
 *
 * What it does
 *  - Saves every page, PDF, leaflet card, font and icon on first visit, so the
 *    whole app works offline.
 *  - Pages: tries the network first (fresh content), falls back to the saved copy.
 *  - Everything else: uses the saved copy first (fast), the network if missing.
 *
 * What it never does
 *  - Never touches requests to other sites.
 *  - Never saves sign-in redirects, error pages or anything that is not a plain
 *    200 response from this site.
 *  - Stores no personal or patient data (the app collects none).
 */
const VERSION = "__VERSION__";
const CACHE = "fmg-app-" + VERSION;
const PRECACHE = __PRECACHE__;
const OFFLINE = "/offline.html";
const NAV_TIMEOUT_MS = 4000;

// One cache key per file, whatever URL form the host serves
// ("/", "/index.html", "/counselling", "/counselling.html" → same key).
function keyFor(input) {
  const u = new URL(typeof input === "string" ? input : input.url, self.location.origin);
  let p = u.pathname;
  if (p.endsWith("/")) p += "index.html";
  else if (!/\.[a-z0-9]+$/i.test(p.split("/").pop())) p += ".html";
  return new URL(p, self.location.origin).href;
}

// A response is only kept if it is a real, same-site, successful file.
function keepable(res) {
  return res && res.ok && res.status === 200 && res.type === "basic" &&
    new URL(res.url).origin === self.location.origin;
}

// Hosts that drop ".html" answer with a redirect; store a clean copy instead.
async function clean(res) {
  if (!res.redirected) return res;
  const body = await res.blob();
  return new Response(body, { status: res.status, statusText: res.statusText, headers: res.headers });
}

self.addEventListener("install", (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    for (const url of PRECACHE) {
      const res = await fetch(url, { cache: "reload", credentials: "same-origin" });
      if (!keepable(res)) throw new Error("Not saved: " + url + " (" + res.status + ")");
      await cache.put(keyFor(url), await clean(res));
    }
  })());
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    for (const name of await caches.keys()) {
      if (name.startsWith("fmg-app-") && name !== CACHE) await caches.delete(name);
    }
    await self.clients.claim();
  })());
});

self.addEventListener("message", (event) => {
  if (event.data === "skipWaiting") self.skipWaiting();
  if (event.data === "version" && event.source) event.source.postMessage({ version: VERSION });
});

function timeout(ms) {
  return new Promise((_, reject) => setTimeout(() => reject(new Error("timeout")), ms));
}

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return; // other sites: leave alone
  if (url.pathname === "/sw.js") return;

  if (req.mode === "navigate") {
    event.respondWith((async () => {
      try {
        const res = await Promise.race([fetch(req), timeout(NAV_TIMEOUT_MS)]);
        if (keepable(res)) {
          const copy = res.clone();
          caches.open(CACHE).then(async (c) => c.put(keyFor(req), await clean(copy)));
        }
        return res; // includes sign-in redirects, so the login page still works
      } catch (_) {
        const cached = await caches.match(keyFor(req), { ignoreSearch: true });
        return cached || (await caches.match(keyFor(OFFLINE))) || Response.error();
      }
    })());
    return;
  }

  event.respondWith((async () => {
    const cached = await caches.match(keyFor(req), { ignoreSearch: true });
    if (cached) return cached;
    const res = await fetch(req);
    if (keepable(res)) {
      const copy = res.clone();
      caches.open(CACHE).then(async (c) => c.put(keyFor(req), await clean(copy)));
    }
    return res;
  })());
});
