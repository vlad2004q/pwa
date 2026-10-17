(()=>{'use strict';
const fmt=(n,d=1)=>Number(n).toLocaleString('ru-RU',{maximumFractionDigits:d});
const ceil=Math.ceil;
function plan(v){
 const L=v.length*1000,W=v.width*1000,pl=v.plankL,pw=v.plankW,g=v.gap;
 const run=(v.direction==='length'?L:W)-2*g, span=(v.direction==='length'?W:L)-2*g;
 const rows=ceil(span/pw), lastWidth=span-(rows-1)*pw, fullArea=v.length*v.width;
 const parts=[], pool=[];let boards=0,usedOffcuts=0,shortCuts=0;
 const minPiece=Math.min(v.mincut,pl);
 function cut(need){let idx=-1,best=Infinity;for(let i=0;i<pool.length;i++)if(pool[i]>=need-0.05&&pool[i]<best){best=pool[i];idx=i}
  if(idx>=0){const source=pool.splice(idx,1)[0],rest=source-need;if(rest>=minPiece)pool.push(rest);usedOffcuts++;return true}
  boards++;const rest=pl-need;if(rest>=minPiece)pool.push(rest);else if(rest>1)shortCuts++;return false;
 }
 for(let row=0;row<rows;row++){
  const target=v.pattern==='half'?(row%2)*pl/2:v.pattern==='random'?([0,0.37,0.62,0.25,0.51][row%5]*pl):(row%3)*pl/3;
  let x=0,step=0;const rowWidth=Math.min(pw,span-row*pw);
  while(x<run-0.1&&step<2000){
   const desired=step===0?(target>0?pl-target:pl):pl;
   const len=Math.min(desired,run-x);const reused=cut(len);
   parts.push({x,y:row*pw,w:len,h:rowWidth,reused,cut:len<pl-0.1});x+=len;step++;
  }
 }
 const boughtArea=boards*pl*pw/1e6,coverage=pl*pw/1e6;
 const nominalNeed=fullArea*(1+v.reserve/100),minPacks=ceil(nominalNeed/v.pack);
 const cutPacks=ceil(boughtArea/v.pack),packs=Math.max(minPacks,cutPacks);
 const boardCountInPacks=Math.max(1,Math.floor(v.pack/coverage+1e-7));
 const packsByCount=ceil(boards/boardCountInPacks),actualPacks=Math.max(packs,packsByCount);
 const perimeter=Math.max(0,2*(v.length+v.width)-v.baseboard);
 const metrics=[['Площадь комнаты',fmt(fullArea)+' м²'],['Упаковок к покупке',actualPacks+' шт'],['Планок по раскрою',boards+' шт'],['Рядов укладки',rows+''],['Обрезков использовано',usedOffcuts+' шт'],['Плинтус',fmt(perimeter)+' м']];
 const items=[['Напольное покрытие',actualPacks,'уп.',v.packPrice],['Подложка',nominalNeed,'м²',v.underlay],['Плинтус',perimeter,'м',v.baseboardPrice]];
 const sx=640/(v.direction==='length'?L:W),sy=350/(v.direction==='length'?W:L);
 const w=run*sx,h=span*sy, gapX=g*sx,gapY=g*sy;
 const maxPieces=2500;
 const rectangles=parts.slice(0,maxPieces).map((p,i)=>`<rect x="${(gapX+p.x*sx).toFixed(2)}" y="${(gapY+p.y*sy).toFixed(2)}" width="${Math.max(.15,p.w*sx).toFixed(2)}" height="${Math.max(.15,p.h*sy).toFixed(2)}" fill="${p.reused?'#4d9b93':p.cut?'#b78047':i%2?'#9c7952':'#bb9264'}" stroke="#182d38" stroke-width="1.3"/>`).join('');
 const svg=`<svg class="floor-plan" viewBox="0 0 700 424" role="img" aria-label="Схема укладки: ${rows} рядов, ${boards} планок, направление ${v.direction==='length'?'вдоль длины':'вдоль ширины'}"><defs><linearGradient id="floorwood" x1="0" x2="1"><stop stop-color="#cda678"/><stop offset="1" stop-color="#78583c"/></linearGradient></defs><rect x="16" y="16" width="668" height="386" rx="14" fill="#071521" stroke="#355269"/><g transform="translate(30 28)"><rect width="640" height="350" fill="#14293c" stroke="#8ba1b4" stroke-width="2"/>${rectangles}<rect x="${gapX.toFixed(2)}" y="${gapY.toFixed(2)}" width="${w.toFixed(2)}" height="${h.toFixed(2)}" fill="none" stroke="#e7c895" stroke-dasharray="5 4" stroke-width="1.5"/></g><text x="350" y="399" text-anchor="middle" fill="#c4d4e2" font-size="15">${fmt(v.length)} × ${fmt(v.width)} м · зазор ${fmt(g,0)} мм</text></svg>`;
 const note=`Раскладка по реальным размерам планок (${fmt(pl,0)} × ${fmt(pw,0)} мм), ${rows} рядов, направление: ${v.direction==='length'?'вдоль длины':'вдоль ширины'}. Коричневые планки — целые, янтарные — подрезанные, зелёные — использованные обрезки. Планок по модели: ${boards}; использовано обрезков: ${usedOffcuts}. Упаковок: ${actualPacks} (с учётом запаса ${fmt(v.reserve)}% и количества планок). Остатки менее ${fmt(minPiece,0)} мм повторно не используются. Схема плановая, без дверных переходов, труб и сложных контуров; для реального монтажа проверьте требования производителя к минимальному смещению торцевых стыков и ширине последнего ряда (${fmt(lastWidth)} мм).`;
 return {area:fullArea,metrics,items,svg,note,boards,rows,parts,packs:actualPacks,usedOffcuts};
}
window.FloorPro={plan};
})();