#!/usr/bin/env python3
"""Build Korean SEO cluster 1: U.S. stock options for beginners."""

from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://options-america.com"
OUT = ROOT / "ko" / "blog"
COURSE = "/courses/options-trading-course-level-1-buying-call-option/"
PUBLISHED = "2026-09-14"


ARTICLES = [
    {
        "slug": "us-stock-options-guide",
        "title": "미국 주식 옵션 기초 가이드: 초보자가 꼭 알아야 할 모든 것",
        "short": "미국 주식 옵션 기초",
        "description": "미국 주식 옵션의 구조, 콜옵션과 풋옵션, 프리미엄, 행사가, 만기, 손익과 위험을 초보자 눈높이에서 설명합니다.",
        "deck": "미국 주식 옵션을 처음 접했다면 종목을 고르기 전에 계약의 권리, 의무, 시간과 위험부터 이해해야 합니다. 이 가이드는 학습 순서를 한 번에 정리합니다.",
        "tag": "미국 주식 옵션 · 종합 가이드",
        "read": "12분",
        "image": "/assets/images/courses/legacy/options-trading-course-level-1-buying-call-option.png",
        "alt": "미국 주식 옵션 기초를 설명하는 교육 화면",
        "sections": [
            ("미국 주식 옵션이란?", "what", """
<p><strong>미국 주식 옵션</strong>은 특정 미국 주식이나 ETF를 미리 정한 가격에 사거나 팔 수 있는 권리를 일정 기간 동안 거래하는 계약입니다. 주식을 직접 매수하는 것과 달리 옵션에는 기초자산, 콜 또는 풋, 행사가격, 만기일이라는 네 가지 핵심 조건이 붙습니다. 이 조건 중 하나만 달라져도 전혀 다른 계약입니다.</p>
<p>옵션 매수자는 권리를 얻기 위해 프리미엄을 지불합니다. 옵션 매도자는 프리미엄을 받는 대신 배정될 경우 계약을 이행할 의무를 부담합니다. 따라서 “가격이 오를까 내릴까”만 맞히는 상품으로 보면 위험합니다. 방향뿐 아니라 움직임의 크기, 발생 시점, 변동성 변화까지 결과에 영향을 줍니다.</p>"""),
            ("콜옵션과 풋옵션", "calls-puts", """
<p><strong>콜옵션</strong> 매수자는 만기 전 또는 만기에 기초자산을 행사가격으로 살 수 있는 권리를 가집니다. 주가 상승을 예상할 때 활용할 수 있지만, 예상 방향이 맞아도 상승 폭이 프리미엄과 시간가치 감소를 넘지 못하면 손실이 날 수 있습니다.</p>
<p><strong>풋옵션</strong> 매수자는 기초자산을 행사가격으로 팔 수 있는 권리를 가집니다. 하락 전망이나 보유 주식의 위험 관리에 활용됩니다. 두 계약의 차이를 먼저 익히려면 <a href="../what-are-us-stock-options/">미국 주식 옵션의 구조</a>와 다음에 공개될 콜·풋 심화 학습을 순서대로 보는 것이 좋습니다.</p>"""),
            ("한 계약의 가격은 어떻게 읽나", "contract", """
<p>미국 상장 주식 옵션은 표준 계약 한 개가 일반적으로 주식 100주를 기준으로 하지만, 기업행동으로 조정된 계약 등 예외가 있으므로 항상 브로커의 계약 명세를 확인해야 합니다. 화면에 프리미엄이 2.50달러로 표시되고 승수가 100이라면 단순 계약 대금은 250달러입니다.</p>
<div class="article-table-wrap"><table class="article-table"><thead><tr><th>항목</th><th>의미</th><th>확인할 점</th></tr></thead><tbody><tr><td>기초자산</td><td>옵션 가치의 기준이 되는 주식·ETF</td><td>티커가 정확한가</td></tr><tr><td>행사가격</td><td>사거나 팔 권리의 기준 가격</td><td>현재 주가와의 거리</td></tr><tr><td>만기일</td><td>계약이 끝나는 날짜</td><td>남은 시간과 이벤트</td></tr><tr><td>프리미엄</td><td>옵션의 시장가격</td><td>100배 계약금액과 수수료</td></tr></tbody></table></div>"""),
            ("손익은 방향만으로 결정되지 않는다", "pricing", """
<p>옵션 가격에는 내재가치와 시간가치가 포함됩니다. 기초자산 가격, 남은 시간, 내재변동성, 금리와 배당 등이 동시에 변합니다. 그래서 주가가 예상한 방향으로 움직였는데도 옵션 가격이 충분히 오르지 않는 일이 생깁니다.</p>
<p>초보자는 진입 전에 최대손실, 만기 손익분기점, 목표가, 종료 시점을 적어 두는 습관이 필요합니다. 옵션 매수의 최대손실은 일반적으로 지불한 프리미엄과 비용으로 제한되지만 전액 손실될 수 있습니다. 일부 옵션 매도 포지션은 손실이 매우 크거나 이론상 제한되지 않을 수 있습니다.</p>"""),
            ("초보자를 위한 학습 순서", "roadmap", """
<ol><li>콜과 풋의 권리와 매도자의 의무를 구분합니다.</li><li>행사가격·만기·프리미엄·승수를 읽습니다.</li><li>ITM, ATM, OTM과 내재가치·시간가치를 배웁니다.</li><li>옵션 체인의 거래량, 미결제약정, 호가 차이를 확인합니다.</li><li>손익도와 만기 손익분기점을 계산합니다.</li><li>소액의 모의거래로 주문과 청산 과정을 연습합니다.</li></ol>
<p>실제 주문 과정을 알고 싶다면 <a href="../how-to-trade-us-stock-options/">미국 주식 옵션 거래 방법</a>을, 전체 학습 계획은 <a href="../options-trading-guide-for-beginners/">초보자 옵션 거래 로드맵</a>을 이어서 읽으세요.</p>"""),
            ("위험을 줄이는 기본 원칙", "risk", """
<p>옵션은 적은 금액으로 큰 명목가치를 움직일 수 있어 손익 변화가 빠릅니다. 이해하지 못한 계약은 거래하지 않고, 한 번의 프리미엄 전액 손실이 계좌에 큰 영향을 주지 않도록 포지션 크기를 제한해야 합니다. 만기 직전에는 감마와 시간가치 변화가 커질 수 있다는 점도 기억하세요.</p>
<div class="article-callout"><strong>핵심:</strong> 옵션은 주식의 저렴한 대체품이 아닙니다. 가격 전망과 기간, 변동성, 유동성, 배정 가능성을 함께 관리해야 하는 별도의 계약입니다.</div>"""),
            ("다음 단계", "next", """
<p>이제 개념을 실제 주문 흐름과 연결할 차례입니다. <a href="../how-to-trade-us-stock-options/">옵션 거래 하는 법</a>에서 계좌 승인부터 청산까지 확인하고, <a href="../free-us-stock-options-course/">무료 미국 주식 옵션 강의 안내</a>에서 학습 과정을 시작하세요.</p>"""),
        ],
        "faqs": [
            ("미국 주식 옵션은 주식과 무엇이 다른가요?", "주식은 기업의 지분이지만 옵션은 정해진 조건으로 기초자산을 사거나 팔 수 있는 권리와 의무를 거래하는 만기 있는 계약입니다."),
            ("옵션 매수자는 투자금 전부를 잃을 수 있나요?", "네. 옵션이 가치 없이 만료되거나 가격이 크게 하락하면 지불한 프리미엄과 거래비용 전부를 잃을 수 있습니다."),
            ("처음부터 실제 돈으로 거래해야 하나요?", "아닙니다. 계약 구조와 주문 방식을 익힌 뒤 모의거래로 손익 변화를 관찰하는 방법이 초보자에게 유용합니다."),
        ],
    },
    {
        "slug": "what-are-us-stock-options",
        "title": "미국 주식 옵션이란? 계약 구조와 콜·풋 쉽게 이해하기",
        "short": "미국 주식 옵션이란?",
        "description": "미국 주식 옵션이 무엇인지 콜옵션, 풋옵션, 행사가격, 만기일, 프리미엄과 배정의 개념으로 쉽게 설명합니다.",
        "deck": "옵션은 주가 방향을 맞히는 티켓이 아니라 권리와 의무가 명확하게 정의된 계약입니다. 구조를 이해하면 옵션 체인이 훨씬 단순하게 보입니다.",
        "tag": "미국 주식 옵션 · 핵심 개념",
        "read": "10분",
        "image": "/assets/images/blog/what-is-buying-a-put-option.webp",
        "alt": "콜옵션과 풋옵션 계약 구조",
        "sections": [
            ("옵션 계약의 두 당사자", "parties", """
<p>모든 옵션 거래에는 매수자와 매도자가 있습니다. 매수자는 프리미엄을 지불하고 계약에 적힌 권리를 얻습니다. 매도자는 프리미엄을 받지만 매수자가 권리를 행사하고 자신에게 배정이 발생하면 계약 조건을 이행해야 합니다.</p>
<p>이 차이가 옵션 위험을 이해하는 출발점입니다. 콜 매수와 콜 매도는 같은 시장을 보더라도 손익 구조가 반대이며, 풋도 마찬가지입니다. “콜은 상승, 풋은 하락”이라는 한 문장만 외우면 매도자의 의무와 배정 위험을 놓치기 쉽습니다.</p>"""),
            ("콜옵션의 권리와 의무", "call", """
<p>콜옵션 매수자는 행사가격으로 기초자산을 살 권리를 가집니다. 예를 들어 주가가 100달러이고 105달러 콜을 매수했다면, 만기 시 주가가 105달러를 넘을수록 계약에 내재가치가 생깁니다. 그러나 매수자가 지불한 프리미엄까지 회수하려면 만기 손익분기점은 행사가격보다 높아집니다.</p>
<p>콜옵션 매도자는 배정 시 해당 가격에 주식을 인도할 의무를 질 수 있습니다. 주식을 이미 보유한 커버드콜인지, 보유하지 않은 네이키드 콜인지에 따라 위험과 담보 요구가 크게 달라집니다.</p>"""),
            ("풋옵션의 권리와 의무", "put", """
<p>풋옵션 매수자는 행사가격으로 기초자산을 팔 권리를 가집니다. 주가 하락에 대한 방향성 포지션이나 보유 주식의 하방 위험을 제한하는 보험 성격으로 사용할 수 있습니다. 만기 시 풋의 내재가치는 행사가격이 주가보다 높은 만큼 발생합니다.</p>
<p>풋옵션 매도자는 배정 시 기초자산을 행사가격에 매수할 의무를 질 수 있습니다. 받은 프리미엄만 보고 매도하면 큰 하락에서 상당한 손실과 자금 요구를 맞을 수 있으므로, 실제로 주식을 인수할 능력과 의향을 먼저 확인해야 합니다.</p>"""),
            ("행사가격·만기·프리미엄", "terms", """
<div class="article-table-wrap"><table class="article-table"><thead><tr><th>용어</th><th>쉬운 설명</th><th>왜 중요한가</th></tr></thead><tbody><tr><td>행사가격</td><td>계약상 매수·매도 기준 가격</td><td>내재가치와 손익분기점에 영향</td></tr><tr><td>만기일</td><td>옵션 권리가 끝나는 날짜</td><td>시간가치와 관리 기한을 결정</td></tr><tr><td>프리미엄</td><td>옵션을 사고파는 가격</td><td>매수 비용·매도 수입의 출발점</td></tr><tr><td>승수</td><td>표시 가격을 계약금액으로 바꾸는 수</td><td>표준 미국 주식 옵션은 흔히 100</td></tr></tbody></table></div>
<p>예를 들어 프리미엄이 3달러인 표준 계약 한 개의 단순 대금은 300달러입니다. 다만 조정 계약이나 다른 상품은 명세가 다를 수 있으므로 주문 전에 승수와 결제 방식을 확인해야 합니다.</p>"""),
            ("ITM·ATM·OTM", "moneyness", """
<p>현재 주가와 행사가격의 관계를 머니니스라고 합니다. 콜은 주가가 행사가격보다 높을 때 ITM, 풋은 주가가 행사가격보다 낮을 때 ITM입니다. 주가와 행사가가 비슷하면 ATM, 즉 외가격 상태를 OTM이라고 부릅니다.</p>
<p>머니니스는 현재 내재가치만 설명할 뿐 미래 수익을 보장하지 않습니다. OTM 옵션이 싸 보이더라도 필요한 가격 움직임이 크고 만기가 가까우면 전액 손실 가능성이 높아질 수 있습니다.</p>"""),
            ("행사, 배정, 청산", "exercise", """
<p>행사는 옵션 매수자가 계약의 권리를 사용하는 것이고, 배정은 옵션 매도자가 의무를 이행하도록 지정되는 과정입니다. 그러나 옵션에서 수익을 실현하기 위해 반드시 행사해야 하는 것은 아닙니다. 많은 포지션은 만기 전에 반대 주문으로 청산됩니다.</p>
<p>미국식 주식 옵션은 일반적으로 만기 전 행사될 수 있으므로 매도자는 조기 배정 가능성을 고려해야 합니다. 배당락일, 깊은 내가격 상태, 남은 시간가치 등이 조기 행사 판단에 영향을 줄 수 있습니다.</p>"""),
            ("옵션 구조를 배운 다음", "next", """
<p>계약을 이해했다면 <a href="../how-to-trade-us-stock-options/">미국 주식 옵션 거래 방법</a>으로 이동해 옵션 체인과 주문 과정을 배우세요. 전체 개념을 다시 연결하려면 <a href="../us-stock-options-guide/">미국 주식 옵션 기초 가이드</a>가 도움이 됩니다.</p>"""),
        ],
        "faqs": [
            ("콜옵션 매수자는 주식을 반드시 사야 하나요?", "아닙니다. 매수자는 권리를 가질 뿐 의무는 없습니다. 만기 전 옵션을 매도해 청산하는 것도 가능합니다."),
            ("옵션 가격 2달러는 계약 한 개에 2달러라는 뜻인가요?", "표준 승수가 100이면 보통 2달러 × 100 = 200달러가 단순 계약 대금입니다. 주문 전 계약 명세를 확인해야 합니다."),
            ("풋옵션을 매도하면 어떤 의무가 생기나요?", "배정될 경우 행사가격으로 기초자산을 매수해야 할 수 있습니다. 프리미엄보다 훨씬 큰 자금과 위험이 필요할 수 있습니다."),
        ],
    },
    {
        "slug": "how-to-trade-us-stock-options",
        "title": "미국 주식 옵션 거래 방법: 계좌 준비부터 청산까지",
        "short": "미국 주식 옵션 거래 방법",
        "description": "미국 주식 옵션 거래 방법을 계좌 승인, 옵션 체인, 만기와 행사가 선택, 지정가 주문, 포지션 관리와 청산 순서로 설명합니다.",
        "deck": "옵션 거래는 주문 버튼보다 준비 과정이 중요합니다. 거래 권한을 확인하고 계약을 읽은 뒤 손실 한도를 먼저 정하는 실전 흐름을 살펴봅니다.",
        "tag": "옵션 거래 하는 법 · 단계별 안내",
        "read": "12분",
        "image": "/assets/images/blog/how-to-buy-a-call-option.webp",
        "alt": "미국 주식 옵션 거래 과정을 보여주는 옵션 체인",
        "sections": [
            ("1. 옵션 거래가 가능한 계좌 확인", "account", """
<p>미국 주식 거래 계좌가 있다고 해서 옵션 권한이 자동으로 제공되는 것은 아닙니다. 브로커는 경험, 재무상태, 투자목적 등에 따라 옵션 거래 수준을 심사할 수 있습니다. 허용되는 전략과 담보 요구, 수수료, 환전 방식, 거래 가능 시간을 먼저 확인하세요.</p>
<p>브로커가 제공하는 위험고지와 계약 명세도 읽어야 합니다. 미국 상장 옵션은 상품별로 결제 방식과 만기 처리 규칙이 다를 수 있고, 한국 시간 기준 거래시간도 서머타임에 따라 달라질 수 있습니다.</p>"""),
            ("2. 거래 아이디어를 구체화", "thesis", """
<p>“오를 것 같다” 대신 목표 가격, 예상 기간, 판단 근거, 틀렸다고 인정할 조건을 적습니다. 옵션은 방향과 시간이 함께 작동하기 때문에 예상 움직임이 만기 이후에 발생하면 좋은 아이디어도 잘못된 계약 선택이 될 수 있습니다.</p>
<p>예상되는 실적 발표, 배당락일, 경제지표 같은 이벤트를 확인하세요. 이벤트 전에는 내재변동성이 높아질 수 있고 이벤트 이후 급격히 낮아지면 방향을 맞혀도 옵션 가치가 감소할 수 있습니다.</p>"""),
            ("3. 옵션 체인 읽기", "chain", """
<p>기초자산과 만기를 선택하면 행사가별 콜과 풋이 표시됩니다. 매수호가와 매도호가, 거래량, 미결제약정, 내재변동성, 델타 등을 비교하세요. 호가 차이가 넓으면 진입과 청산 비용이 커질 수 있습니다.</p>
<div class="article-callout"><strong>주문 전 점검:</strong> 티커, 콜·풋 구분, 만기일, 행사가, 계약 수, 승수, 총 프리미엄과 최대손실을 소리 내어 다시 확인하세요.</div>"""),
            ("4. 만기와 행사가 선택", "selection", """
<p>짧은 만기는 프리미엄이 낮아 보일 수 있지만 시간가치 감소가 빠르고 판단할 시간이 적습니다. 긴 만기는 더 많은 시간을 제공하지만 지불 프리미엄이 커질 수 있습니다. 예상 시나리오가 전개될 시간을 충분히 포함시키는 것이 출발점입니다.</p>
<p>행사가 선택에서는 “가장 싼 옵션”보다 필요한 주가 움직임, 델타, 손익분기점과 유동성을 함께 비교합니다. 먼 외가격 옵션은 작은 비용으로 큰 수익 가능성을 보여 주지만 가치 없이 만료될 가능성도 높을 수 있습니다.</p>"""),
            ("5. 손익과 포지션 크기 계산", "sizing", """
<div class="example-box"><strong>단순 예시</strong><ul><li>주가: 100달러</li><li>콜 행사가: 105달러</li><li>프리미엄: 주당 3달러</li><li>계약 승수: 100</li><li>한 계약 비용: 300달러</li><li>만기 손익분기점: 108달러</li><li>매수자의 최대손실: 300달러와 비용</li></ul></div>
<p>이 금액을 잃어도 전체 계좌와 생활에 영향을 주지 않는지 확인합니다. 여러 계약을 매수하면 위험도 같은 비율로 증가합니다. 옵션 매도는 단순 프리미엄보다 훨씬 큰 잠재 손실과 담보 요구가 생길 수 있습니다.</p>"""),
            ("6. 지정가 주문 사용", "order", """
<p>매수로 포지션을 열 때는 Buy to Open, 매도로 청산할 때는 Sell to Close를 사용합니다. 시장가 주문은 체결을 우선하지만 호가 차이가 넓은 옵션에서 불리한 가격으로 거래될 수 있습니다. 지정가는 지불할 최대 가격을 통제하는 데 도움이 됩니다.</p>
<p>주문이 체결되지 않는다고 무조건 가격을 따라가지 마세요. 기초자산과 옵션 호가는 계속 변하므로 처음 세운 위험·보상 기준이 무너지면 거래를 건너뛰는 것도 결정입니다.</p>"""),
            ("7. 포지션 관리와 청산", "manage", """
<p>진입 전에 이익 목표, 허용 손실, 시간 기준 종료일과 만기 처리 계획을 정합니다. 포지션을 보유하는 동안 주가뿐 아니라 남은 시간과 내재변동성, 호가를 확인하세요. 옵션은 만기 전에 매도하여 청산할 수 있으며 수익 실현을 위해 반드시 행사할 필요는 없습니다.</p>
<p>만기까지 방치하면 자동 행사, 배정, 주식 포지션 또는 예상보다 큰 자금 요구가 생길 수 있습니다. 브로커의 만기일 처리 규정을 확인하고 충분히 일찍 결정하세요.</p>"""),
            ("실전에 앞서", "next", """
<p><a href="../options-trading-guide-for-beginners/">초보자 옵션 거래 가이드</a>에서 4주 학습 순서를 확인하고, 준비가 되면 <a href="../free-us-stock-options-course/">무료 강의</a>에서 콜옵션 과정을 단계별로 시작하세요.</p>"""),
        ],
        "faqs": [
            ("미국 주식 옵션은 시장가로 주문해도 되나요?", "가능하지만 유동성이 낮고 호가 차이가 넓은 계약에서는 예상보다 불리하게 체결될 수 있어 지정가 주문이 가격 통제에 도움이 됩니다."),
            ("옵션을 만기까지 보유해야 하나요?", "아닙니다. 많은 옵션 포지션은 만기 전에 반대 주문으로 청산됩니다. 만기 처리 규칙은 브로커에서 확인해야 합니다."),
            ("주가 방향만 맞으면 수익이 나나요?", "반드시 그렇지 않습니다. 움직임의 크기와 시기, 지불 프리미엄, 시간가치 감소와 내재변동성 변화도 결과에 영향을 줍니다."),
        ],
    },
    {
        "slug": "options-trading-guide-for-beginners",
        "title": "초보자를 위한 옵션 거래 가이드: 무엇부터 공부해야 할까?",
        "short": "초보자 옵션 거래 가이드",
        "description": "옵션 거래 초보자가 계약 구조부터 손익, 옵션 체인, 위험관리와 모의거래까지 공부해야 할 순서를 4주 로드맵으로 정리합니다.",
        "deck": "처음부터 복잡한 전략을 외우지 마세요. 계약 한 개를 정확히 읽고 손익을 직접 계산하는 능력이 모든 옵션 전략의 기반입니다.",
        "tag": "옵션 초보 · 학습 로드맵",
        "read": "11분",
        "image": "/assets/images/blog/buying-call-options-risks-mistakes.webp",
        "alt": "초보자를 위한 옵션 거래 학습 로드맵",
        "sections": [
            ("초보자가 가장 먼저 버려야 할 오해", "myths", """
<p>옵션은 적은 돈으로 빠르게 큰 수익을 얻는 단축키가 아닙니다. 프리미엄이 낮은 계약은 싸서 좋은 것이 아니라, 큰 가격 움직임이나 짧은 시간 같은 어려운 조건이 반영되었을 수 있습니다. 높은 승률도 한 번의 큰 손실을 막아 주지 못합니다.</p>
<p>학습 목표는 전략 이름을 많이 아는 것이 아니라, 계약의 권리와 의무, 최대손실, 손익분기점, 만기 처리와 청산 방법을 설명할 수 있게 되는 것입니다.</p>"""),
            ("1주차: 계약 언어 익히기", "week1", """
<p>첫 주에는 콜, 풋, 행사가격, 만기일, 프리미엄, 승수, 행사와 배정을 학습합니다. 이어서 ITM·ATM·OTM, 내재가치와 시간가치를 구분합니다. 각 용어를 암기하기보다 한 계약 예시에서 직접 찾아보세요.</p>
<p><a href="../what-are-us-stock-options/">미국 주식 옵션이란?</a>에서 구조를 읽고, 콜 매수자와 콜 매도자의 권리·의무를 각각 한 문장으로 적어 보는 것이 좋습니다.</p>"""),
            ("2주차: 손익 구조 계산하기", "week2", """
<p>두 번째 주에는 롱 콜과 롱 풋의 최대이익, 최대손실, 만기 손익분기점을 계산합니다. 주가를 여러 값으로 바꾸어 만기 손익표를 만들어 보세요. 그다음 만기 전에는 시간가치와 변동성 때문에 실제 가격이 다를 수 있다는 점을 연결합니다.</p>
<p>옵션 매수는 손실이 프리미엄으로 제한되는 경우가 많지만 전액 손실 가능성이 있습니다. 옵션 매도는 받은 프리미엄보다 손실이 훨씬 커질 수 있으므로 별도의 담보와 위험 학습이 필요합니다.</p>"""),
            ("3주차: 옵션 체인과 주문", "week3", """
<p>세 번째 주에는 실제 옵션 체인을 열어 만기와 행사가를 바꾸며 프리미엄, 델타, 거래량, 미결제약정과 호가 차이가 어떻게 달라지는지 관찰합니다. 실제 주문을 제출하지 않아도 많은 것을 배울 수 있습니다.</p>
<p><a href="../how-to-trade-us-stock-options/">미국 주식 옵션 거래 방법</a>의 체크리스트를 이용해 티커부터 총 계약금액까지 확인하는 연습을 하세요. Buy to Open과 Sell to Close 같은 주문 효과를 혼동하지 않는 것이 중요합니다.</p>"""),
            ("4주차: 모의거래와 기록", "week4", """
<p>마지막 주에는 하나의 단순한 롱 콜 또는 롱 풋을 모의거래로 추적합니다. 진입 이유, 목표 가격, 만기, 선택한 행사가, 지불 프리미엄, 최대손실과 종료 조건을 기록합니다. 매일 주가와 옵션 가격이 왜 다르게 움직였는지 설명해 보세요.</p>
<p>결과보다 과정의 일관성을 평가해야 합니다. 우연히 수익이 났더라도 계획 없이 진입했다면 좋은 거래 습관이 아닙니다. 반대로 계획한 위험 안에서 종료했다면 손실 거래도 유용한 학습 자료가 됩니다.</p>"""),
            ("초보자가 자주 하는 실수", "mistakes", """
<ul><li>가장 저렴한 외가격 옵션만 선택합니다.</li><li>만기 손익분기점과 총 계약금액을 계산하지 않습니다.</li><li>실적 발표 전후의 변동성 변화를 무시합니다.</li><li>시장가 주문으로 넓은 호가 차이를 감수합니다.</li><li>한 거래에 계좌의 큰 비중을 사용합니다.</li><li>만기일의 자동 행사와 배정 규칙을 확인하지 않습니다.</li><li>손실 포지션을 계획 없이 계속 연장합니다.</li></ul>"""),
            ("실제 거래 전 체크리스트", "checklist", """
<div class="article-table-wrap"><table class="article-table"><thead><tr><th>질문</th><th>답할 수 있어야 하는 내용</th></tr></thead><tbody><tr><td>무엇을 거래하는가?</td><td>기초자산, 콜·풋, 만기, 행사가</td></tr><tr><td>얼마를 잃을 수 있는가?</td><td>최대손실과 계좌 대비 비중</td></tr><tr><td>무엇이 일어나야 수익인가?</td><td>목표 움직임, 기간, 손익분기점</td></tr><tr><td>언제 나올 것인가?</td><td>이익·손실·시간 종료 규칙</td></tr><tr><td>만기에 무슨 일이 생기는가?</td><td>청산, 행사, 배정과 자금 요구</td></tr></tbody></table></div>"""),
            ("무료로 학습 시작하기", "next", """
<p>준비된 순서대로 배우려면 <a href="../free-us-stock-options-course/">미국 주식 옵션 무료 강의</a>를 시작하세요. 먼저 <a href="../us-stock-options-guide/">종합 기초 가이드</a>를 북마크하면 학습 중 필요한 개념을 빠르게 다시 찾을 수 있습니다.</p>"""),
        ],
        "faqs": [
            ("옵션 초보자는 어떤 전략부터 시작해야 하나요?", "전략보다 계약 구조와 롱 콜·롱 풋의 정의된 손익을 먼저 학습하는 것이 좋습니다. 이해한 뒤 모의거래로 주문 흐름을 연습하세요."),
            ("옵션 공부에 얼마나 걸리나요?", "개인차가 있지만 핵심 용어, 손익 계산, 옵션 체인과 위험관리를 여러 주에 걸쳐 반복하는 편이 하루에 모든 전략을 외우는 것보다 효과적입니다."),
            ("모의거래만으로 충분한가요?", "모의거래는 구조와 절차 학습에 유용하지만 실제 체결, 감정과 유동성의 영향을 완전히 재현하지는 못합니다."),
        ],
    },
    {
        "slug": "free-us-stock-options-course",
        "title": "미국 주식 옵션 무료 강의: 초보자를 위한 단계별 학습 과정",
        "short": "미국 주식 옵션 무료 강의",
        "description": "미국 주식 옵션을 처음 배우는 사람을 위한 무료 강의입니다. 콜옵션 구조, 계약 선택, 손익, 위험관리와 실전 사례를 단계별로 학습하세요.",
        "deck": "무작정 거래하기 전에 콜옵션 한 계약을 처음부터 끝까지 이해하세요. Google 계정으로 무료 등록하면 학습 진도를 저장할 수 있습니다.",
        "tag": "무료 옵션 강의 · 학습 안내",
        "read": "8분",
        "image": "/assets/images/blog/option-greeks-explained.webp",
        "alt": "미국 주식 옵션 무료 온라인 강의",
        "sections": [
            ("이 무료 강의에서 배우는 것", "learn", """
<p>Options America의 첫 과정은 미국 주식 콜옵션을 중심으로 옵션 계약의 기본 구조를 단계별로 설명합니다. 단순히 상승 종목을 고르는 법이 아니라 계약을 읽고 비용과 위험을 계산하며 주문 전 확인해야 할 내용을 학습합니다.</p>
<ul><li>콜옵션 매수자가 얻는 권리와 제한된 기간</li><li>기초자산, 행사가격, 만기일과 프리미엄</li><li>표준 계약의 승수와 실제 계약 비용</li><li>ITM·ATM·OTM과 손익분기점</li><li>시간가치 감소와 변동성의 영향</li><li>진입 전 위험관리와 청산 계획</li></ul>"""),
            ("누구를 위한 과정인가", "audience", """
<p>미국 주식은 거래해 보았지만 옵션은 처음인 사람, 옵션 체인이 복잡하게 보이는 사람, 콜옵션을 샀는데 왜 주가와 같은 비율로 움직이지 않는지 이해하고 싶은 사람을 위한 입문 과정입니다.</p>
<p>특정 종목 추천이나 확정 수익을 제공하는 과정이 아닙니다. 옵션 거래의 구조와 위험을 스스로 판단할 수 있도록 교육하는 것이 목적입니다. 거래 경험이 있더라도 기초 개념을 다시 정리하는 용도로 사용할 수 있습니다.</p>"""),
            ("추천 학습 순서", "order", """
<ol><li><a href="../what-are-us-stock-options/">미국 주식 옵션의 계약 구조</a>를 읽습니다.</li><li><a href="../us-stock-options-guide/">기초 종합 가이드</a>로 핵심 용어를 연결합니다.</li><li>무료 Level 1 강의에서 콜옵션을 단계별로 학습합니다.</li><li><a href="../how-to-trade-us-stock-options/">거래 방법 체크리스트</a>로 주문 절차를 정리합니다.</li><li>모의거래에서 계약 하나의 가격 변화를 기록합니다.</li></ol>"""),
            ("등록과 진도 저장", "signup", """
<p>강의는 무료입니다. 시작 버튼을 누르면 Google 계정으로 가입 또는 로그인하는 화면이 열립니다. 로그인 후에는 학습 진행 상황을 저장하고 대시보드에서 수강 중인 과정을 다시 찾을 수 있습니다.</p>
<p><a class="btn btn-gold" href="/courses/options-trading-course-level-1-buying-call-option/">Google로 무료 강의 시작 →</a></p>
<p>로그인은 강의 진도와 학습 계정을 연결하기 위한 절차입니다. 결제 정보를 입력할 필요 없이 무료 과정부터 시작할 수 있습니다.</p>"""),
            ("강의를 듣기 전에 준비할 것", "prepare", """
<p>메모할 수 있는 문서와 계산기를 준비하세요. 실제 거래 계좌나 입금은 학습에 필요하지 않습니다. 각 예시에서 행사가격, 프리미엄, 승수, 최대손실과 손익분기점을 직접 계산하면 영상만 보는 것보다 이해가 빨라집니다.</p>
<div class="article-callout"><strong>학습 원칙:</strong> 이해하지 못한 옵션은 거래하지 마세요. 무료 강의의 목표는 빠른 주문이 아니라 계약을 정확히 설명할 수 있는 능력입니다.</div>"""),
            ("강의 이후의 학습", "after", """
<p>Level 1을 완료한 뒤에는 옵션 매도, 풋옵션, 변동성과 그릭스, 스프레드 전략으로 확장할 수 있습니다. 그러나 다음 단계로 넘어가기 전에 콜옵션의 최대손실, 만기 손익분기점과 청산 주문을 스스로 계산할 수 있는지 확인하세요.</p>
<p><a href="../options-trading-guide-for-beginners/">초보자 4주 학습 로드맵</a>을 이용하면 강의와 읽을거리를 순서대로 배치할 수 있습니다.</p>"""),
            ("지금 시작하기", "start", """
<p>미국 주식 옵션을 제대로 배우는 가장 좋은 출발점은 작은 계약을 서둘러 사는 것이 아니라, 한 계약이 어떻게 움직이고 언제 가치가 사라질 수 있는지 이해하는 것입니다.</p>
<p><a class="btn btn-gold" href="/courses/options-trading-course-level-1-buying-call-option/">무료 Level 1 과정 시작 →</a></p>"""),
        ],
        "faqs": [
            ("미국 주식 옵션 강의는 정말 무료인가요?", "네. Options America의 Level 1 입문 과정은 무료로 학습할 수 있으며 Google 계정으로 가입하면 진도를 저장할 수 있습니다."),
            ("실제 거래 계좌가 필요한가요?", "아닙니다. 개념과 계산을 학습하는 데 실제 거래 계좌나 입금은 필요하지 않습니다."),
            ("강의가 투자 종목을 추천하나요?", "아닙니다. 과정은 옵션 계약의 구조와 위험을 설명하는 교육 자료이며 개인 투자 조언이나 수익 보장을 제공하지 않습니다."),
        ],
    },
]


def schema(article: dict) -> str:
    article_url = f"{BASE}/ko/blog/{article['slug']}/"
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article["title"],
        "description": article["description"],
        "datePublished": PUBLISHED,
        "dateModified": PUBLISHED,
        "inLanguage": "ko-KR",
        "author": {"@type": "Organization", "name": "Options America"},
        "publisher": {"@type": "Organization", "name": "Options America"},
        "mainEntityOfPage": article_url,
        "image": f"{BASE}{article['image']}",
    }
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": "ko-KR",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in article["faqs"]
        ],
    }
    return "\n".join(
        f'<script type="application/ld+json">{json.dumps(value, ensure_ascii=False, separators=(",", ":"))}</script>'
        for value in (article_schema, faq_schema)
    )


def article_html(article: dict) -> str:
    url = f"{BASE}/ko/blog/{article['slug']}/"
    nav = """<header class="site-header"><div class="container nav"><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><nav><a href="/courses/">강의</a><a href="/learning-paths/beginner/">학습 경로</a><a href="/ko/blog/">한국어 블로그</a><a href="/blog/" lang="en">English</a></nav><a class="btn btn-gold" href="/courses/options-trading-course-level-1-buying-call-option/">무료 강의 시작</a></div></header>"""
    toc = "".join(f'<a href="#{sid}">{html.escape(title)}</a>' for title, sid, _ in article["sections"])
    sections = "\n".join(f'<h2 id="{sid}">{html.escape(title)}</h2>\n{body}' for title, sid, body in article["sections"])
    faq = "\n".join(f'<div class="faq-item"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></div>' for q, a in article["faqs"])
    related = "".join(
        f'<a href="../{item["slug"]}/"><span>{html.escape(item["tag"])}</span><strong>{html.escape(item["short"])}</strong></a>'
        for item in ARTICLES if item["slug"] != article["slug"]
    )
    footer = """<footer><div class="container footer-grid"><div><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><p>초보자부터 고급 과정까지 무료로 배우는 미국 옵션 교육 자료입니다.</p></div><div><h4>학습</h4><a href="/courses/">전체 강의</a><a href="/learning-paths/beginner/">초보자 경로</a></div><div><h4>한국어</h4><a href="/ko/blog/">한국어 블로그</a><a href="/ko/blog/us-stock-options-guide/">미국 주식 옵션 기초</a></div><div><h4>자료</h4><a href="/blog/" lang="en">English Blog</a><a href="/risk-disclaimer/">위험 고지</a></div></div><div class="container copyright">© <span data-current-year></span> Options America · 교육 목적의 콘텐츠이며 투자 조언이 아닙니다.</div></footer>"""
    return f"""<!doctype html>
<html lang="ko-KR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{html.escape(article['title'])} | Options America</title>
  <meta name="description" content="{html.escape(article['description'], quote=True)}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="ko_KR">
  <meta property="og:title" content="{html.escape(article['title'], quote=True)}">
  <meta property="og:description" content="{html.escape(article['description'], quote=True)}">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="Options America">
  <meta property="og:image" content="{BASE}{article['image']}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="../../../styles.css">
  <link rel="stylesheet" href="../../../blog/blog.css">
  <link rel="stylesheet" href="../ko-blog.css">
  <script src="/favicon.js"></script>
  {schema(article)}
</head>
<body>
  {nav}
  <main>
    <section class="article-hero"><div class="container"><div class="breadcrumbs"><a href="/">홈</a><span>›</span><a href="/ko/blog/">한국어 블로그</a><span>›</span><span>{html.escape(article['short'])}</span></div><p class="eyebrow">{html.escape(article['tag'])}</p><h1>{html.escape(article['title'])}</h1><p class="article-deck">{html.escape(article['deck'])}</p><div class="article-meta"><span>Options America</span><span>2026년 9월 14일 업데이트</span><span>{article['read']} 읽기</span></div></div></section>
    <div class="container article-layout">
      <article class="article-body">
        <img src="{article['image']}" alt="{html.escape(article['alt'], quote=True)}">
        {sections}
        <h2 id="faq">자주 묻는 질문</h2>
        {faq}
        <h2>같은 기초 과정의 다른 글</h2>
        <div class="ko-related">{related}</div>
        <div class="ko-sources"><strong>교육 참고자료</strong><p><a href="https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document" rel="noopener noreferrer">OCC — Characteristics and Risks of Standardized Options</a></p><p><a href="https://www.theocc.com/clearance-and-settlement/clearing/equity-options-product-specifications" rel="noopener noreferrer">OCC — Equity Options Product Specifications</a></p></div>
        <p class="article-disclaimer">옵션은 위험을 수반하며 모든 투자자에게 적합하지 않을 수 있습니다. 이 글은 교육 목적이며 투자, 세금 또는 법률 조언이 아닙니다. 거래 전 브로커가 제공하는 상품 명세와 공식 위험고지를 확인하세요.</p>
      </article>
      <aside class="article-sidebar"><div class="toc"><strong>이 글의 내용</strong>{toc}<a href="#faq">자주 묻는 질문</a></div><div class="course-cta"><strong>무료 Level 1 강의</strong><p>콜옵션의 구조, 계약 선택과 위험을 순서대로 학습하세요.</p><a class="btn btn-gold" href="{COURSE}">Google로 무료 시작 →</a></div></aside>
    </div>
  </main>
  {footer}
  <script>document.querySelectorAll('[data-current-year]').forEach(e=>e.textContent=new Date().getFullYear())</script>
</body>
</html>
"""


def index_html() -> str:
    cards = "\n".join(
        f'''<a class="post-card" href="{item['slug']}/"><img src="{item['image']}" alt="{html.escape(item['alt'], quote=True)}"><div class="post-card-copy"><span class="tag">{html.escape(item['tag'])}</span><h2>{html.escape(item['short'])}</h2><p>{html.escape(item['description'])}</p><strong>가이드 읽기 →</strong></div></a>'''
        for item in ARTICLES
    )
    item_list = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "미국 주식 옵션 초보자 학습 과정",
        "inLanguage": "ko-KR",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": item["short"], "url": f"{BASE}/ko/blog/{item['slug']}/"}
            for i, item in enumerate(ARTICLES, 1)
        ],
    }
    return f"""<!doctype html>
<html lang="ko-KR">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <title>미국 주식 옵션 무료 강의와 초보자 가이드 | Options America</title>
  <meta name="description" content="미국 주식 옵션을 처음 배우는 초보자를 위한 한국어 가이드입니다. 옵션 기초, 계약 구조, 거래 방법과 무료 강의를 순서대로 학습하세요.">
  <link rel="canonical" href="{BASE}/ko/blog/">
  <meta property="og:locale" content="ko_KR"><meta property="og:type" content="website"><meta property="og:title" content="미국 주식 옵션 무료 강의와 초보자 가이드"><meta property="og:description" content="미국 주식 옵션 기초부터 거래 방법까지 순서대로 배우는 한국어 학습 허브입니다."><meta property="og:url" content="{BASE}/ko/blog/"><meta property="og:image" content="{BASE}/assets/images/courses/legacy/options-trading-course-level-1-buying-call-option.png">
  <link rel="stylesheet" href="../../styles.css"><link rel="stylesheet" href="../../blog/blog.css"><link rel="stylesheet" href="ko-blog.css"><script src="/favicon.js"></script>
  <script type="application/ld+json">{json.dumps(item_list, ensure_ascii=False, separators=(",", ":"))}</script>
</head>
<body>
  <header class="site-header"><div class="container nav"><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><nav><a href="/courses/">강의</a><a href="/learning-paths/beginner/">학습 경로</a><a href="/ko/blog/" aria-current="page">한국어 블로그</a><a href="/blog/" lang="en">English</a></nav><a class="btn btn-gold" href="{COURSE}">무료 강의 시작</a></div></header>
  <main><section class="blog-hero ko-blog-hero"><div class="container"><p class="eyebrow">미국 주식 옵션 · 한국어 학습 허브</p><h1>미국 주식 옵션, 기초부터 순서대로 배우세요</h1><p>콜옵션과 풋옵션의 계약 구조부터 옵션 체인, 주문, 손익과 위험관리까지. 초보자가 길을 잃지 않도록 다섯 개의 가이드를 하나의 과정으로 연결했습니다.</p><div class="ko-hero-actions"><a class="btn btn-gold" href="{COURSE}">Google로 무료 강의 시작</a><a class="btn ko-secondary" href="us-stock-options-guide/">종합 가이드 먼저 읽기</a></div></div></section>
  <section class="blog-main"><div class="container"><div class="section-heading"><div><p class="eyebrow blue">Cluster 1 · Beginner</p><h2>미국 주식 옵션 초보자 과정</h2><p>아래 순서대로 읽으면 개념에서 실제 주문 준비까지 자연스럽게 이어집니다.</p></div></div><div class="blog-grid ko-blog-grid">{cards}</div></div></section></main>
  <footer><div class="container footer-grid"><div><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><p>초보자부터 고급 과정까지 무료로 배우는 미국 옵션 교육 자료입니다.</p></div><div><h4>학습</h4><a href="/courses/">전체 강의</a><a href="/learning-paths/beginner/">초보자 경로</a></div><div><h4>한국어</h4><a href="/ko/blog/">한국어 블로그</a><a href="/ko/blog/us-stock-options-guide/">미국 주식 옵션 기초</a></div><div><h4>자료</h4><a href="/blog/" lang="en">English Blog</a><a href="/risk-disclaimer/">위험 고지</a></div></div><div class="container copyright">© <span data-current-year></span> Options America · 교육 목적의 콘텐츠이며 투자 조언이 아닙니다.</div></footer>
  <script>document.querySelectorAll('[data-current-year]').forEach(e=>e.textContent=new Date().getFullYear())</script>
</body></html>
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(index_html(), encoding="utf-8")
    for article in ARTICLES:
        directory = OUT / article["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(article_html(article), encoding="utf-8")
    print(f"Built Korean cluster 1: {len(ARTICLES)} articles plus hub")


if __name__ == "__main__":
    main()
