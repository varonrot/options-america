const state={data:null,current:1,completed:new Set(JSON.parse(localStorage.getItem('oa-level1-completed')||'[]')),player:null};
const $=s=>document.querySelector(s);
const list=$('#syllabusList'),frame=$('#vimeoFrame'),videoCard=$('#videoCard'),nonVideoCard=$('#nonVideoCard');

async function init(){
  const res=await fetch('../course-data.json');
  state.data=await res.json();
  const params=new URLSearchParams(location.search);
  const requested=Number(params.get('lesson'))||1;
  renderSyllabus();
  loadLesson(Math.min(Math.max(requested,1),state.data.lessons.length),false);
  bind();
}

function bind(){
  $('#prevBtn').addEventListener('click',()=>go(-1));
  $('#nextBtn').addEventListener('click',()=>go(1));
  $('#markComplete').addEventListener('click',()=>{completeCurrent();go(1)});
}

function renderSyllabus(){
  const grouped=new Map();
  state.data.lessons.forEach(l=>{if(!grouped.has(l.section))grouped.set(l.section,[]);grouped.get(l.section).push(l)});
  list.innerHTML=[...grouped.entries()].map(([section,items])=>`<section class="syllabus-section"><h3>${esc(section)}</h3>${items.map(l=>`<div class="syllabus-item ${state.completed.has(l.number)?'done':''}" data-lesson="${l.number}"><span class="lesson-number">${l.number}</span><span class="lesson-check">${state.completed.has(l.number)?'✓':''}</span><div class="lesson-copy"><strong>${esc(l.title)}</strong><small>${esc(l.duration)}</small></div><span class="lesson-symbol">${l.type==='video'?'▶':l.type==='quiz'?'?':'▤'}</span></div>`).join('')}</section>`).join('');
  list.querySelectorAll('.syllabus-item').forEach(el=>el.addEventListener('click',()=>loadLesson(Number(el.dataset.lesson),true)));
  updateProgress();
}

function loadLesson(n,push=true){
  state.current=n;
  const lesson=state.data.lessons[n-1];
  if(!lesson)return;
  $('#lessonTitle').textContent=lesson.title;
  $('#lessonType').textContent=lesson.type==='video'?'Video lesson':lesson.type==='quiz'?'Quiz':'Text lesson';
  $('#lessonMeta').textContent=`Lesson ${lesson.number} of ${state.data.lessons.length} · ${lesson.duration}`;
  $('#aboutTitle').textContent=lesson.title;
  $('#factLesson').textContent=`${lesson.number} of ${state.data.lessons.length}`;
  $('#factDuration').textContent=lesson.duration;
  $('#factSection').textContent=lesson.section;
  const next=state.data.lessons[n];
  $('#factNext').textContent=next?next.title:'Course complete';
  $('#prevBtn').disabled=n===1;
  $('#nextBtn').disabled=n===state.data.lessons.length;

  list.querySelectorAll('.syllabus-item').forEach(el=>el.classList.toggle('active',Number(el.dataset.lesson)===n));
  const active=list.querySelector(`[data-lesson="${n}"]`); if(active)active.scrollIntoView({block:'nearest'});

  if(lesson.type==='video' && lesson.vimeoId){
    nonVideoCard.hidden=true;videoCard.hidden=false;
    loadVimeo(lesson);
  }else{
    videoCard.hidden=true;nonVideoCard.hidden=false;
    $('#nonVideoTitle').textContent=lesson.title;
    $('#nonVideoText').textContent=lesson.type==='quiz'?'This quiz will be connected after the question data is extracted from WordPress.':'This text lesson will be migrated from the original course content.';
  }
  if(push){history.replaceState(null,'',`?lesson=${n}`)}
}

function loadVimeo(lesson){
  if(state.player){try{state.player.unload()}catch(e){}}
  frame.src=`https://player.vimeo.com/video/${lesson.vimeoId}?title=0&byline=0&portrait=0&autopause=0`;
  state.player=new Vimeo.Player(frame);
  state.player.on('ended',()=>{
    completeCurrent();
    if($('#autoNext').checked && state.current<state.data.lessons.length){setTimeout(()=>go(1),700)}
  });
}

function completeCurrent(){
  state.completed.add(state.current);
  localStorage.setItem('oa-level1-completed',JSON.stringify([...state.completed]));
  const item=list.querySelector(`[data-lesson="${state.current}"]`);
  if(item){item.classList.add('done');item.querySelector('.lesson-check').textContent='✓'}
  updateProgress();
}

function updateProgress(){
  const total=state.data?state.data.lessons.length:74;
  const done=[...state.completed].filter(n=>n>=1&&n<=total).length;
  const pct=Math.round(done/total*100);
  $('#progressText').textContent=`${done} / ${total}`;
  $('#percentText').textContent=`${pct}% complete`;
  $('#progressBar').style.width=`${pct}%`;
}

function go(delta){
  let target=state.current+delta;
  if(target<1||target>state.data.lessons.length)return;
  loadLesson(target,true);
}

function esc(s){return String(s??'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]))}

init().catch(err=>{console.error(err);$('#lessonTitle').textContent='Could not load course data';});