const curriculumGroups=[
{title:"Module 1: Event-Driven Foundations",lessons:[1,2,3,4,5]},
{title:"Module 2: Identifying and Researching Catalysts",lessons:[6,7,8,9,10]},
{title:"Module 3: Volatility and Market Response",lessons:[11,12,13,14,15]},
{title:"Module 4: Event-Driven Options Strategies",lessons:[16,17,18,19,20]},
{title:"Module 5: Earnings and Corporate Events",lessons:[21,22,23,24,25]},
{title:"Module 6: Mergers, Regulatory, and Macro Events",lessons:[26,27,28,29,30]},
{title:"Module 7: Trade Construction and Execution",lessons:[31,32,33,34,35]},
{title:"Module 8: Risk Management and Adjustments",lessons:[36,37,38,39,40]},
{title:"Module 9: Case Studies and Trading Plan",lessons:[41,42,43,44,45]}
];
async function loadSourceData(){const r=await fetch('course-data.json');if(!r.ok)throw new Error('course data');return r.json();}
function renderCurriculum(d){const c=document.querySelector('.curriculum-list');if(!c)return;c.innerHTML=curriculumGroups.map(g=>{const a=g.lessons.map(n=>d.lessons[n-1]).filter(Boolean);return `<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(g.title)}</h3>${a.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">↻</span><div><strong>${esc(l.title)}</strong><small>${esc(l.duration)}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`}).join('');}
async function initLevel49(){const d=await loadSourceData();renderCurriculum(d);const n=document.querySelector('.curriculum-title strong');if(n)n.textContent=`${d.lessons.length} Lessons`;const w=document.querySelector('.course-image-wrap'),b=document.querySelector('.course-preview-play'),p=d.course.previewVimeoId;if(w&&b&&p)b.onclick=()=>{w.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${p}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Event-Driven Catalyst course preview"></iframe>`};}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
initLevel49().catch(console.error);
