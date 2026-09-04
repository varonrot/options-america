const syllabusSections = [
  {
    title: 'Course Start',
    items: [
      [1,'What will we learn in this course?','2 min','video'],
      [2,'About the instructor','3 min','video'],
      [3,'Viewing our courses is for subscribers only','2 min','video'],
      [4,'The trading platform we will use in the course','2 min','video'],
      [5,'Main windows of the trading platform','3 min','video'],
      [6,'Video viewing quality','1 min','video'],
      [7,'The lessons in the course are short and focused','2 min','video'],
      [8,'5 reasons why to trade options','3 min','video'],
      [9,'Risk Disclaimer','3 min','video']
    ]
  },
  {
    title: "Options Course Syllabus: Part 1 - Introduction to the Call Option - A Buyer's Perspective",
    items: [
      [10,'Welcome to the first part of the long call strategy','2 min','video'],
      [11,'Understanding Options in the Financial World','2 min','video'],
      [12,'How much money did John make from buying the option?','2 min','video'],
      [13,'What if John had bought a stock instead of an option?','2 min','video'],
      [14,'Call options definition','2 min','video'],
      [15,"What happens if Apple's price reaches $200 per share?",'2 min','video'],
      [16,"What happens if Apple's price reaches $150 or $100 at expiration?",'2 min','video'],
      [17,'What will happen if Apple shares reach $175 at expiration?','2 min','video'],
      [18,'Conclusion of the concepts: in the money, out of the money and in the money','2 min','video'],
      [19,'Call Option Definition in the real estate','2 min','video'],
      [20,'Break down the scenarios based on the example provided','3 min','video'],
      [21,'Summary lesson','2 min','video'],
      [22,'Test on Buying Call Options','10 questions','quiz']
    ]
  },
  {
    title: 'Part 2 Analyze risk reward chart',
    items: [
      [23,'What will we learn in this part?','2 min','video'],
      [24,'Display of profit and loss analysis on the platform','2 min','video'],
      [25,'The difference between profit and loss analysis of a stock option','2 min','video'],
      [26,'The types of graphs in the analysis of an option','2 min','video'],
      [27,'Display profit and loss analysis of an option','2 min','video'],
      [28,'Scenarios of a price change in the underlying asset','2 min','video'],
      [29,'Demonstration purposes','2 min','video'],
      [30,'A scenario where Apple stock rises to $200 per share','3 min','video'],
      [31,'The time limit in options trading','3 min','video'],
      [32,'The break even point in the option','2 min','video'],
      [33,'Different break even points','2 min','video'],
      [34,'Further explanation of the time limit: real estate VS. option','2 min','video'],
      [35,'A test on trading analysis','11 questions','quiz']
    ]
  },
  {
    title: "Part 3 - Chain of Options - Buyer's Perspective",
    items: [
      [36,'An introduction to option chains','3 min','video'],
      [37,'Options with different expiration dates','2 min','video'],
      [38,'Display of different expiration dates on a trading platform','3 min','video'],
      [39,'An option with a far versus near expiration date','2 min','video'],
      [40,'Explain why a more distant option is more expensive','3 min','video'],
      [41,'Display of different exercise prices on the price graph','3 min','video'],
      [42,'The various exercise prices in the option chains','2 min','video'],
      [43,'Understanding In-the-Money Options: Navigating the Options Chain','3 min','video'],
      [44,'Movement of strike prices in the options chain','3 min','video'],
      [45,'What if the stock price goes down?','2 min','video'],
      [46,'bid and ask price in the options chains','3 min','video'],
      [47,'The relationship between the exercise price and the premium','3 min','video'],
      [48,'Internal value and external value','3 min','video'],
      [49,'Average premium price','3 min','video'],
      [50,'External value curve','2 min','video'],
      [51,'Option chains during active trading','2 min','video'],
      [52,'Summary lesson on option chains','3 min','video']
    ]
  },
  {
    title: 'Part 4 - Integrated Options Analysis: Connecting Chains, Profit, and Price',
    items: [
      [53,'What will we learn in this segment?','2 min','video'],
      [54,'Trader assumptions','3 min','video'],
      [55,'Expect Apple stock to reach 230 in October','2 min','video'],
      [56,'190 exercise price selection in October 2024','3 min','video'],
      [57,'Choosing the option for profit and loss analysis','3 min','video'],
      [58,'The breakeven point in our strategy','2 min','video'],
      [59,'Plot the breakeven point on the graph','3 min','video'],
      [60,'Key points of the profit and loss analysis','3 min','video'],
      [61,'A scenario where Apple shares rise to 230 in October 2024','3 min','video'],
      [62,'Summary of part 4','2 min','video']
    ]
  },
  {
    title: 'Part 5 - Integrated Options Analysis: T+0',
    items: [
      [63,'What will we learn in this part?','2 min','video'],
      [64,'Bid and Ask price in real time','3 min','video'],
      [65,'Profit and loss display on the platform','3 min','video'],
      [66,'T+0 scenario if Apple rises to 190','2 min','video'],
      [67,'The T+0 movement','2 min','video'],
      [68,'An explanation of Bid and Ask in the real estate world','2 min','video'],
      [69,'Lesson summary on the relationship of t+0','3 min','video']
    ]
  },
  {
    title: 'Part 6: Case Study - TOS Buying Call Options',
    items: [
      [70,'What will we demonstrate in this part?','2 min','video'],
      [71,'It is important that the spread be as small as possible','3 min','video'],
      [72,'Display mark price & probability in the money','3 min','video'],
      [73,'Mid and Nat price difference','2 min','video']
    ]
  },
  {
    title: 'Part 6.1: Call Options Case Study',
    items: [
      [74,'Practical Usage – Level 1.1 – Long Call','Text lesson','text']
    ]
  }
];

const curriculum = document.querySelector('.curriculum-list');
if (curriculum) {
  curriculum.innerHTML = syllabusSections.map(section => `
    <section class="curriculum-group">
      <h3 class="curriculum-group-title">${section.title}</h3>
      ${section.items.map(([n,title,meta,type]) => `
        <a class="curriculum-item" id="lesson-${n}" href="player/?lesson=${n}">
          <span class="lesson-index">${n}</span>
          <span class="lesson-icon">${type === 'quiz' ? '?' : type === 'text' ? '▤' : '▶'}</span>
          <div><strong>${title}</strong><small>${meta}</small></div>
          <span class="lesson-arrow">›</span>
        </a>`).join('')}
    </section>`).join('');
}

const count = document.querySelector('.curriculum-title strong');
if (count) count.textContent = '74 Lessons';

const mainCourseImage = document.querySelector('.course-image-wrap img');
if (mainCourseImage) {
  mainCourseImage.src = '../../assets/images/courses/legacy/options-trading-course-level-1-buying-call-option.png';
  mainCourseImage.style.display = '';
  mainCourseImage.parentElement.classList.remove('image-missing');
}
