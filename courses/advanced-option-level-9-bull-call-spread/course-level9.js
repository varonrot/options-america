const DURATION_KEY='oa-level9-vimeo-durations';
function originalSection(n){
  if(n<=7)return 'Starting Course';
  if(n<=25)return 'Chapter 2: At the Money Spread Strategy';
  if(n<=40)return 'Chapter 3: Different Types of Bull Call Spread';
  if(n<=47)return 'Chapter 5: Bull Put Spread';
  if(n<=70)return 'Adjustments and Hedging Options Trades';
  if(n<=74)return 'Trade Execution & Case Studies';
  return 'Professional Trading Framework';
}
function fmtDuration(seconds){seconds=Math.max(0,Math.round(Number(seconds)||0));const h=Math.floor(seconds/3600),m=Math.floor((seconds%3600)/60),s=seconds%60;return h?`${h}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`:`${m}:${String(s).padStart(2,'0')}`}
function loadDurations(){try{return JSON.parse(localStorage.getItem(DURATION_KEY)||'{}')}catch(e){return {}}}
function saveDurations(d){localStorage.setItem(DURATION_KEY,JSON.stringify(d))}
async function initLevel9(){
  const r=await fetch('course-data.json');if(!r.ok)throw new Error('course data');
  const d=await r.json(),c=document.querySelector('.curriculum-list'),durations=loadDurations();
  d.lessons.forEach(l=>l.section=originalSection(l.number));
  const render=()=>{
    if(c){const g=new Map();d.lessons.forEach(l=>{if(!g.has(l.section))g.set(l.section,[]);g.get(l.section).push(l)});c.innerHTML=[...g].map(([s,a])=>`<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(s)}</h3>${a.map(l=>{const duration=l.type==='video'&&l.vimeoId&&durations[String(l.vimeoId)]?fmtDuration(durations[String(l.vimeoId)]):(l.duration||'Reading');return `<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">${l.type==='video'?'▶':'▤'}</span><div><strong>${esc(l.title)}</strong><small data-duration-id="${l.vimeoId||''}">${esc(duration)}</small></div><span class="lesson-arrow">›</span></a>`}).join('')}</section>`).join('')}
  };
  render();
  const n=document.querySelector('.curriculum-title strong');if(n)n.textContent=`${d.lessons.length} Lessons`;
  const w=document.querySelector('.course-image-wrap'),b=document.querySelector('.course-preview-play'),p=d.course.previewVimeoId;if(w&&b&&p)b.onclick=()=>{w.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${p}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>`};
  for(const l of d.lessons.filter(x=>x.type==='video'&&x.vimeoId)){
    const id=String(l.vimeoId);if(durations[id])continue;
    try{const res=await fetch(`https://vimeo.com/api/oembed.json?url=${encodeURIComponent('https://vimeo.com/'+id)}`);if(!res.ok)continue;const data=await res.json();if(data.duration){durations[id]=Number(data.duration);saveDurations(durations);document.querySelectorAll(`[data-duration-id="${id}"]`).forEach(el=>el.textContent=fmtDuration(data.duration))}}catch(e){console.debug('Vimeo duration unavailable for',id)}
  }
}
function esc(s){return String(s??'').replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[c]))}
initLevel9().catch(console.error);