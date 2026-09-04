const courses = [
  {title:'Options Trading Course Level 1: Buying Call Option',level:'Beginner',categories:['Basic Option'],url:'/courses/options-trading-course-level-1-buying-call-option/',image:'../assets/images/courses/options-trading-course-level-1-buying-call-option.webp'},
  {title:'Options Trading Course Level 2: Selling Call Option',level:'Beginner',categories:['Basic Option'],url:'/courses/options-trading-level-2-selling-call-option-strategy-2/',image:'../assets/images/courses/options-trading-level-2-selling-call-option-strategy-2.webp'},
  {title:'Options Trading Course Level 3: Buying Put Option',level:'Beginner',categories:['Basic Option'],url:'/courses/options-trading-level-3-buying-put-option-strategy/',image:'../assets/images/courses/options-trading-level-3-buying-put-option-strategy.webp'},
  {title:'Options Trading Course Level 4: Selling Put Option',level:'Beginner',categories:['Basic Option'],url:'/courses/options-trading-level-4-selling-put-option-strategy/',image:'../assets/images/courses/options-trading-level-4-selling-put-option-strategy.webp'},
  {title:'Options Trading Course Level 5: Theta & Time Decay',level:'Beginner',categories:['Basic Option','Option Greeks'],url:'/courses/option-greeks-level-5-theta-time-decay/',image:'../assets/images/courses/option-greeks-level-5-theta-time-decay.webp'},
  {title:'Options Trading Course Level 6: Vega and Volatility',level:'Beginner',categories:['Basic Option','Option Greeks'],url:'/courses/greek-option-level-6-vega-volatility-trading/',image:'../assets/images/courses/greek-option-level-6-vega-volatility-trading.webp'},
  {title:'Options Trading Course Level 7: Delta Effect',level:'Beginner',categories:['Basic Option','Option Greeks'],url:'/courses/option-greeks-level-7-delta-effect-strategy/',image:'../assets/images/courses/option-greeks-level-7-delta-effect-strategy.webp'},
  {title:'Options Trading Course Level 8: All Greeks In Action',level:'Beginner',categories:['Basic Option','Option Greeks'],url:'/courses/option-greeks-level-8-option-greeks-in-action/',image:'../assets/images/courses/option-greeks-level-8-option-greeks-in-action.webp'},
  {title:'Advanced Option: Level 9 – Bull Call Spread Strategy',level:'Intermediate',categories:['Advanced Options'],url:'/courses/advanced-option-level-9-bull-call-spread/',image:'../assets/images/courses/advanced-option-level-9-bull-call-spread.webp'},
  {title:'Advanced Option: Level 10 – Bear Put Spread',level:'Intermediate',categories:['Advanced Options'],url:'/courses/advanced-option-level-10-bear-put-spread/',image:'../assets/images/courses/advanced-option-level-10-bear-put-spread.webp'},
  {title:'Advanced Option: Level 11 – Short Iron Condor',level:'Intermediate',categories:['Advanced Options'],url:'/courses/advanced-option-level-11-short-iron-condor/',image:'../assets/images/courses/advanced-option-level-11-short-iron-condor.webp'},
  {title:'Advanced Option: Level 12 – Butterfly',level:'Intermediate',categories:['Advanced Options'],url:'/courses/advanced-option-level-12-butterfly/',image:'../assets/images/courses/advanced-option-level-12-butterfly.webp'},
  {title:'Advanced Option: Level 13 – Calendar Spreads',level:'Intermediate',categories:['Advanced Options'],url:'/courses/advanced-option-level-13-calendar-spreads/',image:'../assets/images/courses/advanced-option-level-13-calendar-spreads.webp'},
  {title:'Options Trading Option Level 14: Backspread',level:'Intermediate',categories:['Advanced Options'],url:'/courses/advanced-option-level-14-backspread/',image:'../assets/images/courses/advanced-option-level-14-backspread.webp'},
  {title:'Advanced Option: Level 15 – Short Straddle',level:'Intermediate',categories:['Advanced Options'],url:'/courses/advanced-option-level-15-short-straddle/',image:'../assets/images/courses/advanced-option-level-15-short-straddle.webp'},
  {title:'Advanced Option: Level 16 – Short Strangle',level:'Intermediate',categories:['Advanced Options'],url:'/courses/advanced-option-level-16-short-strangle/',image:'../assets/images/courses/advanced-option-level-16-short-strangle.webp'},
  {title:'Advanced Option: Level 17 – Covered Calls',level:'Intermediate',categories:['Advanced Options'],url:'/courses/advanced-option-level-17-covered-calls/',image:'../assets/images/courses/advanced-option-level-17-covered-calls.webp'},
  {title:'Advanced Option: Level 18 – Protective Puts',level:'Intermediate',categories:['Advanced Options'],url:'/courses/advanced-option-level-18-protective-puts/',image:'../assets/images/courses/advanced-option-level-18-protective-puts.webp'},
  {title:'Options Portfolio: Level 20 – Optimizing Portfolio',level:'Intermediate',categories:['Options Portfolio'],url:'/courses/options-portfolio-level-20-optimizing-portfolio/',image:'../assets/images/courses/options-portfolio-level-20-optimizing-portfolio.webp'},
  {title:'Options Strategies Level 21: Mastering VIX Volatility',level:'Intermediate',categories:['Advanced Options'],url:'/courses/level-21-mastering-vix-volatility-trading/',image:'../assets/images/courses/level-21-mastering-vix-volatility-trading.webp'},
  {title:'Options Strategies Level 22: VIX Hedging And Speculation',level:'Intermediate',categories:['Advanced Options'],url:'/courses/level-22-vix-options-hedging-and-speculation/',image:'../assets/images/courses/level-22-vix-options-hedging-and-speculation.webp'},
  {title:'Level 45/A – Pre-Earnings Announcement Options Strategies',level:'Advanced',categories:['Options Strategies'],url:'/courses/level-45-a-pre-earnings-announcement-options-strategies/',image:'../assets/images/courses/level-45-a-pre-earnings-announcement-options-strategies.webp'},
  {title:'Level 45/B – At-Earnings Announcement Options Strategies',level:'Advanced',categories:['Options Strategies'],url:'/courses/level-45-b-at-earnings-announcement-options-strategies/',image:'../assets/images/courses/level-45-b-at-earnings-announcement-options-strategies.webp'},
  {title:'Level 45/C – Post-Earnings Announcement Options Strategies',level:'Advanced',categories:['Options Strategies'],url:'/courses/level-45-c-post-earnings-announcement-options-strategies/',image:'../assets/images/courses/level-45-c-post-earnings-announcement-options-strategies.webp'},
  {title:'Options Strategies Level 46 – Dividend Capture Strategy',level:'Advanced',categories:['Options Strategies'],url:'/courses/level-46-dividend-capture-strategy-minimizing-risk/',image:'../assets/images/courses/level-46-dividend-capture-strategy-minimizing-risk.webp'},
  {title:'Options Strategies Level 47 – Broken Wings Butterfly',level:'Advanced',categories:['Options Strategies'],url:'/courses/level-47-broken-wings-butterfly/',image:'../assets/images/courses/level-47-broken-wings-butterfly.webp'},
  {title:'Options Strategies Level 48: Sector Rotation',level:'Advanced',categories:['Options Strategies'],url:'/courses/level-48-sector-rotation-strategy/',image:'../assets/images/courses/level-48-sector-rotation-strategy.webp'},
  {title:'Options Strategies Level 49: Event-Driven Catalyst',level:'Advanced',categories:['Options Strategies'],url:'/courses/level-49-event-driven-catalyst-strategy/',image:'../assets/images/courses/level-49-event-driven-catalyst-strategy.webp'},
  {title:'Adjustments Short Iron Condor Strategies',level:'Intermediate',categories:['Options Adjustments'],url:'/courses/adjustments-short-iron-condor-strategies/',image:'../assets/images/courses/adjustments-short-iron-condor-strategies.webp'},
  {title:'Case Studies – Butterfly Strategies',level:'Intermediate',categories:['Case Studies'],url:'/courses/case-studies-butterfly-strategiesgle-3/',image:'../assets/images/courses/case-studies-butterfly-strategiesgle-3.webp'},
  {title:'Case Studies – Short Strangle',level:'Intermediate',categories:['Case Studies'],url:'/courses/case-studies-short-strangle-3/',image:'../assets/images/courses/case-studies-short-strangle-3.webp'},
  {title:'Adjustments – Short Strangle',level:'Intermediate',categories:['Options Adjustments'],url:'/courses/adjustments-short-strangle-2/',image:'../assets/images/courses/adjustments-short-strangle-2.webp'},
  {title:'Adjustments – Bull Call Spread',level:'Intermediate',categories:['Options Adjustments'],url:'/courses/adjustments-bull-call-spread-2/',image:'../assets/images/courses/adjustments-bull-call-spread-2.webp'},
  {title:'Case Studies – Bull Call Spread',level:'Intermediate',categories:['Case Studies'],url:'/courses/case-studies-bull-call-spread-2/',image:'../assets/images/courses/case-studies-bull-call-spread-2.webp'},
  {title:'Case Studies – Calendar Spreads',level:'Intermediate',categories:['Case Studies'],url:'/courses/case-studies-calendar-spreads-2/',image:'../assets/images/courses/case-studies-calendar-spreads-2.webp'},
  {title:'Adjustments Calendar Spreads',level:'Intermediate',categories:['Options Adjustments'],url:'/courses/adjustments-calendar-spreads-2/',image:'../assets/images/courses/adjustments-calendar-spreads-2.webp'},
  {title:'Adjustments – Short Straddle',level:'Intermediate',categories:['Options Adjustments'],url:'/courses/adjustments-short-straddle-2/',image:'../assets/images/courses/adjustments-short-straddle-2.webp'},
  {title:'Case Studies – Short Straddle',level:'Intermediate',categories:['Case Studies'],url:'/courses/case-studies-short-straddle-2/',image:'../assets/images/courses/case-studies-short-straddle-2.webp'},
  {title:'Adjustment Poor Man’s Covered Call',level:'Intermediate',categories:['Options Adjustments'],url:'/courses/adjustment-poor-mans-covered-call-2/',image:'../assets/images/courses/adjustment-poor-mans-covered-call-2.webp'},
  {title:'Case Studies – Short Iron Condor Strategies',level:'Intermediate',categories:['Case Studies'],url:'/courses/case-studies-short-iron-condor-strategies/',image:'../assets/images/courses/case-studies-short-iron-condor-strategies.webp'},
  {title:'Adjustments Butterfly Strategies',level:'Intermediate',categories:['Options Adjustments'],url:'/courses/adjustments-butterfly-strategies/',image:'../assets/images/courses/adjustments-butterfly-strategies.webp'},
  {title:'Adjusting Covered Call',level:'Intermediate',categories:['Options Adjustments'],url:'/courses/adjusting-covered-call/',image:'../assets/images/courses/adjusting-covered-call.webp'},
  {title:'Case Study Covered Call',level:'Intermediate',categories:['Case Studies'],url:'/courses/case-study-covered-call/',image:'../assets/images/courses/case-study-covered-call.webp'},
  {title:'Poor Man’s Covered Call',level:'Intermediate',categories:['Advanced Options'],url:'/courses/poor-mans-covered-call/',image:'../assets/images/courses/poor-mans-covered-call.webp'},
  {title:'Managing a Bullish to Neutral Options Portfolio',level:'Intermediate',categories:['Options Portfolio'],url:'/courses/managing-a-bullish-to-neutral-options-portfolio/',image:'../assets/images/courses/managing-a-bullish-to-neutral-options-portfolio.webp'},
  {title:'Introduction to Futures Contract',level:'Advanced',categories:['Options on Futures'],url:'/courses/introduction-to-futures-contract/',image:'../assets/images/courses/introduction-to-futures-contract.webp'},
  {title:'Level 72 – Natural Gas Options on Futures',level:'Advanced',categories:['Options on Futures'],url:'/courses/level-72-natural-gas-options-on-futures-2/',image:'../assets/images/courses/level-72-natural-gas-options-on-futures-2.webp'},
  {title:'Level 73 – Crude Oil Options on Futures',level:'Advanced',categories:['Options on Futures'],url:'/courses/level-73-crude-oil-options-on-futures/',image:'../assets/images/courses/level-73-crude-oil-options-on-futures.webp'},
  {title:'Level 77 – Silver Trading Options on Future',level:'Advanced',categories:['Options on Futures'],url:'/courses/level-77-silver-trading-options-on-future/',image:'../assets/images/courses/level-77-silver-trading-options-on-future.webp'},
  {title:'Level 81 – Gold Trading Options on Future',level:'Advanced',categories:['Options on Futures'],url:'/courses/level-81-gold-trading-options-on-future/',image:'../assets/images/courses/level-81-gold-trading-options-on-future.webp'},
  {title:'Level 82 – Corn Futures Trading Strategy',level:'Advanced',categories:['Options on Futures'],url:'/courses/level-82-corn-futures-trading-strategy/',image:'../assets/images/courses/level-82-corn-futures-trading-strategy.webp'},
  {title:'Level 83 – Soybean Trading Future Professionals',level:'Advanced',categories:['Options on Futures'],url:'/courses/level-83-soybean-trading-future-professionals/',image:'../assets/images/courses/level-83-soybean-trading-future-professionals.webp'},
  {title:'Level 84 – Wheat Trading Future Professionals',level:'Advanced',categories:['Options on Futures'],url:'/courses/level-84-wheat-trading-future-professionals/',image:'../assets/images/courses/level-84-wheat-trading-future-professionals.webp'},
  {title:'Level 85 – UVXY Stock Strategies',level:'Advanced',categories:['Options Strategies'],url:'/courses/level-85-uvxy-stock-strategies/',image:'../assets/images/courses/level-85-uvxy-stock-strategies.webp'},
  {title:'Building a Diversified Portfolio',level:'Intermediate',categories:['Options Portfolio'],url:'/courses/building-a-diversified-portfolio/',image:'../assets/images/courses/building-a-diversified-portfolio.webp'},
  {title:'Selling Put Case Study',level:'Beginner',categories:['Beginner Case Studies'],url:'/courses/selling-put-case-study/',image:'../assets/images/courses/selling-put-case-study.webp'},
  {title:'Selling Call Case Study',level:'Beginner',categories:['Beginner Case Studies'],url:'/courses/selling-call-case-study/',image:'../assets/images/courses/selling-call-case-study.webp'},
  {title:'Practical Usage – Level 1.1 – Long Call',level:'Beginner',categories:['Basic Option','Beginner Case Studies'],url:'/courses/practical-usage-level-1-1-long-call/',image:'../assets/images/courses/practical-usage-level-1-1-long-call.webp'},
  {title:'Practical Usage – Level 3.1 – Long Put',level:'Beginner',categories:['Basic Option','Beginner Case Studies'],url:'/courses/practical-usage-level-3-1-long-put/',image:'../assets/images/courses/practical-usage-level-3-1-long-put.webp'}
];

const PAGE_SIZE = 9;
let currentPage = 1;
const grid = document.getElementById('allCourseGrid');
const pagination = document.getElementById('pagination');
const search = document.getElementById('courseSearch');
const sort = document.getElementById('sortCourses');
const noResults = document.getElementById('noResults');
const resultCount = document.getElementById('resultCount');
const toolbarCount = document.getElementById('toolbarCount');

function activeValues(name){return [...document.querySelectorAll(`input[name="${name}"]:checked`)].map(x=>x.value)}
function filteredCourses(){
  const q=search.value.trim().toLowerCase();
  const levels=activeValues('level');
  const categories=activeValues('category');
  let list=courses.filter(c=>(!q||`${c.title} ${c.categories.join(' ')} ${c.level}`.toLowerCase().includes(q))&&(!levels.length||levels.includes(c.level))&&(!categories.length||categories.some(cat=>c.categories.includes(cat))));
  if(sort.value==='title') list=list.slice().sort((a,b)=>a.title.localeCompare(b.title));
  if(sort.value==='level'){const rank={Beginner:1,Intermediate:2,Advanced:3};list=list.slice().sort((a,b)=>rank[a.level]-rank[b.level]||a.title.localeCompare(b.title));}
  return list;
}
function card(c){
  return `<article class="catalog-course-card"><div class="thumb"><img src="${c.image}" alt="" loading="lazy" onerror="this.style.display='none'"></div><a href="${c.url}"><span class="free-pill">FREE COURSE</span><div class="category">${c.categories.join(' · ')}</div><h2>${c.title}</h2><div class="meta"><strong>${c.level}</strong><span>Start course →</span></div></a></article>`;
}
function render(){
  const list=filteredCourses();
  const pages=Math.max(1,Math.ceil(list.length/PAGE_SIZE));
  if(currentPage>pages)currentPage=pages;
  resultCount.textContent=`${list.length} course${list.length===1?'':'s'}`;
  toolbarCount.textContent=list.length===courses.length?`All ${courses.length} courses`:`${list.length} courses found`;
  const start=(currentPage-1)*PAGE_SIZE;
  const slice=list.slice(start,start+PAGE_SIZE);
  grid.innerHTML=slice.map(card).join('');
  grid.hidden=!slice.length;noResults.hidden=!!slice.length;
  renderPagination(pages);
}
function renderPagination(pages){
  if(pages<=1){pagination.innerHTML='';return}
  let html=`<button ${currentPage===1?'disabled':''} data-page="${currentPage-1}">Previous</button>`;
  const visible=[];for(let i=1;i<=pages;i++){if(i===1||i===pages||Math.abs(i-currentPage)<=1)visible.push(i)}
  let prev=0;visible.forEach(i=>{if(prev&&i-prev>1)html+='<span>…</span>';html+=`<button class="${i===currentPage?'active':''}" data-page="${i}">${i}</button>`;prev=i});
  html+=`<button ${currentPage===pages?'disabled':''} data-page="${currentPage+1}">Next</button>`;
  pagination.innerHTML=html;
  pagination.querySelectorAll('button[data-page]').forEach(b=>b.addEventListener('click',()=>{const p=Number(b.dataset.page);if(p>=1&&p<=pages){currentPage=p;render();document.getElementById('catalog').scrollIntoView({behavior:'smooth',block:'start'})}}));
}
function reset(){search.value='';sort.value='default';document.querySelectorAll('.filters input[type=checkbox]').forEach(x=>x.checked=false);currentPage=1;render()}
search.addEventListener('input',()=>{currentPage=1;render()});
sort.addEventListener('change',()=>{currentPage=1;render()});
document.querySelectorAll('.filters input[type=checkbox]').forEach(x=>x.addEventListener('change',()=>{currentPage=1;render()}));
document.getElementById('resetFilters').addEventListener('click',reset);
render();