#!/usr/bin/env python3
"""Build the Level 12 Butterfly Spread SEO cluster and original artwork."""

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
COURSE = "../../courses/advanced-option-level-12-butterfly/"


def guide(slug, tag, title, description, key, sections, example, faq):
    return dict(slug=slug, tag=f"Butterfly Spread · {tag}", title=title, description=description,
                key=key, sections=sections, example=example, faq=faq)


ARTICLES = [
guide("butterfly-spread-explained", "Complete Guide", "Butterfly Spread Explained: Strategy, Risk and Reward",
"Learn how a butterfly spread uses three strikes to create a defined-risk options position centered on a target price.",
"A standard long butterfly has limited risk, limited profit and its highest expiration value at the middle strike.", [
("The three-strike structure", "A long call butterfly buys one lower-strike call, sells two middle-strike calls and buys one higher-strike call with the same expiration. A put butterfly can create the same expiration shape using puts."),
("The market outlook", "The position fits a forecast that the underlying will move toward a specific target by expiration. It is not simply neutral: entry price relative to the body strike determines the initial directional exposure."),
("Defined payoff", "Maximum loss is generally the opening debit. Maximum profit for equal wings is the wing width minus that debit, reached at the middle strike at expiration. Two breakevens surround the body."),
("Before expiration", "Delta, gamma, theta, vega, skew and time affect all four contracts. The narrow expiration peak does not describe interim value, and reaching the body early does not guarantee maximum profit."),
], "Buy the 95 call, sell two 100 calls and buy the 105 call for a $1.20 debit. Maximum risk is $120 and maximum expiration profit at $100 is $380 before costs.",
[("Is a butterfly neutral?", "It targets a price area, although it can begin bullish or bearish relative to that target."),("Is risk unlimited?", "No. A standard long butterfly has defined debit risk."),("Where is maximum profit?", "At the middle strike at expiration.")]),

guide("how-to-build-butterfly-spread", "Step by Step", "How to Build a Butterfly Spread",
"Build a long butterfly by defining a price target, selecting three strikes and entering the four contracts as one limit order.",
"Choose the body strike from a forecast, then choose wing width and debit together rather than searching only for the cheapest butterfly.", [
("Define the target", "Estimate where the underlying may trade near expiration and why. The middle strike represents the payoff peak, so a vague range forecast is not enough to select the structure intelligently."),
("Choose the contracts", "For a call butterfly, buy the lower call, sell two calls at the body and buy the upper call. All legs normally share one underlying, expiration and contract multiplier."),
("Set equal or unequal wings", "Equal distances create a symmetrical butterfly. Unequal distances create a broken-wing structure with different risk and reward on each side and require separate calculations."),
("Use one multi-leg order", "Enter the position for a net limit debit and verify the 1:-2:1 ratio. Review liquidity at all strikes, commissions, assignment, expiration and the planned exit before sending."),
], "With stock at $98 and a $100 expiration target, a trader enters the 95/100/105 call butterfly for a $1.10 debit through one four-leg order.",
[("Why are two body options sold?", "They create the payoff peak and offset much of the wing cost."),("Must wings be equal?", "No, but unequal wings change the payoff."),("Should legs be entered separately?", "A combined order normally provides clearer debit and risk control.")]),

guide("butterfly-spread-profit-loss-breakevens", "Payoff", "Butterfly Spread Profit, Loss and Breakevens",
"Calculate maximum profit, maximum loss and the two expiration breakevens for a standard equal-wing long butterfly.",
"For an equal-wing debit butterfly, lower breakeven is lower strike plus debit and upper breakeven is upper strike minus debit.", [
("Maximum loss", "The opening net debit is generally the maximum expiration loss. It occurs below the lower strike or above the upper strike when the options offset or expire worthless, before transaction costs."),
("Maximum profit", "Subtract the debit from one wing's width. At the body strike at expiration, the lower long option has full wing-width intrinsic value while the other legs expire worthless or offset."),
("The two breakevens", "Add the debit to the lower strike and subtract it from the upper strike. These formulas assume equal widths and a debit entry; broken-wing and credit structures require side-specific analysis."),
("Probability and payoff", "A large theoretical return comes from a narrow peak, not free leverage. Compare the width of the profitable zone, time, forecast accuracy, liquidity and realistic exit price."),
], "A 50/55/60 call butterfly costs $1.40. Maximum loss is $140, maximum profit is $360, and expiration breakevens are $51.40 and $58.60.",
[("Can both sides lose?", "One final price can finish outside either side of the profit zone."),("Does maximum profit occur before expiration?", "Usually not exactly; remaining time value affects the legs."),("Do fees matter more here?", "They can, because four contracts are opened and closed.")]),

guide("butterfly-spread-example", "Worked Example", "Butterfly Spread Example With Full Payoff Scenarios",
"Walk through a long call butterfly across expiration prices below, near and above its three strikes.",
"A scenario table reveals the butterfly's narrow central reward and limited losses beyond both wings.", [
("Set up the example", "Assume shares trade at $98. Buy the 95 call, sell two 100 calls and buy the 105 call for a $1.25 debit, or $125 for one standard butterfly."),
("Below the lower strike", "At $95 or lower, all calls expire worthless and the debit is lost. At $97, the lower call is worth $2, so the position produces $75 before costs after subtracting the debit."),
("At and near the body", "At $100, the lower call is worth $5 and maximum profit is $375. At $102, the lower call is worth $7 and the two short calls lose $4 combined, leaving $3 intrinsic value and $175 profit."),
("Above the upper strike", "At $105 or higher, the long and short calls offset to zero net intrinsic value beyond the fixed widths. The $125 debit becomes the maximum loss."),
], "At expiration prices of $94, $97, $100, $102 and $106, approximate P&L is −$125, +$75, +$375, +$175 and −$125 before costs.",
[("Why does profit fall after $100?", "The two short body calls begin offsetting the lower long call faster."),("What happens at $105?", "The structure returns to zero intrinsic payoff before the debit."),("Can it be closed early?", "Yes, as a complete multi-leg position.")]),

guide("choose-butterfly-spread-strikes", "Strike Selection", "How to Choose Butterfly Spread Strikes",
"Choose the lower strike, body and upper strike using the target price, wing width, debit, delta, liquidity and desired profit zone.",
"The body is the expiration target; the wings determine the size and shape of the opportunity around that target.", [
("Select the body", "Place the middle strike near the price forecast for expiration, not automatically at the current stock price. Consider available strike increments and whether the target is realistic within the time selected."),
("Choose wing width", "Wider equal wings increase maximum intrinsic value but usually cost more and may change the profitable range. Narrow wings can offer large percentage returns while being more sensitive to fees and forecast error."),
("Use delta and probability carefully", "Delta can help describe current directional exposure, but it is not a fixed probability. Model several underlying prices because the butterfly's net delta changes sign around the body."),
("Check three markets", "The middle strike needs enough liquidity for two contracts, and both wings need executable quotes. Evaluate the combined bid-ask spread rather than relying on theoretical midpoint values."),
], "For a $100 target, compare 97.5/100/102.5, 95/100/105 and 90/100/110 butterflies. Each changes debit, profit zone and sensitivity.",
[("Must the body be ATM?", "No. It should reflect the forecast target."),("Are wider wings always better?", "No. They change cost and risk as well as reward."),("Why is body liquidity important?", "Two body contracts magnify slippage at that strike.")]),

guide("butterfly-spread-expiration-dte", "Expiration", "Butterfly Spread Expiration and DTE Selection",
"Choose butterfly expiration using the target's timing, theta, gamma, vega, event risk and time available for management.",
"Expiration must align with when the underlying is expected to approach the body, because timing is as important as direction.", [
("Near-term butterflies", "Short duration can provide inexpensive debit and fast payoff changes, but the profit tent narrows quickly and gamma becomes concentrated. A small timing error can move the final price outside the peak."),
("Longer-duration butterflies", "More time allows the thesis to develop and can reduce immediate gamma, but it normally increases debit and vega exposure. The underlying may pass through the target too early."),
("Event placement", "Earnings and macro events can create large moves and IV shifts. Decide whether the butterfly targets the event outcome, a post-event pin, or a move that occurs outside the event window."),
("Plan the exit date", "Many butterflies are closed before expiration because maximum theoretical profit is difficult to capture and assignment risk rises. Set a date for reassessment rather than relying only on price."),
], "If the target is based on a six-week catalyst, compare expirations seven, nine and twelve weeks away using live Greeks, debit and expected movement.",
[("What DTE is best?", "There is no universal number; match it to the thesis."),("Why not always choose the nearest date?", "The target may arrive after the payoff window collapses."),("Does more time guarantee safety?", "No. It adds cost and volatility exposure.")]),

guide("call-butterfly-vs-put-butterfly", "Comparison", "Call Butterfly vs Put Butterfly",
"Compare call and put butterflies with the same strikes through expiration payoff, debit, liquidity, assignment and capital treatment.",
"A call and put butterfly can share the same expiration payoff shape, but live pricing and operational details can differ.", [
("Equivalent shape", "A long call butterfly and long put butterfly using identical strikes and expiration can produce the same payoff at expiration under standard assumptions. Put-call parity links their theoretical values."),
("Pricing differences", "Dividends, interest rates, borrow conditions and bid-ask markets can create different executable debits. Compare complete orders instead of assuming quoted legs produce perfect parity."),
("Assignment exposure", "Both contain two short body options that can be assigned early if American-style and ITM. Call assignment interacts with dividends, while put assignment can create long shares."),
("Choose the cleaner market", "Prefer the version with better liquidity, tighter combined pricing and simpler account handling. The strategic forecast should not change merely because puts or calls look familiar."),
], "The 95/100/105 call butterfly and put butterfly may show nearly identical modeled expiration P&L, while their combined bid-ask spreads differ by $0.15.",
[("Are call and put butterflies identical?", "Their expiration payoff can be equivalent, but execution and assignment differ."),("Which is cheaper?", "Compare live net prices; there is no permanent winner."),("Can either be entered for a credit?", "Market pricing and structure may create unusual credits, which require careful payoff verification.")]),

guide("butterfly-vs-iron-butterfly", "Comparison", "Long Butterfly vs Short Iron Butterfly",
"Compare a long debit butterfly with a short iron butterfly across construction, profit zone, volatility exposure and risk profile.",
"The terms sound similar, but a long butterfly targets the body while a short iron butterfly collects credit for staying near its short strike.", [
("Construction", "A standard long call butterfly uses one option type and a 1:-2:1 ratio. A short iron butterfly sells an ATM straddle and buys an OTM put and call as protective wings."),
("Debit and credit", "The long butterfly normally pays a debit with that debit at risk. The short iron butterfly receives a credit, with maximum loss equal to wing width minus credit."),
("Greeks", "Both can profit near a central price, yet entry Greeks and volatility behavior differ by moneyness and pricing. The short iron butterfly often begins short vega and positive theta."),
("Avoid naming confusion", "Broker tickets may label structures differently. Verify exact strikes, quantities, option types, net price, maximum profit and maximum loss rather than trading from the strategy name."),
], "A 95/100/105 call butterfly costs $1.20. A 95-put/100-straddle/105-call iron butterfly receives a credit; both peak near $100 but have different cash flows and Greeks.",
[("Do both target one price?", "Their expiration maximum profit is centered on the body strike."),("Which receives credit?", "The short iron butterfly."),("Are risks the same?", "Not automatically; compare actual debit, credit and widths.")]),

guide("butterfly-vs-iron-condor", "Comparison", "Butterfly Spread vs Iron Condor",
"Compare a target-centered butterfly with a range-based iron condor across credit, profit zone, Greeks and forecast precision.",
"A butterfly concentrates reward near one body strike; an iron condor spreads smaller maximum profit across a wider central range.", [
("Expiration shape", "The long butterfly creates a triangular peak at its body and loses outside the wings. A short iron condor creates a flat maximum-profit zone between two separated short strikes and loses beyond its outer wings."),
("Forecast", "Use a butterfly when analysis supports a specific expiration target. Use an iron condor when the primary thesis is that price remains within a broader range rather than pinning one level."),
("Cash flow and Greeks", "A long butterfly normally pays a debit. A short iron condor receives credit and often starts positive theta and negative vega. Exact Greeks change with strikes and current price."),
("Management", "A butterfly may benefit from moving toward its body, while a condor is threatened near either short strike. Adjustment triggers and remaining reward therefore require different rules."),
], "At $100, a 95/100/105 butterfly peaks only at $100. A 90/95/105/110 iron condor can retain maximum profit anywhere from $95 through $105.",
[("Which has a wider maximum-profit zone?", "The iron condor."),("Which can offer a higher peak?", "A butterfly may, but only near its body."),("Are both defined-risk?", "Yes, when constructed and maintained correctly.")]),

guide("broken-wing-butterfly-explained", "Variation", "Broken Wing Butterfly Explained",
"Learn how unequal butterfly wings reshape debit, credit, breakevens, directional bias and maximum loss.",
"A broken-wing butterfly intentionally uses unequal strike distances, reducing or shifting risk on one side while increasing it on the other.", [
("How it differs", "A symmetrical butterfly has equal lower and upper wing widths. A broken-wing version moves one outer strike, so the expiration payoff is no longer balanced around the body."),
("Why traders use it", "The unequal wing can lower the debit, create a small credit or move a breakeven. That improvement is funded by greater exposure on the wider side, not by eliminating risk."),
("Calculate each side", "Do not use the standard equal-wing maximum-profit formula blindly. Map payoff at every strike and calculate the widest adverse interval, net debit or credit, and assignment outcomes."),
("Directional use", "Strike placement can express a bullish or bearish bias while still targeting the body region. The target, expected path and side of larger loss must agree with the thesis."),
], "A 95/100/108 call butterfly has a five-point lower wing and eight-point upper wing. It may cost less, but upside loss is no longer equal to downside debit risk.",
[("Is broken wing safer?", "Only on one side; the other side can carry more risk."),("Can it open for a credit?", "Sometimes, depending on widths and pricing."),("Are breakevens symmetrical?", "No. Calculate the actual payoff.")]),

guide("butterfly-spread-greeks", "Greeks", "Butterfly Spread Greeks: Delta, Gamma, Theta and Vega",
"Understand how the long wings and two short body options combine into butterfly delta, gamma, theta and vega.",
"Butterfly Greeks change sign around the body and evolve sharply near expiration, so entry values cannot describe the entire trade.", [
("Delta", "A butterfly placed above the stock can begin with positive delta as price moves toward the target. Above the body it can become negative delta, because additional upside moves away from the expiration peak."),
("Gamma", "Gamma can be positive outside portions of the structure and negative near the body, especially late in the cycle. This curvature makes delta change rapidly around the strikes."),
("Theta", "Time decay may help near the body as the position converges toward its central intrinsic value, but can hurt outside the profitable region as the debit decays toward zero."),
("Vega", "The two short body options often make the butterfly negative vega near the center, while the net profile can vary elsewhere. Model separate price, time and IV scenarios across all legs."),
], "A butterfly below its body begins with positive delta. After the stock crosses the target, delta turns negative, illustrating why its directional exposure is target-seeking rather than permanently bullish.",
[("Is butterfly delta neutral?", "Only at certain prices and moments."),("Is theta always positive?", "No. Location relative to the body matters."),("Can gamma be negative?", "Yes, particularly near the central peak.")]),

guide("implied-volatility-butterfly-spread", "Vega", "Implied Volatility and Vega in a Butterfly Spread",
"Learn how IV level, volatility crush, skew and surface changes can affect butterfly pricing and target selection.",
"A butterfly often benefits from volatility contraction near its body, but its vega changes with price, time and strike placement.", [
("Net vega", "Two short body options can outweigh the long-wing vega and create negative net exposure near the target. A volatility decline may help, while expansion can flatten the value concentration."),
("Price changes the exposure", "Far from the body, the long wing closest to the market may dominate and net vega can differ from the entry sign. Recalculate after meaningful movement instead of assuming permanent short vega."),
("Skew", "Each of the three strikes can trade at a different IV. Skew changes alter wing cost and can make an apparently symmetrical butterfly asymmetric in value and Greeks."),
("Events", "Post-earnings IV contraction can support a butterfly if price lands near the body, but a gap beyond the wings can still produce maximum loss. Model price and volatility jointly."),
], "A butterfly centered at $100 may gain from an IV decline if stock stays near $100. The same volatility crush cannot rescue it if shares gap to $112 beyond the upper wing.",
[("Does lower IV always help?", "No. Net vega changes and price location dominates."),("Why does skew matter?", "The three strikes may not reprice uniformly."),("Is a butterfly an earnings strategy?", "It can be, but gap risk and target precision are substantial.")]),

guide("theta-time-decay-butterfly-spread", "Theta", "Theta and Time Decay in a Butterfly Spread",
"See when passing time helps or hurts a butterfly and why theta changes sign around the central target region.",
"Time decay is favorable near the body and unfavorable outside much of the profit tent, especially as expiration approaches.", [
("Near the body", "When price is near the middle strike, the two short options can decay faster in total than the long wings. The butterfly may gain as its expiration payoff becomes more concentrated."),
("Outside the tent", "Below the lower breakeven or above the upper breakeven, passing time can push the position toward its maximum debit loss. A positive target forecast must also arrive on time."),
("Late-cycle acceleration", "Theta and gamma become highly sensitive near expiration. A favorable one-day decay estimate can be overwhelmed by a modest move away from the body."),
("Use a management date", "Decide how late the butterfly will be held and what value justifies closing. Waiting for a perfect expiration pin can risk a large open gain for a small theoretical remainder."),
], "A butterfly at its body has positive theta, but a move outside the upper breakeven changes the profile and daily decay begins working toward the debit loss.",
[("Is theta always positive?", "No."),("Why does time help at the body?", "Short body premium decays while central intrinsic structure remains."),("Should I hold for expiration?", "Not automatically; gamma and assignment risk increase.")]),

guide("adjust-butterfly-spread", "Adjustments", "How to Adjust a Butterfly Spread",
"Evaluate rolling the body, widening a wing, adding another butterfly or closing when the target or timing changes.",
"Every butterfly adjustment changes the target, debit, Greeks and loss zones; compare it with closing and opening a fresh trade.", [
("Close or reduce", "If the target thesis fails, closing is the simplest risk reduction. Defined debit does not justify holding an unattractive position until it becomes worthless."),
("Move the body", "Rolling the short body options toward a revised target changes the entire payoff and may be difficult to fill. Calculate the new combined position rather than viewing the roll credit alone."),
("Change a wing", "Widening or narrowing one side creates a broken-wing structure with asymmetric risk. Verify the new maximum loss and buying power before removing any protective option."),
("Add a second butterfly", "Another butterfly can broaden or split the target zone but adds contracts, commissions and overlapping Greeks. Stress test the combined payoff at all important strikes."),
], "A 95/100/105 butterfly misses as stock moves to $103. Adding a 100/105/110 butterfly broadens exposure, but also adds debit and a new set of risks rather than repairing the first trade for free.",
[("Must a losing butterfly be adjusted?", "No. Closing may be better."),("Can I roll only the body?", "Yes, but the resulting position must be recalculated."),("Does adding another butterfly reduce risk?", "Not necessarily; total debit and complexity increase.")]),

guide("when-to-close-butterfly-spread", "Management", "When to Close a Butterfly Spread",
"Plan price, profit, loss, time and event exits for a butterfly instead of depending on a perfect expiration pin.",
"Manage the butterfly by its executable value and remaining risk, not only by how close the stock is to the body strike.", [
("Profit target", "Consider closing after capturing a chosen portion of the maximum realistic value. Near the target, the last theoretical dollars may require holding concentrated gamma and assignment risk."),
("Target failure", "Exit or reassess if the expected price path, catalyst or timing is invalidated. The small defined debit can still represent a 100% position loss."),
("Time exit", "A target reached too early may not deliver the expiration peak because extrinsic values remain. Set a management date and compare current closing value with the risk of waiting."),
("Expiration risk", "Two short body options can be assigned, and pinning near a strike can produce uncertain stock positions. Close before expiration when exercise outcomes are not intended."),
], "A butterfly bought for $1.20 trades at $3.40 near the body with days remaining. Closing captures $220 while avoiding the risk of a fast move that returns it toward the $120 loss.",
[("Must I wait for the body strike?", "No. The position can be closed at any executable value."),("Why not hold for maximum profit?", "It is concentrated at one price at expiration."),("How is it closed?", "Use a closing multi-leg order and confirm all legs fill.")]),

guide("butterfly-spread-mistakes", "Risk Management", "Butterfly Spread: 12 Mistakes to Avoid",
"Avoid common butterfly errors involving target selection, wing width, debit, liquidity, Greeks, adjustments and expiration.",
"Limited debit risk does not make a butterfly easy; the strategy demands accuracy in price, timing, structure and execution.", [
("Mistakes 1–3: poor target", "Do not place the body without a forecast, assume neutral means any sideways price or choose expiration before the catalyst. Direction and timing must converge on the target."),
("Mistakes 4–6: construction", "Do not confuse call and iron butterflies, use the wrong 1:-2:1 ratio or apply equal-wing formulas to broken wings. Verify the full payoff before entry."),
("Mistakes 7–9: execution", "Do not ignore four-leg commissions, accept wide markets or trust midpoint values that cannot fill. Body-strike slippage is multiplied across two short contracts."),
("Mistakes 10–12: management", "Do not expect maximum profit before expiration, adjust without recalculating total risk or hold through pin and assignment risk unintentionally. Confirm every closing fill."),
], "A trader buys a cheap narrow butterfly with no time-specific target, sees the stock touch the body early and expects maximum profit. Remaining extrinsic value and later movement produce a loss.",
[("What is the most common mistake?", "Treating the payoff peak as easy to capture."),("Can a correct direction still lose?", "Yes, if timing or final price misses the tent."),("Why verify the ratio?", "One missing or extra body contract creates a different risk profile.")]),
]

base.ARTICLES = ARTICLES
base.COURSE = COURSE
base.DATE = "September 12, 2026"


def article_html(article: dict, index: int) -> str:
    return (base.article_html(article, index)
            .replace("2026-09-11", "2026-09-12")
            .replace("Learn Vega — Free", "Learn Butterfly Spreads — Free")
            .replace("Vega &amp; Volatility", "Butterfly Spreads")
            .replace("Vega planning example", "Butterfly spread example")
            .replace("This simplified example holds other inputs constant to isolate volatility exposure.", "This simplified example focuses on one structure and selected expiration outcomes.")
            .replace("Level 6 – Butterfly Spreads course", "Level 12 – Butterfly Spread course")
            .replace("Level 6 – Vega &amp; Volatility course", "Level 12 – Butterfly Spread course")
            .replace("Start Level 6 — Free", "Start Level 12 — Free")
            .replace("Free Level 6 Course", "Free Level 12 Course")
            .replace("Learn vega and volatility through structured lessons and practical examples.", "Learn Butterfly Spreads through structured lessons and practical examples."))


def update_index() -> None:
    path = BLOG / "index.html"
    source = path.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    if 'href="butterfly-spread-explained/"' not in source:
        source = source.replace(marker, "\n".join(base.card_html(a) for a in ARTICLES) + "\n" + marker, 1)
    source = source.replace("<strong>175</strong> guides", "<strong>191</strong> guides")
    source = source.replace("<strong>190</strong> guides", "<strong>191</strong> guides")
    if "Explore Level 12" not in source:
        source = source.replace('<a class="btn btn-gold" href="../courses/advanced-option-level-11-short-iron-condor/">Explore Level 11 →</a>', '<a class="btn btn-gold" href="../courses/advanced-option-level-11-short-iron-condor/">Explore Level 11 →</a><a class="btn btn-gold" href="../courses/advanced-option-level-12-butterfly/">Explore Level 12 →</a>')
    path.write_text(source)


def update_scripts() -> None:
    path = BLOG / "blog.js"
    source = path.read_text().replace("const clusterPriority = card => card.textContent.includes('Short Iron Condor') ? 11 :", "const clusterPriority = card => card.textContent.includes('Butterfly Spread') ? 12 : card.textContent.includes('Short Iron Condor') ? 11 :")
    path.write_text(source)
    path = ROOT / "favicon.js"
    source = path.read_text()
    marker = "    'short-iron-condor-mistakes': '/assets/images/blog/short-iron-condor-mistakes.webp'"
    additions = ",\n".join(f"    '{a['slug']}': '/assets/images/blog/{a['slug']}.webp'" for a in ARTICLES)
    if "'butterfly-spread-explained'" not in source:
        source = source.replace(marker, marker + ",\n" + additions)
    path.write_text(source)


def update_existing_links() -> None:
    targets = ["short-iron-condor-vs-iron-butterfly", "option-greeks-iron-condor", "gamma-near-expiration",
               "theta-vs-gamma-near-expiration", "option-greeks-debit-spreads", "short-iron-condor-explained"]
    bridge = ('<p class="cluster-bridge"><strong>Next strategy:</strong> Continue with the '
              '<a href="../butterfly-spread-explained/">Butterfly Spread guide</a> and the '
              '<a href="../../courses/advanced-option-level-12-butterfly/">free Level 12 course</a>.</p>\n')
    for slug in targets:
        path = BLOG / slug / "index.html"
        if path.exists():
            source = path.read_text()
            if "../butterfly-spread-explained/" not in source:
                path.write_text(source.replace('<p class="article-disclaimer">', bridge + '<p class="article-disclaimer">', 1))


def font(size: int, bold: bool = False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


def create_image(article: dict, index: int) -> None:
    image = Image.new("RGB", (1200, 675), "#071426")
    draw = ImageDraw.Draw(image)
    accents = ["#f6b81f", "#52d3ff", "#80e0a7", "#ff8e72", "#b89cff"]
    accent = accents[index % 5]
    for y in range(675):
        t = y / 675
        draw.line((0, y, 1200, y), fill=(7 + int(7*t), 20 + int(20*t), 38 + int(30*t)))
    draw.ellipse((760, -170, 1320, 390), fill="#0c3157")
    draw.ellipse((880, 360, 1280, 760), fill="#092746")
    draw.rounded_rectangle((58, 52, 310, 98), 20, fill=accent)
    draw.text((76, 63), f"LEVEL 12  •  GUIDE {index + 1:02d}", font=font(18, True), fill="#07172d")
    y = 145
    for line in textwrap.wrap(article["title"], width=24)[:4]:
        draw.text((62, y), line, font=font(42, True), fill="white")
        y += 50
    draw.text((64, 570), "OPTIONS AMERICA", font=font(22, True), fill="#b9c9da")
    draw.text((64, 605), "Butterfly Spread Learning Series", font=font(20), fill="#7892aa")
    draw.rounded_rectangle((720, 150, 1130, 505), 28, fill="#081c32", outline="#31506d", width=2)
    draw.line((760, 430, 1090, 430), fill="#6b8298", width=2)
    draw.line((925, 190, 925, 455), fill="#31506d", width=2)
    payoff = [(760, 430), (800, 430), (925, 235), (1050, 430), (1090, 430)]
    draw.line(payoff, fill=accent, width=8, joint="curve")
    if index == 1:
        for x, n in zip((800, 925, 1050), ("LONG", "2 SHORT", "LONG")):
            draw.ellipse((x-7, 423 if x != 925 else 228, x+7, 437 if x != 925 else 242), fill="white")
            draw.text((x-24, 195), n, font=font(12, True), fill=accent)
    elif index == 2:
        draw.line((820, 205, 820, 450), fill="#ff8e72", width=3)
        draw.line((1030, 205, 1030, 450), fill="#ff8e72", width=3)
        draw.text((870, 205), "PROFIT ZONE", font=font(14, True), fill="white")
    elif index == 3:
        for x, ydot in ((780, 430), (850, 350), (925, 235), (1000, 350), (1070, 430)):
            draw.ellipse((x-7, ydot-7, x+7, ydot+7), fill="#52d3ff")
    elif index == 4:
        for x in (800, 925, 1050): draw.line((x, 205, x, 450), fill="#31506d", width=2)
    elif index == 5:
        for x, label in ((770, "14D"), (875, "45D"), (990, "90D")):
            draw.rounded_rectangle((x, 195, x+65, 232), 10, outline=accent, width=2)
            draw.text((x+13, 205), label, font=font(13, True), fill="white")
    elif index == 6:
        draw.line([(760, 420), (800, 420), (925, 250), (1050, 420), (1090, 420)], fill="#52d3ff", width=4)
        draw.line([(760, 440), (800, 440), (925, 270), (1050, 440), (1090, 440)], fill="#ff8e72", width=4)
    elif index == 7:
        draw.line([(760, 430), (815, 430), (925, 260), (1035, 430), (1090, 430)], fill="#ff8e72", width=4)
        draw.text((865, 275), "DEBIT / CREDIT", font=font(13, True), fill="white")
    elif index == 8:
        draw.line([(760, 440), (810, 440), (855, 285), (995, 285), (1040, 440), (1090, 440)], fill="#52d3ff", width=4)
    elif index == 9:
        draw.line([(760, 430), (800, 430), (925, 235), (1080, 430)], fill="#ff8e72", width=5)
    elif index == 10:
        for x, h, c in ((770, 80, "#52d3ff"), (830, 130, accent), (890, 60, "#80e0a7"), (950, 110, "#ff8e72")):
            draw.rounded_rectangle((x, 445-h, x+34, 445), 8, fill=c)
    elif index == 11:
        for box, c in (((755, 205, 880, 350), "#52d3ff"), ((855, 220, 1015, 370), "#80e0a7"), ((980, 250, 1090, 355), "#ff8e72")):
            draw.arc(box, 5, 175, fill=c, width=4)
    elif index == 12:
        draw.arc((785, 205, 965, 385), 0, 300, fill="#52d3ff", width=5)
        draw.line((875, 295, 875, 237), fill="white", width=4)
        draw.line((875, 295, 920, 320), fill="white", width=4)
    elif index == 13:
        draw.line((805, 205, 1000, 205), fill="#52d3ff", width=5)
        draw.polygon([(1000, 205), (975, 189), (975, 221)], fill="#52d3ff")
        draw.line((1020, 350, 835, 350), fill="#ff8e72", width=5)
        draw.polygon([(835, 350), (860, 334), (860, 366)], fill="#ff8e72")
    elif index == 14:
        draw.rounded_rectangle((765, 390, 1080, 430), 10, fill="#123a55")
        draw.rounded_rectangle((875, 390, 1010, 430), 10, fill=accent)
        draw.text((893, 400), "CLOSE ZONE", font=font(14, True), fill="#07172d")
    elif index == 15:
        for x in (790, 925, 1060):
            draw.polygon([(x, 205), (x-24, 252), (x+24, 252)], outline="#ff8e72")
            draw.text((x-4, 219), "!", font=font(20, True), fill="#ff8e72")
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
