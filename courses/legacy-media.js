(() => {
  const legacyPathFor = (course) => {
    try {
      const url = new URL(course.url, window.location.origin);
      const parts = url.pathname.split('/').filter(Boolean);
      const slug = parts[parts.length - 1];
      return `../assets/images/courses/legacy/${slug}.png`;
    } catch (_) {
      return course.image;
    }
  };

  if (typeof courses !== 'undefined' && Array.isArray(courses)) {
    courses.forEach(course => {
      course.image = legacyPathFor(course);
    });
  }

  const refreshVisibleCards = () => {
    document.querySelectorAll('.catalog-course-card').forEach(card => {
      const link = card.querySelector('a[href]');
      const img = card.querySelector('.thumb img');
      if (!link || !img) return;
      try {
        const url = new URL(link.getAttribute('href'), window.location.origin);
        const parts = url.pathname.split('/').filter(Boolean);
        const slug = parts[parts.length - 1];
        img.src = `../assets/images/courses/legacy/${slug}.png`;
        img.style.display = '';
      } catch (_) {}
    });
  };

  refreshVisibleCards();

  const grid = document.getElementById('allCourseGrid');
  if (grid) {
    const observer = new MutationObserver(refreshVisibleCards);
    observer.observe(grid, { childList: true, subtree: true });
  }
})();
