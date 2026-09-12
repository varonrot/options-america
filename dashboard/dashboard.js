const COURSE_ROWS=`
options-trading-course-level-1-buying-call-option|Options Trading Course Level 1: Buying Call Option|Beginner|74|oa-level1-completed
options-trading-level-2-selling-call-option-strategy-2|Options Trading Course Level 2: Selling Call Option|Beginner|45|oa-level2-completed
options-trading-level-3-buying-put-option-strategy|Options Trading Course Level 3: Buying Put Option|Beginner|38|oa-level3-completed
options-trading-level-4-selling-put-option-strategy|Options Trading Course Level 4: Selling Put Option|Beginner|45|oa-level4-completed
option-greeks-level-5-theta-time-decay|Options Trading Course Level 5: Theta & Time Decay|Beginner|43|oa-level5-completed
options-trading-course-level-6-vega-and-volatility|Options Trading Course Level 6: Vega and Volatility|Beginner|48|oa-level6-completed
option-greeks-level-7-delta-effect-strategy|Options Trading Course Level 7: Delta Effect|Beginner|38|oa-level7-completed
option-greeks-level-8-option-greeks-in-action|Options Trading Course Level 8: All Greeks In Action|Beginner|46|oa-level8-completed
advanced-option-level-9-bull-call-spread|Advanced Option: Level 9 – Bull Call Spread Strategy|Intermediate|85|oa-level9-completed
advanced-option-level-10-bear-put-spread|Advanced Option: Level 10 – Bear Put Spread|Intermediate|1|oa-level10-completed
advanced-option-level-11-short-iron-condor|Advanced Option: Level 11 – Short Iron Condor|Intermediate|63|oa-level11-completed
advanced-option-level-12-butterfly|Advanced Option: Level 12 – Butterfly|Intermediate|50|oa-level12-completed
advanced-option-level-13-calendar-spreads|Advanced Option: Level 13 – Calendar Spreads|Intermediate|38|oa-level13-completed
advanced-option-level-14-backspread|Options Trading Option Level 14: Backspread|Intermediate|47|oa-level14-completed
advanced-option-level-15-short-straddle|Advanced Option: Level 15 – Short Straddle|Intermediate|57|oa-level15-completed
advanced-option-level-16-short-strangle|Advanced Option: Level 16 – Short Strangle|Intermediate|60|oa-level16-completed
advanced-option-level-17-covered-calls|Advanced Option: Level 17 – Covered Calls|Intermediate|68|oa-level17-completed
advanced-option-level-18-protective-puts|Advanced Option: Level 18 – Protective Puts|Intermediate|45|oa-level18-completed
options-portfolio-level-20-optimizing-portfolio|Options Portfolio: Level 20 – Optimizing Portfolio|Intermediate|56|oa-level20-completed
level-21-mastering-vix-volatility-trading|Options Strategies Level 21: Mastering VIX Volatility|Intermediate|45|oa-level21-completed
level-22-vix-options-hedging-and-speculation|Options Strategies Level 22: VIX Hedging And Speculation|Intermediate|45|oa-level22-completed
level-45-a-pre-earnings-announcement-options-strategies|Level 45/A – Pre-Earnings Announcement Options Strategies|Advanced|33|oa-level45a-completed
level-45-b-at-earnings-announcement-options-strategies|Level 45/B – At-Earnings Announcement Options Strategies|Advanced|26|oa-level45b-completed
level-45-c-post-earnings-announcement-options-strategies|Level 45/C – Post-Earnings Announcement Options Strategies|Advanced|24|oa-level45c-completed
level-46-dividend-capture-strategy-minimizing-risk|Options Strategies Level 46 – Dividend Capture Strategy|Advanced|35|oa-level46-completed
level-47-broken-wings-butterfly|Options Strategies Level 47 – Broken Wings Butterfly|Advanced|42|oa-level47-completed
level-48-sector-rotation-strategy|Options Strategies Level 48: Sector Rotation|Advanced|45|oa-level48-completed
level-49-event-driven-catalyst-strategy|Options Strategies Level 49: Event-Driven Catalyst|Advanced|45|oa-level49-completed
adjustments-short-iron-condor-strategies|Adjustments Short Iron Condor Strategies|Intermediate|24|oa-adjustments-short-iron-condor-completed
case-studies-butterfly-strategiesgle-3|Case Studies – Butterfly Strategies|Intermediate|32|oa-case-studies-butterfly-completed
case-studies-short-strangle-3|Case Studies – Short Strangle|Intermediate|1|oa-case-studies-short-strangle-completed
adjustments-short-strangle-2|Adjustments – Short Strangle|Intermediate|10|oa-adjustments-short-strangle-completed
adjustments-bull-call-spread-2|Adjustments – Bull Call Spread|Intermediate|25|oa-adjustments-bull-call-spread-completed
case-studies-bull-call-spread-2|Case Studies – Bull Call Spread|Intermediate|12|oa-case-studies-bull-call-spread-completed
case-studies-calendar-spreads-2|Case Studies – Calendar Spreads|Intermediate|1|oa-case-studies-calendar-spreads-completed
adjustments-calendar-spreads-2|Adjustments Calendar Spreads|Intermediate|1|oa-adjustments-calendar-spreads-completed
adjustments-short-straddle-2|Adjustments – Short Straddle|Intermediate|18|oa-adjustments-short-straddle-completed
case-studies-short-straddle-2|Case Studies – Short Straddle|Intermediate|20|oa-case-studies-short-straddle-2-completed
adjustment-poor-mans-covered-call-2|Adjustment Poor Man’s Covered Call|Intermediate|8|oa-adjustment-pmcc-completed
case-studies-short-iron-condor-strategies|Case Studies – Short Iron Condor Strategies|Intermediate|4|oa-case-studies-short-iron-condor-completed
adjustments-butterfly-strategies|Adjustments Butterfly Strategies|Intermediate|32|oa-adjustments-butterfly-completed
adjusting-covered-call|Adjusting Covered Call|Intermediate|16|oa-adjusting-covered-call-completed
case-study-covered-call|Case Study Covered Call|Intermediate|1|oa-case-study-covered-call-completed
poor-mans-covered-call|Poor Man’s Covered Call|Intermediate|63|oa-poor-mans-covered-call-completed
managing-a-bullish-to-neutral-options-portfolio|Managing a Bullish to Neutral Options Portfolio|Advanced|12|oa-bullish-neutral-portfolio-completed
introduction-to-futures-contract|Introduction to Futures Contract|Advanced|60|oa-introduction-futures-completed
level-72-natural-gas-options-on-futures-2|Level 72 – Natural Gas Options on Futures|Advanced|1|oa-natural-gas-futures-completed
level-73-crude-oil-options-on-futures|Level 73 – Crude Oil Options on Futures|Advanced|1|oa-crude-oil-futures-completed
level-77-silver-trading-options-on-future|Level 77 – Silver Trading Options on Future|Advanced|1|oa-silver-futures-completed
level-81-gold-trading-options-on-future|Level 81 – Gold Trading Options on Future|Advanced|1|oa-gold-futures-completed
level-82-corn-futures-trading-strategy|Level 82 – Corn Futures Trading Strategy|Advanced|1|oa-corn-futures-completed
level-83-soybean-trading-future-professionals|Level 83 – Soybean Trading Future Professionals|Advanced|1|oa-soybean-futures-completed
level-84-wheat-trading-future-professionals|Level 84 – Wheat Trading Future Professionals|Advanced|1|oa-wheat-futures-completed
level-85-uvxy-stock-strategies|Level 85 – UVXY Stock Strategies|Advanced|1|oa-uvxy-strategies-completed
building-a-diversified-portfolio|Building a Diversified Portfolio|Intermediate|1|oa-diversified-portfolio-completed
selling-put-case-study|Selling Put Case Study|Beginner|1|oa-selling-put-case-study-completed
selling-call-case-study|Selling Call Case Study|Beginner|1|oa-selling-call-case-study-completed
practical-usage-level-1-1-long-call|Practical Usage – Level 1.1 – Long Call|Beginner|21|oa-practical-long-call-completed
practical-usage-level-3-1-long-put|Practical Usage – Level 3.1 – Long Put|Beginner|5|oa-practical-long-put-completed`.trim();
const COURSE_PROGRESS=COURSE_ROWS.split('\n').map(row=>{const [slug,title,level,total,key]=row.split('|');return{slug,title,level,total:Number(total),key}});
const $=selector=>document.querySelector(selector);let currentFilter='active';
function readArray(key){try{const value=JSON.parse(localStorage.getItem(key)||'[]');return Array.isArray(value)?value:[]}catch(_){return[]}}
function positionFor(course){const completed=[...new Set(readArray(course.key).map(Number))].filter(n=>n>=1&&n<=course.total).sort((a,b)=>a-b);const next=Array.from({length:course.total},(_,i)=>i+1).find(n=>!completed.includes(n))||course.total;return{...course,done:completed.length,percent:course.total?Math.round(completed.length/course.total*100):0,next}}
function playerLink(course,lesson=course.next){return`/courses/${course.slug}/player/?lesson=${lesson}`}
function courseImage(course,className){const image=course.slug==='options-trading-course-level-6-vega-and-volatility'?'/assets/images/courses/legacy/greek-option-level-6-vega-volatility-trading.png':`/assets/images/courses/legacy/${course.slug}.png`;return`<div class="${className}"><img src="${image}" alt="" onerror="this.remove()"></div>`}
function renderContinue(activity){let last=null;try{last=JSON.parse(localStorage.getItem('oa-last-course')||'null')}catch(_){}let course=activity.find(c=>c.slug===last?.slug&&c.percent<100)||activity.find(c=>c.percent>0&&c.percent<100)||activity.find(c=>c.percent===100)||positionFor(COURSE_PROGRESS[0]);const lesson=course.percent===100?course.total:(last?.slug===course.slug?Math.max(1,Number(last.lesson)||course.next):course.next);const label=course.done?'Continue course':'Start your first course';$('#continueCard').innerHTML=`${courseImage(course,'continue-thumb')}<div class="continue-copy"><span class="course-level">${course.level} · ${course.done} of ${course.total} lessons</span><h3>${course.title}</h3><p>${course.done?`Continue with lesson ${lesson}.`:'Begin the structured learning path with the fundamentals.'}</p><div class="progress-track"><i style="width:${course.percent}%"></i></div><div class="progress-label"><span>${course.percent}% complete</span><span>${course.total-course.done} lessons remaining</span></div></div><div class="continue-action"><a class="btn btn-gold" href="${playerLink(course,lesson)}">${label} →</a></div>`}
function renderCards(activity){const filtered=activity.filter(c=>currentFilter==='completed'?c.percent===100:currentFilter==='active'?c.percent>0&&c.percent<100:c.done>0);$('#learningGrid').innerHTML=filtered.map(course=>`<article class="learning-card">${courseImage(course,'learning-card-image')}<div class="learning-card-body"><span class="course-level">${course.level}</span><h3>${course.title}</h3><div class="progress-track"><i style="width:${course.percent}%"></i></div><div class="progress-label"><span>${course.done} / ${course.total} lessons</span><strong>${course.percent}%</strong></div><div class="learning-card-foot"><span>${course.percent===100?'Course completed':'Lesson '+course.next+' is next'}</span><a href="${playerLink(course)}">${course.percent===100?'Review':'Continue'} →</a></div></div></article>`).join('');$('#learningGrid').hidden=!filtered.length;$('#emptyLearning').hidden=!!filtered.length;$('#emptyLearning h3').textContent=activity.some(c=>c.done)?(currentFilter==='completed'?'No completed courses yet':'No courses in this view'):'Your learning journey starts here'}
function renderDashboard(){const activity=COURSE_PROGRESS.map(positionFor),started=activity.filter(c=>c.done>0),completed=activity.filter(c=>c.percent===100),lessons=activity.reduce((sum,c)=>sum+c.done,0),total=activity.reduce((sum,c)=>sum+c.total,0),overall=total?Math.round(lessons/total*100):0;$('#startedCount').textContent=started.length;$('#completedCount').textContent=completed.length;$('#lessonCount').textContent=lessons;$('#availableCount').textContent=COURSE_PROGRESS.length;$('#overallPercent').textContent=`${overall}%`;$('#heroRing').style.setProperty('--progress',overall);renderContinue(activity);renderCards(activity);const next=activity.find(c=>c.done===0)||activity.find(c=>c.percent<100)||activity[0];$('#recommendedTitle').textContent=next.title;$('#recommendedText').textContent=`Continue your ${next.level.toLowerCase()} learning path with ${next.total} structured lessons.`;$('#recommendedLink').href=`/courses/${next.slug}/`}
function showUser(user){const name=user?.user_metadata?.full_name||user?.user_metadata?.name||'';$('#welcomeTitle').textContent=name?`Welcome back, ${name.split(/\s+/)[0]}`:'Welcome back';$('#signinNote').hidden=!!user}
async function loadUser(){if(window.optionsAmericaAuth?.getCurrentUser)showUser(await window.optionsAmericaAuth.getCurrentUser())}
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{currentFilter=button.dataset.filter;document.querySelectorAll('[data-filter]').forEach(x=>x.classList.toggle('active',x===button));renderDashboard()}));
$('#dashboardSignIn').addEventListener('click',()=>window.optionsAmericaAuth?.beginGoogleLogin());window.addEventListener('oa:authchange',event=>showUser(event.detail?.user));window.addEventListener('storage',renderDashboard);renderDashboard();setTimeout(loadUser,0);
