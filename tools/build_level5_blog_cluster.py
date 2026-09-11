#!/usr/bin/env python3
"""Build the Level 5 Theta & Time Decay SEO cluster."""

from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"
COURSE = "../../courses/option-greeks-level-5-theta-time-decay/"
DATE = "September 11, 2026"


ARTICLES = [
    {
        "slug": "what-is-theta-in-options",
        "tag": "Theta · Beginner",
        "title": "What Is Theta in Options?",
        "description": "Learn what option theta measures, why it is usually negative for buyers and positive for sellers, and what the number can—and cannot—predict.",
        "key": "Theta estimates the theoretical change in an option's value from one day passing, assuming other pricing inputs stay unchanged.",
        "sections": [
            ("Theta in plain English", "Theta is one of the option Greeks. It translates the passage of time into an estimated dollar change in an option's theoretical value. A theta of -0.08 is commonly interpreted as about eight cents of theoretical value lost per share over one day, all else equal; a standard equity contract would therefore reflect about $8."),
            ("Why theta exists", "An option has a finite life. As expiration approaches, there is less time for the underlying price to make a favorable move, so the time-value portion of the premium generally shrinks. Theta describes that erosion rather than a fee charged by a broker or clearinghouse."),
            ("Why theta is not a promise", "Stock price, implied volatility, interest rates and dividends can move at the same time. A favorable price move or volatility increase can outweigh one day's decay, while an unfavorable move can create a loss much larger than the theta estimate."),
            ("How traders use it", "Buyers use theta to judge the cost of waiting; sellers use it to estimate the decay they hope to capture. Both should compare theta with delta, gamma, vega, liquidity and the position's maximum risk instead of using it alone."),
        ],
        "example": "An option quoted at $2.40 has theta of -0.06. If every other pricing input were unchanged, the model might value it near $2.34 after one day. The actual market price may be higher or lower because the underlying and implied volatility rarely stand still.",
        "faq": [("Is theta deducted from my account?", "No. Theta is a model estimate of time-related value change, not a separate cash charge."), ("Does theta apply on every calendar day?", "The market prices the passage of time continuously, but the realized change is not a fixed daily subtraction and can incorporate weekends before they arrive."), ("Can theta be positive?", "A short option position commonly has positive theta because the position may benefit as the option's time value declines.")],
    },
    {
        "slug": "how-time-decay-works-options",
        "tag": "Theta · Core Concept",
        "title": "How Time Decay Works in Options",
        "description": "Understand how an option's extrinsic value erodes, why the path is nonlinear and how expiration changes the balance between opportunity and decay.",
        "key": "Time decay affects extrinsic value; intrinsic value is determined by the relationship between the stock price and strike.",
        "sections": [
            ("Intrinsic value versus time value", "An option premium can contain intrinsic value and extrinsic value. Time decay works on the extrinsic portion. At expiration, an option is worth only its intrinsic value, if any, because no time remains for another favorable move."),
            ("The decay curve", "Decay is not normally linear. Longer-dated options may lose time value gradually, while decay can become more noticeable as expiration approaches, particularly for at-the-money contracts. The exact curve changes with moneyness and implied volatility."),
            ("What changes decay", "A long call or long put can lose value even when the directional thesis is roughly right if the move is too small or too slow. Short-option positions may benefit from decay, but their directional and volatility risk can easily dominate the collected time value."),
            ("A better way to plan", "Match expiration to the expected timing of the thesis, compare several strikes and dates, and model what happens if the move arrives late. Treat the premium as capital at risk, not as a static price tag."),
        ],
        "example": "Two calls share the same strike but expire in 20 and 120 days. The longer contract generally costs more because it contains more time value. The shorter contract may lose a larger percentage of that value each day as expiration nears.",
        "faq": [("Can intrinsic value decay?", "Intrinsic value changes with the underlying price; time decay directly reduces extrinsic value."), ("Does every option decay at the same speed?", "No. Days to expiration, moneyness and implied volatility materially change the decay profile."), ("Can a decaying option still rise?", "Yes. A favorable underlying move or volatility increase can outweigh decay.")],
    },
    {
        "slug": "positive-theta-vs-negative-theta",
        "tag": "Theta · Position Exposure",
        "title": "Positive Theta vs Negative Theta",
        "description": "Compare positions that theoretically benefit from time passing with positions that pay for time, and see why the sign alone does not define risk.",
        "key": "Positive theta can collect decay while carrying substantial price and volatility risk; negative theta can buy convexity or protection.",
        "sections": [
            ("Reading the sign", "Long calls and puts usually carry negative theta. Short calls and puts usually carry positive theta. Multi-leg positions combine the theta of each leg, so their net exposure may be positive, negative or close to neutral."),
            ("What positive theta means", "A positive-theta position may gain theoretical value as time passes if the underlying price, implied volatility and other inputs remain unchanged. It does not mean the trade earns money every day or has a high probability of profit."),
            ("What negative theta buys", "Negative theta is often the cost of maintaining asymmetric upside, downside protection or exposure to a large move. The buyer accepts erosion in exchange for rights without the short option's obligation."),
            ("Compare complete payoffs", "Review maximum profit, maximum loss, breakevens, assignment, gamma and vega together with theta. A small daily credit is not adequate compensation for an undefined tail risk unless the complete position is acceptable."),
        ],
        "example": "A long straddle may have negative theta but can benefit from a large move or higher implied volatility. A short straddle may have positive theta but can lose sharply if the underlying moves far from the strike.",
        "faq": [("Is positive theta always better?", "No. It describes time exposure, not total expected return or risk."), ("Can a spread change theta sign?", "Yes. Moneyness, time and volatility changes can cause a multi-leg position's net theta to cross zero."), ("Why accept negative theta?", "Traders may accept it to obtain defined risk, directional leverage, convexity or portfolio protection.")],
    },
    {
        "slug": "theta-long-options-vs-short-options",
        "tag": "Theta · Buyers & Sellers",
        "title": "Theta in Long Options vs Short Options",
        "description": "See how the same time-value decay creates opposite exposure for option buyers and sellers—and why neither side has a free advantage.",
        "key": "The option buyer owns time-sensitive rights; the option seller receives premium for accepting an obligation and the associated risk.",
        "sections": [
            ("Long-option theta", "A long option normally has negative theta. The buyer needs the underlying move, volatility change or another favorable repricing to offset the gradual loss of extrinsic value."),
            ("Short-option theta", "A short option normally has positive theta. The seller can benefit as extrinsic value falls, but maximum reward is limited to the premium while losses may be large or, for an uncovered call, theoretically unlimited."),
            ("Moneyness matters", "At-the-money options often have the greatest absolute time value and meaningful theta exposure. Deep in-the-money and far out-of-the-money contracts can behave differently because their premium composition and probabilities differ."),
            ("Position-level thinking", "Spreads pair long and short legs, so net theta matters more than any single contract. Calculate the aggregate Greek exposure and reassess it as price, volatility and expiration change."),
        ],
        "example": "If one option has theta of -0.10, the buyer sees roughly -$10 of modeled daily exposure per contract while the seller sees roughly +$10, before price, volatility and transaction effects.",
        "faq": [("Do buyers always lose to theta?", "No. Directional or volatility gains can be larger than decay."), ("Do sellers receive theta as cash?", "No. Sellers receive premium at entry; theta describes how the option may reprice over time."), ("Do spreads have theta?", "Yes. Add the signed theta of every leg to estimate the position's net theta.")],
    },
    {
        "slug": "why-option-time-decay-accelerates",
        "tag": "Theta · Expiration",
        "title": "Why Option Time Decay Accelerates Near Expiration",
        "description": "Learn why the final weeks can change an option's time value rapidly and why the familiar decay curve differs across strikes.",
        "key": "Near expiration, each passing day removes a larger share of the remaining opportunity for an at-the-money option to become profitable.",
        "sections": [
            ("Less time, less possibility", "With months remaining, many price paths are still possible. With only days remaining, the range of plausible outcomes narrows. The market therefore removes the remaining time value more aggressively when other inputs are unchanged."),
            ("At-the-money sensitivity", "At-the-money options often show the clearest acceleration because their expiration outcome is most uncertain. Deep in-the-money options are increasingly intrinsic, while far out-of-the-money options may already have little premium left to lose."),
            ("Theta and gamma", "The approach to expiration can produce high theta and high gamma together. Sellers may collect faster decay but face sharper changes in delta from small underlying moves; buyers pay decay but may own stronger convexity."),
            ("Practical expiration choice", "Do not choose a short expiration only because the premium looks cheap or theta looks large. The trade also has less time to recover, greater sensitivity around the strike and more frequent execution decisions."),
        ],
        "example": "An at-the-money option with 90 days remaining may lose time value gradually. In its final two weeks, the remaining extrinsic value can compress much faster even though the calendar still advances one day at a time.",
        "faq": [("Does decay always accelerate?", "The common acceleration pattern is strongest near the money; deep ITM and far OTM options can follow different curves."), ("When does acceleration begin?", "There is no universal day; it evolves continuously and depends on moneyness and volatility."), ("Is high theta attractive to sellers?", "Only when the accompanying gamma, gap, assignment and liquidity risks are also acceptable.")],
    },
    {
        "slug": "theta-itm-atm-otm-options",
        "tag": "Theta · Moneyness",
        "title": "Theta in ITM, ATM and OTM Options",
        "description": "Compare how time decay behaves for in-the-money, at-the-money and out-of-the-money options as expiration approaches.",
        "key": "At-the-money options often carry the most time value, while ITM and OTM contracts divide premium differently between intrinsic value and probability.",
        "sections": [
            ("At-the-money options", "ATM contracts often have high absolute theta because uncertainty around the strike creates substantial extrinsic value. That value must disappear by expiration if the option finishes exactly at the strike."),
            ("In-the-money options", "An ITM option contains intrinsic value plus possible extrinsic value. Theta erodes only the extrinsic portion, so a deep ITM contract may act more like the underlying and show less percentage decay than a comparable ATM option."),
            ("Out-of-the-money options", "OTM options contain only extrinsic value. Far OTM contracts may have low dollar theta because little premium remains, yet the percentage loss can be severe and the entire premium can expire worthless."),
            ("Compare apples with apples", "Review both dollar theta and theta as a percentage of premium. Also compare delta, bid-ask spread, open interest and the move required to reach breakeven."),
        ],
        "example": "Three options with the same expiration can show very different theta. The ATM contract may lose the most dollars per day, while a cheap far-OTM contract loses a larger percentage of its premium.",
        "faq": [("Which option has the highest theta?", "ATM options often have the greatest absolute theta, though actual values vary by contract and market inputs."), ("Do OTM options have intrinsic value?", "No. Their premium is entirely extrinsic value."), ("Does theta affect ITM options?", "Yes, but it erodes only their extrinsic value, not the intrinsic value created by moneyness.")],
    },
    {
        "slug": "option-theta-weekends-holidays",
        "tag": "Theta · Calendar",
        "title": "Option Theta Over Weekends and Holidays",
        "description": "Understand how markets price non-trading days, why Monday is not simply a three-day theta charge and what event risk can change.",
        "key": "Weekend decay is priced by the market and model conventions; it is not reliably captured by multiplying Friday's displayed theta by the number of calendar days.",
        "sections": [
            ("Calendar time still passes", "Options have less remaining life after a weekend or holiday. Models may use calendar days, trading days or adjusted conventions, while market makers can reprice expected decay before the market closes."),
            ("Why the shortcut fails", "Multiplying displayed theta by three assumes every other input and the decay rate remain fixed. In practice, implied volatility, underlying price, news risk and dealer pricing can change between Friday and Monday."),
            ("Event risk remains", "A closed exchange does not eliminate company, geopolitical or macroeconomic news. Sellers may collect decay but carry gap risk; buyers may lose time value but retain exposure to a weekend surprise."),
            ("Plan around the calendar", "Check expirations, market holidays, earnings, economic releases and ex-dividend dates. Judge the complete risk during the closed period rather than treating the weekend as automatic income."),
        ],
        "example": "A Friday option displaying theta of -0.05 should not automatically be expected to open $0.15 lower Monday. Some weekend effect may already be embedded, and a price or volatility move can dominate.",
        "faq": [("Does theta decay on Saturday and Sunday?", "Time passes, but market prices do not update continuously and weekend decay can be reflected before or after the weekend."), ("Is selling options before weekends free profit?", "No. Gap, volatility and directional risks remain."), ("Do holidays matter?", "Yes. They reduce trading sessions and may alter how the market prices remaining time and event exposure.")],
    },
    {
        "slug": "theta-vs-implied-volatility",
        "tag": "Theta · Volatility",
        "title": "Theta vs Implied Volatility: How They Interact",
        "description": "Separate time decay from volatility repricing and understand why an option can gain value despite negative theta—or fall despite positive theta.",
        "key": "Theta assumes implied volatility is unchanged, but real option prices reflect time and volatility simultaneously.",
        "sections": [
            ("Two different inputs", "Theta estimates sensitivity to time; vega estimates sensitivity to implied volatility. They describe different parts of the pricing model even though both affect extrinsic value."),
            ("Higher volatility, more time value", "Higher implied volatility generally increases option premiums because a wider range of future outcomes is being priced. That can create more extrinsic value available to decay, but also more volatility risk."),
            ("When vega overwhelms theta", "A long option can rise while time passes if implied volatility increases enough. A short option can lose even with positive theta if volatility expands or the underlying moves sharply."),
            ("Event-driven repricing", "Ahead of earnings or major announcements, volatility may rise; afterward, it can fall abruptly. Compare implied volatility with the event's expected move and avoid attributing every premium change to theta."),
        ],
        "example": "A long option loses $0.07 of modeled theta but gains $0.40 from a volatility expansion and price movement. Its net market value rises even though its theta is negative.",
        "faq": [("Are theta and vega the same?", "No. Theta measures time sensitivity; vega measures implied-volatility sensitivity."), ("Does high IV mean faster decay?", "High IV can create more extrinsic value, but the exact theta relationship depends on strike, time and other inputs."), ("What is volatility crush?", "It is a rapid fall in implied volatility that can reduce option premiums, often after a known event passes.")],
    },
    {
        "slug": "theta-vs-gamma-near-expiration",
        "tag": "Theta · Gamma Risk",
        "title": "Theta vs Gamma Near Expiration",
        "description": "Understand the tradeoff between faster time decay and faster delta changes when options approach expiration.",
        "key": "Near expiration, attractive theta for sellers can arrive with concentrated gamma risk around the strike.",
        "sections": [
            ("What gamma changes", "Gamma estimates how much delta changes when the underlying price changes. High gamma means the position's directional exposure can shift rapidly, especially near the strike."),
            ("The theta-gamma tradeoff", "Short options may collect faster decay near expiration but are typically short gamma. Long options pay decay but own gamma. The two exposures help explain why steady small gains can be interrupted by a sharp move."),
            ("Pin risk and late movement", "When the underlying finishes near a strike, small late moves can change whether an option expires in or out of the money. Exercise, assignment and after-hours movement can complicate the result."),
            ("Risk controls", "Size for a sudden move, understand automatic exercise procedures, monitor liquidity and avoid relying on a static delta. Closing before expiration can remove some operational uncertainty but may require paying the spread."),
        ],
        "example": "A near-expiration short option may show attractive positive theta. A small move toward or through the strike can rapidly increase its delta and loss because gamma is concentrated.",
        "faq": [("Why are theta and gamma linked?", "Both reflect how option value changes as time and price interact, particularly near expiration."), ("Is high gamma good?", "It benefits some long-option convexity but increases instability and risk for short-gamma positions."), ("What is pin risk?", "It is uncertainty around exercise and assignment when the underlying closes near the strike.")],
    },
    {
        "slug": "theta-0dte-weekly-options",
        "tag": "Theta · Short-Dated Options",
        "title": "Theta in 0DTE and Weekly Options",
        "description": "Learn why short-dated options combine rapid time decay with extreme price sensitivity, execution risk and little recovery time.",
        "key": "A large theta number in a very short-dated option is inseparable from concentrated gamma, spread and intraday-move risk.",
        "sections": [
            ("What short-dated means", "Weekly options expire within a short window; 0DTE options expire the same trading day. Their premium can change quickly because the time remaining is measured in hours rather than weeks or months."),
            ("Intraday theta", "A single daily theta figure is a rough snapshot. Decay occurs through the session and can be nonlinear, while the underlying and implied volatility continuously reshape the option's value."),
            ("Gamma and execution", "Near-the-money 0DTE options can have intense gamma. Bid-ask spreads, slippage, fast markets and delayed orders can materially alter a trade that appears precise in a payoff diagram."),
            ("Defined-risk planning", "Use position sizes that can tolerate a rapid loss, understand settlement and cutoff rules, and define exits before entry. Premium collected is not a reliable measure of the worst intraday move."),
        ],
        "example": "A same-day option can lose much of its time value during a quiet afternoon, then reprice sharply after a small late move because the probability of finishing in the money changes quickly.",
        "faq": [("Does 0DTE have the highest theta?", "Short-dated ATM options can have intense decay, but comparing raw theta without premium and gamma can mislead."), ("Can 0DTE lose more than the premium?", "A long option is generally limited to premium; an uncovered short option can have much larger losses."), ("Is decay constant intraday?", "No. Theoretical exposure changes continuously with price, volatility and remaining time.")],
    },
    {
        "slug": "theta-leaps-long-term-options",
        "tag": "Theta · LEAPS",
        "title": "Theta in LEAPS and Long-Term Options",
        "description": "See why long-dated options usually decay more slowly per day yet can carry substantial premium, vega exposure and capital risk.",
        "key": "More time can reduce near-term theta pressure, but it also costs more and creates longer exposure to volatility and thesis risk.",
        "sections": [
            ("Longer life, slower daily erosion", "A long-dated option generally loses a smaller proportion of its time value each day than a similar short-dated contract. The holder buys more time for the thesis to develop."),
            ("More premium at risk", "Slower daily decay does not make LEAPS cheap. Their larger absolute premium can produce a meaningful dollar loss if the thesis fails, volatility declines or the option is closed early."),
            ("Vega matters more", "Longer-dated options often have greater sensitivity to implied-volatility changes. A decline in volatility can offset the benefit of slower theta, while an increase can support the premium."),
            ("Strike and liquidity", "Compare delta, intrinsic value, bid-ask spread and open interest. Deep ITM LEAPS may provide higher delta and less extrinsic value, but capital requirements and execution still matter."),
        ],
        "example": "A 15-month call may show modest daily theta compared with a 30-day call. It can still lose significantly if implied volatility falls or the stock remains below the strike for months.",
        "faq": [("Do LEAPS have theta?", "Yes. Their time value decays, usually more slowly at first and faster as expiration approaches."), ("Are LEAPS safer than short-term options?", "They provide more time but can require more premium and still expire worthless."), ("Why choose a deep ITM LEAPS?", "Some traders seek higher delta and less extrinsic value, but cost, liquidity and downside exposure remain important.")],
    },
    {
        "slug": "calculate-option-time-decay-theta",
        "tag": "Theta · Calculation",
        "title": "How to Calculate Option Time Decay Using Theta",
        "description": "Translate a quoted theta into estimated daily dollar exposure and avoid the common mistakes of treating it as a fixed forecast.",
        "key": "Multiply per-share theta by the contract multiplier and position quantity, then remember that the result is only a changing model estimate.",
        "sections": [
            ("Read the quote", "Theta is usually displayed as a per-share value. For a standard U.S. equity option representing 100 shares, multiply the quoted theta by 100 and by the number of contracts."),
            ("Keep the sign", "A long option with theta -0.05 has about -$5 of modeled one-day exposure per contract. The same contract sold short contributes about +$5 before any hedge or other leg."),
            ("Add every leg", "For a spread, calculate signed theta for each leg and add them. Contract ratios matter: two short contracts contribute twice the exposure of one otherwise identical contract."),
            ("Recalculate often", "Theta changes as the underlying, implied volatility and expiration change. Do not multiply today's theta by 30 to forecast next month's option price; the exposure itself will not remain constant."),
        ],
        "example": "Three long contracts each show theta of -0.04: -0.04 × 100 × 3 = about -$12 of modeled daily time exposure. A separate short contract with +$7 of position theta would bring net theta to about -$5.",
        "faq": [("Why multiply theta by 100?", "Standard equity option quotes are per share while one contract normally represents 100 shares; verify each contract's multiplier."), ("Can I multiply theta by days remaining?", "That is usually inaccurate because theta changes over time and other pricing inputs move."), ("Where can I find theta?", "Many broker option chains and analytic platforms display it, often alongside delta, gamma and vega.")],
    },
    {
        "slug": "positive-theta-option-strategies",
        "tag": "Theta · Strategies",
        "title": "Positive Theta Option Strategies for Sellers",
        "description": "Compare defined- and undefined-risk ways to seek time decay while keeping direction, volatility and assignment risk in view.",
        "key": "Positive theta is a source of exposure, not a strategy guarantee; the payoff and worst-case loss matter more than the daily estimate.",
        "sections": [
            ("Single short options", "Covered calls and cash-secured puts can produce positive theta while retaining stock downside or assignment exposure. Uncovered calls and puts may require less capital but can create much greater margin and tail risk."),
            ("Credit spreads", "Vertical credit spreads combine a short option with a farther out-of-the-money long option. They can retain positive theta while defining maximum loss, although the long leg reduces the net credit and decay collected."),
            ("Range strategies", "Iron condors and other multi-leg structures may seek decay within a range. Their risk depends on strike placement, width, premium, volatility, correlation between legs and management rules."),
            ("Select risk before theta", "Start with the market view and acceptable maximum loss. Then compare liquidity, event exposure, breakevens and position Greeks. Do not maximize theta by concentrating risk near expiration or near the money without a reason."),
        ],
        "example": "A credit spread collects less theta than an uncovered short option but caps the expiration loss. The reduced daily credit is the cost of limiting tail exposure.",
        "faq": [("Which strategy has the most theta?", "The largest theta is not automatically best because it can accompany large gamma, volatility and loss exposure."), ("Are covered calls risk-free?", "No. The stock can fall substantially, while the call caps some upside."), ("Do credit spreads always have positive theta?", "Often, but their net theta can change with price, time and volatility.")],
    },
    {
        "slug": "reduce-time-decay-option-buyers",
        "tag": "Theta · Buyer Tactics",
        "title": "How Option Buyers Can Reduce Time Decay",
        "description": "Use expiration, strike, timing, spreads and exit rules to control theta without pretending that time risk can be eliminated.",
        "key": "Buy enough time for the thesis, but do not pay for time that the plan does not need.",
        "sections": [
            ("Choose a realistic expiration", "The option should extend beyond the expected catalyst or move, allowing room for timing error. Very short expirations may be cheap in dollars but expensive in daily percentage decay."),
            ("Consider moneyness", "Higher-delta or in-the-money options often contain a greater intrinsic-value share and may experience less percentage decay than far-OTM lottery-like contracts. They also cost more upfront."),
            ("Use spreads deliberately", "Selling another option against the long contract can offset some negative theta. The tradeoff is capped profit, additional legs, assignment considerations and more complex management."),
            ("Control holding time", "Define the catalyst, invalidation point and latest acceptable exit before entry. Closing after the thesis fails can preserve remaining time value instead of waiting for expiration."),
        ],
        "example": "A buyer expecting a development within six weeks compares a two-month and a six-month option. The longer contract decays more slowly but costs more; the correct choice depends on timing uncertainty, volatility and budget.",
        "faq": [("Can buyers eliminate theta?", "Not entirely while owning time value, though spreads and strike selection can reduce net exposure."), ("Are longer expirations always better?", "No. They cost more and may carry greater vega exposure."), ("Why avoid far-OTM options?", "They can be inexpensive but may require a large fast move and can lose 100% of premium.")],
    },
    {
        "slug": "theta-time-decay-mistakes",
        "tag": "Theta · Risk Management",
        "title": "Theta and Time Decay: 10 Mistakes to Avoid",
        "description": "Avoid the most common errors involving fixed daily decay, weekends, expiration, cheap options, premium selling and Greek isolation.",
        "key": "Theta is useful only when it is interpreted as a changing model sensitivity inside the complete option position.",
        "sections": [
            ("Mistakes 1–3: treating theta as certain", "Do not treat theta as a guaranteed daily debit, multiply it mechanically by days remaining or assume weekend decay equals several identical weekday charges. Theta changes and markets price time alongside every other input."),
            ("Mistakes 4–5: ignoring price and volatility", "Do not attribute every option change to decay or ignore vega around an event. Underlying movement and implied-volatility repricing can overwhelm theta."),
            ("Mistakes 6–8: choosing contracts by decay alone", "Do not buy a very short option only because it is cheap, sell the highest-theta contract without checking gamma, or ignore moneyness. Compare the complete payoff, probability, liquidity and maximum loss."),
            ("Mistakes 9–10: forgetting execution and size", "Do not overlook bid-ask spreads and do not scale a position from premium received alone. Slippage, assignment, contract multipliers and tail losses can exceed many days of expected decay."),
        ],
        "example": "A trader sells a high-theta option just before expiration and expects easy decay. A small stock move sharply changes delta because gamma is high, producing a loss far larger than the anticipated daily credit.",
        "faq": [("What is the biggest theta mistake?", "Treating a model estimate as guaranteed income or loss."), ("Is high theta a reason to sell?", "Not by itself; it may reflect concentrated expiration and gamma risk."), ("How often should theta be reviewed?", "Whenever price, volatility, time or the position structure changes materially.")],
    },
]


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def article_html(article: dict, index: int) -> str:
    related = [ARTICLES[(index + offset) % len(ARTICLES)] for offset in (1, 4, 9)]
    schema_article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article["title"],
        "description": article["description"],
        "datePublished": "2026-09-11",
        "dateModified": "2026-09-11",
        "author": {"@type": "Organization", "name": "Options America"},
        "publisher": {"@type": "Organization", "name": "Options America"},
        "mainEntityOfPage": f"https://options-america.onrender.com/blog/{article['slug']}/",
    }
    schema_faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in article["faq"]
        ],
    }
    sections = "\n".join(
        f'          <h2 id="s{num}">{esc(title)}</h2>\n          <p>{esc(body)}</p>'
        for num, (title, body) in enumerate(article["sections"], 1)
    )
    faqs = "\n".join(
        f'          <div class="faq-item"><h3>{esc(q)}</h3><p>{esc(a)}</p></div>'
        for q, a in article["faq"]
    )
    related_links = " · ".join(
        f'<a href="../{item["slug"]}/"><strong>{esc(item["title"])}</strong></a>' for item in related
    )
    toc = "\n".join(
        f'            <a href="#s{num}">{esc(title)}</a>' for num, (title, _) in enumerate(article["sections"], 1)
    )
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{esc(article['title'])} | Options America</title>
  <meta name="description" content="{esc(article['description'])}">
  <link rel="canonical" href="https://options-america.onrender.com/blog/{article['slug']}/">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{esc(article['title'])}">
  <meta property="og:description" content="{esc(article['description'])}">
  <meta property="og:image" content="https://options-america.onrender.com/assets/images/blog/{article['slug']}.webp">
  <link rel="stylesheet" href="../../styles.css"><link rel="stylesheet" href="../blog.css"><script src="/favicon.js"></script>
  <script type="application/ld+json">{json.dumps(schema_article, ensure_ascii=False, separators=(',', ':'))}</script>
  <script type="application/ld+json">{json.dumps(schema_faq, ensure_ascii=False, separators=(',', ':'))}</script>
</head>
<body>
  <header class="site-header"><div class="container nav"><a class="brand" href="../../"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><nav><a href="../../courses/">Courses</a><a href="../../#paths">Learning Paths</a><a href="../../#strategies">Strategies</a><a href="../../#futures">Options on Futures</a><a href="../">Blog</a><a href="../../#resources">Resources</a></nav><a class="btn btn-gold" href="{COURSE}">Learn Theta — Free</a></div></header>
  <main>
    <section class="article-hero"><div class="container"><div class="breadcrumbs"><a href="../../">Home</a><span>›</span><a href="../">Blog</a><span>›</span><span>Theta &amp; Time Decay</span></div><p class="eyebrow">{esc(article['tag'])}</p><h1>{esc(article['title'])}</h1><p class="article-deck">{esc(article['description'])}</p><div class="article-meta"><span>By Options America</span><span>Updated {DATE}</span><span>9-minute read</span></div></div></section>
    <div class="container article-layout">
      <article class="article-body">
        <img src="../../assets/images/blog/{article['slug']}.webp" alt="{esc(article['title'])}">
        <p>{esc(article['description'])}</p>
        <div class="article-callout"><strong>Key idea:</strong> {esc(article['key'])}</div>
{sections}
        <h2 id="example">A practical example</h2>
        <div class="example-box"><strong>Theta planning example</strong><p>{esc(article['example'])}</p></div>
        <p>The example isolates time so the concept is easy to see. A live option position must also account for the underlying price, implied volatility, dividends, rates, liquidity and transaction costs. Greeks are estimates, not guarantees.</p>
        <h2 id="faq">Frequently asked questions</h2>
{faqs}
        <h2>Continue the Theta &amp; Time Decay cluster</h2>
        <p>Explore related guides: {related_links}. For a structured sequence, use the free <a href="{COURSE}"><strong>Level 5 – Theta &amp; Time Decay course</strong></a>.</p>
        <p><a class="btn btn-gold" href="{COURSE}">Start Level 5 — Free →</a></p>
        <p class="article-disclaimer">Options involve risk and are not suitable for every investor. This material is educational and is not investment, tax or legal advice. Greeks are theoretical estimates, and contract terms and broker requirements can vary.</p>
      </article>
      <aside class="article-sidebar"><div class="toc"><strong>In this guide</strong>
{toc}
        <a href="#example">Practical example</a><a href="#faq">FAQs</a></div><div class="course-cta"><strong>Free Level 5 Course</strong><p>Learn theta and time decay through structured lessons and practical examples.</p><a class="btn btn-gold" href="{COURSE}">Start the course →</a></div></aside>
    </div>
  </main>
  <footer><div class="container footer-grid"><div><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><p>The free resource for learning options trading from beginner to advanced.</p></div><div><h4>Learn</h4><a href="/courses/">Courses</a><a href="/learning-paths/beginner/">Beginner Path</a></div><div><h4>Strategies</h4><a href="/#strategies">All Strategies</a><a href="/learning-paths/option-greeks/">Option Greeks</a></div><div><h4>Futures</h4><a href="/learning-paths/options-on-futures/">Options on Futures</a></div><div><h4>Resources</h4><a href="/blog/">Blog</a><a href="/courses/">Course Library</a></div></div><div class="container copyright">© <span data-current-year></span> Options America · Educational content only — not financial advice.</div></footer>
  <script>document.querySelectorAll('[data-current-year]').forEach(e=>e.textContent=new Date().getFullYear())</script>
</body>
</html>
'''


def card_html(article: dict) -> str:
    return f'        <a class="post-card" href="{article["slug"]}/"><img src="../assets/images/blog/{article["slug"]}.webp" alt="{esc(article["title"])}"><div class="post-card-copy"><span class="tag">{esc(article["tag"])}</span><h2>{esc(article["title"])}</h2><p>{esc(article["description"])}</p><strong>Read the guide →</strong></div></a>'


def update_index() -> None:
    path = BLOG / "index.html"
    source = path.read_text()
    marker = "      </div>\n      <div class=\"blog-empty\""
    if 'href="what-is-theta-in-options/"' not in source:
        cards = "\n".join(card_html(article) for article in ARTICLES)
        source = source.replace(marker, f"{cards}\n{marker}", 1)
    source = source.replace("<strong>60</strong> guides", "<strong>75</strong> guides")
    if "Explore Level 5" not in source:
        source = source.replace(
            '<a class="btn btn-gold" href="../courses/options-trading-level-4-selling-put-option-strategy/">Explore Level 4 →</a>',
            '<a class="btn btn-gold" href="../courses/options-trading-level-4-selling-put-option-strategy/">Explore Level 4 →</a><a class="btn btn-gold" href="../courses/option-greeks-level-5-theta-time-decay/">Explore Level 5 →</a>',
        )
    path.write_text(source)


def update_scripts() -> None:
    blog_js = BLOG / "blog.js"
    source = blog_js.read_text()
    old = "const clusterPriority = card => card.textContent.includes('Selling Puts') ? 4 :"
    new = "const clusterPriority = card => card.textContent.includes('Theta') ? 5 : card.textContent.includes('Selling Puts') ? 4 :"
    source = source.replace(old, new)
    blog_js.write_text(source)

    favicon = ROOT / "favicon.js"
    source = favicon.read_text()
    marker = "    'selling-put-margin-buying-power': '/assets/images/blog/selling-put-margin-buying-power.webp'"
    additions = ",\n".join(
        f"    '{article['slug']}': '/assets/images/blog/{article['slug']}.webp'" for article in ARTICLES
    )
    if "'what-is-theta-in-options'" not in source:
        source = source.replace(marker, marker + ",\n" + additions)
    favicon.write_text(source)


def main() -> None:
    for index, article in enumerate(ARTICLES):
        directory = BLOG / article["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(article_html(article, index))
    update_index()
    update_scripts()


if __name__ == "__main__":
    main()
