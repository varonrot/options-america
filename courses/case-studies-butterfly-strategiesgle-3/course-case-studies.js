const DURATION_CACHE_KEY='oa-case-studies-butterfly-vimeo-durations';
const curriculumGroups=[
{title:"Module 1: Butterfly Foundations",lessons:[1,2,3,4,5]},
{title:"Module 2: Rolling and Risk Adjustments",lessons:[6,7,8,9,10,11,12,13]},
{title:"Module 3: Position Management and Hedging",lessons:[14,15,16,17]},
{title:"Module 4: Market Scenarios",lessons:[18,19,20,21]},
{title:"Module 5: Practical Case Studies",lessons:[22,23,24,25,26,27,28,29,30,31]},
{title:"Module 6: Summary and Review",lessons:[32]}
];
function fmtDuration(seconds){seconds=Math.max(0,Math.round(Number(seconds)||0));if(!seconds)return '';const h=Math.floor(seconds/3600),m=Math.floor((seconds%3600)/60),s=seconds%60;return h?`${h}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`:`${m}:${String(s).padStart(2,'0')}`;}
function readCache(){try{return JSON.parse(localStorage.getItem(DURATION_CACHE_KEY)||'{}')}catch(e){return {}}}function saveCache(c){try{localStorage.setItem(DURATION_CACHE_KEY,JSON.stringify(c))}catch(e){}}
function lessonDuration(l,cache){return cache[String(l.vimeoId)]||l.duration||'';}
async function loadSourceData(){const r=await fetch('course-data.json');if(!r.ok)throw new Error('course data');return r.json();}
function renderCurriculum(d,cache){const c=document.querySelector('.curriculum-list');if(!c)return;c.innerHTML=curriculumGroups.map(g=>{const a=g.lessons.map(n=>d.lessons[n-1]).filter(Boolean);return `<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(g.title)}</h3>${a.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">▶</span><div><strong>${esc(l.title)}</strong><small data-duration-id="${l.vimeoId}">${esc(lessonDuration(l,cache))}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`}).join('');}
async function hydrateVimeoDurations(d,cache){await Promise.allSettled(d.lessons.map(async l=>{const id=String(l.vimeoId);if(cache[id])return;try{const r=await fetch(`https://vimeo.com/api/oembed.json?url=${encodeURIComponent('https://vimeo.com/'+id)}`);if(!r.ok)return;const j=await r.json();const duration=fmtDuration(j.duration);if(duration)cache[id]=duration;}catch(e){}}));saveCache(cache);renderCurriculum(d,cache);}
async function initCourse(){const d=await loadSourceData(),cache=readCache();renderCurriculum(d,cache);const n=document.querySelector('.curriculum-title strong');if(n)n.textContent=`${d.lessons.length} Lessons`;const w=document.querySelector('.course-image-wrap'),b=document.querySelector('.course-preview-play'),p=d.course.previewVimeoId;if(w&&b&&p)b.onclick=()=>{w.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${p}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Butterfly case studies course preview"></iframe>`};hydrateVimeoDurations(d,cache);}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}initCourse().catch(console.error);
