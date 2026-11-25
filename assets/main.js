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
  // ----- Mobile slide-out menu -----
  var openBtn = document.querySelector('.menu-btn');
  var nav = document.getElementById('site-nav');
  var backdrop = document.querySelector('.nav-backdrop');
  var closeBtn = nav ? nav.querySelector('.nav-close') : null;
  var mobile = window.matchMedia('(max-width: 899px)');

  function focusables() {
    return nav.querySelectorAll('a[href], button:not([disabled])');
  }
  function setOpen(open) {
    nav.classList.toggle('is-open', open);
    if (backdrop) backdrop.classList.toggle('is-open', open);
    document.body.classList.toggle('nav-open', open);
    openBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) {
      nav.setAttribute('role', 'dialog');
      nav.setAttribute('aria-modal', 'true');
      (closeBtn || focusables()[0]).focus();
    } else {
      nav.removeAttribute('role');
      nav.removeAttribute('aria-modal');
    }
  }
  if (openBtn && nav) {
    openBtn.addEventListener('click', function () { setOpen(true); });
    if (closeBtn) closeBtn.addEventListener('click', function () { setOpen(false); openBtn.focus(); });
    if (backdrop) backdrop.addEventListener('click', function () { setOpen(false); });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a') && mobile.matches) setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (!nav.classList.contains('is-open')) return;
      if (e.key === 'Escape') { setOpen(false); openBtn.focus(); return; }
      if (e.key === 'Tab') {
        var f = focusables(), first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
    var onChange = function () { if (!mobile.matches && nav.classList.contains('is-open')) setOpen(false); };
    if (mobile.addEventListener) mobile.addEventListener('change', onChange);
  }

  // ----- Keep every affiliate link on the central redirect -----
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

  // ----- Footer year -----
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
