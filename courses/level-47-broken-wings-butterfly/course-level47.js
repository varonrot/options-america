const curriculumGroups=[
{title:"Module 1: Strategy Foundations",lessons:[1,2,3,4,5]},
{title:"Module 2: Trade Construction",lessons:[6,7,8,9,10]},
{title:"Module 3: Market Conditions and Analysis",lessons:[11,12,13,14,15,16]},
{title:"Module 4: Adjustments and Advanced Combinations",lessons:[17,18,19,20,21,22,23,24,25]},
{title:"Module 5: Case Studies",lessons:[26,27,28,29,30]},
{title:"Module 6: Simulated Trades",lessons:[31,32,33,34,35]},
{title:"Module 7: Trading Plan and Long-Term Success",lessons:[36,37,38,39,40,41,42]}
];
async function loadSourceData(){try{const r=await fetch('course-data-source.b64');if(!r.ok)throw 0;const b64=(await r.text()).trim();const bytes=Uint8Array.from(atob(b64),c=>c.charCodeAt(0));const stream=new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'));return JSON.parse(await new Response(stream).text());}catch(e){const r=await fetch('course-data.json');if(!r.ok)throw new Error('course data');return r.json();}}
function renderCurriculum(d){const c=document.querySelector('.curriculum-list');if(!c)return;c.innerHTML=curriculumGroups.map(g=>{const a=g.lessons.map(n=>d.lessons[n-1]).filter(Boolean);return `<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(g.title)}</h3>${a.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">↻</span><div><strong>${esc(l.title)}</strong><small>${esc(l.duration)}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`}).join('');}
async function initLevel47(){const d=await loadSourceData();renderCurriculum(d);const n=document.querySelector('.curriculum-title strong');if(n)n.textContent=`${d.lessons.length} Lessons`;const w=document.querySelector('.course-image-wrap'),b=document.querySelector('.course-preview-play'),p=d.course.previewVimeoId;if(w&&b&&p)b.onclick=()=>{w.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${p}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Broken Wings Butterfly course preview"></iframe>`};}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
initLevel47().catch(console.error);
