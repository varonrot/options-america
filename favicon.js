// Options America global site bootstrap: favicon + Google Tag Manager + shared course messaging.
(() => {
  const href = '/assets/images/options-america-favicon.png';
  let icon = document.querySelector('link[rel="icon"]');
  if (!icon) {
    icon = document.createElement('link');
    icon.rel = 'icon';
    document.head.appendChild(icon);
  }
  icon.type = 'image/png';
  icon.sizes = '128x128';
  icon.href = href;

  let apple = document.querySelector('link[rel="apple-touch-icon"]');
  if (!apple) {
    apple = document.createElement('link');
    apple.rel = 'apple-touch-icon';
    document.head.appendChild(apple);
  }
  apple.href = href;

  // Keep the public-facing free-course message consistent across all course pages.
  const applyCourseMessage = () => {
    document.querySelectorAll('.sidebar-note').forEach(note => {
      const heading = note.querySelector('strong');
      const text = note.querySelector('p');
      if (heading && heading.textContent.trim().toLowerCase() === 'free course' && text) {
        text.textContent = 'Professional, structured options education designed to build practical trading knowledge step by step.';
      }
    });
  };
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyCourseMessage, { once: true });
  } else {
    applyCourseMessage();
  }

  // Give every Level 1 article its own topic-specific visual.
  const blogImages = {
    'what-is-a-call-option': '/assets/images/blog/what-is-a-call-option.webp',
    'how-to-buy-a-call-option': '/assets/images/blog/how-to-buy-a-call-option.webp',
    'long-call-profit-loss-breakeven': '/assets/images/blog/long-call-profit-loss-breakeven.webp',
    'how-to-choose-call-option-strike-price': '/assets/images/blog/how-to-choose-call-option-strike-price.webp',
    'how-to-choose-call-option-expiration': '/assets/images/blog/how-to-choose-call-option-expiration.webp',
    'buying-call-options-risks-mistakes': '/assets/images/blog/buying-call-options-risks-mistakes.webp',
    'itm-atm-otm-call-options': '/assets/images/blog/itm-atm-otm-call-options.webp',
    'call-option-intrinsic-value-time-value': '/assets/images/blog/call-option-intrinsic-value-time-value.webp',
    'bid-ask-spread-options': '/assets/images/blog/bid-ask-spread-options.webp',
    'what-happens-call-option-stock-goes-down': '/assets/images/blog/what-happens-call-option-stock-goes-down.webp',
    'average-option-premium-price': '/assets/images/blog/average-option-premium-price.webp',
    'when-to-sell-call-option': '/assets/images/blog/when-to-sell-call-option.webp',
    'sell-call-option-vs-exercise': '/assets/images/blog/sell-call-option-vs-exercise.webp',
    'theta-time-decay-long-call': '/assets/images/blog/theta-time-decay-long-call.webp',
    'implied-volatility-long-call': '/assets/images/blog/implied-volatility-long-call.webp',
    'what-is-selling-a-call-option': '/assets/images/blog/what-is-selling-a-call-option.webp',
    'covered-call-vs-naked-call': '/assets/images/blog/covered-call-vs-naked-call.webp',
    'how-to-sell-a-covered-call': '/assets/images/blog/how-to-sell-a-covered-call.webp',
    'short-call-profit-loss-breakeven': '/assets/images/blog/short-call-profit-loss-breakeven.webp',
    'how-to-choose-covered-call-strike': '/assets/images/blog/how-to-choose-covered-call-strike.webp',
    'how-to-choose-covered-call-expiration': '/assets/images/blog/how-to-choose-covered-call-expiration.webp',
    'covered-call-assignment-explained': '/assets/images/blog/covered-call-assignment-explained.webp',
    'covered-call-early-assignment-dividends': '/assets/images/blog/covered-call-early-assignment-dividends.webp',
    'how-to-roll-a-covered-call': '/assets/images/blog/how-to-roll-a-covered-call.webp',
    'when-to-close-covered-call': '/assets/images/blog/when-to-close-covered-call.webp',
    'covered-call-risks-mistakes': '/assets/images/blog/covered-call-risks-mistakes.webp',
    'covered-call-income-potential': '/assets/images/blog/covered-call-income-potential.webp',
    'covered-call-vs-buy-and-hold': '/assets/images/blog/covered-call-vs-buy-and-hold.webp',
    'covered-call-vs-cash-secured-put': '/assets/images/blog/covered-call-vs-cash-secured-put.webp',
    'selling-call-margin-buying-power': '/assets/images/blog/selling-call-margin-buying-power.webp'
  };
  const applyBlogImages = () => {
    document.querySelectorAll('.post-card[href]').forEach(card => {
      const slug = new URL(card.href, location.href).pathname.split('/').filter(Boolean).pop();
      const img = card.querySelector('img');
      if (img && blogImages[slug]) img.src = blogImages[slug];
    });
    const parts = location.pathname.split('/').filter(Boolean);
    if (parts[0] === 'blog' && parts[1] && blogImages[parts[1]]) {
      const image = blogImages[parts[1]];
      const hero = document.querySelector('.article-body > img');
      const ogImage = document.querySelector('meta[property="og:image"]');
      if (hero) hero.src = image;
      if (ogImage) ogImage.content = location.origin + image;
    }
  };
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyBlogImages, { once: true });
  } else {
    applyBlogImages();
  }

  // Google Tag Manager — Options America
  const GTM_ID = 'GTM-TSZLK9R4';
  if (!window.__optionsAmericaGtmLoaded) {
    window.__optionsAmericaGtmLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({'gtm.start': Date.now(), event: 'gtm.js'});
    const gtm = document.createElement('script');
    gtm.async = true;
    gtm.src = 'https://www.googletagmanager.com/gtm.js?id=' + encodeURIComponent(GTM_ID);
    const firstScript = document.getElementsByTagName('script')[0];
    if (firstScript && firstScript.parentNode) firstScript.parentNode.insertBefore(gtm, firstScript);
    else document.head.appendChild(gtm);

    // Equivalent fallback to GTM's noscript iframe for users with JS enabled.
    if (document.body) {
      const frame = document.createElement('iframe');
      frame.src = 'https://www.googletagmanager.com/ns.html?id=' + encodeURIComponent(GTM_ID);
      frame.height = '0';
      frame.width = '0';
      frame.style.display = 'none';
      frame.style.visibility = 'hidden';
      frame.setAttribute('aria-hidden', 'true');
      document.body.insertBefore(frame, document.body.firstChild);
    }
  }
})();
