// Google AdSense + JPG2Go Ad Unit
(function() {
  var script = document.createElement('script');
  script.async = true;
  script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4542839087220625';
  script.crossOrigin = 'anonymous';
  script.onload = function() {
    var container = document.getElementById('jpg2go-ad');
    if (!container) {
      container = document.createElement('div');
      container.id = 'jpg2go-ad';
      document.body.appendChild(container);
    }
    var ins = document.createElement('ins');
    ins.className = 'adsbygoogle';
    ins.style.display = 'block';
    ins.setAttribute('data-ad-client', 'ca-pub-4542839087220625');
    ins.setAttribute('data-ad-slot', '5563960436');
    ins.setAttribute('data-ad-format', 'auto');
    ins.setAttribute('data-full-width-responsive', 'true');
    container.appendChild(ins);
    (window.adsbygoogle = window.adsbygoogle || []).push({});
  };
  document.head.appendChild(script);
})();
