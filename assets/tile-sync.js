(()=>{'use strict';
const by=id=>document.getElementById(id), key='pro-material-tile-selection';
const number=id=>{const el=by(id);return el&&el.value.trim()!==''?Number(el.value):NaN};
const fmt=n=>Number(n).toLocaleString('ru-RU',{maximumFractionDigits:3});
let chosen=null, lastAutoRate=null;
const panel=by('materialSelection');if(!panel)return;
const status=document.createElement('div');status.id='tile-sync-status';status.setAttribute('aria-live','polite');status.style.cssText='margin-top:9px;line-height:1.55';panel.append(status);
const btn=document.createElement('button');btn.type='button';btn.textContent='↻ Обновить данные из Material Hub';btn.style.cssText='margin-top:9px';panel.append(btn);
const v3=()=>!!by('tv3-l');
function selected(){try{const item=JSON.parse(localStorage.getItem(key)||'null');if(!item?.id)return null;return window.PRO_MATERIALS?.read()?.find(p=>p.id===item.id)||item}catch{return null}}
function put(id,val){const el=by(id);if(!el||!Number.isFinite(val)||val<=0)return false;if(Math.abs(Number(el.value)-val)<1e-8)return false;el.value=String(Number(val.toFixed(5)));return true}
function category(p){const s=String(p?.category||'').toLowerCase();return /фуг|затир/.test(s)?'grout':/кле/.test(s)?'adhesive':'other'}
function syncGeometry(){if(!v3())return;const length=number('f_tileL'),width=number('f_tileW'),joint=number('f_joint');put('tv3-l',length);put('tv3-w',width);put('tv3-j',joint);
const area=number('f_length')*number('f_width')-number('f_openL')*number('f_openW');put('tv3-a',area);
// Depth is a separate installation parameter; never infer it from tile width or length.
by('tv3-l').dispatchEvent(new Event('input',{bubbles:false}));}
function applyMaterial(){chosen=selected();if(!chosen){status.textContent='Материал не выбран. Выберите клей или затирку в Material Hub BY и нажмите «Передать в Tile Master».';return}
const type=category(chosen),t=chosen.technical||{},rate=Number(chosen.rate)>0?Number(chosen.rate):Number(t.rateMax)>0?Number(t.rateMax):NaN;
const basis=t.rateBasis||'area';const unit=t.rateUnit||'кг/м²';const details=[];
if(type==='grout'){
const density=Number(chosen.density)>0?Number(chosen.density):Number(t.density)>0?Number(t.density):NaN;
if(put('tv3-rho',density))details.push('паспортная плотность '+fmt(density)+' кг/л');
else if(!Number.isFinite(density))details.push('плотность не указана — введите её из паспорта');
if(v3())by('tv3-rho').dispatchEvent(new Event('input'));
// A grout's area consumption is not transferable when tile geometry differs.
if(Number.isFinite(rate))details.push('норма каталога '+fmt(rate)+' '+unit+' (не подменяет геометрический расчёт)');
}else if(type==='adhesive'){
if(Number.isFinite(rate)&&unit==='кг/м²'&&basis!=='per_mm'&&chosen.rateStatus!=='minimum'){
const field=by('f_adhesive');if(field){field.value=String(rate);field.dispatchEvent(new Event('input'));lastAutoRate=rate;details.push('расход клея '+fmt(rate)+' кг/м² передан в смету')}
}else if(basis==='per_mm')details.push('норма на 1 мм — требуется указать толщину слоя, расход не подставлен');
else details.push('подтверждённой нормы расхода нет — значение оставлено для ручного ввода');
}else details.push('материал не относится к клею или затирке');
status.textContent='Выбран: '+(chosen.brand||'')+' '+chosen.name+'. '+details.join('; ')+'. Проверьте данные по паспорту.';
}
function syncGroutEstimate(){if(!v3())return;const l=number('tv3-l'),w=number('tv3-w'),j=number('tv3-j'),d=number('tv3-d'),rho=number('tv3-rho');const area=number('tv3-a');
const output=by('tile-grout-sync');if(!output)return;
if([l,w,j,d,rho,area].some(x=>!Number.isFinite(x)||x<=0)||j>=Math.min(l,w)){
output.textContent='Для автоматической сметы затирки укажите паспортную плотность и корректные размеры шва.';return}
const rate=(l+w)/(l*w)*j*d*rho;
const field=by('f_grout');if(field){field.value=String(Number(rate.toFixed(5)));field.dispatchEvent(new Event('input'))}
output.textContent='Расход по геометрии: '+fmt(rate)+' кг/м² · На площадь '+fmt(area)+' м²: '+fmt(rate*area)+' кг. Без запаса.';
}
function init(){if(!v3()){setTimeout(init,60);return}
const output=document.createElement('p');output.id='tile-grout-sync';output.style.cssText='font-weight:600;color:var(--accent,#f59e0b)';by('tv3-out').after(output);
for(const id of ['f_length','f_width','f_tileL','f_tileW','f_joint','f_openL','f_openW'])by(id)?.addEventListener('input',()=>{syncGeometry();syncGroutEstimate()});
for(const id of ['tv3-l','tv3-w','tv3-j','tv3-d','tv3-a','tv3-rho'])by(id)?.addEventListener('input',syncGroutEstimate);
btn.addEventListener('click',()=>{applyMaterial();syncGroutEstimate()});window.addEventListener('storage',e=>{if(e.key===key||e.key===window.PRO_MATERIALS?.key){applyMaterial();syncGroutEstimate()}});
syncGeometry();applyMaterial();syncGroutEstimate();}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
})();
