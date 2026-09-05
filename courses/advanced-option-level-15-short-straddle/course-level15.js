const curriculumGroups=[
  {title:'What will you learn in this course?',lessons:[1,2,3,4,5,6]},
  {title:'Module 2: Market Analysis',lessons:[7,8,9]},
  {title:'The Greeks and Short Straddle',lessons:[10,11,12,13,14,15,16,17,18,19,20,21]},
  {title:'Module 3: Constructing the Short Straddle',lessons:[22,23,24]},
  {title:'Module 4: Managing the Short Straddle',lessons:[25,26,27,28]},
  {title:'Module 5: Risk Management',lessons:[29,30,31,32,33,34]},
  {title:'Module 6: Real-Life Case Studies',lessons:[33]},
  {title:'Module 6.2: Short Straddle Adjustments',lessons:[34]},
  {title:'Module 7: Advanced Strategies',lessons:[35,36,37,38,39,40,41,42]},
  {title:'Module 8: Psychological Aspects',lessons:[43,44,45,46,47]},
  {title:'Module 9: Tools and Resources',lessons:[48,49,50,51,52]},
  {title:'Module 10: Course Summary and Next Steps',lessons:[53,54,55,56,57]}
];
async function initLevel15(){const r=await fetch('course-data.json');const d=await r.json(),c=document.querySelector('.curriculum-list');c.innerHTML=curriculumGroups.map(g=>{const a=g.lessons.map(n=>d.lessons[n-1]).filter(Boolean);return `<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(g.title)}</h3>${a.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">${l.type==='video'?'▶':'▤'}</span><div><strong>${esc(l.title)}</strong><small>${esc(l.duration||'Reading')}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`}).join('');document.querySelector('.curriculum-title strong').textContent=`${d.lessons.length} Lessons`;const w=document.querySelector('.course-image-wrap'),b=document.querySelector('.course-preview-play'),p=d.course.previewVimeoId;if(w&&b&&p)b.onclick=()=>w.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${p}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>`}function esc(s){return String(s??'').replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[c]))}initLevel15().catch(console.error);