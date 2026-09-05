const curriculumGroups=[
  {title:'Chapter 1: Delta Fundamentals',lessons:[1,2,3,4,5]},
  {title:'Chapter 2: Delta and the Option Chains',lessons:[6,7,8,9,10,11,12,13]},
  {title:'Chapter 3: Delta in Profit and Loss Analysis',lessons:[14,15,16,17]},
  {title:'Chapter 4: The Delta Curve',lessons:[18,19,20,21,22]},
  {title:'Chapter 4.1: Gamma',lessons:[23,24,25,26,27,28]},
  {title:'Chapter 5: Delta for Hedging an Investment Portfolio',lessons:[29,30,31,32,33,34,35,36,37]},
  {title:'Practical Delta Application',lessons:[38]}
];
const DURATION_CACHE_KEY='oa-level7-vimeo-durations';
function formatDuration(seconds){seconds=Math.round(Number(seconds)||0);if(!seconds)return '';const h=Math.floor(seconds/3600),m=Math.floor((seconds%3600)/60),s=seconds%60;return h?`${h}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`:`${m}:${String(s).padStart(2,'0')}`}
function readDurationCache(){try{return JSON.parse(localStorage.getItem(DURATION_CACHE_KEY)||'{}')}catch(e){return {}}}
function writeDurationCache(cache){try{localStorage.setItem(DURATION_CACHE_KEY,JSON.stringify(cache))}catch(e){}}
async function getVimeoDuration(vimeoId,cache){if(!vimeoId)return '';if(cache[vimeoId])return cache[vimeoId];try{const r=await fetch(`https://vimeo.com/api/oembed.json?url=${encodeURIComponent(`https://vimeo.com/${vimeoId}`)}`);if(!r.ok)return '';const j=await r.json();const d=formatDuration(j.duration);if(d){cache[vimeoId]=d;writeDurationCache(cache)}return d}catch(e){return ''}}
async function initLevel7(){
  const res=await fetch('course-data.json');
  if(!res.ok) throw new Error(`Failed to load course data: ${res.status}`);
  const data=await res.json();
  const byNumber=new Map(data.lessons.map(l=>[l.number,l]));
  const cache=readDurationCache();
  data.lessons.forEach(l=>{if(l.vimeoId&&cache[l.vimeoId])l.duration=cache[l.vimeoId]});
  const curriculum=document.querySelector('.curriculum-list');
  function render(){
    if(!curriculum)return;
    curriculum.innerHTML=curriculumGroups.map(group=>{const items=group.lessons.map(n=>byNumber.get(n)).filter(Boolean);return `<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(group.title)}</h3>${items.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">▶</span><div><strong>${esc(l.title)}</strong><small data-duration-id="${l.vimeoId||''}">${esc(l.duration||'—')}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`}).join('');
  }
  render();
  const count=document.querySelector('.curriculum-title strong'); if(count) count.textContent=`${data.lessons.length} Lessons`;
  const wrap=document.querySelector('.course-image-wrap'),btn=document.querySelector('.course-preview-play');
  const preview=data.course.previewVimeoId||data.lessons.find(l=>l.vimeoId)?.vimeoId;
  if(wrap&&btn&&preview) btn.addEventListener('click',()=>{wrap.classList.add('is-playing');wrap.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${preview}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Course preview"></iframe>`});
  await Promise.all(data.lessons.filter(l=>l.vimeoId&&!cache[l.vimeoId]).map(async l=>{const d=await getVimeoDuration(l.vimeoId,cache);if(d){l.duration=d;document.querySelectorAll(`[data-duration-id="${l.vimeoId}"]`).forEach(el=>el.textContent=d)}}));
}
function esc(s){return String(s??'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]))}
initLevel7().catch(console.error);
