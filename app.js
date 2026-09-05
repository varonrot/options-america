const courses=[
  {title:'Buying Call Option',level:'Beginner',desc:'Learn how call options work and how to buy them.',url:'/courses/options-trading-course-level-1-buying-call-option/',image:'/assets/images/courses/legacy/options-trading-course-level-1-buying-call-option.png'},
  {title:'Selling Put Option',level:'Beginner',desc:'Generate income by selling put options.',url:'/courses/options-trading-level-4-selling-put-option-strategy/',image:'/assets/images/courses/legacy/options-trading-level-4-selling-put-option-strategy.png'},
  {title:'Understanding Theta',level:'Intermediate',desc:'Time decay and its impact on options.',url:'/courses/option-greeks-level-5-theta-time-decay/',image:'/assets/images/courses/legacy/option-greeks-level-5-theta-time-decay.png'},
  {title:'Iron Condor Strategy',level:'Advanced',desc:'Learn one of the most popular neutral strategies.',url:'/courses/advanced-option-level-11-short-iron-condor/',image:'/assets/images/courses/legacy/advanced-option-level-11-short-iron-condor.png'},
  {title:'Calendar Spread',level:'Intermediate',desc:'Profit from time decay with calendar spreads.',url:'/courses/advanced-option-level-13-calendar-spreads/',image:'/assets/images/courses/legacy/advanced-option-level-13-calendar-spreads.png'},
  {title:'Options on Futures',level:'Advanced',desc:'Trade options on crude oil, gold and more.',url:'/courses/introduction-to-futures-contract/',image:'/assets/images/courses/legacy/introduction-to-futures-contract.png'}
];
const grid=document.getElementById('courseGrid');
if(grid){grid.innerHTML=courses.map(c=>`<a class="course-card" href="${c.url}"><div class="course-art course-art-image"><img src="${c.image}" alt="${c.title}" loading="lazy"></div><div class="course-body"><span>FREE COURSE · ${c.level}</span><h3>${c.title}</h3><p>${c.desc}</p></div></a>`).join('')}
