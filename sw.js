const CACHE="tb-v27",ASSETS=["/","/index.html","/logo.svg?v=11","/logo-white.svg?v=11","/chevrons.svg","/theme.css?v=1","/core.js?v=1"];
self.addEventListener("install",e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)).then(()=>self.skipWaiting())));
self.addEventListener("activate",e=>e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener("fetch",e=>{const u=new URL(e.request.url);if(u.pathname.endsWith("data.json")){e.respondWith(fetch(e.request).then(r=>{caches.open(CACHE).then(c=>c.put(e.request,r.clone()));return r}).catch(()=>caches.match(e.request)))}else{e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)))}});
