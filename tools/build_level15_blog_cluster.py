#!/usr/bin/env python3
"""Build the Level 15 Short Straddle SEO cluster and original artwork."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("level14_builder", ROOT / "tools/build_level14_blog_cluster.py")
level14 = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(level14)
base = level14.base
BLOG = ROOT / "blog"
COURSE = "../../courses/advanced-option-level-15-short-straddle/"


def guide(slug, tag, title, description, key, sections, example, faq):
    return dict(slug=slug, tag=f"Short Straddle · {tag}", title=title, description=description,
                key=key, sections=sections, example=example, faq=faq)


ARTICLES = [
guide("short-straddle-options-strategy-explained", "Complete Guide", "Short Straddle Options Strategy Explained",
"Learn how a short straddle sells an at-the-money call and put to collect premium while accepting substantial two-sided risk.",
"A short straddle benefits when price stays close to one strike and implied volatility or time value declines, but losses expand outside the two breakevens.", [
("Construction", "Sell one call and one put at the same strike and expiration, normally near the current stock price. The combined credit is the maximum possible profit and widens both expiration breakevens."),
("Expiration payoff", "Profit is highest when the underlying expires exactly at the common strike. Above it the short call loses value; below it the short put loses value. The opposite option expires worthless but does not cap the active leg."),
("Volatility and time", "The position is generally negative vega and positive theta. Falling implied volatility and passing time can help, while volatility expansion and fast price movement can overwhelm collected decay."),
("Risk reality", "Upside loss is theoretically unlimited and downside loss is substantial until the underlying reaches zero. Margin can rise during stress, and early assignment can change the intended two-leg position."),
], "With stock at $100, sell the 100 call for $4.50 and the 100 put for $4. The $8.50 credit creates expiration breakevens at $91.50 and $108.50 before costs.",
[("What is maximum profit?", "The total premium received."),("Is the risk defined?", "No. Upside risk is unlimited and downside risk is substantial."),("What market view fits?", "A range-bound market with volatility expected to fall.")]),

guide("how-short-straddle-works", "Mechanics", "How a Short Straddle Works",
"Understand the mechanics of selling a call and put at one strike, including premium, assignment and changing directional exposure.",
"Although entered as a neutral trade, a short straddle becomes increasingly directional whenever the underlying moves away from its strike.", [
("Two obligations", "The short call obligates the seller to deliver shares if assigned, while the short put obligates the seller to buy shares. Only one side is normally in the money at expiration, but both legs retain value before expiration."),
("Credit and breakevens", "Add both option premiums to find the opening credit. Add the credit to the strike for the upper breakeven and subtract it from the strike for the lower breakeven at expiration."),
("Delta changes", "Near the strike, call and put deltas can partly offset. A rally makes the call delta more negative for the seller; a decline makes the put delta more positive in absolute directional risk."),
("Lifecycle", "Profit can arrive through time decay or a volatility contraction without waiting for expiration. Loss can accelerate through gamma, a volatility spike, widening markets or a margin increase."),
], "A 50-strike call and put sell for a combined $5. The trade is profitable at expiration between $45 and $55, with the full $5 earned only at $50.",
[("Must both options be ATM?", "The classic straddle uses the same near-ATM strike."),("Can both legs be assigned?", "It is possible under unusual conditions and should be planned for."),("Does neutral mean low risk?", "No.")]),

guide("short-straddle-payoff-profit-loss-breakevens", "Payoff", "Short Straddle Profit, Loss and Breakevens",
"Calculate maximum profit, upper and lower breakevens and scenario losses for a short straddle at expiration.",
"The collected credit defines maximum profit but not maximum loss; every dollar beyond a breakeven adds approximately one dollar of loss per share.", [
("Maximum profit", "Maximum profit equals the call premium plus put premium and occurs only when the underlying finishes at the shared strike. Commissions reduce the retained amount."),
("Lower breakeven", "Subtract total credit from the strike. Below that price, put intrinsic value exceeds the premium received and loss grows as the underlying continues to fall."),
("Upper breakeven", "Add total credit to the strike. Above that price, call intrinsic value exceeds the premium received and loss grows without a theoretical ceiling."),
("Before expiration", "A payoff diagram is not a forecast of interim P&L. Remaining time value, implied volatility, skew, dividends and liquidity can keep the trade profitable or unprofitable at prices inside the expiration range."),
], "A 100 short straddle collects $9. Maximum profit is $900, breakevens are $91 and $109, and expiration at $115 produces a $600 loss before costs.",
[("How many breakevens are there?", "Two at expiration."),("Where is maximum profit?", "At the common strike."),("Can loss exceed the credit?", "Yes, by a large amount.")]),

guide("short-straddle-example", "Worked Example", "Short Straddle Example With Payoff Scenarios",
"Follow a complete short straddle example across no move, moderate moves, breakevens and a large gap.",
"Testing several prices reveals how quickly a limited credit can be overtaken when the underlying leaves the expected range.", [
("Open the position", "Stock trades at $100. Sell one 100 call for $5 and one 100 put for $4.50. The total $9.50 credit is $950 per standard straddle."),
("Near the strike", "At $100 both options expire worthless and the full credit remains. At $104 the call has $4 intrinsic value, leaving $5.50 of expiration profit."),
("At the boundaries", "Expiration at $90.50 or $109.50 uses the entire credit to offset intrinsic value. These are the lower and upper breakevens before fees."),
("Outside the range", "At $120, the short call loses $20 while the put expires worthless. Net loss is $10.50 per share, or $1,050, and further upside keeps increasing the loss."),
], "Approximate expiration P&L at $85, $95, $100, $105 and $120 is −$550, +$450, +$950, +$450 and −$1,050 before transaction costs.",
[("Why is $100 best?", "Both options expire worthless at their shared strike."),("Does the losing option use all premium?", "It is offset by the combined credit from both legs."),("Can the trade be closed early?", "Yes, with a two-leg order.")]),

guide("short-straddle-vs-long-straddle", "Comparison", "Short Straddle vs Long Straddle",
"Compare short and long straddles across premium, volatility, theta, movement requirements and tail risk.",
"The same strikes create opposite exposures: the short straddle sells movement and volatility, while the long straddle buys them.", [
("Cash flow", "A short straddle receives a credit and has limited maximum profit. A long straddle pays a debit that defines its maximum loss."),
("Movement", "The short position prefers price near the strike; the long position requires a move beyond either breakeven. One trader's expiration payoff is approximately the other trader's loss before costs."),
("Greeks", "Short straddles are usually negative gamma, negative vega and positive theta. Long straddles reverse those signs and benefit from acceleration or volatility expansion."),
("Risk choice", "Selling the straddle introduces substantial tail and margin risk. Buying it controls dollar loss but can lose steadily through decay when realized movement disappoints."),
], "A 100 straddle costs $8. The buyer risks $800 and needs expiration below $92 or above $108; the seller earns at most $800 and loses outside the same boundaries.",
[("Which has defined loss?", "The long straddle."),("Which benefits from time decay?", "Usually the short straddle."),("Are they exact opposites?", "Their legs are opposite, although execution costs differ.")]),

guide("short-straddle-vs-short-strangle", "Comparison", "Short Straddle vs Short Strangle",
"Compare two neutral premium-selling strategies across strikes, credit, probability range, Greeks and tail risk.",
"A straddle sells more premium at one central strike; a strangle uses separate OTM strikes to create a wider initial range.", [
("Strike placement", "The short straddle sells an ATM call and put at the same strike. The short strangle sells an OTM call above price and an OTM put below price."),
("Credit and range", "The straddle normally collects more credit, but its intrinsic exposure begins immediately after any price move. The strangle collects less and provides space between its short strikes."),
("Greeks", "ATM options give the straddle stronger gamma, theta and vega exposure. A strangle often starts with smaller sensitivities but can become highly reactive when price approaches either short strike."),
("Shared tail risk", "Both retain an uncovered short call and put, so neither defines tail loss. Strike distance should never be mistaken for protection during a sufficiently large move."),
], "With stock at $100, compare a 100 straddle collecting $9 with a 90/110 strangle collecting $4. The strangle starts wider but offers less credit to absorb a tail move.",
[("Which collects more premium?", "Normally the short straddle."),("Which starts with a wider range?", "The short strangle."),("Is the strangle defined risk?", "No.")]),

guide("short-straddle-vs-iron-butterfly", "Comparison", "Short Straddle vs Iron Butterfly",
"Compare the uncovered short straddle with a defined-risk iron butterfly across wings, credit, buying power and outcomes.",
"Adding protective wings converts the two uncovered tails of a short straddle into the capped risk of an iron butterfly.", [
("Core position", "Both structures sell a call and put at the same central strike. The iron butterfly additionally buys a lower-strike put and higher-strike call."),
("Credit", "The short straddle receives more premium because it does not pay for wings. The iron butterfly receives less but its maximum loss can be calculated from wing width and net credit."),
("Buying power", "Undefined-risk margin for the straddle can change as volatility and price move. The butterfly's defined maximum loss generally creates a clearer capital requirement."),
("Management", "Wings reduce catastrophe risk but can add slippage and complicate rolls. Choose the structure by loss tolerance and liquidity rather than headline credit."),
], "A 100 straddle collects $9. Buying the 90 put and 110 call for $2 converts it to a 10-point iron butterfly with a $7 net credit and $3 maximum loss per share.",
[("Which has defined risk?", "The iron butterfly."),("Why does the straddle collect more?", "It does not buy protection."),("Do wings guarantee easy exits?", "No; liquidity still matters.")]),

guide("best-market-conditions-short-straddle", "Entry", "Best Market Conditions for a Short Straddle",
"Evaluate implied versus realized volatility, catalysts, liquidity and price stability before considering a short straddle.",
"The strategy needs future movement to stay smaller than the movement embedded in option prices; high IV alone is not an edge.", [
("Implied versus realized", "Compare the market's implied move with a defensible range of realized outcomes. Rich options help only when the premium more than compensates for actual movement and tail risk."),
("Catalyst calendar", "Earnings, court decisions, product news and economic releases can create gaps that bypass gradual adjustments. Decide whether the event premium is intentional or avoid the event."),
("Liquidity", "Use underlyings with tight option markets, reliable multi-leg execution and sufficient open interest. Slippage matters twice at entry and again when adjusting or closing."),
("Portfolio context", "Correlated short-volatility positions can all lose together during a market shock. Review aggregate vega, gamma, delta and buying-power stress before adding another trade."),
], "An index has elevated IV without a scheduled binary event and its options imply a wider range than the trader's tested scenarios. The setup is analyzed with strict loss and margin limits.",
[("Is high IV enough?", "No."),("Why avoid some events?", "Gaps can create losses before an adjustment is possible."),("Does diversification remove tail risk?", "No, especially when positions are correlated.")]),

guide("implied-volatility-short-straddle", "Volatility", "Implied Volatility and the Short Straddle",
"Understand negative vega, volatility crush, term structure and why high implied volatility can still become higher.",
"A short straddle sells volatility at entry, so the level paid by buyers and the path of IV afterward materially affect mark-to-market results.", [
("Negative vega", "Both legs are short options and normally contribute negative vega. A one-point IV decline can help, while an increase raises the theoretical cost to repurchase the position."),
("Volatility crush", "After a known event, IV may contract sharply. The contraction can help the straddle, but only if the price move and resulting intrinsic value do not consume more than the volatility gain."),
("Term structure", "Front expirations can price event risk differently from later months. Compare the selected expiration with surrounding maturities rather than viewing IV rank as one universal number."),
("Volatility is dynamic", "IV can expand as price approaches a breakeven or liquidity deteriorates. Stress a further volatility rise instead of assuming today's elevated level is a ceiling."),
], "A straddle has vega −0.22, about −$22 per IV point. A four-point IV decline implies roughly $88 of theoretical benefit before delta, gamma, theta and skew effects.",
[("Does falling IV always produce profit?", "No; a large price move can dominate."),("Can high IV rise further?", "Yes."),("What is vega?", "Sensitivity to a one-point IV change, all else equal.")]),

guide("short-straddle-greeks", "Greeks", "Short Straddle Greeks: Delta, Gamma, Theta and Vega",
"Learn how delta, negative gamma, positive theta and negative vega interact in a short straddle.",
"The trade collects decay but sells convexity, so its directional exposure grows against the seller during a large move.", [
("Delta", "At initiation, call and put deltas may nearly offset. Delta does not stay neutral: a rally makes the position increasingly short delta, while a decline makes it increasingly long delta relative to the falling stock."),
("Gamma", "Negative gamma causes delta to change unfavorably as price moves. The effect becomes stronger near expiration and can make small market moves produce rapid P&L changes."),
("Theta", "Two short options commonly create positive theta. The daily estimate is not guaranteed income and can be overwhelmed by gamma loss or volatility expansion."),
("Vega", "Both short legs normally create negative vega. A volatility rise increases repurchase cost and often occurs at the same time as adverse price movement and wider bid-ask spreads."),
], "A straddle begins delta 0.02, gamma −0.06, theta +0.09 and vega −0.24 per share. After a rally, delta can become materially negative because of short gamma.",
[("Is delta always zero?", "No."),("Why is gamma negative?", "Both options are sold."),("Does positive theta guarantee profit?", "No.")]),

guide("theta-decay-short-straddle", "Theta", "Theta and Time Decay in a Short Straddle",
"Learn when time decay helps a short straddle and why gamma risk intensifies as expiration approaches.",
"Theta can accelerate near expiration, but the payment for that decay is exposure to increasingly sharp gamma and assignment risk.", [
("Decay profile", "ATM options often carry substantial extrinsic value, so a stable underlying can allow both legs to lose time value. Theta changes daily and with price and volatility."),
("Weekend effect", "Option prices may reflect expected non-trading days before the calendar arrives. Selling on Friday does not guarantee an automatic multi-day profit on Monday."),
("Gamma trade-off", "Short-dated options can show attractive theta, but their negative gamma is also concentrated. A late move can erase many days of collected decay quickly."),
("Expiration management", "Closing before the final session can reduce pin and assignment uncertainty. Compare remaining profit with the risk still carried rather than chasing the last few dollars."),
], "A straddle shows $18 of theta per day but can lose $250 from a rapid gamma-driven move. The daily decay estimate is small relative to the tail scenario.",
[("Is theta constant?", "No."),("Does a weekend guarantee decay profit?", "No."),("Why close early?", "To reduce gamma, pin and assignment risk.")]),

guide("short-straddle-expiration-selection", "Expiration", "Short Straddle Expiration and DTE Selection",
"Choose expiration using theta, gamma, event timing, liquidity and the holding period of a short straddle.",
"Shorter duration increases decay concentration and gamma risk; longer duration increases vega and time exposed to an unexpected move.", [
("Short DTE", "Near-term straddles decay rapidly when price is stable but react sharply to movement. There is little recovery time after a gap or move toward a breakeven."),
("Longer DTE", "More time generally produces a larger credit and more vega exposure. The position has slower gamma initially but remains exposed to news and volatility changes for longer."),
("Match the thesis", "Select an expiration that matches the forecast window and explicitly includes or excludes known catalysts. Do not choose duration from annualized premium alone."),
("Liquidity and exits", "Compare spreads and open interest across expirations. Establish a profit target, loss trigger and latest exit date before the final week's gamma becomes dominant."),
], "Compare 14-DTE and 45-DTE 100 straddles. The first has faster decay and sharper gamma; the second has more vega and more calendar time for an adverse event.",
[("Is shorter DTE safer?", "No."),("Why use more DTE?", "It may reduce initial gamma and provide more management time."),("Should expiration include earnings?", "Only intentionally.")]),

guide("short-straddle-margin-buying-power", "Capital", "Short Straddle Margin and Buying Power",
"Understand why undefined-risk margin can expand and how to stress buying power before selling a short straddle.",
"Displayed opening margin is not the maximum capital the trade can demand during volatility expansion or a large price move.", [
("Broker formulas", "Margin depends on account type, underlying value, option prices and broker policy. Portfolio margin and standard margin can produce very different requirements."),
("Expansion risk", "A rising stock increases short-call exposure; a falling stock increases short-put exposure. Higher IV can also raise option value and the broker's risk estimate simultaneously."),
("Liquidation risk", "If available buying power falls too far, the broker may close positions at unfavorable prices. Defined theoretical breakevens do not protect against forced liquidation."),
("Reserve policy", "Stress price gaps and volatility spikes across the entire portfolio. Keep a deliberate cash reserve and size from stressed loss and margin, not premium received."),
], "A trade opens with $4,000 margin but a market shock raises the requirement to $7,500 while the position loses value. Planning only for the opening figure creates forced-action risk.",
[("Is opening margin maximum risk?", "No."),("Can margin change overnight?", "Yes."),("How should size be chosen?", "Using stressed portfolio loss and buying power.")]),

guide("adjust-short-straddle", "Management", "How to Adjust a Short Straddle",
"Evaluate rolling the untested or tested side, moving the center, adding wings or closing a challenged short straddle.",
"An adjustment changes the trade; it does not erase loss, and every new credit must be weighed against added time and tail exposure.", [
("Close first", "Closing the complete position is a valid adjustment when the thesis fails or the loss limit is reached. It removes both gamma and volatility exposure rather than extending the decision."),
("Roll the untested side", "Moving the profitable option toward price can collect credit and rebalance delta, but it narrows the range and creates additional risk if price reverses."),
("Roll the tested side", "Moving the challenged strike or expiration can reposition risk for a debit or credit. Track all realized and unrealized cash flows instead of resetting the scorecard."),
("Add protection", "Buying wings can convert the trade into an iron butterfly or related defined-risk position. Protection has a cost and should be evaluated with realistic fills."),
], "Stock rallies from $100 to $108. Rolling the short put from 100 to 105 adds credit but places both short options closer to the new price and increases reversal risk.",
[("Does a roll remove loss?", "No."),("Must every trade be adjusted?", "No; closing may be better."),("Can wings define risk?", "Yes, if both tails are properly covered.")]),

guide("close-roll-short-straddle", "Exit", "When to Close or Roll a Short Straddle",
"Create objective profit, loss, volatility and time-based exit rules for a short straddle.",
"The remaining premium is compensation for remaining risk; closing early can be rational even when more theta is available.", [
("Profit target", "Many traders close after capturing a planned share of maximum credit instead of holding for the final amount. The exact target should reflect DTE, costs and portfolio risk."),
("Loss trigger", "Use a position or portfolio threshold defined before entry. Waiting for an expiration breakeven ignores interim volatility, margin and gap exposure."),
("Thesis invalidation", "Exit when the expected range, volatility forecast or catalyst assumption changes. A new forecast deserves a new trade analysis rather than an automatic roll."),
("Roll decision", "A roll closes the current options and opens later or different strikes. Compare it with closing and opening no new trade, including total credits, time added and tail risk."),
], "A straddle sold for $8 can be repurchased for $4 after volatility falls. Closing realizes 50% of maximum credit and removes the risk of a coming announcement.",
[("Why close before expiration?", "To exchange remaining profit potential for lower risk."),("Is a roll one transaction economically?", "It is a close plus a new position."),("Should breakeven be the only stop?", "No.")]),

guide("short-straddle-mistakes", "Risk Management", "Short Straddle Options Strategy: 12 Mistakes to Avoid",
"Avoid errors involving unlimited risk, IV, earnings, sizing, margin, adjustments, assignment and expiration.",
"The central mistake is treating collected premium as income without pricing the rare but potentially very large losses that fund it.", [
("Mistakes 1–3: risk", "Do not call the trade safe because it begins delta-neutral, size from maximum profit or assume the breakevens cap loss. Tail risk remains open."),
("Mistakes 4–6: volatility", "Do not sell only because IV is high, ignore event timing or assume volatility cannot rise further. Compare implied movement with scenario risk."),
("Mistakes 7–9: capital", "Do not use all buying power, ignore correlation or rely on opening margin. A volatility shock can expand losses and requirements across positions."),
("Mistakes 10–12: management", "Do not improvise rolls, hold for the last premium or ignore assignment and pin risk. Plan exit dates, loss limits and complete multi-leg orders."),
], "A trader sells several correlated straddles using most available margin. One market gap expands every position and the broker liquidates them into wide spreads.",
[("What is the biggest risk?", "Uncapped tail loss combined with leverage."),("Does delta-neutral stay neutral?", "No."),("Why reserve buying power?", "For stress, adjustments and orderly exits.")]),
]


def article_html(article: dict, index: int) -> str:
    base.ARTICLES = ARTICLES
    base.COURSE = COURSE
    base.DATE = "September 12, 2026"
    plan = f'''<h2 id="plan">Build a risk-first trading plan</h2>
<p>Before using {article["title"].lower()}, record the underlying price, strike, expiration, total credit and contract multiplier. Calculate both expiration breakevens, then model losses beyond them rather than stopping at the profitable range. The maximum credit is visible at entry, but the largest future loss is not.</p>
<p>Stress at least five underlying prices, a volatility increase and decrease, and several dates. Include a gap that cannot be adjusted intraday. Review delta, gamma, theta and vega at the position and portfolio level because several neutral premium trades can become directional together.</p>
<p>Define a profit target, maximum tolerated loss, margin reserve, event rule and latest exit date. Use a single multi-leg order where possible and verify both legs after every fill or adjustment. This process does not eliminate risk, but it makes the decision measurable and repeatable.</p>
<p>After the trade, record actual movement, volatility change, slippage and the largest directional exposure. Comparing those results with the original forecast helps separate sound execution from a lucky outcome and improves future duration, strike and position-size decisions.</p>'''
    return (base.article_html(article, index)
            .replace("2026-09-11", "2026-09-12")
            .replace("Learn Vega — Free", "Learn Short Straddles — Free")
            .replace("Vega &amp; Volatility", "Short Straddle")
            .replace("Vega planning example", "Short Straddle example")
            .replace("This simplified example holds other inputs constant to isolate volatility exposure.", "This simplified scenario focuses on expiration outcomes; live prices and risks will differ.")
            .replace("Level 6 – Short Straddle course", "Level 15 – Short Straddle course")
            .replace("Level 6 – Vega &amp; Volatility course", "Level 15 – Short Straddle course")
            .replace("Start Level 6 — Free", "Start Level 15 — Free")
            .replace("Free Level 6 Course", "Free Level 15 Course")
            .replace("Learn vega and volatility through structured lessons and practical examples.", "Learn Short Straddle construction, Greeks, risk and adjustments through structured lessons.")
            .replace('<h2 id="faq">Frequently asked questions</h2>', plan + '\n<h2 id="faq">Frequently asked questions</h2>')
            .replace('<a href="#example">Practical example</a><a href="#faq">FAQs</a>', '<a href="#example">Practical example</a><a href="#plan">Risk plan</a><a href="#faq">FAQs</a>')
            .replace("<span>5-minute read</span>", "<span>7-minute read</span>"))


def create_image(article: dict, index: int) -> None:
    image = Image.new("RGB", (1200, 675), "#07172d")
    draw = ImageDraw.Draw(image)
    accents = ["#ffbd16", "#51d5ff", "#8be39a", "#ff8b72", "#b995ff"]
    accent = accents[index % len(accents)]
    draw.ellipse((760, -250, 1350, 390), fill="#0d3152")
    draw.rounded_rectangle((720, 132, 1120, 535), 28, fill="#091f38", outline="#214767", width=3)
    fonts = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    bold = lambda size: ImageFont.truetype(fonts[0], size)
    regular = lambda size: ImageFont.truetype(fonts[1], size)
    draw.rounded_rectangle((62, 55, 242, 91), 18, fill=accent)
    draw.text((79, 64), f"LEVEL 15  •  GUIDE {index + 1:02}", font=bold(14), fill="#07172d")
    title = article["title"]
    lines = []
    for word in title.split():
        if not lines or len(lines[-1] + " " + word) > 28: lines.append(word)
        else: lines[-1] += " " + word
    for n, line in enumerate(lines[:4]): draw.text((62, 128 + n * 53), line, font=bold(37), fill="white")
    draw.text((62, 574), "OPTIONS AMERICA", font=bold(17), fill="white")
    draw.text((62, 601), "Short Straddle Learning Series", font=regular(13), fill="#8daac4")
    cx, cy = 920, 340
    draw.line((770, cy, 1070, cy), fill="#607d96", width=2)
    draw.line((cx, 190, cx, 490), fill="#607d96", width=2)
    if index in (6, 12):
        draw.line((790, 440, 920, 250, 1050, 440), fill=accent, width=8)
        draw.line((790, 440, 790, 390), fill="#51d5ff", width=5)
        draw.line((1050, 440, 1050, 390), fill="#51d5ff", width=5)
    elif index in (9, 10):
        for x, h, c in ((820, 95, "#51d5ff"), (875, 145, accent), (930, 80, "#8be39a"), (985, 165, "#ff8b72")):
            draw.rounded_rectangle((x, 445-h, x+34, 445), 6, fill=c)
    elif index in (13, 14):
        draw.arc((805, 235, 1035, 465), 30, 320, fill=accent, width=7)
        draw.line((920, 350, 1000, 292), fill="#51d5ff", width=6)
    else:
        draw.line((790, 220, 920, 430, 1050, 220), fill=accent, width=8)
        if index % 3 == 1: draw.ellipse((895, 405, 945, 455), outline="#51d5ff", width=5)
        if index % 3 == 2:
            draw.line((820, 255, 1020, 255), fill="#8be39a", width=4)
            draw.line((820, 425, 1020, 425), fill="#ff8b72", width=4)
    image.save(ROOT / "assets/images/blog" / f"{article['slug']}.webp", "WEBP", quality=88, method=6)


def update_index() -> None:
    path = BLOG / "index.html"
    source = path.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    if 'href="short-straddle-options-strategy-explained/"' not in source:
        source = source.replace(marker, "\n".join(base.card_html(a) for a in ARTICLES) + "\n" + marker, 1)
    source = source.replace("<strong>223</strong> guides", "<strong>239</strong> guides")
    if "Explore Level 15" not in source:
        source = source.replace('<a class="btn btn-gold" href="../courses/advanced-option-level-14-backspread/">Explore Level 14 →</a>', '<a class="btn btn-gold" href="../courses/advanced-option-level-14-backspread/">Explore Level 14 →</a><a class="btn btn-gold" href="../courses/advanced-option-level-15-short-straddle/">Explore Level 15 →</a>')
    path.write_text(source)


def update_scripts() -> None:
    path = BLOG / "blog.js"
    source = path.read_text().replace("const clusterPriority = card => card.textContent.includes('Backspread') ? 14 :", "const clusterPriority = card => card.textContent.includes('Short Straddle') ? 15 : card.textContent.includes('Backspread') ? 14 :")
    path.write_text(source)
    path = ROOT / "favicon.js"
    source = path.read_text()
    marker = "    'backspread-mistakes': '/assets/images/blog/backspread-mistakes.webp'"
    additions = ",\n".join(f"    '{a['slug']}': '/assets/images/blog/{a['slug']}.webp'" for a in ARTICLES)
    if "'short-straddle-options-strategy-explained'" not in source:
        source = source.replace(marker, marker + ",\n" + additions)
    path.write_text(source)


def update_existing_links() -> None:
    targets = ["option-greeks-straddles-strangles", "positive-theta-option-strategies", "vega-vs-theta-options", "theta-vs-gamma-near-expiration"]
    bridge = ('<p class="cluster-bridge"><strong>Neutral premium strategy:</strong> Read the '
              '<a href="../short-straddle-options-strategy-explained/">Short Straddle guide</a> and take the '
              '<a href="../../courses/advanced-option-level-15-short-straddle/">free Level 15 course</a>.</p>\n')
    for slug in targets:
        path = BLOG / slug / "index.html"
        if path.exists():
            source = path.read_text()
            if "../short-straddle-options-strategy-explained/" not in source:
                source = source.replace("</article>", bridge + "</article>", 1)
                path.write_text(source)


def main() -> None:
    base.ARTICLES = ARTICLES
    base.COURSE = COURSE
    for index, article in enumerate(ARTICLES):
        directory = BLOG / article["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(article_html(article, index))
        create_image(article, index)
    update_index(); update_scripts(); update_existing_links()


if __name__ == "__main__":
    main()
