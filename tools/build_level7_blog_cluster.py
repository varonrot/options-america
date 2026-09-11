#!/usr/bin/env python3
"""Build the Level 7 Delta Effect SEO cluster."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("level6_builder", ROOT / "tools/build_level6_blog_cluster.py")
base = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(base)

BLOG = ROOT / "blog"
COURSE = "../../courses/option-greeks-level-7-delta-effect-strategy/"


def guide(slug, tag, title, description, key, sections, example, faq):
    return dict(slug=slug, tag=f"Delta · {tag}", title=title, description=description,
                key=key, sections=sections, example=example, faq=faq)


ARTICLES = [
guide("what-is-delta-in-options", "Beginner", "What Is Delta in Options?",
"Learn what option delta measures, how it connects stock movement to option premium and why the number changes throughout a trade.",
"Delta estimates the change in an option's theoretical value for a $1 move in the underlying, assuming other pricing inputs remain unchanged.", [
("Delta in plain English", "A call with delta 0.50 may gain about $0.50 per share if the stock rises $1, all else equal. For a standard 100-share contract, that is roughly $50. The same call may lose about $0.50 if the stock falls $1."),
("The sign of delta", "Long calls normally have positive delta and long puts have negative delta. Selling reverses the position sign: a short call has negative delta and a short put has positive delta. Multi-leg positions combine every signed exposure."),
("Why delta changes", "Moneyness, time and implied volatility all affect delta. Gamma estimates how quickly delta changes as the underlying moves, so today's delta should be treated as a snapshot rather than a fixed hedge ratio."),
], "A stock trades at $80 and its call has delta 0.45. A rise to $82 implies an initial option gain near $0.90 per share. Because gamma changes delta during the move, a full repricing may produce a different result.",
[("Is delta guaranteed?", "No. It is a model estimate that holds other inputs constant."),("Can delta exceed 1?", "A single standard option's model delta generally remains between 0 and 1 for calls and 0 and -1 for puts."),("Does stock have delta?", "Long stock has delta +1 per share and short stock has delta -1 per share.")]),

guide("call-delta-vs-put-delta", "Calls & Puts", "Call Delta vs Put Delta",
"Compare the direction and range of call and put delta, including how long and short positions reverse the exposure.",
"Calls and puts respond in opposite directions to the same underlying move, but the position quantity determines the final sign.", [
("Call delta", "A long call has positive delta because its value generally rises with the underlying. An out-of-the-money call may have a delta near zero, an at-the-money call is often near 0.50 and a deep in-the-money call can approach 1.00."),
("Put delta", "A long put has negative delta because its value generally rises as the underlying falls. Its delta can range from near zero for far OTM contracts toward -1.00 for deep ITM contracts."),
("Short positions", "Selling an option reverses its exposure. A short call is negative delta and a short put is positive delta. Always multiply the quoted contract delta by the signed position quantity before judging direction."),
], "One long 0.55-delta call contributes about +55 share equivalents. One long -0.35-delta put contributes about -35. Together the simplified net exposure is approximately +20 deltas.",
[("Why is put delta negative?", "Put value generally moves opposite to the underlying price."),("Is a short put bullish?", "Its positive delta creates bullish directional exposure, though the payoff and risks differ from stock."),("Do call and put deltas add to one?", "Under standard assumptions, same-strike call and put deltas have a close relationship, but dividends and conventions matter.")]),

guide("positive-delta-vs-negative-delta", "Direction", "Positive Delta vs Negative Delta",
"Understand bullish and bearish portfolio exposure through delta without confusing direction with maximum risk or probability of profit.",
"Positive delta tends to benefit from a rise in the underlying; negative delta tends to benefit from a decline, but payoff shape still matters.", [
("Positive delta", "Long stock, long calls and short puts commonly contribute positive delta. A +30 position delta suggests an initial price sensitivity similar to 30 long shares, not an identical payoff across large moves."),
("Negative delta", "Short stock, long puts and short calls commonly contribute negative delta. A -30 position may initially react like 30 short shares, while gamma, theta and vega make the option payoff evolve differently."),
("Direction is not total risk", "Two positions can share the same delta and have very different maximum losses, assignment exposure and curvature. Compare the payoff diagram and all Greeks before using delta as a position label."),
], "A covered call may remain positive delta because the +100 stock delta is partly offset by a short call. If the call contributes -40, the combined position begins near +60 deltas.",
[("Is positive delta always bullish?", "It indicates positive near-term price sensitivity, but other Greeks and payoff limits still matter."),("Can delta change sign?", "Yes, especially in multi-leg positions as price and time change."),("Does zero delta mean no risk?", "No. Gamma, vega, theta, gaps and nonlinear moves remain.")]),

guide("option-delta-itm-atm-otm", "Moneyness", "Option Delta for ITM, ATM and OTM Contracts",
"See how delta behaves across in-the-money, at-the-money and out-of-the-money options and as expiration approaches.",
"Delta typically moves toward its expiration endpoints as an option becomes more clearly in or out of the money.", [
("At the money", "ATM calls are often near +0.50 and ATM puts near -0.50, though rates, dividends and contract details can shift the values. Uncertainty around the strike also tends to create meaningful gamma."),
("In the money", "As a call moves deeper ITM, delta generally approaches +1. A deep ITM put can approach -1. These options respond more like the underlying because intrinsic value dominates their premium."),
("Out of the money", "Far OTM deltas approach zero as the modeled chance of finishing with intrinsic value declines. A small delta does not prevent a large percentage gain or total premium loss."),
], "With a stock at $100, a $90 call may have high delta, the $100 call may sit near 0.50 and a $115 call may have low delta. One price jump can move all three values and their deltas.",
[("Which option has the highest delta?", "A deep ITM call is closest to +1, while a deep ITM put is closest to -1."),("Why is ATM delta near 0.50?", "The strike is near the boundary between expiring in and out of the money under common assumptions."),("Does delta become 0 or 1 at expiration?", "For calls it converges toward 0 or 1 depending on moneyness; puts converge toward 0 or -1.")]),

guide("calculate-option-delta", "Calculation", "How to Calculate Option Delta Exposure",
"Convert quoted delta into contract and portfolio dollar sensitivity using position signs, quantities and contract multipliers.",
"Position delta equals quoted delta multiplied by the contract multiplier and signed number of contracts.", [
("One contract", "A standard equity option represents 100 shares. One long call with delta 0.42 therefore contributes about +42 share equivalents. One long put with delta -0.42 contributes about -42."),
("Multiple contracts", "Multiply by quantity and preserve the sign. Three long 0.30-delta calls contribute +90; two short 0.25-delta calls contribute -50. Contract specifications should always be checked before assuming a multiplier of 100."),
("Portfolio total", "Add options and stock deltas to estimate the initial response to a small underlying move. Recalculate after price, time or volatility changes because gamma makes the hedge ratio drift."),
], "A portfolio owns 100 shares, two long puts with delta -0.30 and one short call with contract delta 0.25. Net delta is 100 - 60 - 25 = approximately +15.",
[("Why multiply by 100?", "Standard U.S. equity options usually represent 100 shares, but adjusted and other contracts can differ."),("What does +50 delta mean?", "The position initially behaves approximately like 50 long shares for a small move."),("Can I use current delta for a large move?", "Only as a rough starting point because delta changes during the move.")]),

guide("delta-probability-in-the-money", "Probability", "Can Delta Estimate Probability In the Money?",
"Learn why traders use delta as a rough probability proxy—and why it is not the same as an exact expiration forecast.",
"Delta can be a useful shorthand for modeled probability, but delta and probability in the money are distinct model outputs with limitations.", [
("The common shortcut", "A 0.30-delta call is often described as having roughly a 30% modeled chance of expiring ITM. This interpretation helps compare strikes quickly, but it depends on pricing assumptions and is not a guarantee."),
("Why it is imperfect", "Delta measures price sensitivity, while probability ITM asks a binary expiration question. Rates, dividends, volatility assumptions and the difference between risk-neutral and real-world probabilities can make the values diverge."),
("Use the right metric", "Use a dedicated probability calculator when probability is the actual decision input. Pair any estimate with breakeven probability, expected payoff, premium, liquidity and maximum loss."),
], "A far-OTM call has delta 0.12. Calling that a 12% chance is a practical approximation, not evidence that exactly 12 of 100 similar trades will finish ITM.",
[("Does 0.50 delta mean a 50% win rate?", "No. Finishing ITM is not the same as finishing profitable after premium and costs."),("Is delta a real-world probability?", "It is derived from option-pricing assumptions, not a complete forecast of actual outcomes."),("Can probability change quickly?", "Yes. Price, time and volatility continuously change model estimates.")]),

guide("delta-as-share-equivalent", "Position Sizing", "Delta as Share Equivalent",
"Use position delta to compare option exposure with shares while respecting the nonlinear payoff of options.",
"Share-equivalent delta describes current first-order exposure, not permanent ownership or identical risk.", [
("The basic translation", "One long 0.60-delta call on a standard contract is approximately +60 share equivalents. A $1 stock rise suggests about a $60 initial option gain, all else equal."),
("Where the comparison helps", "Share equivalents make it easier to aggregate stock, calls and puts, compare candidate positions and estimate the size of a hedge. They also support portfolio-level scenario planning."),
("Where it breaks down", "Stock delta remains constant, but option delta changes because of gamma. Options also have expiration, volatility sensitivity and limited or asymmetric payoffs, so equal starting deltas do not create equal long-term outcomes."),
], "A trader replaces 100 shares with two 0.50-delta calls. Both begin near +100 delta, yet the calls can lose time value and their combined delta may rise or fall sharply as the stock moves.",
[("Is a 0.70-delta call equal to 70 shares?", "Only as an approximate current sensitivity to a small move."),("Does leverage change delta?", "Delta captures sensitivity, while premium and capital determine leverage and return percentages."),("How often should equivalents be updated?", "Whenever the underlying, time or volatility changes materially.")]),

guide("what-is-gamma-options", "Gamma", "What Is Gamma in Options?",
"Learn how gamma measures the change in delta, why long options have positive gamma and where gamma risk becomes concentrated.",
"Gamma estimates how much an option's delta changes for a $1 move in the underlying, assuming other inputs stay constant.", [
("Gamma as acceleration", "If a call has delta 0.50 and gamma 0.06, a $1 stock rise suggests a new delta near 0.56. A $1 decline suggests delta near 0.44. This is a local approximation because gamma also changes."),
("Long versus short gamma", "Long calls and puts normally have positive gamma, allowing their directional exposure to improve with a favorable move. Short options have negative gamma, so their delta can become more adverse as the market moves against them."),
("Where gamma is highest", "Gamma is commonly greatest near the money and close to expiration. Deep ITM and far OTM options usually have lower gamma because their deltas sit closer to endpoints."),
], "A long put has delta -0.45 and gamma 0.08. If the stock falls $1, its delta may become more negative, near -0.53, increasing downside sensitivity as the favorable move continues.",
[("Is gamma positive for puts?", "Long puts and long calls normally have positive gamma; the delta direction differs."),("Does stock have gamma?", "No. Stock delta remains +1 or -1 per share."),("Can gamma predict exact new delta?", "It is a first approximation for a small move, not a fixed value across large changes.")]),

guide("delta-vs-gamma-options", "Greek Relationship", "Delta vs Gamma in Options",
"Separate current directional sensitivity from the rate at which that sensitivity changes as the underlying moves.",
"Delta is the position's current speed; gamma is the acceleration that changes that speed.", [
("What delta answers", "Delta estimates how option value responds to the next small underlying move. It helps describe direction, size hedges and convert options into share-equivalent exposure."),
("What gamma answers", "Gamma estimates how delta itself changes. High gamma means the current hedge ratio can become stale quickly, especially when the stock trades near a strike close to expiration."),
("Read them together", "A low-delta option can become high delta after a large favorable move if it has positive gamma. A short option can develop increasingly adverse delta because negative gamma works against the position."),
], "A call begins with delta 0.40 and gamma 0.07. After a $1 rise, delta is roughly 0.47; after another $1, simply adding gamma again is only approximate because gamma has changed too.",
[("Which Greek affects price first?", "Delta describes the first-order price response; gamma refines how that response changes."),("Is high gamma good?", "It supports convexity for long options but creates instability and risk for short options."),("Can delta be stable with high gamma?", "Only briefly; a meaningful underlying move changes it quickly.")]),

guide("gamma-near-expiration", "Expiration Risk", "Gamma Risk Near Option Expiration",
"Understand why near-expiration options can switch directional exposure rapidly around the strike and how that affects buyers and sellers.",
"Near expiration, at-the-money gamma can become highly concentrated because delta must converge toward an expiration endpoint.", [
("The narrowing decision", "With little time remaining, a small move can decide whether an option finishes ITM or OTM. Delta can therefore move quickly toward 1 or 0 for calls and -1 or 0 for puts."),
("Long and short experience", "Long-gamma buyers may gain convexity from a sharp move but pay rapid theta. Short-gamma sellers may collect decay but face delta that becomes increasingly unfavorable during a large move."),
("Operational risk", "Pin risk, exercise, assignment, settlement and thin late-session liquidity add complications. Size for a sudden move and understand broker procedures before holding positions into expiration."),
], "A same-day call trades near its strike with delta 0.50. A small late rally can push delta rapidly higher, while a reversal can drive it toward zero, changing the hedge need within minutes.",
[("Is gamma always highest on expiration day?", "ATM gamma can be extreme near expiration, while ITM and OTM contracts may have much less."),("Does high gamma guarantee profit?", "No. Direction, premium, theta and execution still matter."),("What is pin risk?", "It is uncertainty around exercise and assignment when the underlying closes near a strike.")]),

guide("delta-hedging-options", "Hedging", "How Delta Hedging Works in Options",
"Learn how shares or options can offset directional exposure, why hedges drift and what risks remain after reaching zero delta.",
"Delta hedging offsets current directional sensitivity; gamma ensures that the hedge changes as the underlying moves.", [
("Create the initial hedge", "A long option position with +60 share-equivalent delta can be offset initially by shorting about 60 shares. A negative-delta position can be offset with positive shares or other positive-delta instruments."),
("Rebalancing", "When the underlying moves, option delta changes. A delta hedge therefore requires monitoring and possible rebalancing. Frequent adjustments can reduce directional exposure but increase costs and execution risk."),
("What remains", "A delta-neutral portfolio can still have gamma, theta, vega, gap and liquidity risk. Hedging is a risk transformation rather than a guarantee, and overnight jumps may occur before a hedge can be adjusted."),
], "A trader owns calls with +75 total delta and shorts 75 shares. After a rally, positive gamma lifts option delta to +92, so the portfolio is now +17 delta before rebalancing.",
[("Does delta hedging lock in profit?", "No. Other Greeks, gaps and trading costs remain."),("How often is a hedge adjusted?", "It depends on risk limits, gamma, market movement and costs."),("Can another option hedge delta?", "Yes, though it also adds its own gamma, theta and vega.")]),

guide("portfolio-delta-beta-weighting", "Portfolio", "Portfolio Delta and Beta Weighting",
"Aggregate directional exposure across positions and understand how beta weighting creates an approximate common market benchmark.",
"Raw deltas across different underlyings cannot be added meaningfully without considering price, volatility and their relationship to a common benchmark.", [
("Position delta first", "Calculate each holding's signed share-equivalent delta. For dollar delta, multiply by the underlying price, which better reflects the money sensitivity of differently priced stocks."),
("Why beta weight", "Beta weighting translates positions into approximate sensitivity to a chosen index or ETF using historical relationships. It can reveal whether a diversified-looking portfolio still carries concentrated market direction."),
("Limitations", "Beta changes across regimes and can behave poorly during stress. Nonlinear options, volatility shifts and company events add risks that a single weighted delta cannot describe."),
], "Two positions each have +50 share delta, but one stock trades at $20 and another at $300. Their raw counts match, while dollar exposure and benchmark sensitivity differ substantially.",
[("What is dollar delta?", "It is commonly position delta multiplied by the underlying price."),("Is beta weighting exact?", "No. It relies on estimated historical relationships that can change."),("Which benchmark should be used?", "Choose one relevant to the portfolio and understand the basis of comparison.")]),

guide("delta-neutral-option-strategies", "Strategies", "Delta-Neutral Option Strategies",
"Explore how traders construct near-zero delta positions and why neutrality is temporary rather than risk-free.",
"A delta-neutral position minimizes current first-order direction but can intentionally retain gamma, volatility or time exposure.", [
("Ways to build neutral", "Traders can combine calls, puts and shares so positive and negative deltas offset. Straddles may begin near neutral, while stock can fine-tune the residual exposure of an option structure."),
("The intended exposure", "A long straddle may seek positive gamma and vega while paying theta. A short straddle may seek theta and lower realized movement while carrying negative gamma and potentially large loss."),
("Neutrality drifts", "Price movement, time and volatility change the legs unequally. Rebalancing restores delta neutrality only at that moment and may realize gains or losses while adding transaction costs."),
], "A long call contributes +52 delta and a long put -47, leaving +5. Shorting five shares makes the position approximately delta neutral, but the hedge changes after the next stock move.",
[("Is a straddle always delta neutral?", "It may start near neutral when strikes and quantities align, but the delta changes."),("Can delta-neutral trades lose?", "Yes. Theta, vega, gamma path, gaps and costs remain."),("Why rebalance?", "To bring drifting directional exposure back toward the chosen target.")]),

guide("delta-option-chain", "Option Chain", "How to Read Delta in an Option Chain",
"Use delta columns to compare strikes, expirations and directional exposure without overlooking spreads, liquidity and changing inputs.",
"Delta is most useful when contracts are compared on the same underlying with consistent prices, timestamps and assumptions.", [
("Find the quote", "Most analytic option chains place delta beside gamma, theta and vega for each call and put. Confirm whether figures are per share or position-level and whether the platform displays long-contract or signed position values."),
("Compare strikes and dates", "Higher-delta calls are generally deeper ITM; more negative puts are deeper ITM. Time and IV can change the pattern, so compare several expirations instead of choosing a contract from delta alone."),
("Check the market", "A precise Greek is not useful if the bid-ask spread is wide or the quote is stale. Review bid, ask, volume, open interest and the underlying price timestamp before calculating exposure."),
], "An option chain shows calls with deltas 0.75, 0.51 and 0.22 across three strikes. The figures summarize different current sensitivities, not guaranteed gains or exact probabilities.",
[("Is broker delta live?", "It updates with market inputs, but refresh rates and models vary."),("Why can two platforms disagree?", "They may use different volatility, rates, dividends, models or timestamps."),("Should I choose a strike by delta?", "Delta can support selection, but cost, liquidity, payoff and risk must also fit.")]),

guide("delta-gamma-mistakes", "Risk Management", "Delta and Gamma: 10 Mistakes to Avoid",
"Avoid common errors involving signs, multipliers, probability shortcuts, static hedges and expiration gamma.",
"Delta and gamma are changing sensitivities, not fixed forecasts or complete measures of option risk.", [
("Mistakes 1–3: reading delta", "Do not forget the position sign, ignore the contract multiplier or treat delta as an exact price forecast. The quote is per share under stated model assumptions and must be scaled correctly."),
("Mistakes 4–6: probability and sizing", "Do not equate delta with guaranteed win rate, assume equal delta means equal risk or use share equivalents as a permanent stock substitute. Options remain nonlinear and time-limited."),
("Mistakes 7–10: changing exposure", "Do not ignore gamma, leave hedges static, sell high-gamma expiration risk without stress tests or call zero delta risk-free. Reprice after meaningful changes and inspect every Greek."),
], "A trader sells several ATM weekly options, hedges delta once and stops monitoring. A fast move changes delta through negative gamma, creating a much larger directional position than the opening hedge suggested.",
[("What is the biggest delta mistake?", "Treating a current sensitivity as a fixed prediction."),("Why does gamma matter to a hedge?", "It determines how quickly delta and the required hedge can change."),("How often should Greeks be reviewed?", "Whenever price, time, volatility or position structure changes materially.")]),
]


base.ARTICLES = ARTICLES
base.COURSE = COURSE


def article_html(article: dict, index: int) -> str:
    return (base.article_html(article, index)
            .replace("Learn Vega — Free", "Learn Delta — Free")
            .replace("Vega &amp; Volatility", "Delta Effect")
            .replace("Vega planning example", "Delta planning example")
            .replace("This simplified example holds other inputs constant to isolate volatility exposure.", "This simplified example holds other inputs constant to isolate directional exposure.")
            .replace("Continue the Vega &amp; Volatility cluster", "Continue the Delta Effect cluster")
            .replace("Level 6 – Vega &amp; Volatility course", "Level 7 – Delta Effect course")
            .replace("Start Level 6 — Free", "Start Level 7 — Free")
            .replace("Free Level 6 Course", "Free Level 7 Course")
            .replace("Learn vega and volatility through structured lessons and practical examples.", "Learn delta, gamma and hedging through structured lessons and practical examples."))


def card_html(article: dict) -> str:
    return base.card_html(article)


def update_index() -> None:
    path = BLOG / "index.html"
    source = path.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    if 'href="what-is-delta-in-options/"' not in source:
        source = source.replace(marker, "\n".join(card_html(a) for a in ARTICLES) + "\n" + marker, 1)
    source = source.replace("<strong>90</strong> guides", "<strong>105</strong> guides")
    if "Explore Level 7" not in source:
        source = source.replace('<a class="btn btn-gold" href="../courses/options-trading-course-level-6-vega-and-volatility/">Explore Level 6 →</a>', '<a class="btn btn-gold" href="../courses/options-trading-course-level-6-vega-and-volatility/">Explore Level 6 →</a><a class="btn btn-gold" href="../courses/option-greeks-level-7-delta-effect-strategy/">Explore Level 7 →</a>')
    path.write_text(source)


def update_scripts() -> None:
    path = BLOG / "blog.js"
    source = path.read_text().replace("const clusterPriority = card => card.textContent.includes('Vega') ? 6 :", "const clusterPriority = card => card.textContent.includes('Delta') ? 7 : card.textContent.includes('Vega') ? 6 :")
    path.write_text(source)
    path = ROOT / "favicon.js"
    source = path.read_text()
    marker = "    'vega-volatility-mistakes': '/assets/images/blog/vega-volatility-mistakes.webp'"
    additions = ",\n".join(f"    '{a['slug']}': '/assets/images/blog/{a['slug']}.webp'" for a in ARTICLES)
    if "'what-is-delta-in-options'" not in source:
        source = source.replace(marker, marker + ",\n" + additions)
    path.write_text(source)


def main() -> None:
    for index, article in enumerate(ARTICLES):
        directory = BLOG / article["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(article_html(article, index))
    update_index()
    update_scripts()


if __name__ == "__main__":
    main()
