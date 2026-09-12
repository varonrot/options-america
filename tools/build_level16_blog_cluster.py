#!/usr/bin/env python3
"""Build the Level 16 Short Strangle SEO cluster and original artwork."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("level15_builder", ROOT / "tools/build_level15_blog_cluster.py")
level15 = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(level15)
base = level15.base
BLOG = ROOT / "blog"
COURSE = "../../courses/advanced-option-level-16-short-strangle/"


def guide(slug, tag, title, description, key, sections, example, faq):
    return dict(slug=slug, tag=f"Short Strangle · {tag}", title=title, description=description,
                key=key, sections=sections, example=example, faq=faq)


ARTICLES = [
guide("short-strangle-options-strategy-explained", "Complete Guide", "Short Strangle Options Strategy Explained",
"Learn how selling an OTM call and put creates a wide premium-selling range with substantial uncovered tail risk.",
"A short strangle earns a limited credit when price stays between its breakevens, while loss expands beyond either side and is not capped by the strike distance.", [
("Construction", "Sell one out-of-the-money put below the current price and one out-of-the-money call above it using the same expiration. The distance between strikes creates an initial range with both options OTM."),
("Profit and breakevens", "Maximum profit equals the combined premium. Subtract the credit from the put strike for the lower breakeven and add it to the call strike for the upper breakeven at expiration."),
("Volatility and decay", "Both short options usually create negative vega and positive theta. A quiet market and volatility contraction can help, but a fast directional move and IV expansion can work against both P&L and margin."),
("Undefined tails", "The short call has theoretically unlimited upside loss; the short put has substantial downside loss. Distant strikes reduce initial delta but do not turn the position into defined risk."),
], "With stock at $100, sell the 90 put for $2 and 110 call for $1.50. The $3.50 credit creates expiration breakevens at $86.50 and $113.50 before costs.",
[("What is maximum profit?", "The total call and put premium received."),("Is the loss defined?", "No."),("Why use OTM strikes?", "They create an initial range around the stock price.")]),

guide("how-short-strangle-works", "Mechanics", "How a Short Strangle Works",
"Understand how two OTM short options collect premium, change delta and create assignment and margin obligations.",
"The trade may begin nearly neutral, but the option nearest the moving stock becomes the tested leg and increasingly controls total risk.", [
("Two separate strikes", "The put is sold below spot and the call above spot. Both can expire worthless, but either option can gain value before expiration through price movement, time value or volatility."),
("Tested and untested sides", "A rally tests the call and usually reduces the put's value. A decline tests the put and reduces the call's value. The profitable leg does not cap the losing leg."),
("Changing delta", "Initial deltas may partly offset, but negative gamma makes the position shorter delta into a rally and longer delta into a decline. Neutrality must be monitored, not assumed."),
("Assignment", "An assigned put creates long shares; an assigned call can create short shares. Dividends, borrow conditions and remaining extrinsic value affect early-assignment decisions."),
], "A 90 put and 110 call are sold while stock is $100. A rally to $108 makes the call the tested side even though it may still be OTM and raises directional risk.",
[("Can an OTM option lose money?", "Yes, its price can rise before expiration."),("Does one winning leg cap the other?", "No."),("Can assignment occur early?", "Yes.")]),

guide("short-strangle-payoff-profit-loss-breakevens", "Payoff", "Short Strangle Profit, Loss and Breakevens",
"Calculate credit, maximum profit, two breakevens and losses outside a short strangle's expiration range.",
"The strike interval plus collected credit defines the profitable expiration range, not the maximum loss.", [
("Inside both strikes", "If the underlying expires between the put and call strikes, both options are worthless and the seller retains the full opening credit, less costs."),
("Lower breakeven", "Subtract the combined credit from the short-put strike. Below that price, put intrinsic value exceeds total premium and loss grows toward the underlying's zero-price boundary."),
("Upper breakeven", "Add combined credit to the short-call strike. Above that price, call intrinsic value exceeds total premium and loss grows without a theoretical limit."),
("Interim P&L", "Before expiration, implied volatility and remaining time value can create losses even inside the eventual profitable range. Margin and liquidity can also change before the payoff converges."),
], "A 90/110 short strangle collects $4. Maximum profit is $400, the lower breakeven is $86 and the upper breakeven is $114; expiration at $120 loses $600.",
[("Where is maximum profit earned?", "Anywhere between the two strikes at expiration."),("How many breakevens?", "Two."),("Does the range define risk?", "No.")]),

guide("short-strangle-example", "Worked Example", "Short Strangle Example With Payoff Scenarios",
"Follow a short strangle through prices inside the strikes, at breakeven and beyond the expected range.",
"Scenario P&L shows how the smaller probability-focused credit can be overtaken by one sufficiently large tail move.", [
("Open the trade", "Stock trades at $100. Sell the 90 put for $2.40 and the 110 call for $2.10. The total credit is $4.50, or $450 per standard strangle."),
("Inside the strikes", "At expiration prices from $90 through $110, both options are OTM or exactly at the money and the full $450 credit remains before costs."),
("Between strike and breakeven", "At $113 the call has $3 intrinsic value, leaving $1.50 per share of profit. At $114.50 the call exactly consumes the full credit."),
("Tail outcome", "At $125 the call has $15 intrinsic value. After the $4.50 credit, loss is $10.50 per share, and continued upside keeps increasing the loss."),
], "Approximate expiration P&L at $80, $88, $100, $112 and $125 is −$550, +$250, +$450, +$250 and −$1,050 before costs.",
[("Why is profit flat between strikes?", "Both options expire worthless."),("Can the position be closed early?", "Yes, preferably as a two-leg order."),("Which side loses at $125?", "The short call.")]),

guide("short-strangle-strike-selection", "Strikes", "How to Choose Short Strangle Strikes",
"Choose call and put strikes using expected move, delta, skew, liquidity, credit and portfolio stress tests.",
"Wider strikes raise the initial probability range but normally reduce credit; no strike distance removes uncovered tail exposure.", [
("Expected move", "Compare candidate strikes with the option market's implied move and independent price scenarios. A strike just outside one standard range can still be reached frequently."),
("Delta selection", "Some traders use similar absolute deltas for call and put, but skew means equal delta does not mean equal distance or equal dollar risk. Delta also changes rapidly near a tested strike."),
("Skew and credit", "OTM puts often carry higher IV than comparable calls. The extra put credit reflects demand for downside protection and should not be mistaken for free compensation."),
("Liquidity and portfolio", "Choose strikes with executable markets, then stress each tail across all positions. Correlated put exposure can dominate a portfolio during a broad decline."),
], "At $100, a 15-delta put may be $8 below spot while a 15-delta call is $11 above. Equal starting delta still produces asymmetric price and volatility risk.",
[("Are equal-delta strikes required?", "No."),("Do wider strikes define risk?", "No."),("Why inspect skew?", "Put and call IV can differ materially.")]),

guide("short-strangle-vs-iron-condor", "Comparison", "Short Strangle vs Iron Condor",
"Compare an uncovered short strangle with a wing-protected iron condor across credit, loss, margin and flexibility.",
"Buying farther OTM wings transforms the undefined strangle tails into a defined-risk iron condor at the cost of premium.", [
("Structure", "Both sell an OTM put and call. The iron condor also buys a lower put and higher call, creating two vertical credit spreads."),
("Credit and loss", "The strangle collects more because it buys no protection, but losses remain open. The condor's net credit is lower and maximum loss is limited by wing width."),
("Buying power", "Strangle margin can expand with price and IV. A condor generally has a clearer requirement based on its defined maximum loss, although broker treatment varies."),
("Management", "The strangle can be easier to roll with fewer legs, while the condor limits disaster risk. Liquidity, commissions and fill quality matter in either structure."),
], "A 90/110 strangle collects $4. Buying the 85 put and 115 call for $1 converts it to a five-point iron condor with a $3 credit and $2 maximum loss per share.",
[("Which has defined risk?", "The iron condor."),("Which collects more credit?", "Normally the short strangle."),("Do wings remove all execution risk?", "No.")]),

guide("short-strangle-vs-covered-strangle", "Comparison", "Short Strangle vs Covered Strangle",
"Compare an uncovered short strangle with a covered strangle that combines shares, a short call and a short put.",
"Owning shares covers the call obligation but adds stock exposure; it does not eliminate downside risk from the short put and shares together.", [
("Position components", "A short strangle contains only a short OTM call and put. A covered strangle adds 100 long shares per short call while retaining the short put."),
("Directional bias", "The uncovered strangle can start near delta-neutral. The covered version begins bullish because of the long shares and may acquire more shares if the put is assigned."),
("Risk", "Shares cover call delivery and cap stock upside at the call strike, but downside combines loss on the shares with the short-put obligation. Capital usage is usually much larger."),
("Income framing", "Premium is not independent income. Evaluate the full stock-and-options payoff, dividend dates, assignment and concentration before comparing yields."),
], "Own 100 shares at $100, sell a 110 call and 90 put. Above $110 the shares may be called away; below $90 assignment can increase the holding to 200 shares.",
[("Is the call covered?", "Yes, by the shares."),("Can shares double after assignment?", "Yes, one short put can add 100 shares."),("Is downside defined?", "It is substantial, not eliminated.")]),

guide("best-market-conditions-short-strangle", "Entry", "Best Market Conditions for a Short Strangle",
"Assess implied versus realized volatility, catalysts, liquidity, trend and portfolio exposure before selling a strangle.",
"The trade works when the premium overstates future movement enough to compensate for rare tail losses and transaction costs.", [
("Volatility edge", "Compare implied movement with a range of realized scenarios and volatility risk premium, not a single historical average. High IV may correctly anticipate a large move."),
("Trend and catalysts", "Strong trends and binary announcements can move price rapidly toward or through a short strike. Decide which events are deliberately included in the holding period."),
("Market quality", "Liquid chains support two-leg entries, rolls and exits. A wide market can turn a small statistical edge into poor realized execution."),
("Portfolio fit", "Avoid stacking similar short puts or calls across correlated assets. Stress the whole portfolio for a common volatility shock and directional gap."),
], "A diversified index has liquid options, elevated IV and no scheduled binary event during the planned holding period. The trade is still sized against a gap beyond either strike.",
[("Is a range forecast enough?", "No; volatility, liquidity and tail loss also matter."),("Why check correlation?", "Many positions can become tested together."),("Can high IV be justified?", "Yes.")]),

guide("implied-volatility-short-strangle", "Volatility", "Implied Volatility and the Short Strangle",
"Understand negative vega, skew, volatility expansion and event crush across two OTM short options.",
"The call and put can carry different implied volatilities, so a one-number IV view can hide asymmetric exposure.", [
("Negative vega", "Both options are short, making the position generally negative vega. An IV increase raises theoretical repurchase cost even if price remains between strikes."),
("Put skew", "OTM puts often trade at higher IV than OTM calls. Selling the put may collect more premium because the market prices more downside demand and crash risk."),
("Event crush", "Volatility can decline after an announcement, helping both legs, but a gap may create intrinsic loss larger than the volatility benefit. Test price and IV together."),
("Dynamic surface", "During a selloff, put skew and overall IV can steepen while the underlying approaches the put strike. Parallel-vega estimates may understate the actual change."),
], "The put is sold at 32% IV and the call at 24% IV. A downside shock can raise both levels and steepen skew, increasing the put's price beyond a simple equal-IV estimate.",
[("Are call and put IV equal?", "Not necessarily."),("Does IV crush guarantee profit?", "No."),("Why is put IV often higher?", "Demand and perceived downside risk influence skew.")]),

guide("short-strangle-greeks", "Greeks", "Short Strangle Greeks: Delta, Gamma, Theta and Vega",
"Learn how delta, negative gamma, positive theta and negative vega change as price approaches either short strike.",
"OTM placement makes initial Greeks look mild, but negative gamma causes risk to accelerate when one option becomes tested.", [
("Delta", "Call and put deltas can offset at entry. A rally makes the position increasingly short delta through the call; a decline makes it increasingly long delta through the put relative to a falling asset."),
("Gamma", "Both short options contribute negative gamma, especially as price approaches a strike and expiration nears. Delta therefore changes in the unfavorable direction during movement."),
("Theta", "The two options usually provide positive theta. Decay is not linear and is not guaranteed realized profit when movement or volatility overwhelms it."),
("Vega", "Negative vega means broad IV expansion increases option value. Volatility often rises precisely when the tested leg is also developing adverse delta and gamma."),
], "A strangle begins delta 0.01, gamma −0.025, theta +0.06 and vega −0.17. After a decline toward the put strike, delta and gamma exposure can increase sharply.",
[("Does low initial delta mean low risk?", "No."),("Why does risk accelerate?", "Negative gamma changes delta against the move."),("Is theta guaranteed income?", "No.")]),

guide("theta-decay-short-strangle", "Theta", "Theta and Time Decay in a Short Strangle",
"Understand how OTM time value decays and why the tested side can overwhelm positive theta near expiration.",
"Time decay helps only while price movement and volatility remain controlled; the option nearest a strike can retain or gain value.", [
("Two decay sources", "Both the OTM call and put can lose extrinsic value as time passes. The rate depends on distance from spot, IV and remaining time."),
("Tested option", "When price approaches one strike, that option gains delta and may gain IV. Its increase can exceed the decay collected from the distant untested option."),
("Gamma near expiry", "Shorter DTE concentrates theta but also negative gamma. A small late move can change an apparently safe position into a rapid loss."),
("Close the cheap tail", "The final dollars of premium may offer poor reward relative to assignment, gap and execution risk. Evaluate remaining credit instead of holding mechanically."),
], "The untested call loses $12 while the tested put gains $90 during a selloff. Positive portfolio theta does not prevent the net position from losing $78.",
[("Do both legs decay equally?", "No."),("Can the tested leg rise despite time passing?", "Yes."),("Why close before expiry?", "To reduce gamma and assignment uncertainty.")]),

guide("short-strangle-expiration-dte", "Expiration", "Short Strangle Expiration and DTE Selection",
"Choose DTE using theta, gamma, vega, event timing, strike distance and the planned management window.",
"Short DTE offers faster decay with less reaction time; longer DTE offers wider strike choices but greater vega and calendar exposure.", [
("Near-term expiration", "Short-dated OTM options can decay quickly, but price can cross a strike before there is time to roll. Bid-ask spreads and gamma may expand near the close."),
("Longer expiration", "More DTE usually supports farther strikes and a larger absolute credit. It also exposes the trade to more news and often more net vega."),
("Event placement", "Check every scheduled catalyst inside the expiration. The term structure can concentrate premium in the expiration containing earnings or a major release."),
("Management window", "Choose an exit date before the final risk becomes inconsistent with the plan. A DTE selection is incomplete without a profit target and tested-side response."),
], "Compare 21-DTE and 60-DTE strangles at similar deltas. The short contract has concentrated gamma; the longer contract carries more time and volatility exposure.",
[("Is short DTE always better for theta?", "It may show more concentrated decay but also more gamma."),("Can longer DTE use wider strikes?", "Often, but pricing varies."),("Should events be checked?", "Always.")]),

guide("short-strangle-margin-buying-power", "Capital", "Short Strangle Margin and Buying Power",
"Plan for changing margin, volatility stress and correlated portfolio exposure before opening an undefined-risk strangle.",
"The initial requirement is a broker estimate, not a fixed ceiling on the cash or loss the position may demand.", [
("Requirement inputs", "Brokers consider underlying price, strike distance, premium, volatility and account permissions. Standard and portfolio-margin accounts can calculate very different amounts."),
("Tested-side expansion", "A move toward the call or put can increase intrinsic and risk exposure while IV rises. Margin may expand at the same time the trade loses."),
("Portfolio concentration", "Several strangles can appear diversified but share market beta and volatility risk. A broad shock can test many puts and reduce buying power together."),
("Capital reserve", "Keep enough reserve for a stressed price gap, higher volatility and orderly closure. Size from worst credible portfolio scenarios rather than the credit-to-margin percentage."),
], "A strangle opens using $3,500 of buying power. After a market decline and IV spike, the requirement reaches $7,000 while the position needs cash to close or adjust.",
[("Can margin double?", "It can change substantially."),("Is premium yield a complete metric?", "No."),("Why stress the portfolio?", "Correlated positions may move together.")]),

guide("adjust-short-strangle", "Management", "How to Adjust a Short Strangle",
"Compare rolling the untested side, moving a tested strike, extending time, adding wings and closing the trade.",
"Every adjustment exchanges one risk for another; additional credit does not erase accumulated loss or guarantee recovery.", [
("Close the position", "A full close is the cleanest response when the volatility or range thesis fails. It prevents a management decision from becoming a permanently extended position."),
("Roll the untested side", "Moving the profitable option toward spot collects more credit and can reduce current delta. It narrows the range and increases whipsaw exposure after a reversal."),
("Roll the tested side", "Moving the challenged strike out or forward can require more time and may change the credit. Recalculate breakevens, Greeks and total cash flows after the roll."),
("Add wings", "Buying farther OTM options converts open tails into an iron condor or related defined-risk structure. Evaluate protection cost, liquidity and the risk left between strikes."),
], "Stock rallies toward the 110 call. Rolling the 90 put up to 100 collects credit and reduces short delta, but a reversal can quickly test the newly raised put.",
[("Does rolling guarantee recovery?", "No."),("Can the trade be closed instead?", "Yes."),("What do wings change?", "They can cap tail loss.")]),

guide("close-roll-short-strangle", "Exit", "When to Close or Roll a Short Strangle",
"Set profit, loss, time, volatility and tested-strike rules for closing or rolling a short strangle.",
"A roll is a new risk decision, not a bookkeeping method for avoiding recognition of the current trade's outcome.", [
("Profit capture", "Closing after a planned fraction of maximum credit can remove tail exposure while much of the intended decay has already been earned. Account for commissions and remaining DTE."),
("Tested-strike rule", "Some plans act when delta, price distance or loss reaches a threshold. Choose the trigger before entry and test it against gaps where execution occurs beyond the threshold."),
("Volatility rule", "A rise in IV may invalidate the original premium assumption or create a new opportunity. Reassess objectively instead of rolling simply because repurchase cost increased."),
("Roll economics", "Separate the debit to close from the credit on the new expiration. Compare the rolled position with closing and staying flat, including added time and capital."),
], "A strangle sold for $4.50 can be bought for $2 after four weeks. Closing captures $250 and removes exposure before an event rather than risking it for the remaining $200.",
[("Why close a profitable trade early?", "To reduce remaining tail risk."),("Is a roll a loss-free action?", "No."),("Should a new event change the plan?", "Yes, it should be reassessed.")]),

guide("short-strangle-mistakes", "Risk Management", "Short Strangle Options Strategy: 12 Mistakes to Avoid",
"Avoid strike, volatility, sizing, margin, correlation, adjustment, assignment and expiration mistakes.",
"A wide range can create false comfort; the open call and put tails remain capable of losses far larger than the initial credit.", [
("Mistakes 1–3: false safety", "Do not equate OTM with safe, treat probability of profit as expected return or assume the opposite leg caps loss. Model tail size."),
("Mistakes 4–6: selection", "Do not choose strikes only by delta, sell merely because IV is high or ignore skew and catalysts. Price the scenario behind the premium."),
("Mistakes 7–9: leverage", "Do not use all buying power, ignore correlation or size from opening margin. Stress both market direction and volatility together."),
("Mistakes 10–12: management", "Do not roll without recalculating, leave accidental naked exposure or hold cheap options into assignment. Verify fills and follow written exit rules."),
], "A trader sells low-delta puts across several correlated stocks. A market gap tests them all, IV rises and total margin expands before individual adjustments can help.",
[("Does low delta mean no tail risk?", "No."),("What is a common portfolio mistake?", "Stacking correlated short-volatility exposure."),("Why verify every fill?", "A missing leg changes risk and margin.")]),
]


def article_html(article: dict, index: int) -> str:
    base.ARTICLES = ARTICLES
    base.COURSE = COURSE
    base.DATE = "September 12, 2026"
    plan = f'''<h2 id="plan">Build a risk-first trading plan</h2>
<p>Before using {article["title"].lower()}, record the stock price, put and call strikes, expiration, total credit and contract multiplier. Calculate both breakevens, then estimate dollar loss beyond them under upside and downside gaps. A wide strike range improves the starting room but does not define either tail.</p>
<p>Stress several prices, time points and volatility levels, including a skew change that affects the put and call differently. Review delta, gamma, theta, vega and buying power for the complete portfolio. Multiple OTM positions can become tested together during a common market shock.</p>
<p>Define a profit target, maximum tolerated loss, tested-side trigger, margin reserve and latest exit date before entry. Decide whether an event is intentionally included and how assignment would be handled. Use multi-leg orders and confirm quantities after every fill, roll or partial close.</p>
<p>Document the result after exit, including slippage, assignment effects and the largest intraday exposure. Comparing the original forecast with the actual path helps distinguish a sound process from a lucky outcome and improves later strike, duration, margin-reserve and position-size choices under similar market conditions.</p>'''
    return (base.article_html(article, index)
            .replace("2026-09-11", "2026-09-12")
            .replace("Learn Vega — Free", "Learn Short Strangles — Free")
            .replace("Vega &amp; Volatility", "Short Strangle")
            .replace("Vega planning example", "Short Strangle example")
            .replace("This simplified example holds other inputs constant to isolate volatility exposure.", "This simplified scenario focuses on selected outcomes; live prices and risks will differ.")
            .replace("Level 6 – Short Strangle course", "Level 16 – Short Strangle course")
            .replace("Level 6 – Vega &amp; Volatility course", "Level 16 – Short Strangle course")
            .replace("Start Level 6 — Free", "Start Level 16 — Free")
            .replace("Free Level 6 Course", "Free Level 16 Course")
            .replace("Learn vega and volatility through structured lessons and practical examples.", "Learn Short Strangle strikes, Greeks, risk and adjustments through structured lessons.")
            .replace('<h2 id="faq">Frequently asked questions</h2>', plan + '\n<h2 id="faq">Frequently asked questions</h2>')
            .replace('<a href="#example">Practical example</a><a href="#faq">FAQs</a>', '<a href="#example">Practical example</a><a href="#plan">Risk plan</a><a href="#faq">FAQs</a>')
            .replace("<span>5-minute read</span>", "<span>7-minute read</span>"))


def create_image(article: dict, index: int) -> None:
    image = Image.new("RGB", (1200, 675), "#07172d")
    draw = ImageDraw.Draw(image)
    accents = ["#54d5ff", "#ffbd16", "#8be39a", "#b995ff", "#ff8b72"]
    accent = accents[index % len(accents)]
    draw.ellipse((740, -270, 1360, 400), fill="#103858")
    draw.rounded_rectangle((715, 128, 1122, 538), 28, fill="#091f38", outline="#255170", width=3)
    bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    reg_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    bold = lambda size: ImageFont.truetype(bold_path, size)
    regular = lambda size: ImageFont.truetype(reg_path, size)
    draw.rounded_rectangle((62, 55, 242, 91), 18, fill=accent)
    draw.text((79, 64), f"LEVEL 16  •  GUIDE {index + 1:02}", font=bold(14), fill="#07172d")
    lines = []
    for word in article["title"].split():
        if not lines or len(lines[-1] + " " + word) > 28: lines.append(word)
        else: lines[-1] += " " + word
    for n, line in enumerate(lines[:4]): draw.text((62, 128 + n * 53), line, font=bold(37), fill="white")
    draw.text((62, 574), "OPTIONS AMERICA", font=bold(17), fill="white")
    draw.text((62, 601), "Short Strangle Learning Series", font=regular(13), fill="#8daac4")
    draw.line((775, 340, 1065, 340), fill="#607d96", width=2)
    draw.line((920, 185, 920, 490), fill="#607d96", width=2)
    if index in (5, 6):
        draw.line((790, 220, 865, 410, 975, 410, 1050, 220), fill=accent, width=8)
        draw.line((790, 440, 790, 390), fill="#8be39a", width=5)
        draw.line((1050, 440, 1050, 390), fill="#8be39a", width=5)
    elif index in (9, 10):
        for x, h, c in ((810, 90, accent), (865, 145, "#8be39a"), (920, 70, "#ffbd16"), (975, 170, "#ff8b72")):
            draw.rounded_rectangle((x, 445-h, x+34, 445), 6, fill=c)
    elif index in (13, 14):
        draw.arc((805, 230, 1035, 460), 20, 325, fill=accent, width=7)
        draw.line((920, 345, 1005, 285), fill="#8be39a", width=6)
    else:
        draw.line((785, 220, 865, 420, 975, 420, 1055, 220), fill=accent, width=8)
        if index % 3 == 1:
            draw.line((840, 255, 840, 425), fill="#ff8b72", width=4)
            draw.line((1000, 255, 1000, 425), fill="#8be39a", width=4)
        if index % 3 == 2: draw.ellipse((895, 392, 945, 442), outline="#ffbd16", width=5)
    image.save(ROOT / "assets/images/blog" / f"{article['slug']}.webp", "WEBP", quality=88, method=6)


def update_index() -> None:
    path = BLOG / "index.html"
    source = path.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    if 'href="short-strangle-options-strategy-explained/"' not in source:
        source = source.replace(marker, "\n".join(base.card_html(a) for a in ARTICLES) + "\n" + marker, 1)
    source = source.replace("<strong>239</strong> guides", "<strong>255</strong> guides")
    if "Explore Level 16" not in source:
        source = source.replace('<a class="btn btn-gold" href="../courses/advanced-option-level-15-short-straddle/">Explore Level 15 →</a>', '<a class="btn btn-gold" href="../courses/advanced-option-level-15-short-straddle/">Explore Level 15 →</a><a class="btn btn-gold" href="../courses/advanced-option-level-16-short-strangle/">Explore Level 16 →</a>')
    path.write_text(source)


def update_scripts() -> None:
    path = BLOG / "blog.js"
    source = path.read_text().replace("const clusterPriority = card => card.textContent.includes('Short Straddle') ? 15 :", "const clusterPriority = card => card.textContent.includes('Short Strangle') ? 16 : card.textContent.includes('Short Straddle') ? 15 :")
    path.write_text(source)
    path = ROOT / "favicon.js"
    source = path.read_text()
    marker = "    'short-straddle-mistakes': '/assets/images/blog/short-straddle-mistakes.webp'"
    additions = ",\n".join(f"    '{a['slug']}': '/assets/images/blog/{a['slug']}.webp'" for a in ARTICLES)
    if "'short-strangle-options-strategy-explained'" not in source:
        source = source.replace(marker, marker + ",\n" + additions)
    path.write_text(source)


def update_existing_links() -> None:
    targets = ["short-iron-condor-vs-short-strangle", "short-iron-condor-explained", "implied-volatility-short-iron-condor", "choose-short-iron-condor-strikes"]
    bridge = ('<p class="cluster-bridge"><strong>Undefined-risk comparison:</strong> Read the '
              '<a href="../short-strangle-options-strategy-explained/">Short Strangle guide</a> and take the '
              '<a href="../../courses/advanced-option-level-16-short-strangle/">free Level 16 course</a>.</p>\n')
    for slug in targets:
        path = BLOG / slug / "index.html"
        if path.exists():
            source = path.read_text()
            if "../short-strangle-options-strategy-explained/" not in source:
                source = source.replace("</article>", bridge + "</article>", 1)
                path.write_text(source)
    pillar = BLOG / "short-straddle-vs-short-strangle" / "index.html"
    if pillar.exists():
        source = pillar.read_text()
        if "../short-strangle-options-strategy-explained/" not in source:
            source = source.replace("</article>", '<p class="cluster-bridge"><strong>Next:</strong> Continue with the <a href="../short-strangle-options-strategy-explained/">complete Short Strangle guide</a>.</p>\n</article>', 1)
            pillar.write_text(source)


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
