#!/usr/bin/env python3
"""Build the Level 14 Backspread SEO cluster and original artwork."""

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
COURSE = "../../courses/advanced-option-level-14-backspread/"


def guide(slug, tag, title, description, key, sections, example, faq):
    return dict(slug=slug, tag=f"Backspread · {tag}", title=title, description=description,
                key=key, sections=sections, example=example, faq=faq)


ARTICLES = [
guide("backspread-options-strategy-explained", "Complete Guide", "Backspread Options Strategy Explained",
"Learn how a ratio backspread uses more long options than short options to create asymmetric exposure to a large market move.",
"A backspread normally sells fewer options at one strike and buys more options farther OTM, creating a defined loss zone and strong convexity beyond it.", [
("The asymmetric ratio", "The common 1-by-2 structure sells one option and buys two options of the same type at another strike and expiration. More long contracts than short contracts create positive convexity when price moves far enough."),
("Call and put versions", "A call backspread targets a strong upside move by selling a lower-strike call and buying more higher-strike calls. A put backspread targets a sharp decline by selling a higher-strike put and buying more lower-strike puts."),
("The dangerous middle", "The trade is not simply a cheap long-volatility position. Its largest expiration loss often occurs near the strike of the extra long options, where the short option has intrinsic loss but the long options have not yet created enough value."),
("Volatility and path", "Positive gamma and vega can support the trade, but direction, speed, time decay, skew and entry credit or debit all matter. A modest move into the loss valley can be worse than no move at all."),
], "Sell one 100 call and buy two 105 calls for a small credit. A large rally above the upper breakeven creates uncapped upside, while expiration near $105 can produce the maximum loss.",
[("Is a backspread unlimited risk?", "A standard call backspread has uncapped upside profit and a defined loss valley; verify the exact structure."),("Why buy more options than are sold?", "The extra long option creates convex exposure beyond the purchased strike."),("Can it open for a credit?", "Yes, although pricing can also require a debit.")]),

guide("call-ratio-backspread-explained", "Call Strategy", "Call Ratio Backspread Explained",
"Understand the 1-by-2 call backspread, its upside potential, downside result, maximum-loss area and two breakevens.",
"A call ratio backspread is a bullish volatility strategy whose best outcome requires a move well above the long-call strike.", [
("Construction", "Sell one lower-strike call and buy two higher-strike calls with the same expiration. The lower short-call premium finances part or all of the two OTM long calls."),
("Expiration outcomes", "Below the short strike, all calls expire worthless and the result is the initial credit or debit. Between strikes, the short call loses intrinsic value while both long calls remain worthless, creating the loss slope."),
("Above the long strike", "The two long calls gain twice as fast as the single short call loses. Net exposure becomes one additional long call, so upside profit is theoretically unlimited after the upper breakeven."),
("Operational risk", "The short call may be assigned early, particularly around dividends. If one long call is sold or expires differently, the intended ratio and risk can change substantially."),
], "Sell one 100 call for $6 and buy two 105 calls for $2.90 each. The $0.20 credit is retained below $100, maximum loss occurs at $105 and upside profit grows above the upper breakeven.",
[("Is it bullish?", "Yes, it seeks a large upside move."),("Can it profit if stock falls?", "A credit entry can retain a small profit below the short strike."),("Where is the worst price?", "Near the long-call strike at expiration.")]),

guide("put-ratio-backspread-explained", "Put Strategy", "Put Ratio Backspread Explained",
"Learn how selling one higher-strike put and buying more lower-strike puts creates convex downside exposure.",
"A put ratio backspread targets a sharp decline while concentrating its expiration loss near the lower long-put strike.", [
("Construction", "Sell one higher-strike put and buy two lower-strike puts with the same expiration. The short put helps finance the additional downside options."),
("Above the short strike", "All puts can expire worthless. The result is the opening credit retained or the debit lost, depending on how the spread was priced."),
("Between the strikes", "The short higher-strike put gains intrinsic loss while the long puts remain OTM. This produces the loss valley and makes a modest decline potentially worse than no decline."),
("Below the long strike", "Two long puts begin gaining against one short put, leaving net exposure similar to one additional long put. Profit grows as price falls, although the underlying cannot decline below zero."),
], "Sell one 100 put for $5.50 and buy two 95 puts for $2.60 each. The $0.30 credit can remain above $100, while a large decline below the lower breakeven creates the desired payoff.",
[("Is downside profit unlimited?", "No, because the underlying cannot fall below zero, but it can be substantial."),("Can a small decline lose?", "Yes, especially near the long-put strike."),("Is assignment possible?", "Yes. The short higher-strike put may be assigned.")]),

guide("how-to-build-ratio-backspread", "Step by Step", "How to Build a Ratio Backspread",
"Build a call or put backspread by defining the extreme-move thesis, selecting strikes, choosing the ratio and controlling the net price.",
"Design the loss valley first and confirm it fits the risk budget before focusing on the backspread's attractive tail payoff.", [
("Define direction and catalyst", "Choose call options for a large upside thesis or puts for a large downside thesis. Identify the catalyst, expected timing and move size that could carry price beyond the upper or lower breakeven."),
("Choose the short strike", "The short option provides financing but creates assignment and intermediate-price risk. Its strike should relate to current price and the point where the forecast begins."),
("Choose long strike and ratio", "Buy more contracts farther OTM, commonly two for every one sold. Wider strike distance may lower cost but enlarges the loss valley and requires a bigger move."),
("Enter as one order", "Use a ratio-spread limit order and verify signed quantities carefully. Record the maximum loss, both relevant breakevens, margin treatment, assignment plan and exit rules."),
], "For an earnings upside thesis, a trader sells one 100 call and buys two 110 calls. Before entry, the trader models the maximum loss at $110 and the rally needed for recovery.",
[("Is 1-by-2 mandatory?", "No, but other ratios change exposure and risk."),("Why not leg into it?", "A partial fill can leave an uncovered short option."),("What should be calculated first?", "The maximum loss zone and breakevens.")]),

guide("ratio-backspread-profit-loss-breakevens", "Payoff", "Ratio Backspread Profit, Loss and Breakevens",
"Calculate the expiration credit or debit result, maximum-loss zone and far-move breakeven of a 1-by-2 backspread.",
"The maximum loss is concentrated near the long-option strike; the far breakeven depends on strike width and net entry price.", [
("Quiet-side result", "Below both call strikes or above both put strikes, all options expire worthless. A net credit is retained; a net debit becomes the loss. This is the backspread's flat quiet-side outcome."),
("Maximum loss", "At the long-option strike, the short option has intrinsic loss equal to the strike width while the long options have no intrinsic value. Offset that amount by the opening credit or debit."),
("Far breakeven", "For a credit call backspread, upper breakeven is long strike plus strike width minus credit. For a credit put backspread, the lower breakeven is long strike minus strike width plus credit."),
("Beyond breakeven", "Two long options change value against one short option, leaving one net long option. Call upside is uncapped; put downside is limited only by the underlying reaching zero."),
], "A 100/105 1-by-2 call backspread entered for a $0.20 credit has $480 maximum loss at $105 and an upper breakeven near $109.80 before costs.",
[("Why can it have two profitable regions?", "A credit can profit on the quiet side and again after a large move."),("Are formulas identical for debit entries?", "No. Include the debit with the correct sign."),("Do commissions matter?", "Yes, three contracts are opened and closed per unit.")]),

guide("ratio-backspread-example", "Worked Example", "Ratio Backspread Example With Full Payoff Scenarios",
"Walk through a 1-by-2 call backspread at expiration across prices below, between and far above its strikes.",
"Scenario analysis exposes the middle loss valley that can be hidden by the strategy's unlimited upside headline.", [
("Set up the trade", "Stock is $100. Sell one 100 call for $6.20 and buy two 105 calls for $3 each. The position opens for a $0.20 credit, or $20 per standard ratio."),
("At or below $100", "All calls expire worthless and the $20 credit is retained. This small outcome does not compensate for a move that stops in the middle loss region."),
("Between $100 and $105", "Only the short call has intrinsic value. At $103 it loses $300, so net expiration loss is $280 after the original credit."),
("At and above $105", "Maximum loss is $480 at $105. At $110 the short call loses $1,000 while the two long calls gain $1,000, leaving the $20 credit. Above $110, net profit grows dollar for dollar with stock."),
], "Approximate P&L at $98, $103, $105, $110 and $115 is +$20, −$280, −$480, +$20 and +$520 before costs.",
[("Why is $105 worst?", "The short call is fully five points ITM while both long calls have zero intrinsic value."),("When does upside accelerate?", "Once price moves beyond the long strike."),("Can it be closed early?", "Yes, as a complete ratio order.")]),

guide("choose-backspread-option-ratio", "Position Ratio", "How to Choose a Backspread Option Ratio",
"Compare 1-by-2, 1-by-3 and other backspread ratios through debit, gamma, vega, delta and maximum loss.",
"More long options increase convexity and cost while changing both the quiet-side result and the size of the middle loss.", [
("The common 1-by-2", "Selling one option and buying two creates one net long option beyond the long strike. It is the simplest backspread ratio and provides a clear payoff for analysis."),
("Higher long ratios", "Buying three or more options can create stronger gamma and vega but usually requires more debit. The position may lose on the quiet side and can become highly sensitive to volatility changes."),
("Contract multiplier and scale", "A ratio describes relative quantities, not position size. A 5-by-10 position has the same ratio as 1-by-2 but five times the exposure, costs and assignment complexity."),
("Broker and liquidity limits", "Confirm margin treatment and that all strikes can fill in the intended ratio. Body-leg slippage and partial fills can leave uncovered short exposure."),
], "A 1-by-2 call backspread costs $0.10, while 1-by-3 costs $2.40. The additional long call improves far-upside convexity but creates a much larger quiet-side debit loss.",
[("Is a higher ratio safer?", "No. It changes cost and exposure rather than universally reducing risk."),("Does 2-by-4 differ from 1-by-2?", "The payoff shape is scaled to twice the size."),("Why check margin?", "Broker treatment can change with ratios and fills.")]),

guide("choose-backspread-strikes", "Strike Selection", "How to Choose Backspread Strikes",
"Choose short and long backspread strikes using the catalyst target, expected move, option skew, credit and maximum-loss zone.",
"Strike distance controls financing and the width of the dangerous middle region, so farther OTM is not automatically better.", [
("Place the short strike", "The short strike can be ATM or ITM to raise financing, but this also increases assignment and directional exposure. Relate it to where the forecast begins, not premium alone."),
("Place the long strike", "The long strike should be reachable under the large-move thesis. Moving it farther away reduces option cost but widens the maximum-loss interval and pushes the profitable tail farther out."),
("Use skew", "Call and put skew can make the long options relatively cheap or expensive. Compare volatility at both strikes rather than treating one underlying as having a single IV."),
("Test executable prices", "Model the spread using realistic fills for all three contracts. A visually favorable theoretical credit can disappear after bid-ask width and commissions."),
], "Compare 100/105 and 100/110 call backspreads. The wider version may be cheaper but carries a larger maximum loss at the long strike and needs a much stronger rally.",
[("Should the short option be ATM?", "It is common, not mandatory."),("Do wider strikes reduce risk?", "They often increase the middle loss width."),("Why examine skew?", "The two strikes can have materially different implied volatility.")]),

guide("backspread-expiration-dte", "Expiration", "Backspread Expiration and DTE Selection",
"Choose backspread expiration using catalyst timing, gamma, vega, theta, liquidity and the time required for an extreme move.",
"Expiration must provide enough time for the large move while preserving the convexity and cost profile the thesis requires.", [
("Near-term backspreads", "Short duration can provide powerful gamma around an event, but long options decay quickly if the move does not occur. Price can also settle in the maximum-loss zone with little time to recover."),
("Longer-duration backspreads", "More time raises long-option value and vega, commonly increasing debit. The thesis has more time to develop, but the trade remains exposed to volatility contraction and path changes."),
("Event alignment", "Choose an expiration that contains the catalyst and enough post-event time for execution. Earnings IV can be elevated across strikes, so model the expected move and volatility crush together."),
("Management date", "Set a latest date to close or roll if the move has not appeared. Waiting for expiration merely because loss is defined can allow the long options to decay while short-option risk remains."),
], "For an announcement in four weeks, compare 35-DTE and 70-DTE backspreads. The first has more concentrated gamma; the second costs more and carries greater vega.",
[("Is nearest expiration best?", "No. It may not provide time for the thesis."),("Do longer options improve safety?", "They add time but also cost and vega exposure."),("Should expiration include earnings?", "Only when the event is intentional and modeled.")]),

guide("backspread-vs-ratio-spread", "Comparison", "Backspread vs Ratio Spread",
"Understand why a backspread owns more options than it sells while a front ratio spread usually sells more than it owns.",
"Reversing the quantity ratio reverses the tail profile: backspreads seek convexity, while ratio spreads often carry dangerous uncovered tails.", [
("Backspread ratio", "A 1-by-2 call backspread sells one lower call and buys two higher calls. Beyond the upper strike it behaves like one extra long call and has unlimited upside potential."),
("Front ratio spread", "A typical 1-by-2 call ratio spread buys one lower call and sells two higher calls. Beyond the short strike it behaves like one uncovered short call and can have unlimited upside loss."),
("Credit is not risk", "Both may be entered for a credit, but initial cash flow does not reveal maximum loss. The number and location of short contracts determine tail exposure."),
("Naming discipline", "Broker labels vary. Verify signed quantities, payoff graph and margin before entry because confusing backspread with ratio spread can reverse the intended risk completely."),
], "Sell one 100 call and buy two 105 calls: backspread with long upside convexity. Buy one 100 call and sell two 105 calls: front ratio with uncovered upside risk.",
[("Which has more long options?", "The backspread."),("Can a front ratio have unlimited loss?", "Yes, when it leaves a net uncovered short call."),("Why ignore the strategy name?", "Exact quantities determine the real payoff.")]),

guide("backspread-vs-long-straddle", "Comparison", "Ratio Backspread vs Long Straddle",
"Compare an asymmetric directional backspread with a two-sided long straddle across cost, volatility, movement and loss zones.",
"A backspread targets one extreme direction and may be financed by a short option; a long straddle owns both upside and downside movement.", [
("Directional reach", "A call backspread emphasizes a large rally and a put backspread emphasizes a large decline. A long straddle buys one call and one put at the same strike and can profit from a large move in either direction."),
("Cost", "A backspread may open near zero cost or for a credit because of the short option. A long straddle normally requires a substantial debit and loses that debit if movement is insufficient."),
("Loss shape", "The straddle's worst expiration outcome is at its strike. The backspread can retain a credit on the quiet side yet suffer its largest loss after a moderate move into the long-option strike."),
("Volatility and events", "Both are commonly positive gamma and vega, but exposure sizes differ. Compare event-implied move, skew and the directionality of the forecast rather than choosing by debit alone."),
], "Before earnings, a long straddle costs $9 and needs a large move either way. A call backspread costs near zero but only benefits meaningfully from a sufficiently large upside gap.",
[("Which benefits from both directions?", "The long straddle."),("Which can open for credit?", "A backspread sometimes can."),("Do both have positive vega?", "They often do, but exact net vega varies.")]),

guide("backspread-greeks", "Greeks", "Backspread Greeks: Delta, Gamma, Theta and Vega",
"Understand how one short option and multiple long options combine into the changing Greeks of a ratio backspread.",
"Backspreads are designed for positive gamma and vega, but delta and theta can be unfavorable before the extreme move develops.", [
("Delta", "A call backspread can begin near neutral or even negative delta because the lower short call has high delta. As price rises through the long strike, the two long calls dominate and net delta becomes strongly positive."),
("Gamma", "More long options typically create positive net gamma. Delta changes in the favorable direction during a sufficiently large move, producing the strategy's convex payoff."),
("Theta", "Long-option quantity commonly produces negative theta. A credit entry does not mean time decay is always favorable; price in the loss region can make the long options decay while the short option remains valuable."),
("Vega", "Two OTM long options often create positive net vega. Volatility expansion can help, while post-event crush can reduce value even if direction begins to move correctly."),
], "A call backspread begins delta −0.08, gamma +0.05, theta −0.06 and vega +0.14 per share. After a rally, delta can turn strongly positive as long calls activate.",
[("Is backspread delta always bullish or bearish?", "No. It changes with price."),("Why is gamma positive?", "There are more long options than short options."),("Does a credit mean positive theta?", "No.")]),

guide("implied-volatility-backspread", "Vega", "Implied Volatility and Vega in Backspreads",
"Learn how volatility expansion, crush and strike skew affect the short option and multiple long options in a backspread.",
"A backspread is often net long vega, but relative IV changes between strikes can matter as much as a parallel volatility move.", [
("Positive vega", "Two long options commonly contribute more vega than one short option, so a broad IV rise can increase theoretical value. Multiply net vega by quantity and contract multiplier to understand dollar exposure."),
("Volatility crush", "After earnings, IV can fall sharply across all legs. A large favorable price gap may overwhelm the crush, but a modest move can leave the trade in its loss valley while long premium contracts."),
("Skew", "The short and long strikes may trade at different IV and respond differently during a move. Put skew is especially important in put backspreads, where downside long options may already be expensive."),
("Scenario testing", "Model several stock prices with separate IV changes at both strikes. A one-number vega approximation is useful only for small, parallel changes and can miss skew dynamics."),
], "A backspread has net vega +0.18, or about +$18 per IV point per unit. A five-point crush implies roughly −$90 before delta, gamma and theta effects.",
[("Does higher IV always help?", "No. Net vega changes and price may dominate."),("Why can OTM longs be expensive?", "Skew and event demand can raise their IV."),("Do all legs experience the same crush?", "Not necessarily.")]),

guide("theta-time-decay-backspread", "Theta", "Theta and Time Decay in a Backspread",
"Understand why a ratio backspread can have negative theta even when it opens for a credit and how decay changes by price.",
"Initial credit is cash flow; theta is a changing sensitivity. They are not the same measure and can point in opposite directions.", [
("Quiet market", "When price remains far from the long options, their combined time value can decay faster than the short option. The spread may lose mark-to-market value even if a small credit remains possible at expiration."),
("Inside the loss valley", "Near the long strike, the short option is valuable and the extra long option has not created enough intrinsic value. Passing time can lock the position closer to maximum loss."),
("Beyond the long strike", "After a large move, intrinsic value and positive gamma may dominate theta. The position behaves increasingly like one net long option in the target direction."),
("Use a time exit", "If the catalyst passes or the expected move fails to appear, reassess before long premium erodes. Do not confuse defined loss with a reason to wait until expiration."),
], "A credit call backspread shows theta −$7 per day. With stock unchanged, the theoretical spread can lose $35 over five days even though the expiration payoff below the short strike remains a small credit.",
[("Can a credit trade have negative theta?", "Yes."),("Does theta stay constant?", "No. Price, time and IV change it."),("Why exit after a failed catalyst?", "The extra long option premium can decay rapidly.")]),

guide("adjust-and-close-backspread", "Management", "How to Adjust and Close a Ratio Backspread",
"Plan exits for quiet, moderate and extreme moves and evaluate rolling strikes, expiration or ratio without creating naked risk.",
"Manage the complete ratio by its current payoff and thesis; every roll changes the loss valley, Greeks and total capital committed.", [
("Close the full ratio", "A multi-leg closing order removes both the short option and extra longs together. This is the clearest response when the catalyst or volatility thesis is invalidated."),
("Manage a large favorable move", "As price moves beyond the long strike, the position may develop large directional delta. Scaling out of one long option changes it into a vertical or covered relationship that must be recalculated."),
("Roll strikes or time", "Moving the ratio can reposition the loss valley or extend duration, often for an additional debit. Count all prior cash flows and verify the new maximum loss and breakeven."),
("Prevent naked exposure", "Never assume all legs filled. Closing the long options first can leave an uncovered short call or put with substantially different margin and assignment risk."),
], "After an upside gap, a 1-by-2 call backspread is profitable. Selling one long call leaves a one-to-one vertical; selling both longs first leaves a naked short call until it is closed.",
[("Must a winning backspread be held?", "No. Convex profit can be realized early."),("Can one long option be sold?", "Yes, but the remaining position changes."),("Why use a ratio closing order?", "It helps avoid temporary uncovered exposure.")]),

guide("backspread-mistakes", "Risk Management", "Backspread Options Strategy: 12 Mistakes to Avoid",
"Avoid backspread errors involving ratio direction, maximum-loss zones, credit, strikes, volatility, assignment and partial fills.",
"The backspread's attractive tail hides a meaningful middle loss; verify signed quantities and scenario P&L before trading.", [
("Mistakes 1–3: wrong structure", "Do not reverse the ratio, confuse a front ratio with a backspread or assume credit means low risk. More short options can create uncovered tail loss."),
("Mistakes 4–6: weak forecast", "Do not enter without a large-move thesis, choose distant longs only because they are cheap or ignore the maximum-loss price near their strike."),
("Mistakes 7–9: volatility and time", "Do not assume earnings guarantees movement, ignore IV crush or treat opening credit as positive theta. Price, speed and volatility must work together."),
("Mistakes 10–12: execution", "Do not leg into the ratio casually, oversize because loss is defined or close long options before confirming the short is covered. Verify fills and assignment exposure."),
], "A trader intends to sell one call and buy two but enters the quantities in reverse. The resulting front ratio has uncovered upside loss—the opposite of the planned convexity.",
[("What is the most dangerous mistake?", "Reversing the ratio and creating net short tail exposure."),("Can no move be better than a small move?", "Yes, for a credit backspread."),("Why verify fills?", "A missing long option can leave an uncovered short.")]),
]

base.ARTICLES = ARTICLES
base.COURSE = COURSE
base.DATE = "September 12, 2026"


def article_html(article: dict, index: int) -> str:
    decision_section = f'''<h2 id="plan">Turn the payoff into a trading plan</h2>
<p>Before entering {article["title"].lower()}, write down the stock price, both strikes, expiration, contract ratio and total opening credit or debit. Then calculate the quiet-side result, maximum loss at the long-option strike and the far-move breakeven. These three checkpoints make the position easier to monitor and help prevent the attractive tail payoff from hiding the loss valley.</p>
<p>Test at least five scenarios: no move, a move to the short strike, a move to the long strike, a move to breakeven and a move well beyond breakeven. Repeat the exercise with implied volatility higher and lower and with less time remaining. The resulting range is more useful than a single payoff line because a live backspread can change substantially before expiration.</p>
<p>Finally, define the catalyst, maximum acceptable loss, review date and closing method in advance. Use one multi-leg order whenever possible, confirm every fill and recalculate the remaining position before changing any leg. Assignment, liquidity and transaction costs belong in the plan even when the expiration loss appears defined.</p>'''
    return (base.article_html(article, index)
            .replace("2026-09-11", "2026-09-12")
            .replace("Learn Vega — Free", "Learn Backspreads — Free")
            .replace("Vega &amp; Volatility", "Backspread Strategies")
            .replace("Vega planning example", "Backspread payoff example")
            .replace("This simplified example holds other inputs constant to isolate volatility exposure.", "This simplified example focuses on selected expiration outcomes; live prices and risks will differ.")
            .replace("Level 6 – Backspread Strategies course", "Level 14 – Backspread course")
            .replace("Level 6 – Vega &amp; Volatility course", "Level 14 – Backspread course")
            .replace("Start Level 6 — Free", "Start Level 14 — Free")
            .replace("Free Level 6 Course", "Free Level 14 Course")
            .replace("Learn vega and volatility through structured lessons and practical examples.", "Learn Call and Put Backspreads through structured lessons and practical examples.")
            .replace('<h2 id="faq">Frequently asked questions</h2>', decision_section + '\n<h2 id="faq">Frequently asked questions</h2>')
            .replace('<a href="#example">Practical example</a><a href="#faq">FAQs</a>', '<a href="#example">Practical example</a><a href="#plan">Trading plan</a><a href="#faq">FAQs</a>')
            .replace("<span>5-minute read</span>", "<span>7-minute read</span>"))


def update_index() -> None:
    path = BLOG / "index.html"
    source = path.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    if 'href="backspread-options-strategy-explained/"' not in source:
        source = source.replace(marker, "\n".join(base.card_html(a) for a in ARTICLES) + "\n" + marker, 1)
    source = source.replace("<strong>207</strong> guides", "<strong>223</strong> guides")
    if "Explore Level 14" not in source:
        source = source.replace('<a class="btn btn-gold" href="../courses/advanced-option-level-13-calendar-spreads/">Explore Level 13 →</a>', '<a class="btn btn-gold" href="../courses/advanced-option-level-13-calendar-spreads/">Explore Level 13 →</a><a class="btn btn-gold" href="../courses/advanced-option-level-14-backspread/">Explore Level 14 →</a>')
    path.write_text(source)


def update_scripts() -> None:
    path = BLOG / "blog.js"
    source = path.read_text().replace("const clusterPriority = card => card.textContent.includes('Calendar Spread') ? 13 :", "const clusterPriority = card => card.textContent.includes('Backspread') ? 14 : card.textContent.includes('Calendar Spread') ? 13 :")
    path.write_text(source)
    path = ROOT / "favicon.js"
    source = path.read_text()
    marker = "    'calendar-spread-mistakes': '/assets/images/blog/calendar-spread-mistakes.webp'"
    additions = ",\n".join(f"    '{a['slug']}': '/assets/images/blog/{a['slug']}.webp'" for a in ARTICLES)
    if "'backspread-options-strategy-explained'" not in source:
        source = source.replace(marker, marker + ",\n" + additions)
    path.write_text(source)


def update_existing_links() -> None:
    targets = ["what-is-gamma-options", "positive-vega-vs-negative-vega", "option-greeks-straddles-strangles",
               "delta-vs-gamma-options", "calendar-spread-explained", "butterfly-spread-explained"]
    bridge = ('<p class="cluster-bridge"><strong>Advanced strategy:</strong> Read the '
              '<a href="../backspread-options-strategy-explained/">Backspread guide</a> and take the '
              '<a href="../../courses/advanced-option-level-14-backspread/">free Level 14 course</a>.</p>\n')
    for slug in targets:
        path = BLOG / slug / "index.html"
        if path.exists():
            source = path.read_text()
            if "../backspread-options-strategy-explained/" not in source:
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
    draw.text((76, 63), f"LEVEL 14  •  GUIDE {index + 1:02d}", font=font(18, True), fill="#07172d")
    y = 145
    for line in textwrap.wrap(article["title"], width=24)[:4]:
        draw.text((62, y), line, font=font(42, True), fill="white")
        y += 50
    draw.text((64, 570), "OPTIONS AMERICA", font=font(22, True), fill="#b9c9da")
    draw.text((64, 605), "Backspread Learning Series", font=font(20), fill="#7892aa")
    draw.rounded_rectangle((720, 150, 1130, 505), 28, fill="#081c32", outline="#31506d", width=2)
    draw.line((760, 385, 1090, 385), fill="#6b8298", width=2)
    draw.line((900, 190, 900, 455), fill="#31506d", width=2)
    curve = [(760, 330), (825, 330), (900, 440), (960, 330), (1090, 205)]
    if index in (2,):
        curve = [(760, 205), (890, 330), (950, 440), (1025, 330), (1090, 330)]
    draw.line(curve, fill=accent, width=8, joint="curve")
    if index == 1:
        draw.text((780, 205), "SHORT 1", font=font(14, True), fill="#ff8e72")
        draw.text((980, 205), "LONG 2", font=font(14, True), fill="#52d3ff")
    elif index == 2:
        draw.text((775, 205), "LONG 2", font=font(14, True), fill="#52d3ff")
        draw.text((995, 205), "SHORT 1", font=font(14, True), fill="#ff8e72")
    elif index == 3:
        for x, label in ((805, "1×"), (975, "2×")):
            draw.rounded_rectangle((x, 195, x+65, 232), 10, outline=accent, width=2)
            draw.text((x+20, 205), label, font=font(14, True), fill="white")
    elif index == 4:
        draw.line((850, 205, 850, 450), fill="#ff8e72", width=3)
        draw.line((1015, 205, 1015, 450), fill="#ff8e72", width=3)
        draw.text((870, 205), "LOSS VALLEY", font=font(13, True), fill="white")
    elif index == 5:
        for x, ydot in ((780, 330), (860, 380), (900, 440), (980, 310), (1070, 225)):
            draw.ellipse((x-7, ydot-7, x+7, ydot+7), fill="#52d3ff")
    elif index == 6:
        for x, h, c in ((780, 60, "#ff8e72"), (870, 115, accent), (960, 165, "#52d3ff")):
            draw.rounded_rectangle((x, 445-h, x+48, 445), 8, fill=c)
    elif index == 7:
        for x in (825, 900, 960): draw.line((x, 205, x, 450), fill="#31506d", width=2)
    elif index == 8:
        for x, label in ((770, "21D"), (875, "45D"), (990, "90D")):
            draw.rounded_rectangle((x, 195, x+65, 232), 10, outline=accent, width=2)
            draw.text((x+13, 205), label, font=font(13, True), fill="white")
    elif index == 9:
        draw.line([(760, 330), (850, 230), (950, 330), (1090, 455)], fill="#ff8e72", width=5)
    elif index == 10:
        draw.line([(760, 210), (900, 420), (1090, 210)], fill="#52d3ff", width=5)
    elif index == 11:
        for x, h, c in ((770, 80, "#52d3ff"), (830, 130, accent), (890, 60, "#80e0a7"), (950, 110, "#ff8e72")):
            draw.rounded_rectangle((x, 445-h, x+34, 445), 8, fill=c)
    elif index == 12:
        for box, c in (((755, 205, 880, 350), "#52d3ff"), ((855, 220, 1015, 370), "#80e0a7"), ((980, 250, 1090, 355), "#ff8e72")):
            draw.arc(box, 5, 175, fill=c, width=4)
    elif index == 13:
        draw.arc((785, 205, 965, 385), 0, 300, fill="#52d3ff", width=5)
        draw.line((875, 295, 875, 237), fill="white", width=4)
        draw.line((875, 295, 920, 320), fill="white", width=4)
    elif index == 14:
        draw.line((805, 205, 1000, 205), fill="#52d3ff", width=5)
        draw.polygon([(1000, 205), (975, 189), (975, 221)], fill="#52d3ff")
        draw.rounded_rectangle((850, 390, 1010, 430), 10, fill=accent)
        draw.text((875, 400), "EXIT PLAN", font=font(14, True), fill="#07172d")
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
