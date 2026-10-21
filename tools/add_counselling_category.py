"""Add a top-level "Counselling & Communication" category (cat-counsel) to the
homepage, the topic directory and the shared menu, then copy the menu to every
page. Idempotent (marker FMG-CAT-COUNSEL) and safe on the full 17-page copy.

usage: python3 add_counselling_category.py SITE_DIR
Run after counselling.html is in SITE_DIR (update_site.py already run).
"""
import sys, glob, pathlib

SITE = pathlib.Path(sys.argv[1])
TONE = '#9C4F2E'
MARK = 'FMG-CAT-COUNSEL'
CHEV = ('<svg class="fmg-chev" width="8" height="14" viewBox="0 0 8 14" fill="none"><path d="M1 1l6 6-6 6" '
        'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
BACK = ('<button class="fmg-back" data-back="cats"><svg width="8" height="14" viewBox="0 0 8 14" fill="none"><path d="M7 1L1 7l6 6" '
        'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg> Back</button>')
ICON = ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">'
        '<path d="M4 5h11a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H9l-4 3v-3H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z" stroke-linejoin="round"/>'
        '<path d="M19 9h1a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-1v3l-3.5-3H12" stroke-linecap="round" stroke-linejoin="round"/></svg>')

TITLE = 'Counselling &amp; Communication'
BLURB = 'The consultation is the treatment — behaviour change, difficult news and shared decisions.'
LIVE = [  # (href, title, sub)
    ('counselling.html', 'Counselling in family medicine', 'foundations · bilingual EN / ع'),
    ('counselling.html#stages', 'Stages of change &amp; the 5 A’s', 'readiness ruler · strategy chooser'),
    ('counselling.html#frames', 'Brief interventions (FRAMES)', 'alcohol · substances · lifestyle'),
    ('counselling.html#mi', 'Motivational interviewing', 'OARS · change talk · rolling with resistance'),
    ('counselling.html#bathe', 'BATHE — the 15-minute psychotherapy', 'psychosocial check in any visit'),
    ('counselling.html#smoking', 'Smoking cessation', 'incl. shisha &amp; medwakh · HSI · Sehhaty clinics'),
]
PLANNED = [
    ('Breaking bad news', 'SPIKES'),
    ('Shared decision-making', 'risk communication · decision aids'),
    ('Weight &amp; physical-activity counselling', ''),
    ('Medication adherence', ''),
    ('Difficult consultations', 'angry or demanding patient · requests for antibiotics or opioids'),
]
COUNT = f'{len(LIVE)} live · {len(PLANNED)} planned'
TAGS = ('counselling counseling communication motivational interviewing mi oars change talk stages of change '
        'transtheoretical five a&#x27;s 5a frames brief intervention bathe psychosocial smoking cessation tobacco '
        'shisha medwakh nicotine varenicline breaking bad news spikes shared decision making adherence')


def once(s, old, new, what):
    n = s.count(old)
    assert n == 1, f'{what}: found {n}'
    return s.replace(old, new)


def nav_row(href, label, sub):
    return (f'<a href="{href}" class="fmg-row"><span class="fmg-row-main"><span class="fmg-row-dot" style="background:{TONE}"></span>'
            f'<span class="fmg-row-text"><span class="fmg-row-label">{label}</span><span class="fmg-row-sub">{sub}</span></span></span>{CHEV}</a>')


def nav_planned(label, sub):
    s = f'<span class="fmg-row-sub">{sub}</span>' if sub else ''
    return (f'<div class="fmg-row fmg-row-disabled"><span class="fmg-row-main"><span class="fmg-row-dot" style="background:{TONE}"></span>'
            f'<span class="fmg-row-text"><span class="fmg-row-label">{label}</span>{s}</span></span><span class="fmg-plan-pill">Planned</span></div>')


def dir_live(href, t, sub):
    return (f'<a class="dir-row dir-live" href="{href}"><span class="dir-dot" style="background:{TONE}"></span><span class="dir-text">'
            f'<span class="dir-title">{t}</span><span class="dir-sub">{sub}</span></span><span class="dir-open">Open →</span></a>')


def dir_planned(t, sub):
    s = f'<span class="dir-sub">{sub}</span>' if sub else ''
    return (f'<div class="dir-row dir-planned"><span class="dir-dot" style="background:{TONE}"></span><span class="dir-text">'
            f'<span class="dir-title">{t}</span>{s}</span><span class="dir-pill">Planned</span></div>')


def split_nav(s):
    a = s.find('<!-- FMG-NAV:START -->'); b = s.find('<!-- FMG-NAV:END -->') + len('<!-- FMG-NAV:END -->')
    return a, b


# ---------- 1. shared menu (built on index.html, then copied to every page)
idx_p = SITE / 'index.html'
idx = idx_p.read_text(encoding='utf-8')
a, b = split_nav(idx)
nav = idx[a:b]
if MARK not in nav:
    btn_mental_start = nav.find('<button class="fmg-row" data-goto="cat-mental">')
    btn_mental_end = nav.find('</button>', btn_mental_start) + len('</button>')
    assert btn_mental_start > 0
    # stale count on the Mental Health button -> match the directory
    btn = nav[btn_mental_start:btn_mental_end]
    import re
    btn_fixed = re.sub(r'<span class="fmg-row-sub">[^<]*</span>', '<span class="fmg-row-sub">8 live · 7 planned</span>', btn, count=1)
    new_btn = (f'\n<!-- {MARK}:BTN --><button class="fmg-row" data-goto="cat-counsel"><span class="fmg-row-main"><span class="fmg-row-text">'
               f'<span class="fmg-row-label">{TITLE}</span><span class="fmg-row-sub">{COUNT}</span></span></span>{CHEV}</button>')
    nav = nav[:btn_mental_start] + btn_fixed + new_btn + nav[btn_mental_end:]
    nav = once(nav, '<span class="fmg-row-sub">21 categories</span>', '<span class="fmg-row-sub">22 categories</span>', 'menu count')
    # panel after the cat-mental panel
    p0 = nav.find('<div class="fmg-panel" data-panel="cat-mental">')
    p1 = nav.find('<div class="fmg-panel"', p0 + 10)
    panel = (f'<!-- {MARK}:PANEL -->\n<div class="fmg-panel" data-panel="cat-counsel">\n{BACK}\n'
             '<div class="fmg-menu-section-label">Live</div>\n'
             + '\n'.join(nav_row(*r) for r in LIVE) + '\n'
             '<div class="fmg-menu-section-label">Planned</div>\n'
             + '\n'.join(nav_planned(*r) for r in PLANNED) + '\n</div>\n')
    nav = nav[:p1] + panel + nav[p1:]
    idx = idx[:a] + nav + idx[b:]

# ---------- 2. homepage card after Mental Health
body_at = idx.find('<!-- FMG-NAV:END -->')
if f'<!-- {MARK}:CARD -->' not in idx:
    j = idx.find('<a href="mental-health.html" class="cat-card"', body_at)
    k = idx.find('</a>', j) + len('</a>')
    assert j > 0
    card = (f'\n      <!-- {MARK}:CARD --><a href="categories.html#cat-counsel" class="cat-card" style="--tag-color:{TONE}" data-tags="{TAGS}">\n'
            f'        <div class="cat-icon">{ICON}</div>\n'
            f'        <h3>{TITLE}</h3>\n'
            f'        <p>{BLURB}</p>\n'
            f'        <span class="cat-count">{COUNT}</span>\n      </a>')
    idx = idx[:k] + card + idx[k:]
idx_p.write_text(idx, encoding='utf-8')

# ---------- 3. directory: chip + section after Mental Health
cat_p = SITE / 'categories.html'
cat = cat_p.read_text(encoding='utf-8')
cb = cat.find('<!-- FMG-NAV:END -->')
if f'<!-- {MARK}:SECTION -->' not in cat:
    chip = '<a class="dir-chip" href="#cat-mental" style="--tag-color:#5C4A8A">Mental Health</a>'
    head, tail = cat[:cb], cat[cb:]
    tail = once(tail, chip, chip + f'<a class="dir-chip" href="#cat-counsel" style="--tag-color:{TONE}">{TITLE}</a>', 'dir chip')
    s0 = tail.find('id="cat-mental"'); s1 = tail.find('</section>', s0) + len('</section>')
    sec = (f'\n<!-- {MARK}:SECTION --><section class="dir-cat" id="cat-counsel" style="--tag-color:{TONE}">\n<div class="dir-cat-head">\n'
           f'<div class="dir-cat-icon">{ICON}</div>\n<div>\n<h2 id="counselling-communication">{TITLE}</h2>\n'
           f'<p class="dir-blurb">{BLURB}</p>\n<p class="dir-count">{COUNT}</p>\n</div>\n</div>\n'
           '<h3 class="dir-group" id="live-cs">Live</h3>' + ''.join(dir_live(*r) for r in LIVE)
           + '<h3 class="dir-group" id="planned-cs">Planned</h3>' + ''.join(dir_planned(*r) for r in PLANNED) + '</section>')
    tail = tail[:s1] + sec + tail[s1:]
    cat = head + tail
cat_p.write_text(cat, encoding='utf-8')

# ---------- 4. copy the menu to every page
for f in sorted(SITE.glob('*.html')):
    s = f.read_text(encoding='utf-8')
    a2, b2 = split_nav(s)
    if a2 < 0:
        print('no nav in', f.name); continue
    s = s[:a2] + nav + s[b2:]
    f.write_text(s, encoding='utf-8')
print('category cat-counsel ready:', COUNT)
