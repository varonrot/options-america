const COMPLETED_KEY='oa-level10-completed';
const $=selector=>document.querySelector(selector);
const state={data:null,current:1,completed:new Set(JSON.parse(localStorage.getItem(COMPLETED_KEY)||'[]'))};
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function groupLessons(lessons){const groups=[];lessons.forEach((lesson,index)=>{let group=groups.find(item=>item.name===lesson.section);if(!group){group={name:lesson.section,lessons:[]};groups.push(group)}group.lessons.push({...lesson,index:index+1})});return groups}
function renderSyllabus(){
  $('#syllabusList').innerHTML=groupLessons(state.data.lessons).map(group=>`<section class="syllabus-section"><h3>${esc(group.name)}</h3>${group.lessons.map(lesson=>`<div class="syllabus-item ${lesson.index===state.current?'active':''} ${state.completed.has(lesson.index)?'done':''}" data-lesson="${lesson.index}"><span class="lesson-number">${lesson.index}</span><span class="lesson-check">${state.completed.has(lesson.index)?'✓':''}</span><div class="lesson-copy"><strong>${esc(lesson.title)}</strong><small>${esc(lesson.duration||'—')}</small></div><span class="lesson-symbol">${lesson.vimeoId?'▶':'◷'}</span></div>`).join('')}</section>`).join('');
  $('#syllabusList').querySelectorAll('[data-lesson]').forEach(item=>item.onclick=()=>loadLesson(Number(item.dataset.lesson),true));updateProgress();
}
function loadLesson(number,updateUrl=false){
  if(number<1||number>state.data.lessons.length)return;state.current=number;const lesson=state.data.lessons[number-1],next=state.data.lessons[number];
  $('#lessonTitle').textContent=lesson.title;$('#lessonType').textContent=lesson.vimeoId?'Video lesson':'Video pending';$('#lessonMeta').textContent=`Lesson ${number} of ${state.data.lessons.length} · ${lesson.duration||'—'}`;
  $('#aboutTitle').textContent=lesson.title;$('#aboutText').textContent=lesson.description||state.data.course.availabilityMessage;
  $('#nonVideoCard').innerHTML=`<div class="non-video-icon">◷</div><h2>Video being edited</h2><p>${esc(lesson.description||state.data.course.availabilityMessage)}</p>`;
  $('#factLesson').textContent=`${number} of ${state.data.lessons.length}`;$('#factDuration').textContent=lesson.duration||'—';$('#factSection').textContent=lesson.section||'—';$('#factNext').textContent=next?next.title:'Course complete';
  $('#prevBtn').disabled=number===1;$('#nextBtn').disabled=number===state.data.lessons.length;renderSyllabus();if(updateUrl)history.replaceState(null,'',`?lesson=${number}`);
}
function updateProgress(){const total=state.data?.lessons.length||45,done=[...state.completed].filter(number=>number>=1&&number<=total).length,percent=total?Math.round(done/total*100):0;$('#progressText').textContent=`${done} / ${total}`;$('#percentText').textContent=`${percent}% complete`;$('#progressBar').style.width=`${percent}%`}
function completeCurrent(){state.completed.add(state.current);localStorage.setItem(COMPLETED_KEY,JSON.stringify([...state.completed]));renderSyllabus();if($('#autoNext').checked&&state.current<state.data.lessons.length)loadLesson(state.current+1,true)}
async function init(){const response=await fetch('../course-data.json');if(!response.ok)throw new Error('course data');state.data=await response.json();const requested=Number(new URLSearchParams(location.search).get('lesson'))||1;$('#prevBtn').onclick=()=>loadLesson(state.current-1,true);$('#nextBtn').onclick=()=>loadLesson(state.current+1,true);$('#markComplete').onclick=completeCurrent;loadLesson(Math.min(Math.max(requested,1),state.data.lessons.length))}
init().catch(error=>{console.error(error);$('#lessonTitle').textContent='Could not load course data'});
