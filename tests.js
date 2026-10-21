const fs=require('fs'),assert=require('assert'),path=require('path');
const root=__dirname;
const read=x=>fs.readFileSync(path.join(root,x),'utf8');
for(const app of ['electric','finance','drywall']){
 const s=read('apps/'+app+'/index.html');
 assert(s.includes('href="../../index.html"'),'missing hub back: '+app);
 assert(!s.includes('cdn.tailwindcss.com'),'external Tailwind: '+app);
 assert(s.includes('../../assets/workspace.js'),'missing workspace: '+app);
}
const registry=read('apps-config.js');for(const app of ['electric','finance','drywall'])assert(registry.includes("id:'"+app+"'"));
const sw=read('sw.js');for(const app of ['electric','finance','drywall'])assert(sw.includes('./apps/'+app+'/index.html'));
for(const x of ['workspace.js','workspace-ui.js','offline-ui.css','finance-plus.js','drywall-plus.js','electric-plus.js'])assert(fs.existsSync(path.join(root,'assets',x)));
assert(read('assets/workspace.js').includes("indexedDB.open"));
console.log('PASS: navigation, registry, offline assets, workspace references');

for (const app of ['finance','drywall']) { const html=read('apps/'+app+'/index.html'); assert(html.includes('desktop-responsive.css'), 'desktop stylesheet missing: '+app); assert(html.includes('pro-desktop pro-'+app),'desktop layout missing: '+app); assert(!html.includes('fonts.googleapis.com'), 'remote font dependency: '+app); }
assert(read('sw.js').includes('./assets/desktop-responsive.css'),'PWA desktop css not cached');
console.log('PASS: desktop layouts and offline stylesheet');

for(const app of ['measure','tile','paint','plumbing','heat','floor','materials','electric','finance','drywall']){
 const html=read('apps/'+app+'/index.html');
 assert(html.includes('pro-ux.css'), 'UX stylesheet missing: '+app);
 assert(html.includes('pro-premium.js'), 'shared settings missing: '+app);
 assert(html.includes('../../index.html'), 'back link missing: '+app);
}
assert(read('index.html').includes('pro-ux.css'));
assert(read('sw.js').includes('./assets/pro-ux.css'));
assert(!read('assets/pro-elegance.js').includes('document.body.appendChild(toggle)'), 'duplicate animation toggle');
console.log('PASS: all 10 apps, mobile UX styles, unified settings and offline cache');

for(const app of ['garage','estimate','car-care','home-budget','converter','checklist']){
 const html=read('apps/'+app+'/index.html');
 assert(html.includes('href="../../index.html"'),'missing hub back: '+app);
 assert(html.includes('manifest.webmanifest'),'missing PWA manifest: '+app);
 assert(fs.existsSync(path.join(root,'apps',app,'index.html')),'missing app: '+app);
 assert(sw.includes('./apps/'+app+'/index.html'),'missing offline precache: '+app);
 assert(registry.includes(app),'missing registry entry: '+app);
}
assert((registry.match(/path['\"]?:/g)||[]).length>=16,'expected 16 app entries');
console.log('PASS: six new modules, registry and offline cache');
