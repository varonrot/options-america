const LEVEL6_DURATION_KEY='oa-level6-vimeo-durations';
const level6DurationCache=JSON.parse(localStorage.getItem(LEVEL6_DURATION_KEY)||'{}');
const level6Groups=[
  {title:'Course Introduction & Volatility Foundations',from:1,to:7},
  {title:'Chapter 2: Types of Volatility in Options Trading',from:8,to:13},
  {title:'Chapter 3: IV Rank vs IV Percentile',from:14,to:19},
  {title:'Chapter 4–5: Vega and the Option Chains',from:20,to:28},
  {title:'Chapter 6: The Vega Curve',from:29,to:35},
  {title:'Chapter 7: Implied Volatility Adjustments',from:36,to:42},
  {title:'VIX Index & Portfolio Vega',from:43,to:48}
];
function level6Section(n){return level6Groups.find(g=>n>=g.from&&n<=g.to)?.title||'Course Curriculum'}
function fmtDuration(sec){sec=Math.round(Number(sec)||0);if(!sec)return null;const h=Math.floor(sec/3600),m=Math.floor((sec%3600)/60),s=sec%60;return h?`${h}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`:`${m}:${String(s).padStart(2,'0')}`}
function lessonDuration(l){return l.type==='text'?'Reading':(level6DurationCache[l.vimeoId]||l.duration||'—')}
async function hydrateVimeoDurations(data){await Promise.all(data.lessons.filter(l=>l.type==='video'&&l.vimeoId&&!level6DurationCache[l.vimeoId]).map(async l=>{try{const r=await fetch(`https://vimeo.com/api/oembed.json?url=https://vimeo.com/${encodeURIComponent(l.vimeoId)}`);if(!r.ok)return;const j=await r.json(),d=fmtDuration(j.duration);if(d)level6DurationCache[l.vimeoId]=d}catch(e){}}));localStorage.setItem(LEVEL6_DURATION_KEY,JSON.stringify(level6DurationCache));renderLevel6Curriculum(data)}
function renderLevel6Curriculum(data){const curriculum=document.querySelector('.curriculum-list');if(!curriculum)return;curriculum.innerHTML=level6Groups.map(g=>{const items=data.lessons.filter(l=>l.number>=g.from&&l.number<=g.to);return `<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(g.title)}</h3>${items.map(l=>`<a class="curriculum-item" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">${l.type==='video'?'▶':'▤'}</span><div><strong>${esc(l.title)}</strong><small>${esc(lessonDuration(l))}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`}).join('')}
async function initLevel6(){const res=await fetch('course-data.json');if(!res.ok)throw new Error(`Failed to load course data: ${res.status}`);const data=await res.json();data.lessons.forEach(l=>l.section=level6Section(l.number));renderLevel6Curriculum(data);const count=document.querySelector('.curriculum-title strong');if(count)count.textContent=`${data.lessons.length} Lessons`;const wrap=document.querySelector('.course-image-wrap'),btn=document.querySelector('.course-preview-play');const preview=data.course.previewVimeoId||data.lessons.find(l=>l.vimeoId)?.vimeoId;if(wrap&&btn&&preview)btn.addEventListener('click',()=>{wrap.classList.add('is-playing');wrap.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${preview}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Course preview"></iframe>`});hydrateVimeoDurations(data)}
function esc(s){return String(s??'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]))}
initLevel6().catch(console.error);
