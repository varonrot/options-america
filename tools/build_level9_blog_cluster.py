#!/usr/bin/env python3
"""Build the Level 9 Bull Call Spread SEO cluster and its original artwork."""

from __future__ import annotations

import importlib.util
import math
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("level6_builder", ROOT / "tools/build_level6_blog_cluster.py")
base = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(base)
BLOG = ROOT / "blog"
COURSE = "../../courses/advanced-option-level-9-bull-call-spread/"


def guide(slug, tag, title, description, key, sections, example, faq):
    return dict(slug=slug, tag=f"Bull Call Spread · {tag}", title=title, description=description,
                key=key, sections=sections, example=example, faq=faq)


ARTICLES = [
guide("bull-call-spread-explained", "Complete Guide", "Bull Call Spread Explained: Strategy, Risk and Reward",
"Learn how a bull call spread combines a long call and a higher-strike short call to create a defined-risk bullish options position.",
"A bull call spread reduces the cost of a long call by selling another call, but the short call also caps the maximum profit.", [
("How the strategy is built", "Buy one call and sell another call on the same underlying and expiration, using a higher strike for the short leg. The position normally opens for a net debit because the lower-strike call costs more than the higher-strike call brings in."),
("The market outlook", "The strategy fits a moderately bullish forecast. It needs the underlying to rise, but it does not require unlimited upside. The best expiration outcome occurs at or above the short strike, where the spread reaches its maximum width."),
("Defined profit and loss", "Maximum loss is generally the debit paid. Maximum profit is the strike width minus that debit, multiplied by the contract multiplier. The expiration breakeven is the long strike plus the debit per share."),
("What changes before expiration", "Before expiration, delta, gamma, theta and implied volatility affect both legs. The spread may trade below its eventual intrinsic value because time remains, and closing prices can differ from a simple expiration diagram."),
], "Buy the 100 call for $6 and sell the 110 call for $2. The net debit is $4, maximum loss is $400, maximum profit is $600 and the expiration breakeven is $104.",
[("Is a bull call spread bullish?", "Yes. It generally has positive delta and benefits from a rise in the underlying."),("Can it lose more than the debit?", "A standard spread entered and maintained correctly generally limits expiration loss to the debit plus costs."),("Why not buy only the call?", "The short call lowers cost and some Greek exposure, but caps the upside.")]),

guide("how-to-build-bull-call-spread", "Step by Step", "How to Build a Bull Call Spread",
"Follow a practical process for selecting the underlying, buying the lower strike, selling the higher strike and entering the spread as one order.",
"Build and price the spread as a single defined-risk position rather than treating its two calls as unrelated trades.", [
("Start with a specific thesis", "Define the expected direction, target price and time window before opening the option chain. A vague bullish view makes it difficult to choose strikes or judge whether the spread's capped reward is sufficient."),
("Choose matching contracts", "Both calls should normally use the same underlying, expiration and contract multiplier. Buy the lower strike and sell the higher strike in equal quantity. Confirm that the order ticket shows a vertical call debit spread."),
("Set a limit debit", "Enter the position as one multi-leg limit order. The natural and midpoint prices can change quickly, and legging into the trade can create temporary naked exposure, directional slippage and execution risk."),
("Record the complete plan", "Before sending the order, write down maximum loss, maximum profit, breakeven, target exit, time exit and the event calendar. Check commissions, assignment features and liquidity for both legs."),
], "A trader expects a stock at $98 to reach about $108 within six weeks. The trader buys the 100 call and sells the 110 call together, paying a $3.20 net debit through one vertical-spread order.",
[("Which call is purchased?", "The lower-strike call is purchased and the higher-strike call is sold."),("Must the quantities match?", "A standard one-to-one bull call spread uses equal quantities."),("Should the legs be entered separately?", "A combined limit order usually provides clearer risk control than legging.")]),

guide("bull-call-spread-profit-loss-breakeven", "Payoff", "Bull Call Spread Profit, Loss and Breakeven",
"Calculate the maximum profit, maximum loss and expiration breakeven of a bull call debit spread using its strikes and net debit.",
"The spread's expiration payoff is determined by two strikes and one net debit; calculate all three outputs before entry.", [
("Maximum loss", "Maximum loss generally equals the net debit paid when both options expire worthless. Multiply the per-share debit by the contract multiplier and number of spreads, then add transaction costs."),
("Maximum profit", "Maximum profit equals the distance between strikes minus the debit. It is reached at expiration when the underlying is at or above the short strike, subject to exercise, assignment and settlement."),
("Breakeven", "The expiration breakeven is the long-call strike plus the net debit per share. Breakeven before expiration is not fixed because remaining time value and implied volatility affect both option prices."),
("Reward-to-risk", "Compare maximum profit with maximum loss, but do not confuse a favorable ratio with a high probability. Strike placement, time and volatility determine how likely each outcome may be."),
], "A 50/55 call spread costs $1.80. Maximum loss is $180, maximum profit is ($5 − $1.80) × 100 = $320, and expiration breakeven is $51.80.",
[("Where is maximum profit reached?", "At expiration, it is generally reached at or above the short-call strike."),("Is breakeven the same before expiration?", "No. Before expiration, extrinsic value can shift the mark."),("Do commissions matter?", "Yes. They reduce profit and increase the effective loss and breakeven.")]),

guide("bull-call-spread-example", "Worked Example", "Bull Call Spread Example With Full Payoff Scenarios",
"Walk through a bull call spread from entry to expiration across prices below, between and above its two strikes.",
"A scenario table reveals the capped payoff more clearly than focusing on the premium of either option alone.", [
("Set up the example", "Assume shares trade at $100. Buy the 100 call for $5.50 and sell the 110 call for $2.00. The spread costs $3.50, or $350 for one standard contract spread."),
("Below the long strike", "If the stock finishes below $100, both calls expire worthless and the $350 debit is lost. Between $100 and $103.50, the long call has intrinsic value but not enough to recover the full debit."),
("Between the strikes", "At $106, the long call is worth $6 and the short call expires worthless. The spread value is $600, creating a $250 expiration profit after subtracting the original $350 debit."),
("Above the short strike", "At $110 or higher, the spread is worth its full $10 width. Maximum expiration profit is $650. Additional stock upside no longer increases the spread's intrinsic value."),
], "At expiration prices of $95, $103.50, $106 and $115, the spread's P&L is approximately −$350, $0, +$250 and +$650 respectively, before costs.",
[("What happens at $105?", "The spread is worth $5 at expiration, producing $150 profit after a $3.50 debit."),("Why is profit capped above $110?", "Gains on the long call are offset by losses on the short call."),("Can the spread be closed early?", "Yes. Sell the spread using a closing multi-leg order.")]),

guide("choose-bull-call-spread-strikes", "Strike Selection", "How to Choose Bull Call Spread Strikes",
"Choose long and short call strikes using the price target, delta, debit, breakeven, spread width and desired probability profile.",
"The short strike should reflect a realistic target, while the long strike controls cost, delta and downside risk.", [
("Place the long strike", "An ITM long call usually creates higher delta and a larger debit. An OTM long call is cheaper but requires a stronger move. Compare the resulting breakeven and not just the quoted premium."),
("Place the short strike", "The short strike often sits near the forecast target. Moving it higher increases possible profit but collects less premium; moving it lower reduces cost but caps the trade sooner."),
("Choose the width", "Wider spreads generally offer more potential value and require more debit. Narrow spreads may show attractive percentage returns but can be more sensitive to execution costs and require price to finish in a smaller payoff zone."),
("Check both markets", "Review bid-ask spreads, open interest and executable prices for both legs. A liquid long call cannot compensate for a wide or difficult short leg."),
], "With stock at $98 and a $108 target, compare 100/105, 100/110 and 105/110 spreads. Each has a different debit, breakeven, maximum profit and probability profile.",
[("Should the short strike equal the target?", "It is a useful starting point, not a rule."),("Are ITM spreads safer?", "They may have higher delta and cost; risk still equals the debit."),("Does a wider spread always earn more?", "It raises the cap but also commonly costs more.")]),

guide("choose-bull-call-spread-expiration", "Expiration", "How to Choose a Bull Call Spread Expiration",
"Match expiration to the bullish thesis while balancing time cost, theta, liquidity, event risk and the timing of the expected move.",
"Expiration should leave enough time for the thesis to work without buying substantially more time than the trade can use.", [
("Match the catalyst window", "Select an expiration after the expected move or catalyst, with a buffer for timing uncertainty. An expiration before the thesis develops turns a correct directional idea into a losing trade."),
("Compare short and long duration", "Near-term spreads cost less in absolute dollars but can carry faster-changing gamma and theta. Longer-dated spreads may be more forgiving on timing but tie up more debit and react differently to volatility."),
("Review the event calendar", "Earnings and other announcements can inflate implied volatility in specific expirations. Model both the price move and post-event volatility change rather than assuming bullish direction alone determines the result."),
("Plan the time exit", "Many traders choose to close before the final expiration days to reduce gamma, assignment and execution risk. The chosen exit date should be part of the original trade plan."),
], "If a product decision is expected in five weeks, compare expirations six, eight and twelve weeks away. Measure debit, Greeks and liquidity instead of automatically choosing the nearest date.",
[("Is the nearest expiration best?", "Not automatically; it leaves less time for the forecast to develop."),("Do longer spreads have more vega?", "They often carry more volatility sensitivity, though the two legs offset part of it."),("Should I hold to expiration?", "Not necessarily. Early closing can reduce operational risk.")]),

guide("bull-call-spread-vs-long-call", "Comparison", "Bull Call Spread vs Long Call",
"Compare a call debit spread with buying one call across cost, maximum profit, breakeven, Greeks and the size of the expected move.",
"The spread exchanges unlimited call upside for lower cost and reduced exposure to time decay and implied volatility.", [
("Cost and maximum loss", "A bull call spread normally costs less because the short call offsets part of the long-call premium. Maximum loss is lower in dollars, but both positions can lose 100% of their debit."),
("Upside potential", "A long call has uncapped upside above breakeven, while the spread stops gaining intrinsic value above the short strike. The spread is better aligned with a defined, moderate price target."),
("Greek exposure", "Selling the higher strike reduces positive delta, gamma and vega as well as negative theta. That smaller Greek profile can make the spread less sensitive to both favorable and unfavorable changes."),
("Decision framework", "Choose based on target range, volatility view, time horizon and acceptable debit. Do not choose the spread only because it appears cheaper; understand what upside has been sold."),
], "A $6 long call may offer unlimited upside, while selling a $2 higher-strike call creates a $4 spread. The $2 savings also creates a firm profit ceiling.",
[("Which has more upside?", "The standalone long call has uncapped upside."),("Which has lower theta?", "The spread often has less negative net theta."),("Can both lose everything paid?", "Yes, if they expire below the long strike.")]),

guide("bull-call-spread-vs-bull-put-spread", "Comparison", "Bull Call Spread vs Bull Put Spread",
"Compare two defined-risk bullish vertical spreads through debit versus credit, payoff, assignment, volatility and buying-power treatment.",
"Both can express a bullish view, but their strike placement and debit-or-credit structure create different paths and operational risks.", [
("Debit versus credit", "A bull call spread is usually opened for a debit with calls. A bull put spread is usually opened for a credit with puts. Cash flow at entry does not determine whether one strategy is safer."),
("Payoff location", "A bull call spread needs price above its breakeven to profit at expiration. A bull put spread can profit if price stays above its breakeven, which may sit below the current stock price depending on its strikes."),
("Greeks and volatility", "Both normally have positive delta. Their theta and vega profiles can differ materially: the call debit spread often begins with negative theta and positive vega, while the put credit spread often reverses those signs."),
("Assignment and capital", "American-style short options can be assigned before expiration. Broker buying-power treatment, dividends and exercise outcomes should be compared before choosing between equivalent-looking spreads."),
], "A trader can compare a 100/110 call debit spread with a 100/90 put credit spread. Both are bullish, but the stock levels required for maximum profit and the time-volatility exposures differ.",
[("Are the strategies identical?", "No. They may be synthetically related in some configurations, but strikes and pricing matter."),("Which receives premium?", "The bull put spread normally opens for a credit."),("Which has positive theta?", "Often the bull put spread, but live Greeks can change.")]),

guide("bull-call-spread-vs-covered-call", "Comparison", "Bull Call Spread vs Covered Call",
"Compare a defined-risk call debit spread with stock plus a short call across capital, downside exposure, dividends and return profile.",
"A covered call owns stock and retains substantial downside risk; a bull call spread limits risk to its debit and does not own shares.", [
("Position construction", "The bull call spread uses two calls and no stock. A covered call owns 100 shares per standard short call. These are different capital and portfolio exposures even when both have capped upside."),
("Downside risk", "The spread's loss is limited to the debit. A covered call can lose substantially if the shares decline; the premium only provides a small downside cushion relative to stock ownership."),
("Income and participation", "A covered call can receive dividends and behaves largely like stock below the short strike. A call spread has a nonlinear payoff and may expire worthless if price does not exceed the long strike."),
("Choose by objective", "Use capital, stock-ownership intent, downside tolerance, tax considerations and target price to compare them. Neither strategy is simply a higher-yield version of the other."),
], "At $100, a covered call may require roughly $10,000 of stock before premium, while a 100/110 call spread may risk only its several-hundred-dollar debit.",
[("Does a covered call have defined risk?", "Its upside is capped, but stock downside remains substantial."),("Does the spread receive dividends?", "No, option ownership does not create shareholder dividend rights."),("Which uses less capital?", "The call spread commonly requires much less upfront capital.")]),

guide("bull-call-spread-greeks", "Greeks", "Bull Call Spread Greeks: Delta, Gamma, Theta and Vega",
"Understand the net Greeks of a bull call debit spread and how they change as price moves between the long and short strikes.",
"The spread's Greeks are the signed sum of both calls, and the short leg deliberately reduces the long call's sensitivity.", [
("Positive delta", "The long lower-strike call usually has more delta than the short higher-strike call, leaving positive net delta. Delta may increase as price enters the spread, then shrink as both calls become deep ITM."),
("Gamma and curvature", "The long call contributes positive gamma and the short call negative gamma. Net gamma changes with price and time, so the spread's directional response is not constant."),
("Theta and vega", "A bull call spread often begins with modest negative theta and positive vega, both smaller than a standalone long call. Their signs can change in some price regions, especially near expiration."),
("Rho and position scale", "Interest-rate exposure is generally modest and partly offset. Multiply every quoted Greek by signed quantity and contract multiplier, and recalculate as the underlying, IV and time change."),
], "If the long call has delta 0.58 and the short call has delta 0.27, the spread has about +0.31 net delta, or roughly +31 share equivalents per standard spread.",
[("Is delta always positive?", "It is normally positive for a standard bull call spread, but approaches zero at extreme prices."),("Does the spread have theta decay?", "Often yes, though less than the long call alone and not with a fixed sign everywhere."),("How is net vega calculated?", "Subtract the short call's vega from the long call's vega.")]),

guide("implied-volatility-bull-call-spread", "Volatility", "How Implied Volatility Affects a Bull Call Spread",
"Learn how changes in implied volatility affect both legs of a call debit spread and why net vega is smaller than a long call's.",
"The two calls partially offset volatility exposure, but unequal strikes mean an IV change can still affect the spread materially.", [
("Net positive vega", "At many entries, the lower-strike long call has greater vega than the higher-strike short call, leaving positive net vega. A broad IV rise may help, while a decline may hurt."),
("Skew matters", "The two strikes can trade at different implied volatilities and may not reprice equally. A change in call skew can move the spread even when an average IV number appears stable."),
("Events and volatility crush", "After earnings, both calls may lose extrinsic value. The short call offsets part of that decline, but the price gap and changing deltas can dominate the net result."),
("Model combined scenarios", "Test stock price, time and volatility together. A bullish move with an IV decline can still produce a gain, while a small move may be insufficient after decay and volatility crush."),
], "A spread with net vega 0.07 has about +$7 of modeled exposure per IV point per standard spread. A five-point decline implies roughly −$35 before delta, gamma and theta.",
[("Does higher IV always help?", "Not always; net vega can change and price movement may dominate."),("Does the short call remove vega?", "It reduces rather than necessarily eliminates vega."),("What is skew risk?", "The two strikes may experience different IV changes.")]),

guide("time-decay-bull-call-spread", "Theta", "Time Decay in a Bull Call Spread",
"See how theta affects both calls and why time can hurt, help or have little effect depending on price relative to the strikes.",
"A bull call spread does not have one permanent theta number; its decay profile changes as price and expiration approach.", [
("Below the long strike", "When both calls are OTM, the spread often has negative theta because the long call carries more value and sensitivity. A quiet underlying can steadily erode the debit."),
("Between the strikes", "Time decay remains sensitive to the exact price. Near expiration, intrinsic value begins to dominate, and net theta can change quickly as the probability of finishing within the spread shifts."),
("Above the short strike", "When both calls are ITM and the spread is near maximum value, the passage of time may help the spread converge toward full width. Execution prices and early-assignment considerations still matter."),
("Use a time exit", "Track days remaining and the percentage of maximum profit already captured. Waiting for the final dollars can expose the position to sharp gamma and give back a large portion of an open gain."),
], "A 100/110 spread worth $8.80 with the stock above $112 may gain toward $10 as time passes, while the same spread below $100 can decay toward zero.",
[("Is theta always negative?", "No. Its sign can change with price and time."),("Does the short call reduce decay?", "It offsets part of the long call's negative theta."),("Why avoid the final days?", "Gamma and assignment risk can become concentrated.")]),

guide("when-to-close-bull-call-spread", "Exit Planning", "When to Close a Bull Call Spread",
"Create profit, loss, time and event exits for a bull call spread instead of relying on hope or holding automatically to expiration.",
"A complete entry includes a closing plan based on spread value, thesis validity and remaining risk—not only a stock-price target.", [
("Profit target", "Consider closing after capturing a chosen portion of maximum profit, especially when little additional reward remains relative to the risk of reversal. Use an executable spread price rather than the stock price alone."),
("Loss or thesis exit", "Exit when the original price or timing thesis is invalidated. The defined maximum loss is a boundary, not a requirement to hold until every dollar is lost."),
("Time-based exit", "If the expected move has not appeared by a selected date, remaining theta and gamma may no longer justify staying. A time stop prevents repeated extensions of a failed forecast."),
("Events and expiration", "Close or reassess before earnings, dividends or expiration when those risks were not part of the plan. Use a multi-leg limit order and confirm both legs have closed."),
], "A spread has reached $8.50 of its $10 maximum value with two weeks remaining. Closing realizes most of the opportunity while removing the risk of losing that gain during a reversal.",
[("Must I hold until expiration?", "No. Bull call spreads can be closed before expiration."),("How is the spread closed?", "Sell the long call and buy back the short call, normally as one order."),("What if only one leg fills?", "The remaining option changes the risk profile, so order status must be checked.")]),

guide("adjust-bull-call-spread", "Adjustments", "How to Adjust a Bull Call Spread",
"Evaluate closing, rolling or restructuring a bull call spread while recognizing that every adjustment creates a new trade with new risk.",
"An adjustment cannot erase an existing loss; judge the resulting position on its own expected return, cost and risk.", [
("Start with closing", "The simplest response to a broken thesis is often to close the spread. Complexity is not automatically superior, and transaction costs can turn repeated adjustments into a larger loss."),
("Rolling in time", "Moving both legs to a later expiration buys more time but usually requires a new debit or changes the payoff. Recalculate total capital committed, not just the latest roll price."),
("Changing strikes", "Rolling the short call higher can reopen upside but may cost money and increase long-premium exposure. Moving strikes lower may reduce required movement but can crystallize losses or narrow remaining reward."),
("Avoid accidental exposure", "Use multi-leg orders where possible and verify quantities after every fill. Closing only the short leg leaves a long call; closing only the long leg can leave an uncovered short call."),
], "A 100/110 spread is losing because the stock stayed at $98. Rolling to a later 100/110 spread for another $1.40 raises total capital at risk; the new trade must justify that added debit.",
[("Can rolling recover a loss?", "It can create a new opportunity, but the original loss remains part of total P&L."),("Should I remove the short call?", "That creates a long call with higher cost and uncapped upside."),("What is the safest adjustment?", "Often closing is the clearest defined action when the thesis fails.")]),

guide("bull-call-spread-mistakes", "Risk Management", "Bull Call Spread: 12 Mistakes to Avoid",
"Avoid common bull call spread errors involving strikes, debit, liquidity, earnings, assignment, expiration and position management.",
"Defined risk does not remove the need for price discipline, execution planning and careful management of both option legs.", [
("Mistakes 1–3: weak construction", "Do not choose strikes without a target, focus only on a cheap debit or ignore the resulting breakeven. A low-cost spread can still have a low probability of producing meaningful value."),
("Mistakes 4–6: execution", "Do not leg into the position casually, use illiquid strikes or evaluate only midpoint marks. Model realistic fills and include commissions across opening and closing two-leg orders."),
("Mistakes 7–9: incomplete risk", "Do not ignore earnings volatility, assume maximum profit arrives before expiration or treat the debit as the only operational risk. Early assignment and expiration mechanics still require attention."),
("Mistakes 10–12: poor management", "Do not hold automatically for the last dollar, adjust without recalculating total risk or leave one leg open by mistake. Confirm fills and compare remaining reward with reversal risk."),
], "A trader buys a far-OTM narrow spread because the percentage return looks large, ignores a wide bid-ask market and holds through expiration. The forecast, execution and operational risks compound.",
[("What is the most common mistake?", "Choosing strikes by maximum percentage return without a realistic target and fill."),("Can defined risk be unmanaged?", "Yes. Defined loss does not make the trade suitable or efficient."),("Why check both legs after closing?", "A partial fill can leave unintended long or short option exposure.")]),
]


base.ARTICLES = ARTICLES
base.COURSE = COURSE
base.DATE = "September 12, 2026"


def article_html(article: dict, index: int) -> str:
    return (base.article_html(article, index)
            .replace("2026-09-11", "2026-09-12")
            .replace("Learn Vega — Free", "Learn Bull Call Spreads — Free")
            .replace("Vega &amp; Volatility", "Bull Call Spreads")
            .replace("Vega planning example", "Bull call spread example")
            .replace("This simplified example holds other inputs constant to isolate volatility exposure.", "This simplified example focuses on the spread at a specific moment and expiration outcome.")
            .replace("Continue the Vega &amp; Volatility cluster", "Continue the Bull Call Spread cluster")
            .replace("Level 6 – Vega &amp; Volatility course", "Level 9 – Bull Call Spread Strategy course")
            .replace("Level 6 – Bull Call Spreads course", "Level 9 – Bull Call Spread Strategy course")
            .replace("Start Level 6 — Free", "Start Level 9 — Free")
            .replace("Free Level 6 Course", "Free Level 9 Course")
            .replace("Learn vega and volatility through structured lessons and practical examples.", "Learn the Bull Call Spread through structured lessons and practical examples."))


def card_html(article: dict) -> str:
    return base.card_html(article)


def update_index() -> None:
    path = BLOG / "index.html"
    source = path.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    if 'href="bull-call-spread-explained/"' not in source:
        source = source.replace(marker, "\n".join(card_html(a) for a in ARTICLES) + "\n" + marker, 1)
    source = source.replace("<strong>130</strong> guides", "<strong>145</strong> guides")
    if "Explore Level 9" not in source:
        source = source.replace('<a class="btn btn-gold" href="../courses/option-greeks-level-8-option-greeks-in-action/">Explore Level 8 →</a>', '<a class="btn btn-gold" href="../courses/option-greeks-level-8-option-greeks-in-action/">Explore Level 8 →</a><a class="btn btn-gold" href="../courses/advanced-option-level-9-bull-call-spread/">Explore Level 9 →</a>')
    path.write_text(source)


def update_scripts() -> None:
    path = BLOG / "blog.js"
    source = path.read_text().replace("const clusterPriority = card => card.textContent.includes('Greeks') ? 8 :", "const clusterPriority = card => card.textContent.includes('Bull Call Spread') ? 9 : card.textContent.includes('Greeks') ? 8 :")
    path.write_text(source)


def update_existing_links() -> None:
    targets = [
        "option-greeks-debit-spreads",
        "option-greeks-long-call",
        "how-to-buy-a-call-option",
        "implied-volatility-options-explained",
        "calculate-option-time-decay-theta",
    ]
    bridge = ('<p class="cluster-bridge"><strong>Apply the concept:</strong> See how these ideas work together '
              'in the <a href="../bull-call-spread-explained/">Bull Call Spread guide</a>, then continue with the '
              '<a href="../../courses/advanced-option-level-9-bull-call-spread/">free Level 9 course</a>.</p>\n')
    for slug in targets:
        path = BLOG / slug / "index.html"
        if not path.exists():
            continue
        source = path.read_text()
        if "../bull-call-spread-explained/" not in source:
            source = source.replace('<p class="article-disclaimer">', bridge + '<p class="article-disclaimer">', 1)
            path.write_text(source)
    path = ROOT / "favicon.js"
    source = path.read_text()
    marker = "    'option-greeks-mistakes': '/assets/images/blog/option-greeks-mistakes.webp'"
    additions = ",\n".join(f"    '{a['slug']}': '/assets/images/blog/{a['slug']}.webp'" for a in ARTICLES)
    if "'bull-call-spread-explained'" not in source:
        source = source.replace(marker, marker + ",\n" + additions)
    path.write_text(source)


def font(size: int, bold: bool = False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


def create_image(article: dict, index: int) -> None:
    width, height = 1200, 675
    image = Image.new("RGB", (width, height), "#061426")
    draw = ImageDraw.Draw(image)
    accent = ["#f6b81f", "#52d3ff", "#80e0a7", "#ff8e72", "#b89cff"][index % 5]
    for y in range(height):
        t = y / height
        draw.line((0, y, width, y), fill=(6 + int(6*t), 20 + int(18*t), 38 + int(30*t)))
    draw.ellipse((760, -170, 1320, 390), fill="#0c3157")
    draw.ellipse((880, 360, 1280, 760), fill="#092746")
    draw.rounded_rectangle((58, 52, 310, 98), 20, fill=accent)
    draw.text((78, 63), f"LEVEL 9  •  GUIDE {index + 1:02d}", font=font(19, True), fill="#07172d")
    wrapped = textwrap.wrap(article["title"], width=24)
    y = 145
    for line in wrapped[:4]:
        draw.text((62, y), line, font=font(42, True), fill="white")
        y += 50
    draw.text((64, 570), "OPTIONS AMERICA", font=font(22, True), fill="#b9c9da")
    draw.text((64, 605), "Bull Call Spread Learning Series", font=font(20), fill="#7892aa")

    x0, y0, x1, y1 = 720, 150, 1130, 505
    draw.rounded_rectangle((x0, y0, x1, y1), 28, fill="#081c32", outline="#31506d", width=2)
    draw.line((770, 440, 1085, 440), fill="#6b8298", width=2)
    draw.line((825, 190, 825, 465), fill="#6b8298", width=2)
    draw.line((940, 205, 940, 465), fill=accent, width=3)
    draw.text((792, 470), "LONG", font=font(15, True), fill="#9bb1c5")
    draw.text((910, 470), "SHORT", font=font(15, True), fill=accent)
    variant = index
    if variant == 0:
        points = [(755, 410), (825, 410), (940, 255), (1085, 255)]
    elif variant == 1:
        points = [(755, 405), (825, 405), (940, 245), (1085, 245)]
        draw.line((755, 330, 1085, 330), fill="#274661", width=2)
    elif variant == 2:
        points = [(755, 420), (825, 420), (940, 275), (1085, 275)]
        draw.arc((775, 220, 1050, 455), 205, 335, fill="#52d3ff", width=3)
    elif variant == 3:
        points = [(755, 395), (825, 395), (940, 235), (1085, 235)]
        for x in (790, 865, 1015): draw.ellipse((x-6, 325-6, x+6, 325+6), fill=accent)
    elif variant == 4:
        points = [(755, 425), (825, 425), (940, 290), (1085, 290)]
        for x in range(760, 1080, 42): draw.line((x, 210, x+18, 210), fill="#31506d", width=2)
    elif variant == 5:
        points = [(755, 405), (825, 405), (940, 250), (1085, 250)]
        for x, label in ((785, "7D"), (880, "30D"), (1000, "60D")):
            draw.rounded_rectangle((x, 205, x + 54, 238), 10, outline=accent, width=2)
            draw.text((x + 12, 213), label, font=font(13, True), fill="white")
    elif variant == 6:
        points = [(755, 410), (825, 410), (940, 255), (1085, 255)]
        draw.line([(755, 390), (875, 300), (1085, 205)], fill="#52d3ff", width=4)
    elif variant == 7:
        points = [(755, 415), (825, 415), (940, 265), (1085, 265)]
        draw.line([(755, 250), (825, 250), (940, 405), (1085, 405)], fill="#ff8e72", width=4)
    elif variant == 8:
        points = [(755, 420), (825, 420), (940, 280), (1085, 280)]
        draw.line([(755, 405), (900, 320), (1085, 210)], fill="#52d3ff", width=4)
        draw.ellipse((1035, 194, 1069, 228), outline="#52d3ff", width=3)
    elif variant == 9:
        points = [(755, 420), (825, 420), (940, 280), (1085, 280)]
        for x, h, color in ((775, 82, "#52d3ff"), (835, 126, accent), (895, 62, "#80e0a7"), (955, 104, "#ff8e72")):
            draw.rounded_rectangle((x, 410-h, x+34, 410), 8, fill=color)
    elif variant == 10:
        points = [(755, 420), (825, 420), (940, 275), (1085, 275)]
        draw.arc((760, 220, 870, 350), 180, 355, fill="#52d3ff", width=4)
        draw.arc((865, 205, 1010, 365), 180, 355, fill="#80e0a7", width=4)
        draw.arc((985, 245, 1090, 345), 180, 355, fill="#ff8e72", width=4)
    elif variant == 11:
        points = [(755, 415), (825, 415), (940, 270), (1085, 270)]
        draw.arc((785, 220, 965, 400), 0, 300, fill="#52d3ff", width=5)
        draw.line((875, 310, 875, 252), fill="white", width=4)
        draw.line((875, 310, 920, 335), fill="white", width=4)
    elif variant == 12:
        points = [(755, 420), (825, 420), (940, 275), (1085, 275)]
        draw.rounded_rectangle((765, 225, 1080, 265), 10, fill="#123a55")
        draw.rounded_rectangle((880, 225, 1010, 265), 10, fill=accent)
        draw.text((895, 235), "EXIT ZONE", font=font(14, True), fill="#07172d")
    elif variant == 13:
        points = [(755, 420), (825, 420), (940, 275), (1085, 275)]
        draw.line((805, 230, 995, 230), fill="#52d3ff", width=5)
        draw.polygon([(995, 230), (970, 214), (970, 246)], fill="#52d3ff")
        draw.line((1010, 335, 835, 335), fill="#ff8e72", width=5)
        draw.polygon([(835, 335), (860, 319), (860, 351)], fill="#ff8e72")
    else:
        points = [(755, 425), (825, 425), (940, 290), (1085, 290)]
        for x in (790, 905, 1020):
            draw.polygon([(x, 218), (x-24, 265), (x+24, 265)], outline="#ff8e72")
            draw.text((x-4, 232), "!", font=font(20, True), fill="#ff8e72")
    draw.line(points, fill=accent, width=8, joint="curve")
    draw.ellipse((934, points[2][1]-6, 946, points[2][1]+6), fill="white")
    image.save(ROOT / "assets/images/blog" / f"{article['slug']}.webp", "WEBP", quality=88, method=6)


def main() -> None:
    for index, article in enumerate(ARTICLES):
        directory = BLOG / article["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(article_html(article, index))
        create_image(article, index)
    update_index()
    update_scripts()
    update_existing_links()


if __name__ == "__main__":
    main()
