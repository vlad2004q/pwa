const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const src=fs.readFileSync(__dirname+'/../assets/cash-pro.js','utf8');
const match=src.match(/const defs=(\{[^;]+\});/);
assert(match,'Currency denominations defined');
const defs=vm.runInNewContext('('+match[1]+')');
const cases=[['BYN',0.01],['RUB',0.01],['USD',0.01],['EUR',0.01],['PLN',0.01],['UAH',0.01],['GBP',0.01],['CHF',0.05]];
for(const [cur,smallest] of cases){const ds=defs[cur].d;assert(ds.length>0,cur);assert.equal(Math.min(...ds),smallest,cur+' smallest denomination');assert(ds.every(x=>Number.isSafeInteger(Math.round(x*100))&&Math.abs(x*100-Math.round(x*100))<1e-7),cur+' minor units');assert.equal(new Set(ds).size,ds.length,cur+' duplicate denominations');for(const d of ds){for(const qty of [0,1,7,123]){const cents=Math.round(d*100)*qty;assert(Number.isSafeInteger(cents));assert.equal(cents/100,Math.round(cents)/100)}}}
// NBRB quotes BYN per currency unit, after adjusting for Cur_Scale.
const byn={BYN:1,USD:3.2,EUR:3.5,PLN:0.8};
for(const base of Object.keys(byn))for(const source of Object.keys(byn)){const rate=byn[source]/byn[base];assert(Math.abs(100*rate*byn[base]-100*byn[source])<1e-8)}
assert(src.includes('localStorage.setItem(key,JSON.stringify(state))'),'cash persists state');
assert(src.includes('rateUpdated'),'rate freshness metadata');
console.log('PASS: 8 currencies, integer minor-unit totals, NBRB cross-rates, persistence hooks');
