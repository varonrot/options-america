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

  // Shared legal/footer styles are loaded globally so the migration links render consistently.
  if (!document.querySelector('link[href="/legal.css"]')) {
    const legalStyles = document.createElement('link');
    legalStyles.rel = 'stylesheet';
    legalStyles.href = '/legal.css';
    document.head.appendChild(legalStyles);
  }

  if (!document.querySelector('link[href="/options-auth.css"]')) {
    const authStyles = document.createElement('link');
    authStyles.rel = 'stylesheet';
    authStyles.href = '/options-auth.css';
    document.head.appendChild(authStyles);
  }
  if (!document.getElementById('options-america-auth')) {
    const authScript = document.createElement('script');
    authScript.id = 'options-america-auth';
    authScript.src = '/options-auth.js';
    authScript.defer = true;
    document.head.appendChild(authScript);
  }

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

  // Remember the latest course and lesson so the student dashboard can resume it.
  const rememberCoursePosition = () => {
    const match = location.pathname.match(/^\/courses\/([^/]+)\/player\/?/);
    if (!match) return;
    const save = lesson => {
      try {
        localStorage.setItem('oa-last-course', JSON.stringify({
          slug: match[1], lesson: Math.max(1, Number(lesson) || 1), visitedAt: Date.now()
        }));
      } catch (_) {}
    };
    save(new URLSearchParams(location.search).get('lesson'));
    document.addEventListener('click', event => {
      const item = event.target.closest?.('.syllabus-item[data-lesson]');
      if (item) save(item.dataset.lesson);
    });
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', rememberCoursePosition, { once: true });
  else rememberCoursePosition();


  // Track Vimeo watch percentage and restore the last playback position.
  const setupVideoProgress = () => {
    const courseMatch = location.pathname.match(/^\/courses\/([^/]+)\/player\/?/);
    if (!courseMatch) return;
    const courseSlug = courseMatch[1];
    const storageKey = 'oa-video-progress-v1';
    let activeToken = '';
    const style = document.createElement('style');
    style.textContent = '.oa-viewing-progress{display:flex;align-items:center;gap:12px;margin:10px 0 0;padding:10px 14px;border:1px solid #dce5ef;border-radius:10px;background:#fff;color:#53657a;font:600 12px/1.3 Inter,Arial,sans-serif}.oa-viewing-progress[hidden]{display:none}.oa-viewing-progress-track{flex:1;height:6px;overflow:hidden;border-radius:99px;background:#e6edf4}.oa-viewing-progress-track i{display:block;height:100%;border-radius:inherit;background:#f6b81f}.oa-viewing-progress strong{color:#0b2d51;white-space:nowrap}@media(max-width:640px){.oa-viewing-progress{margin:8px 10px 0}}';
    document.head.appendChild(style);
    const status = document.createElement('div');
    status.className = 'oa-viewing-progress';
    status.hidden = true;
    document.getElementById('videoCard')?.after(status);

    const readStore = () => {
      try { return JSON.parse(localStorage.getItem(storageKey) || '{}') || {}; }
      catch (_) { return {}; }
    };
    const showProgress = record => {
      const percent = Math.min(100, Math.max(0, Math.round(Number(record?.percent) || 0)));
      status.hidden = false;
      status.innerHTML = `<strong>${percent}% watched</strong><span class="oa-viewing-progress-track"><i style="width:${percent}%"></i></span><span>Saved automatically</span>`;
    };
    const writeRecord = record => {
      try {
        const store = readStore();
        const old = store[courseSlug]?.[String(record.lesson)] || {};
        store[courseSlug] = store[courseSlug] || {};
        store[courseSlug][String(record.lesson)] = {
          ...old, ...record,
          percent: Math.max(Number(old.percent) || 0, Number(record.percent) || 0),
          completed: Boolean(old.completed || record.completed),
          updatedAt: Date.now()
        };
        localStorage.setItem(storageKey, JSON.stringify(store));
        window.dispatchEvent(new CustomEvent('oa:progresschange'));
        return store[courseSlug][String(record.lesson)];
      } catch (_) { return record; }
    };
    const lessonNumber = () => Math.max(1, Number(document.querySelector('.syllabus-item.active')?.dataset.lesson || new URLSearchParams(location.search).get('lesson')) || 1);
    const cloudSave = record => window.optionsAmericaAuth?.saveVideoProgress?.({
      course_slug: courseSlug,
      lesson_number: record.lesson,
      vimeo_id: record.vimeoId,
      position_seconds: record.position,
      duration_seconds: record.duration,
      watched_percent: record.percent,
      completed: record.completed,
      updated_at: new Date(record.updatedAt || Date.now()).toISOString()
    });

    const bindPlayer = async () => {
      const iframe = document.getElementById('vimeoFrame');
      const src = iframe?.getAttribute('src') || '';
      const vimeoId = (src.match(/video\/(\d+)/) || [])[1];
      const lesson = lessonNumber();
      const token = `${lesson}:${vimeoId || ''}:${src}`;
      if (!iframe || !vimeoId || token === activeToken || !window.Vimeo?.Player) return;
      activeToken = token;
      const player = new Vimeo.Player(iframe);
      let duration = 0;
      let lastCloudSave = 0;
      let local = readStore()[courseSlug]?.[String(lesson)] || null;
      try {
        for (let i = 0; i < 30 && !window.optionsAmericaAuth?.loadVideoProgress; i += 1) await new Promise(resolve => setTimeout(resolve, 100));
        const remoteRows = await window.optionsAmericaAuth?.loadVideoProgress?.(courseSlug, lesson) || [];
        const remote = remoteRows[0];
        if (remote) {
          const remoteRecord = {
            lesson, vimeoId: remote.vimeo_id || vimeoId,
            position: Number(remote.position_seconds) || 0,
            duration: Number(remote.duration_seconds) || 0,
            percent: Number(remote.watched_percent) || 0,
            completed: Boolean(remote.completed),
            updatedAt: Date.parse(remote.updated_at) || 0
          };
          if (!local || remoteRecord.updatedAt > (Number(local.updatedAt) || 0)) local = writeRecord(remoteRecord);
        }
      } catch (_) {}
      try {
        if (token !== activeToken) return;
        await player.ready();
        duration = Number(await player.getDuration()) || Number(local?.duration) || 0;
        const resumeAt = Number(local?.position) || 0;
        if (local) showProgress(local);
        if (!local?.completed && resumeAt >= 5 && duration && resumeAt < duration - 8) await player.setCurrentTime(resumeAt);
      } catch (_) {}
      const save = (data, forceCloud = false, ended = false) => {
        if (token !== activeToken) return;
        const seconds = ended ? (Number(data?.duration) || duration) : (Number(data?.seconds) || 0);
        duration = Number(data?.duration) || duration || 0;
        const currentPercent = duration ? Math.min(100, seconds / duration * 100) : 0;
        const previous = readStore()[courseSlug]?.[String(lesson)] || {};
        const percent = ended ? 100 : Math.max(Number(previous.percent) || 0, currentPercent);
        const record = writeRecord({ lesson, vimeoId, position: seconds, duration, percent: Math.round(percent * 10) / 10, completed: ended || percent >= 90 });
        showProgress(record);
        try { localStorage.setItem('oa-last-course', JSON.stringify({ slug: courseSlug, lesson, position: seconds, visitedAt: Date.now() })); } catch (_) {}
        const now = Date.now();
        if (forceCloud || now - lastCloudSave >= 15000) {
          lastCloudSave = now;
          cloudSave(record);
        }
      };
      player.on('timeupdate', data => save(data));
      player.on('pause', data => save(data, true));
      player.on('ended', data => save(data, true, true));
    };
    let checks = 0;
    const timer = setInterval(() => {
      checks += 1;
      bindPlayer();
      if (checks >= 120) clearInterval(timer);
    }, 500);
    const iframe = document.getElementById('vimeoFrame');
    if (iframe) new MutationObserver(bindPlayer).observe(iframe, { attributes: true, attributeFilter: ['src'] });
    document.addEventListener('click', event => {
      if (event.target.closest?.('.syllabus-item[data-lesson],#prevBtn,#nextBtn')) setTimeout(bindPlayer, 50);
    });
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', setupVideoProgress, { once: true });
  else setupVideoProgress();

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
    'selling-call-margin-buying-power': '/assets/images/blog/selling-call-margin-buying-power.webp',
    'what-is-buying-a-put-option': '/assets/images/blog/what-is-buying-a-put-option.webp',
    'how-to-buy-a-put-option': '/assets/images/blog/how-to-buy-a-put-option.webp',
    'long-put-profit-loss-breakeven': '/assets/images/blog/long-put-profit-loss-breakeven.webp',
    'how-to-choose-put-option-strike': '/assets/images/blog/how-to-choose-put-option-strike.webp',
    'how-to-choose-put-option-expiration': '/assets/images/blog/how-to-choose-put-option-expiration.webp',
    'itm-atm-otm-put-options': '/assets/images/blog/itm-atm-otm-put-options.webp',
    'put-option-intrinsic-value-time-value': '/assets/images/blog/put-option-intrinsic-value-time-value.webp',
    'what-happens-put-option-stock-rises': '/assets/images/blog/what-happens-put-option-stock-rises.webp',
    'when-to-sell-put-option-you-bought': '/assets/images/blog/when-to-sell-put-option-you-bought.webp',
    'sell-put-option-vs-exercise': '/assets/images/blog/sell-put-option-vs-exercise.webp',
    'theta-time-decay-long-put': '/assets/images/blog/theta-time-decay-long-put.webp',
    'implied-volatility-long-put': '/assets/images/blog/implied-volatility-long-put.webp',
    'protective-put-vs-long-put': '/assets/images/blog/protective-put-vs-long-put.webp',
    'long-put-risks-mistakes': '/assets/images/blog/long-put-risks-mistakes.webp',
    'put-option-delta-explained': '/assets/images/blog/put-option-delta-explained.webp',
    'what-is-selling-a-put-option': '/assets/images/blog/what-is-selling-a-put-option.webp',
    'cash-secured-put-vs-naked-put': '/assets/images/blog/cash-secured-put-vs-naked-put.webp',
    'how-to-sell-a-cash-secured-put': '/assets/images/blog/how-to-sell-a-cash-secured-put.webp',
    'short-put-profit-loss-breakeven': '/assets/images/blog/short-put-profit-loss-breakeven.webp',
    'how-to-choose-short-put-strike': '/assets/images/blog/how-to-choose-short-put-strike.webp',
    'how-to-choose-short-put-expiration': '/assets/images/blog/how-to-choose-short-put-expiration.webp',
    'put-option-assignment-explained': '/assets/images/blog/put-option-assignment-explained.webp',
    'early-assignment-short-put': '/assets/images/blog/early-assignment-short-put.webp',
    'how-to-roll-a-short-put': '/assets/images/blog/how-to-roll-a-short-put.webp',
    'when-to-close-a-short-put': '/assets/images/blog/when-to-close-a-short-put.webp',
    'short-put-risks-mistakes': '/assets/images/blog/short-put-risks-mistakes.webp',
    'cash-secured-put-income-potential': '/assets/images/blog/cash-secured-put-income-potential.webp',
    'cash-secured-put-vs-limit-order': '/assets/images/blog/cash-secured-put-vs-limit-order.webp',
    'short-put-vs-covered-call': '/assets/images/blog/short-put-vs-covered-call.webp',
    'selling-put-margin-buying-power': '/assets/images/blog/selling-put-margin-buying-power.webp',
    'what-is-theta-in-options': '/assets/images/blog/what-is-theta-in-options.webp',
    'how-time-decay-works-options': '/assets/images/blog/how-time-decay-works-options.webp',
    'positive-theta-vs-negative-theta': '/assets/images/blog/positive-theta-vs-negative-theta.webp',
    'theta-long-options-vs-short-options': '/assets/images/blog/theta-long-options-vs-short-options.webp',
    'why-option-time-decay-accelerates': '/assets/images/blog/why-option-time-decay-accelerates.webp',
    'theta-itm-atm-otm-options': '/assets/images/blog/theta-itm-atm-otm-options.webp',
    'option-theta-weekends-holidays': '/assets/images/blog/option-theta-weekends-holidays.webp',
    'theta-vs-implied-volatility': '/assets/images/blog/theta-vs-implied-volatility.webp',
    'theta-vs-gamma-near-expiration': '/assets/images/blog/theta-vs-gamma-near-expiration.webp',
    'theta-0dte-weekly-options': '/assets/images/blog/theta-0dte-weekly-options.webp',
    'theta-leaps-long-term-options': '/assets/images/blog/theta-leaps-long-term-options.webp',
    'calculate-option-time-decay-theta': '/assets/images/blog/calculate-option-time-decay-theta.webp',
    'positive-theta-option-strategies': '/assets/images/blog/positive-theta-option-strategies.webp',
    'reduce-time-decay-option-buyers': '/assets/images/blog/reduce-time-decay-option-buyers.webp',
    'theta-time-decay-mistakes': '/assets/images/blog/theta-time-decay-mistakes.webp',
    'what-is-vega-in-options': '/assets/images/blog/what-is-vega-in-options.webp',
    'implied-volatility-options-explained': '/assets/images/blog/implied-volatility-options-explained.webp',
    'vega-long-options-vs-short-options': '/assets/images/blog/vega-long-options-vs-short-options.webp',
    'positive-vega-vs-negative-vega': '/assets/images/blog/positive-vega-vs-negative-vega.webp',
    'calculate-option-vega': '/assets/images/blog/calculate-option-vega.webp',
    'vega-itm-atm-otm-options': '/assets/images/blog/vega-itm-atm-otm-options.webp',
    'vega-expiration-long-term-short-term-options': '/assets/images/blog/vega-expiration-long-term-short-term-options.webp',
    'historical-vs-implied-volatility': '/assets/images/blog/historical-vs-implied-volatility.webp',
    'iv-rank-vs-iv-percentile': '/assets/images/blog/iv-rank-vs-iv-percentile.webp',
    'volatility-crush-options': '/assets/images/blog/volatility-crush-options.webp',
    'vega-around-earnings': '/assets/images/blog/vega-around-earnings.webp',
    'vega-vs-theta-options': '/assets/images/blog/vega-vs-theta-options.webp',
    'vega-neutral-option-strategies': '/assets/images/blog/vega-neutral-option-strategies.webp',
    'vix-vs-implied-volatility': '/assets/images/blog/vix-vs-implied-volatility.webp',
    'vega-volatility-mistakes': '/assets/images/blog/vega-volatility-mistakes.webp',
    'what-is-delta-in-options': '/assets/images/blog/what-is-delta-in-options.webp',
    'call-delta-vs-put-delta': '/assets/images/blog/call-delta-vs-put-delta.webp',
    'positive-delta-vs-negative-delta': '/assets/images/blog/positive-delta-vs-negative-delta.webp',
    'option-delta-itm-atm-otm': '/assets/images/blog/option-delta-itm-atm-otm.webp',
    'calculate-option-delta': '/assets/images/blog/calculate-option-delta.webp',
    'delta-probability-in-the-money': '/assets/images/blog/delta-probability-in-the-money.webp',
    'delta-as-share-equivalent': '/assets/images/blog/delta-as-share-equivalent.webp',
    'what-is-gamma-options': '/assets/images/blog/what-is-gamma-options.webp',
    'delta-vs-gamma-options': '/assets/images/blog/delta-vs-gamma-options.webp',
    'gamma-near-expiration': '/assets/images/blog/gamma-near-expiration.webp',
    'delta-hedging-options': '/assets/images/blog/delta-hedging-options.webp',
    'portfolio-delta-beta-weighting': '/assets/images/blog/portfolio-delta-beta-weighting.webp',
    'delta-neutral-option-strategies': '/assets/images/blog/delta-neutral-option-strategies.webp',
    'delta-option-chain': '/assets/images/blog/delta-option-chain.webp',
    'delta-gamma-mistakes': '/assets/images/blog/delta-gamma-mistakes.webp',
    'option-greeks-explained': '/assets/images/blog/option-greeks-explained.webp',
    'how-option-greeks-interact': '/assets/images/blog/how-option-greeks-interact.webp',
    'what-is-rho-in-options': '/assets/images/blog/what-is-rho-in-options.webp',
    'option-greeks-long-call': '/assets/images/blog/option-greeks-long-call.webp',
    'option-greeks-long-put': '/assets/images/blog/option-greeks-long-put.webp',
    'option-greeks-credit-spreads': '/assets/images/blog/option-greeks-credit-spreads.webp',
    'option-greeks-debit-spreads': '/assets/images/blog/option-greeks-debit-spreads.webp',
    'option-greeks-straddles-strangles': '/assets/images/blog/option-greeks-straddles-strangles.webp',
    'option-greeks-iron-condor': '/assets/images/blog/option-greeks-iron-condor.webp',
    'option-greeks-calendar-spreads': '/assets/images/blog/option-greeks-calendar-spreads.webp',
    'option-greeks-around-earnings': '/assets/images/blog/option-greeks-around-earnings.webp',
    'portfolio-option-greeks-risk': '/assets/images/blog/portfolio-option-greeks-risk.webp',
    'option-greeks-scenario-analysis': '/assets/images/blog/option-greeks-scenario-analysis.webp',
    'option-greeks-pnl-explained': '/assets/images/blog/option-greeks-pnl-explained.webp',
    'option-greeks-mistakes': '/assets/images/blog/option-greeks-mistakes.webp'
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

  // Keep the legal migration links available from every page that uses the global bootstrap.
  const applyLegalLinks = () => {
    const copyright = document.querySelector('footer .copyright');
    if (!copyright || copyright.querySelector('.site-legal-links')) return;
    const links = [
      ['/privacy-policy/', 'Privacy Policy'],
      ['/terms-and-conditions/', 'Terms and Conditions'],
      ['/risk-disclaimer/', 'Risk Disclaimer'],
      ['/refund-policy/', 'Refund Policy'],
      ['/accessibility-statement/', 'Accessibility Statement']
    ];
    const nav = document.createElement('nav');
    nav.className = 'site-legal-links';
    nav.setAttribute('aria-label', 'Legal');
    links.forEach(([href, label]) => {
      const link = document.createElement('a');
      link.href = href;
      link.textContent = label;
      nav.appendChild(link);
    });
    copyright.appendChild(nav);
  };
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyLegalLinks, { once: true });
  } else {
    applyLegalLinks();
  }

  // Mobile course players show the active lesson before the long curriculum.
  if (!document.getElementById('mobile-player-order')) {
    const playerOrderStyles = document.createElement('style');
    playerOrderStyles.id = 'mobile-player-order';
    playerOrderStyles.textContent = '@media(max-width:1000px){.player-page .player-main{order:1;scroll-margin-top:70px}.player-page .player-syllabus{order:2}}';
    document.head.appendChild(playerOrderStyles);
  }
  document.addEventListener('click', event => {
    if (!event.target.closest('.player-page .syllabus-item') || !window.matchMedia('(max-width: 1000px)').matches) return;
    window.setTimeout(() => {
      document.querySelector('.player-main')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 0);
  });

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
