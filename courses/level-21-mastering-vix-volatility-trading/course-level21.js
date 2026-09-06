const DURATION_CACHE_KEY='oa-level21-vimeo-durations';
const curriculumGroups=[
{title:"Module 1: VIX Foundations",lessons:[1,2,3,4,5]},
{title:"Module 2: VIX Options Mechanics",lessons:[6,7,8,9,10]},
{title:"Module 3: Volatility Analysis",lessons:[11,12,13,14,15]},
{title:"Module 4: VIX Trading Strategies",lessons:[16,17,18,19,20,21,22,23,24,25]},
{title:"Module 5: Timing and Market Events",lessons:[26,27,28,29,30]},
{title:"Module 6: Risk Management",lessons:[31,32,33,34,35]},
{title:"Module 7: VIX Case Studies",lessons:[36,37,38,39,40]},
{title:"Module 8: Portfolio Planning",lessons:[41,42,43,44,45]}
];
async function loadSourceData(){try{const r=await fetch('course-data-source.b64');if(!r.ok)throw 0;const b64=(await r.text()).trim();const bytes=Uint8Array.from(atob(b64),c=>c.charCodeAt(0));const stream=new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'));return JSON.parse(await new Response(stream).text());}catch(e){const r=await fetch('course-data.json');if(!r.ok)throw new Error('course data');return r.json();}}
function readCache(){try{return JSON.parse(localStorage.getItem(DURATION_CACHE_KEY)||'{}')}catch(e){return {}}}function saveCache(c){try{localStorage.setItem(DURATION_CACHE_KEY,JSON.stringify(c))}catch(e){}}
function fmtDuration(seconds){seconds=Math.max(0,Math.round(Number(seconds)||0));if(!seconds)return '';const h=Math.floor(seconds/3600),m=Math.floor((seconds%3600)/60),s=seconds%60;return h?`${h}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`:`${m}:${String(s).padStart(2,'0')}`;}
function duration(l,cache){return l.vimeoId?(cache[l.vimeoId]||l.duration):l.duration;}
function renderCurriculum(d,cache){const c=document.querySelector('.curriculum-list');if(!c)return;c.innerHTML=curriculumGroups.map(g=>{const a=g.lessons.map(n=>d.lessons[n-1]).filter(Boolean);return `<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(g.title)}</h3>${a.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">${l.vimeoId?'▶':'◷'}</span><div><strong>${esc(l.title)}</strong><small data-duration-id="${l.vimeoId||''}">${esc(duration(l,cache))}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`}).join('');}
async function hydrateDuration(d,cache){const l=d.lessons.find(x=>x.vimeoId);if(!l||cache[l.vimeoId])return;try{const r=await fetch(`https://vimeo.com/api/oembed.json?url=${encodeURIComponent('https://vimeo.com/'+l.vimeoId)}`);if(!r.ok)return;const j=await r.json(),value=fmtDuration(j.duration);if(value){cache[l.vimeoId]=value;saveCache(cache);document.querySelectorAll(`[data-duration-id="${l.vimeoId}"]`).forEach(e=>e.textContent=value)}}catch(e){}}
async function initLevel21(){const d=await loadSourceData(),cache=readCache();renderCurriculum(d,cache);const n=document.querySelector('.curriculum-title strong');if(n)n.textContent=`${d.lessons.length} Lessons`;const w=document.querySelector('.course-image-wrap'),b=document.querySelector('.course-preview-play'),p=d.course.previewVimeoId;if(w&&b&&p)b.onclick=()=>{w.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${p}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Mastering VIX Volatility course preview"></iframe>`};hydrateDuration(d,cache);}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
initLevel21().catch(console.error);
