/* PRO 7.5: visual enhancement only; no calculation or storage logic changed */
(()=>{'use strict';
const KEY='pro75-motion-disabled';const root=document.documentElement;
const reduced=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
let disabled=false;try{disabled=localStorage.getItem(KEY)==='1'}catch(e){}
if(disabled)root.classList.add('e75-motion-off');
const active=()=>!disabled&&!reduced;
function init(){
 const progress=document.createElement('div');progress.className='e75-progress';progress.setAttribute('aria-hidden','true');document.body.appendChild(progress);
 let frame=0;function updateProgress(){if(frame)return;frame=requestAnimationFrame(()=>{frame=0;const total=document.documentElement.scrollHeight-innerHeight;progress.style.transform='scaleX('+(total>0?Math.max(0,Math.min(1,scrollY/total)):0)+')'})}
 addEventListener('scroll',updateProgress,{passive:true});addEventListener('resize',updateProgress,{passive:true});updateProgress();
 // Theme and motion settings are handled by the unified PRO settings panel.
 const selector='.app-card,.hero,.glass,.card,.panel,.result,.summary,.pro6-dialog,.pro7-dialog,.mc-dialog';
 const observer=('IntersectionObserver' in window)?new IntersectionObserver(entries=>{for(const e of entries)if(e.isIntersecting){e.target.classList.add('e75-visible');observer.unobserve(e.target)}},{threshold:.05,rootMargin:'0px 0px 45px 0px'}):null;
 let count=0;function enhance(node){if(node.nodeType!==1)return;const list=[];if(node.matches&&node.matches(selector))list.push(node);if(node.querySelectorAll)list.push(...node.querySelectorAll(selector));for(const el of list){if(el.classList.contains('e75-reveal'))continue;el.classList.add('e75-reveal');el.style.setProperty('--e75-delay',(count++%6)*35+'ms');if(active()&&observer)observer.observe(el);else el.classList.add('e75-visible')}const dialogs=[];if(node.matches&&node.matches('[role="dialog"],dialog'))dialogs.push(node);if(node.querySelectorAll)dialogs.push(...node.querySelectorAll('[role="dialog"],dialog'));if(active())dialogs.forEach(d=>{if(!d.dataset.e75Dialog){d.dataset.e75Dialog='1';d.classList.add('e75-modal-open')}})}
 enhance(document.body);const mo=new MutationObserver(records=>{for(const rec of records)for(const n of rec.addedNodes)if(n.nodeType===1)enhance(n)});mo.observe(document.body,{subtree:true,childList:true});
 // Avoid watching or rewriting numerical outputs; pre-existing result animations remain in charge.
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
})();