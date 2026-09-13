function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function groupLessons(lessons){const groups=[];lessons.forEach((lesson,index)=>{let group=groups.find(item=>item.name===lesson.section);if(!group){group={name:lesson.section,lessons:[]};groups.push(group)}group.lessons.push({...lesson,index:index+1})});return groups}
async function initLevel10(){
  const response=await fetch('course-data.json');if(!response.ok)throw new Error('course data');const data=await response.json();
  const curriculum=document.querySelector('.curriculum-list');
  if(curriculum)curriculum.innerHTML=groupLessons(data.lessons).map(group=>`<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(group.name)}</h3>${group.lessons.map(lesson=>`<a class="curriculum-item" href="player/?lesson=${lesson.index}"><span class="lesson-index">${lesson.index}</span><span class="lesson-icon">${lesson.vimeoId?'▶':'◷'}</span><div><strong>${esc(lesson.title)}</strong><small>${esc(lesson.duration||'—')}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`).join('');
  const count=document.querySelector('.curriculum-title strong');if(count)count.textContent=`${data.lessons.length} Lessons`;
  const wrap=document.querySelector('.course-image-wrap'),button=document.querySelector('.course-preview-play'),preview=data.course.previewVimeoId;
  if(wrap&&button&&preview)button.onclick=()=>{wrap.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${preview}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Bear Put Spread course preview"></iframe>`};
}
initLevel10().catch(console.error);
