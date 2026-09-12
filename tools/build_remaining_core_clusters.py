#!/usr/bin/env python3
"""Build the remaining core SEO clusters (Levels 18, 20, 21 and 22)."""

from __future__ import annotations

import html
import json
import math
import re
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"
IMAGE_DIR = ROOT / "assets/images/blog"
DATE_ISO = "2026-09-12"
DATE_TEXT = "September 12, 2026"
DOMAIN = "https://options-america.onrender.com"


def item(slug, tag, title, description, key, example):
    return {"slug": slug, "tag": tag, "title": title, "description": description, "key": key, "example": example}


CLUSTERS = [
    {
        "level": 18, "name": "Protective Puts", "label": "Protective Put",
        "course": "advanced-option-level-18-protective-puts", "priority": 18,
        "cta": "Learn Protective Puts", "color": "#5ee0c2",
        "source": "https://www.cboe.com/tradable_products/equity_indices_leaps_options/specifications/",
        "articles": [
            item("protective-put-strategy-explained", "Complete Guide", "Protective Put Strategy Explained", "Learn how stock plus a long put creates a downside floor while preserving upside participation.", "A protective put is portfolio insurance: the premium buys a contractual sale price, but the insurance cost reduces the position's net return.", "Buy 100 shares at $100 and one 95 put for $3. At expiration the floor is $95, so the maximum stock-and-put loss is $8 per share before costs."),
            item("how-protective-put-works", "Mechanics", "How a Protective Put Works", "Understand the two-leg structure, exercise right, expiration outcomes and changing option value.", "The shares retain upside while the put gains value as the stock falls below its strike; before expiration, time and volatility also affect the hedge.", "At $82, a 95 put has at least $13 of intrinsic value, offsetting most of the decline in shares bought at $100."),
            item("protective-put-profit-loss-breakeven", "Payoff", "Protective Put Profit, Loss and Breakeven", "Calculate the downside floor, maximum loss and adjusted breakeven for a married-put position.", "Maximum loss equals stock cost minus put strike plus premium, while the upside breakeven rises by the cost of protection.", "Shares cost $70 and a 65 put costs $2.50. Maximum expiration loss is $7.50 per share and upside breakeven is $72.50."),
            item("protective-put-example", "Worked Example", "Protective Put Example With Expiration Scenarios", "Follow one hedged stock position through a rally, a flat market, a moderate decline and a crash.", "Scenario analysis must combine both legs; looking only at the profitable put or losing shares gives a misleading answer.", "For stock at $100 plus a 95 put costing $3, expiration P&L at $70, $95, $100 and $120 is about -$800, -$800, -$300 and +$1,700."),
            item("choose-protective-put-strike", "Strike Selection", "How to Choose a Protective Put Strike", "Compare deductible, premium, delta and protection level when selecting a hedge strike.", "A higher strike usually provides a tighter floor at a larger premium; a lower strike is cheaper but leaves a larger deductible.", "A 98 put costing $4 limits more downside than a 90 put costing $1.50, but raises the portfolio's insurance expense by $250 per contract."),
            item("choose-protective-put-expiration", "Expiration", "How to Choose Protective Put Expiration", "Match hedge duration to the risk window while balancing theta, event exposure and renewal cost.", "Expiration should cover the period that matters; repeatedly buying short protection can be cheap per contract yet expensive over a full year.", "A 30-day put may cover earnings, while a six-month put may better match a planned holding period and reduce renewal decisions."),
            item("protective-put-cost-insurance", "Cost", "How Much Does Protective Put Insurance Cost?", "Measure put premium, opportunity cost, volatility pricing and the drag created by repeated hedging.", "Insurance cost is the premium plus execution costs and foregone return; its value should be judged against the loss it is designed to prevent.", "Paying 2% every quarter would consume roughly 8% before compounding if every hedge expired worthless."),
            item("protective-put-greeks", "Greeks", "Protective Put Greeks: Delta, Gamma, Theta and Vega", "See how long stock and a long put combine into a changing risk profile.", "The position begins with positive delta, positive gamma and vega, and negative theta; its delta falls toward zero as the stock drops.", "Stock delta +1.00 combined with put delta -0.30 produces about +0.70 net delta initially, before gamma changes the hedge."),
            item("protective-put-vs-stop-loss", "Comparison", "Protective Put vs Stop-Loss Order", "Compare contractual downside protection with a conditional sell order across gaps, cost and execution.", "A put provides a strike-based right through a gap; a stop order has no premium but can fill well below its trigger in a fast market.", "A stock closes at $100 and opens at $78. A 95 put retains protection, while a $92 stop may execute near the lower available market."),
            item("protective-put-vs-collar", "Comparison", "Protective Put vs Collar Strategy", "Compare uncapped stock upside with a lower-cost hedge funded by selling a call.", "A collar can reduce put cost, but the short call caps upside and introduces assignment considerations.", "Buy a 90 put for $2 and sell a 110 call for $2: the zero-cost collar floors downside near $90 and caps upside near $110."),
            item("rolling-protective-puts", "Management", "How to Roll a Protective Put", "Plan when to extend time, move the strike or close an appreciated downside hedge.", "A roll closes one insurance contract and buys another; every debit, credit and realized gain remains part of total hedge cost.", "A 95 put rises from $2 to $8 during a decline. Selling it and buying a later 90 put realizes protection while keeping a new floor."),
            item("protective-put-mistakes", "Risk Management", "Protective Put Strategy: 10 Mistakes to Avoid", "Avoid errors involving strike, duration, volatility, sizing, exercise and false expectations.", "The biggest mistake is assuming any put eliminates loss; the deductible, premium, expiration and contract quantity define what is actually protected.", "A trader owns 300 shares but buys one put, leaving 200 shares unhedged despite describing the entire position as protected."),
        ],
    },
    {
        "level": 20, "name": "Optimizing Portfolio", "label": "Options Portfolio",
        "course": "options-portfolio-level-20-optimizing-portfolio", "priority": 20,
        "cta": "Optimize Your Portfolio", "color": "#f7c44a",
        "source": "https://www.optionseducation.org/advancedconcepts/position-greeks",
        "articles": [
            item("options-portfolio-optimization-guide", "Complete Guide", "Options Portfolio Optimization Guide", "Build a portfolio process around objectives, aggregate Greeks, scenario risk and capital reserves.", "A collection of individually reasonable trades can create one concentrated portfolio when their common market exposures are added together.", "Five bullish spreads may each risk only 1% but can behave like one 5% directional position during a broad decline."),
            item("how-to-analyze-options-portfolio", "Framework", "How to Analyze an Options Portfolio", "Review positions as one system using exposure, scenario P&L, liquidity and event concentration.", "Start with signed quantities and contract multipliers, then aggregate risk by underlying, sector, expiration and strategy.", "Ten contracts with delta 0.20 represent roughly 200 share-equivalents before gamma changes the number."),
            item("portfolio-delta-beta-weighting-guide", "Delta", "Portfolio Delta and Beta Weighting Guide", "Translate positions into a common benchmark estimate and understand the limits of beta-weighted delta.", "Beta weighting is a model-based comparison, not a guarantee; correlations and beta can change sharply during stress.", "A position with 100 deltas and beta 1.4 contributes roughly 140 benchmark-weighted deltas under a simplified linear estimate."),
            item("manage-portfolio-theta", "Theta", "How to Manage Portfolio Theta", "Balance desired time-decay exposure against gamma, event and tail risk.", "Positive theta is compensation for risks elsewhere in the portfolio; it is not a daily interest payment.", "A portfolio showing +$120 theta can still lose thousands during a gap because its short gamma and vega dominate."),
            item("manage-portfolio-vega", "Vega", "How to Manage Portfolio Vega", "Measure volatility sensitivity across symbols, strikes and expirations without assuming parallel IV moves.", "Net vega hides surface risk: front-month, back-month, call and put volatility can move by different amounts.", "Long $500 of back-month vega and short $500 of front-month vega is numerically flat but exposed to term-structure changes."),
            item("portfolio-gamma-risk", "Gamma", "Portfolio Gamma Risk Explained", "Understand how portfolio delta can accelerate as prices move and expiration approaches.", "Gamma describes changing delta, so a portfolio that looks neutral now can become strongly directional after a modest move.", "Net gamma of -40 deltas per $1 can turn a flat book into about -200 deltas after a $5 rise, before other changes."),
            item("options-portfolio-stress-testing", "Stress Testing", "How to Stress-Test an Options Portfolio", "Model price gaps, volatility shocks, time passage and correlation changes across the complete book.", "Useful stress tests combine drivers rather than changing price, IV or time one at a time.", "Model the index down 8%, single-stock IV up 20 points, spreads wider and put skew steeper on the same scenario."),
            item("options-position-sizing-portfolio", "Position Sizing", "Options Position Sizing at Portfolio Level", "Size trades from stressed loss, liquidity and total exposure instead of maximum profit.", "Position size should reflect what can happen to the whole portfolio when several supposedly separate trades fail together.", "Four trades each sized for a $1,000 loss can create more than $4,000 of stress loss if correlations rise and exits widen."),
            item("diversify-options-strategies", "Diversification", "How to Diversify an Options Portfolio", "Diversify by risk driver, underlying, duration and market thesis rather than ticker count alone.", "Different symbols are not diversified when they share the same beta, volatility and event exposure.", "Short puts on five technology stocks may respond like one concentrated downside-volatility trade during a sector shock."),
            item("portfolio-hedging-with-options", "Hedging", "Portfolio Hedging With Options", "Compare index puts, collars, spreads and dynamic hedges by objective, basis risk and cost.", "A hedge should be sized to a defined loss scenario and benchmark relationship, not purchased simply because fear has risen.", "A broad-index put may soften market beta but will not fully offset a company-specific collapse in a concentrated holding."),
            item("options-portfolio-rebalancing", "Rebalancing", "When to Rebalance an Options Portfolio", "Use exposure bands, thesis changes and event rules to avoid both neglect and excessive trading.", "Rebalancing should respond to measurable drift; constant adjustment can turn model precision into slippage and fees.", "A delta band of ±150 triggers review only after the portfolio leaves the planned range, not after every small tick."),
            item("options-portfolio-mistakes", "Risk Management", "Options Portfolio Management: 12 Mistakes to Avoid", "Avoid hidden leverage, correlation, Greek-sign, expiration and buying-power errors.", "The most damaging errors come from measuring trades separately while funding and market shocks affect the account together.", "Using nearly all available buying power leaves no reserve when volatility expands requirements across several short-premium positions."),
        ],
    },
    {
        "level": 21, "name": "Mastering VIX Volatility", "label": "VIX Fundamentals",
        "course": "level-21-mastering-vix-volatility-trading", "priority": 21,
        "cta": "Master VIX Volatility", "color": "#56bfff",
        "source": "https://www.cboe.com/tradable_products/vix/",
        "articles": [
            item("what-is-vix-index", "Complete Guide", "What Is the VIX Index and How Does It Work?", "Learn what the VIX measures, how option prices inform it and what the index does not predict.", "VIX is a market estimate of near-term S&P 500 volatility, not a direction forecast or a directly investable stock.", "A VIX reading of 24 is an annualized volatility measure; dividing by about √12 gives a rough one-month scale, not a guaranteed range."),
            item("how-vix-is-calculated", "Methodology", "How Is the VIX Calculated?", "Understand the strip of S&P 500 options, variance weighting and 30-day interpolation behind VIX.", "The calculation uses many out-of-the-money SPX options across two expirations, not one at-the-money straddle.", "Near- and next-term option variances are weighted to create a constant 30-day measure before volatility is annualized."),
            item("vix-fear-index-explained", "Interpretation", "Why Is VIX Called the Fear Index?", "Separate the popular nickname from the index's actual measurement of expected volatility.", "VIX often rises during equity declines, but it measures priced volatility rather than investor emotion itself.", "A calm rally can coincide with low VIX, while a fast two-sided market can sustain high VIX without a continuous decline."),
            item("vix-levels-meaning", "Interpretation", "What Do Different VIX Levels Mean?", "Interpret VIX in historical, event and term-structure context instead of using fixed magic thresholds.", "A level is meaningful relative to the current regime and option surface; 20 is not universally high or low.", "VIX at 25 after a shock may represent falling fear, while 25 after months near 13 may represent a major expansion."),
            item("vix-term-structure-explained", "Term Structure", "VIX Term Structure Explained", "Read the relationship among VIX futures maturities and distinguish it from spot VIX.", "The futures curve expresses prices for different settlement dates and does not have to converge across maturities until each contract expires.", "Front VIX futures at 18 and second-month futures at 20 form an upward-sloping curve even if spot VIX is 17."),
            item("vix-contango-backwardation", "Term Structure", "VIX Contango vs Backwardation", "Understand upward- and downward-sloping volatility futures curves and their market implications.", "Contango and backwardation describe relationships among futures maturities, not a promise about future spot VIX direction.", "If front-month VIX futures trade at 26 and second month at 23, the nearby curve is backwardated."),
            item("vix-futures-vs-spot-vix", "Products", "VIX Futures vs Spot VIX", "Learn why a futures contract can differ substantially from the displayed VIX Index.", "Tradable VIX derivatives reference expectations and converge to their own settlement process; spot VIX cannot be bought directly.", "Spot VIX jumps to 35 while a three-month future trades at 27 because the market does not price the shock as permanent."),
            item("vix-options-basics", "Options", "VIX Options Basics: Calls, Puts and Settlement", "Learn contract style, cash settlement, expiration and the relationship to forward VIX pricing.", "VIX options are European-style and cash-settled, and their settlement value is not simply the prior close of spot VIX.", "A VIX call finishing in the money settles in cash against the official settlement value rather than delivering shares."),
            item("vix-options-settlement-soq", "Settlement", "VIX Options Settlement and SOQ Explained", "Understand the Special Opening Quotation and why expiration-day settlement can surprise traders.", "Final settlement uses a special opening calculation from relevant SPX option quotes, which can differ from the displayed VIX level.", "A position that looked profitable against Tuesday's VIX close can settle differently on Wednesday's SOQ."),
            item("vix-vs-realized-volatility", "Comparison", "VIX vs Realized Volatility", "Compare forward-looking option-implied volatility with movement that actually occurred.", "The difference between implied and subsequent realized volatility is uncertain compensation, not a guaranteed premium.", "VIX averages 22 during a month in which annualized realized volatility finishes at 17; the gap does not reveal the path or trading costs."),
            item("vix-mean-reversion", "Behavior", "Does VIX Mean-Revert?", "Use mean reversion carefully while respecting regime shifts, clustering and asymmetric spikes.", "VIX has historically shown mean-reverting behavior, but neither the timing nor destination of a reversal is fixed.", "VIX at 40 can fall quickly, remain elevated, or spike higher before reverting; a short position must survive every path."),
            item("vix-trading-mistakes", "Risk Management", "VIX Trading: 10 Mistakes to Avoid", "Avoid confusing spot and futures, ignoring settlement, leverage, roll yield and product structure.", "Most VIX errors begin by treating the index, futures, options and exchange-traded products as interchangeable.", "Buying a volatility ETP because spot VIX rose can disappoint when futures exposure, daily resets and roll effects dominate."),
        ],
    },
    {
        "level": 22, "name": "VIX Hedging and Speculation", "label": "VIX Strategies",
        "course": "level-22-vix-options-hedging-and-speculation", "priority": 22,
        "cta": "Learn VIX Hedging", "color": "#bf91ff",
        "source": "https://www.cboe.com/tradable_products/vix/vix_options/specifications/",
        "articles": [
            item("vix-hedging-strategies-guide", "Complete Guide", "VIX Hedging Strategies Guide", "Design volatility hedges around objectives, horizon, basis risk, carry and exit rules.", "A VIX hedge must gain in the specific equity-loss scenario that matters; owning volatility exposure alone does not guarantee an offset.", "A three-month VIX call may react less than spot VIX during a brief shock because its matching future rises by a smaller amount."),
            item("hedge-portfolio-with-vix-calls", "Calls", "How to Hedge a Portfolio With VIX Calls", "Choose call strike, expiration and size while accounting for forward pricing and option premium.", "VIX calls can create convex exposure, but hedge efficiency depends on the corresponding VIX future and settlement date.", "Ten calls with estimated crisis gain of $800 each offset about $8,000 only in the modeled scenario, not every market decline."),
            item("vix-call-spread-hedge", "Call Spreads", "VIX Call Spread for Portfolio Hedging", "Reduce premium by capping the payoff and define where a call-spread hedge stops helping.", "Selling the higher-strike call lowers cost but creates a maximum hedge value precisely when volatility exceeds that strike.", "Buy a 25 call and sell a 40 call for a $2 net debit; the maximum spread value is $15 and maximum profit is $13 before costs."),
            item("vix-put-strategies", "Puts", "VIX Put Strategies for Falling Volatility", "Analyze long puts, put spreads and the challenge of timing volatility normalization.", "A correct view that volatility will fall can still lose if the relevant VIX future, timing or premium behaves differently.", "A 20 VIX put may remain out of the money even after spot VIX falls to 18 if the settlement-linked future stays above 20."),
            item("vix-calendar-spread-strategy", "Calendars", "VIX Calendar Spread Strategy", "Trade relative movement between volatility expirations while managing nonparallel term-structure shifts.", "VIX calendar legs reference different futures and settlements, making the structure more than an ordinary time spread.", "Long a later call and short a nearer call can lose if front volatility spikes much more than the back month."),
            item("vix-ratio-spread-strategy", "Ratio Spreads", "VIX Ratio Spread Strategy", "Compare front ratios and backspreads by tail exposure, premium and settlement risk.", "The direction of the ratio determines whether the volatility tail is owned or sold; reversing quantities can create uncovered risk.", "Sell one 25 call and buy two 35 calls: the backspread can have a middle loss and convex upside beyond the upper breakeven."),
            item("vix-iron-condor-butterfly", "Neutral Structures", "VIX Iron Condor and Butterfly Strategies", "Use defined-risk range structures only after understanding VIX settlement and futures-based pricing.", "A defined expiration payoff does not eliminate mark-to-market, liquidity or settlement-basis risk.", "A 20/25/30 call butterfly reaches maximum value near 25 at settlement, but can trade very differently beforehand."),
            item("size-vix-portfolio-hedge", "Sizing", "How to Size a VIX Portfolio Hedge", "Translate a target equity loss into scenario-based contract quantities and a premium budget.", "Hedge ratios are conditional estimates because the relationship between equities, VIX futures and options changes across shocks.", "If a $500,000 portfolio stress test loses $50,000 and each call spread gains $2,500, twenty spreads provide a modeled full offset."),
            item("vix-hedge-cost-carry", "Cost", "VIX Hedge Cost, Carry and Roll Yield", "Measure repeated premium expense, futures curve effects and the cost of maintaining crisis protection.", "A hedge can work in a crash and still reduce long-run returns if renewal and carry costs are ignored.", "Spending 0.75% each quarter costs about 3% a year before compounding when no hedge payout is realized."),
            item("when-to-close-vix-hedge", "Exit Planning", "When to Close or Roll a VIX Hedge", "Use portfolio recovery, volatility targets, remaining convexity and time rules to manage exits.", "A hedge gain is only useful when it is harvested or deliberately retained against continuing portfolio risk.", "Selling half after a volatility spike can fund losses while leaving partial protection if stress continues."),
            item("vix-etf-etn-risks", "Products", "VIX ETF and ETN Risks Explained", "Understand futures exposure, daily resets, roll effects, leverage and issuer structure in volatility products.", "A VIX-linked ETP is not spot VIX; its return depends on the futures methodology and product wrapper.", "Spot VIX can finish unchanged over a month while a long futures-based product loses from curve and daily path effects."),
            item("vix-hedging-mistakes", "Risk Management", "VIX Hedging and Speculation: 12 Mistakes to Avoid", "Avoid timing, product, settlement, sizing, carry and exit errors in volatility positions.", "The central mistake is selecting a VIX product first and defining the portfolio problem afterward.", "An oversized hedge bought after volatility already spikes can lose quickly when fear normalizes even if the portfolio remains below its high."),
        ],
    },
]


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def font(size: int, bold: bool = False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


def paragraphs(cluster, article, index):
    topic = article["title"].lower()
    label = cluster["label"].lower()
    variants = [
        [
            f"The useful starting point for {topic} is the job the position must perform. {article['description']} State the horizon, desired exposure, affordable cost and event being addressed. That written objective makes it possible to compare the strategy with cash, stock or a simpler option structure.",
            f"Treat {topic} as a decision problem before treating it as an order ticket. {article['description']} Define success in dollars and time, then identify the market path that would make the position unnecessary or ineffective. This prevents a familiar strategy name from replacing analysis.",
            f"Begin by separating forecast from objective. In {topic}, the forecast describes price or volatility; the objective states what the account needs. {article['description']} A clear objective includes a review date, budget and maximum acceptable drawdown, not merely a directional opinion.",
            f"Every sound {label} plan starts with a precise reason for taking risk. For {topic}, write the exposure being added or reduced, how long it is needed and how much the result may cost. {article['description']} If those items cannot be measured, position quality cannot be evaluated afterward.",
        ],
        [
            f"{article['key']} Calculate the complete economic position with signed quantities, contract multipliers and every opening cash flow. Stock, options and futures must be viewed together. Before expiration, changing time value and volatility can produce a result that looks very different from the final payoff line.",
            f"The central mechanism is simple but the live exposure is dynamic: {article['key']} Separate intrinsic value from extrinsic value and identify which leg controls the next dollar of risk. Include commissions, exercise or settlement mechanics and capital tied up by the position.",
            f"To understand the exposure, translate {topic} into rights, obligations and cash flows. {article['key']} Then calculate what happens at expiration and what can happen earlier when implied volatility, skew or liquidity changes. Both views are required for a complete risk estimate.",
            f"Focus on the combined payoff rather than celebrating the leg that happens to be profitable. {article['key']} Record entry values and the contract multiplier so percentages do not conceal dollar risk. Reprice the position whenever the underlying driver changes materially.",
        ],
        [
            f"Build a scenario table for {topic} using at least five outcomes and two dates. Combine price moves with higher and lower volatility rather than changing one input at a time. Include a discontinuous gap and a wider bid-ask spread; the adverse cases determine whether the proposed size is survivable.",
            f"One forecast is not enough for {label}. Model a calm path, the expected path, an early adverse move and a tail event. Repeat the exercise with less time remaining. This exposes positions that appear comfortable at expiration but require too much capital or patience before then.",
            f"Stress testing should answer how much the account can lose, when that loss can occur and whether the position can still be closed. For {topic}, combine the wrong direction with a volatility shock and reduced liquidity. A useful test challenges the assumptions that make the base case attractive.",
            f"Create a small matrix rather than relying on one payoff chart: several market levels across today, the planned review date and expiration. For {topic}, add nonparallel volatility changes where relevant. Compare every result with the portfolio loss limit and available buying-power reserve.",
        ],
        [
            f"Delta, gamma, theta and vega are snapshots around current inputs. In {topic}, the dominant Greek can change as price moves or expiration approaches. Recalculate after a meaningful move and review the portfolio total; offsetting today's delta does not neutralize tomorrow's gamma or volatility exposure.",
            f"Use Greeks as sensitivities, not promises. A delta estimate assumes a small move and other inputs held constant, while real markets move price, time and volatility together. For {topic}, inspect both the current values and how they change in the stress scenarios already defined.",
            f"A single net Greek can hide important structure. Two legs may offset vega while referencing different expirations, or offset delta while carrying negative gamma. Map the signed sensitivities of {topic} by leg, then aggregate them with the rest of the account.",
            f"The Greek profile of {label} is conditional on price, time and volatility. Ask which sensitivity creates profit, which one finances it and which one accelerates loss. That question is more informative than describing the position as simply bullish, bearish, long volatility or hedged.",
        ],
        [
            f"Before entering {topic}, inspect bid-ask spreads, quoted size, open interest and the exact settlement or exercise rules. Use limit orders and confirm each filled quantity. Slippage and partial execution can materially change a multi-leg payoff, especially when markets widen during stress.",
            f"Execution belongs in the analysis, not in a footnote. Estimate entry and exit slippage for {topic}, check whether each leg trades actively and understand what happens at expiration. A strategy with a small theoretical edge may have no practical edge after two trips through a wide market.",
            f"Choose contracts that can be managed under the adverse scenario, not only entered during calm conditions. For {topic}, verify expiration dates, settlement conventions, multipliers and broker handling. Place the order as a defined package when possible and audit the position immediately after it fills.",
            f"Liquidity changes the realized version of {label}. Compare displayed markets across strikes and maturities, avoid assuming midpoint fills, and plan how a partial fill would be handled. Product specifications also matter: cash settlement, exercise style and assignment can change both timing and capital needs.",
        ],
        [
            f"Set the management rules for {topic} while the decision is still calm: profit objective, loss limit, review trigger and latest exit date. A roll closes the existing contract and opens another, so keep all prior cash flows in the record. The new position must be justified on its own forward-looking merits.",
            f"Write a response for three states: thesis working, thesis delayed and thesis invalidated. For {topic}, specify whether each state calls for holding, reducing, closing or replacing exposure. This reduces the temptation to convert a planned trade into an indefinite commitment after a loss.",
            f"Management is a sequence of new choices, not a way to erase history. Preserve the original cost and every subsequent debit or credit in {topic}. Recalculate the remaining payoff after any adjustment and compare it with the alternative of closing and holding no position.",
            f"The exit plan should identify what will be harvested and what risk will remain. In {label}, an unrealized hedge gain or volatility profit can disappear as quickly as it appeared. Use observable triggers and account-level limits so the decision does not depend on finding the perfect market top or bottom.",
        ],
    ]
    headings = ["Start with the objective", "Understand the economic exposure", "Measure more than one outcome", "Check the changing Greeks", "Plan execution and liquidity", "Define management before entry"]
    families = [(heading, variants[n][(index + n) % len(variants[n])]) for n, heading in enumerate(headings)]
    shift = index % len(families)
    return families[shift:] + families[:shift]


def article_html(cluster, article, index):
    articles = cluster["articles"]
    related = [articles[(index + n) % len(articles)] for n in (1, 4, 8)]
    sections = paragraphs(cluster, article, index)
    article_schema = {"@context": "https://schema.org", "@type": "Article", "headline": article["title"], "description": article["description"], "datePublished": DATE_ISO, "dateModified": DATE_ISO, "author": {"@type": "Organization", "name": "Options America"}, "publisher": {"@type": "Organization", "name": "Options America"}, "mainEntityOfPage": f"{DOMAIN}/blog/{article['slug']}/"}
    faq = [
        (f"What is the key idea behind {article['title']}?", article["key"]),
        ("Does the example guarantee a live-market result?", "No. It is an educational scenario; live prices, volatility, liquidity, costs and contract terms can change the outcome."),
        ("What should be defined before entry?", "The objective, size, maximum tolerated loss, review triggers, settlement or assignment plan and exit date."),
    ]
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    section_html = "\n".join(f'<h2 id="s{n}">{esc(title)}</h2><p>{esc(body)}</p>' for n, (title, body) in enumerate(sections, 1))
    toc = "".join(f'<a href="#s{n}">{esc(title)}</a>' for n, (title, _) in enumerate(sections, 1))
    links = " · ".join(f'<a href="../{x["slug"]}/"><strong>{esc(x["title"])}</strong></a>' for x in related)
    faqs = "".join(f'<div class="faq-item"><h3>{esc(q)}</h3><p>{esc(a)}</p></div>' for q, a in faq)
    course = f'../../courses/{cluster["course"]}/'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(article['title'])} | Options America</title><meta name="description" content="{esc(article['description'])}">
<link rel="canonical" href="{DOMAIN}/blog/{article['slug']}/"><meta property="og:type" content="article"><meta property="og:title" content="{esc(article['title'])}"><meta property="og:description" content="{esc(article['description'])}"><meta property="og:image" content="{DOMAIN}/assets/images/blog/{article['slug']}.webp">
<link rel="stylesheet" href="../../styles.css"><link rel="stylesheet" href="../blog.css"><script src="/favicon.js"></script>
<script type="application/ld+json">{json.dumps(article_schema,separators=(',',':'))}</script><script type="application/ld+json">{json.dumps(faq_schema,separators=(',',':'))}</script></head>
<body><header class="site-header"><div class="container nav"><a class="brand" href="../../"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><nav><a href="../../courses/">Courses</a><a href="../../#paths">Learning Paths</a><a href="../../#strategies">Strategies</a><a href="../../#futures">Options on Futures</a><a href="../">Blog</a><a href="../../#resources">Resources</a></nav><a class="btn btn-gold" href="{course}">{esc(cluster['cta'])} — Free</a></div></header>
<main><section class="article-hero"><div class="container"><div class="breadcrumbs"><a href="../../">Home</a><span>›</span><a href="../">Blog</a><span>›</span><span>{esc(cluster['name'])}</span></div><p class="eyebrow">{esc(cluster['label'])} · {esc(article['tag'])}</p><h1>{esc(article['title'])}</h1><p class="article-deck">{esc(article['description'])}</p><div class="article-meta"><span>By Options America</span><span>Updated {DATE_TEXT}</span><span>8-minute read</span></div></div></section>
<div class="container article-layout"><article class="article-body"><img src="../../assets/images/blog/{article['slug']}.webp" alt="{esc(article['title'])}"><p>{esc(article['description'])}</p><div class="article-callout"><strong>Key idea:</strong> {esc(article['key'])}</div>
{section_html}
<h2 id="example">A practical example</h2><div class="example-box"><strong>{esc(cluster['label'])} example</strong><p>{esc(article['example'])}</p></div><p>This simplified example is educational and focuses on selected outcomes. Live prices also reflect time, implied volatility, skew, rates, dividends where applicable, liquidity, settlement conventions and transaction costs. Greeks and scenario values are estimates, not guarantees.</p>
<h2 id="checklist">Decision checklist</h2><p>Confirm the market thesis and time horizon. Calculate the full-position payoff and premium at risk. Stress price, volatility and time together. Check contract specifications and settlement. Set the maximum account-level loss, reserve capital and exit trigger. Finally, record the result after closing so the next decision is based on evidence rather than memory.</p>
<h2 id="faq">Frequently asked questions</h2>{faqs}
<h2>Continue the {esc(cluster['name'])} cluster</h2><p>Explore related guides: {links}. For a structured sequence, use the free <a href="{course}"><strong>Level {cluster['level']} – {esc(cluster['name'])} course</strong></a>.</p><p><a class="btn btn-gold" href="{course}">Start Level {cluster['level']} — Free →</a></p><p class="article-disclaimer">Options and volatility products involve risk and are not suitable for every investor. This material is educational and is not investment, tax or legal advice. Verify current contract specifications with the exchange and your broker.</p></article>
<aside class="article-sidebar"><div class="toc"><strong>In this guide</strong>{toc}<a href="#example">Practical example</a><a href="#checklist">Checklist</a><a href="#faq">FAQs</a></div><div class="course-cta"><strong>Free Level {cluster['level']} Course</strong><p>Follow the complete {esc(cluster['name'])} learning sequence.</p><a class="btn btn-gold" href="{course}">Start the course →</a></div><div class="course-cta"><strong>Primary reference</strong><p>Verify product mechanics and current specifications.</p><a href="{cluster['source']}" rel="noopener">Official reference →</a></div></aside></div></main>
<footer><div class="container footer-grid"><div><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><p>The free resource for learning options trading from beginner to advanced.</p></div><div><h4>Learn</h4><a href="/courses/">Courses</a><a href="/learning-paths/beginner/">Beginner Path</a></div><div><h4>Strategies</h4><a href="/#strategies">All Strategies</a><a href="/learning-paths/option-greeks/">Option Greeks</a></div><div><h4>Futures</h4><a href="/learning-paths/options-on-futures/">Options on Futures</a></div><div><h4>Resources</h4><a href="/blog/">Blog</a><a href="/courses/">Course Library</a></div></div><div class="container copyright">© <span data-current-year></span> Options America · Educational content only — not financial advice.</div></footer><script>document.querySelectorAll('[data-current-year]').forEach(e=>e.textContent=new Date().getFullYear())</script></body></html>'''


def card_html(cluster, article):
    return f'<a class="post-card" href="{article["slug"]}/"><img src="../assets/images/blog/{article["slug"]}.webp" alt="{esc(article["title"])}"><div class="post-card-copy"><span class="tag">{esc(cluster["label"])} · {esc(article["tag"])}</span><h2>{esc(article["title"])}</h2><p>{esc(article["description"])}</p><strong>Read the guide →</strong></div></a>'


def create_image(cluster, article, index):
    image = Image.new("RGB", (1200, 675), "#07172d")
    draw = ImageDraw.Draw(image)
    accent = cluster["color"]
    for y in range(675):
        draw.line((0, y, 1200, y), fill=(7 + y // 90, 20 + y // 35, 40 + y // 22))
    draw.ellipse((730 + (index % 3) * 25, -180, 1320, 410), fill="#0c3157")
    draw.rounded_rectangle((56, 52, 315, 98), 20, fill=accent)
    draw.text((74, 64), f"LEVEL {cluster['level']}  •  GUIDE {index + 1:02d}", font=font(17, True), fill="#07172d")
    y = 142
    for line in textwrap.wrap(article["title"], width=25)[:4]:
        draw.text((62, y), line, font=font(40, True), fill="white")
        y += 49
    draw.text((64, 572), "OPTIONS AMERICA", font=font(21, True), fill="#dce8f4")
    draw.text((64, 606), f"{cluster['name']} Learning Series", font=font(17), fill="#8daac4")
    draw.rounded_rectangle((724, 148, 1132, 516), 28, fill="#081d34", outline="#315473", width=3)
    cx, cy = 925, 342
    draw.line((770, cy, 1085, cy), fill="#55748f", width=2)
    draw.line((cx, 190, cx, 474), fill="#55748f", width=2)
    mode = index % 6
    if cluster["level"] == 18:
        draw.line([(775, 230), (885, 340), (1010, 450), (1085, 450)], fill="#ff8879", width=7)
        draw.line([(775, 230), (900, 355), (950, 405), (1085, 405)], fill=accent, width=7)
        draw.line((950, 205, 950, 470), fill=accent, width=3)
    elif cluster["level"] == 20:
        for j, h in enumerate((90 + mode*8, 155, 65 + mode*12, 125, 185 - mode*7)):
            x = 770 + j * 62
            draw.rounded_rectangle((x, 455-h, x+38, 455), 7, fill=[accent,"#54c7ff","#80dfa7","#ff8978","#b891ff"][j])
        draw.line([(770, 410), (840, 335), (910, 365), (980, 255), (1085, 220)], fill="white", width=4)
    elif cluster["level"] == 21:
        points = [(770 + x*28, 345 + int(math.sin((x+mode)*.8)*75)) for x in range(12)]
        draw.line(points, fill=accent, width=7, joint="curve")
        draw.text((792, 202), "VOLATILITY", font=font(15, True), fill="white")
    else:
        draw.line([(770, 430), (835, 360), (890, 390), (955, 250), (1010, 285), (1085, 205)], fill=accent, width=7, joint="curve")
        draw.arc((790, 230, 1055, 495), 185, 350, fill="#54c7ff", width=5)
        draw.polygon([(1085,205),(1054,207),(1076,232)], fill=accent)
    image.save(IMAGE_DIR / f"{article['slug']}.webp", "WEBP", quality=88, method=6)


def update_index():
    path = BLOG / "index.html"
    source = path.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    cards = []
    for cluster in CLUSTERS:
        for article in cluster["articles"]:
            if f'href="{article["slug"]}/"' not in source:
                cards.append(card_html(cluster, article))
    if cards:
        source = source.replace(marker, "\n".join(cards) + "\n" + marker, 1)
    actual = len(list(BLOG.glob("*/index.html")))
    source = re.sub(r'<strong>\d+</strong> guides', f'<strong>{actual}</strong> guides', source, count=1)
    anchor = '<a class="btn btn-gold" href="../courses/advanced-option-level-16-short-strangle/">Explore Level 16 →</a>'
    extras = ''.join(f'<a class="btn btn-gold" href="../courses/{c["course"]}/">Explore Level {c["level"]} →</a>' for c in CLUSTERS)
    if "Explore Level 18" not in source:
        source = source.replace(anchor, anchor + extras)
    path.write_text(source)


def update_blog_js():
    path = BLOG / "blog.js"
    source = path.read_text()
    old = "const clusterPriority = card => "
    start = source.index(old)
    end = source.index(";", start) + 1
    rule = "const clusterPriority = card => card.textContent.includes('VIX Strategies') ? 22 : card.textContent.includes('VIX Fundamentals') ? 21 : card.textContent.includes('Options Portfolio') ? 20 : card.textContent.includes('Protective Put') ? 18 : card.textContent.includes('Short Strangle') ? 16 : card.textContent.includes('Short Straddle') ? 15 : card.textContent.includes('Backspread') ? 14 : card.textContent.includes('Calendar Spread') ? 13 : card.textContent.includes('Butterfly Spread') ? 12 : card.textContent.includes('Short Iron Condor') ? 11 : card.textContent.includes('Bear Put Spread') ? 10 : card.textContent.includes('Bull Call Spread') ? 9 : card.textContent.includes('Greeks') ? 8 : card.textContent.includes('Delta') ? 7 : card.textContent.includes('Vega') ? 6 : card.textContent.includes('Theta') ? 5 : card.textContent.includes('Selling Puts') ? 4 : card.textContent.includes('Buying Puts') ? 3 : card.textContent.includes('Selling Calls') ? 2 : card.textContent.includes('Call Options') ? 1 : 0;"
    path.write_text(source[:start] + rule + source[end:])


def update_favicon_map():
    path = ROOT / "favicon.js"
    source = path.read_text()
    marker = "  const courseImageMap = {"
    if marker not in source:
        return
    additions = []
    for cluster in CLUSTERS:
        for article in cluster["articles"]:
            if f"'{article['slug']}'" not in source:
                additions.append(f"    '{article['slug']}': '/assets/images/blog/{article['slug']}.webp',")
    if additions:
        source = source.replace(marker, marker + "\n" + "\n".join(additions), 1)
        path.write_text(source)


def update_course_pages():
    for cluster in CLUSTERS:
        path = ROOT / "courses" / cluster["course"] / "index.html"
        source = path.read_text()
        if "companion-guides-core" in source:
            continue
        links = "".join(f'<li><a href="../../blog/{a["slug"]}/">{esc(a["title"])}</a></li>' for a in cluster["articles"])
        section = f'<section class="related-section companion-guides-core"><h2>Level {cluster["level"]} Companion Guides</h2><p>Go deeper with the complete Options America learning cluster.</p><div class="info-box"><ul>{links}</ul></div></section>'
        source = source.replace('<section class="related-section">', section + '<section class="related-section">', 1)
        path.write_text(source)


def update_sitemap():
    path = ROOT / "sitemap.xml"
    source = path.read_text()
    closing = "</urlset>"
    additions = []
    for cluster in CLUSTERS:
        for article in cluster["articles"]:
            url = f"{DOMAIN}/blog/{article['slug']}/"
            if url not in source:
                additions.append(f"  <url><loc>{url}</loc></url>")
    if additions:
        source = source.replace(closing, "\n".join(additions) + "\n" + closing)
        path.write_text(source)


def main():
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    for cluster in CLUSTERS:
        for index, article in enumerate(cluster["articles"]):
            directory = BLOG / article["slug"]
            directory.mkdir(parents=True, exist_ok=True)
            (directory / "index.html").write_text(article_html(cluster, article, index))
            create_image(cluster, article, index)
    update_index()
    update_blog_js()
    update_favicon_map()
    update_course_pages()
    update_sitemap()


if __name__ == "__main__":
    main()
