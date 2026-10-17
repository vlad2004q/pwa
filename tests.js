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
