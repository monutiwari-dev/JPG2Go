// Google Analytics (load-analytics.js)
(function(){var s=document.createElement('script');s.src='load-analytics.js';s.async=true;document.head.appendChild(s);})();

// Load footer from external file
document.addEventListener('DOMContentLoaded', function() {
  const footerPlaceholder = document.getElementById('footer-placeholder');
  if (footerPlaceholder) {
    fetch('footer.html')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to load footer.html');
        }
        return response.text();
      })
      .then(html => {
        footerPlaceholder.outerHTML = html;
      })
      .catch(error => {
        console.error('Error loading footer:', error);
      });
  }
});
