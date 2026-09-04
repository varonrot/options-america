const state={data:null,quizzes:{},current:1,completed:new Set(JSON.parse(localStorage.getItem('oa-level1-completed')||'[]')),player:null,quiz:null};
const $=s=>document.querySelector(s);
const list=$('#syllabusList'),frame=$('#vimeoFrame'),videoCard=$('#videoCard'),quizCard=$('#quizCard'),nonVideoCard=$('#nonVideoCard');

async function init(){
  const [courseRes,quizRes]=await Promise.all([fetch('../course-data.json'),fetch('../quiz-data.json')]);
  state.data=await courseRes.json();
  state.quizzes=await quizRes.json();
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
  stopPlayer();
  $('#lessonTitle').textContent=lesson.title;
  $('#lessonType').textContent=lesson.type==='video'?'Video lesson':lesson.type==='quiz'?'Knowledge check':'Text lesson';
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

  videoCard.hidden=true;quizCard.hidden=true;nonVideoCard.hidden=true;
  $('#markComplete').hidden=false;
  $('#autoNext').closest('label').hidden=false;

  if(lesson.type==='video' && lesson.vimeoId){
    videoCard.hidden=false;
    $('#aboutText').textContent='Watch the lesson, then continue to the next item. When the video ends, the lesson is marked complete automatically.';
    loadVimeo(lesson);
  }else if(lesson.type==='quiz'){
    quizCard.hidden=false;
    $('#markComplete').hidden=true;
    $('#autoNext').closest('label').hidden=true;
    $('#aboutText').textContent='Complete the knowledge check and reach the passing score to mark this lesson complete.';
    startQuiz(n);
  }else{
    nonVideoCard.hidden=false;
    $('#nonVideoTitle').textContent=lesson.title;
    $('#nonVideoText').textContent='This text lesson will be migrated from the original course content.';
    $('#aboutText').textContent='Read the lesson and mark it complete when you are ready to continue.';
  }
  if(push){history.replaceState(null,'',`?lesson=${n}`)}
}

function loadVimeo(lesson){
  frame.src=`https://player.vimeo.com/video/${lesson.vimeoId}?title=0&byline=0&portrait=0&autopause=0`;
  state.player=new Vimeo.Player(frame);
  state.player.on('ended',()=>{
    completeCurrent();
    if($('#autoNext').checked && state.current<state.data.lessons.length){setTimeout(()=>go(1),700)}
  });
}

function stopPlayer(){
  if(state.player){try{state.player.unload()}catch(e){} state.player=null;}
  frame.src='';
}

function startQuiz(lessonNumber){
  const quiz=state.quizzes[String(lessonNumber)];
  if(!quiz){
    $('#quizBody').innerHTML='<div class="quiz-empty">Quiz data is not available yet.</div>';
    return;
  }
  state.quiz={data:quiz,index:0,score:0,answers:[],locked:false};
  renderQuizQuestion();
}

function renderQuizQuestion(){
  const qz=state.quiz;
  const q=qz.data.questions[qz.index];
  const total=qz.data.questions.length;
  $('#quizProgress').textContent=`Question ${qz.index+1} of ${total}`;
  $('#quizScore').textContent=`Score: ${qz.score}`;
  $('#quizProgressBar').style.width=`${Math.round(qz.index/total*100)}%`;
  $('#quizBody').innerHTML=`
    <div class="quiz-question-wrap">
      <div class="quiz-question-number">QUESTION ${qz.index+1}</div>
      <h2>${esc(q.question)}</h2>
      <div class="quiz-answers">
        ${q.answers.map((a,i)=>`<button class="quiz-answer" data-answer="${i}"><span>${String.fromCharCode(65+i)}</span>${esc(a)}</button>`).join('')}
      </div>
      <div id="quizFeedback" class="quiz-feedback" hidden></div>
      <div class="quiz-actions"><button id="quizCheck" class="primary-btn" disabled>Check answer</button></div>
    </div>`;
  let selected=null;
  qz.locked=false;
  document.querySelectorAll('.quiz-answer').forEach(btn=>btn.addEventListener('click',()=>{
    if(qz.locked)return;
    selected=Number(btn.dataset.answer);
    document.querySelectorAll('.quiz-answer').forEach(b=>b.classList.remove('selected'));
    btn.classList.add('selected');
    $('#quizCheck').disabled=false;
  }));
  $('#quizCheck').addEventListener('click',()=>checkQuizAnswer(selected));
}

function checkQuizAnswer(selected){
  const qz=state.quiz;
  if(qz.locked||selected===null)return;
  qz.locked=true;
  const q=qz.data.questions[qz.index];
  const correct=selected===q.correct;
  if(correct)qz.score++;
  qz.answers.push({questionId:q.id,selected,correct});
  document.querySelectorAll('.quiz-answer').forEach(btn=>{
    const i=Number(btn.dataset.answer);
    btn.disabled=true;
    if(i===q.correct)btn.classList.add('correct');
    if(i===selected&&!correct)btn.classList.add('wrong');
  });
  const feedback=$('#quizFeedback');
  feedback.hidden=false;
  feedback.className=`quiz-feedback ${correct?'good':'bad'}`;
  feedback.textContent=correct?'Correct. Nice work.':`Not quite. Correct answer: ${q.answers[q.correct]}`;
  const check=$('#quizCheck');
  check.textContent=qz.index===qz.data.questions.length-1?'See results':'Next question →';
  check.disabled=false;
  check.onclick=()=>{
    if(qz.index<qz.data.questions.length-1){qz.index++;renderQuizQuestion();}
    else renderQuizResults();
  };
}

function renderQuizResults(){
  const qz=state.quiz;
  const total=qz.data.questions.length;
  const pct=Math.round(qz.score/total*100);
  const passed=pct>=qz.data.passingGrade;
  $('#quizProgress').textContent='Quiz complete';
  $('#quizScore').textContent=`${qz.score} / ${total}`;
  $('#quizProgressBar').style.width='100%';
  if(passed)completeCurrent();
  $('#quizBody').innerHTML=`
    <div class="quiz-results ${passed?'passed':'failed'}">
      <div class="quiz-result-ring">${pct}%</div>
      <span class="quiz-result-label">${passed?'PASSED':'TRY AGAIN'}</span>
      <h2>${passed?'Great work — you passed the quiz.':'You are close. Review and try again.'}</h2>
      <p>You answered <strong>${qz.score} of ${total}</strong> questions correctly. Passing score: ${qz.data.passingGrade}%.</p>
      <div class="quiz-result-actions">
        <button id="quizRetry" class="ghost-btn">Retry quiz</button>
        ${passed&&state.current<state.data.lessons.length?'<button id="quizContinue" class="primary-btn">Continue course →</button>':''}
      </div>
    </div>`;
  $('#quizRetry').addEventListener('click',()=>startQuiz(state.current));
  const cont=$('#quizContinue');if(cont)cont.addEventListener('click',()=>go(1));
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
  const target=state.current+delta;
  if(target<1||target>state.data.lessons.length)return;
  loadLesson(target,true);
}

function esc(s){return String(s??'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]))}

init().catch(err=>{console.error(err);$('#lessonTitle').textContent='Could not load course data';});