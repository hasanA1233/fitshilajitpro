// FitShilajitPro — small helpers (no libraries)
(function () {
  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var links = document.querySelector('.nav-links');
  if (btn && links) {
    btn.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Copy coupon code
  document.querySelectorAll('[data-copy]').forEach(function (el) {
    el.addEventListener('click', function () {
      var code = el.getAttribute('data-copy');
      var done = function () {
        var old = el.textContent;
        el.textContent = 'Copied!';
        setTimeout(function () { el.textContent = old; }, 1400);
      };
      if (navigator.clipboard) navigator.clipboard.writeText(code).then(done, done);
      else done();
    });
  });

  // Pass ad click id (?clickid= or ?subid=) through to affiliate links for tracking
  try {
    var params = new URLSearchParams(window.location.search);
    var cid = params.get('clickid') || params.get('subid');
    if (cid) {
      document.querySelectorAll('a[data-aff]').forEach(function (a) {
        var u = new URL(a.href);
        u.searchParams.set('subid', cid);
        a.href = u.toString();
      });
    }
  } catch (e) {}

  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
