async function initLevel6(){
  const res=await fetch('course-data.json');
  if(!res.ok) throw new Error(`Failed to load course data: ${res.status}`);
  const data=await res.json();
  const curriculum=document.querySelector('.curriculum-list');
  if(curriculum){
    const groups=new Map();
    data.lessons.forEach(l=>{if(!groups.has(l.section))groups.set(l.section,[]);groups.get(l.section).push(l)});
    curriculum.innerHTML=[...groups.entries()].map(([section,items])=>`<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(section)}</h3>${items.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">${l.type==='video'?'▶':'▤'}</span><div><strong>${esc(l.title)}</strong><small>${esc(l.duration)}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`).join('');
  }
  const count=document.querySelector('.curriculum-title strong'); if(count) count.textContent=`${data.lessons.length} Lessons`;
  const wrap=document.querySelector('.course-image-wrap'), btn=document.querySelector('.course-preview-play');
  const preview=data.course.previewVimeoId||data.lessons.find(l=>l.vimeoId)?.vimeoId;
  if(wrap&&btn&&preview) btn.addEventListener('click',()=>{wrap.classList.add('is-playing');wrap.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${preview}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Course preview"></iframe>`});
}
function esc(s){return String(s??'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]))}
initLevel6().catch(console.error);
