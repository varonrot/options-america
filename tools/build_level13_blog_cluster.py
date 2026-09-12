#!/usr/bin/env python3
"""Build the Level 13 Calendar Spreads SEO cluster and original artwork."""

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
COURSE = "../../courses/advanced-option-level-13-calendar-spreads/"


def guide(slug, tag, title, description, key, sections, example, faq):
    return dict(slug=slug, tag=f"Calendar Spread · {tag}", title=title, description=description,
                key=key, sections=sections, example=example, faq=faq)


ARTICLES = [
guide("calendar-spread-explained", "Complete Guide", "Calendar Spread Explained: Strategy, Risk and Reward",
"Learn how a calendar spread sells a near-term option and buys a longer-dated option at the same strike.",
"A long calendar combines faster decay in the short front-month option with longer-lasting time and volatility exposure in the back-month option.", [
("The two-expiration structure", "A standard long calendar sells one near-term call or put and buys one later-dated option of the same type and strike. Quantity and contract multiplier normally match, but the expirations deliberately differ."),
("The target at front expiration", "The position commonly performs best when the underlying is near the shared strike as the short option expires. The front option can lose much of its time value while the back option still retains time and volatility value."),
("Risk and reward", "The opening debit is often the practical risk boundary if the position is maintained as a spread, but maximum profit and exact breakevens are not fixed at entry because the back option's value at front expiration depends on implied volatility."),
("Operational complexity", "The position has two expirations, two volatility levels and changing Greeks. Early assignment, event timing, skew, term structure and decisions about the remaining back option all require a written plan."),
], "Sell a 30-day 100 call and buy a 60-day 100 call for a $1.80 debit. The goal is for price to be near $100 when the first call expires while the 60-day call retains value.",
[("Is a calendar neutral?", "An ATM calendar may begin near neutral, while OTM calendars can be directional."),("Is maximum profit known?", "Not exactly, because back-month IV and value at front expiration are unknown."),("Can calendars use puts?", "Yes. Calls and puts can both build calendars.")]),

guide("how-to-build-calendar-spread", "Step by Step", "How to Build a Calendar Spread",
"Build a calendar spread by choosing a target strike, selling the front expiration and buying the back expiration as one order.",
"Select the target and time window before comparing the two option expirations, then enter the pair for a controlled net debit.", [
("Define the thesis", "State the target price, expected timing and volatility view. The trade should explain why the underlying may remain near or move toward the strike and why back-month volatility should hold relative to the front month."),
("Choose matching options", "Use the same underlying, option type, strike and quantity. Sell the nearer expiration and buy the later expiration, then verify that the order ticket shows a long calendar rather than a reversed short calendar."),
("Price the term structure", "Compare the debit, implied volatility and extrinsic value in each expiration. A cheap-looking spread can reflect an unfavorable term structure or an event concentrated in the short option."),
("Enter and document", "Use one multi-leg limit order. Record the target, maximum acceptable debit, profit objective, price exit, volatility exit, front-expiration plan and assignment procedures before sending."),
], "With stock at $99 and a $100 target, sell the 28-day 100 call and buy the 63-day 100 call together for a $1.65 debit.",
[("Which option is sold?", "The nearer expiration."),("Must the strike match?", "A standard calendar uses the same strike; different strikes create a diagonal."),("Why use one order?", "It controls the net debit and avoids unintended single-leg exposure.")]),

guide("calendar-spread-profit-loss-breakeven", "Payoff", "Calendar Spread Profit, Loss and Breakeven",
"Understand why calendar spread maximum profit and breakevens are estimates rather than fixed expiration formulas.",
"At front expiration, the short option has little or no time value while the back option still has value that depends on volatility and remaining time.", [
("Why payoff is curved", "The two options do not expire together, so the later option cannot be reduced to intrinsic value at the first expiration. Its price must be modeled using remaining time, IV, rates, dividends and the underlying price."),
("Maximum loss", "For a standard long calendar entered for a debit, the debit is commonly the practical maximum loss if both legs remain paired. Closing or being assigned on only one leg can create a different exposure."),
("Estimated maximum profit", "Modeling often shows the highest value near the shared strike at front expiration. The number changes when the assumed back-month IV changes, so a platform's peak is a scenario, not a guaranteed maximum."),
("Estimated breakevens", "The two displayed breakevens also depend on the chosen date and volatility assumptions. Recalculate the graph using several IV shifts instead of treating one pair of points as permanent."),
], "A platform estimates a $3.20 peak for a calendar costing $1.60, assuming back-month IV stays at 28%. If IV falls to 22%, both the peak and estimated breakevens contract.",
[("Is there a simple breakeven formula?", "No, not like a same-expiration vertical spread."),("Can loss exceed the debit?", "Assignment or unpaired-leg actions can create additional exposure."),("Why do broker graphs differ?", "They may use different IV, pricing and date assumptions.")]),

guide("calendar-spread-example", "Worked Example", "Calendar Spread Example With Price and Volatility Scenarios",
"Walk through a call calendar under target, downside, upside and implied-volatility scenarios before the front option expires.",
"Calendar P&L must be tested across price, time and volatility because no single expiration line describes the trade.", [
("Set up the example", "Stock trades at $100. Sell a 30-day 100 call for $2.20 and buy a 60-day 100 call for $3.90. Net debit and initial risk budget are $1.70, or $170 per standard spread."),
("Price stays near $100", "As the first expiration approaches, the short call can shed extrinsic value faster. If back-month IV remains stable, the long call may retain enough value for the spread to appreciate."),
("Price moves away", "A fast move to $90 or $110 can reduce the relative time-value advantage around the strike. Delta and gamma change, and the short option may become deeply ITM on the upside."),
("Volatility changes", "A back-month IV rise can support the long option; a broad volatility contraction can reduce the calendar even when price is near target. Front and back IV may not move equally."),
], "After 20 days, stock is $101, the short call is $1.55 and the back call is $3.80. Closing for $2.25 produces about $55 profit over the original $1.70 debit before costs.",
[("Why is the result not the front option's decay alone?", "The back option also reprices."),("What if stock jumps?", "Directional and assignment risk can dominate theta."),("Can the spread be closed early?", "Yes, by closing both expirations together.")]),

guide("choose-calendar-spread-strike", "Strike Selection", "How to Choose a Calendar Spread Strike",
"Choose an ATM, OTM or ITM calendar strike using the target price, delta, event range, liquidity and directional bias.",
"The shared strike is the center of the calendar's modeled value at front expiration, so it should reflect the forecast rather than habit.", [
("ATM calendars", "A strike near the current price often creates a broadly neutral starting position with strong time-value concentration. It is appropriate only when the target is also near the current market."),
("OTM calendars", "Placing a call calendar above price expresses a bullish target; placing a put calendar below price can express a bearish target. The underlying must move toward the strike within the planned window."),
("ITM calendars", "An ITM strike can carry larger intrinsic values and assignment exposure in the short option. Compare extrinsic value and delta rather than assuming moneyness alone improves probability."),
("Liquidity and events", "Both expirations must have viable markets at the same strike. Review earnings, dividends and strike-specific IV because an attractive target with poor execution is not an attractive trade."),
], "With stock at $98, compare 95, 100 and 105 call calendars. They represent different targets and starting deltas even when their expiration dates match.",
[("Must a calendar be ATM?", "No."),("Can strike choice make it directional?", "Yes. An OTM target creates directional exposure."),("Why inspect extrinsic value?", "Calendar economics depend on the relative time value sold and bought.")]),

guide("choose-calendar-spread-expirations", "Expiration", "How to Choose Calendar Spread Expirations",
"Select front and back expirations by comparing decay, vega, event timing, liquidity and the spacing between maturities.",
"The short expiration sets the first decision date; the long expiration determines how much time and volatility value remains then.", [
("Choose the front month", "Sell an expiration that covers the period during which price is expected to approach the target. Near-term options decay faster but carry greater gamma and assignment sensitivity."),
("Choose the back month", "Buy enough additional duration so the long option retains meaningful time value at front expiration. More distance usually increases debit and vega exposure."),
("Measure the gap", "A small expiration gap may be inexpensive but leave little residual value. A large gap can create a strong term-structure trade while tying up capital and exposing the position to more volatility regimes."),
("Place known events intentionally", "Decide whether earnings or macro events belong in neither expiration, both, or only the back month. Event placement can dominate ordinary theta assumptions."),
], "Compare selling 21 DTE and buying 49 DTE with selling 35 DTE and buying 91 DTE. The second structure has more duration, debit and potential vega exposure.",
[("How far apart should expirations be?", "There is no universal gap; compare decay, debit and thesis timing."),("Can the short expire after earnings while the long includes it too?", "Yes, but model how event premium is distributed."),("Is more back-month time always better?", "No. It costs more and changes risk.")]),

guide("call-calendar-vs-put-calendar", "Comparison", "Call Calendar vs Put Calendar Spread",
"Compare call and put calendars with the same strike and expirations through pricing, delta, assignment, dividends and liquidity.",
"Call and put calendars can have similar time-spread objectives, but operational and directional details differ.", [
("Shared time thesis", "Both sell a near option and buy a later option at one strike. When centered ATM, both can seek faster front-month decay while retaining back-month time value."),
("Directional exposure", "OTM call calendars are commonly used for bullish targets and OTM put calendars for bearish targets. Exact delta depends on both options and can shift as price approaches the strike."),
("Assignment", "An ITM short call may be assigned around dividends, while an ITM short put can create long shares. American-style exercise risk must be monitored separately from modeled P&L."),
("Choose by execution", "Compare net debit, extrinsic values, spreads and open interest. Put-call parity may link theoretical prices, but live markets and account consequences can favor one version."),
], "At a $100 strike, the call calendar costs $1.70 and the put calendar $1.62. The smaller debit does not automatically win if the put markets are wider or assignment is less convenient.",
[("Are call and put calendars identical?", "Not operationally, even when modeled results are similar."),("Which is bullish?", "An OTM call calendar is often used for a bullish target."),("Which should I trade?", "Use the version that matches the target and offers cleaner execution.")]),

guide("calendar-spread-vs-diagonal-spread", "Comparison", "Calendar Spread vs Diagonal Spread",
"Compare same-strike calendars with different-strike diagonals across directional bias, credit or debit, Greeks and management.",
"A calendar changes expiration only; a diagonal changes both expiration and strike, combining a time spread with a vertical component.", [
("Construction", "The standard calendar sells and buys the same strike in different expirations. A diagonal typically sells a near option at one strike and buys a later option at another strike."),
("Directional shape", "Moving the long and short strikes apart can add bullish or bearish delta and reshape the front-expiration value curve. The diagonal is not merely a calendar with a wider profit zone."),
("Pricing and risk", "Some diagonals open for a debit and others for a credit. Maximum risk can depend on strike relationship, assignment and what happens after the short option expires, so map the complete position."),
("Management", "Rolling the short option can turn a calendar into a diagonal or change an existing diagonal again. Track total debits and credits across every cycle rather than evaluating only the latest roll."),
], "Selling a 30-day 105 call and buying a 90-day 100 call creates a diagonal, while buying and selling the 105 strike would create a calendar.",
[("What defines a diagonal?", "Different strikes and different expirations."),("Can a calendar become a diagonal?", "Yes, after rolling the short leg to another strike."),("Which is more directional?", "A diagonal commonly carries more intentional directional exposure.")]),

guide("calendar-spread-vs-vertical-spread", "Comparison", "Calendar Spread vs Vertical Spread",
"Compare time spreads and same-expiration vertical spreads through strike selection, payoff certainty, Greeks and breakevens.",
"A calendar separates expirations at one strike; a vertical separates strikes within one expiration, producing fundamentally different risk maps.", [
("Structure", "A calendar normally uses the same strike and two expirations. A vertical spread uses two strikes and the same expiration, such as a bull call spread or bear put spread."),
("Payoff calculation", "Vertical maximum profit, loss and expiration breakeven can often be calculated exactly at entry. Calendar front-expiration value depends on the remaining option's implied volatility."),
("Greek focus", "Calendars emphasize relative theta and vega across maturities. Verticals often emphasize directional delta with reduced premium exposure, although all Greeks still matter."),
("Choose by thesis", "Use a vertical for a directional price range at one expiration. Use a calendar when the thesis specifically involves target timing, relative decay and volatility term structure."),
], "A 100/110 call vertical uses one expiration and caps directional upside. A 30/60-day 100 call calendar uses one strike and targets relative decay near $100.",
[("Which has fixed breakeven?", "A standard vertical has a calculable expiration breakeven."),("Which uses two expirations?", "The calendar."),("Can both be debit trades?", "Yes, but their risks differ.")]),

guide("double-calendar-spread-explained", "Advanced", "Double Calendar Spread Explained",
"Learn how a double calendar uses two target strikes and two expirations to create a wider time-spread structure.",
"A double calendar combines a lower-strike calendar and an upper-strike calendar, trading more range for more debit and complexity.", [
("Four option pairs", "Sell a near-term option and buy a later option at a lower strike, then repeat at an upper strike. Calls, puts or a combination can be used depending on platform and pricing."),
("Why use two targets", "Two calendar peaks can create a broader modeled profitable region than one calendar. The space between peaks depends on strikes, expiration gap, IV and time."),
("Risk and pricing", "The total debit is usually the initial risk budget, but assignment or unpaired legs can alter exposure. Eight contracts per unit make commissions and combined bid-ask width important."),
("Management", "Each side can react differently as price moves and skew changes. Closing or rolling one calendar leaves a separate directional time spread, so analyze the remaining position on its own."),
], "With stock at $100, combine a 95 put calendar and a 105 call calendar using 30-day shorts and 60-day longs to create two front-expiration targets.",
[("Is a double calendar an iron condor?", "No. It uses different expirations and retains back-month options."),("Does it guarantee a wider profit zone?", "No. The modeled valley between peaks can still be unprofitable."),("Why are costs important?", "The structure uses many contracts.")]),

guide("calendar-spread-greeks", "Greeks", "Calendar Spread Greeks: Delta, Gamma, Theta and Vega",
"Understand how near- and back-month options combine into calendar delta, gamma, theta and vega.",
"A calendar often starts positive theta and positive vega, but every Greek changes with price, time and the relationship between expirations.", [
("Delta", "An ATM calendar may begin near delta-neutral because the two options partly offset. OTM calendars carry directional delta toward the target, and delta can reverse after price passes the strike."),
("Gamma", "The short front option often has more gamma than the longer option, creating negative net gamma near the strike as front expiration approaches. Small moves can therefore change delta unfavorably."),
("Theta", "The front option usually decays faster, supporting positive net theta near the target. Far from the strike or after a large price move, the balance can change."),
("Vega", "The longer-dated option typically has more vega, creating positive net exposure. A back-month volatility contraction can hurt even while front-month time decay works as expected."),
], "A calendar shows delta +0.04, gamma −0.03, theta +0.07 and vega +0.16 per share. Position size and contract multiplier turn these into material dollar exposures.",
[("Is calendar theta always positive?", "No. Price and time can change it."),("Why is vega often positive?", "The longer option generally has greater volatility sensitivity."),("Can delta reverse?", "Yes, as price crosses the target strike.")]),

guide("theta-time-decay-calendar-spread", "Theta", "Theta and Time Decay in a Calendar Spread",
"Learn how differential time decay creates calendar theta and when passing time helps or hurts the position.",
"Time decay helps when the short option loses extrinsic value faster while the longer option retains useful time value.", [
("Front-month acceleration", "Short-dated extrinsic value tends to decay faster as expiration approaches. That decay is the calendar's central advantage only if price remains near the strike and other inputs do not move adversely."),
("Back-month preservation", "The long option also decays, just usually more slowly. A large expiration gap can preserve more time value but costs a larger debit and may carry more vega."),
("Gamma tradeoff", "Faster front decay comes with rising short gamma. A small underlying move near expiration can create a loss larger than several days of favorable theta."),
("After front expiration", "If the short expires, the trader owns a standalone longer-dated option unless it is sold or another option is written. That new position has different theta and directional risk."),
], "The short option loses $8 of theoretical value in one day while the long loses $4, creating about $4 positive theta per spread before price and IV changes.",
[("Is theta collected as cash?", "No. It is a model estimate reflected in prices."),("Does the long option decay too?", "Yes."),("Why can positive theta still lose?", "Gamma, delta and vega changes may dominate.")]),

guide("implied-volatility-calendar-spread", "Vega", "Implied Volatility and Vega in Calendar Spreads",
"Understand volatility term structure, front-versus-back IV, event premium and the calendar's typically positive vega exposure.",
"Calendar value depends on relative volatility across expirations, not only whether one headline IV number rises or falls.", [
("Positive net vega", "The later option commonly has more vega than the near option, leaving positive net exposure. A broad IV rise can help, while back-month contraction can damage the position."),
("Term structure", "Front and back expirations often trade at different IV levels and may move independently. A calendar can lose even during a broad IV rise if the short expiration rises much more than the long expiration."),
("Event placement", "When earnings fall between expirations, the back option may contain event premium that the front option does not. After the event moves into or out of a maturity, the structure can reprice abruptly."),
("Surface scenarios", "Model separate changes for front IV and back IV at several stock prices. A parallel shift is only one scenario and can hide term-structure and skew risk."),
], "Front IV rises from 25% to 32% while back IV moves from 27% to 29%. Despite positive net vega, the short option's relative expansion may hurt the calendar.",
[("Does higher IV always help?", "No. Relative expiration changes matter."),("What is term structure?", "The pattern of IV across expiration dates."),("Why can earnings help or hurt?", "Event premium may be concentrated in only one leg.")]),

guide("adjust-calendar-spread", "Adjustments", "How to Adjust a Calendar Spread",
"Evaluate rolling the short option, moving the strike, changing duration or converting a calendar into another structure.",
"Every calendar adjustment changes term structure, target, Greeks and total debit; judge the resulting trade as a new position.", [
("Close or reduce", "When the target or volatility thesis fails, closing both legs or reducing size is the cleanest response. A small defined debit does not make repeated adjustments automatically sensible."),
("Roll the short expiration", "Buying back the front option and selling a later option can collect or spend value and extend the trade. Track total credits against the original debit and the remaining long option's life."),
("Move the strike", "Rolling the short to a different strike creates a diagonal and new directional exposure. The original calendar payoff graph no longer describes the position."),
("Change the structure", "Adding another calendar can create a double calendar; adding vertical legs can create a more complex hybrid. Recalculate assignment, buying power and every Greek before modifying protective relationships."),
], "A 100 calendar misses as stock rises to $105. Rolling the short 100 call to a later 105 call creates a diagonal with a new target and delta, not a repaired version of the same trade.",
[("Must a losing calendar be rolled?", "No. Closing may be preferable."),("Can a roll create a diagonal?", "Yes, if the strike changes."),("How should roll credit be measured?", "Against all prior debits and credits, not in isolation.")]),

guide("when-to-close-calendar-spread", "Management", "When to Close a Calendar Spread",
"Plan profit, target, volatility, time and assignment exits for a calendar before the front option approaches expiration.",
"Close based on executable spread value and thesis validity, with an explicit decision for the remaining back-month option.", [
("Profit target", "Consider closing after the spread reaches a planned return or captures a meaningful portion of modeled potential. A broker's theoretical peak may depend on an IV assumption that will not occur."),
("Price exit", "If the underlying moves too far from the strike or passes the target at the wrong time, delta and gamma can overwhelm theta. Define a price or loss level for reassessment."),
("Volatility exit", "A collapse in back-month IV or adverse term-structure move can invalidate the trade even when price behaves. Monitor each expiration rather than one aggregate IV reading."),
("Front-expiration decision", "Before the short expires, close the pair, roll the short or intentionally retain the long option. Avoid accidental assignment or an unplanned standalone option."),
], "A calendar bought for $1.70 can be sold for $2.45 with front expiration approaching. Closing locks about $75 rather than accepting gamma and assignment risk for an uncertain remaining peak.",
[("Must I wait for front expiration?", "No."),("Can I keep the back option?", "Yes, but it becomes a separate long-option decision."),("Why close both legs together?", "It controls spread value and avoids temporary naked exposure.")]),

guide("calendar-spread-mistakes", "Risk Management", "Calendar Spread: 12 Mistakes to Avoid",
"Avoid calendar spread errors involving expiration selection, IV term structure, target timing, assignment, execution and management.",
"Calendar spreads are not simple theta trades; price, volatility and two separate clocks must align with the plan.", [
("Mistakes 1–3: weak thesis", "Do not choose a strike without a timed target, assume sideways price guarantees profit or sell the nearest expiration by habit. The target must align with the front-expiration window."),
("Mistakes 4–6: volatility", "Do not look only at headline IV, ignore term structure or assume positive vega means every IV rise helps. Model front and back expirations separately."),
("Mistakes 7–9: execution", "Do not leg into the spread casually, ignore combined bid-ask width or overlook four-leg costs across entry and exit. Confirm option type, strike, dates and ratio."),
("Mistakes 10–12: management", "Do not hold through front expiration without a plan, evaluate roll credit alone or forget assignment and dividend risk. Verify the final account position after every fill."),
], "A trader buys a calendar before earnings without noticing the event is priced only in the back month, then holds the ITM short call into expiration. Volatility and assignment risks were both misread.",
[("What is the biggest mistake?", "Treating a calendar as guaranteed positive theta."),("Why is the front expiration critical?", "It changes the spread into a standalone long option if not managed."),("Can correct price still lose?", "Yes, if volatility or timing differs from the model.")]),
]

base.ARTICLES = ARTICLES
base.COURSE = COURSE
base.DATE = "September 12, 2026"


def article_html(article: dict, index: int) -> str:
    return (base.article_html(article, index)
            .replace("2026-09-11", "2026-09-12")
            .replace("Learn Vega — Free", "Learn Calendar Spreads — Free")
            .replace("Vega &amp; Volatility", "Calendar Spreads")
            .replace("Vega planning example", "Calendar spread example")
            .replace("This simplified example holds other inputs constant to isolate volatility exposure.", "This simplified example uses selected price, time and volatility assumptions; live results will differ.")
            .replace("Level 6 – Calendar Spreads course", "Level 13 – Calendar Spreads course")
            .replace("Level 6 – Vega &amp; Volatility course", "Level 13 – Calendar Spreads course")
            .replace("Start Level 6 — Free", "Start Level 13 — Free")
            .replace("Free Level 6 Course", "Free Level 13 Course")
            .replace("Learn vega and volatility through structured lessons and practical examples.", "Learn Calendar Spreads through structured lessons and practical examples."))


def update_index() -> None:
    path = BLOG / "index.html"
    source = path.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    if 'href="calendar-spread-explained/"' not in source:
        source = source.replace(marker, "\n".join(base.card_html(a) for a in ARTICLES) + "\n" + marker, 1)
    source = source.replace("<strong>191</strong> guides", "<strong>207</strong> guides")
    if "Explore Level 13" not in source:
        source = source.replace('<a class="btn btn-gold" href="../courses/advanced-option-level-12-butterfly/">Explore Level 12 →</a>', '<a class="btn btn-gold" href="../courses/advanced-option-level-12-butterfly/">Explore Level 12 →</a><a class="btn btn-gold" href="../courses/advanced-option-level-13-calendar-spreads/">Explore Level 13 →</a>')
    path.write_text(source)


def update_scripts() -> None:
    path = BLOG / "blog.js"
    source = path.read_text().replace("const clusterPriority = card => card.textContent.includes('Butterfly Spread') ? 12 :", "const clusterPriority = card => card.textContent.includes('Calendar Spread') ? 13 : card.textContent.includes('Butterfly Spread') ? 12 :")
    path.write_text(source)
    path = ROOT / "favicon.js"
    source = path.read_text()
    marker = "    'butterfly-spread-mistakes': '/assets/images/blog/butterfly-spread-mistakes.webp'"
    additions = ",\n".join(f"    '{a['slug']}': '/assets/images/blog/{a['slug']}.webp'" for a in ARTICLES)
    if "'calendar-spread-explained'" not in source:
        source = source.replace(marker, marker + ",\n" + additions)
    path.write_text(source)


def update_existing_links() -> None:
    targets = ["option-greeks-calendar-spreads", "vega-vs-theta-options", "positive-theta-option-strategies",
               "vega-expiration-long-term-short-term-options", "butterfly-spread-explained", "short-iron-condor-explained"]
    bridge = ('<p class="cluster-bridge"><strong>Continue learning:</strong> Read the '
              '<a href="../calendar-spread-explained/">Calendar Spread guide</a> and take the '
              '<a href="../../courses/advanced-option-level-13-calendar-spreads/">free Level 13 course</a>.</p>\n')
    for slug in targets:
        path = BLOG / slug / "index.html"
        if path.exists():
            source = path.read_text()
            if "../calendar-spread-explained/" not in source:
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
    draw.text((76, 63), f"LEVEL 13  •  GUIDE {index + 1:02d}", font=font(18, True), fill="#07172d")
    y = 145
    for line in textwrap.wrap(article["title"], width=24)[:4]:
        draw.text((62, y), line, font=font(42, True), fill="white")
        y += 50
    draw.text((64, 570), "OPTIONS AMERICA", font=font(22, True), fill="#b9c9da")
    draw.text((64, 605), "Calendar Spread Learning Series", font=font(20), fill="#7892aa")
    draw.rounded_rectangle((720, 150, 1130, 505), 28, fill="#081c32", outline="#31506d", width=2)
    draw.line((760, 430, 1090, 430), fill="#6b8298", width=2)
    draw.line((925, 190, 925, 455), fill="#31506d", width=2)
    curve = [(760, 430), (810, 420), (860, 350), (900, 250), (925, 220), (950, 250), (990, 350), (1040, 420), (1090, 430)]
    draw.line(curve, fill=accent, width=8, joint="curve")
    if index == 1:
        draw.line((790, 205, 1060, 205), fill="#52d3ff", width=4)
        draw.text((790, 175), "FRONT", font=font(13, True), fill="#52d3ff")
        draw.text((1000, 175), "BACK", font=font(13, True), fill=accent)
    elif index == 2:
        draw.line((825, 210, 825, 445), fill="#ff8e72", width=3)
        draw.line((1025, 210, 1025, 445), fill="#ff8e72", width=3)
        draw.text((865, 195), "MODELED RANGE", font=font(13, True), fill="white")
    elif index == 3:
        for x, ydot in ((785, 425), (850, 365), (925, 220), (1000, 365), (1065, 425)):
            draw.ellipse((x-7, ydot-7, x+7, ydot+7), fill="#52d3ff")
    elif index == 4:
        for x in (840, 925, 1010): draw.line((x, 205, x, 450), fill="#31506d", width=2)
    elif index == 5:
        for x, label in ((770, "21D"), (875, "49D"), (990, "91D")):
            draw.rounded_rectangle((x, 195, x+65, 232), 10, outline=accent, width=2)
            draw.text((x+13, 205), label, font=font(13, True), fill="white")
    elif index == 6:
        draw.line([(760, 440), (840, 365), (925, 235), (1010, 365), (1090, 440)], fill="#52d3ff", width=4)
        draw.line([(760, 420), (840, 345), (925, 255), (1010, 345), (1090, 420)], fill="#ff8e72", width=4)
    elif index == 7:
        draw.line([(760, 440), (825, 390), (900, 265), (980, 330), (1090, 430)], fill="#ff8e72", width=5)
    elif index == 8:
        draw.line([(760, 430), (820, 430), (870, 290), (980, 290), (1030, 430), (1090, 430)], fill="#52d3ff", width=4)
    elif index == 9:
        second = [(760, 430), (800, 410), (845, 315), (875, 280), (910, 315), (955, 410), (1090, 430)]
        draw.line(second, fill="#80e0a7", width=4)
    elif index == 10:
        for x, h, c in ((770, 80, "#52d3ff"), (830, 130, accent), (890, 60, "#80e0a7"), (950, 110, "#ff8e72")):
            draw.rounded_rectangle((x, 445-h, x+34, 445), 8, fill=c)
    elif index == 11:
        draw.arc((785, 205, 965, 385), 0, 300, fill="#52d3ff", width=5)
        draw.line((875, 295, 875, 237), fill="white", width=4)
        draw.line((875, 295, 920, 320), fill="white", width=4)
    elif index == 12:
        for box, c in (((755, 205, 880, 350), "#52d3ff"), ((855, 220, 1015, 370), "#80e0a7"), ((980, 250, 1090, 355), "#ff8e72")):
            draw.arc(box, 5, 175, fill=c, width=4)
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
