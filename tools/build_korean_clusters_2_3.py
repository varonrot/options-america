#!/usr/bin/env python3
"""Build Korean SEO clusters 2 and 3 for Options America."""

from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://options-america.com"
OUT = ROOT / "ko" / "blog"
COURSE = "/courses/options-trading-course-level-1-buying-call-option/"
PUBLISHED = "2026-09-14"
OCC_ODD = "https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document"
OCC_COVERED = "https://www.theocc.com/newsroom/insights/2018/08-15-get-the-facts-about-covered-calls"
CBOE_101 = "https://www.cboe.com/optionsinstitute/courses/options101/"


CLUSTERS = [
    {
        "number": 2,
        "slug": "call-put-options",
        "label": "콜옵션·풋옵션",
        "title": "콜옵션과 풋옵션: 뜻, 차이와 손익 구조",
        "description": "콜옵션 뜻과 풋옵션 뜻부터 두 계약의 차이, ITM·ATM·OTM, 행사가격·만기·프리미엄까지 순서대로 배우는 한국어 가이드입니다.",
        "intro": "콜과 풋은 옵션의 가장 기본적인 두 계약입니다. 매수자의 권리와 매도자의 의무, 만기 손익을 각각 이해한 뒤 옵션 체인의 핵심 용어까지 연결하세요.",
        "image": "/assets/images/blog/call-delta-vs-put-delta.webp",
        "articles": [
            {
                "slug": "call-option-meaning",
                "title": "콜옵션 뜻: 매수·매도 권리와 손익 구조 쉽게 이해하기",
                "short": "콜옵션 뜻",
                "description": "콜옵션 뜻을 매수자의 권리, 매도자의 의무, 프리미엄, 손익분기점과 만기 손익 예시로 쉽게 설명합니다.",
                "deck": "콜옵션은 단순히 ‘주가가 오르면 수익’인 상품이 아닙니다. 누가 권리를 사고 누가 의무를 부담하는지부터 확인해야 손익 구조가 보입니다.",
                "tag": "콜 옵션 뜻 · 기초",
                "read": "10분",
                "image": "/assets/images/blog/how-to-buy-a-call-option.webp",
                "alt": "콜옵션 매수와 매도 구조를 설명하는 화면",
                "sections": [
                    ("콜옵션 뜻을 한 문장으로", "meaning", "<p><strong>콜옵션</strong>은 매수자가 정해진 만기까지 기초자산을 행사가격으로 살 수 있는 권리를 얻는 계약입니다. 매수자는 이 권리를 위해 프리미엄을 지불하며, 권리를 사용할 의무는 없습니다.</p><p>반대로 콜옵션 매도자는 프리미엄을 받는 대신 배정될 경우 행사가격에 기초자산을 인도해야 할 수 있습니다. 따라서 같은 콜옵션이라도 매수와 매도의 위험은 완전히 다릅니다.</p>"),
                    ("콜옵션 매수자의 손익", "buyer", "<p>콜 매수자는 기초자산 상승에서 이익 가능성을 얻습니다. 만기 시 주가가 행사가격보다 높으면 내재가치가 생기지만, 지불한 프리미엄까지 회수하려면 주가가 만기 손익분기점을 넘어야 합니다.</p><div class=\"example-box\"><strong>예시</strong><ul><li>행사가격: 100달러</li><li>프리미엄: 4달러</li><li>승수: 100</li><li>계약 비용: 400달러</li><li>만기 손익분기점: 104달러</li><li>일반적인 최대손실: 프리미엄 400달러와 비용</li></ul></div>"),
                    ("콜옵션 매도자의 의무", "seller", "<p>콜 매도자는 매수자가 아니라 의무를 부담하는 쪽입니다. 주식을 보유한 상태에서 콜을 매도하면 커버드콜, 주식 없이 매도하면 네이키드 콜로 분류될 수 있으며 후자는 손실이 이론상 제한되지 않을 수 있습니다.</p><p>받은 프리미엄은 최대이익을 제한하지만 기초자산이 크게 오르면 매도자의 손실이나 기회비용은 커집니다. 담보 요구와 배정 처리도 주문 전에 확인해야 합니다.</p>"),
                    ("주가가 올라도 손실이 날 수 있는 이유", "pricing", "<p>옵션 가격은 주가뿐 아니라 남은 시간, 내재변동성, 금리와 배당의 영향을 받습니다. 예상한 상승이 늦거나 작으면 시간가치 감소를 이기지 못할 수 있습니다.</p><p>특히 실적 발표 뒤에는 내재변동성이 급격히 낮아질 수 있습니다. 방향을 맞혔더라도 옵션 가격 상승이 제한되는 이른바 변동성 축소를 고려해야 합니다.</p>"),
                    ("콜옵션을 확인하는 순서", "checklist", "<ol><li>기초자산과 계약 승수를 확인합니다.</li><li>만기일과 행사가격을 확인합니다.</li><li>프리미엄 총액과 최대손실을 계산합니다.</li><li>만기 손익분기점과 필요한 주가 움직임을 계산합니다.</li><li>거래량, 미결제약정과 호가 차이를 살핍니다.</li><li>청산일과 만기 처리 계획을 정합니다.</li></ol>"),
                    ("다음 학습", "next", "<p><a href=\"../put-option-meaning/\">풋옵션 뜻</a>을 이어서 읽은 뒤 <a href=\"../call-vs-put-options/\">콜옵션과 풋옵션 차이</a>에서 두 계약을 같은 기준으로 비교하세요.</p>"),
                ],
                "faqs": [("콜옵션을 사면 주식을 반드시 사야 하나요?", "아닙니다. 콜옵션 매수자는 권리를 가질 뿐 의무는 없으며 만기 전에 옵션을 매도해 청산할 수 있습니다."), ("콜옵션 매수의 최대손실은 얼마인가요?", "일반적인 롱 콜에서는 지불한 프리미엄과 거래비용이 최대손실입니다. 계약 조건을 반드시 확인해야 합니다."), ("주가가 행사가격보다 높으면 무조건 수익인가요?", "아닙니다. 만기 기준으로 지불한 프리미엄까지 회수하려면 주가가 행사가격과 프리미엄을 합한 손익분기점을 넘어야 합니다.")],
            },
            {
                "slug": "put-option-meaning",
                "title": "풋옵션 뜻: 하락 위험과 매수·매도 손익 구조",
                "short": "풋옵션 뜻",
                "description": "풋옵션 뜻과 매수자의 매도 권리, 매도자의 매수 의무, 손익분기점, 헤지와 투기 목적의 차이를 설명합니다.",
                "deck": "풋옵션은 하락에 베팅하는 도구로만 보면 절반만 이해한 것입니다. 주식 위험을 제한하는 보험과 비슷한 역할도 하지만 비용과 만기가 있습니다.",
                "tag": "풋 옵션 뜻 · 기초",
                "read": "10분",
                "image": "/assets/images/blog/what-is-buying-a-put-option.webp",
                "alt": "풋옵션 권리와 손익 구조",
                "sections": [
                    ("풋옵션 뜻을 한 문장으로", "meaning", "<p><strong>풋옵션</strong>은 매수자가 정해진 만기까지 기초자산을 행사가격으로 팔 수 있는 권리를 얻는 계약입니다. 매수자는 프리미엄을 지불하고 하락 시 가치가 증가할 가능성을 확보합니다.</p><p>풋 매도자는 프리미엄을 받는 대신 배정될 경우 행사가격에 기초자산을 매수해야 할 수 있습니다. 주가가 크게 하락하면 받은 프리미엄보다 훨씬 큰 손실이 발생할 수 있습니다.</p>"),
                    ("풋옵션 매수 손익 예시", "buyer", "<div class=\"example-box\"><strong>예시</strong><ul><li>풋 행사가격: 100달러</li><li>프리미엄: 5달러</li><li>계약 비용: 500달러</li><li>만기 손익분기점: 95달러</li><li>만기 주가 85달러일 때 내재가치: 주당 15달러</li></ul></div><p>만기 주가가 95달러 아래로 내려가야 단순 손익이 플러스로 전환됩니다. 만기 전 가격은 남은 시간과 내재변동성 때문에 이 계산과 다를 수 있습니다.</p>"),
                    ("보호용 풋과 방향성 풋", "uses", "<p>주식을 보유하면서 풋을 매수하면 일정 기간 하방 가격을 제한하는 보호용 풋으로 사용할 수 있습니다. 보험료처럼 프리미엄을 지불하기 때문에 주가가 오르거나 횡보하면 전체 수익률을 낮출 수 있습니다.</p><p>주식 없이 풋만 매수하면 하락 방향성 포지션입니다. 손실은 일반적으로 프리미엄으로 제한되지만 예상 하락의 크기와 시점이 충분하지 않으면 전액 손실될 수 있습니다.</p>"),
                    ("풋 매도의 위험", "seller", "<p>풋 매도는 ‘주식을 싸게 사는 방법’으로 소개되기도 하지만 하락 위험이 사라지는 것은 아닙니다. 배정되면 시장가격보다 높은 행사가격으로 주식을 인수해야 할 수 있습니다.</p><p>현금담보 풋이라도 기초자산이 큰 폭으로 하락하면 손실이 큽니다. 실제 인수 의향, 충분한 현금, 종목 집중도와 만기 처리 규정을 먼저 점검하세요.</p>"),
                    ("풋옵션 체크리스트", "checklist", "<ul><li>헤지인지 방향성 거래인지 목적을 적습니다.</li><li>행사가와 프리미엄으로 만기 손익분기점을 계산합니다.</li><li>만기까지 필요한 하락 폭을 확인합니다.</li><li>보유 주식 수와 풋 계약 승수가 일치하는지 봅니다.</li><li>풋 매도라면 배정 시 필요한 현금을 계산합니다.</li></ul>"),
                    ("다음 학습", "next", "<p><a href=\"../call-option-meaning/\">콜옵션 뜻</a>과 비교한 다음 <a href=\"../itm-atm-otm-options/\">ITM·ATM·OTM</a>에서 현재 주가와 행사가의 관계를 익히세요.</p>"),
                ],
                "faqs": [("풋옵션은 공매도와 같은가요?", "아닙니다. 풋옵션은 만기와 행사가가 있는 계약이며 일반적인 풋 매수의 손실은 프리미엄으로 제한됩니다."), ("풋옵션은 주가가 내려가면 항상 오르나요?", "항상 그렇지는 않습니다. 남은 시간, 내재변동성, 하락 폭과 호가 등 여러 요인이 가격에 영향을 줍니다."), ("풋옵션 매도자는 무엇을 해야 하나요?", "배정될 경우 행사가격으로 기초자산을 매수해야 할 수 있으므로 필요한 현금과 손실 가능성을 준비해야 합니다.")],
            },
            {
                "slug": "call-vs-put-options",
                "title": "콜옵션 풋옵션 차이: 권리·의무·손익 비교표",
                "short": "콜옵션 풋옵션 차이",
                "description": "콜옵션과 풋옵션의 차이를 매수자 권리, 매도자 의무, 시장 전망, 손익분기점과 위험 기준으로 비교합니다.",
                "deck": "콜은 상승, 풋은 하락이라는 암기만으로는 부족합니다. 매수와 매도를 구분해 네 가지 기본 포지션을 비교해야 실제 위험을 이해할 수 있습니다.",
                "tag": "콜 옵션 풋 옵션 뜻 · 비교",
                "read": "11분",
                "image": "/assets/images/blog/call-delta-vs-put-delta.webp",
                "alt": "콜옵션과 풋옵션 차이 비교",
                "sections": [
                    ("콜과 풋의 핵심 차이", "comparison", "<div class=\"article-table-wrap\"><table class=\"article-table\"><thead><tr><th>구분</th><th>콜옵션</th><th>풋옵션</th></tr></thead><tbody><tr><td>매수자 권리</td><td>행사가에 살 권리</td><td>행사가에 팔 권리</td></tr><tr><td>매수자의 기본 전망</td><td>상승</td><td>하락 또는 하방 보호</td></tr><tr><td>만기 내재가치</td><td>주가 - 행사가</td><td>행사가 - 주가</td></tr><tr><td>매도자 의무</td><td>배정 시 인도</td><td>배정 시 매수</td></tr></tbody></table></div>"),
                    ("롱 콜과 롱 풋", "long", "<p>롱 콜은 상승 가능성에 프리미엄을 지불하고 참여하며, 롱 풋은 하락 가능성 또는 보험 기능에 프리미엄을 지불합니다. 두 포지션 모두 일반적으로 최대손실이 지불 프리미엄으로 제한됩니다.</p><p>그러나 만기가 있어 방향만 맞히는 것으로는 부족합니다. 필요한 움직임이 정해진 시간 안에 발생하고 프리미엄과 시간가치 감소를 넘어야 합니다.</p>"),
                    ("숏 콜과 숏 풋", "short", "<p>숏 콜은 프리미엄을 받는 대신 상승 시 인도 의무를 부담합니다. 주식 없이 매도한 콜은 매우 큰 손실이 가능하며, 주식을 보유한 커버드콜도 상승 이익이 제한됩니다.</p><p>숏 풋은 배정 시 주식을 행사가에 매수할 의무를 부담합니다. 최대이익은 받은 프리미엄이지만 기초자산 하락 시 큰 손실이 가능합니다.</p>"),
                    ("손익분기점 비교", "breakeven", "<p>만기 기준 롱 콜 손익분기점은 행사가격에 지불 프리미엄을 더한 값입니다. 롱 풋 손익분기점은 행사가격에서 프리미엄을 뺀 값입니다.</p><p>이 계산은 만기 시점의 단순 구조입니다. 만기 전에는 시간가치와 변동성이 남아 있으므로 옵션 시장가격은 내재가치만으로 결정되지 않습니다.</p>"),
                    ("어떤 계약이 적합한가", "choice", "<p>선택은 상승·하락 전망뿐 아니라 보유 주식, 기간, 변동성, 손실 한도와 목적에 달려 있습니다. 하락을 예상해도 풋 프리미엄이 매우 높으면 위험·보상은 불리할 수 있습니다.</p><div class=\"article-callout\"><strong>중요:</strong> 옵션 매수와 옵션 매도는 반대 주문이 아니라 서로 다른 위험 구조입니다. 전략 이름보다 권리와 의무를 먼저 확인하세요.</div>"),
                    ("다음 학습", "next", "<p><a href=\"../option-strike-expiration-premium/\">행사가격·만기·프리미엄</a>을 배우고 실제 옵션 체인에서 같은 종목의 콜과 풋을 비교해 보세요.</p>"),
                ],
                "faqs": [("콜옵션과 풋옵션 중 무엇이 더 위험한가요?", "계약 종류보다 매수인지 매도인지, 담보가 있는지, 만기와 포지션 크기가 위험을 결정합니다."), ("콜옵션과 풋옵션을 동시에 살 수 있나요?", "가능합니다. 같은 행사가와 만기의 콜과 풋을 매수하는 스트래들 같은 조합이 있지만 두 프리미엄과 복합 위험을 이해해야 합니다."), ("콜과 풋의 손익분기점은 어떻게 계산하나요?", "만기 기준 롱 콜은 행사가+프리미엄, 롱 풋은 행사가-프리미엄입니다.")],
            },
            {
                "slug": "itm-atm-otm-options",
                "title": "ITM ATM OTM 뜻: 옵션 내가격·등가격·외가격 구분법",
                "short": "ITM·ATM·OTM 뜻",
                "description": "옵션의 ITM, ATM, OTM 뜻을 콜과 풋별로 구분하고 내재가치, 시간가치, 델타와 행사 가능성의 관계를 설명합니다.",
                "deck": "ITM·ATM·OTM은 옵션이 싸거나 비싸다는 평가가 아니라 현재 주가와 행사가격의 관계를 나타내는 언어입니다.",
                "tag": "옵션 머니니스 · 용어",
                "read": "9분",
                "image": "/assets/images/blog/call-option-intrinsic-value-time-value.webp",
                "alt": "ITM ATM OTM 옵션 머니니스",
                "sections": [
                    ("머니니스란 무엇인가", "meaning", "<p>머니니스는 현재 기초자산 가격과 옵션 행사가격의 관계입니다. 현재 내재가치가 있는지 설명하지만 거래가 수익인지, 앞으로 수익이 날지는 알려 주지 않습니다.</p><p>같은 행사가에서도 콜과 풋의 ITM·OTM 방향은 반대입니다. 이를 혼동하면 옵션 체인을 잘못 읽기 쉽습니다.</p>"),
                    ("콜옵션 ITM·ATM·OTM", "call", "<div class=\"article-table-wrap\"><table class=\"article-table\"><thead><tr><th>현재 주가 100달러</th><th>상태</th><th>내재가치</th></tr></thead><tbody><tr><td>90 콜</td><td>ITM</td><td>10달러</td></tr><tr><td>100 콜</td><td>ATM</td><td>약 0</td></tr><tr><td>110 콜</td><td>OTM</td><td>0</td></tr></tbody></table></div>"),
                    ("풋옵션 ITM·ATM·OTM", "put", "<div class=\"article-table-wrap\"><table class=\"article-table\"><thead><tr><th>현재 주가 100달러</th><th>상태</th><th>내재가치</th></tr></thead><tbody><tr><td>110 풋</td><td>ITM</td><td>10달러</td></tr><tr><td>100 풋</td><td>ATM</td><td>약 0</td></tr><tr><td>90 풋</td><td>OTM</td><td>0</td></tr></tbody></table></div>"),
                    ("내재가치와 시간가치", "value", "<p>옵션 프리미엄은 내재가치와 시간가치로 나눌 수 있습니다. ITM 옵션은 내재가치를 포함할 수 있고, ATM과 OTM 옵션의 프리미엄은 대체로 시간가치로 구성됩니다.</p><p>시간이 지나고 다른 조건이 같다면 시간가치는 감소하는 경향이 있습니다. OTM 옵션은 만기에 내재가치가 없으면 가치 없이 만료됩니다.</p>"),
                    ("ITM이 안전하고 OTM이 위험한가", "risk", "<p>ITM 옵션은 델타가 더 높고 내재가치를 포함할 수 있지만 프리미엄도 큽니다. OTM 옵션은 비용이 낮아 보여도 수익이 되려면 더 큰 가격 움직임이 필요할 수 있습니다.</p><p>머니니스 하나만으로 계약을 고르지 말고 만기, 유동성, 변동성, 손익분기점과 전체 포지션 크기를 함께 비교해야 합니다.</p>"),
                    ("다음 학습", "next", "<p><a href=\"../option-strike-expiration-premium/\">행사가격과 만기 선택</a>으로 이동해 머니니스를 실제 계약 선택 과정에 연결하세요.</p>"),
                ],
                "faqs": [("ATM은 정확히 주가와 행사가가 같아야 하나요?", "시장에서는 현재 주가와 가장 가까운 행사가를 ATM이라고 부르는 경우가 많습니다."), ("OTM 옵션은 가치가 없나요?", "현재 내재가치는 없지만 만기 전에는 시간가치가 있어 시장가격이 존재할 수 있습니다."), ("ITM 옵션은 만기에 자동 행사되나요?", "브로커와 청산기관의 기준에 따라 자동 행사될 수 있지만 계좌와 만기 처리 규정을 직접 확인해야 합니다.")],
            },
            {
                "slug": "option-strike-expiration-premium",
                "title": "옵션 행사가격·만기일·프리미엄: 계약 선택 핵심",
                "short": "행사가격·만기·프리미엄",
                "description": "옵션 행사가격, 만기일과 프리미엄의 뜻과 관계를 설명하고 계약 선택 전 확인해야 할 위험과 유동성 기준을 정리합니다.",
                "deck": "같은 종목의 옵션도 행사가와 만기가 다르면 전혀 다른 계약입니다. 낮은 프리미엄만 보고 선택하지 말고 필요한 움직임과 시간을 계산하세요.",
                "tag": "옵션 계약 · 선택 기준",
                "read": "11분",
                "image": "/assets/images/blog/choose-bull-call-spread-strikes.webp",
                "alt": "옵션 행사가격 만기 프리미엄 선택",
                "sections": [
                    ("행사가격의 역할", "strike", "<p>행사가격은 옵션 매수자가 기초자산을 사거나 팔 수 있는 계약 기준 가격입니다. 현재 주가와의 거리에 따라 ITM·ATM·OTM이 결정되며 내재가치와 델타에도 영향을 줍니다.</p><p>행사가가 멀수록 프리미엄이 낮아 보일 수 있지만 목표 주가까지 필요한 움직임은 커집니다. ‘싼 옵션’과 ‘좋은 거래’는 같은 뜻이 아닙니다.</p>"),
                    ("만기일의 역할", "expiration", "<p>만기일은 옵션 권리가 끝나는 날짜입니다. 짧은 만기는 비용이 낮을 수 있지만 시간가치 감소가 빠르고 판단할 시간이 적습니다. 긴 만기는 더 많은 시간을 주는 대신 프리미엄이 커질 수 있습니다.</p><p>예상 이벤트가 발생할 날짜보다 너무 이른 만기를 선택하면 방향이 맞아도 기회를 얻지 못합니다. 만기일의 자동 행사와 거래 종료 시각도 브로커에서 확인하세요.</p>"),
                    ("프리미엄은 무엇으로 결정되나", "premium", "<p>프리미엄에는 현재 내재가치와 미래 가능성에 대한 시간가치가 반영됩니다. 주가, 행사가, 남은 시간, 내재변동성, 금리와 배당이 동시에 영향을 줍니다.</p><p>표준 미국 주식 옵션의 표시 가격은 일반적으로 주당 기준입니다. 프리미엄 2.50달러와 승수 100이면 단순 계약 대금은 250달러입니다.</p>"),
                    ("세 요소를 함께 비교하는 법", "together", "<div class=\"article-table-wrap\"><table class=\"article-table\"><thead><tr><th>선택</th><th>장점처럼 보이는 점</th><th>확인할 위험</th></tr></thead><tbody><tr><td>짧은 만기</td><td>낮은 비용</td><td>빠른 시간가치 감소</td></tr><tr><td>긴 만기</td><td>더 많은 시간</td><td>큰 프리미엄</td></tr><tr><td>먼 OTM</td><td>낮은 가격</td><td>큰 필요 움직임</td></tr><tr><td>깊은 ITM</td><td>높은 델타</td><td>큰 자본과 스프레드</td></tr></tbody></table></div>"),
                    ("주문 전 최종 확인", "checklist", "<ul><li>티커와 콜·풋을 확인합니다.</li><li>정확한 만기일과 행사가를 확인합니다.</li><li>승수를 적용한 총 계약금액을 계산합니다.</li><li>손익분기점과 최대손실을 적습니다.</li><li>호가 차이와 거래량을 확인합니다.</li><li>만기 전에 청산할 기준을 정합니다.</li></ul>"),
                    ("다음 학습", "next", "<p>기초 용어를 익혔다면 <a href=\"../../covered-call/\">커버드콜 학습 과정</a>에서 주식과 콜옵션을 결합하는 첫 전략을 살펴보세요.</p>"),
                ],
                "faqs": [("행사가격은 내가 원하는 숫자로 정할 수 있나요?", "아닙니다. 거래소에 상장된 행사가격 중에서 선택합니다."), ("만기가 길수록 항상 더 좋은가요?", "아닙니다. 더 많은 시간을 제공하지만 프리미엄과 자본 사용이 커질 수 있어 목적과 위험에 맞춰야 합니다."), ("옵션 프리미엄이 낮으면 위험도 낮나요?", "낮은 비용은 최대손실 금액을 줄일 수 있지만 가치 없이 만료될 확률이나 필요한 가격 움직임이 더 클 수 있습니다.")],
            },
        ],
    },
    {
        "number": 3,
        "slug": "covered-call",
        "label": "커버드콜",
        "title": "커버드콜 전략: 수익 구조, 위험과 운용 방법",
        "description": "커버드콜 뜻부터 수익·손실, 행사가와 만기 선택, 배정·배당, 장단점과 실수까지 설명하는 한국어 학습 과정입니다.",
        "intro": "커버드콜은 주식을 보유하면서 콜옵션을 매도해 프리미엄을 받는 전략입니다. 현금흐름만 보지 말고 상승 제한과 주식 하락 위험을 함께 이해하세요.",
        "image": "/assets/images/blog/covered-call-income-potential.webp",
        "articles": [
            {
                "slug": "covered-call-strategy",
                "title": "커버드콜 뜻과 전략 구조: 초보자 완전 가이드",
                "short": "커버드콜 뜻과 구조",
                "description": "커버드콜 뜻, 주식 100주와 콜옵션 매도의 결합, 프리미엄 수입, 상승 제한과 하락 위험을 초보자 관점에서 설명합니다.",
                "deck": "커버드콜은 이자를 받는 상품이 아니라 주식 상승 가능성 일부를 프리미엄과 교환하는 옵션 전략입니다.",
                "tag": "커버드콜 뜻 · 종합 가이드",
                "read": "12분",
                "image": "/assets/images/blog/covered-call-income-potential.webp",
                "alt": "커버드콜 전략의 주식과 콜옵션 구조",
                "sections": [
                    ("커버드콜 뜻", "meaning", "<p><strong>커버드콜</strong>은 기초자산 주식을 보유하면서 그 주식에 대한 콜옵션을 매도하는 전략입니다. 미국 표준 주식 옵션 한 계약이 일반적으로 100주를 기준으로 하므로 보통 주식 100주당 콜 한 계약을 매도합니다.</p><p>‘커버드’라는 말은 배정될 때 인도할 주식을 이미 보유하고 있다는 뜻입니다. 네이키드 콜보다 의무를 충족할 자산이 있지만 주식의 하락 위험까지 사라지는 것은 아닙니다.</p>"),
                    ("왜 커버드콜을 사용하는가", "purpose", "<p>주요 목적은 콜 매도 프리미엄 수입, 목표 매도가 설정, 주식 취득원가 일부 완화입니다. 주가가 횡보하거나 완만하게 상승할 것이라는 전망에서 고려할 수 있습니다.</p><p>강한 상승이 예상되면 단순 주식 보유보다 불리할 수 있습니다. 행사가 위의 상승 이익을 포기할 수 있기 때문입니다.</p>"),
                    ("전략 구성 예시", "example", "<div class=\"example-box\"><strong>단순 예시</strong><ul><li>주식 100주 매수 가격: 50달러</li><li>55 콜 한 계약 매도</li><li>받은 프리미엄: 주당 2달러, 총 200달러</li><li>만기 최대 단순이익: 주가 상승 500달러 + 프리미엄 200달러</li><li>하락 손익분기점: 주당 48달러</li></ul></div><p>수수료, 세금과 만기 전 옵션 가치 변화는 제외한 교육용 예시입니다.</p>"),
                    ("수익과 위험의 교환", "tradeoff", "<p>받은 프리미엄은 작은 하락을 완충하지만 급락을 막는 보호 장치가 아닙니다. 주식이 크게 하락하면 손실은 프리미엄보다 훨씬 커질 수 있습니다.</p><p>반대로 주식이 크게 상승하면 콜 배정으로 행사가에 매도될 수 있어 추가 상승을 누리지 못합니다. 현금흐름과 상방 제한을 동시에 평가해야 합니다.</p>"),
                    ("커버드콜이 맞지 않는 경우", "when-not", "<ul><li>주식을 어떤 가격에서도 팔고 싶지 않을 때</li><li>단기 급등 가능성이 크다고 판단할 때</li><li>주식 하락 위험을 감당할 수 없을 때</li><li>배정과 배당 일정을 관리할 시간이 없을 때</li><li>세금 영향을 확인하지 않았을 때</li></ul>"),
                    ("다음 학습", "next", "<p><a href=\"../covered-call-profit-loss/\">커버드콜 수익·손실 계산</a>으로 이동해 만기 시나리오를 숫자로 확인하세요.</p>"),
                ],
                "faqs": [("커버드콜은 원금이 보장되나요?", "아닙니다. 기초주식이 하락하면 받은 프리미엄보다 훨씬 큰 손실이 발생할 수 있습니다."), ("주식 100주 없이 커버드콜을 할 수 있나요?", "일반적인 주식 커버드콜은 콜 한 계약당 인도 가능한 주식 100주를 보유하는 구조입니다. 다른 구조는 별도 위험이 있습니다."), ("커버드콜은 상승장에서 좋은가요?", "급등장에서는 상승 이익이 행사가 부근에서 제한되어 단순 주식 보유보다 뒤처질 수 있습니다.")],
            },
            {
                "slug": "covered-call-profit-loss",
                "title": "커버드콜 수익·손실과 손익분기점 계산법",
                "short": "커버드콜 수익·손실",
                "description": "커버드콜 최대이익, 손익분기점, 주가 상승·횡보·하락 시 손익을 계산하고 프리미엄과 기회비용을 설명합니다.",
                "deck": "커버드콜의 프리미엄은 수익의 전부가 아닙니다. 주식 손익과 콜 매도 손익을 합쳐 전체 포지션으로 계산해야 합니다.",
                "tag": "커버드콜 수익 · 계산",
                "read": "11분",
                "image": "/assets/images/blog/covered-call-assignment-explained.webp",
                "alt": "커버드콜 만기 손익 그래프 설명",
                "sections": [
                    ("전체 포지션으로 계산하기", "total", "<p>커버드콜은 주식 매수와 콜 매도 두 구성요소로 이루어집니다. 프리미엄만 수익으로 기록하면 주식 가격 변화와 상방 제한을 놓칩니다.</p><p>만기 손익은 주식의 매수가격, 콜 행사가격, 받은 순프리미엄, 계약 수와 수수료를 함께 사용해 계산합니다.</p>"),
                    ("최대이익 계산", "max-profit", "<p>주식 매수가보다 높은 행사가의 콜을 매도했다면 만기 최대 단순이익은 ‘행사가−주식 매수가+받은 프리미엄’에 주식 수를 곱한 값입니다.</p><div class=\"example-box\"><strong>50달러에 100주, 55 콜을 2달러에 매도</strong><ul><li>주가 상승 이익: 5 × 100 = 500달러</li><li>프리미엄: 2 × 100 = 200달러</li><li>최대 단순이익: 700달러</li></ul></div>"),
                    ("손익분기점 계산", "breakeven", "<p>단순 손익분기점은 주식 매수가에서 받은 주당 프리미엄을 뺀 값입니다. 예시에서는 50−2=48달러입니다.</p><p>프리미엄은 2달러의 완충만 제공합니다. 주가가 35달러로 하락하면 프리미엄을 받았더라도 큰 손실이 남습니다.</p>"),
                    ("세 가지 만기 시나리오", "scenarios", "<div class=\"article-table-wrap\"><table class=\"article-table\"><thead><tr><th>만기 주가</th><th>결과</th><th>단순 손익</th></tr></thead><tbody><tr><td>60달러</td><td>55에 배정 가능</td><td>+700달러</td></tr><tr><td>52달러</td><td>콜 무가치, 주식 보유</td><td>+400달러</td></tr><tr><td>45달러</td><td>콜 무가치, 주식 하락</td><td>-300달러</td></tr></tbody></table></div>"),
                    ("표면 수익률의 함정", "yield", "<p>프리미엄을 주식 가치로 나눈 비율을 연환산해 매우 높은 수익률처럼 표시하기도 합니다. 그러나 같은 프리미엄이 매번 반복된다는 보장은 없고 주가 하락, 변동성 변화와 배정을 무시할 수 없습니다.</p><p>세금, 거래비용, 매수·매도 호가 차이와 주식의 배당도 실제 결과에 영향을 줍니다.</p>"),
                    ("다음 학습", "next", "<p><a href=\"../covered-call-strike-expiration/\">행사가와 만기 선택</a>에서 수익 상한과 배정 가능성을 어떻게 조정하는지 살펴보세요.</p>"),
                ],
                "faqs": [("커버드콜의 최대손실은 프리미엄으로 제한되나요?", "아닙니다. 주식이 0에 가까워지면 주식 가치 대부분을 잃을 수 있고 프리미엄은 일부만 완충합니다."), ("커버드콜 손익분기점은 어떻게 계산하나요?", "단순 계산은 주식 매수가에서 받은 주당 순프리미엄을 뺍니다."), ("주가가 행사가 위로 오르면 더 이상 손실인가요?", "보통 최대이익에 도달하지만 단순 주식 보유와 비교하면 추가 상승을 포기하는 기회비용이 발생합니다.")],
            },
            {
                "slug": "covered-call-strike-expiration",
                "title": "커버드콜 행사가격과 만기 선택: 델타·수익·배정",
                "short": "커버드콜 행사가·만기",
                "description": "커버드콜 행사가격과 만기 선택 시 프리미엄, 상승 여지, 델타, 배정 가능성, 유동성과 이벤트를 비교하는 방법입니다.",
                "deck": "가장 높은 프리미엄을 주는 콜이 항상 최선은 아닙니다. 받고 싶은 수입과 포기할 상승 폭, 주식을 팔 의향을 함께 정해야 합니다.",
                "tag": "커버드콜 운용 · 계약 선택",
                "read": "12분",
                "image": "/assets/images/blog/covered-call-risks-mistakes.webp",
                "alt": "커버드콜 행사가격과 만기 선택",
                "sections": [
                    ("먼저 목표 매도가를 정한다", "target", "<p>콜을 고르기 전에 주식을 실제로 매도해도 괜찮은 가격을 정합니다. 해당 가격보다 낮은 행사가를 선택하면 프리미엄은 커질 수 있지만 원하지 않는 가격에 주식이 배정될 수 있습니다.</p><p>커버드콜은 목표 매도가를 설정하고 기다리는 구조로 생각할 수 있지만, 중간에 주가가 변하면 그 목표가 여전히 적절한지 다시 판단해야 합니다.</p>"),
                    ("행사가에 따른 차이", "strike", "<div class=\"article-table-wrap\"><table class=\"article-table\"><thead><tr><th>행사가</th><th>일반적 특성</th><th>교환</th></tr></thead><tbody><tr><td>ATM 부근</td><td>상대적으로 큰 프리미엄</td><td>낮은 상승 여지</td></tr><tr><td>약간 OTM</td><td>중간 프리미엄</td><td>일부 상승 여지</td></tr><tr><td>먼 OTM</td><td>작은 프리미엄</td><td>더 큰 상승 여지</td></tr></tbody></table></div>"),
                    ("델타를 참고하는 법", "delta", "<p>델타는 기초자산 가격 변화에 대한 옵션 가격 민감도를 나타냅니다. 일부 투자자는 델타를 만기 ITM 가능성의 거친 참고치로 사용하지만 정확한 확률이나 보장은 아닙니다.</p><p>델타 하나만 보고 선택하지 말고 유동성, 이벤트, 변동성, 남은 시간과 주식 매도 의향을 함께 확인해야 합니다.</p>"),
                    ("짧은 만기와 긴 만기", "expiration", "<p>짧은 만기는 시간가치 감소가 빠르고 포지션을 자주 관리해야 합니다. 긴 만기는 더 큰 프리미엄을 받을 수 있지만 주식 상승을 더 오래 제한하고 시장 변화에 대응하기 어려울 수 있습니다.</p><p>월간 수익률을 기계적으로 반복할 수 있다고 가정하지 마세요. 옵션 가격과 시장 환경은 매 만기마다 달라집니다.</p>"),
                    ("이벤트와 유동성 확인", "events", "<p>실적 발표 전에는 프리미엄이 높아질 수 있지만 주가 갭 위험도 커집니다. 배당락일 부근에는 깊은 ITM 콜의 조기 배정 가능성을 주의해야 합니다.</p><p>호가 차이가 넓고 거래량이 적은 옵션은 진입과 청산 비용이 커질 수 있습니다. 가능하면 지정가 주문으로 가격을 통제하세요.</p>"),
                    ("다음 학습", "next", "<p><a href=\"../covered-call-assignment-dividends/\">배정과 배당</a>에서 만기 전 주식을 잃을 수 있는 상황을 확인하세요.</p>"),
                ],
                "faqs": [("커버드콜은 어떤 델타를 선택해야 하나요?", "정답은 없습니다. 원하는 프리미엄, 상승 여지와 배정 가능성에 따라 달라지며 델타는 여러 참고 지표 중 하나입니다."), ("매주 콜을 매도하면 수익이 더 좋은가요?", "보장되지 않습니다. 잦은 거래는 비용과 관리 부담을 늘리고 급등·급락 위험에 더 자주 노출될 수 있습니다."), ("실적 발표 전에 커버드콜을 해도 되나요?", "가능하지만 프리미엄이 높은 만큼 큰 가격 변동과 상승 제한 위험도 커질 수 있습니다.")],
            },
            {
                "slug": "covered-call-assignment-dividends",
                "title": "커버드콜 배정과 배당: 조기 배정은 언제 발생할까?",
                "short": "커버드콜 배정·배당",
                "description": "커버드콜의 행사와 배정, 미국식 옵션의 조기 배정, 배당락일과 시간가치의 관계, 만기 전 관리 방법을 설명합니다.",
                "deck": "콜 만기일까지 기다려야만 배정되는 것은 아닙니다. 미국식 주식 옵션은 만기 전에도 행사될 수 있어 배당 일정과 남은 시간가치를 확인해야 합니다.",
                "tag": "커버드콜 관리 · 배정",
                "read": "10분",
                "image": "/assets/images/blog/covered-call-early-assignment-dividends.webp",
                "alt": "커버드콜 조기 배정과 배당 일정",
                "sections": [
                    ("행사와 배정의 차이", "terms", "<p>행사는 콜 매수자가 주식을 행사가에 살 권리를 사용하는 것입니다. 배정은 콜 매도자에게 주식을 인도할 의무가 지정되는 과정입니다.</p><p>커버드콜 매도자는 주식을 보유하고 있으므로 배정되면 일반적으로 해당 주식이 행사가에 매도됩니다. 배정 여부를 매도자가 선택할 수는 없습니다.</p>"),
                    ("조기 배정이 가능한 이유", "early", "<p>미국식 주식 옵션은 만기 전에도 행사될 수 있습니다. 정확한 시점은 예측할 수 없으며 콜이 깊은 ITM이고 남은 시간가치가 매우 작을 때 가능성이 커질 수 있습니다.</p><p>만기일까지 시간이 남았다는 이유만으로 배정이 없다고 가정하면 안 됩니다. 계좌에서 옵션과 주식 상태를 정기적으로 확인하세요.</p>"),
                    ("배당락일과 콜옵션", "dividend", "<p>콜 매수자는 주식을 보유하지 않으면 배당을 받지 못합니다. 배당을 받기 위해 콜을 행사할 경제적 유인이 생길 수 있어 배당락일 전 조기 배정 위험을 점검해야 합니다.</p><p>대체로 예상 배당과 남은 시간가치를 비교하지만 이는 확정 공식이 아닙니다. 브로커의 안내와 옵션 가격을 확인해야 합니다.</p>"),
                    ("배정되면 무슨 일이 생기나", "result", "<p>콜 한 계약이 배정되면 일반적으로 주식 100주가 행사가에 매도됩니다. 받은 프리미엄은 유지되며 주식 매도에 따른 세금과 손익이 발생할 수 있습니다.</p><p>주식을 계속 보유하고 싶다면 배정 위험이 커지기 전에 콜을 되사서 청산하거나 다른 계약으로 롤링하는 방법을 검토할 수 있지만 추가 비용과 새로운 위험이 생깁니다.</p>"),
                    ("만기 전 관리 체크리스트", "checklist", "<ul><li>콜이 ITM인지 확인합니다.</li><li>남은 시간가치와 매수 비용을 확인합니다.</li><li>배당락일과 예상 배당을 확인합니다.</li><li>주식을 행사가에 팔아도 괜찮은지 다시 판단합니다.</li><li>세금과 계좌 규정을 확인합니다.</li><li>청산·롤링·배정 수용 중 계획을 정합니다.</li></ul>"),
                    ("다음 학습", "next", "<p><a href=\"../covered-call-risks-mistakes/\">커버드콜 위험과 실수</a>에서 배정 외에 놓치기 쉬운 위험을 정리하세요.</p>"),
                ],
                "faqs": [("커버드콜은 만기일에만 배정되나요?", "아닙니다. 미국식 주식 옵션은 만기 전에도 행사될 수 있어 조기 배정이 가능합니다."), ("배정되면 받은 프리미엄을 돌려줘야 하나요?", "일반적으로 받은 프리미엄은 유지되지만 주식이 행사가에 매도되고 세금·수수료가 발생할 수 있습니다."), ("배당을 받기 전에 주식이 배정될 수 있나요?", "네. 배당락일 전 깊은 ITM 콜 등에서 조기 배정 위험이 커질 수 있습니다.")],
            },
            {
                "slug": "covered-call-risks-mistakes",
                "title": "커버드콜 장단점과 위험: 초보자가 피할 실수 8가지",
                "short": "커버드콜 장단점·실수",
                "description": "커버드콜 장단점, 주식 급락과 상승 제한, 조기 배정, 세금, 유동성 위험과 초보자가 자주 하는 실수를 설명합니다.",
                "deck": "프리미엄이 들어오면 안전해 보이지만 커버드콜의 핵심 위험은 그대로 보유한 주식과 포기한 상승 가능성입니다.",
                "tag": "커버드콜 위험 · 실수",
                "read": "12분",
                "image": "/assets/images/blog/bull-call-spread-vs-covered-call.webp",
                "alt": "커버드콜 장단점과 위험 분석",
                "sections": [
                    ("커버드콜의 장점", "advantages", "<ul><li>콜 매도 프리미엄으로 현금흐름을 만들 수 있습니다.</li><li>받은 프리미엄만큼 취득원가를 일부 완화합니다.</li><li>원하는 목표 매도가를 정하는 데 활용할 수 있습니다.</li><li>횡보·완만한 상승 환경에서 단순 보유보다 유리할 수 있습니다.</li></ul><p>장점은 시장 환경과 계약 선택에 따라 달라지며 수익을 보장하지 않습니다.</p>"),
                    ("커버드콜의 단점", "disadvantages", "<ul><li>주식 급등 시 행사가 위의 상승 이익이 제한됩니다.</li><li>주식 급락 위험은 대부분 그대로 남습니다.</li><li>배정, 만기와 배당 일정을 관리해야 합니다.</li><li>거래비용과 세금이 수익을 줄일 수 있습니다.</li></ul>"),
                    ("가장 큰 오해: 프리미엄은 보호막", "downside", "<p>프리미엄은 작은 하락만 완충합니다. 50달러 주식에서 2달러를 받았더라도 주가가 30달러가 되면 주당 18달러의 단순 손실이 남습니다.</p><p>급락을 걱정한다면 커버드콜만으로 충분한 보호가 되는지 다시 검토해야 합니다. 커버드콜은 주로 수입 전략이지 큰 하락에 대한 보험이 아닙니다.</p>"),
                    ("초보자의 실수 8가지", "mistakes", "<ol><li>프리미엄만 보고 품질이 낮은 주식을 매수합니다.</li><li>팔고 싶지 않은 주식에 콜을 매도합니다.</li><li>주식 수보다 많은 콜을 매도합니다.</li><li>실적 발표와 배당락일을 확인하지 않습니다.</li><li>세금 영향을 무시합니다.</li><li>유동성이 낮은 옵션을 시장가로 거래합니다.</li><li>손실 주식을 프리미엄으로 회복하려 계속 매도합니다.</li><li>롤링을 손실 제거로 착각합니다.</li></ol>"),
                    ("롤링은 새로운 거래", "rolling", "<p>롤링은 기존 콜을 되사고 다른 행사가나 만기의 콜을 새로 매도하는 두 거래입니다. 신용으로 롤링하더라도 기존 손실이 사라지는 것은 아닙니다.</p><p>새 계약의 최대이익, 손익분기점, 기간과 배정 위험을 처음부터 다시 계산해야 합니다. 계획 없이 계속 롤링하면 주식과 옵션 위험이 장기간 묶일 수 있습니다.</p>"),
                    ("사용 전 최종 질문", "checklist", "<div class=\"article-callout\"><strong>주문 전 질문:</strong> 이 주식을 계속 보유하고 싶은가, 행사가에 팔아도 괜찮은가, 주가가 30% 하락해도 감당할 수 있는가, 배정과 세금을 이해했는가?</div><p>모두 명확히 답할 수 없다면 먼저 <a href=\"../covered-call-strategy/\">커버드콜 구조</a>와 <a href=\"../covered-call-profit-loss/\">손익 계산</a>으로 돌아가세요.</p>"),
                ],
                "faqs": [("커버드콜은 안전한 전략인가요?", "네이키드 콜보다 의무를 충족할 주식을 보유하지만 주식 급락, 상승 제한과 배정 위험이 있어 안전이나 원금 보장을 의미하지 않습니다."), ("커버드콜로 매달 고정 수익을 얻을 수 있나요?", "아닙니다. 프리미엄과 주가, 변동성, 배정 여부가 계속 변하므로 고정 수익은 보장되지 않습니다."), ("롤링하면 손실을 피할 수 있나요?", "보장되지 않습니다. 롤링은 기존 옵션을 청산하고 새 옵션을 여는 거래이며 비용과 새로운 위험이 생깁니다.")],
            },
        ],
    },
]


PRACTICE = {
    "call-option-meaning": """<p>옵션 체인에서 같은 만기의 95·100·105 콜을 나란히 놓고 프리미엄과 델타를 비교해 보세요. 현재 주가를 100달러로 가정한 뒤 각 계약의 만기 손익분기점을 계산하면 낮은 프리미엄이 왜 더 큰 주가 움직임을 요구하는지 확인할 수 있습니다.</p><p>그다음 주가가 5달러 상승하는 시점을 내일, 한 달 후, 만기일로 바꾸어 생각하세요. 같은 방향이라도 남은 시간과 변동성에 따라 옵션 결과가 달라질 수 있다는 점이 콜옵션 학습의 핵심입니다. 계산 결과와 실제 옵션 호가가 다른 이유도 메모해 두면 좋습니다.</p>""",
    "put-option-meaning": """<p>주식 100주를 100달러에 보유한 상황과 주식 없이 95 풋만 매수한 상황을 따로 계산해 보세요. 만기 주가를 110·95·80달러로 바꾸면 보호용 풋은 주식 손실을 제한하는 대신 프리미엄 비용을 부담하고, 방향성 풋은 독립적인 하락 포지션이라는 차이가 드러납니다.</p><p>풋 매도도 같은 표에 추가해 배정 시 필요한 현금을 계산하세요. 프리미엄 수입만 기록하지 말고 주가가 50% 하락했을 때의 손실과 계좌 집중도를 적어야 실제 위험을 볼 수 있습니다.</p>""",
    "call-vs-put-options": """<p>네 칸으로 된 표를 만들어 롱 콜, 숏 콜, 롱 풋, 숏 풋을 적고 각 칸에 권리 또는 의무, 최대이익, 최대손실과 기본 전망을 써 보세요. 같은 콜이나 풋이라도 매수와 매도에 따라 손익이 반대라는 사실을 가장 빠르게 익히는 방법입니다.</p><p>이후 동일한 종목·만기·주가에서 콜과 풋 호가를 관찰하세요. 배당, 금리, 행사가와 선도 가격 관계 때문에 단순히 두 프리미엄이 같아야 한다고 가정하면 안 됩니다. 초보 단계에서는 정확한 가격 모형보다 계약의 권리와 손익 방향을 먼저 설명할 수 있어야 합니다.</p>""",
    "itm-atm-otm-options": """<p>현재 주가가 100달러인 가상의 종목에서 90부터 110까지 행사가를 적고 콜과 풋의 ITM·ATM·OTM을 각각 표시하세요. 그다음 각 계약의 내재가치를 계산하면 콜과 풋의 방향이 반대라는 점이 명확해집니다.</p><p>실제 옵션 체인에서는 프리미엄에서 내재가치를 빼 시간가치를 구해 보세요. 만기가 다른 계약을 비교하면 더 긴 만기에 왜 시간가치가 더 많이 포함될 수 있는지 관찰할 수 있습니다. 다만 호가가 넓은 계약의 중간가격은 실제 체결가격과 다를 수 있습니다.</p><p>마지막으로 주가를 5달러씩 올리고 내리면서 각 계약의 머니니스가 어떻게 바뀌는지 다시 표시하세요. 오늘의 OTM 계약이 내일 ITM이 될 수 있고 그 반대도 가능하므로, 머니니스는 고정된 상품 등급이 아니라 계속 변하는 현재 상태라는 점을 익힐 수 있습니다.</p>""",
    "option-strike-expiration-premium": """<p>한 종목에 대해 가까운 만기와 먼 만기, ATM과 OTM을 조합한 네 계약을 골라 총비용, 손익분기점, 델타와 호가 차이를 표로 만드세요. 가장 싼 계약이 가장 작은 가격 움직임을 요구하는지 확인하면 대부분 그렇지 않다는 것을 알 수 있습니다.</p><p>계약을 선택한 이유를 ‘가격이 싸서’가 아니라 예상 목표가, 예상 날짜와 허용 손실로 설명해 보세요. 이 세 가지가 계약의 만기와 행사가에 연결되지 않으면 주문하지 않는 규칙을 세우는 것이 좋습니다.</p>""",
    "covered-call-strategy": """<p>보유 주식의 현재 가격, 평균 매수가와 실제로 팔아도 괜찮은 목표 가격을 먼저 적으세요. 그 목표에 가까운 콜의 프리미엄을 확인한 뒤 주가가 급등·횡보·20% 하락하는 세 시나리오에서 주식과 옵션의 합산 손익을 계산합니다.</p><p>계산 결과를 단순 주식 보유와 비교하면 커버드콜의 교환이 분명해집니다. 횡보에서는 프리미엄이 도움이 될 수 있지만 급등에서는 상승을 포기하고 급락에서는 손실을 일부만 완충합니다. 이 비교 없이 월 프리미엄만 보면 전략의 목적을 잘못 이해하기 쉽습니다.</p>""",
    "covered-call-profit-loss": """<p>예시의 만기 주가를 30달러부터 70달러까지 5달러 간격으로 바꾸어 손익표를 만들어 보세요. 행사가 이상에서는 손익이 더 증가하지 않고, 손익분기점 아래에서는 주식 하락이 프리미엄을 넘어서는 모양을 확인할 수 있습니다.</p><p>같은 표에 단순 주식 100주 손익을 추가하면 커버드콜의 상대 성과를 볼 수 있습니다. 커버드콜이 이익인 상황에서도 단순 보유보다 적게 벌 수 있고, 둘 다 손실이지만 커버드콜의 손실이 조금 작을 수도 있습니다. ‘수익’과 ‘상대적으로 유리함’을 구분하세요.</p>""",
    "covered-call-strike-expiration": """<p>현재 주가보다 5%, 10%, 15% 높은 세 행사가를 비교하고 각 계약의 프리미엄, 델타, 최대이익과 배정 시 매도가를 적으세요. 프리미엄이 커질수록 포기하는 상승 여지가 어떻게 달라지는지 숫자로 확인할 수 있습니다.</p><p>그다음 7일, 30일, 60일 만기를 비교하되 프리미엄을 단순 연환산하지 마세요. 거래 횟수, 호가 차이, 실적 발표와 배당 일정, 주식을 제한하는 기간까지 함께 기록해야 공정한 비교가 됩니다.</p>""",
    "covered-call-assignment-dividends": """<p>보유 콜의 현재 시장가격에서 내재가치를 빼 남은 시간가치를 계산하고 예상 배당과 비교하는 연습을 하세요. 이 계산은 조기 배정을 확정하지 않지만 어떤 계약을 더 면밀히 관리해야 하는지 판단하는 데 도움이 됩니다.</p><p>배정될 경우의 주식 매도대금, 실현손익, 세금 검토 항목과 이후 포트폴리오 비중을 미리 적어 두세요. 주식을 팔고 싶지 않다는 판단은 배정된 뒤에는 늦을 수 있으므로 배당락일과 만기 전에 계획을 세워야 합니다.</p>""",
    "covered-call-risks-mistakes": """<p>최근 보유 종목의 가장 큰 일일 하락과 상승 구간을 찾아 당시 커버드콜이 있었다고 가정해 보세요. 하락에서는 프리미엄이 전체 손실의 얼마만큼만 막았는지, 상승에서는 행사가 위로 포기한 이익이 얼마인지 계산하면 양쪽 위험이 구체적으로 보입니다.</p><p>거래 일지에는 받은 프리미엄 외에 주식 매수가, 목표 매도가, 최대 허용 하락, 배당락일, 실적일, 청산 비용과 세금 확인 여부를 남기세요. 월별 프리미엄 합계만 기록하는 일지는 커버드콜의 진짜 성과와 위험을 왜곡할 수 있습니다.</p>""",
}


def schemas(cluster: dict, article: dict) -> str:
    url = f"{BASE}/ko/blog/{cluster['slug']}/{article['slug']}/"
    values = [
        {"@context": "https://schema.org", "@type": "Article", "headline": article["title"], "description": article["description"], "datePublished": PUBLISHED, "dateModified": PUBLISHED, "inLanguage": "ko-KR", "author": {"@type": "Organization", "name": "Options America"}, "publisher": {"@type": "Organization", "name": "Options America"}, "mainEntityOfPage": url, "image": f"{BASE}{article['image']}"},
        {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": "ko-KR", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in article["faqs"]]},
    ]
    return "\n".join(f'<script type="application/ld+json">{json.dumps(v, ensure_ascii=False, separators=(",", ":"))}</script>' for v in values)


def header() -> str:
    return f'<header class="site-header"><div class="container nav"><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><nav><a href="/courses/">강의</a><a href="/learning-paths/beginner/">학습 경로</a><a href="/ko/blog/">한국어 블로그</a><a href="/blog/" lang="en">English</a></nav><a class="btn btn-gold" href="{COURSE}">무료 강의 시작</a></div></header>'


def footer() -> str:
    return '<footer><div class="container footer-grid"><div><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><p>초보자부터 고급 과정까지 무료로 배우는 미국 옵션 교육 자료입니다.</p></div><div><h4>학습</h4><a href="/courses/">전체 강의</a><a href="/learning-paths/beginner/">초보자 경로</a></div><div><h4>한국어</h4><a href="/ko/blog/">한국어 블로그</a><a href="/ko/blog/call-put-options/">콜·풋 옵션</a><a href="/ko/blog/covered-call/">커버드콜</a><a href="/ko/blog/option-greeks/">옵션 그릭스</a></div><div><h4>자료</h4><a href="/blog/" lang="en">English Blog</a><a href="/risk-disclaimer/">위험 고지</a></div></div><div class="container copyright">© <span data-current-year></span> Options America · 교육 목적의 콘텐츠이며 투자 조언이 아닙니다.</div></footer>'


def article_html(cluster: dict, article: dict) -> str:
    url = f"{BASE}/ko/blog/{cluster['slug']}/{article['slug']}/"
    toc = "".join(f'<a href="#{sid}">{html.escape(title)}</a>' for title, sid, _ in article["sections"])
    toc += '<a href="#practice">실전 학습 노트</a>'
    sections = "\n".join(f'<h2 id="{sid}">{html.escape(title)}</h2>\n{body}' for title, sid, body in article["sections"])
    sections += f'<h2 id="practice">실전 학습 노트</h2>{PRACTICE[article["slug"]]}'
    faq = "\n".join(f'<div class="faq-item"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></div>' for q, a in article["faqs"])
    related = "".join(f'<a href="../{a["slug"]}/"><span>{html.escape(a["tag"])}</span><strong>{html.escape(a["short"])}</strong></a>' for a in cluster["articles"] if a["slug"] != article["slug"])
    sources = f'<div class="ko-sources"><strong>교육 참고자료</strong><p><a href="{OCC_ODD}" rel="noopener noreferrer">OCC — Characteristics and Risks of Standardized Options</a></p><p><a href="{CBOE_101}" rel="noopener noreferrer">Cboe Options Institute — Options 101</a></p>'
    if cluster["number"] == 3:
        sources += f'<p><a href="{OCC_COVERED}" rel="noopener noreferrer">OIC/OCC — Get the Facts About Covered Calls</a></p>'
    sources += '</div>'
    return f'''<!doctype html>
<html lang="ko-KR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(article['title'])} | Options America</title><meta name="description" content="{html.escape(article['description'], quote=True)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="article"><meta property="og:locale" content="ko_KR"><meta property="og:title" content="{html.escape(article['title'], quote=True)}"><meta property="og:description" content="{html.escape(article['description'], quote=True)}"><meta property="og:url" content="{url}"><meta property="og:site_name" content="Options America"><meta property="og:image" content="{BASE}{article['image']}"><meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/styles.css"><link rel="stylesheet" href="/blog/blog.css"><link rel="stylesheet" href="/ko/blog/ko-blog.css"><script src="/favicon.js"></script>{schemas(cluster, article)}</head>
<body>{header()}<main><section class="article-hero"><div class="container"><div class="breadcrumbs"><a href="/">홈</a><span>›</span><a href="/ko/blog/">한국어 블로그</a><span>›</span><a href="/ko/blog/{cluster['slug']}/">{html.escape(cluster['label'])}</a><span>›</span><span>{html.escape(article['short'])}</span></div><p class="eyebrow">{html.escape(article['tag'])}</p><h1>{html.escape(article['title'])}</h1><p class="article-deck">{html.escape(article['deck'])}</p><div class="article-meta"><span>Options America</span><span>2026년 9월 14일 업데이트</span><span>{article['read']} 읽기</span></div></div></section>
<div class="container article-layout"><article class="article-body"><img src="{article['image']}" alt="{html.escape(article['alt'], quote=True)}">{sections}<h2 id="faq">자주 묻는 질문</h2>{faq}<h2>같은 과정의 다른 글</h2><div class="ko-related">{related}</div>{sources}<p class="article-disclaimer">옵션은 위험을 수반하며 모든 투자자에게 적합하지 않을 수 있습니다. 이 글은 교육 목적이며 투자, 세금 또는 법률 조언이 아닙니다. 거래 전 브로커가 제공하는 상품 명세와 공식 위험고지를 확인하세요.</p></article>
<aside class="article-sidebar"><div class="toc"><strong>이 글의 내용</strong>{toc}<a href="#faq">자주 묻는 질문</a></div><div class="course-cta"><strong>무료 옵션 강의</strong><p>계약 구조와 위험을 기초부터 순서대로 학습하세요.</p><a class="btn btn-gold" href="{COURSE}">Google로 무료 시작 →</a></div></aside></div></main>{footer()}<script>document.querySelectorAll('[data-current-year]').forEach(e=>e.textContent=new Date().getFullYear())</script></body></html>'''


def hub_html(cluster: dict) -> str:
    url = f"{BASE}/ko/blog/{cluster['slug']}/"
    cards = "\n".join(f'<a class="post-card" href="{a["slug"]}/"><img src="{a["image"]}" alt="{html.escape(a["alt"], quote=True)}"><div class="post-card-copy"><span class="tag">{html.escape(a["tag"])}</span><h2>{html.escape(a["short"])}</h2><p>{html.escape(a["description"])}</p><strong>가이드 읽기 →</strong></div></a>' for a in cluster["articles"])
    schema = {"@context": "https://schema.org", "@type": "ItemList", "name": cluster["title"], "inLanguage": "ko-KR", "itemListElement": [{"@type": "ListItem", "position": i, "name": a["short"], "url": f"{url}{a['slug']}/"} for i, a in enumerate(cluster["articles"], 1)]}
    return f'''<!doctype html><html lang="ko-KR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(cluster['title'])} | Options America</title><meta name="description" content="{html.escape(cluster['description'], quote=True)}"><link rel="canonical" href="{url}"><meta property="og:locale" content="ko_KR"><meta property="og:type" content="website"><meta property="og:title" content="{html.escape(cluster['title'], quote=True)}"><meta property="og:description" content="{html.escape(cluster['description'], quote=True)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}{cluster['image']}"><link rel="stylesheet" href="/styles.css"><link rel="stylesheet" href="/blog/blog.css"><link rel="stylesheet" href="/ko/blog/ko-blog.css"><script src="/favicon.js"></script><script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(",", ":"))}</script></head><body>{header()}<main><section class="blog-hero ko-blog-hero"><div class="container"><p class="eyebrow">Cluster {cluster['number']} · {html.escape(cluster['label'])}</p><h1>{html.escape(cluster['title'])}</h1><p>{html.escape(cluster['intro'])}</p><div class="ko-hero-actions"><a class="btn btn-gold" href="{COURSE}">Google로 무료 강의 시작</a><a class="btn ko-secondary" href="/ko/blog/">전체 한국어 과정</a></div></div></section><section class="blog-main"><div class="container"><div class="section-heading"><div><p class="eyebrow blue">학습 순서</p><h2>{html.escape(cluster['label'])} 집중 과정</h2><p>아래 다섯 개의 가이드를 순서대로 읽으면 개념부터 실제 관리까지 연결됩니다.</p></div></div><div class="blog-grid ko-blog-grid">{cards}</div></div></section></main>{footer()}<script>document.querySelectorAll('[data-current-year]').forEach(e=>e.textContent=new Date().getFullYear())</script></body></html>'''


def main() -> None:
    for cluster in CLUSTERS:
        directory = OUT / cluster["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(hub_html(cluster), encoding="utf-8")
        for article in cluster["articles"]:
            article_dir = directory / article["slug"]
            article_dir.mkdir(parents=True, exist_ok=True)
            (article_dir / "index.html").write_text(article_html(cluster, article), encoding="utf-8")
    print(f"Built Korean clusters 2-3: {sum(len(c['articles']) for c in CLUSTERS)} articles plus 2 hubs")


if __name__ == "__main__":
    main()
