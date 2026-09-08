const state={data:null,current:1,completed:new Set(JSON.parse(localStorage.getItem('oa-level49-completed')||'[]'))};
const $=s=>document.querySelector(s),list=$('#syllabusList');
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
async function loadSourceData(){const r=await fetch('../course-data.json');if(!r.ok)throw new Error('course data');return r.json();}
async function init(){state.data=await loadSourceData();const q=new URLSearchParams(location.search),requested=Number(q.get('lesson'))||1;renderSyllabus();loadLesson(Math.min(Math.max(requested,1),state.data.lessons.length),false);$('#prevBtn').onclick=()=>go(-1);$('#nextBtn').onclick=()=>go(1);$('#markComplete').onclick=()=>{completeCurrent();if(state.current<state.data.lessons.length)go(1)};}
function renderSyllabus(){list.innerHTML=curriculumGroups.map(g=>{const items=g.lessons.map(n=>state.data.lessons[n-1]).filter(Boolean);return `<section class="syllabus-section"><h3>${esc(g.title)}</h3>${items.map(l=>`<div class="syllabus-item ${state.completed.has(l.number)?'done':''} ${state.current===l.number?'active':''}" data-lesson="${l.number}"><span class="lesson-number">${l.number}</span><span class="lesson-check">${state.completed.has(l.number)?'✓':''}</span><div class="lesson-copy"><strong>${esc(l.title)}</strong><small>${esc(l.duration)}</small></div><span class="lesson-symbol">↻</span></div>`).join('')}</section>`}).join('');list.querySelectorAll('.syllabus-item').forEach(el=>el.onclick=()=>loadLesson(Number(el.dataset.lesson),true));updateProgress();}
function primarySection(n){for(const g of curriculumGroups)if(g.lessons.includes(n))return g.title;return '';}
function loadLesson(n,push=true){state.current=n;const l=state.data.lessons[n-1];if(!l)return;const message=state.data.course.availabilityMessage;$('#lessonTitle').textContent=l.title;$('#lessonType').textContent='Video lesson';$('#lessonMeta').textContent=`Lesson ${l.number} of ${state.data.lessons.length} · ${l.duration}`;$('#availabilityMessage').textContent=message;$('#aboutTitle').textContent=l.title;$('#aboutText').textContent=message;$('#factLesson').textContent=`${l.number} of ${state.data.lessons.length}`;$('#factDuration').textContent=l.duration;$('#factSection').textContent=primarySection(l.number);$('#factNext').textContent=state.data.lessons[n]?.title||'Course complete';$('#prevBtn').disabled=n===1;$('#nextBtn').disabled=n===state.data.lessons.length;list.querySelectorAll('.syllabus-item').forEach(el=>el.classList.toggle('active',Number(el.dataset.lesson)===n));const active=list.querySelector(`[data-lesson="${n}"]`);if(active)active.scrollIntoView({block:'nearest'});if(push)history.replaceState(null,'',`?lesson=${n}`);}
function completeCurrent(){state.completed.add(state.current);localStorage.setItem('oa-level49-completed',JSON.stringify([...state.completed]));list.querySelectorAll(`[data-lesson="${state.current}"]`).forEach(item=>{item.classList.add('done');item.querySelector('.lesson-check').textContent='✓'});updateProgress();}
function updateProgress(){const total=state.data?.lessons.length||45,done=[...state.completed].filter(n=>n>=1&&n<=total).length,pct=total?Math.round(done/total*100):0;$('#progressText').textContent=`${done} / ${total}`;$('#percentText').textContent=`${pct}% complete`;$('#progressBar').style.width=`${pct}%`;}
function go(d){const t=state.current+d;if(t>=1&&t<=state.data.lessons.length)loadLesson(t,true);}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
init().catch(e=>{console.error(e);$('#lessonTitle').textContent='Could not load course data'});
