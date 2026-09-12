#!/usr/bin/env python3
"""Build the Level 11 Short Iron Condor SEO cluster and original artwork."""

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
COURSE = "../../courses/advanced-option-level-11-short-iron-condor/"


def guide(slug, tag, title, description, key, sections, example, faq):
    return dict(slug=slug, tag=f"Short Iron Condor · {tag}", title=title, description=description,
                key=key, sections=sections, example=example, faq=faq)


ARTICLES = [
guide("short-iron-condor-explained", "Complete Guide", "Short Iron Condor Explained: Strategy, Risk and Reward",
"Learn how a short iron condor combines two credit spreads to create a defined-risk options position for a range-bound market.",
"A short iron condor collects a net credit and reaches maximum profit when the underlying finishes between its two short strikes at expiration.", [
("The four-leg structure", "Sell an OTM put and buy a farther OTM put, then sell an OTM call and buy a farther OTM call with the same expiration. The long wings define risk on both sides while the short options establish the intended range."),
("Market outlook", "The strategy fits a neutral outlook in which realized movement is expected to remain inside a selected range. It is commonly evaluated when option premiums appear rich, but elevated IV can also warn that a large move is plausible."),
("Defined payoff", "Maximum profit is the opening credit. Maximum loss is generally the wider wing width minus the credit, multiplied by the contract multiplier. There are two expiration breakevens around the profitable range."),
("Risk before expiration", "Delta, gamma, theta, vega, skew and time interact across four legs. Defined maximum loss does not prevent rapid mark-to-market losses, difficult fills, early assignment or expiration complications."),
], "Sell the 95/90 put spread and the 105/110 call spread for a total $1.60 credit. Maximum profit is $160 and maximum loss is $340 per standard condor before costs.",
[("Is a short iron condor neutral?", "It is designed for a range-bound outlook, although live delta may not be exactly zero."),("Is risk unlimited?", "No. Long wings define risk when the position is constructed correctly."),("Where is maximum profit?", "Between the two short strikes at expiration.")]),

guide("how-to-build-short-iron-condor", "Step by Step", "How to Build a Short Iron Condor",
"Build a short iron condor by selecting an underlying, expiration, short strikes, protective wings and a four-leg limit credit.",
"Start with the expected range and risk budget, then choose all four strikes as one complete position rather than four independent options.", [
("Define the range", "Estimate the price zone expected through the chosen expiration using market structure, event risk and option-implied movement. The forecast must be specific enough to evaluate whether both short strikes provide meaningful room."),
("Choose the short options", "Sell an OTM put below the market and an OTM call above it. Delta or probability metrics can provide consistent reference points, but they are model estimates rather than guaranteed probabilities."),
("Add protective wings", "Buy a lower-strike put and a higher-strike call. Equal wing widths create a balanced condor; unequal widths change maximum loss and buying-power exposure on each side."),
("Enter as one order", "Use a four-leg limit order for a net credit. Confirm expiration, quantities, strike order, maximum loss, commission impact and assignment procedures before transmitting the trade."),
], "With shares at $100, sell the 95 put and 105 call, buy the 90 put and 110 call, and enter all four legs together at a chosen net credit.",
[("Which options are sold?", "The two inner strikes."),("Which options define risk?", "The farther OTM long put and long call."),("Should I leg into it?", "A single limit order usually offers clearer price and risk control.")]),

guide("short-iron-condor-profit-loss-breakevens", "Payoff", "Short Iron Condor Profit, Loss and Breakevens",
"Calculate maximum profit, maximum loss and both expiration breakevens from the strikes, wing widths and net credit.",
"The credit creates two breakevens: short put minus credit and short call plus credit, when both wings have equal width.", [
("Maximum profit", "The opening net credit is retained when all four options expire worthless, which requires the underlying to finish between the short put and short call. Subtract commissions and fees from the real result."),
("Maximum loss", "For equal-width wings, subtract the credit from the strike width. If widths differ, calculate each side independently; the wider side can produce the larger loss and may determine buying power."),
("Lower breakeven", "Subtract the credit per share from the short-put strike. Below that level at expiration, losses increase until the long put caps the put-side loss."),
("Upper breakeven", "Add the credit per share to the short-call strike. Above it, losses increase until the long call caps the call-side loss."),
], "A 90/95/105/110 condor receives $1.50. Breakevens are $93.50 and $106.50; maximum profit is $150 and maximum loss is $350 per spread.",
[("Can both sides lose at expiration?", "Only one side can be breached by one final underlying price."),("Do unequal wings change the formula?", "Yes. Calculate call-side and put-side loss separately."),("Is the credit guaranteed profit?", "No. It is only maximum profit if the price finishes inside the short strikes.")]),

guide("short-iron-condor-example", "Worked Example", "Short Iron Condor Example With Full Payoff Scenarios",
"Follow a complete iron condor example across prices below, inside and above its profit range at expiration.",
"Scenario analysis shows why a high probability of a small credit must be weighed against the larger defined loss outside the wings.", [
("Set up the trade", "Assume stock is $100. Buy the 90 put, sell the 95 put, sell the 105 call and buy the 110 call for a net $1.40 credit. Each side is five points wide."),
("Inside the range", "Between $95 and $105 at expiration, all options expire worthless and the $140 credit is maximum profit. At $94 or $106, one short option has $1 intrinsic value, leaving a $40 profit before costs."),
("Between short and long strikes", "At $92, the short put is worth $3 while the long put is worthless. Subtracting $300 from the $140 credit produces a $160 loss. The call side expires worthless."),
("Beyond a long wing", "At $88 or $112, one vertical spread is worth its full $5 width. The defined expiration loss is $500 minus the $140 credit, or $360."),
], "At expiration prices of $88, $92, $100, $108 and $112, approximate P&L is −$360, −$160, +$140, −$160 and −$360 before costs.",
[("What happens exactly at a short strike?", "The full credit is normally retained at expiration, ignoring costs."),("Can it be closed early?", "Yes, by buying back the complete condor."),("Why model five prices?", "It reveals the plateau, transition zones and capped losses.")]),

guide("choose-short-iron-condor-strikes", "Strike Selection", "How to Choose Short Iron Condor Strikes",
"Choose short strikes and protective wings using expected range, delta, skew, credit, liquidity and maximum-loss limits.",
"Short strikes define the profit zone; long strikes define tail risk. Choose them together rather than maximizing credit alone.", [
("Anchor the short strikes", "Use the expected range, chart levels and option deltas as reference points. Moving short strikes farther away increases room but usually reduces credit, theta and compensation for risk."),
("Choose wing widths", "Narrow wings reduce maximum dollar loss and credit. Wider wings can improve credit and execution but increase capital at risk. Unequal wings express an asymmetric forecast and require separate loss calculations."),
("Account for skew", "Put skew often makes downside protection expensive and put-side credit different from call-side credit. Equal deltas do not necessarily create equal distance, risk or premium."),
("Check all four markets", "Evaluate bid-ask width, volume, open interest and realistic combined fills. One illiquid wing can make a visually attractive payoff difficult or expensive to manage."),
], "At $100, compare 90/95/105/110 with 85/92/108/115. The wider range may have less credit and different downside-versus-upside exposure.",
[("Are 15-delta shorts required?", "No. Delta is one selection input, not a rule."),("Should wings always be equal?", "No, but unequal risk must be intentional."),("Why not choose the widest range?", "Very distant shorts may provide too little credit for the risk and costs.")]),

guide("short-iron-condor-expiration-dte", "Expiration", "Short Iron Condor Expiration and DTE Selection",
"Compare short and longer expirations for credit, theta, gamma, vega, event exposure and management time.",
"Expiration determines how quickly the position earns decay and how violently risk can change when price approaches a short strike.", [
("Short-duration condors", "Near-term positions can decay quickly but carry concentrated gamma. A small move can rapidly change delta and loss, leaving little time or liquidity for an adjustment."),
("Longer-duration condors", "More time can provide wider strikes and larger credits, but vega exposure and event uncertainty remain for longer. Capital may be committed through several market regimes."),
("Match the event calendar", "Avoid placing an unplanned earnings announcement, economic release or dividend inside the trade. High IV does not automatically compensate for discontinuous gap risk."),
("Set the management date", "Choose a profit target and a latest review date before entry. Many traders close before expiration to reduce assignment and last-week gamma risk rather than seeking the final portion of credit."),
], "Compare a 21-DTE condor with a 45-DTE condor using the same delta targets. The nearer trade may offer faster theta but a narrower dollar range and sharper gamma.",
[("What DTE is best?", "There is no universal value; it depends on range, events and risk plan."),("Does theta always accelerate safely?", "No. Gamma risk accelerates too."),("Must it expire worthless?", "No. It can be closed early for a debit.")]),

guide("iv-rank-short-iron-condor", "Volatility", "IV Rank and IV Percentile for Short Iron Condors",
"Use IV Rank, IV Percentile, term structure and event context when evaluating a short iron condor entry.",
"High relative IV can support richer credit, but it often exists because the market expects real movement or event risk.", [
("What IV Rank measures", "IV Rank places current implied volatility within a selected high-low range. One extreme observation can distort the result, so review the actual series and lookback methodology."),
("What IV Percentile measures", "IV Percentile estimates how often historical IV readings were below today's level. It describes frequency rather than distance from the high and can disagree sharply with IV Rank."),
("Why high IV is not enough", "Rich premium increases potential credit and breakeven width, but a volatility spike may coincide with unstable price or a known catalyst. Selling volatility is not automatically favorable because a metric is elevated."),
("Read the surface", "Compare expiration-specific IV, put-call skew and expected movement. The four legs can reprice differently, so one headline IV number does not describe the complete condor."),
], "IV Percentile is 80 while IV Rank is 42 after one historic spike. The readings answer different questions and neither replaces analysis of earnings, skew and expected move.",
[("Must IV Rank be above 50?", "No fixed threshold guarantees a good trade."),("Can high IV rise further?", "Yes, producing vega losses and often larger price moves."),("Which metric is better?", "Use both only after understanding each platform's calculation.")]),

guide("short-iron-condor-vs-short-strangle", "Comparison", "Short Iron Condor vs Short Strangle",
"Compare two neutral premium strategies across credit, maximum loss, buying power, Greeks, adjustment flexibility and tail risk.",
"The iron condor buys protective wings to define risk; the short strangle receives more credit but retains substantial tail exposure.", [
("Construction", "Both sell an OTM put and OTM call. The condor adds a farther OTM long put and long call, reducing credit while capping losses beyond the wings."),
("Capital and risk", "Defined risk can reduce buying-power requirements, depending on the broker. A short strangle can suffer very large downside losses and theoretically unlimited upside loss from the uncovered call."),
("Greeks and management", "Long wings reduce net negative vega, negative gamma and positive theta. They also change adjustment economics because rolling one side can alter width and defined-risk status."),
("Decision framework", "Compare expected range, volatility, account permissions, stress loss and liquidity. A larger strangle credit is compensation for a fundamentally different tail-risk profile."),
], "A short strangle collects $3.20. Adding two $0.45 wings creates a condor for $2.30 credit and transforms open-ended tail risk into known maximum losses.",
[("Which collects more credit?", "Normally the short strangle."),("Which has defined risk?", "The iron condor."),("Are the long wings free?", "No. Their cost reduces the net credit.")]),

guide("short-iron-condor-vs-iron-butterfly", "Comparison", "Iron Condor vs Iron Butterfly",
"Compare the short iron condor and iron butterfly through strike placement, credit, profit range, breakevens and directional tolerance.",
"An iron butterfly places both short options at one central strike; an iron condor separates them to create a wider maximum-profit range.", [
("Structure", "The iron butterfly sells an ATM call and put at the same strike and buys outside wings. The condor sells an OTM put and OTM call at different strikes."),
("Credit and maximum profit", "The butterfly usually collects more credit because its short straddle is closer to the money. The condor generally collects less but can retain maximum profit across a range rather than at one exact strike."),
("Breakevens", "A larger butterfly credit can create meaningful breakevens, yet its P&L changes immediately away from the body strike. Condor short strikes create a flat expiration-profit plateau between them."),
("Choose by forecast", "Use the butterfly when the forecast centers on a specific expiration price and its reward justifies concentration. Use the condor when the thesis is a broader range with smaller maximum credit."),
], "With $100 stock, a 95/100/105 iron butterfly targets $100. A 90/95/105/110 iron condor accepts less credit in exchange for a $95–$105 maximum-profit zone.",
[("Which has a wider profit plateau?", "The iron condor."),("Which often receives more credit?", "The iron butterfly."),("Are both defined-risk?", "Yes, when their long wings are maintained.")]),

guide("short-iron-condor-greeks", "Greeks", "Short Iron Condor Greeks: Delta, Gamma, Theta and Vega",
"Understand how four option legs combine into the net Greeks of a short iron condor and how those exposures change near each boundary.",
"A centered condor may begin near delta-neutral, positive theta and negative vega, but movement toward a short strike can change risk quickly.", [
("Delta", "Call-side and put-side delta may offset near entry. As price approaches the short call, net delta becomes increasingly negative; toward the short put, it becomes increasingly positive, resisting the move and creating losses."),
("Gamma", "Short options usually dominate the long wings, leaving negative gamma through much of the central range. Delta therefore changes unfavorably during large moves, especially close to expiration."),
("Theta and vega", "The position commonly earns positive theta and carries negative vega. Long wings reduce both exposures, and their net values vary with price, time, skew and unequal strike placement."),
("Portfolio scaling", "Add signed Greeks across all legs, multiply by contract quantity and multiplier, and beta-weight when appropriate. Entry neutrality does not remain fixed, so test up, down and volatility scenarios."),
], "A centered condor begins at delta −0.02, theta +0.11 and vega −0.18 per share. Ten contracts scale those theoretical sensitivities dramatically and require stress testing.",
[("Is delta exactly zero?", "Rarely, and it changes continuously."),("Why is gamma negative?", "The short inner options often dominate the long wings."),("Does positive theta guarantee profit?", "No. Delta, gamma and vega losses can be larger.")]),

guide("theta-time-decay-short-iron-condor", "Theta", "Theta and Time Decay in a Short Iron Condor",
"Learn when time decay helps a short iron condor and why positive theta does not remove price, gamma or volatility risk.",
"Time decay helps most when price stays comfortably inside the range and implied volatility does not expand materially.", [
("How theta is created", "The two short inner options generally lose time value faster in total than the cheaper long wings, producing positive net theta. The effect depends on moneyness and the exact four-leg structure."),
("The center of the range", "Theta is typically most useful when both short options remain OTM and the position is not threatened. Daily decay estimates assume other inputs stay constant, which real markets do not do."),
("Near a boundary", "As price approaches a short strike, negative gamma and directional delta can overwhelm accumulated decay. A high theta number can accompany a position that is already carrying substantial loss risk."),
("Expiration tradeoff", "Theta may accelerate late in the cycle, but so do gamma, assignment and execution risks. Compare remaining credit with potential reversal loss rather than holding automatically for every dollar."),
], "A condor earns an estimated $9 from one day of theta but loses $70 from an adverse move and IV expansion. Positive theta describes only one component of total P&L.",
[("Does theta arrive as cash?", "No. It is a model estimate reflected in option prices."),("Is more theta always better?", "No. It can accompany higher gamma or narrower strikes."),("Why close early?", "To avoid risking a large amount for a small remaining credit.")]),

guide("implied-volatility-short-iron-condor", "Vega", "Implied Volatility and Vega in a Short Iron Condor",
"Understand how IV contraction, expansion, skew and term structure affect the four legs of a short iron condor.",
"Short iron condors are often net short vega, so falling IV can help while a volatility expansion can hurt even before a short strike is breached.", [
("Net negative vega", "The short inner options often carry more combined vega than the farther long wings, leaving negative net exposure. A parallel IV decline may reduce the debit required to close."),
("Volatility expansion", "IV often rises during fast price moves, combining vega loss with adverse delta and gamma. Long wings cap expiration loss but may not prevent a sharp interim drawdown."),
("Skew and surface risk", "Put and call strikes can reprice differently. A downside selloff may steepen put skew, so modeling one uniform IV shift can understate put-side loss."),
("Event volatility", "Earnings may offer rich credit and a large expected range, but the realized gap can exceed both short and long strikes. Compare the event-implied move with the complete defined loss."),
], "Net vega of −0.20 implies roughly a $20 loss per IV point per standard condor, all else equal. A five-point expansion suggests about −$100 before price and time effects.",
[("Does falling IV guarantee profit?", "No. A price move can overwhelm vega gains."),("Do wings remove vega?", "They reduce but rarely eliminate it."),("Why model skew?", "Each strike may experience a different IV change.")]),

guide("adjust-short-iron-condor", "Adjustments", "How to Adjust a Short Iron Condor",
"Evaluate rolling, moving the untested side, adding protection, narrowing risk or closing without turning one defined trade into uncontrolled exposure.",
"Every adjustment is a new trade. Compare its incremental credit, added risk, commissions and new breakevens with simply closing the position.", [
("Close or reduce", "Closing the complete condor or reducing size is the cleanest way to lower risk. Defined maximum loss is not a reason to keep a broken position open."),
("Move the untested side", "Rolling the profitable side toward the market may collect credit and reduce delta, but it narrows the range and creates whipsaw risk if price reverses."),
("Roll the tested side", "Moving threatened strikes away or out in time can require a debit, widen risk or extend exposure. Recalculate total credit and maximum loss after every proposed roll."),
("Protect the account", "Confirm all fills and maintain the long wings. Closing a protective option or one spread can leave uncovered short-option risk, assignment exposure or unexpected buying-power usage."),
], "Price approaches the short call. Rolling the put spread upward adds credit but narrows the downside room; rolling calls outward may cost debit. Both choices must be compared with closing.",
[("Must every tested condor be adjusted?", "No. Closing can be the best risk decision."),("Should I always roll the untested side?", "No. It increases reversal risk."),("Can an adjustment increase maximum loss?", "Yes, especially when widths, quantities or expirations change.")]),

guide("when-to-close-short-iron-condor", "Management", "When to Close a Short Iron Condor",
"Create profit, loss, time, volatility and event exits for a short iron condor before opening the four-leg position.",
"Manage the condor using the cost to close, remaining credit and range validity rather than waiting automatically for expiration.", [
("Profit target", "Many plans close after capturing a selected portion of maximum profit because the remaining reward shrinks while tail and reversal risk continue. Use a realistic four-leg closing debit."),
("Price and loss exits", "Define action points near each short strike and a maximum acceptable position loss. A tested strike is a warning, not a universal automatic adjustment signal."),
("Time and volatility exits", "Close or reassess if price fails to stabilize, IV expands beyond the thesis or the trade reaches its planned management date. Avoid adding time merely to postpone recognizing a loss."),
("Expiration operations", "Short ITM options may be assigned and long options may exercise. Closing before expiration can reduce pin risk, settlement uncertainty and accidental share positions."),
], "A condor opened for $2 can be bought back for $1, capturing half its maximum credit. The decision compares the remaining $100 potential with the full range and tail risk still carried.",
[("Must I wait for 100% profit?", "No."),("How is the position closed?", "Buy back all four legs as a condor order."),("What is pin risk?", "Expiration near a strike can create uncertain exercise and assignment outcomes.")]),

guide("short-iron-condor-mistakes", "Risk Management", "Short Iron Condor: 12 Mistakes to Avoid",
"Avoid errors involving IV, narrow ranges, small credits, position size, liquidity, adjustments, assignment and expiration.",
"Defined risk does not make every condor attractive; the small maximum profit must be evaluated against frequency and size of losses.", [
("Mistakes 1–3: weak entry", "Do not sell premium only because IV is high, choose short strikes without an expected range or accept tiny credit relative to width. Elevated IV often reflects genuine risk."),
("Mistakes 4–6: construction", "Do not ignore skew, mix expirations or overlook unequal wing loss. Verify all four quantities, strikes, buying power and realistic fill before entry."),
("Mistakes 7–9: oversizing", "Do not size by maximum profit, confuse probability with certainty or assume long wings prevent painful drawdowns. Multiple condors can create large correlated exposure."),
("Mistakes 10–12: management", "Do not adjust repeatedly without total P&L, hold for the final credit near expiration or leave a short option uncovered after partial fills. Confirm the final account position."),
], "A trader opens ten narrow condors for a small credit because modeled probability looks high, then a volatility shock breaches one side. Defined loss multiplied by ten becomes the real risk.",
[("What is the biggest mistake?", "Oversizing a trade with a small credit and larger maximum loss."),("Does high probability mean safe?", "No. Loss severity and model error matter."),("Why verify closing fills?", "Four legs create more ways to leave unintended exposure.")]),
]

base.ARTICLES = ARTICLES
base.COURSE = COURSE
base.DATE = "September 12, 2026"


def article_html(article: dict, index: int) -> str:
    return (base.article_html(article, index)
            .replace("2026-09-11", "2026-09-12")
            .replace("Learn Vega — Free", "Learn Short Iron Condors — Free")
            .replace("Vega &amp; Volatility", "Short Iron Condor")
            .replace("Vega planning example", "Short iron condor example")
            .replace("This simplified example holds other inputs constant to isolate volatility exposure.", "This simplified example focuses on one position and a limited set of price and volatility outcomes.")
            .replace("Continue the Short Iron Condor cluster", "Continue the Short Iron Condor cluster")
            .replace("Level 6 – Short Iron Condor course", "Level 11 – Short Iron Condor course")
            .replace("Level 6 – Vega &amp; Volatility course", "Level 11 – Short Iron Condor course")
            .replace("Start Level 6 — Free", "Start Level 11 — Free")
            .replace("Free Level 6 Course", "Free Level 11 Course")
            .replace("Learn vega and volatility through structured lessons and practical examples.", "Learn the Short Iron Condor through structured lessons and practical examples."))


def update_index() -> None:
    path = BLOG / "index.html"
    source = path.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    if 'href="short-iron-condor-explained/"' not in source:
        source = source.replace(marker, "\n".join(base.card_html(a) for a in ARTICLES) + "\n" + marker, 1)
    source = source.replace("<strong>160</strong> guides", "<strong>175</strong> guides")
    if "Explore Level 11" not in source:
        source = source.replace('<a class="btn btn-gold" href="../courses/advanced-option-level-10-bear-put-spread/">Explore Level 10 →</a>', '<a class="btn btn-gold" href="../courses/advanced-option-level-10-bear-put-spread/">Explore Level 10 →</a><a class="btn btn-gold" href="../courses/advanced-option-level-11-short-iron-condor/">Explore Level 11 →</a>')
    path.write_text(source)


def update_scripts() -> None:
    path = BLOG / "blog.js"
    source = path.read_text().replace("const clusterPriority = card => card.textContent.includes('Bear Put Spread') ? 10 :", "const clusterPriority = card => card.textContent.includes('Short Iron Condor') ? 11 : card.textContent.includes('Bear Put Spread') ? 10 :")
    path.write_text(source)
    path = ROOT / "favicon.js"
    source = path.read_text()
    marker = "    'bear-put-spread-mistakes': '/assets/images/blog/bear-put-spread-mistakes.webp'"
    additions = ",\n".join(f"    '{a['slug']}': '/assets/images/blog/{a['slug']}.webp'" for a in ARTICLES)
    if "'short-iron-condor-explained'" not in source:
        source = source.replace(marker, marker + ",\n" + additions)
    path.write_text(source)


def update_existing_links() -> None:
    targets = ["option-greeks-iron-condor", "iv-rank-vs-iv-percentile", "positive-theta-option-strategies",
               "option-greeks-credit-spreads", "how-option-greeks-interact", "bear-put-spread-explained"]
    bridge = ('<p class="cluster-bridge"><strong>Apply the concept:</strong> Continue with the '
              '<a href="../short-iron-condor-explained/">Short Iron Condor guide</a> and the '
              '<a href="../../courses/advanced-option-level-11-short-iron-condor/">free Level 11 course</a>.</p>\n')
    for slug in targets:
        path = BLOG / slug / "index.html"
        if path.exists():
            source = path.read_text()
            if "../short-iron-condor-explained/" not in source:
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
    draw.text((76, 63), f"LEVEL 11  •  GUIDE {index + 1:02d}", font=font(18, True), fill="#07172d")
    y = 145
    for line in textwrap.wrap(article["title"], width=24)[:4]:
        draw.text((62, y), line, font=font(42, True), fill="white")
        y += 50
    draw.text((64, 570), "OPTIONS AMERICA", font=font(22, True), fill="#b9c9da")
    draw.text((64, 605), "Short Iron Condor Learning Series", font=font(20), fill="#7892aa")
    draw.rounded_rectangle((720, 150, 1130, 505), 28, fill="#081c32", outline="#31506d", width=2)
    draw.line((760, 375, 1090, 375), fill="#6b8298", width=2)
    draw.line((925, 190, 925, 455), fill="#31506d", width=2)
    payoff = [(755, 445), (800, 445), (855, 270), (995, 270), (1050, 445), (1095, 445)]
    draw.line(payoff, fill=accent, width=8, joint="curve")
    if index == 1:
        for x, n in zip((800, 855, 995, 1050), ("LP", "SP", "SC", "LC")):
            draw.ellipse((x-7, 263, x+7, 277), fill="white")
            draw.text((x-10, 210), n, font=font(14, True), fill=accent)
    elif index == 2:
        draw.line((855, 200, 855, 450), fill="#ff8e72", width=3)
        draw.line((995, 200, 995, 450), fill="#ff8e72", width=3)
        draw.text((870, 220), "PROFIT RANGE", font=font(14, True), fill="white")
    elif index == 3:
        for x, ydot in ((780, 430), (835, 330), (925, 270), (1020, 350), (1080, 440)):
            draw.ellipse((x-7, ydot-7, x+7, ydot+7), fill="#52d3ff")
    elif index == 4:
        for x in (800, 855, 995, 1050): draw.line((x, 205, x, 450), fill="#31506d", width=2)
    elif index == 5:
        for x, label in ((770, "21D"), (875, "45D"), (990, "60D")):
            draw.rounded_rectangle((x, 195, x+65, 232), 10, outline=accent, width=2)
            draw.text((x+13, 205), label, font=font(13, True), fill="white")
    elif index == 6:
        for x, h, c in ((775, 75, "#52d3ff"), (845, 125, accent), (915, 95, "#80e0a7"), (985, 145, "#ff8e72")):
            draw.rounded_rectangle((x, 440-h, x+38, 440), 8, fill=c)
    elif index == 7:
        draw.line([(760, 440), (850, 285), (1000, 285), (1090, 440)], fill="#52d3ff", width=4)
    elif index == 8:
        draw.line([(760, 440), (925, 230), (1090, 440)], fill="#ff8e72", width=5)
    elif index == 9:
        for x, h, c in ((770, 80, "#52d3ff"), (830, 130, accent), (890, 60, "#80e0a7"), (950, 110, "#ff8e72")):
            draw.rounded_rectangle((x, 445-h, x+34, 445), 8, fill=c)
    elif index == 10:
        draw.arc((785, 205, 965, 385), 0, 300, fill="#52d3ff", width=5)
        draw.line((875, 295, 875, 237), fill="white", width=4)
        draw.line((875, 295, 920, 320), fill="white", width=4)
    elif index == 11:
        for box, c in (((755, 205, 880, 350), "#52d3ff"), ((855, 220, 1015, 370), "#80e0a7"), ((980, 250, 1090, 355), "#ff8e72")):
            draw.arc(box, 5, 175, fill=c, width=4)
    elif index == 12:
        draw.line((805, 205, 1000, 205), fill="#52d3ff", width=5)
        draw.polygon([(1000, 205), (975, 189), (975, 221)], fill="#52d3ff")
        draw.line((1020, 335, 835, 335), fill="#ff8e72", width=5)
        draw.polygon([(835, 335), (860, 319), (860, 351)], fill="#ff8e72")
    elif index == 13:
        draw.rounded_rectangle((765, 390, 1080, 430), 10, fill="#123a55")
        draw.rounded_rectangle((875, 390, 1010, 430), 10, fill=accent)
        draw.text((893, 400), "CLOSE ZONE", font=font(14, True), fill="#07172d")
    elif index == 14:
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
