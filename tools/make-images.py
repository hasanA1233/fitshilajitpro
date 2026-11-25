"""Generate FitShilajitPro's own illustrations (SVG sources) in the Himalayan Premium palette.

Writes SVG files to assets/img/src/. Convert to WebP with:
    node tools/svg-to-webp.mjs        (needs `npm i sharp` somewhere on NODE_PATH)
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'assets', 'img', 'src')
os.makedirs(SRC, exist_ok=True)

BG, STONE, BORDER, INK, GOLD, GOLD_D, MUTED = '#FAF8F5', '#E9E4DC', '#E2DCD2', '#1C1A17', '#B8893B', '#94692A', '#6B645B'


def write(name, svg):
    with open(os.path.join(SRC, name + '.svg'), 'w') as f:
        f.write(svg)


def ranges(w, h, base):
    """Two soft layered mountain ranges plus a thin gold ridge line, scaled to w x h."""
    def pts(seq):
        return ' '.join(f'L{x * w / 100:.0f} {y * h / 100:.0f}' for x, y in seq)
    far = [(0, base - 8), (12, base - 24), (22, base - 14), (34, base - 34), (46, base - 16), (58, base - 28), (70, base - 12), (82, base - 30), (92, base - 18), (100, base - 22)]
    near = [(0, base + 6), (14, base - 8), (26, base + 2), (40, base - 14), (54, base + 4), (66, base - 6), (80, base + 6), (92, base - 4), (100, base)]
    farp = f'M0 {h} {pts(far)} L{w} {h}Z'
    nearp = f'M0 {h} {pts(near)} L{w} {h}Z'
    ridge = 'M' + pts(far)[1:]
    # snow caps on the two tallest far peaks
    caps = ''
    for x, y in ((34, base - 34), (82, base - 30)):
        cx, cy = x * w / 100, y * h / 100
        s = h * 0.045
        caps += f'<path d="M{cx - s * 1.6:.0f} {cy + s:.0f} L{cx:.0f} {cy:.0f} L{cx + s * 1.6:.0f} {cy + s:.0f} L{cx + s * .5:.0f} {cy + s * .6:.0f} L{cx:.0f} {cy + s * 1.1:.0f} L{cx - s * .6:.0f} {cy + s * .6:.0f}Z" fill="#FFFFFF" opacity=".85"/>'
    return (f'<path d="{farp}" fill="#DDD5C8"/>{caps}'
            f'<path d="{ridge}" fill="none" stroke="{GOLD}" stroke-width="{max(1.5, w / 600):.1f}" opacity=".55"/>'
            f'<path d="{nearp}" fill="#D2C8B8"/>')


def defs(w, h):
    return (f'<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="{STONE}"/></linearGradient>'
            f'<radialGradient id="sun"><stop offset="0" stop-color="{GOLD}" stop-opacity=".28"/>'
            f'<stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="resin" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3A2A1A"/>'
            f'<stop offset="1" stop-color="{INK}"/></linearGradient></defs>')


# ---------- hero (wide, soft mountains on warm off-white) ----------
def hero(w, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{defs(w, h)}'
            f'<rect width="{w}" height="{h}" fill="url(#sky)"/>'
            f'<circle cx="{w * .78:.0f}" cy="{h * .30:.0f}" r="{h * .32:.0f}" fill="url(#sun)"/>'
            f'<circle cx="{w * .78:.0f}" cy="{h * .30:.0f}" r="{h * .07:.0f}" fill="none" stroke="{GOLD}" stroke-width="2" opacity=".6"/>'
            + ranges(w, h, 78) + '</svg>')


write('hero-mountains', hero(1600, 640))


# ---------- What's inside: resin drop with mineral dots ----------
minerals = ''.join(
    f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'
    for x, y, r, c in [(170, 250, 14, GOLD), (640, 220, 10, GOLD_D), (600, 520, 16, GOLD), (180, 560, 9, GOLD_D),
                       (690, 380, 7, MUTED), (120, 410, 7, MUTED), (250, 150, 6, MUTED), (560, 130, 8, GOLD)])
orbit = f'<ellipse cx="400" cy="420" rx="300" ry="120" fill="none" stroke="{GOLD}" stroke-width="2" stroke-dasharray="4 10" opacity=".7" transform="rotate(-14 400 420)"/>'
write('resin-drop', (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">{defs(800, 800)}'
    f'<rect width="800" height="800" rx="0" fill="url(#sky)"/>'
    f'<circle cx="400" cy="400" r="300" fill="url(#sun)"/>'
    + ranges(800, 800, 92) + orbit +
    f'<path d="M400 140 C400 140 250 340 250 460 a150 150 0 0 0 300 0 C550 340 400 140 400 140Z" fill="url(#resin)"/>'
    f'<path d="M400 140 C400 140 250 340 250 460 a150 150 0 0 0 300 0 C550 340 400 140 400 140Z" fill="none" stroke="{GOLD}" stroke-width="4"/>'
    f'<path d="M318 430 c0 -40 22 -88 48 -126" fill="none" stroke="#F3E3C0" stroke-width="10" stroke-linecap="round" opacity=".55"/>'
    + minerals + '</svg>'))


# ---------- article thumbnails: shared scene + one gold line motif each ----------
ICONS = {
    'what-is-shilajit': 'M50 12C50 12 24 44 24 62a26 26 0 0 0 52 0C76 44 50 12 50 12Z M38 62a12 12 0 0 0 12 12',
    'shilajit-benefits': 'M50 34a16 16 0 1 0 0.01 0Z M50 12v10 M50 78v10 M12 50h10 M78 50h10 M23 23l7 7 M70 70l7 7 M77 23l-7 7 M30 70l-7 7',
    'how-to-take-shilajit-resin': 'M20 44h50v14a25 25 0 0 1-50 0z M70 50h6a9 9 0 0 1 0 18h-8 M34 16c-5 7 5 11 0 18 M48 16c-5 7 5 11 0 18 M16 90h62',
    'best-time-to-take-shilajit': 'M50 18a32 32 0 1 0 0.01 0Z M50 30v20l14 10 M50 12v4 M50 84v4',
    'shilajit-for-men': 'M10 84L40 36l14 20 10-14 26 42Z M40 36V14l16 7-16 7',
    'shilajit-for-women': 'M50 80C38 66 38 44 50 26C62 44 62 66 50 80Z M50 80C34 78 20 66 16 48C34 50 46 62 50 80Z M50 80C66 78 80 66 84 48C66 50 54 62 50 80Z',
    'shilajit-for-athletes': 'M18 50h64 M26 36v28 M34 28v44 M74 36v28 M66 28v44',
    'shilajit-side-effects': 'M50 12L80 24V48C80 68 66 80 50 88C34 80 20 68 20 48V24Z M36 50l10 10 20-22',
    'how-to-spot-fake-shilajit': 'M42 16a26 26 0 1 0 0.01 0Z M61 61L86 86 M42 28C42 28 30 42 30 50a12 12 0 0 0 24 0C54 42 42 28 42 28Z',
    'altai-vs-himalayan-shilajit': 'M4 80L26 42l18 30 M56 80L76 30l20 50 M50 22v8 M50 40v8 M50 58v8 M50 76v6',
    'shilajit-and-fulvic-acid': 'M50 22a8 8 0 1 0 0.01 0Z M24 62a8 8 0 1 0 0.01 0Z M76 62a8 8 0 1 0 0.01 0Z M50 80a6 6 0 1 0 0.01 0Z M45 36L29 56 M55 36L71 56 M32 66l14 10 M68 66l-14 10',
    'shilajit-resin-vs-capsules-vs-powder': 'M14 70L36 48a10 10 0 0 1 14 14L28 84a10 10 0 0 1-14-14Z M25 59l14 14 M58 40h28v40a6 6 0 0 1-6 6H64a6 6 0 0 1-6-6Z M56 32h32v8H56Z',
}
for slug, d in ICONS.items():
    w, h = 800, 500
    write('thumb-' + slug, (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{defs(w, h)}'
        f'<rect width="{w}" height="{h}" fill="url(#sky)"/>'
        f'<circle cx="400" cy="210" r="190" fill="url(#sun)"/>'
        + ranges(w, h, 84) +
        f'<circle cx="400" cy="220" r="118" fill="#FFFFFF" stroke="{BORDER}" stroke-width="2"/>'
        f'<circle cx="400" cy="220" r="104" fill="none" stroke="{GOLD}" stroke-width="1.5" opacity=".6"/>'
        f'<g transform="translate(330 150) scale(1.4)" fill="none" stroke="{GOLD_D}" stroke-width="4.2" stroke-linecap="round" stroke-linejoin="round"><path d="{d}"/></g>'
        '</svg>'))


print('SVG sources written to', SRC)
