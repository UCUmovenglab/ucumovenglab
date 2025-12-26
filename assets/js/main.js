// Movement Engineering Lab - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
  // Mobile menu toggle
  const menuToggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('nav');

  if (menuToggle && nav) {
    menuToggle.addEventListener('click', function() {
      nav.classList.toggle('show');
    });
  }

  // Simple search functionality
  const searchInput = document.getElementById('search-input');
  const searchInfo = document.getElementById('search-info');
  const searchCount = document.getElementById('search-count');

  if (searchInput) {
    searchInput.addEventListener('input', function() {
      const query = this.value.toLowerCase().trim();
      const items = document.querySelectorAll('.citation, .card, .post-excerpt');
      let visibleCount = 0;

      items.forEach(function(item) {
        const text = item.textContent.toLowerCase();
        if (query === '' || text.includes(query)) {
          item.style.display = '';
          visibleCount++;
        } else {
          item.style.display = 'none';
        }
      });

      if (searchInfo && searchCount) {
        if (query !== '') {
          searchInfo.style.display = 'block';
          searchCount.textContent = visibleCount;
        } else {
          searchInfo.style.display = 'none';
        }
      }
    });
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
});
