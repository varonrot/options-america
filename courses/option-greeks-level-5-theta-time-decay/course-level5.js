const DURATION_CACHE_KEY='oa-level5-vimeo-durations';
function fmtDuration(seconds){const s=Math.max(0,Math.round(Number(seconds)||0));if(!s)return '—';const h=Math.floor(s/3600),m=Math.floor((s%3600)/60),r=s%60;return h?`${h}:${String(m).padStart(2,'0')}:${String(r).padStart(2,'0')}`:`${m}:${String(r).padStart(2,'0')}`}
function chapterLabel(title){const t=String(title||'');const m=t.match(/chapter\s*([0-9]+(?:\.[0-9]+)?)/i);if(!m)return null;let rest=t.replace(/^.*?chapter\s*[0-9]+(?:\.[0-9]+)?\s*:?\s*/i,'').trim();rest=rest.replace(/^(what\s+(?:we|will)\s+(?:will\s+)?learn(?:ed)?(?:\s+in)?|what\s+will\s+be\s+learned)\s*/i,'').trim();return `Chapter ${m[1]}${rest?`: ${rest}`:''}`}
function applyOriginalChapters(lessons){let current='Course Introduction';for(const l of lessons){const marker=chapterLabel(l.title);if(marker)current=marker;l.section=current}}
async function initLevel5(){
  const res=await fetch('course-data.json');
  if(!res.ok) throw new Error(`Failed to load course-data.json: ${res.status}`);
  const data=await res.json();
  applyOriginalChapters(data.lessons);
  let cache={};try{cache=JSON.parse(localStorage.getItem(DURATION_CACHE_KEY)||'{}')}catch(e){}
  data.lessons.forEach(l=>{if(l.vimeoId&&cache[l.vimeoId])l.duration=cache[l.vimeoId];if(l.type!=='video')l.duration=l.duration||'Reading'});
  const curriculum=document.querySelector('.curriculum-list');
  const render=()=>{
    if(curriculum){
      const groups=new Map();
      data.lessons.forEach(l=>{if(!groups.has(l.section))groups.set(l.section,[]);groups.get(l.section).push(l)});
      curriculum.innerHTML=[...groups.entries()].map(([section,items])=>`<section class="curriculum-group"><h3 class="curriculum-group-title">${esc(section)}</h3>${items.map(l=>`<a class="curriculum-item" data-vimeo-id="${l.vimeoId||''}" href="player/?lesson=${l.number}"><span class="lesson-index">${l.number}</span><span class="lesson-icon">${l.type==='video'?'▶':l.type==='quiz'?'?':'▤'}</span><div><strong>${esc(l.title)}</strong><small>${esc(l.duration)}</small></div><span class="lesson-arrow">›</span></a>`).join('')}</section>`).join('');
    }
  };
  render();
  const count=document.querySelector('.curriculum-title strong');if(count)count.textContent=`${data.lessons.length} Lessons`;
  const wrap=document.querySelector('.course-image-wrap'),btn=document.querySelector('.course-preview-play');
  const preview=data.course.previewVimeoId||data.lessons.find(l=>l.vimeoId)?.vimeoId;
  if(wrap&&btn&&preview)btn.addEventListener('click',()=>{wrap.classList.add('is-playing');wrap.innerHTML=`<iframe class="course-preview-iframe" src="https://player.vimeo.com/video/${preview}?autoplay=1&title=0&byline=0&portrait=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Course preview"></iframe>`});
  const missing=[...new Set(data.lessons.filter(l=>l.type==='video'&&l.vimeoId&&!cache[l.vimeoId]).map(l=>l.vimeoId))];
  if(missing.length){await Promise.allSettled(missing.map(async id=>{const r=await fetch(`https://vimeo.com/api/oembed.json?url=${encodeURIComponent(`https://vimeo.com/${id}`)}`);if(!r.ok)return;const j=await r.json();if(j.duration)cache[id]=fmtDuration(j.duration)}));localStorage.setItem(DURATION_CACHE_KEY,JSON.stringify(cache));data.lessons.forEach(l=>{if(l.vimeoId&&cache[l.vimeoId])l.duration=cache[l.vimeoId]});render()}
}
function esc(s){return String(s??'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]))}
initLevel5().catch(err=>{console.error(err);const count=document.querySelector('.curriculum-title strong');if(count)count.textContent='Unable to load'});
