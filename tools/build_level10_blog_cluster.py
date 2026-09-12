#!/usr/bin/env python3
"""Build the Level 10 Bear Put Spread SEO cluster and original artwork."""

from __future__ import annotations

import importlib.util
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("level6_builder", ROOT / "tools/build_level6_blog_cluster.py")
base = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(base)
BLOG = ROOT / "blog"
COURSE = "../../courses/advanced-option-level-10-bear-put-spread/"


def guide(slug, tag, title, description, key, sections, example, faq):
    return dict(slug=slug, tag=f"Bear Put Spread · {tag}", title=title, description=description,
                key=key, sections=sections, example=example, faq=faq)


ARTICLES = [
guide("bear-put-spread-explained", "Complete Guide", "Bear Put Spread Explained: Strategy, Risk and Reward",
"Learn how a bear put spread combines a long put and a lower-strike short put to create a defined-risk bearish options position.",
"A bear put spread lowers the cost of a long put by selling another put, while the short strike limits the maximum profit.", [
("How the strategy is built", "Buy one put and sell another put on the same underlying and expiration, using a lower strike for the short leg. The higher-strike put normally costs more, so the position opens for a net debit."),
("The market outlook", "The strategy fits a moderately bearish forecast with a defined downside target. The best expiration outcome occurs at or below the short strike, where the spread reaches its full intrinsic width."),
("Defined profit and loss", "Maximum loss is generally the debit paid. Maximum profit equals the strike width minus the debit, multiplied by the contract multiplier. Expiration breakeven is the long strike minus the debit per share."),
("Before expiration", "Delta, gamma, theta, implied volatility and skew affect both legs. A payoff chart describes expiration only; the spread can trade above or below that path while time and uncertainty remain."),
], "Buy the 100 put for $6 and sell the 90 put for $2. The $4 debit creates a $400 maximum loss, $600 maximum profit and a $96 expiration breakeven.",
[("Is a bear put spread bearish?", "Yes. It normally has negative delta and benefits from a decline in the underlying."),("Can it lose more than the debit?", "A correctly maintained standard spread generally limits expiration loss to the debit plus costs."),("Why sell the lower put?", "It reduces cost and some Greek exposure, but caps profit below that strike.")]),

guide("how-to-build-bear-put-spread", "Step by Step", "How to Build a Bear Put Spread",
"Follow a practical process for selecting an underlying, buying the higher-strike put and selling the lower-strike put as one order.",
"Define the bearish target first, then build and price both legs as one position instead of treating them as separate trades.", [
("Write a measurable thesis", "State the expected decline, target price, catalyst and time window before opening the option chain. These assumptions determine whether the capped payoff is appropriate."),
("Select matching contracts", "Use the same underlying, expiration and contract multiplier. Buy the higher strike and sell the lower strike in equal quantity, then confirm the ticket identifies a vertical put debit spread."),
("Use a net-debit limit", "Submit both legs together with a limit price. Legging can expose the account to slippage, temporary naked risk and a very different debit from the one originally modeled."),
("Document the management plan", "Record maximum loss, maximum profit, breakeven, profit target, thesis exit, time exit and known events. Review liquidity, commissions, assignment and expiration procedures for both legs."),
], "With shares at $102 and a six-week target of $92, a trader buys the 100 put and sells the 90 put together for a $3.25 net debit.",
[("Which put is purchased?", "The higher-strike put is purchased and the lower-strike put is sold."),("Must quantities match?", "A standard one-to-one spread uses equal quantities."),("Why enter one order?", "It controls the net debit and avoids unintended single-leg exposure.")]),

guide("bear-put-spread-profit-loss-breakeven", "Payoff", "Bear Put Spread Profit, Loss and Breakeven",
"Calculate maximum profit, maximum loss and expiration breakeven for a bear put debit spread using its two strikes and net debit.",
"Every bear put spread should be reduced to three numbers before entry: debit at risk, capped reward and expiration breakeven.", [
("Maximum loss", "Maximum loss generally equals the debit when the underlying finishes at or above the long-put strike and both puts expire worthless. Include contract quantity and transaction costs."),
("Maximum profit", "Maximum profit is the distance between strikes minus the debit. At expiration it is reached at or below the short strike, subject to exercise, assignment and settlement mechanics."),
("Breakeven", "Subtract the net debit per share from the long-put strike. Before expiration there is no fixed breakeven because time value and implied volatility influence the closing value."),
("Reward versus probability", "A large maximum return does not prove that the trade is attractive. Compare target probability, liquidity, required move and time available alongside the payoff ratio."),
], "A 105/95 put spread costs $3.60. Maximum loss is $360, maximum profit is $640 and expiration breakeven is $101.40.",
[("Where is maximum profit reached?", "At expiration, generally at or below the short-put strike."),("Is breakeven fixed before expiration?", "No. Remaining extrinsic value changes the mark."),("Do fees change the calculation?", "Yes. They reduce profit and worsen the effective breakeven.")]),

guide("bear-put-spread-example", "Worked Example", "Bear Put Spread Example With Full Payoff Scenarios",
"Walk through one bear put spread across expiration prices above the long strike, between the strikes and below the short strike.",
"A scenario table makes the limited loss, declining-price profit zone and capped maximum reward easy to verify.", [
("Set up the example", "Assume shares trade at $100. Buy the 100 put for $5.40 and sell the 90 put for $1.90. The net debit is $3.50, or $350 for one standard spread."),
("Above the long strike", "At $100 or higher at expiration, both puts have no intrinsic value and the debit is lost. Between $100 and $96.50, the long put gains value but not enough to recover the debit."),
("Between the strikes", "At $94, the long put is worth $6 while the short put remains worthless. The spread is worth $600 and produces a $250 expiration profit after the initial debit."),
("Below the short strike", "At $90 or lower, the two puts together are worth the full $10 strike width. Maximum expiration profit is $650; a further stock decline cannot add intrinsic spread value."),
], "At expiration prices of $105, $96.50, $94 and $80, approximate P&L is −$350, $0, +$250 and +$650 before costs.",
[("What happens at $95?", "The spread is worth $5 at expiration, producing $150 after the $3.50 debit."),("Why is profit capped below $90?", "Additional long-put gains are offset by the short put."),("Can it be closed early?", "Yes, through a closing multi-leg order.")]),

guide("choose-bear-put-spread-strikes", "Strike Selection", "How to Choose Bear Put Spread Strikes",
"Choose long and short put strikes using the downside target, delta, debit, breakeven, width and probability profile.",
"The short strike should reflect a realistic downside target, while the long strike controls initial delta, cost and breakeven.", [
("Place the long strike", "An ITM long put usually has more negative delta and costs more. An OTM long put is cheaper but needs a larger decline. Compare breakeven and probability rather than premium alone."),
("Place the short strike", "The short put often sits near the forecast target. Moving it lower expands possible profit but collects less premium; moving it higher lowers cost while capping the trade sooner."),
("Choose the width", "Wider spreads offer more maximum value but normally require more debit. Narrow spreads can be dominated by commissions and bid-ask costs, especially when the expected move is uncertain."),
("Check liquidity and skew", "Evaluate executable prices, open interest and bid-ask width for both puts. Downside skew may make the lower-strike short put comparatively rich, materially changing the economics."),
], "With stock at $103 and a $92 target, compare 100/95, 100/90 and 95/90 spreads. Each produces different debit, breakeven and maximum reward.",
[("Should the short strike equal the target?", "It is a useful starting point, not a rule."),("Is an ITM spread safer?", "It may need a smaller decline, but the larger debit remains at risk."),("Why check skew?", "Put implied volatility often differs substantially across strikes.")]),

guide("choose-bear-put-spread-expiration", "Expiration", "How to Choose a Bear Put Spread Expiration",
"Match expiration to the bearish thesis while balancing time cost, theta, event risk, liquidity and the expected timing of the decline.",
"Buy enough time for the bearish thesis to develop, but avoid paying for duration that the planned trade cannot use.", [
("Match the catalyst", "Choose an expiration after the anticipated move with a buffer for timing uncertainty. A correct bearish forecast can still lose if the decline arrives after expiration."),
("Compare durations", "Near-term spreads cost less but carry faster gamma and theta changes. Longer-dated spreads may tolerate timing error but use more capital and can be more sensitive to volatility."),
("Review events", "Earnings, economic releases and dividends can change volatility and early-assignment risk. Model both the price reaction and the possible volatility decline after the event."),
("Set a time exit", "Decide when the trade will be reassessed if the decline does not occur. Exiting before the final days can reduce gamma, liquidity and expiration-management risk."),
], "For a bearish catalyst expected in five weeks, compare expirations six, eight and twelve weeks away using live debit, Greeks and open interest.",
[("Is the nearest expiration cheapest?", "Often, but it also provides the least time."),("Do longer spreads have more vega?", "Often, though the short leg offsets part of it."),("Must it be held to expiration?", "No. A planned early exit is common.")]),

guide("bear-put-spread-vs-long-put", "Comparison", "Bear Put Spread vs Long Put",
"Compare a put debit spread with buying one put across cost, downside potential, breakeven, theta, vega and target size.",
"The spread sacrifices profit from an extreme decline in exchange for a smaller debit and reduced volatility and time exposure.", [
("Cost and risk", "Selling the lower-strike put reduces the cash debit and maximum dollar loss. Both structures can still lose 100% of the amount paid if price finishes above the long strike."),
("Profit potential", "A long put can keep gaining as the underlying falls toward zero. The spread stops adding intrinsic value below its short strike, making it better suited to a defined moderate target."),
("Greeks", "The short put offsets part of the long put's negative delta, positive vega, positive gamma and negative theta. This smaller Greek footprint cuts both favorable and unfavorable sensitivity."),
("Decision framework", "Compare target range, implied volatility, time horizon, debit and liquidity. Do not choose the spread solely because it looks inexpensive; quantify the downside profit that is being sold."),
], "A $6 long put has broad downside participation. Selling a $2 lower-strike put creates a $4 spread, saving $200 while establishing a hard profit cap.",
[("Which has more downside profit potential?", "The standalone long put."),("Which usually has less negative theta?", "The bear put spread."),("Can both expire worthless?", "Yes, above the long-put strike.")]),

guide("bear-put-spread-vs-bear-call-spread", "Comparison", "Bear Put Spread vs Bear Call Spread",
"Compare bearish put debit and call credit spreads through payoff location, theta, vega, assignment and buying-power treatment.",
"Both are defined-risk bearish verticals, but debit versus credit and strike placement create different probabilities and exposures.", [
("Debit versus credit", "The bear put spread pays a debit and usually starts with negative theta and positive vega. The bear call spread receives a credit and often starts with positive theta and negative vega."),
("Required price path", "The put spread typically needs a decline through its breakeven. A call credit spread can profit if price stays below its breakeven, which may sit above the current market."),
("Assignment and expiration", "Each contains a short American-style option that may be assigned. Dividend exposure is especially relevant to short calls, while short puts can create share-purchase obligations."),
("Choose by thesis", "A stronger downside forecast or expected volatility expansion may support the put debit structure. A neutral-to-bearish forecast with rich volatility may better fit a call credit spread."),
], "Compare a 100/90 put debit spread with a 105/115 call credit spread. Both are bearish, but their winning price ranges and volatility exposures differ.",
[("Which receives cash at entry?", "The bear call spread normally receives a credit."),("Which benefits from rising IV?", "Often the bear put spread, depending on live net vega."),("Are they equivalent?", "Not unless strikes, expiration and pricing create a specific synthetic relationship.")]),

guide("bear-put-spread-vs-protective-put", "Comparison", "Bear Put Spread vs Protective Put",
"Compare a speculative bearish vertical spread with owning shares plus a protective put across objective, capital and downside exposure.",
"A bear put spread seeks profit from a decline; a protective put is insurance for stock that the investor already wants to own.", [
("Different starting positions", "The spread contains two puts and no shares. A protective put combines long stock with a long put, so the investor retains stock upside, dividends and voting rights."),
("Downside behavior", "The bear spread gains during a decline until its short strike. The protective put offsets stock losses below its strike but normally does not create a net bearish position."),
("Cost and capital", "A bear put spread risks only its debit. A protective put requires stock capital plus premium, although the put establishes a floor for the combined position during its life."),
("Use the correct objective", "Choose the spread for a standalone moderate-bearish thesis. Choose protection when the goal is to continue holding shares while limiting a temporary or event-driven drawdown."),
], "An investor with 100 shares buys a 95 put to insure the position. A separate 100/90 bear put spread instead profits from a forecast decline and owns no stock.",
[("Does a protective put profit from a crash?", "It mainly offsets stock losses below the strike."),("Does the bear spread own shares?", "No."),("Which preserves unlimited stock upside?", "The protective-put position, less the insurance cost.")]),

guide("bear-put-spread-greeks", "Greeks", "Bear Put Spread Greeks: Delta, Gamma, Theta and Vega",
"Understand the net Greeks of a bear put debit spread and how they evolve as price moves between and beyond its strikes.",
"Net Greeks equal the signed exposure of both puts; the short lower strike deliberately reduces the long put's sensitivity.", [
("Negative delta", "The higher-strike long put normally has more negative delta than the lower-strike short put contributes positively, leaving net negative delta. It can approach zero far above or below both strikes."),
("Gamma", "The long put adds positive gamma and the short put negative gamma. Net gamma is often positive near entry but changes with moneyness, volatility and time."),
("Theta and vega", "The spread commonly begins with modest negative theta and positive vega. Both are smaller than for the long put alone and can change sign in some price regions near expiration."),
("Calculate position exposure", "Multiply each leg's Greek by signed quantity and contract multiplier, then add the legs. Recalculate after price, time or volatility changes rather than treating entry Greeks as permanent."),
], "If the long put delta is −0.58 and the short put delta is −0.25, net spread delta is about −0.33, or roughly −33 share equivalents per standard spread.",
[("Is delta always negative?", "Normally, but it approaches zero at extreme prices."),("Is theta always negative?", "No. Its sign can change by moneyness and time."),("How is net vega found?", "Subtract the short put's vega from the long put's vega.")]),

guide("implied-volatility-bear-put-spread", "Volatility", "How Implied Volatility Affects a Bear Put Spread",
"Learn how volatility level, downside skew and event-driven IV changes affect both legs of a bear put debit spread.",
"The two puts offset much of the volatility exposure, but unequal strikes and downside skew can still move the spread materially.", [
("Net vega", "The long higher-strike put often carries more vega, leaving positive net exposure. A broad IV increase may support the spread, while contraction can offset part of a favorable price decline."),
("Downside skew", "Lower-strike puts frequently trade at higher implied volatility. Selling that rich lower strike can reduce net debit, but changes in skew may reprice the legs differently."),
("Earnings and volatility crush", "After an announcement, both puts may lose extrinsic value. The short leg provides a partial offset, yet price movement, changing delta and skew can dominate the result."),
("Run combined scenarios", "Model stock price, elapsed time and separate IV changes for each strike. A bearish move is not enough to predict exact P&L when volatility and time also change."),
], "With net vega of 0.08, one spread has about +$8 modeled exposure per IV point. A six-point contraction suggests roughly −$48 before delta, gamma and theta effects.",
[("Does rising IV always help?", "No. Net vega changes and price effects can dominate."),("Why does skew matter?", "Each strike can reprice at a different volatility."),("Does the short put remove IV risk?", "It reduces but does not necessarily eliminate it.")]),

guide("time-decay-bear-put-spread", "Theta", "Time Decay in a Bear Put Spread",
"See how theta changes when the underlying is above, between or below the two put strikes as expiration approaches.",
"A bear put spread has no permanent theta number; time can hurt or help depending on price relative to its payoff zone.", [
("Above the long strike", "When both puts are OTM, the long put often dominates and net theta is negative. A quiet or rising underlying can steadily erode the debit."),
("Between the strikes", "The theta profile can change quickly because the position is transitioning from uncertain time value toward intrinsic expiration value. Exact price relative to breakeven matters."),
("Below the short strike", "When both puts are ITM and the spread is near maximum value, passing time can help it converge toward full width. Early assignment and executable closing prices still require attention."),
("Plan a time stop", "Track both days remaining and thesis progress. Waiting for a late decline can expose the position to accelerating decay, while waiting for the final profit dollars adds reversal and expiration risk."),
], "A 100/90 spread below $88 may converge toward $10 as time passes, while the same spread above $100 can decay toward zero.",
[("Is theta always harmful?", "No. Below the short strike, time may help convergence."),("Does the short put reduce decay?", "It offsets part of the long put's theta."),("Why use a time stop?", "A delayed decline may no longer justify the remaining decay risk.")]),

guide("when-to-close-bear-put-spread", "Exit Planning", "When to Close a Bear Put Spread",
"Plan profit, loss, time and event exits for a bear put spread instead of automatically holding until expiration.",
"Base the closing decision on spread value, remaining reward and thesis validity—not on the underlying price alone.", [
("Profit exit", "Consider closing after capturing a chosen percentage of maximum profit, especially when little reward remains compared with reversal risk. Price the complete spread using executable markets."),
("Thesis or loss exit", "Close when the expected decline, catalyst or timing assumption is invalidated. Defined maximum loss is a boundary, not an instruction to lose the entire debit."),
("Time exit", "If the decline has not developed by the planned date, the remaining theta and gamma profile may be unattractive. Avoid repeatedly extending a failed forecast without a fresh analysis."),
("Expiration and assignment", "Close or actively manage ITM spreads before expiration when exercise and assignment are unwanted. Confirm that both legs filled and no residual option or share position remains."),
], "A $10-wide spread trades at $8.70 with two weeks left. Closing captures most of the available value and removes the risk that a sharp rebound erases the gain.",
[("Must it be held to expiration?", "No."),("How is it closed?", "Sell the long put and buy back the short put, preferably as one order."),("Why verify fills?", "A partial fill changes the exposure and can leave an unintended short put.")]),

guide("adjust-bear-put-spread", "Adjustments", "How to Adjust a Bear Put Spread",
"Evaluate closing, rolling or restructuring a bear put spread while treating every adjustment as a new risk decision.",
"An adjustment cannot erase the original loss; calculate the resulting position using total capital committed and current conditions.", [
("Consider closing first", "When the bearish thesis is broken, closing is often the clearest response. Added legs and repeated rolls can increase costs without improving expected value."),
("Roll in time", "Moving both puts to a later expiration buys time but may require another debit and introduce new volatility exposure. Include the original loss when evaluating the revised trade."),
("Change strikes", "Moving the short strike lower can reopen downside profit but costs money. Moving strikes higher may reduce the required decline while changing debit, width and probability."),
("Avoid accidental short-put risk", "Use multi-leg orders and verify quantities after fills. Closing the long put while the short put remains open can create substantial assignment and buying-power exposure."),
], "A losing 100/90 spread is rolled to a later expiration for an additional $1.30. Total risk now includes the original debit and the added cost, not only the new ticket price.",
[("Can rolling recover a loss?", "It creates a new opportunity, but the old loss remains in total P&L."),("Can I remove the short put?", "Yes, but that converts the trade into a more expensive long put."),("What is the simplest adjustment?", "Closing when the thesis fails.")]),

guide("bear-put-spread-mistakes", "Risk Management", "Bear Put Spread: 12 Mistakes to Avoid",
"Avoid common errors involving bearish targets, strikes, debit, volatility skew, liquidity, assignment and expiration.",
"Defined risk simplifies the boundary of loss, but it does not replace disciplined forecasting, execution and position management.", [
("Mistakes 1–3: construction", "Do not open without a price target, choose strikes only by cheap debit or ignore the resulting breakeven. A far-OTM spread can require an unrealistic decline."),
("Mistakes 4–6: execution", "Do not leg into the spread casually, rely on midpoint marks or ignore wide lower-strike put markets. Model realistic fills, commissions and slippage for opening and closing."),
("Mistakes 7–9: incomplete risk", "Do not assume a volatility rise is guaranteed during a decline, overlook skew changes or ignore short-put assignment. Defined payoff does not eliminate operational risk."),
("Mistakes 10–12: management", "Do not hold automatically for maximum profit, roll without counting total debit or close only one leg by mistake. Compare remaining reward with rebound and expiration risk."),
], "A trader buys a far-OTM narrow spread because its percentage return looks large, accepts a wide market and waits for expiration. Forecast, execution and time-decay errors compound.",
[("What is the most common mistake?", "Choosing strikes without a realistic downside target."),("Does a market decline guarantee profit?", "No. Size, timing, IV and entry debit matter."),("Why check both legs after closing?", "A partial fill can leave unintended long or short put exposure.")]),
]

base.ARTICLES = ARTICLES
base.COURSE = COURSE
base.DATE = "September 12, 2026"


def article_html(article: dict, index: int) -> str:
    html = base.article_html(article, index)
    return (html.replace("2026-09-11", "2026-09-12")
            .replace("Learn Vega — Free", "Learn Bear Put Spreads — Free")
            .replace("Vega &amp; Volatility", "Bear Put Spreads")
            .replace("Vega planning example", "Bear put spread example")
            .replace("This simplified example holds other inputs constant to isolate volatility exposure.", "This simplified example focuses on the spread at a specific moment and expiration outcome.")
            .replace("Continue the Vega &amp; Volatility cluster", "Continue the Bear Put Spread cluster")
            .replace("Level 6 – Bear Put Spreads course", "Level 10 – Bear Put Spread course")
            .replace("Level 6 – Vega &amp; Volatility course", "Level 10 – Bear Put Spread course")
            .replace("Start Level 6 — Free", "Start Level 10 — Free")
            .replace("Free Level 6 Course", "Free Level 10 Course")
            .replace("Learn vega and volatility through structured lessons and practical examples.", "Learn the Bear Put Spread through structured lessons and practical examples."))


def update_index() -> None:
    path = BLOG / "index.html"
    source = path.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    if 'href="bear-put-spread-explained/"' not in source:
        source = source.replace(marker, "\n".join(base.card_html(a) for a in ARTICLES) + "\n" + marker, 1)
    source = source.replace("<strong>145</strong> guides", "<strong>160</strong> guides")
    if "Explore Level 10" not in source:
        source = source.replace('<a class="btn btn-gold" href="../courses/advanced-option-level-9-bull-call-spread/">Explore Level 9 →</a>', '<a class="btn btn-gold" href="../courses/advanced-option-level-9-bull-call-spread/">Explore Level 9 →</a><a class="btn btn-gold" href="../courses/advanced-option-level-10-bear-put-spread/">Explore Level 10 →</a>')
    path.write_text(source)


def update_scripts() -> None:
    path = BLOG / "blog.js"
    source = path.read_text().replace("const clusterPriority = card => card.textContent.includes('Bull Call Spread') ? 9 :", "const clusterPriority = card => card.textContent.includes('Bear Put Spread') ? 10 : card.textContent.includes('Bull Call Spread') ? 9 :")
    path.write_text(source)
    path = ROOT / "favicon.js"
    source = path.read_text()
    marker = "    'bull-call-spread-mistakes': '/assets/images/blog/bull-call-spread-mistakes.webp'"
    additions = ",\n".join(f"    '{a['slug']}': '/assets/images/blog/{a['slug']}.webp'" for a in ARTICLES)
    if "'bear-put-spread-explained'" not in source:
        source = source.replace(marker, marker + ",\n" + additions)
    path.write_text(source)


def update_existing_links() -> None:
    targets = ["what-is-buying-a-put-option", "how-to-buy-a-put-option", "long-put-profit-loss-breakeven",
               "option-greeks-long-put", "implied-volatility-long-put", "bull-call-spread-explained"]
    bridge = ('<p class="cluster-bridge"><strong>Next strategy:</strong> Apply these concepts in the '
              '<a href="../bear-put-spread-explained/">Bear Put Spread guide</a>, then continue with the '
              '<a href="../../courses/advanced-option-level-10-bear-put-spread/">free Level 10 course</a>.</p>\n')
    for slug in targets:
        path = BLOG / slug / "index.html"
        if not path.exists():
            continue
        source = path.read_text()
        if "../bear-put-spread-explained/" not in source:
            source = source.replace('<p class="article-disclaimer">', bridge + '<p class="article-disclaimer">', 1)
            path.write_text(source)


def font(size: int, bold: bool = False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


def create_image(article: dict, index: int) -> None:
    image = Image.new("RGB", (1200, 675), "#071426")
    draw = ImageDraw.Draw(image)
    accents = ["#f6b81f", "#52d3ff", "#80e0a7", "#ff8e72", "#b89cff"]
    accent = accents[index % len(accents)]
    for y in range(675):
        t = y / 675
        draw.line((0, y, 1200, y), fill=(7 + int(7*t), 20 + int(20*t), 38 + int(30*t)))
    draw.ellipse((760, -170, 1320, 390), fill="#0c3157")
    draw.ellipse((880, 360, 1280, 760), fill="#092746")
    draw.rounded_rectangle((58, 52, 310, 98), 20, fill=accent)
    draw.text((78, 63), f"LEVEL 10  •  GUIDE {index + 1:02d}", font=font(18, True), fill="#07172d")
    y = 145
    for line in textwrap.wrap(article["title"], width=24)[:4]:
        draw.text((62, y), line, font=font(42, True), fill="white")
        y += 50
    draw.text((64, 570), "OPTIONS AMERICA", font=font(22, True), fill="#b9c9da")
    draw.text((64, 605), "Bear Put Spread Learning Series", font=font(20), fill="#7892aa")
    draw.rounded_rectangle((720, 150, 1130, 505), 28, fill="#081c32", outline="#31506d", width=2)
    draw.line((770, 300, 1085, 300), fill="#6b8298", width=2)
    draw.line((825, 190, 825, 465), fill="#6b8298", width=2)
    draw.line((940, 205, 940, 465), fill=accent, width=3)
    draw.text((792, 470), "SHORT", font=font(15, True), fill="#9bb1c5")
    draw.text((910, 470), "LONG", font=font(15, True), fill=accent)
    points = [(755, 235), (825, 235), (940, 405), (1085, 405)]
    if index in (1, 4):
        draw.line((755, 350, 1085, 350), fill="#274661", width=3)
    elif index == 2:
        draw.arc((770, 205, 1060, 450), 25, 155, fill="#52d3ff", width=4)
    elif index == 3:
        for x, ydot in ((785, 235), (875, 320), (1010, 405)):
            draw.ellipse((x-7, ydot-7, x+7, ydot+7), fill=accent)
    elif index == 5:
        for x, label in ((775, "14D"), (865, "45D"), (975, "90D")):
            draw.rounded_rectangle((x, 200, x+62, 235), 10, outline=accent, width=2)
            draw.text((x+12, 209), label, font=font(13, True), fill="white")
    elif index in (6, 7, 8):
        other = [(755, 415), (875, 330), (1085, 215)] if index != 7 else [(755, 405), (825, 405), (940, 245), (1085, 245)]
        draw.line(other, fill="#52d3ff" if index != 7 else "#ff8e72", width=4)
    elif index == 9:
        for x, h, color in ((775, 90, "#52d3ff"), (835, 130, accent), (895, 65, "#80e0a7"), (955, 108, "#ff8e72")):
            draw.rounded_rectangle((x, 420-h, x+34, 420), 8, fill=color)
    elif index == 10:
        for box, color in (((755, 210, 880, 350), "#52d3ff"), ((855, 225, 1015, 370), "#80e0a7"), ((980, 255, 1090, 355), "#ff8e72")):
            draw.arc(box, 5, 175, fill=color, width=4)
    elif index == 11:
        draw.arc((785, 220, 965, 400), 0, 300, fill="#52d3ff", width=5)
        draw.line((875, 310, 875, 252), fill="white", width=4)
        draw.line((875, 310, 920, 335), fill="white", width=4)
    elif index == 12:
        draw.rounded_rectangle((765, 350, 1080, 390), 10, fill="#123a55")
        draw.rounded_rectangle((880, 350, 1010, 390), 10, fill=accent)
        draw.text((895, 360), "EXIT ZONE", font=font(14, True), fill="#07172d")
    elif index == 13:
        draw.line((805, 220, 995, 220), fill="#52d3ff", width=5)
        draw.polygon([(995, 220), (970, 204), (970, 236)], fill="#52d3ff")
        draw.line((1010, 350, 835, 350), fill="#ff8e72", width=5)
        draw.polygon([(835, 350), (860, 334), (860, 366)], fill="#ff8e72")
    elif index == 14:
        for x in (790, 905, 1020):
            draw.polygon([(x, 205), (x-24, 252), (x+24, 252)], outline="#ff8e72")
            draw.text((x-4, 219), "!", font=font(20, True), fill="#ff8e72")
    draw.line(points, fill=accent, width=8, joint="curve")
    draw.ellipse((934, 399, 946, 411), fill="white")
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
