const curriculumGroups=[
{title:"Module 1: Sector Rotation Foundations",lessons:[1,2,3,4,5]},
{title:"Module 2: Economic Cycles and Sector Leadership",lessons:[6,7,8,9,10]},
{title:"Module 3: Identifying Rotation Opportunities",lessons:[11,12,13,14,15]},
{title:"Module 4: Selecting Sector Instruments",lessons:[16,17,18,19,20]},
{title:"Module 5: Options Strategies for Sector Rotation",lessons:[21,22,23,24,25]},
{title:"Module 6: Trade Construction and Execution",lessons:[26,27,28,29,30]},
{title:"Module 7: Risk Management and Adjustments",lessons:[31,32,33,34,35]},
{title:"Module 8: Sector Case Studies",lessons:[36,37,38,39,40]},
{title:"Module 9: Simulation and Long-Term Planning",lessons:[41,42,43,44,45]}
];
async function loadSourceData(){try{const r=await fetch('course-data-source.b64');if(!r.ok)throw 0;const b64=(await r.text()).trim();const bytes=Uint8Array.from(atob(b64),c=>c.charCodeAt(0));const stream=new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'));return JSON.parse(await new Response(stream).text());}catch(e){const r=await fetch('course-data.json');if(!r.ok)throw new Error('course data');return r.json();}}
function renderCurriculum(d){const c=document.querySelector('.curriculum-list');if(!c)return;c.innerHTML=curriculumGroups.map(g=>{const a=g.lessons.map(n=>d.lessons[n-1]).filter(Boolean);return `<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(g.title)}</h3>${a.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">↻</span><div><strong>${esc(l.title)}</strong><small>${esc(l.duration)}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`}).join('');}
async function initLevel48(){const d=await loadSourceData();renderCurriculum(d);const n=document.querySelector('.curriculum-title strong');if(n)n.textContent=`${d.lessons.length} Lessons`;const w=document.querySelector('.course-image-wrap'),b=document.querySelector('.course-preview-play'),p=d.course.previewVimeoId;if(w&&b&&p)b.onclick=()=>{w.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${p}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Sector Rotation course preview"></iframe>`};}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
initLevel48().catch(console.error);
