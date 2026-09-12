(() => {
  const grid = document.querySelector('#blog-grid');
  const input = document.querySelector('#blog-search-input');
  const pagination = document.querySelector('.blog-pagination');
  const resultText = document.querySelector('.blog-results');
  const clearButton = document.querySelector('.search-clear');
  const emptyState = document.querySelector('.blog-empty');
  if (!grid || !input || !pagination || !resultText || !clearButton || !emptyState) return;

  const cards = Array.from(grid.querySelectorAll('.post-card'));
  const clusterPriority = card => card.textContent.includes('Calendar Spread') ? 13 : card.textContent.includes('Butterfly Spread') ? 12 : card.textContent.includes('Short Iron Condor') ? 11 : card.textContent.includes('Bear Put Spread') ? 10 : card.textContent.includes('Bull Call Spread') ? 9 : card.textContent.includes('Greeks') ? 8 : card.textContent.includes('Delta') ? 7 : card.textContent.includes('Vega') ? 6 : card.textContent.includes('Theta') ? 5 : card.textContent.includes('Selling Puts') ? 4 : card.textContent.includes('Buying Puts') ? 3 : card.textContent.includes('Selling Calls') ? 2 : card.textContent.includes('Call Options') ? 1 : 0;
  cards.sort((a, b) => clusterPriority(b) - clusterPriority(a));
  cards.forEach(card => grid.appendChild(card));
  const pageSize = 6;
  let currentPage = 1;

  const normalized = value => value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').trim();
  const getMatches = () => {
    const query = normalized(input.value);
    return query ? cards.filter(card => normalized(card.textContent).includes(query)) : cards;
  };

  const updateUrl = () => {
    const url = new URL(window.location.href);
    const query = input.value.trim();
    query ? url.searchParams.set('q', query) : url.searchParams.delete('q');
    currentPage > 1 ? url.searchParams.set('page', currentPage) : url.searchParams.delete('page');
    history.replaceState(null, '', url.pathname + url.search);
  };

  const button = (label, page, options = {}) => {
    const element = document.createElement('button');
    element.type = 'button';
    element.className = `page-btn${options.active ? ' active' : ''}${options.arrow ? ' page-arrow' : ''}`;
    element.innerHTML = label;
    element.disabled = Boolean(options.disabled);
    if (options.active) element.setAttribute('aria-current', 'page');
    element.setAttribute('aria-label', options.ariaLabel || `Page ${page}`);
    element.addEventListener('click', () => {
      currentPage = page;
      render(true);
    });
    return element;
  };

  const paginationItems = totalPages => {
    if (totalPages <= 7) return Array.from({length: totalPages}, (_, index) => index + 1);
    const compact = window.matchMedia('(max-width: 620px)').matches;
    if (compact) {
      if (currentPage <= 2) return [1, 2, 3, 'end-gap', totalPages];
      if (currentPage >= totalPages - 1) return [1, 'start-gap', totalPages - 2, totalPages - 1, totalPages];
      return [1, 'start-gap', currentPage, 'end-gap', totalPages];
    }
    if (currentPage <= 3) return [1, 2, 3, 4, 'end-gap', totalPages];
    if (currentPage >= totalPages - 2) return [1, 'start-gap', totalPages - 3, totalPages - 2, totalPages - 1, totalPages];
    return [1, 'start-gap', currentPage - 1, currentPage, currentPage + 1, 'end-gap', totalPages];
  };

  const ellipsis = () => {
    const element = document.createElement('span');
    element.className = 'page-ellipsis';
    element.textContent = '…';
    element.setAttribute('aria-hidden', 'true');
    return element;
  };

  const renderPagination = totalPages => {
    pagination.replaceChildren();
    if (totalPages <= 1) {
      pagination.hidden = true;
      return;
    }
    pagination.hidden = false;
    pagination.appendChild(button('<span>←</span> Previous', currentPage - 1, {arrow: true, disabled: currentPage === 1, ariaLabel: 'Previous page'}));
    paginationItems(totalPages).forEach(item => {
      pagination.appendChild(typeof item === 'number' ? button(String(item), item, {active: item === currentPage}) : ellipsis());
    });
    pagination.appendChild(button('Next <span>→</span>', currentPage + 1, {arrow: true, disabled: currentPage === totalPages, ariaLabel: 'Next page'}));
  };

  const render = shouldScroll => {
    const matches = getMatches();
    const totalPages = Math.max(1, Math.ceil(matches.length / pageSize));
    currentPage = Math.min(Math.max(currentPage, 1), totalPages);
    const start = (currentPage - 1) * pageSize;
    const visible = new Set(matches.slice(start, start + pageSize));
    cards.forEach(card => { card.hidden = !visible.has(card); });

    resultText.innerHTML = `<strong>${matches.length}</strong> ${matches.length === 1 ? 'guide' : 'guides'}`;
    clearButton.hidden = input.value.length === 0;
    emptyState.hidden = matches.length !== 0;
    grid.hidden = matches.length === 0;
    renderPagination(matches.length ? totalPages : 0);
    updateUrl();

    if (shouldScroll) {
      document.querySelector('.blog-tools').scrollIntoView({behavior: 'smooth', block: 'start'});
    }
  };

  const clearSearch = () => {
    input.value = '';
    currentPage = 1;
    render(false);
    input.focus();
  };

  input.addEventListener('input', () => {
    currentPage = 1;
    render(false);
  });
  clearButton.addEventListener('click', clearSearch);
  emptyState.querySelector('button').addEventListener('click', clearSearch);

  const params = new URLSearchParams(window.location.search);
  input.value = params.get('q') || '';
  currentPage = Number.parseInt(params.get('page') || '1', 10) || 1;
  window.matchMedia('(max-width: 620px)').addEventListener('change', () => render(false));
  render(false);
})();
