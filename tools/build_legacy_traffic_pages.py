#!/usr/bin/env python3
"""Restore the ten legacy WordPress articles that already receive traffic."""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://options-america.onrender.com"


def article(path, title, description, tag, image, deck, intro, sections, checklist, faqs, related, lang="en"):
    return {
        "path": path,
        "title": title,
        "description": description,
        "tag": tag,
        "image": image,
        "deck": deck,
        "intro": intro,
        "sections": sections,
        "checklist": checklist,
        "faqs": faqs,
        "related": related,
        "lang": lang,
    }


ARTICLES = [
    article(
        "2025/05/01/buying-to-open-vs-selling-to-open-key-differences",
        "Buying to Open vs Selling to Open: Key Differences",
        "Compare buying to open and selling to open, including rights, obligations, margin, assignment risk and practical order-entry examples.",
        "Options Basics · Order Entry",
        "assets/images/courses/legacy/options-trading-course-level-1-buying-call-option.png",
        "“Buy to open” and “sell to open” both create a new options position, but they create opposite rights, obligations and risk profiles.",
        [
            "The word <strong>open</strong> tells the broker that the order is creating or increasing a position. The word before it—buy or sell—determines whether the account owns the option or is short the option.",
            "This distinction matters because an option buyer pays premium for a right, while an option seller receives premium and accepts a contractual obligation. The correct ticket choice prevents accidental short positions and makes risk easier to understand before the order is sent.",
        ],
        [
            ("What does buying to open mean?", [
                "Buying to open creates a long option position. A long call gives the right to buy the underlying at the strike price; a long put gives the right to sell it. The buyer pays the premium and cannot lose more than that premium plus transaction costs in a standard long option.",
                "The position is later closed with a sell-to-close order, exercised, or allowed to expire. Time decay generally works against the buyer, while a favorable price move or an increase in implied volatility may help.",
            ]),
            ("What does selling to open mean?", [
                "Selling to open creates a short option position. The seller collects premium but accepts an obligation if assigned. A short call may require delivering shares; a short put may require buying shares at the strike price.",
                "Collateral depends on whether the option is covered, cash-secured, spread-defined or uncovered. Maximum profit is generally limited to the premium received, while losses can be substantial and may be unlimited for an uncovered short call.",
            ]),
            ("Buying and selling examples", [
                "If a stock trades at $100 and a trader buys one $105 call for $3, the order is buy to open and the initial debit is $300. Selling that same contract later for $5 is sell to close, producing a $200 gross gain.",
                "If another trader sells the $105 call first for $3, that order is sell to open. Buying it back later for $1 is buy to close, producing a $200 gross gain. The identical option can therefore represent opposite positions depending on the opening action.",
            ]),
            ("How risk and assignment differ", [
                "Long option holders control whether to exercise, subject to broker procedures and automatic-exercise rules. Short option holders do not control assignment and must be prepared for the resulting stock or futures position.",
                "Before selling to open, check buying power, contract multiplier, settlement type, dividends and expiration. A defined-risk spread still contains short-option assignment and execution considerations even though its expiration loss is capped.",
            ]),
        ],
        ["Confirm whether the order opens or closes a position.", "Check whether the account will be long or short the option.", "Calculate the total debit or credit using the contract multiplier.", "Review maximum loss, assignment and buying-power requirements.", "Use a limit order and verify the final position after execution."],
        [("Can I sell an option without owning it first?", "Yes. A sell-to-open order creates a short option, subject to broker approval and collateral rules."), ("How do I close a bought option?", "Use sell to close for the contracts you own."), ("How do I close a written option?", "Use buy to close for the contracts you previously sold to open.")],
        [("Buying a call option step by step", "/blog/how-to-buy-a-call-option/"), ("How to sell a covered call", "/blog/how-to-sell-a-covered-call/"), ("Options course library", "/courses/")],
    ),
    article(
        "2025/05/01/butterfly-spread-vs-iron-butterfly-key-differences",
        "Butterfly Spread vs Iron Butterfly: Key Differences",
        "Compare a standard butterfly spread with an iron butterfly through construction, debit or credit, risk, breakevens, volatility and assignment.",
        "Options Strategies · Comparison",
        "assets/images/courses/legacy/advanced-option-level-12-butterfly.png",
        "Both strategies target a price area at expiration, but they use different option combinations and create different cash flows and operational risks.",
        [
            "A standard long butterfly is commonly built with three strikes using calls or puts. An iron butterfly combines a short straddle at the center strike with protective wings, normally producing an opening credit.",
            "Their expiration payoff shapes can look similar, yet entry cost, margin presentation, early-assignment exposure and sensitivity before expiration can differ. Traders should compare the complete position rather than choosing by credit versus debit alone.",
        ],
        [
            ("How each butterfly is constructed", ["A long call butterfly buys one lower-strike call, sells two middle-strike calls and buys one higher-strike call, usually with equal wing widths. A put butterfly can create the same expiration payoff with puts.", "An iron butterfly sells a call and put at the middle strike, buys a lower-strike put and buys a higher-strike call. The long wings define the expiration risk of the short straddle."]),
            ("Debit, credit and maximum risk", ["The long butterfly is generally opened for a net debit, which is usually its maximum expiration loss. Its maximum value occurs when the underlying finishes at the middle strike.", "The iron butterfly is generally opened for a credit. Its maximum loss equals a wing width minus the credit, multiplied by the contract multiplier. The credit is not free income; it is compensation for accepting concentrated risk around the short strike."]),
            ("Breakevens and profit zone", ["For an equal-width long butterfly, the lower breakeven is the lower strike plus the debit and the upper breakeven is the upper strike minus the debit. The iron butterfly uses the middle strike plus or minus the credit for its basic expiration breakevens.", "Both positions are sensitive to where the underlying finishes. A trader can be correct about a quiet market but still miss the narrow high-profit region."]),
            ("Volatility, time and assignment", ["Both structures are often used when a trader expects movement to remain limited. Their live vega and theta change with price, time and strike location, so the current Greek profile should be checked rather than assumed.", "The iron butterfly contains short options on both sides and can face early assignment. The all-call or all-put butterfly can also be assigned on short legs, but the stock consequences and exercise choices depend on the option type and moneyness."]),
        ],
        ["Compare the same expiration and wing widths.", "Calculate both maximum loss and realistic profit targets.", "Check bid-ask spreads across all legs.", "Review early-assignment and dividend risk.", "Plan an exit before expiration-week gamma becomes dominant."],
        [("Is an iron butterfly safer than a butterfly?", "Not automatically. Both can be defined-risk, but their cash flows, assignments and live risk profiles differ."), ("Which strategy receives a credit?", "An iron butterfly is normally a credit trade; a standard long butterfly is normally a debit trade."), ("Where is maximum profit?", "For the basic versions, maximum expiration profit is centered at the middle strike.")],
        [("Broken Wings Butterfly course", "/courses/level-47-broken-wings-butterfly/"), ("Butterfly course", "/courses/advanced-option-level-12-butterfly/"), ("All courses", "/courses/")],
    ),
    article(
        "2025/05/01/case-studies-effective-portfolio-hedges-with-vix-options",
        "Case Studies: Effective Portfolio Hedges with VIX Options",
        "Study practical VIX option hedge structures, sizing, timing, volatility term structure and the limitations of portfolio protection.",
        "Portfolio Hedging · VIX Options",
        "assets/images/courses/legacy/level-22-vix-options-hedging-and-speculation.png",
        "VIX options can respond sharply during equity stress, but an effective hedge requires deliberate timing, sizing and an understanding of VIX settlement.",
        ["A VIX option is not a direct option on the current spot VIX number. Its value reflects the relevant VIX futures market, time to settlement and volatility expectations.", "The case studies below are educational frameworks rather than promises. A hedge can lose money repeatedly during calm periods and still fail to match a specific portfolio if its horizon or size is wrong."],
        [
            ("Case study 1: scheduled event protection", ["A diversified equity portfolio faces a known policy announcement. Instead of hedging permanently, the investor buys a limited number of VIX calls that expire after the event, defining the premium at risk.", "The position benefits if expected volatility rises enough before or during the event. If uncertainty fades, the calls can lose from time decay and falling implied volatility even when equities drift lower."]),
            ("Case study 2: call-spread hedge", ["Buying a VIX call and selling a higher-strike call reduces premium but caps the hedge payoff. This can fit a portfolio that needs protection against a moderate volatility spike rather than an unlimited tail event.", "The short call also changes liquidity, settlement and exit decisions. Both legs should use the same expiration unless the trader intentionally wants calendar risk."]),
            ("Case study 3: rolling protection", ["A rolling program buys protection for a defined horizon and refreshes it before expiration. The advantage is continuity; the cost is repeated premium expenditure during quiet markets.", "Rules for roll dates, target strikes and maximum annual hedge budget reduce emotional decisions. Performance should be measured against the unhedged portfolio after all premiums and execution costs."]),
            ("Sizing and basis risk", ["Hedge size should be based on portfolio dollars, beta, expected drawdown and the estimated option response—not on a fixed number of contracts. VIX may not move in a stable one-for-one relationship with a concentrated stock portfolio.", "Run multiple stress cases, including a slow decline, a sudden crash and an event that raises single-stock volatility without lifting the broad-market VIX materially."]),
        ],
        ["Define the loss the hedge is intended to offset.", "Match the option expiration to the risk window.", "Model VIX futures rather than relying on spot VIX alone.", "Set a premium budget and maximum position size.", "Plan exits for both a volatility spike and a quiet outcome."],
        [("Do VIX calls always rise when stocks fall?", "No. The relationship is strong during many shocks but is not guaranteed for every portfolio or decline."), ("Can VIX options be exercised into VIX shares?", "No. VIX options are cash-settled using a special settlement value."), ("Why can a hedge lose before expiration?", "Time decay, term structure and a decline in implied volatility can reduce its value.")],
        [("VIX vs implied volatility", "/blog/vix-vs-implied-volatility/"), ("VIX hedging course", "/courses/level-22-vix-options-hedging-and-speculation/"), ("Portfolio optimization course", "/courses/options-portfolio-level-20-optimizing-portfolio/")],
    ),
    article(
        "2025/05/01/synthetic-futures-using-options",
        "Synthetic Futures Using Options",
        "Learn how matching-strike calls and puts can create synthetic long or short futures exposure, including payoff, margin and expiration risk.",
        "Options on Futures · Synthetic Positions",
        "assets/images/courses/legacy/introduction-to-futures-contract.png",
        "A synthetic futures position combines a call and a put at the same strike and expiration to approximate the directional payoff of a futures contract.",
        ["Put-call parity links calls, puts, the underlying and financing. Buying a call while selling a put creates synthetic long exposure; buying a put while selling a call creates synthetic short exposure.", "The payoff may resemble a future, but execution, margin, assignment, settlement and liquidity still come from the individual option legs. Contract specifications must be checked for the exact futures option."],
        [
            ("Synthetic long futures", ["A synthetic long normally buys a call and sells a put with the same strike and expiration. Above the strike the call gains; below the strike the short put loses, producing broadly linear bullish exposure at expiration.", "The net debit or credit shifts the economic entry level. It should be included when comparing the synthetic with the quoted futures price."]),
            ("Synthetic short futures", ["A synthetic short buys the put and sells the matching call. A decline helps the long put, while a rally hurts the short call, producing broadly linear bearish exposure.", "The short option creates margin and assignment responsibilities. Defined risk should not be assumed merely because two option legs are present."]),
            ("Pricing and arbitrage logic", ["When equivalent positions become mispriced, professional traders may use conversion or reversal structures to capture differences after financing, dividends, fees and exercise terms.", "Retail traders should treat apparent arbitrage cautiously. Bid-ask spreads, margin rates, early exercise and contract settlement can eliminate a theoretical edge."]),
            ("Futures-option details", ["Confirm whether the option is American- or European-style, whether it settles into a future or cash, the multiplier and the last trading day. These details vary across products.", "A position held through expiration can create a futures position with significant overnight exposure. Closing procedures and broker cutoffs should be understood in advance."]),
        ],
        ["Use the same strike and expiration for both legs.", "Include the net premium in the effective entry price.", "Check multiplier, settlement and exercise style.", "Model the resulting futures exposure after expiration.", "Confirm margin and liquidation rules with the broker."],
        [("What creates a synthetic long future?", "Long call plus short put at the same strike and expiration."), ("What creates a synthetic short future?", "Long put plus short call at the same strike and expiration."), ("Is the risk limited?", "No. The payoff is broadly linear and can carry substantial risk, similar to directional futures exposure.")],
        [("Options on futures learning path", "/learning-paths/options-on-futures/"), ("Introduction to futures", "/courses/introduction-to-futures-contract/"), ("Options course library", "/courses/")],
    ),
    article(
        "2025/05/01/can-you-sell-a-put-option-before-expiration",
        "Can You Sell a Put Option Before Expiration?",
        "Learn how to sell a long put before expiration, choose an order, preserve time value and compare selling with exercising.",
        "Buying Puts · Exit Planning",
        "assets/images/blog/when-to-sell-put-option-you-bought.webp",
        "Yes. A put option you bought can normally be sold at any time before expiration while the market is open and the contract has a tradable bid.",
        ["Selling a purchased put is called <strong>selling to close</strong>. It ends the long-option position without creating a new obligation, provided the quantity does not exceed the contracts owned.", "Many traders sell rather than exercise because the option may still contain time value. The best choice depends on liquidity, remaining premium, stock-position goals and broker procedures."],
        [
            ("How to sell a long put", ["Open the existing position in the broker platform, choose sell to close, confirm the expiration and strike, enter the number of contracts and use a limit price. Review the order before submission.", "After execution, verify that the position quantity is zero. Accidentally choosing sell to open can create an unwanted short put."]),
            ("When selling may make sense", ["A trader may close after reaching a profit target, when the bearish thesis weakens, when time decay is accelerating or before a scheduled event changes the risk.", "Closing can also protect remaining value. Waiting for the final few dollars may expose a profitable put to a rapid rebound or volatility decline."]),
            ("Sell versus exercise", ["Selling transfers the option to another market participant and normally realizes both intrinsic and remaining time value. Exercising uses the put right to sell shares at the strike price.", "Exercise may be appropriate in specific stock-delivery situations, but it can require shares, create a short-stock position or sacrifice time value. Broker rules should be checked first."]),
            ("Liquidity and order execution", ["Volume, open interest and the bid-ask spread affect the price available. A market order in a wide spread can produce a poor fill.", "Start with a realistic limit near the midpoint and adjust deliberately. The theoretical option value is not a guaranteed execution price."]),
        ],
        ["Select sell to close, not sell to open.", "Confirm strike, expiration and contract quantity.", "Compare intrinsic value with the current bid.", "Use a limit order when the spread is wide.", "Verify that the position is closed after execution."],
        [("Can I sell an out-of-the-money put?", "Yes, if there is a buyer and a tradable bid, although the remaining value may be small."), ("Do I need to own shares to sell my long put?", "No. Selling to close the option does not require exercising it against shares."), ("What happens if I hold until expiration?", "The put may expire worthless or be automatically exercised if it meets the broker's in-the-money threshold.")],
        [("When to sell a put you bought", "/blog/when-to-sell-put-option-you-bought/"), ("Sell versus exercise", "/blog/sell-put-option-vs-exercise/"), ("Buying puts course", "/courses/options-trading-level-3-buying-put-option-strategy/")],
    ),
    article(
        "2025/05/01/best-options-strategies-for-small-accounts",
        "Best Options Strategies for Small Accounts",
        "Compare defined-risk options strategies for smaller accounts, including long options, vertical spreads and cash-secured approaches.",
        "Risk Management · Small Accounts",
        "assets/images/courses/legacy/managing-a-bullish-to-neutral-options-portfolio.png",
        "The best strategy for a small account is not the one with the cheapest contract—it is the one whose maximum loss, liquidity and complexity fit the account.",
        ["Small accounts are especially vulnerable to oversized positions, commissions, wide spreads and margin calls. A single loss should not determine the survival of the account.", "Defined-risk structures make the possible expiration loss visible before entry. They still require realistic sizing because several small defined losses can accumulate quickly."],
        [
            ("Long calls and long puts", ["A purchased option limits maximum loss to the premium paid, making the dollar risk easy to define. The trade still needs enough time and a realistic strike; very cheap far-out-of-the-money options frequently expire worthless.", "Use long options when the thesis includes both direction and timing. Keep the premium small relative to account equity."]),
            ("Vertical debit spreads", ["A bull call spread or bear put spread reduces premium by selling another strike. The trade caps maximum profit in exchange for lower cost and often lower theta and vega exposure.", "Spreads can be efficient for smaller accounts, but multi-leg bid-ask costs and expiration assignment must be included."]),
            ("Defined-risk credit spreads", ["Bull put and bear call spreads receive premium while using a protective long option to define expiration risk. The maximum loss—not the credit—should drive position size.", "Credit spreads can lose several times the premium received. Avoid treating a high win rate as proof of low risk."]),
            ("Cash-secured puts and covered calls", ["These strategies can require enough capital for 100 shares, so they are not automatically suitable for a small account. Lower-priced liquid underlyings may fit, but stock downside remains substantial.", "Never choose an underlying only because one contract fits the account. Business quality, diversification and assignment willingness remain essential."]),
        ],
        ["Risk only a modest percentage of account equity per idea.", "Prefer liquid options with tight spreads.", "Know the exact maximum loss before entry.", "Avoid overlapping positions in the same underlying or sector.", "Keep cash available for adjustments and assignment."],
        [("Are spreads good for small accounts?", "They can be because risk is defined, but fees, liquidity and assignment still matter."), ("Should a small account sell naked options?", "Undefined-risk options can create losses and margin demands that are disproportionate to a small account."), ("Are cheap options safer?", "No. A low premium can reflect a low probability of finishing with value.")],
        [("Long call risks", "/blog/buying-call-options-risks-mistakes/"), ("Long put risks", "/blog/long-put-risks-mistakes/"), ("Options course library", "/courses/")],
    ),
    article(
        "2025/05/01/choosing-the-right-strike-price-for-a-put-option",
        "Choosing the Right Strike Price for a Put Option",
        "Choose a put option strike using moneyness, delta, premium, breakeven, liquidity and the purpose of the trade.",
        "Buying Puts · Strike Selection",
        "assets/images/blog/how-to-choose-put-option-strike.webp",
        "The right put strike is the one that matches the expected move, time horizon and maximum acceptable loss—not simply the cheapest available contract.",
        ["Put strikes change the trade's upfront cost, directional sensitivity, breakeven and probability of retaining value at expiration. Higher strikes generally cost more but provide more immediate downside exposure.", "Strike selection should begin with the reason for the trade: bearish speculation, portfolio protection or a spread. The same strike can be appropriate for one purpose and unsuitable for another."],
        [
            ("ITM, ATM and OTM put strikes", ["An in-the-money put contains intrinsic value and usually has a more negative delta. An at-the-money put often provides strong sensitivity but carries meaningful time value.", "An out-of-the-money put costs less but needs a larger decline to gain intrinsic value. Cheap premium does not mean low probability of loss."]),
            ("Use delta as a sensitivity guide", ["Delta estimates how much the option value may change for a small underlying move, all else equal. A -0.60 delta put has more immediate directional exposure than a -0.20 delta put.", "Delta changes with price, time and volatility, so it should not be treated as a fixed forecast or an exact probability."]),
            ("Calculate breakeven and maximum loss", ["For a long put at expiration, breakeven equals the strike minus the premium paid. Maximum loss is the premium plus transaction costs.", "Compare several strikes using the same expiration and model more than one stock-price outcome. A higher strike can have a better breakeven even though its premium is larger."]),
            ("Check liquidity and volatility", ["Favor strikes with active markets, useful open interest and manageable bid-ask spreads. Poor execution can erase the theoretical benefit of a particular strike.", "Implied volatility affects all premiums. A put purchased when fear is expensive may lose from volatility contraction even if the stock declines modestly."]),
        ],
        ["Define the target price and expected timing.", "Compare ITM, ATM and OTM strikes side by side.", "Calculate expiration breakeven for each strike.", "Review delta, implied volatility and bid-ask spread.", "Size the premium so a total loss is acceptable."],
        [("Which put strike has the most protection?", "A higher strike generally begins protecting at a higher stock price but also costs more."), ("Is an OTM put better because it is cheaper?", "Not necessarily. It requires a larger favorable move and has a greater chance of expiring worthless."), ("What is a put's expiration breakeven?", "Strike price minus the premium paid, before fees.")],
        [("Complete put strike guide", "/blog/how-to-choose-put-option-strike/"), ("ITM vs ATM vs OTM puts", "/blog/itm-atm-otm-put-options/"), ("Buying puts course", "/courses/options-trading-level-3-buying-put-option-strategy/")],
    ),
    article(
        "2025/04/12/que-son-las-opciones-una-definicion-sencilla",
        "¿Qué son las opciones? Una definición sencilla",
        "Aprende qué son las opciones financieras, cómo funcionan las calls y puts, qué significa la prima y cuáles son los principales riesgos.",
        "Opciones · Guía para principiantes",
        "assets/images/courses/legacy/options-trading-course-level-1-buying-call-option.png",
        "Una opción es un contrato financiero que otorga un derecho al comprador y crea una obligación para el vendedor durante un período determinado.",
        ["Las opciones se relacionan con un activo subyacente, como una acción, un ETF, un índice o un futuro. Cada contrato tiene un precio de ejercicio, una fecha de vencimiento y una prima.", "Existen dos tipos básicos: la opción de compra, conocida como <strong>call</strong>, y la opción de venta, conocida como <strong>put</strong>. Entender la diferencia entre comprar y vender estos contratos es esencial antes de operar."],
        [
            ("¿Qué es una opción call?", ["Una call concede al comprador el derecho, pero no la obligación, de comprar el activo al precio de ejercicio. El comprador suele utilizarla cuando espera una subida.", "El comprador paga una prima y su pérdida máxima normal se limita a ese importe más los costes. El vendedor recibe la prima y acepta la obligación correspondiente si es asignado."]),
            ("¿Qué es una opción put?", ["Una put concede al comprador el derecho a vender el activo al precio de ejercicio. Puede utilizarse para una expectativa bajista o como protección de una cartera.", "Una put comprada puede perder toda su prima si vence sin valor. Una put vendida puede obligar al vendedor a comprar acciones al precio de ejercicio."]),
            ("Ejemplo sencillo", ["Supongamos que una acción cotiza a $100 y una call con strike $105 cuesta $3. Un contrato estándar suele representar 100 acciones, por lo que la prima total sería $300.", "Al vencimiento, el punto de equilibrio básico sería $108: strike $105 más prima $3. Antes del vencimiento, el precio también depende del tiempo y de la volatilidad implícita."]),
            ("Riesgo, tiempo y volatilidad", ["Las opciones tienen vencimiento. El valor temporal disminuye a medida que pasa el tiempo, especialmente cerca de la fecha final.", "La volatilidad implícita también cambia la prima. Acertar la dirección no garantiza un beneficio si el movimiento llega tarde o es menor que el esperado."]),
        ],
        ["Identifica si es una call o una put.", "Comprueba si compras o vendes el contrato.", "Calcula la prima total y la pérdida máxima.", "Revisa strike, vencimiento y liquidez.", "Empieza con riesgo limitado y una posición pequeña."],
        [("¿Comprar una opción obliga a ejercerla?", "No. El comprador tiene un derecho y normalmente puede vender la opción antes del vencimiento."), ("¿Se puede perder toda la prima?", "Sí. Una opción comprada puede vencer sin valor."), ("¿Vender opciones tiene más riesgo?", "Puede tener un riesgo considerable porque el vendedor acepta una obligación y necesita garantías.")],
        [("Curso gratuito de opciones", "/courses/"), ("Guía sobre opciones call", "/blog/what-is-a-call-option/"), ("Guía sobre opciones put", "/blog/what-is-buying-a-put-option/")],
        lang="es",
    ),
    article(
        "2025/04/01/assignment-on-expiration-how-it-works",
        "Assignment on Expiration: How It Works",
        "Understand option assignment at expiration, automatic exercise, resulting share positions, settlement and the risks of holding spreads too long.",
        "Expiration · Assignment",
        "assets/images/blog/put-option-assignment-explained.webp",
        "Assignment is the process that requires an option seller to fulfill the contract after the holder exercises, including through automatic exercise at expiration.",
        ["Calls and puts create different stock transactions when exercised. Broker thresholds, contrary instructions and account restrictions can also affect the final result.", "Traders should never assume that a spread will simply disappear at expiration. One leg can be exercised or assigned while another expires, creating unexpected stock and market exposure."],
        [
            ("Call assignment at expiration", ["A short call that is assigned generally requires the seller to deliver shares at the strike price. A covered-call writer normally loses the shares; an uncovered writer may become short stock or face a broker closeout.", "The option's closing price alone does not determine the final outcome. The official closing and exercise process, after-hours movement and broker instructions can matter."]),
            ("Put assignment at expiration", ["A short put that is assigned generally requires buying shares at the strike price. One standard U.S. equity contract commonly represents 100 shares.", "The effective stock cost is economically reduced by the premium received, but the account still needs sufficient buying power for the full assignment."]),
            ("Automatic exercise and pin risk", ["Options that finish in the money by the clearing threshold are commonly exercised automatically unless contrary instructions are submitted. Broker practices and deadlines vary.", "When the underlying closes near a strike, the final exercise outcome can be uncertain. This pin risk is especially important for short spreads and positions held into expiration."]),
            ("What happens to spreads", ["A defined-risk spread limits its theoretical expiration loss when both legs are handled as expected. If the short leg is assigned and the long leg is not exercised, the account can hold an unhedged share position.", "Closing the spread before expiration can remove this operational uncertainty, although execution cost and liquidity should be considered."]),
        ],
        ["Know the multiplier and settlement type.", "Check broker exercise and contrary-instruction deadlines.", "Calculate the shares or futures created by assignment.", "Review after-hours and pin risk near the strike.", "Close positions early when the resulting exposure is unacceptable."],
        [("Are all ITM options exercised automatically?", "Many are, subject to clearing thresholds, broker procedures and contrary instructions."), ("Can an OTM option be exercised?", "A holder may submit exercise instructions even when the option appears out of the money."), ("Does assignment happen only at expiration?", "American-style options can be assigned before expiration as well.")],
        [("Put assignment explained", "/blog/put-option-assignment-explained/"), ("Early assignment on short puts", "/blog/early-assignment-short-put/"), ("Covered-call assignment", "/blog/covered-call-assignment-explained/")],
    ),
    article(
        "2025/05/01/best-tools-for-monitoring-open-options-positions",
        "Best Tools for Monitoring Open Options Positions",
        "Compare the essential tools for tracking open options positions, Greeks, P&L, volatility, earnings, assignment and portfolio exposure.",
        "Trading Tools · Position Management",
        "assets/images/courses/legacy/options-portfolio-level-20-optimizing-portfolio.png",
        "A useful options dashboard should show more than today's profit and loss. It should explain how price, time, volatility and events can change the position next.",
        ["The best tool depends on the portfolio. A single long call may need only a clear risk graph and Greeks, while a multi-expiration portfolio needs aggregation, alerts and scenario analysis.", "Broker platforms are often the source of truth for live positions. Independent analytics tools can add better visualization, journaling and stress testing, but their data and contract mapping should be verified."],
        [
            ("Broker position monitor", ["Start with a broker view that clearly shows quantity, average price, current mark, bid-ask spread, expiration and strike. Confirm that multi-leg strategies are grouped correctly.", "Useful alerts include underlying price, option price, days to expiration, earnings and short-option assignment conditions."]),
            ("Greeks and scenario analysis", ["Track position delta, gamma, theta and vega in contract dollars, not only per-share numbers. Aggregate exposures by underlying and expiration.", "A scenario tool should change price, date and implied volatility together. Static payoff diagrams show expiration outcomes but can miss important pre-expiration behavior."]),
            ("Volatility and event calendar", ["Compare current implied volatility with its own history and review the volatility term structure. Earnings, dividends, economic releases and product-specific reports can change risk quickly.", "Event dates should be verified from a reliable primary source because calendar errors can make an otherwise sound trade plan irrelevant."]),
            ("Journal and risk dashboard", ["Record the original thesis, planned exits, position size and adjustments. Screenshots alone do not explain why a decision was made.", "A portfolio dashboard should flag concentration, correlated exposures, upcoming expirations and maximum loss. Simple, accurate data is more valuable than dozens of unused indicators."]),
        ],
        ["Verify positions against the broker.", "Track dollar Greeks and days to expiration.", "Set price, event and assignment alerts.", "Stress price and volatility together.", "Journal entry logic, adjustments and final outcome."],
        [("Do I need a paid options platform?", "Not always. Many brokers provide adequate monitoring, while specialized tools add deeper scenarios or journaling."), ("Which Greek should I monitor most?", "It depends on the strategy; delta, gamma, theta and vega should be viewed together."), ("How often should positions be reviewed?", "Review frequency should match expiration, event risk and position size, with shorter-dated options requiring closer attention.")],
        [("Portfolio Greeks", "/blog/portfolio-option-greeks-risk/"), ("Greeks scenario analysis", "/blog/option-greeks-scenario-analysis/"), ("Portfolio optimization course", "/courses/options-portfolio-level-20-optimizing-portfolio/")],
    ),
]


def paragraphs(items):
    return "".join(f"<p>{item}</p>" for item in items)


def render(a):
    canonical = f"{ORIGIN}/{a['path']}/"
    image_url = f"{ORIGIN}/{a['image']}"
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": answer}}
            for q, answer in a["faqs"]
        ],
    }
    labels = {
        "author": "By Options America",
        "reviewed": "Reviewed September 11, 2026",
        "read": "10-minute read",
        "key": "Key idea",
        "checklist": "Practical checklist",
        "faq": "Frequently asked questions",
        "continue": "Continue learning",
        "courses": "Explore the Free Course Library →",
        "toc": "In this guide",
        "course_title": "Free Options Courses",
        "course_copy": "Build your knowledge through structured lessons and practical examples.",
        "browse": "Browse courses →",
        "disclaimer": "Options and futures involve risk and are not suitable for every investor. This article is for educational purposes only and does not constitute investment advice or a recommendation to buy or sell any security.",
    }
    if a["lang"] == "es":
        labels.update({
            "author": "Por Options America",
            "reviewed": "Revisado el 11 de septiembre de 2026",
            "read": "Lectura de 10 minutos",
            "key": "Idea principal",
            "checklist": "Lista práctica",
            "faq": "Preguntas frecuentes",
            "continue": "Continúa aprendiendo",
            "courses": "Explora los cursos gratuitos →",
            "toc": "En esta guía",
            "course_title": "Cursos gratuitos de opciones",
            "course_copy": "Aprende con lecciones estructuradas y ejemplos prácticos.",
            "browse": "Ver cursos →",
            "disclaimer": "Las opciones y los futuros implican riesgos y no son adecuados para todos los inversores. Este artículo tiene fines educativos y no constituye asesoramiento financiero ni una recomendación de compra o venta.",
        })
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["title"],
        "description": a["description"],
        "datePublished": a["path"][:10].replace("/", "-"),
        "dateModified": "2026-09-11",
        "author": {"@type": "Organization", "name": "Options America"},
        "publisher": {"@type": "Organization", "name": "Options America"},
        "mainEntityOfPage": canonical,
    }
    section_html = "".join(
        f'<h2 id="section-{i}">{html.escape(title)}</h2>{paragraphs(copy)}'
        for i, (title, copy) in enumerate(a["sections"], 1)
    )
    toc_html = "".join(
        f'<a href="#section-{i}">{html.escape(title)}</a>'
        for i, (title, _) in enumerate(a["sections"], 1)
    )
    related_html = "".join(f'<li><a href="{url}">{html.escape(label)}</a></li>' for label, url in a["related"])
    faq_html = "".join(f'<div class="faq-item"><h3>{html.escape(q)}</h3><p>{html.escape(answer)}</p></div>' for q, answer in a["faqs"])
    checklist_html = "".join(f"<li>{html.escape(item)}</li>" for item in a["checklist"])
    return f'''<!doctype html>
<html lang="{a['lang']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{html.escape(a['title'])}</title>
  <meta name="description" content="{html.escape(a['description'], quote=True)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="article"><meta property="og:title" content="{html.escape(a['title'], quote=True)}"><meta property="og:description" content="{html.escape(a['description'], quote=True)}"><meta property="og:image" content="{image_url}">
  <link rel="stylesheet" href="../../../../styles.css">
  <link rel="stylesheet" href="../../../../blog/blog.css">
  <script src="/favicon.js"></script>
  <script type="application/ld+json">{json.dumps(article_schema, ensure_ascii=False)}</script>
  <script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script>
</head>
<body>
  <header class="site-header"><div class="container nav"><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><nav><a href="/courses/">Courses</a><a href="/#paths">Learning Paths</a><a href="/#strategies">Strategies</a><a href="/#futures">Options on Futures</a><a href="/blog/">Blog</a><a href="/#resources">Resources</a></nav><a class="btn btn-gold" href="/courses/">Start Learning — Free</a></div></header>
  <main>
    <section class="article-hero"><div class="container"><div class="breadcrumbs"><a href="/">Home</a><span>›</span><a href="/blog/">Blog</a><span>›</span><span>{html.escape(a['tag'])}</span></div><p class="eyebrow">{html.escape(a['tag'])}</p><h1>{html.escape(a['title'])}</h1><p class="article-deck">{html.escape(a['deck'])}</p><div class="article-meta"><span>{labels['author']}</span><span>{labels['reviewed']}</span><span>{labels['read']}</span></div></div></section>
    <div class="container article-layout">
      <article class="article-body">
        <img src="/{a['image']}" alt="{html.escape(a['title'], quote=True)}">
        {paragraphs(a['intro'])}
        <div class="article-callout"><strong>{labels['key']}:</strong> {html.escape(a['deck'])}</div>
        {section_html}
        <h2 id="checklist">{labels['checklist']}</h2><ul>{checklist_html}</ul>
        <h2 id="faq">{labels['faq']}</h2>{faq_html}
        <h2>{labels['continue']}</h2><ul>{related_html}</ul>
        <p><a class="btn btn-gold" href="/courses/">{labels['courses']}</a></p>
        <p class="article-disclaimer">{labels['disclaimer']}</p>
      </article>
      <aside class="article-sidebar"><div class="toc"><strong>{labels['toc']}</strong>{toc_html}<a href="#checklist">{labels['checklist']}</a><a href="#faq">{labels['faq']}</a></div><div class="course-cta"><strong>{labels['course_title']}</strong><p>{labels['course_copy']}</p><a class="btn btn-gold" href="/courses/">{labels['browse']}</a></div></aside>
    </div>
  </main>
  <footer><div class="container footer-grid"><div><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><p>The free resource for learning options trading from beginner to advanced.</p></div><div><h4>Learn</h4><a href="/courses/">Courses</a><a href="/#paths">Learning Paths</a><a href="/learning-paths/beginner/">Beginner Path</a></div><div><h4>Strategies</h4><a href="/learning-paths/option-greeks/">Option Greeks</a><a href="/#strategies">All Strategies</a></div><div><h4>Futures</h4><a href="/learning-paths/options-on-futures/">Options on Futures</a></div><div><h4>Resources</h4><a href="/blog/">Blog</a><a href="/courses/?category=Case%20Studies">Case Studies</a><a href="/courses/">Course Library</a></div></div><div class="container copyright">© <span data-current-year></span> Options America · Educational content only — not financial advice.</div></footer>
  <script>document.querySelectorAll('[data-current-year]').forEach(e=>e.textContent=new Date().getFullYear())</script>
</body>
</html>'''


def card(a):
    return f'''        <a class="post-card" href="../{a['path']}/"><img src="../{a['image']}" alt="{html.escape(a['title'], quote=True)}"><div class="post-card-copy"><span class="tag">{html.escape(a['tag'])}</span><h2>{html.escape(a['title'])}</h2><p>{html.escape(a['description'])}</p><strong>Read the guide →</strong></div></a>'''


def update_blog_index():
    index = ROOT / "blog" / "index.html"
    source = index.read_text()
    marker = '      </div>\n      <div class="blog-empty"'
    if '../2025/05/01/buying-to-open-vs-selling-to-open-key-differences/' not in source:
        source = source.replace(marker, "\n".join(card(a) for a in ARTICLES) + "\n" + marker, 1)
    source = source.replace("<strong>120</strong> guides", "<strong>130</strong> guides")
    index.write_text(source)


def main():
    for a in ARTICLES:
        target = ROOT / a["path"]
        target.mkdir(parents=True, exist_ok=True)
        (target / "index.html").write_text(render(a))
    update_blog_index()


if __name__ == "__main__":
    main()
