const DURATION_CACHE_KEY='oa-poor-mans-covered-call-vimeo-durations';
const curriculumGroups=[
  {title:'Module 1: Introduction to Poor Man’s Covered Call',lessons:Array.from({length:14},(_,i)=>i+1)},
  {title:'Module 2: Market Conditions and Suitability',lessons:Array.from({length:9},(_,i)=>i+15)},
  {title:'Module 3: The Greeks in PMCC',lessons:Array.from({length:8},(_,i)=>i+24)},
  {title:'Module 4: Setting Up Poor Man’s Covered Call',lessons:Array.from({length:7},(_,i)=>i+32)},
  {title:'Module 5: Execution and Position Management',lessons:Array.from({length:4},(_,i)=>i+39)},
  {title:'Module 6: Combining PMCC with Other Strategies',lessons:Array.from({length:9},(_,i)=>i+43)},
  {title:'Module 7: Strategy Adjustments',lessons:[52]},
  {title:'Module 8: Options Trading Management',lessons:Array.from({length:10},(_,i)=>i+53)},
  {title:'Module 9: Course Summary',lessons:[63]}
];
function fmtDuration(seconds){seconds=Math.max(0,Math.round(Number(seconds)||0));if(!seconds)return '';const h=Math.floor(seconds/3600),m=Math.floor((seconds%3600)/60),s=seconds%60;return h?`${h}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`:`${m}:${String(s).padStart(2,'0')}`;}
function readCache(){try{return JSON.parse(localStorage.getItem(DURATION_CACHE_KEY)||'{}')}catch(e){return {}}}function saveCache(c){try{localStorage.setItem(DURATION_CACHE_KEY,JSON.stringify(c))}catch(e){}}
function lessonDuration(l,cache){if(!l.vimeoId)return l.duration||'Reading';return cache[String(l.vimeoId)]||l.duration||'';}
async function loadSourceData(){const r=await fetch('course-data.json');if(!r.ok)throw new Error('course data');return r.json();}
function renderCurriculum(d,cache){const c=document.querySelector('.curriculum-list');if(!c)return;c.innerHTML=curriculumGroups.map(g=>{const a=g.lessons.map(n=>d.lessons[n-1]).filter(Boolean);return `<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(g.title)}</h3>${a.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">${l.vimeoId?'▶':'◷'}</span><div><strong>${esc(l.title)}</strong><small data-duration-id="${l.vimeoId||''}">${esc(lessonDuration(l,cache))}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`}).join('');}
async function hydrateVimeoDurations(d,cache){await Promise.allSettled(d.lessons.filter(l=>l.vimeoId).map(async l=>{const id=String(l.vimeoId);if(cache[id])return;try{const r=await fetch(`https://vimeo.com/api/oembed.json?url=${encodeURIComponent('https://vimeo.com/'+id)}`);if(!r.ok)return;const j=await r.json();const duration=fmtDuration(j.duration);if(duration)cache[id]=duration;}catch(e){}}));saveCache(cache);renderCurriculum(d,cache);}
async function initCourse(){const d=await loadSourceData(),cache=readCache();renderCurriculum(d,cache);const n=document.querySelector('.curriculum-title strong');if(n)n.textContent=`${d.lessons.length} Lessons`;const w=document.querySelector('.course-image-wrap'),b=document.querySelector('.course-preview-play'),p=d.course.previewVimeoId;if(w&&b&&p)b.onclick=()=>{w.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${p}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Poor Man's Covered Call course preview"></iframe>`};hydrateVimeoDurations(d,cache);}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}initCourse().catch(console.error);
