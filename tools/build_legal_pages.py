#!/usr/bin/env python3
"""Build the five public legal pages used by the Options America footer."""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UPDATED = "September 11, 2026"

PAGES = {
    "privacy-policy": {
        "title": "Privacy Policy",
        "description": "How Options America collects, uses, and protects information when you use our website.",
        "intro": "This policy explains what information Options America may collect when you visit the Site, why we use it, and the choices available to you.",
        "sections": [
            ("Information we collect", "<p>We may collect technical and usage information automatically, including your browser and device type, approximate location derived from your IP address, referring page, pages viewed, clicks, and the date and time of your visit.</p><p>If you voluntarily submit information through a form or email, we receive the information you choose to provide. Please do not send sensitive personal or financial information through the Site.</p>"),
            ("Analytics, cookies, and similar technologies", "<p>The Site uses Google Tag Manager and may use Google Analytics or similar measurement tools. These services may set cookies or use comparable technologies to understand visits and interactions. Information may be processed by Google under its own terms and privacy practices.</p><p>You can limit cookies through your browser settings and may use the <a href=\"https://tools.google.com/dlpage/gaoptout\" rel=\"noopener noreferrer\">Google Analytics Opt-out Browser Add-on</a>. Blocking cookies may affect some Site features.</p>"),
            ("How we use information", "<ul><li>Operate, secure, maintain, and improve the Site.</li><li>Understand which lessons and pages are useful to visitors.</li><li>Diagnose technical problems and prevent abuse.</li><li>Respond to messages or requests you send us.</li><li>Comply with applicable law and protect our rights.</li></ul>"),
            ("Sharing and sale of information", "<p>We may share information with service providers that help us host, measure, secure, or operate the Site, and when required by law or necessary to protect rights and safety. We do not sell personal information for money. Analytics providers may process data according to their own policies.</p>"),
            ("Retention and security", "<p>We retain information only as long as reasonably needed for the purposes described above, legal obligations, dispute resolution, and security. We use reasonable safeguards, but no internet transmission or storage system can be guaranteed completely secure.</p>"),
            ("Your choices and rights", "<p>Depending on where you live, you may have rights to request access, correction, deletion, restriction, or a copy of certain personal information, and to object to or opt out of certain processing. You may also clear or block cookies in your browser.</p><p>To make a privacy request, email <a href=\"mailto:privacy@options-america.com\">privacy@options-america.com</a>. We may need to verify your request before responding.</p>"),
            ("Children's privacy", "<p>The Site is not directed to children under 13, and we do not knowingly collect personal information from children under 13. If you believe a child has provided personal information, contact us so we can review and delete it where appropriate.</p>"),
            ("International visitors and changes", "<p>Your information may be processed in countries other than the one where you live. We may update this policy as the Site or applicable requirements change. The updated date at the top shows when this policy was last revised.</p>"),
        ],
    },
    "terms-and-conditions": {
        "title": "Terms and Conditions",
        "description": "Terms governing access to and use of the Options America educational website.",
        "intro": "By accessing or using Options America, you agree to these Terms. If you do not agree, do not use the Site.",
        "sections": [
            ("Educational purpose only", "<p>The Site provides general educational information about options, futures, markets, and trading concepts. It does not provide personalized investment, legal, tax, or accounting advice and does not create an adviser, fiduciary, broker, or client relationship.</p>"),
            ("No offer or recommendation", "<p>Nothing on the Site is an offer to buy or sell a security, option, futures contract, or other financial product, or a recommendation that any strategy or product is suitable for you. You are solely responsible for your decisions and should consult appropriately licensed professionals.</p>"),
            ("Eligibility and acceptable use", "<p>You must be legally able to agree to these Terms. You may use the Site for lawful, personal, and educational purposes. You may not disrupt the Site, bypass security, introduce malicious code, scrape at a harmful rate, impersonate others, or use content in a way that violates law or third-party rights.</p>"),
            ("Content and intellectual property", "<p>Unless otherwise stated, the Site design, lessons, text, graphics, and original materials are owned by or licensed to Options America and are protected by applicable intellectual-property laws. You may reference and link to public pages for personal education, but you may not republish, sell, or create a competing content library from substantial portions without permission.</p>"),
            ("Accuracy and availability", "<p>Markets and regulations change, and content may contain errors or become outdated. We may correct, remove, or change content and may suspend or discontinue any part of the Site without notice. We do not promise uninterrupted access, completeness, or accuracy.</p>"),
            ("Third-party services and links", "<p>The Site may link to brokers, exchanges, regulators, analytics providers, or other third parties. We do not control and are not responsible for their content, availability, security, products, or practices. A link does not necessarily mean endorsement.</p>"),
            ("Disclaimers and limitation of liability", "<p>The Site is provided on an “as is” and “as available” basis to the extent permitted by law, without warranties of any kind. Options America and its contributors are not liable for trading losses, lost profits, lost data, or indirect, incidental, special, consequential, or punitive damages arising from use of or reliance on the Site.</p>"),
            ("Changes and contact", "<p>We may revise these Terms. Continued use after revised Terms are posted means you accept them. If any provision is found unenforceable, the remaining provisions continue in effect. Questions may be sent to <a href=\"mailto:legal@options-america.com\">legal@options-america.com</a>.</p>"),
        ],
    },
    "risk-disclaimer": {
        "title": "Risk Disclaimer",
        "description": "Important risks and limitations related to options and futures education on Options America.",
        "intro": "Options, futures, and other derivatives involve substantial risk and are not suitable for every investor. Read this notice before relying on any educational example on the Site.",
        "notice": "You can lose all of the money committed to an options position. Some short-option and futures-related positions can create losses greater than the initial amount received or invested.",
        "sections": [
            ("No investment advice", "<p>All material is general education, not individualized advice, a trade signal, a solicitation, or a guarantee of results. Options America does not know your financial situation, objectives, experience, tax position, or risk tolerance.</p>"),
            ("Key trading risks", "<ul><li><strong>Leverage:</strong> small market moves can create large percentage gains or losses.</li><li><strong>Expiration and time decay:</strong> an option can lose value and expire worthless.</li><li><strong>Assignment and exercise:</strong> short positions may be assigned, including before expiration, and can create stock, cash, or margin obligations.</li><li><strong>Liquidity and execution:</strong> wide bid-ask spreads, low volume, volatility, halts, and slippage may prevent execution at an expected price.</li><li><strong>Volatility and model risk:</strong> implied volatility, Greeks, probabilities, and pricing models are estimates, not promises.</li><li><strong>Futures options:</strong> contract specifications, settlement, leverage, and margin can differ materially from equity options.</li></ul>"),
            ("Examples and performance", "<p>Examples may be simplified, hypothetical, delayed, or based on assumptions. They may omit commissions, fees, taxes, slippage, margin changes, early assignment, and other real-world effects. Hypothetical results do not represent actual trading and past performance does not guarantee future results.</p>"),
            ("Your responsibility", "<p>Before trading, review the product documents and your broker's rules, understand the maximum potential loss and margin requirements, and consider advice from licensed financial, legal, and tax professionals. Use only risk capital you can afford to lose.</p>"),
            ("Required options disclosure", "<p>Before buying or selling exchange-traded options, read the Options Clearing Corporation's <a href=\"https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document\" rel=\"noopener noreferrer\">Characteristics and Risks of Standardized Options</a>. Approval by a broker does not make a strategy suitable or safe.</p>"),
        ],
    },
    "refund-policy": {
        "title": "Refund Policy",
        "description": "Refund policy for the current free Options America educational website.",
        "intro": "The lessons, courses, and articles currently available directly on Options America are provided free of charge.",
        "sections": [
            ("Current free content", "<p>Because Options America does not currently charge visitors to access its public educational content, there is no purchase price to refund for that content.</p>"),
            ("Future paid products or services", "<p>If Options America later offers a paid product, membership, event, download, or service, the price, cancellation rules, refund window, and any exclusions will be shown clearly at or before checkout. Those transaction-specific terms will control for that purchase.</p>"),
            ("Third-party purchases", "<p>If you purchase a product or service from a third party reached through a link on the Site, that third party's refund and cancellation policy applies. Options America cannot issue refunds for payments it did not process.</p>"),
            ("Billing questions", "<p>If you believe a charge identifies Options America, email <a href=\"mailto:support@options-america.com\">support@options-america.com</a> with the transaction date, amount, and non-sensitive identifying details. Do not send a full card number, password, or other sensitive financial information.</p>"),
        ],
    },
    "accessibility-statement": {
        "title": "Accessibility Statement",
        "description": "Options America's commitment to an accessible website and how to report an accessibility barrier.",
        "intro": "Options America wants its educational content to be usable by as many people as possible, including people who use assistive technologies.",
        "sections": [
            ("Our accessibility goal", "<p>We aim to improve the Site toward the Web Content Accessibility Guidelines (WCAG) 2.2 Level AA. Accessibility is an ongoing effort, and this statement is not a claim that every page or third-party component is fully conformant.</p>"),
            ("Measures we take", "<ul><li>Use semantic headings, landmarks, and descriptive page titles.</li><li>Support keyboard navigation and visible focus where possible.</li><li>Provide text alternatives for meaningful images.</li><li>Maintain readable typography, responsive layouts, and sufficient color contrast.</li><li>Review new templates and correct barriers identified through testing or feedback.</li></ul>"),
            ("Known limitations", "<p>Some legacy course materials, images, tables, documents, or third-party content may not yet provide an equivalent accessible experience. We are working through migrated content and prioritize issues that prevent access to core educational information.</p>"),
            ("Feedback and assistance", "<p>If you encounter an accessibility barrier, email <a href=\"mailto:accessibility@options-america.com\">accessibility@options-america.com</a>. Include the page URL, a short description of the problem, your browser or assistive technology if relevant, and the format or accommodation that would help. We will make reasonable efforts to respond and provide the information in an accessible alternative.</p>"),
            ("Technical compatibility", "<p>The Site is designed for current versions of major browsers and common assistive technologies. Older browsers or disabled browser features may provide a reduced experience.</p>"),
        ],
    },
}


LEGAL_LINKS = """<a href="/privacy-policy/">Privacy Policy</a><a href="/terms-and-conditions/">Terms and Conditions</a><a href="/risk-disclaimer/">Risk Disclaimer</a><a href="/refund-policy/">Refund Policy</a><a href="/accessibility-statement/">Accessibility Statement</a>"""


def render(slug: str, page: dict) -> str:
    sections = []
    toc = []
    for index, (heading, body) in enumerate(page["sections"], 1):
        section_id = f"section-{index}"
        toc.append(f'<a href="#{section_id}">{escape(heading)}</a>')
        sections.append(f'<section id="{section_id}"><h2>{escape(heading)}</h2>{body}</section>')
    notice = f'<div class="legal-notice"><strong>Important</strong><p>{page["notice"]}</p></div>' if page.get("notice") else ""
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{escape(page["title"])} — Options America</title>
  <meta name="description" content="{escape(page["description"], quote=True)}">
  <link rel="canonical" href="https://options-america.com/{slug}/">
  <link rel="stylesheet" href="/styles.css">
  <link rel="stylesheet" href="/legal.css">
  <script src="/favicon.js"></script>
</head>
<body>
  <header class="site-header"><div class="container nav"><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><nav><a href="/courses/">Courses</a><a href="/#paths">Learning Paths</a><a href="/#strategies">Strategies</a><a href="/#futures">Options on Futures</a><a href="/blog/">Blog</a></nav><a class="btn btn-gold" href="/courses/">Start Learning — Free</a></div></header>
  <main>
    <section class="legal-hero"><div class="container"><div class="legal-breadcrumbs"><a href="/">Home</a><span aria-hidden="true">/</span><span>{escape(page["title"])}</span></div><p class="eyebrow">Site information</p><h1>{escape(page["title"])}</h1><p>{escape(page["intro"])}</p><div class="legal-updated">Last updated: {UPDATED}</div></div></section>
    <div class="container legal-layout">
      <article class="legal-body">{notice}{''.join(sections)}</article>
      <aside class="legal-sidebar"><div class="legal-toc"><strong>On this page</strong>{''.join(toc)}</div><div class="legal-help"><strong>Important note</strong><p>These pages describe the current public Site. They may be updated as services and legal requirements change.</p></div></aside>
    </div>
  </main>
  <footer><div class="container footer-grid legal-footer-grid"><div><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><p>The free resource for learning options trading from beginner to advanced.</p></div><div><h4>Learn</h4><a href="/courses/">Courses</a><a href="/#paths">Learning Paths</a><a href="/blog/">Blog</a></div><div><h4>Legal</h4>{LEGAL_LINKS}</div></div><div class="container copyright">© <span data-current-year></span> Options America · Educational content only — not financial advice.</div></footer>
  <script>document.querySelectorAll('[data-current-year]').forEach(el => el.textContent = new Date().getFullYear());</script>
</body>
</html>'''


for slug, page in PAGES.items():
    destination = ROOT / slug / "index.html"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render(slug, page), encoding="utf-8")
    print(destination.relative_to(ROOT))
