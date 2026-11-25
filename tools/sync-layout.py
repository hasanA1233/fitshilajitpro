#!/usr/bin/env python3
"""Single source for the shared layout (head assets, top bar, header, menu, footer).

Edit the templates below, then run from the project root:
    python3 tools/sync-layout.py
Every *.html page gets the blocks between <!-- layout:NAME --> ... <!-- /layout:NAME --> rewritten.
Page content, titles, meta tags and JSON-LD are never touched.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AFF = 'href="/go/shilajit" data-aff rel="sponsored nofollow noopener" target="_blank"'

HEAD = '''<link rel="preload" href="/assets/fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/cormorant-garamond-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/styles.css">'''

LOGO_MARK = ('<svg viewBox="0 0 26 26" aria-hidden="true"><circle cx="13" cy="13" r="12.5" fill="#1C1A17"/>'
             '<path d="M5 18l5-7 3 4 3.2-5.2L21 18" fill="none" stroke="#B8893B" stroke-width="1.8" '
             'stroke-linejoin="round" stroke-linecap="round"/></svg>')

NAV = [('Home', '/'), ('Benefits', '/blog/shilajit-benefits/'), ('Guides', '/blog/'),
       ('Reviews', '/#review'), ('FAQ', '/#faq')]

HEADER = '''<a class="skip" href="#main">Skip to content</a>
<div class="topbar">Independent review site, not the official store. We may earn a commission from links on this site. <a href="/affiliate-disclosure/">Affiliate disclosure</a></div>
<header class="site-header">
<div class="container header-inner">
<a href="/" class="logo" aria-label="FitShilajitPro home">{logo}FitShilajit<span>Pro</span></a>
<nav class="nav" id="site-nav" aria-label="Main">
<div class="nav-head"><span class="logo" aria-hidden="true">FitShilajit<span>Pro</span></span><button class="nav-close" type="button" aria-label="Close menu"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button></div>
<ul class="nav-list">
{items}
</ul>
</nav>
<a class="btn btn-sm header-cta" {aff}>Check Price</a>
<button class="menu-btn" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="Open menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div>
<div class="nav-backdrop" aria-hidden="true"></div>
</header>'''

FOOTER = '''<footer class="site-footer">
<div class="container">
<div class="footer-grid">
<div class="footer-about">
<a href="/" class="logo">FitShilajit<span>Pro</span></a>
<p>FitShilajitPro is an independent, reader-supported guide to shilajit. We are not the manufacturer or seller of any product we write about. When you buy through links on this site we may earn an affiliate commission at no extra cost to you.</p>
</div>
<div class="footer-col">
<h2>Guides</h2>
<ul>
<li><a href="/blog/what-is-shilajit/">What is shilajit?</a></li>
<li><a href="/blog/shilajit-benefits/">Benefits &amp; research</a></li>
<li><a href="/blog/how-to-take-shilajit-resin/">How to take resin</a></li>
<li><a href="/blog/shilajit-side-effects/">Side effects &amp; safety</a></li>
<li><a href="/blog/how-to-spot-fake-shilajit/">Spot fake shilajit</a></li>
<li><a href="/blog/">All guides</a></li>
</ul>
</div>
<div class="footer-col">
<h2>Legal</h2>
<ul>
<li><a href="/affiliate-disclosure/">Affiliate Disclosure</a></li>
<li><a href="/privacy-policy/">Privacy Policy</a></li>
<li><a href="/terms/">Terms of Use</a></li>
</ul>
</div>
</div>
<div class="footer-legal">
<p class="fda">These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.</p>
<p>The content on this site is for information only and is not medical advice. Talk to your doctor before taking supplements, especially if pregnant, breastfeeding, or taking medication.</p>
<p>© <span id="year">2026</span> FitShilajitPro. All rights reserved.</p>
</div>
</div>
</footer>
<script src="/assets/main.js" defer></script>'''


def active_label(rel):
    if rel == 'index.html':
        return 'Home'
    if rel.startswith('blog/shilajit-benefits/'):
        return 'Benefits'
    if rel.startswith('blog/'):
        return 'Guides'
    return None


def render_header(rel):
    cur = active_label(rel)
    current = ' aria-current="page"'
    items = '\n'.join(
        '<li><a href="%s"%s>%s</a></li>' % (href, current if label == cur else '', label)
        for label, href in NAV)
    return HEADER.format(logo=LOGO_MARK, items=items, aff=AFF)


def block(name, body):
    return f'<!-- layout:{name} -->\n{body}\n<!-- /layout:{name} -->'


def put(s, name, body, legacy_pattern, rel):
    marked = re.compile(rf'<!-- layout:{name} -->.*?<!-- /layout:{name} -->', re.S)
    new, n = marked.subn(lambda m: block(name, body), s)
    if n == 1:
        return new
    if n > 1:
        sys.exit(f'{rel}: more than one {name} block')
    new, n = re.subn(legacy_pattern, lambda m: block(name, body), s, count=1, flags=re.S)
    if n != 1:
        sys.exit(f'{rel}: could not place {name} block')
    return new


def main():
    os.chdir(ROOT)
    pages = sorted(p for p in glob.glob('**/*.html', recursive=True)
                   if not p.startswith(('node_modules/', 'tools/')))
    for rel in pages:
        with open(rel) as f:
            s = f.read()
        s = re.sub(r'<meta name="theme-color" content="[^"]*">', '<meta name="theme-color" content="#FAF8F5">', s)
        # legacy patterns are only used the first time (before markers exist)
        s = put(s, 'head', HEAD,
                r'(?:<link rel="preconnect"[^>]*>\n)*(?:<link href="https://fonts\.googleapis\.com[^>]*>\n)?<link rel="stylesheet" href="/assets/style\.css">', rel)
        s = put(s, 'header', render_header(rel), r'<a class="skip".*?</header>', rel)
        s = put(s, 'footer', FOOTER,
                r'<footer class="site-footer">.*?<script src="/assets/main\.js" defer></script>', rel)
        with open(rel, 'w') as f:
            f.write(s)
        print('synced', rel)


if __name__ == '__main__':
    main()
