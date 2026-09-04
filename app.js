const courses=[
  {title:'Buying Call Option',level:'Beginner',desc:'Learn how call options work and how to buy them.',c1:'#0f4c81',c2:'#22a6f2'},
  {title:'Selling Put Option',level:'Beginner',desc:'Generate income by selling put options.',c1:'#6b1f1f',c2:'#ef5b3f'},
  {title:'Understanding Theta',level:'Intermediate',desc:'Time decay and its impact on options.',c1:'#2c245f',c2:'#7d66e8'},
  {title:'Iron Condor Strategy',level:'Advanced',desc:'Learn one of the most popular neutral strategies.',c1:'#102d4a',c2:'#20a0ad'},
  {title:'Calendar Spread',level:'Intermediate',desc:'Profit from time decay with calendar spreads.',c1:'#6a3c14',c2:'#d49a37'},
  {title:'Options on Futures',level:'Advanced',desc:'Trade options on crude oil, gold and more.',c1:'#2a2518',c2:'#8c6d28'}
];
const grid=document.getElementById('courseGrid');
if(grid){grid.innerHTML=courses.map(c=>`<article class="course-card"><div class="course-art" style="--c1:${c.c1};--c2:${c.c2}"></div><div class="course-body"><span>FREE COURSE · ${c.level}</span><h3>${c.title}</h3><p>${c.desc}</p></div></article>`).join('')}
