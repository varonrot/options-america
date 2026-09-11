#!/usr/bin/env python3
"""Build the Level 8 All Greeks in Action SEO cluster."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("level6_builder", ROOT / "tools/build_level6_blog_cluster.py")
base = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(base)
BLOG = ROOT / "blog"
COURSE = "../../courses/option-greeks-level-8-option-greeks-in-action/"


def guide(slug, tag, title, description, key, sections, example, faq):
    return dict(slug=slug, tag=f"Greeks · {tag}", title=title, description=description,
                key=key, sections=sections, example=example, faq=faq)


ARTICLES = [
guide("option-greeks-explained", "Complete Guide", "Option Greeks Explained: Delta, Gamma, Theta, Vega and Rho",
"Learn what the five principal option Greeks measure and how they work together to describe a changing position.",
"The Greeks are theoretical sensitivities, not separate sources of profit or guarantees about the next market move.", [
("The five core Greeks", "Delta estimates sensitivity to the underlying price, gamma estimates how delta changes, theta estimates the effect of time passing, vega estimates sensitivity to implied volatility and rho estimates sensitivity to interest rates."),
("One position, several forces", "An option can gain from a favorable stock move while losing from time decay or falling volatility. Reading a single Greek in isolation can therefore produce the right observation but the wrong conclusion about total P&L."),
("Use scenarios, not labels", "Scale each Greek by contract quantity and multiplier, then model several combinations of price, time and volatility. Recalculate as conditions change because the Greeks themselves are dynamic."),
], "A long call has positive delta and vega, negative theta and positive gamma. A stock rally may help delta, but a volatility decline and several days of decay can reduce or reverse the gain.",
[("Are Greeks exact predictions?", "No. They are model estimates that isolate one input at a time."),("Which Greek matters most?", "It depends on the position, horizon and market change being considered."),("Do multi-leg trades have Greeks?", "Yes. Add the signed exposure of every leg to estimate net position Greeks.")]),

guide("how-option-greeks-interact", "Core Framework", "How Option Greeks Interact",
"Understand how price, time and volatility change several Greeks simultaneously and reshape an option position's risk.",
"Every market move changes the position and often changes the sensitivities used to describe the next move.", [
("Price changes more than delta", "When the underlying moves, delta estimates the first response and gamma changes the next delta. Moneyness also shifts theta and vega, so a directional move can alter the entire Greek profile."),
("Time changes the balance", "As expiration approaches, extrinsic value declines, vega commonly falls and gamma can become concentrated near the strike. The same strategy can therefore behave very differently with 90 days remaining and one day remaining."),
("Volatility reshapes probabilities", "An IV change affects premium through vega and can also move deltas toward or away from their endpoints. Scenario analysis should change several inputs together rather than simply adding static Greek estimates."),
], "A near-term ATM option enters the week with moderate delta, strong gamma, negative theta and positive vega. A rally plus IV decline changes both its value and the size of each exposure for the following day.",
[("Can Greek effects be added?", "For small changes they provide a useful approximation, but interactions and curvature limit simple addition."),("Why do Greeks change?", "They are derivatives of an option model evaluated at current inputs."),("What should be modeled together?", "At minimum price, time and implied volatility, plus rates or dividends when material.")]),

guide("what-is-rho-in-options", "Interest Rates", "What Is Rho in Options?",
"Learn how interest-rate changes can affect call and put premiums, especially for longer-dated options.",
"Rho estimates the theoretical premium change for a one-percentage-point change in interest rates, all else equal.", [
("Call and put rho", "Purchased calls normally have positive rho because higher rates can increase call values. Purchased puts normally have negative rho because higher rates can reduce put values under standard pricing assumptions."),
("Why time matters", "Interest-rate carrying effects accumulate over time, so long-dated options usually have greater absolute rho than near-term contracts. Higher-priced underlyings may also create larger rate sensitivity."),
("When to pay attention", "Rho may be small for short-dated equity options but can matter for LEAPS, large portfolios or meaningful rate shifts. Models and brokers may also use different rate inputs, so displayed values can vary."),
], "A long call has rho 0.32. If the relevant modeled rate rises from 3% to 4%, its theoretical premium may rise about $0.32 per share, assuming every other input is unchanged.",
[("Is rho positive for calls?", "A purchased call generally has positive rho; selling it reverses the position exposure."),("Why is put rho negative?", "Higher rates generally reduce the present value associated with the strike, lowering put value under standard assumptions."),("Does rho matter near expiration?", "It is usually smaller because little time remains for carrying costs to accumulate.")]),

guide("option-greeks-long-call", "Long Calls", "Option Greeks for a Long Call",
"See how delta, gamma, theta, vega and rho combine in a purchased call from entry through expiration.",
"A long call usually has positive delta, gamma, vega and rho with negative theta, but magnitudes change continuously.", [
("Directional profile", "Positive delta means a rally generally helps the call. Positive gamma makes delta rise during a rally and fall during a decline, creating convexity that can benefit a sufficiently large favorable move."),
("Time and volatility", "Negative theta represents the cost of waiting, while positive vega means an IV increase can support premium. A correct bullish view may still lose if the move is too slow or implied volatility falls sharply."),
("Expiration path", "As the call becomes deep ITM, delta can approach 1 and gamma may fall. If it remains OTM near expiration, delta and premium can approach zero while the remaining time value disappears."),
], "A call starts with delta 0.45, gamma 0.06, theta -0.05 and vega 0.14. A fast rally plus higher IV can help several exposures, while a quiet week creates a theta loss.",
[("What is the maximum loss?", "For a standard purchased call, it is generally the premium paid plus transaction costs."),("Can positive delta guarantee a gain?", "No. Theta, vega and the amount of the stock move also matter."),("Why does call delta rise?", "Positive gamma increases call delta as the underlying rises.")]),

guide("option-greeks-long-put", "Long Puts", "Option Greeks for a Long Put",
"Understand the combined directional, convexity, time and volatility exposure of a purchased put.",
"A long put normally has negative delta, positive gamma and vega, negative theta and negative rho.", [
("Downside exposure", "Negative delta means the put generally gains as the underlying falls. Positive gamma makes delta more negative during a decline, increasing downside sensitivity as the favorable move continues."),
("Insurance costs", "Negative theta erodes time value when the expected decline does not arrive. Positive vega can help when fear and implied volatility rise, but IV can also fall even when the stock moves down."),
("Changing moneyness", "A deep ITM put can approach -1 delta and behave more like short stock. A far OTM put nearing expiration can approach zero delta and lose its remaining premium rapidly."),
], "A protective put begins at -0.30 delta with positive vega. A sharp selloff may make delta more negative and raise IV, but a stable market may produce losses from theta and lower volatility.",
[("Is a long put bearish?", "Its negative delta creates bearish exposure, though it may be used as insurance on long stock."),("Can a put lose when stock falls?", "Yes, if the move is too small relative to premium, time decay and volatility changes."),("Why is put gamma positive?", "Long options have positive gamma even though put delta itself is negative.")]),

guide("option-greeks-credit-spreads", "Credit Spreads", "Option Greeks for Credit Spreads",
"Analyze the net delta, gamma, theta and vega of bull put and bear call spreads instead of focusing only on premium collected.",
"Credit spreads often begin with positive theta and negative vega and gamma, but strike placement and price determine the actual profile.", [
("Directional exposure", "A bull put spread normally has positive delta; a bear call spread normally has negative delta. The long wing defines maximum expiration loss and offsets part of the short option's Greek exposure."),
("The seller tradeoff", "Positive theta may reward time passing and negative vega may benefit from lower IV. Negative gamma means an adverse move can accelerate losses and change delta faster than a static payoff snapshot suggests."),
("Near expiration", "When price stays safely away from the short strike, all Greeks tend toward zero. Near the strike, gamma and assignment risk can become concentrated, making the final days operationally demanding."),
], "A bull put spread starts with +18 delta, positive theta and negative vega. A selloff toward the short strike raises directional exposure and can combine negative gamma with an IV expansion.",
[("Do all credit spreads have positive theta?", "They often do at entry, but net theta can change with price and time."),("Is risk always defined?", "A standard vertical credit spread defines expiration risk when constructed and managed correctly."),("Can falling IV guarantee profit?", "No. An adverse price move can overwhelm the vega benefit.")]),

guide("option-greeks-debit-spreads", "Debit Spreads", "Option Greeks for Debit Spreads",
"Learn how vertical debit spreads reshape the Greeks of a long option by selling another strike against it.",
"A debit spread reduces premium and often reduces theta, vega and gamma exposure while capping potential profit.", [
("Bull and bear direction", "A bull call spread normally has positive delta, while a bear put spread normally has negative delta. The short option offsets part of the directional exposure of the purchased leg."),
("Reduced Greek exposure", "Compared with a single long option, the spread commonly has smaller negative theta and positive vega. Its gamma is also reduced because the two legs have opposing gamma signs at the position level."),
("Changing behavior", "As the underlying moves through the strikes, the legs' deltas and other Greeks change at different speeds. Near maximum value, net delta and remaining time exposure can shrink materially."),
], "A bull call spread begins at +28 delta with modest negative theta and positive vega. A rally toward the short strike helps, but further upside eventually produces less delta as profit becomes capped.",
[("Why sell the higher strike?", "It reduces entry cost and some decay and volatility exposure in exchange for capped upside."),("Can a debit spread have positive theta?", "It can in some price regions and near expiration, so current net Greeks should be checked."),("Is vega always positive?", "Often at entry, but it can change as moneyness and time evolve.")]),

guide("option-greeks-straddles-strangles", "Volatility Strategies", "Option Greeks for Straddles and Strangles",
"Compare the Greek profile of long and short volatility positions that use both a call and a put.",
"Long straddles and strangles generally own gamma and vega while paying theta; short versions reverse that tradeoff.", [
("Long volatility", "A long straddle may begin near zero delta but has positive gamma, positive vega and negative theta. A sufficiently large move or IV increase can help, while a quiet market erodes premium."),
("Short volatility", "A short straddle generally has negative gamma, negative vega and positive theta. Its initial neutral delta can become strongly directional after a move, and losses can be substantial or unlimited on the call side."),
("Strangle differences", "A strangle uses different OTM strikes and usually costs or collects less premium. It may require a larger move, and each leg's delta changes as the underlying approaches its strike."),
], "A long ATM straddle begins near zero delta. After a strong rally, call delta rises and put delta fades, leaving the position positively directional while gamma and vega also change.",
[("Does zero delta mean no price risk?", "No. Gamma can create directional exposure quickly after a move."),("Why do long straddles lose in quiet markets?", "Both options carry negative theta and may also lose from falling IV."),("Are short strangles defined risk?", "Uncovered short strangles generally carry substantial downside and theoretically unlimited upside risk.")]),

guide("option-greeks-iron-condor", "Iron Condors", "Option Greeks for an Iron Condor",
"Understand the changing delta, gamma, theta and vega of an iron condor as price approaches either short strike.",
"An iron condor often starts near delta neutral with positive theta and negative vega and gamma, but neutrality disappears after movement.", [
("At entry", "A balanced condor around the current price may have modest net delta. Time decay can help if the underlying remains within the range, and defined wings cap expiration losses."),
("Approaching a side", "A move toward the call spread makes the condor increasingly negative delta; a move toward the put spread makes it increasingly positive delta. Negative gamma accelerates this adverse change."),
("Volatility and time", "An IV rise often hurts through negative vega, while theta may help. Near expiration, the position can show attractive decay but sharp gamma around a short strike, requiring careful sizing and exit planning."),
], "A condor starts near zero delta. After a rally toward the short call, it becomes negative delta and loses from negative gamma; if IV also rises, negative vega can add pressure.",
[("Is an iron condor always neutral?", "It may start near neutral but becomes directional as price moves."),("Does positive theta mean daily profit?", "No. Price and volatility changes can outweigh decay."),("Are losses defined?", "Standard iron condors have defined expiration risk, subject to execution and assignment considerations.")]),

guide("option-greeks-calendar-spreads", "Calendar Spreads", "Option Greeks for Calendar Spreads",
"Learn how different expirations create a calendar spread's distinctive theta, vega and gamma profile.",
"A long calendar commonly has positive vega and may have positive theta near its strike, but term structure and price movement matter.", [
("Two different clocks", "A long calendar sells a near-term option and buys a longer-term option at the same strike. The front leg usually decays faster, while the back leg commonly carries greater vega."),
("Price location", "The favorable theta profile is often concentrated near the strike. A large move away can reduce the value of the remaining time-spread relationship and change net delta and gamma."),
("Volatility term structure", "The two expirations do not necessarily experience the same IV change. Earnings and other events can concentrate volatility in one maturity, so a parallel-vega estimate may miss the main risk."),
], "A calendar appears positive vega because the back month has more vega. If front-month event IV rises while the back month barely moves, the actual result can differ from a parallel-shift estimate.",
[("Are calendars always positive theta?", "Not everywhere; price relative to the strike and time can change the sign."),("Why is vega usually positive?", "The longer-dated purchased leg often has greater vega than the near-term short leg."),("What happens at front expiration?", "Exercise, assignment and the remaining back option must be managed deliberately.")]),

guide("option-greeks-around-earnings", "Earnings", "Option Greeks Around Earnings",
"Combine delta, gamma, theta and vega when evaluating an options position before and after an earnings announcement.",
"An earnings trade is a joint exposure to gap direction, move magnitude, volatility crush and time—not a direction-only trade.", [
("Before the release", "Near-term IV often rises, lifting premiums through vega. Delta and gamma describe directional and curvature exposure, while theta reflects the high cost of carrying event premium."),
("The overnight gap", "A large move can create substantial delta and gamma P&L before a hedge is possible. The opening option price also reflects the new volatility level and liquidity, so Greek estimates from the previous close are only a starting point."),
("After the event", "IV commonly falls as uncertainty resolves. Long-vega positions may suffer a crush; short-vega positions may benefit but can lose more from a gap. Model price and IV changes together before entry."),
], "A long call correctly predicts an earnings rally, but the stock moves less than options had priced and IV collapses. Delta helps, while vega and theta can leave the trade unprofitable.",
[("Which Greek matters most at earnings?", "Delta, gamma and vega can all be material because price and IV may change abruptly."),("Does IV always crush?", "It commonly falls after uncertainty resolves, but the size is not guaranteed."),("Can spreads reduce vega?", "Yes, though they add caps, multiple legs and other risks.")]),

guide("portfolio-option-greeks-risk", "Portfolio Risk", "How to Measure Portfolio Option Greeks",
"Aggregate Greeks across stocks and option positions while accounting for contract sizes, different underlyings and changing correlations.",
"Portfolio Greeks are useful summaries only when units, multipliers, underlyings and scenario assumptions are kept consistent.", [
("Scale each position", "Multiply per-share Greeks by signed quantity and the correct contract multiplier. Add stock delta where relevant. Check adjusted, index and futures-option specifications rather than assuming every multiplier is 100."),
("Normalize different assets", "Raw delta across unrelated stocks can mislead. Dollar delta or beta weighting can create a common benchmark, while vega may need normalization by volatility points and maturity."),
("Stress the portfolio", "Net zero exposure can hide offsetting concentrations that break during gaps or correlation changes. Test individual positions, sectors, expirations and broad shocks rather than relying on one total."),
], "A portfolio shows near-zero total delta because technology calls offset index puts. A sector-specific rally or correlation break can create losses even though the opening aggregate looked neutral.",
[("Can Greeks across stocks be added?", "They can be aggregated after appropriate scaling, but interpretation across underlyings requires care."),("What is net vega?", "It is the signed first-order sensitivity to an assumed IV-point change across positions."),("Does zero net Greek remove risk?", "No. Offsetting exposures, curvature, basis and gap risks remain.")]),

guide("option-greeks-scenario-analysis", "Planning", "Option Greeks Scenario Analysis",
"Build practical price, time and volatility scenarios that go beyond multiplying today's Greek values by one market change.",
"Greeks approximate local changes; full repricing across combined scenarios better reflects nonlinear option behavior.", [
("Choose meaningful shocks", "Model several underlying prices, dates and IV levels tied to the actual thesis. Include a base case, favorable case and adverse case rather than testing only the expected outcome."),
("Separate and combine", "First change one input to understand delta, theta or vega. Then combine realistic changes, such as a stock decline with higher IV and fewer days remaining, to see interaction effects."),
("Reprice and review", "Large moves require a pricing model or broker analyzer because delta and other Greeks change during the scenario. Include bid-ask spreads, commissions, assignment and position limits in the final decision."),
], "A trader tests a spread after a 5% rally, a 5-point IV decline and seven days of decay. The combined modeled result differs from summing today's static delta, vega and theta estimates.",
[("How many scenarios are enough?", "Use enough to cover plausible favorable, neutral and adverse paths, including tail events."),("Can Greeks replace a pricing model?", "They are helpful for small local moves; full repricing is better for large combined changes."),("Should liquidity be modeled?", "Yes. Slippage can materially alter theoretical outcomes.")]),

guide("option-greeks-pnl-explained", "Profit & Loss", "How Option Greeks Affect Profit and Loss",
"Connect daily option P&L with delta, gamma, theta, vega and rho while recognizing unexplained model and execution effects.",
"Greek attribution decomposes estimated P&L; it does not force live prices to match a perfect accounting identity.", [
("Directional contribution", "Delta estimates the linear price effect and gamma estimates curvature. For a larger move, using the starting delta alone can understate a long-gamma gain or understate a short-gamma loss."),
("Time and volatility contribution", "Theta approximates decay and vega approximates IV repricing. These can offset or reinforce direction, especially around events when volatility changes quickly."),
("The residual", "Rates, dividends, higher-order Greeks, changing inputs, model choice, spreads and discrete market repricing can create differences between estimated and actual P&L. Treat attribution as diagnosis, not certainty."),
], "An option gains $120 from estimated delta and gamma, loses $35 from theta and loses $50 from lower IV. The rough attributed gain is $35 before residual effects and costs.",
[("Why does actual P&L differ?", "Greeks change, markets are discrete and models cannot capture every execution and pricing effect."),("Can theta be seen as a cash charge?", "No. It is a theoretical sensitivity to time passing."),("Does gamma contribute without a move?", "Gamma describes curvature from price movement; without movement its direct contribution is limited.")]),

guide("option-greeks-mistakes", "Risk Management", "Option Greeks: 12 Mistakes to Avoid",
"Avoid common errors involving static Greeks, contract scaling, probability shortcuts, events, hedging and multi-leg positions.",
"The largest Greek mistake is treating a changing model dashboard as a set of independent guarantees.", [
("Mistakes 1–4: units and signs", "Do not forget the contract multiplier, ignore short-position signs, confuse volatility points with percent changes or mix per-share and position-level values. Verify platform conventions before calculating."),
("Mistakes 5–8: isolated readings", "Do not treat delta as exact probability, theta as guaranteed income, vega as a direction forecast or rho as universally irrelevant. Every number needs market and strategy context."),
("Mistakes 9–12: dynamic risk", "Do not keep hedges static, ignore gamma near expiration, assume all IVs move together or call a zero-net-Greek portfolio risk-free. Stress several paths and recalculate after meaningful change."),
], "A trader sells an apparently neutral, positive-theta position before an event. A gap changes delta through negative gamma while IV rises, showing why one attractive Greek cannot define total risk.",
[("Which Greek is most often misunderstood?", "Delta's probability shortcut and theta's income interpretation are both frequently overstated."),("How often should Greeks be updated?", "Whenever price, volatility, time or position structure changes materially."),("Are zero Greeks possible?", "A sensitivity can be near zero at one moment, but other exposures and future drift remain.")]),
]


base.ARTICLES = ARTICLES
base.COURSE = COURSE


def article_html(article: dict, index: int) -> str:
    return (base.article_html(article, index)
            .replace("Learn Vega — Free", "Learn the Greeks — Free")
            .replace("Vega &amp; Volatility", "All Greeks in Action")
            .replace("Vega planning example", "Greeks planning example")
            .replace("This simplified example holds other inputs constant to isolate volatility exposure.", "This simplified example isolates selected sensitivities so their interaction is easier to understand.")
            .replace("Continue the Vega &amp; Volatility cluster", "Continue the All Greeks in Action cluster")
            .replace("Level 6 – Vega &amp; Volatility course", "Level 8 – All Greeks in Action course")
            .replace("Level 6 – All Greeks in Action course", "Level 8 – All Greeks in Action course")
            .replace("Start Level 6 — Free", "Start Level 8 — Free")
            .replace("Free Level 6 Course", "Free Level 8 Course")
            .replace("Learn vega and volatility through structured lessons and practical examples.", "Learn how Delta, Gamma, Theta, Vega and Rho work together in real positions."))


def card_html(article: dict) -> str:
    return base.card_html(article)


def update_index() -> None:
    path = BLOG / "index.html"
    source = path.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    if 'href="option-greeks-explained/"' not in source:
        source = source.replace(marker, "\n".join(card_html(a) for a in ARTICLES) + "\n" + marker, 1)
    source = source.replace("<strong>105</strong> guides", "<strong>120</strong> guides")
    if "Explore Level 8" not in source:
        source = source.replace('<a class="btn btn-gold" href="../courses/option-greeks-level-7-delta-effect-strategy/">Explore Level 7 →</a>', '<a class="btn btn-gold" href="../courses/option-greeks-level-7-delta-effect-strategy/">Explore Level 7 →</a><a class="btn btn-gold" href="../courses/option-greeks-level-8-option-greeks-in-action/">Explore Level 8 →</a>')
    path.write_text(source)


def update_scripts() -> None:
    path = BLOG / "blog.js"
    source = path.read_text().replace("const clusterPriority = card => card.textContent.includes('Delta') ? 7 :", "const clusterPriority = card => card.textContent.includes('Greeks') ? 8 : card.textContent.includes('Delta') ? 7 :")
    path.write_text(source)
    path = ROOT / "favicon.js"
    source = path.read_text()
    marker = "    'delta-gamma-mistakes': '/assets/images/blog/delta-gamma-mistakes.webp'"
    additions = ",\n".join(f"    '{a['slug']}': '/assets/images/blog/{a['slug']}.webp'" for a in ARTICLES)
    if "'option-greeks-explained'" not in source:
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
