/* CSIR UGC NET Quiz Portal - service worker
 *
 * Purpose: let the site be installed as an app and keep opening when the network is slow or gone.
 *
 *  - The page itself (index.html) is network-first, so every time you publish a new index.html the
 *    installed app picks it up on its next online launch. Offline, the last copy is served instead.
 *  - Files from the same folder (icons, manifest) and the few CDNs the page uses (Tailwind, Font Awesome,
 *    Google Fonts, Firebase JS) are served from the cache and refreshed in the background.
 *  - Firebase API calls (sign-in, Firestore reads/writes) are never touched: they always go to the network,
 *    and the app's own localStorage fallback handles being offline.
 *
 * To force every device to drop its old cache after a big change, bump CACHE_VERSION.
 */
const CACHE_VERSION = 'v1';
const CACHE_PREFIX = 'csir-quiz-';
const CACHE_NAME = CACHE_PREFIX + CACHE_VERSION;

// Same-folder files to have ready right after install (relative to this file, so it works under /csir-net-quiz/)
const PRECACHE = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png',
                  './icon-maskable-512.png', './apple-touch-icon.png'];

// Cross-origin hosts that may be cached (host -> allowed path prefix)
const CDN_HOSTS = {
  'cdn.tailwindcss.com': '/',
  'cdnjs.cloudflare.com': '/ajax/libs/font-awesome/',
  'fonts.googleapis.com': '/',
  'fonts.gstatic.com': '/',
  'www.gstatic.com': '/firebasejs/'
};

function isCacheableCdn(url) {
  const prefix = CDN_HOSTS[url.hostname];
  return url.protocol === 'https:' && prefix !== undefined && url.pathname.startsWith(prefix);
}

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    // Not cache.addAll(): one missing optional file must not stop the whole worker from installing.
    await Promise.all(PRECACHE.map(async (path) => {
      try {
        const res = await fetch(new Request(path, { cache: 'reload' }));
        if (res.ok) await cache.put(path, res);
      } catch (_) { /* offline during install: runtime caching will fill in later */ }
    }));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(names.filter((n) => n.startsWith(CACHE_PREFIX) && n !== CACHE_NAME).map((n) => caches.delete(n)));
    await self.clients.claim();
  })());
});

const PAGE_TIMEOUT_MS = 5000;   // on a very slow connection, show the saved copy instead of a blank wait

// Fetch from the network and store a copy in the cache without delaying the response that goes to the page.
// event.waitUntil is called right away (while respondWith is still pending), so the cache write can finish even if
// the page was already answered from the cache.
function fetchAndStore(event, cache, request, key, fetchInit) {
  const job = fetch(request, fetchInit).then((res) => {
    const copy = res && (res.ok || res.type === 'opaque') ? res.clone() : null;   // clone before the page reads it
    const stored = copy ? cache.put(key, copy).catch(() => {}) : Promise.resolve();   // e.g. 206 partials cannot be cached
    return { res, stored };
  });
  event.waitUntil(job.then((r) => r.stored, () => {}));
  return job.then((r) => r.res);
}

async function networkFirstPage(event) {
  const cache = await caches.open(CACHE_NAME);
  // single-page app: every in-scope navigation shows the same page, so keep one canonical copy
  const network = fetchAndStore(event, cache, event.request, './index.html', { cache: 'no-cache' });
  const saved = (await cache.match('./index.html')) || (await cache.match('./'));
  if (!saved) return network.catch(() => Response.error());
  try {
    const timeout = new Promise((_, reject) => setTimeout(() => reject(new Error('slow')), PAGE_TIMEOUT_MS));
    return await Promise.race([network, timeout]);
  } catch (_) {
    return saved;   // offline, or too slow: the late response (if any) still refreshes the cache in the background
  }
}

async function staleWhileRevalidate(event) {
  const request = event.request;
  const cache = await caches.open(CACHE_NAME);
  const cached = await cache.match(request);
  const network = fetchAndStore(event, cache, request, request);
  if (cached) { network.catch(() => {}); return cached; }
  try { return await network; } catch (_) { return Response.error(); }
}

self.addEventListener('fetch', (event) => {
  const request = event.request;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);

  if (request.mode === 'navigate' && url.origin === self.location.origin) {
    event.respondWith(networkFirstPage(event));
    return;
  }
  if (url.origin === self.location.origin || isCacheableCdn(url)) {
    event.respondWith(staleWhileRevalidate(event));
  }
  // anything else (Firebase/Firestore/identity APIs, other sites): untouched, straight to the network
});

// The page sends the list of CDN files it actually loaded, so that everything it needs is cached after the very
// first visit (the worker only controls the page from the second load on, so it cannot see those requests itself).
self.addEventListener('message', (event) => {
  const data = event.data;
  if (!data || data.type !== 'CACHE_URLS' || !Array.isArray(data.urls)) return;
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await Promise.all(data.urls.slice(0, 200).map(async (href) => {
      try {
        const url = new URL(href);
        if (!isCacheableCdn(url) || await cache.match(href)) return;
        let res;
        try { res = await fetch(href, { mode: 'cors' }); }          // CORS copy can serve both module imports and plain tags
        catch (_) { res = await fetch(href, { mode: 'no-cors' }); }
        if (res && (res.ok || res.type === 'opaque')) await cache.put(href, res);
      } catch (_) { /* skip files that cannot be fetched right now */ }
    }));
  })());
});
