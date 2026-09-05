const DURATION_CACHE_KEY='oa-level12-vimeo-durations';
const curriculumGroups=[
 {title:'Butterfly Foundations',lessons:[1,2,3,4,5]},
 {title:'Different Types of Butterfly Spread',lessons:[6,7,8,9]},
 {title:'Vega & Implied Volatility',lessons:[10,11,12,13]},
 {title:'Theta & Time Decay',lessons:[14,15,16,17]},
 {title:'Delta & the Butterfly Strategy',lessons:[18,19,20,21,22]},
 {title:'Butterfly Scenarios',lessons:[23,24,25,26,27,28,29,30,31,32,33,34,35,36]},
 {title:'Trade Execution',lessons:[37]},
 {title:'Position Management & Adjustments',lessons:[38,39,40,41,42,43,44,45,46,47,48,49]},
 {title:'Course Summary',lessons:[50]}
];
function readDurationCache(){try{return JSON.parse(localStorage.getItem(DURATION_CACHE_KEY)||'{}')}catch(e){return {}}}
function saveDurationCache(c){try{localStorage.setItem(DURATION_CACHE_KEY,JSON.stringify(c))}catch(e){}}
function fmtDuration(seconds){const s=Math.max(0,Math.round(Number(seconds)||0));if(!s)return '';const h=Math.floor(s/3600),m=Math.floor((s%3600)/60),r=s%60;return h?`${h}:${String(m).padStart(2,'0')}:${String(r).padStart(2,'0')}`:`${m}:${String(r).padStart(2,'0')}`}
function applyGroups(d){const byNo=new Map(d.lessons.map(l=>[l.number,l]));curriculumGroups.forEach(g=>g.lessons.forEach(n=>{const l=byNo.get(n);if(l)l.section=g.title}))}
function render(d){const c=document.querySelector('.curriculum-list');if(c){const byNo=new Map(d.lessons.map(l=>[l.number,l]));c.innerHTML=curriculumGroups.map(g=>{const a=g.lessons.map(n=>byNo.get(n)).filter(Boolean);return `<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(g.title)}</h3>${a.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">${l.type==='video'?'▶':'▤'}</span><div><strong>${esc(l.title)}</strong><small>${esc(l.duration||'Reading')}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`}).join('')}const n=document.querySelector('.curriculum-title strong');if(n)n.textContent=`${d.lessons.length} Lessons`}
async function hydrateVimeoDurations(d){const cache=readDurationCache();await Promise.allSettled(d.lessons.filter(l=>l.type==='video'&&l.vimeoId).map(async l=>{const id=String(l.vimeoId);if(cache[id]){l.duration=cache[id];return}const r=await fetch(`https://vimeo.com/api/oembed.json?url=${encodeURIComponent(`https://vimeo.com/${id}`)}`);if(!r.ok)return;const j=await r.json(),duration=fmtDuration(j.duration);if(duration){cache[id]=duration;l.duration=duration}}));saveDurationCache(cache);render(d)}
async function initLevel12(){const r=await fetch('course-data.json');if(!r.ok)throw new Error('course data');const d=await r.json();applyGroups(d);const cache=readDurationCache();d.lessons.forEach(l=>{if(l.vimeoId&&cache[String(l.vimeoId)])l.duration=cache[String(l.vimeoId)]});render(d);const w=document.querySelector('.course-image-wrap'),b=document.querySelector('.course-preview-play'),p=d.course.previewVimeoId;if(w&&b&&p)b.onclick=()=>{w.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${p}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>`};hydrateVimeoDurations(d)}
function esc(s){return String(s??'').replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[c]))}
initLevel12().catch(console.error);