// FitShilajitPro — small helpers (no libraries)

// Affiliate config. The real merchant URL lives in ONE place: the /_redirects file
// (/go/shilajit -> https://www.purehimalayanshilajit.com/?ref=4878). Every button links to
// AFFILIATE_URL; change the destination in _redirects, not here.
var AFFILIATE_URL = '/go/shilajit';
// Ad click-id passthrough (?clickid= / ?subid= on landing URL). Off until the
// Pure Himalayan Shilajit program confirms it accepts an extra parameter. To enable,
// set the parameter name the program expects, e.g. 'subid'.
var AFFILIATE_SUBID_PARAM = null;

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

  // Keep every affiliate link on the central redirect
  document.querySelectorAll('a[data-aff]').forEach(function (a) {
    a.setAttribute('href', AFFILIATE_URL);
  });

  // Optional: pass ad click id through to affiliate links (disabled by default)
  if (AFFILIATE_SUBID_PARAM) {
    try {
      var params = new URLSearchParams(window.location.search);
      var cid = params.get('clickid') || params.get('subid');
      if (cid) {
        document.querySelectorAll('a[data-aff]').forEach(function (a) {
          var u = new URL(a.href);
          u.searchParams.set(AFFILIATE_SUBID_PARAM, cid);
          a.href = u.toString();
        });
      }
    } catch (e) {}
  }

  // Closable sticky CTA on mobile (stays closed for the rest of the visit)
  var bar = document.getElementById('sticky-cta');
  if (bar) {
    var closed = false;
    try { closed = sessionStorage.getItem('stickyCtaClosed') === '1'; } catch (e) {}
    if (closed) {
      bar.hidden = true;
    } else {
      document.body.classList.add('has-sticky');
    }
    var close = bar.querySelector('.sticky-cta__close');
    if (close) {
      close.addEventListener('click', function () {
        bar.hidden = true;
        document.body.classList.remove('has-sticky');
        try { sessionStorage.setItem('stickyCtaClosed', '1'); } catch (e) {}
      });
    }
  }

  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
