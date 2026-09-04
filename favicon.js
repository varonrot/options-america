// Options America global site bootstrap: favicon + Google Tag Manager.
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
