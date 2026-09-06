const DURATION_CACHE_KEY='oa-level16-vimeo-durations';
const curriculumGroups=[
{title:"What will you learn in this course?",lessons:[1,2,3,4,5,6,7]},
{title:"Module 2: Market Analysis",lessons:[8,9,10,11]},
{title:"The Greeks and Short Strangle",lessons:[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]},
{title:"Module 3: Constructing the Short Strangle",lessons:[27,28,29,30,31,32]},
{title:"Module 4: Managing the Short Strangle",lessons:[33,34,35]},
{title:"Module 5: Risk Management",lessons:[36,37,38,39,40]},
{title:"Module 7: Real-Life Case Studies",lessons:[41]},
{title:"Module 8: Adjustments in Short Strangle",lessons:[42]},
{title:"Module 9: Advanced Strategies",lessons:[43,44,45,46,47,48,49,50]},
{title:"Module 10: Psychological Aspects",lessons:[51,52,53,54,55]},
{title:"Professional Trading Framework",lessons:[56,57,58,59]},
{title:"Course Summary",lessons:[60]}
];
function fmtDuration(seconds){seconds=Math.max(0,Math.round(Number(seconds)||0));if(!seconds)return '';const h=Math.floor(seconds/3600),m=Math.floor((seconds%3600)/60),s=seconds%60;return h?`${h}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`:`${m}:${String(s).padStart(2,'0')}`;}
function readCache(){try{return JSON.parse(localStorage.getItem(DURATION_CACHE_KEY)||'{}')}catch(e){return {}}}
function saveCache(c){try{localStorage.setItem(DURATION_CACHE_KEY,JSON.stringify(c))}catch(e){}}
function lessonDuration(l,cache){if(l.type!=='video'||!l.vimeoId)return l.duration||'Reading';return cache[String(l.vimeoId)]||l.duration||'';}
async function loadSourceData(){try{const r=await fetch('course-data-source.b64');if(!r.ok)throw 0;const b64=(await r.text()).trim();const bytes=Uint8Array.from(atob(b64),c=>c.charCodeAt(0));const stream=new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'));return JSON.parse(await new Response(stream).text());}catch(e){const r=await fetch('course-data.json');if(!r.ok)throw new Error('course data');return r.json();}}
function renderCurriculum(d,cache){const c=document.querySelector('.curriculum-list');if(!c)return;c.innerHTML=curriculumGroups.map(g=>{const a=g.lessons.map(n=>d.lessons[n-1]).filter(Boolean);return `<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(g.title)}</h3>${a.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">${l.type==='video'?'▶':'▤'}</span><div><strong>${esc(l.title)}</strong><small>${esc(lessonDuration(l,cache))}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`}).join('');}
async function hydrateVimeoDurations(d,cache){await Promise.allSettled(d.lessons.filter(l=>l.type==='video'&&l.vimeoId).map(async l=>{const id=String(l.vimeoId);if(cache[id])return;try{const r=await fetch(`https://vimeo.com/api/oembed.json?url=${encodeURIComponent('https://vimeo.com/'+id)}`);if(!r.ok)return;const j=await r.json();const duration=fmtDuration(j.duration);if(duration)cache[id]=duration;}catch(e){}}));saveCache(cache);renderCurriculum(d,cache);}
async function initLevel16(){const d=await loadSourceData(),cache=readCache();renderCurriculum(d,cache);const n=document.querySelector('.curriculum-title strong');if(n)n.textContent=`${d.lessons.length} Lessons`;const w=document.querySelector('.course-image-wrap'),b=document.querySelector('.course-preview-play'),p=d.course.previewVimeoId;if(w&&b&&p)b.onclick=()=>{w.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${p}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Short Strangle course preview"></iframe>`};hydrateVimeoDurations(d,cache);}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
initLevel16().catch(console.error);