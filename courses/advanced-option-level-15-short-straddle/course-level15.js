const DURATION_CACHE_KEY='oa-level15-vimeo-durations';
const curriculumGroups=[
  {title:'What will you learn in this course?',lessons:[1,2,3,4,5,6]},
  {title:'Module 2: Market Analysis',lessons:[7,8,9]},
  {title:'The Greeks and Short Straddle',lessons:[10,11,12,13,14,15,16,17,18,19,20,21]},
  {title:'Module 3: Constructing the Short Straddle',lessons:[22,23,24]},
  {title:'Module 4: Managing the Short Straddle',lessons:[25,26,27,28]},
  {title:'Module 5: Risk Management',lessons:[29,30,31]},
  {title:'Module 6: Advanced Variations and Case Studies',lessons:[32,33,34,35,36,37,38,39,40,41,42,43,44]},
  {title:'Module 7: Psychological Aspects',lessons:[45,46,47,48,49]},
  {title:'Module 8: Professional Trading Framework',lessons:[50,51,52,53,54,55,56,57,58,59]}
];
function readDurations(){try{return JSON.parse(localStorage.getItem(DURATION_CACHE_KEY)||'{}')}catch(e){return {}}}
function saveDurations(d){try{localStorage.setItem(DURATION_CACHE_KEY,JSON.stringify(d))}catch(e){}}
function fmtDuration(seconds){const s=Math.max(0,Math.round(Number(seconds)||0));if(!s)return '';const h=Math.floor(s/3600),m=Math.floor((s%3600)/60),r=s%60;return h?`${h}:${String(m).padStart(2,'0')}:${String(r).padStart(2,'0')}`:`${m}:${String(r).padStart(2,'0')}`}
function lessonDuration(l,durations){if(l.type!=='video'||!l.vimeoId)return l.duration||'Reading';const raw=durations[String(l.vimeoId)];if(!raw)return l.duration||'';return typeof raw==='number'?fmtDuration(raw):String(raw)}
function renderCurriculum(d,durations){const c=document.querySelector('.curriculum-list');if(!c)return;c.innerHTML=curriculumGroups.map(g=>{const a=g.lessons.map(n=>d.lessons[n-1]).filter(Boolean);return `<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(g.title)}</h3>${a.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">${l.type==='video'?'▶':'▤'}</span><div><strong>${esc(l.title)}</strong><small>${esc(lessonDuration(l,durations))}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`}).join('')}
async function hydrateVimeoDurations(d,durations){await Promise.allSettled(d.lessons.filter(l=>l.type==='video'&&l.vimeoId).map(async l=>{const id=String(l.vimeoId);if(durations[id])return;const res=await fetch(`https://vimeo.com/api/oembed.json?url=${encodeURIComponent(`https://vimeo.com/${id}`)}`);if(!res.ok)return;const data=await res.json();if(data.duration)durations[id]=Number(data.duration)}));saveDurations(durations);renderCurriculum(d,durations)}
async function initLevel15(){const r=await fetch('course-data.json');if(!r.ok)throw new Error('course data');const d=await r.json(),durations=readDurations();renderCurriculum(d,durations);const count=document.querySelector('.curriculum-title strong');if(count)count.textContent=`${d.lessons.length} Lessons`;const w=document.querySelector('.course-image-wrap'),b=document.querySelector('.course-preview-play'),p=d.course.previewVimeoId;if(w&&b&&p)b.onclick=()=>w.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${p}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>`;hydrateVimeoDurations(d,durations)}
function esc(s){return String(s??'').replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[c]))}
initLevel15().catch(console.error);
