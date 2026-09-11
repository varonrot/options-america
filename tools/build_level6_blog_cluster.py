#!/usr/bin/env python3
"""Build the Level 6 Vega & Volatility SEO cluster."""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"
COURSE = "../../courses/options-trading-course-level-6-vega-and-volatility/"
DATE = "September 11, 2026"


def guide(slug, tag, title, description, key, sections, example, faq):
    return dict(slug=slug, tag=f"Vega · {tag}", title=title, description=description,
                key=key, sections=sections, example=example, faq=faq)


ARTICLES = [
guide("what-is-vega-in-options", "Beginner", "What Is Vega in Options?",
"Learn what option vega measures, how a one-point change in implied volatility can affect premium, and why vega is an estimate rather than a promise.",
"Vega estimates the change in an option's theoretical value for a one-percentage-point change in implied volatility, with other inputs held constant.", [
("Vega in plain English", "Vega is one of the option Greeks. If an option has vega of 0.12, a rise in implied volatility from 25% to 26% would add about $0.12 per share to theoretical value, all else equal. A standard equity contract would therefore show roughly $12 of modeled exposure."),
("Why volatility changes premium", "Greater implied volatility represents a wider range of possible future prices. That wider distribution increases the chance an option finishes with meaningful intrinsic value, so both calls and puts generally become more valuable when implied volatility rises."),
("How to use vega", "Compare vega with delta, gamma and theta, then multiply by the contract multiplier and position size. Vega changes with strike, expiration, price and volatility, so recalculate it as the position evolves rather than treating the opening quote as fixed."),
], "A call priced at $3.20 has vega of 0.15. If implied volatility rises two points and everything else is unchanged, its theoretical value may rise about $0.30 to $3.50. A stock move or a day of decay can make the actual result different.",
[("Is vega the same as volatility?", "No. Implied volatility is a pricing input; vega estimates sensitivity to a change in that input."),("Can puts and calls both have positive vega?", "Yes. Long calls and long puts normally have positive vega."),("Is vega guaranteed?", "No. It is a model sensitivity that assumes other inputs remain unchanged.")]),

guide("implied-volatility-options-explained", "Core Concept", "Implied Volatility in Options Explained",
"Understand what implied volatility says about option prices, expected movement and uncertainty—and what it does not predict.",
"Implied volatility is the volatility input consistent with current option prices; it reflects magnitude, not the direction, of possible movement.", [
("A price-derived expectation", "Implied volatility is backed out of option prices through a pricing model. It is forward-looking in the limited sense that current premiums embed the market's uncertainty about future movement. It is not a direct forecast of where the stock will finish."),
("Movement without direction", "High implied volatility means the market is pricing a wider distribution of possible outcomes. It does not say bullish or bearish. Calls and puts can both become more expensive when uncertainty rises, even if the stock has barely moved."),
("Using IV responsibly", "Compare implied volatility across expirations and strikes, against the same underlying's own history, and around known events. Absolute IV levels differ between assets, so a number that is elevated for one stock may be ordinary for another."),
], "Two stocks both trade at $100, but one has a major announcement approaching. Its options may carry higher implied volatility and premium because the market prices a wider range of outcomes—not because it knows whether the announcement will be good or bad.",
[("Does high IV predict a decline?", "No. It indicates expected movement magnitude, not direction."),("Is IV historical volatility?", "No. Historical volatility measures realized past movement; IV is inferred from current option prices."),("Why does IV differ by strike?", "Supply, demand and perceived tail risk create a volatility surface rather than one uniform number.")]),

guide("vega-long-options-vs-short-options", "Position Exposure", "Vega in Long Options vs Short Options",
"See why option buyers are usually long vega, sellers are usually short vega, and neither exposure is automatically superior.",
"Long options generally benefit from rising implied volatility; short options generally benefit from falling implied volatility, all else equal.", [
("Long-option vega", "A purchased call or put usually has positive vega. Rising implied volatility can support its premium, while declining implied volatility can hurt it even when the directional thesis is roughly correct."),
("Short-option vega", "A written call or put normally has negative vega. Falling IV may help the seller, but a sudden volatility expansion can create losses alongside adverse delta and gamma exposure. Premium received is not the same as maximum risk."),
("Net vega matters", "Multi-leg positions combine the signed vega of every leg. A spread can be positive, negative or nearly neutral, and that exposure changes as the underlying moves and expiration approaches."),
], "One long option with vega 0.18 creates about +$18 of exposure per volatility point. Selling another option with vega 0.11 leaves net vega near +$7 per point, before quantity adjustments.",
[("Are buyers always long vega?", "A standalone long option normally is, though a multi-leg trade may have different net exposure."),("Do sellers receive vega?", "No. Vega is a sensitivity, not a cash payment."),("Can net vega change sign?", "Yes. Price, time, volatility and unequal legs can change the balance.")]),

guide("positive-vega-vs-negative-vega", "Risk Profile", "Positive Vega vs Negative Vega",
"Compare volatility-seeking and volatility-selling positions, including their likely benefits, tradeoffs and risk controls.",
"The sign of vega describes the direction of volatility exposure—not the quality, probability or total risk of a trade.", [
("Positive vega", "Positive-vega positions can gain theoretical value when IV rises. Long straddles, strangles and calendars may begin with positive vega, but they can pay theta and still require the magnitude and timing of movement to justify their cost."),
("Negative vega", "Negative-vega positions may benefit as IV falls. Short options and many credit structures carry this exposure, but volatility often rises during sharp adverse moves, which can combine vega losses with directional losses."),
("Choose exposure deliberately", "Start with the volatility thesis, event calendar and maximum acceptable loss. Then compare theta, gamma, skew and liquidity. A positive or negative vega number by itself cannot reveal the full payoff."),
], "A long straddle has positive vega and negative theta; a short straddle has negative vega and positive theta. Their opposite signs reveal a tradeoff between owning movement insurance and collecting premium while accepting tail risk.",
[("Is positive vega bullish?", "Not necessarily. It is bullish on implied volatility, not on stock direction."),("Is negative vega always risky?", "Every exposure carries risk; short volatility can be especially vulnerable to rapid expansions."),("Can stock positions have vega?", "Stock itself does not have option vega, though a stock-plus-options portfolio can.")]),

guide("calculate-option-vega", "Calculation", "How to Calculate Option Vega",
"Turn the vega shown in an option chain into estimated dollar exposure for one contract, multiple contracts and spreads.",
"Multiply quoted per-share vega by the volatility-point change, contract multiplier and signed quantity.", [
("Read the chain", "Broker platforms commonly display vega per share. A quoted vega of 0.09 means roughly nine cents of theoretical premium change for a one-point IV move, such as 30% to 31%, assuming the other inputs do not move."),
("Scale the exposure", "For a standard 100-share equity contract, 0.09 vega equals about $9 per volatility point. Five long contracts create approximately +$45 per point. Short contracts reverse the sign."),
("Add every leg", "Calculate each leg using its own vega and quantity, then sum the results. Recompute scenario outcomes for several IV changes because vega itself changes and large moves are not perfectly linear."),
], "Two long contracts show vega 0.14 and one short contract shows vega 0.08. Net exposure is (2 × 0.14 − 0.08) × 100, or about +$20 for a one-point IV increase.",
[("Why is a 1% IV change called one point?", "A move from 20% to 21% is one percentage point, not a one-percent relative increase."),("Can I multiply vega by any IV move?", "It is a useful first approximation for small moves; larger moves require repricing."),("Why does broker vega differ?", "Models, inputs, timestamps and conventions can differ.")]),

guide("vega-itm-atm-otm-options", "Moneyness", "Vega in ITM, ATM and OTM Options",
"Compare implied-volatility sensitivity across in-the-money, at-the-money and out-of-the-money contracts.",
"Vega is often greatest near the money, where uncertainty about the option's expiration outcome is most consequential.", [
("At-the-money options", "ATM options usually have substantial extrinsic value and strong sensitivity to a wider or narrower distribution of future prices. That often produces higher vega than comparable deep ITM or far OTM contracts."),
("In- and out-of-the-money options", "Deep ITM options contain more intrinsic value and can behave more like stock. Far OTM options may have low dollar vega but can still experience large percentage changes because their premiums are small."),
("Read the whole surface", "Vega varies by strike, and IV itself can vary through skew or smile. Compare both the Greek and the implied volatility at each strike instead of assuming one underlying has a single uniform volatility."),
], "Three calls share an expiration. The ATM call may show the largest dollar vega, while the far-OTM call has lower vega but a bigger percentage premium reaction to the same volatility change.",
[("Which strike has the highest vega?", "It is commonly near the money, though dividends, rates and market conditions can shift the exact peak."),("Do deep ITM options have vega?", "Yes, generally less than a comparable ATM option."),("Can low vega still matter?", "Yes, especially across many contracts or relative to a small premium.")]),

guide("vega-expiration-long-term-short-term-options", "Expiration", "Vega by Expiration: Long-Term vs Short-Term Options",
"Learn why longer-dated options generally carry more vega and how short-dated event risk can complicate the comparison.",
"More time usually creates greater sensitivity to changes in the volatility assumption, so long-dated options often have higher vega.", [
("Why time increases vega", "A volatility change applied across many remaining days meaningfully changes the distribution of possible expiration prices. Longer-dated options therefore commonly respond more in dollar terms to a one-point IV move."),
("Short-term exceptions", "A near-term earnings or product event can concentrate high implied volatility in one expiration. The short-dated option may have lower vega but still undergo a very large IV move when the event passes."),
("Term structure", "Compare implied volatility and vega across the expiration curve. Calendar spreads depend on relative repricing between two maturities, not merely the fact that the back-month leg has more vega."),
], "A 30-day option has vega 0.08 while a 180-day option has vega 0.22. A two-point parallel IV rise implies roughly +$16 versus +$44 per contract, but their IV levels may not move in parallel.",
[("Do LEAPS have high vega?", "They often have greater dollar vega because much more time remains."),("Does vega fall near expiration?", "It generally declines as time runs out, though event repricing can still be powerful."),("Do all expirations share one IV?", "No. The term structure can price different risks at different dates.")]),

guide("historical-vs-implied-volatility", "Comparison", "Historical Volatility vs Implied Volatility",
"Separate realized past movement from the volatility embedded in current option premiums and use the comparison carefully.",
"Historical volatility describes what happened; implied volatility is inferred from what options cost now.", [
("Historical volatility", "Historical or realized volatility is calculated from past price returns over a chosen window. A 20-day reading and a one-year reading can differ because they summarize different market regimes."),
("Implied volatility", "IV is the volatility input that reconciles a model with current option prices. It reflects forward uncertainty, event risk and supply-demand effects, so it does not need to match recent realized movement."),
("Comparing the two", "The gap can help frame a question about whether options appear expensive or cheap relative to recent movement, but it is not an automatic trade signal. Future realized volatility is unknown, and IV often includes compensation for tail risk."),
], "A stock realized 18% volatility over the past month while its options imply 32% ahead of earnings. The gap may reflect the approaching event rather than a simple pricing error.",
[("Which measure predicts the future?", "Neither is a guaranteed forecast; IV reflects current forward-looking pricing while historical volatility is backward-looking."),("What window should I use for historical volatility?", "Match the window to the horizon being studied and test several regimes."),("Is IV usually higher?", "It often includes a risk premium, but the relationship changes over time.")]),

guide("iv-rank-vs-iv-percentile", "Metrics", "IV Rank vs IV Percentile",
"Learn how two popular volatility metrics differ, what each denominator means and why platform definitions must be checked.",
"IV rank measures location within a range; IV percentile measures how often past observations were below the current reading.", [
("IV rank", "A common IV-rank formula compares current IV with the period's minimum and maximum. One extreme observation can stretch the range and make otherwise elevated readings look modest."),
("IV percentile", "A common percentile calculation counts the percentage of observations below current IV. It uses the distribution of daily values, so it may remain high even when an old spike makes IV rank low."),
("Platform differences", "Brokers may use different lookback windows, reference strikes or definitions. Verify methodology before comparing symbols or tools, and pair either metric with the event calendar, term structure and skew."),
], "Current IV sits above most daily readings from the last year but far below one exceptional spike. IV percentile can be high while IV rank is moderate because the two metrics answer different questions.",
[("Is IV rank a percentage?", "It is commonly scaled from 0 to 100 within a chosen high-low range."),("Can rank and percentile disagree?", "Yes, especially after an extreme outlier."),("Which is better?", "Neither is universally better; understand the calculation and use context.")]),

guide("volatility-crush-options", "Events", "What Is Volatility Crush in Options?",
"Understand why option premiums can fall after a known event even when the underlying moves in the expected direction.",
"Volatility crush is a rapid decline in implied volatility when uncertainty resolves, reducing option extrinsic value through negative vega exposure.", [
("Before the event", "Earnings, regulatory decisions and major announcements can widen the distribution of expected outcomes. Buyers bid for optionality, and market makers may demand more premium to warehouse gap risk, raising IV."),
("After uncertainty resolves", "Once the result is known, the next session no longer contains that binary event. IV can fall sharply and remove extrinsic value from both calls and puts, even though time to expiration remains."),
("Managing crush risk", "Compare the move implied by option prices with the move your thesis requires. Model price and IV changes together, consider defined-risk spreads, and size long premium so a correct direction with an insufficient move is survivable."),
], "A trader buys a call before earnings. The stock rises 3%, but options had priced a 7% move and IV collapses afterward. Delta gains may be smaller than the combined vega and theta loss, leaving the call down.",
[("Does IV always fall after earnings?", "It commonly falls when event uncertainty disappears, but the size is not guaranteed."),("Can sellers lose during a crush?", "Yes. A stock move can overwhelm the benefit from falling IV."),("Do spreads avoid crush?", "They can reduce net vega but introduce caps, multiple legs and other risks.")]),

guide("vega-around-earnings", "Earnings", "Vega and Implied Volatility Around Earnings",
"Plan for the rise, skew and post-event reset of implied volatility around a company earnings announcement.",
"Earnings trades are joint bets on direction, move magnitude, volatility repricing and execution—not direction alone.", [
("The pre-earnings build", "Near-term IV often rises as the announcement approaches because one overnight move can dominate the expiration's risk. That premium is concentrated in expirations containing the event and may differ across puts and calls."),
("Expected move versus forecast", "Option prices can be used to approximate the movement being priced, but that range is not a certainty. A trader needs the realized move and volatility change to compare favorably with the premium paid or risk accepted."),
("After the release", "The event premium usually resets once results are public. Long-vega positions can suffer a crush; short-vega positions can benefit but face gap risk. Liquidity and spreads may also change at the open."),
], "A straddle costs $9 before earnings, reflecting substantial expected movement. A $5 stock move can still disappoint a long-premium buyer if IV falls sharply, while a $14 gap can overwhelm a premium seller.",
[("Why is near-term IV high before earnings?", "That expiration contains a concentrated company-specific uncertainty."),("Is buying before earnings always expensive?", "Premium often reflects the event, but relative value requires comparing price with plausible outcomes."),("Can I isolate vega?", "Not perfectly; delta, gamma, theta and execution all act together.")]),

guide("vega-vs-theta-options", "Greek Tradeoff", "Vega vs Theta in Options",
"Understand the tension between volatility exposure and time decay in long and short option positions.",
"Vega measures sensitivity to implied volatility; theta measures sensitivity to passing time, and both reshape extrinsic value simultaneously.", [
("Different clocks", "Theta estimates the effect of one day passing with other inputs fixed. Vega estimates the effect of a one-point IV change. A real option can gain from one exposure and lose from the other during the same session."),
("Long and short premium", "Long options often combine positive vega with negative theta: they benefit from volatility expansion but pay to wait. Short options often combine negative vega with positive theta: they collect decay but are vulnerable to expansion."),
("Strategy balances", "Calendars, diagonals and vertical spreads blend different vega and theta amounts. Evaluate net Greeks under several stock prices and dates because the relationship changes materially as expiration approaches."),
], "A long option loses an estimated $6 from a day of theta but gains $18 from a two-point IV rise. The volatility gain outweighs decay before considering delta and gamma.",
[("Can vega offset theta?", "Yes. A sufficient IV rise can offset time decay in a long option."),("Does positive theta mean negative vega?", "Often for simple short-premium positions, but not as a universal rule for complex spreads."),("Which Greek matters more?", "It depends on the position, horizon, price move and volatility change.")]),

guide("vega-neutral-option-strategies", "Portfolio", "Vega-Neutral Option Strategies",
"Learn how traders approximate zero net vega, why neutrality is temporary and which risks remain after hedging volatility exposure.",
"Vega neutrality offsets current first-order IV sensitivity; it does not eliminate volatility, price, skew, gamma or model risk.", [
("Building the hedge", "Add signed vega across every leg and adjust contract ratios until the total is near zero. Because expirations and strikes respond differently, a zero sum assumes a particular pattern of volatility changes."),
("Why neutrality drifts", "Vega changes as price, time and IV change. Different points on the volatility surface rarely move in perfect parallel, so a position neutral to a broad IV shift can still lose from skew or term-structure movement."),
("Risks that remain", "Delta, gamma, theta, jump risk, assignment, liquidity and transaction costs remain active. Rebalancing can reduce one exposure while increasing another, making a complete scenario analysis essential."),
], "A trader owns $40 of position vega and sells contracts contributing -$39. Net vega is near +$1 for a parallel one-point shift, but unequal expirations can still reprice differently after an event.",
[("Is zero vega risk-free?", "No. It only targets one first-order sensitivity at one moment."),("How often should it be rebalanced?", "That depends on drift, costs and risk limits; there is no universal interval."),("What is surface risk?", "Different strikes and expirations can experience different IV changes.")]),

guide("vix-vs-implied-volatility", "Market Context", "VIX vs Implied Volatility",
"Distinguish the broad-market VIX Index from the implied volatility quoted for a specific stock, strike and expiration.",
"VIX reflects a market-wide measure derived from S&P 500 options; a stock option's IV reflects its own contract and risks.", [
("What VIX represents", "VIX is designed to measure near-term expected volatility conveyed by a broad strip of S&P 500 Index options. It is not the implied volatility of every stock and cannot be substituted directly into an individual option quote."),
("Single-stock IV", "Company options reflect market conditions plus firm-specific earnings, products, litigation and liquidity. A stock's IV can rise while VIX falls, or remain calm while the market index becomes volatile."),
("Use both as context", "VIX can describe the broader risk environment, while the stock's volatility surface reveals contract-specific pricing. Compare like horizons and remember that index and single-stock options have different settlement and exercise features."),
], "VIX rises during a market selloff, but a company has just completed earnings and its near-term IV falls. Broad fear and company-specific uncertainty are moving in opposite directions.",
[("Is VIX the market's fear gauge?", "That nickname is common, but technically it measures expected S&P 500 volatility from option prices."),("Can I compare VIX with stock IV directly?", "Use it as context, not a one-for-one benchmark."),("Does high VIX mean every option is expensive?", "No. Each underlying, strike and expiration has its own pricing.")]),

guide("vega-volatility-mistakes", "Risk Management", "Vega and Volatility: 10 Mistakes to Avoid",
"Avoid common errors involving volatility points, earnings crush, IV rank, vega scaling, direction and portfolio exposure.",
"Volatility analysis works only when definitions, units, position signs, events and the entire Greek profile are kept consistent.", [
("Mistakes 1–3: definitions and units", "Do not confuse IV with historical volatility, interpret a one-point IV move as a one-percent relative change, or forget the contract multiplier. Small unit errors become material across several contracts."),
("Mistakes 4–6: incomplete signals", "Do not assume high IV predicts direction, treat IV rank as a standalone sell signal, or assume a correct directional call guarantees profit. The realized move, paid premium, vega and theta all matter."),
("Mistakes 7–10: hidden portfolio risk", "Do not ignore earnings crush, add legs without calculating net vega, assume all expirations move together, or leave exposure static as price and time change. Stress-test surface shifts, gaps and liquidity."),
], "A trader sees high IV rank and sells a large uncovered position without checking earnings. The stock gaps, IV expands further and delta accelerates, showing why a relative metric cannot replace a complete risk plan.",
[("What is the biggest vega mistake?", "Treating it as an isolated forecast instead of one changing sensitivity."),("Does high IV have to fall?", "No. It can stay high or rise further."),("How should vega be monitored?", "At position and portfolio level, across plausible price, time and volatility scenarios.")]),
]


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def article_html(article: dict, index: int) -> str:
    related = [ARTICLES[(index + offset) % len(ARTICLES)] for offset in (1, 5, 10)]
    schema_article = {"@context":"https://schema.org","@type":"Article","headline":article["title"],"description":article["description"],"datePublished":"2026-09-11","dateModified":"2026-09-11","author":{"@type":"Organization","name":"Options America"},"publisher":{"@type":"Organization","name":"Options America"},"mainEntityOfPage":f"https://options-america.onrender.com/blog/{article['slug']}/"}
    schema_faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in article["faq"]]}
    sections = "\n".join(f'          <h2 id="s{n}">{esc(t)}</h2>\n          <p>{esc(b)}</p>' for n,(t,b) in enumerate(article["sections"],1))
    faqs = "\n".join(f'          <div class="faq-item"><h3>{esc(q)}</h3><p>{esc(a)}</p></div>' for q,a in article["faq"])
    related_links = " · ".join(f'<a href="../{item["slug"]}/"><strong>{esc(item["title"])}</strong></a>' for item in related)
    toc = "\n".join(f'            <a href="#s{n}">{esc(t)}</a>' for n,(t,_) in enumerate(article["sections"],1))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{esc(article['title'])} | Options America</title><meta name="description" content="{esc(article['description'])}">
  <link rel="canonical" href="https://options-america.onrender.com/blog/{article['slug']}/"><meta property="og:type" content="article"><meta property="og:title" content="{esc(article['title'])}"><meta property="og:description" content="{esc(article['description'])}"><meta property="og:image" content="https://options-america.onrender.com/assets/images/blog/{article['slug']}.webp">
  <link rel="stylesheet" href="../../styles.css"><link rel="stylesheet" href="../blog.css"><script src="/favicon.js"></script>
  <script type="application/ld+json">{json.dumps(schema_article,separators=(',',':'))}</script><script type="application/ld+json">{json.dumps(schema_faq,separators=(',',':'))}</script></head>
<body><header class="site-header"><div class="container nav"><a class="brand" href="../../"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><nav><a href="../../courses/">Courses</a><a href="../../#paths">Learning Paths</a><a href="../../#strategies">Strategies</a><a href="../../#futures">Options on Futures</a><a href="../">Blog</a><a href="../../#resources">Resources</a></nav><a class="btn btn-gold" href="{COURSE}">Learn Vega — Free</a></div></header>
<main><section class="article-hero"><div class="container"><div class="breadcrumbs"><a href="../../">Home</a><span>›</span><a href="../">Blog</a><span>›</span><span>Vega &amp; Volatility</span></div><p class="eyebrow">{esc(article['tag'])}</p><h1>{esc(article['title'])}</h1><p class="article-deck">{esc(article['description'])}</p><div class="article-meta"><span>By Options America</span><span>Updated {DATE}</span><span>5-minute read</span></div></div></section>
<div class="container article-layout"><article class="article-body"><img src="../../assets/images/blog/{article['slug']}.webp" alt="{esc(article['title'])}"><p>{esc(article['description'])}</p><div class="article-callout"><strong>Key idea:</strong> {esc(article['key'])}</div>
{sections}
<h2 id="example">A practical example</h2><div class="example-box"><strong>Vega planning example</strong><p>{esc(article['example'])}</p></div><p>This simplified example holds other inputs constant to isolate volatility exposure. Live option prices also reflect the underlying price, time decay, rates, dividends, liquidity and transaction costs. Greeks are theoretical estimates, not guarantees.</p>
<h2 id="faq">Frequently asked questions</h2>{faqs}
<h2>Continue the Vega &amp; Volatility cluster</h2><p>Explore related guides: {related_links}. For a structured sequence, use the free <a href="{COURSE}"><strong>Level 6 – Vega &amp; Volatility course</strong></a>.</p><p><a class="btn btn-gold" href="{COURSE}">Start Level 6 — Free →</a></p><p class="article-disclaimer">Options involve risk and are not suitable for every investor. This material is educational and is not investment, tax or legal advice. Greeks are theoretical estimates, and contract terms and broker requirements can vary.</p></article>
<aside class="article-sidebar"><div class="toc"><strong>In this guide</strong>{toc}<a href="#example">Practical example</a><a href="#faq">FAQs</a></div><div class="course-cta"><strong>Free Level 6 Course</strong><p>Learn vega and volatility through structured lessons and practical examples.</p><a class="btn btn-gold" href="{COURSE}">Start the course →</a></div></aside></div></main>
<footer><div class="container footer-grid"><div><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><p>The free resource for learning options trading from beginner to advanced.</p></div><div><h4>Learn</h4><a href="/courses/">Courses</a><a href="/learning-paths/beginner/">Beginner Path</a></div><div><h4>Strategies</h4><a href="/#strategies">All Strategies</a><a href="/learning-paths/option-greeks/">Option Greeks</a></div><div><h4>Futures</h4><a href="/learning-paths/options-on-futures/">Options on Futures</a></div><div><h4>Resources</h4><a href="/blog/">Blog</a><a href="/courses/">Course Library</a></div></div><div class="container copyright">© <span data-current-year></span> Options America · Educational content only — not financial advice.</div></footer><script>document.querySelectorAll('[data-current-year]').forEach(e=>e.textContent=new Date().getFullYear())</script></body></html>'''


def card_html(article: dict) -> str:
    return f'        <a class="post-card" href="{article["slug"]}/"><img src="../assets/images/blog/{article["slug"]}.webp" alt="{esc(article["title"])}"><div class="post-card-copy"><span class="tag">{esc(article["tag"])}</span><h2>{esc(article["title"])}</h2><p>{esc(article["description"])}</p><strong>Read the guide →</strong></div></a>'


def update_index() -> None:
    path = BLOG / "index.html"
    source = path.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    if 'href="what-is-vega-in-options/"' not in source:
        source = source.replace(marker, "\n".join(card_html(a) for a in ARTICLES) + "\n" + marker, 1)
    source = source.replace("<strong>75</strong> guides", "<strong>90</strong> guides")
    if "Explore Level 6" not in source:
        source = source.replace('<a class="btn btn-gold" href="../courses/option-greeks-level-5-theta-time-decay/">Explore Level 5 →</a>', '<a class="btn btn-gold" href="../courses/option-greeks-level-5-theta-time-decay/">Explore Level 5 →</a><a class="btn btn-gold" href="../courses/options-trading-course-level-6-vega-and-volatility/">Explore Level 6 →</a>')
    path.write_text(source)


def update_scripts() -> None:
    path = BLOG / "blog.js"
    source = path.read_text().replace("const clusterPriority = card => card.textContent.includes('Theta') ? 5 :", "const clusterPriority = card => card.textContent.includes('Vega') ? 6 : card.textContent.includes('Theta') ? 5 :")
    path.write_text(source)
    path = ROOT / "favicon.js"
    source = path.read_text()
    marker = "    'theta-time-decay-mistakes': '/assets/images/blog/theta-time-decay-mistakes.webp'"
    additions = ",\n".join(f"    '{a['slug']}': '/assets/images/blog/{a['slug']}.webp'" for a in ARTICLES)
    if "'what-is-vega-in-options'" not in source:
        source = source.replace(marker, marker + ",\n" + additions)
    path.write_text(source)


def main() -> None:
    for index, article in enumerate(ARTICLES):
        directory = BLOG / article["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(article_html(article, index))
    update_index(); update_scripts()


if __name__ == "__main__":
    main()
