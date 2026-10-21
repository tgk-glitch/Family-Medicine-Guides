"""Wire counselling.html into nav (all pages), directory, homepage and search index."""
import re, json, glob, sys
SITE = '/home/claude/merge/site'
TONE = '#9C4F2E'
CHEV = '<svg class="fmg-chev" width="8" height="14" viewBox="0 0 8 14" fill="none"><path d="M1 1l6 6-6 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def row(href, label, sub, dot=TONE):
    return ('<a href="%s" class="fmg-row"><span class="fmg-row-main"><span class="fmg-row-dot" style="background:%s"></span>'
            '<span class="fmg-row-text"><span class="fmg-row-label">%s</span><span class="fmg-row-sub">%s</span></span></span>%s</a>' % (href, dot, label, sub, CHEV))

def once(s, old, new, what):
    c = s.count(old)
    assert c == 1, '%s: found %d' % (what, c)
    return s.replace(old, new)

idx = open(SITE + '/index.html', encoding='utf-8').read()
a = idx.find('<!-- FMG-NAV:START -->'); b = idx.find('<!-- FMG-NAV:END -->') + len('<!-- FMG-NAV:END -->')
nav = idx[a:b]

if 'counselling.html' not in nav:
    # 1. live panel — after Mental Health row
    mh = row('mental-health.html', 'Mental Health', 'PHQ-9 · GAD-7 · ISI', '#5C4A8A')
    nav = once(nav, mh, mh + '\n' + row('counselling.html', 'Counselling', '5A’s · FRAMES · MI · BATHE · bilingual'), 'live mental row')
    # 2. mental category panel — add before its Planned label
    i = nav.find('data-panel="cat-mental"'); j = nav.find('<div class="fmg-menu-section-label">Planned</div>', i)
    nav = nav[:j] + row('counselling.html', 'Counselling in family medicine', 'stages of change · MI · BATHE · strategy chooser') + '\n' + nav[j:]
    # 3. respiratory: smoking cessation planned -> live
    old = ('<div class="fmg-row fmg-row-disabled"><span class="fmg-row-main"><span class="fmg-row-dot" style="background:#2C7A6B"></span>'
           '<span class="fmg-row-text"><span class="fmg-row-label">Smoking cessation</span><span class="fmg-row-sub">incl. shisha/bukhoor/medwakh counseling</span></span></span><span class="fmg-plan-pill">Planned</span></div>\n')
    nav = once(nav, old, '', 'resp smoking planned')
    i = nav.find('data-panel="cat-resp"'); j = nav.find('<div class="fmg-menu-section-label">Planned</div>', i)
    nav = nav[:j] + row('counselling.html#smoking', 'Smoking cessation', 'incl. shisha & medwakh · HSI · Sehhaty clinics', '#2C7A6B') + '\n' + nav[j:]
    # 4. counts in the specialties panel
    nav = once(nav, '<span class="fmg-row-label">Respiratory (Adult)</span><span class="fmg-row-sub">2 live · 6 planned</span>',
               '<span class="fmg-row-label">Respiratory (Adult)</span><span class="fmg-row-sub">3 live · 5 planned</span>', 'resp count')

assert '<!-- FMG-NAV:START -->' in nav and nav.endswith('<!-- FMG-NAV:END -->')

# write the nav into every page
for f in sorted(glob.glob(SITE + '/*.html')):
    s = open(f, encoding='utf-8').read()
    a = s.find('<!-- FMG-NAV:START -->'); b = s.find('<!-- FMG-NAV:END -->') + len('<!-- FMG-NAV:END -->')
    if a < 0:
        print('no nav in', f); continue
    s = s[:a] + nav + s[b:]
    open(f, 'w', encoding='utf-8').write(s)

# homepage: quick pill + resp card count + resp card tags
idx = open(SITE + '/index.html', encoding='utf-8').read()
if 'quick-pill" style="--pc:%s' % TONE not in idx:
    pill = '<a href="mental-health.html" class="quick-pill" style="--pc:#5C4A8A"><span class="quick-dot"></span>Mental Health</a>'
    idx = once(idx, pill, pill + '\n      <a href="counselling.html" class="quick-pill" style="--pc:%s"><span class="quick-dot"></span>Counselling · EN / ع</a>' % TONE, 'quick pill')
    i = idx.find('href="categories.html#cat-resp" class="cat-card"'); j = idx.find('<span class="cat-count">2 live · 6 planned</span>', i)
    assert 0 < j - i < 3000
    idx = idx[:j] + '<span class="cat-count">3 live · 5 planned</span>' + idx[j + len('<span class="cat-count">2 live · 6 planned</span>'):]
    i = idx.find('href="categories.html#cat-mental" class="cat-card"')
    if i > 0:
        k = idx.find('data-tags="', i) + len('data-tags="')
        idx = idx[:k] + 'counselling motivational interviewing stages of change five a&#x27;s frames bathe ' + idx[k:]
open(SITE + '/index.html', 'w', encoding='utf-8').write(idx)

# categories directory
cat = open(SITE + '/categories.html', encoding='utf-8').read()
if 'counselling.html' not in cat.split('<!-- FMG-NAV:END -->')[1]:
    old = ('<div class="dir-row dir-planned"><span class="dir-dot" style="background:#2C7A6B"></span><span class="dir-text"><span class="dir-title">Smoking cessation</span>'
           '<span class="dir-sub">incl. shisha/bukhoor/medwakh counseling</span></span><span class="dir-pill">Planned</span></div>')
    cat = once(cat, old, '', 'dir smoking planned')
    live_resp = ('<a class="dir-row dir-live" href="urgent-care.html#asthma-exacerbation-adult"><span class="dir-dot" style="background:#2C7A6B"></span><span class="dir-text">'
                 '<span class="dir-title">Asthma Exacerbation (SINA)</span><span class="dir-sub">urgent care protocol</span></span><span class="dir-open">Open →</span></a>')
    cat = once(cat, live_resp, live_resp + '<a class="dir-row dir-live" href="counselling.html#smoking"><span class="dir-dot" style="background:#2C7A6B"></span><span class="dir-text">'
               '<span class="dir-title">Smoking cessation</span><span class="dir-sub">incl. shisha &amp; medwakh · HSI · Sehhaty clinics</span></span><span class="dir-open">Open →</span></a>', 'dir resp live')
    i = cat.find('id="cat-resp"'); j = cat.find('<p class="dir-count">2 live · 6 planned</p>', i)
    assert 0 < j - i < 3000, 'resp count'
    cat = cat[:j] + '<p class="dir-count">3 live · 5 planned</p>' + cat[j + len('<p class="dir-count">2 live · 6 planned</p>'):]
    i = cat.find('id="cat-mental"'); j = cat.find('<p class="dir-count">7 live · 7 planned</p>', i)
    assert 0 < j - i < 3000, 'mental count'
    cat = cat[:j] + '<p class="dir-count">8 live · 7 planned</p>' + cat[j + len('<p class="dir-count">7 live · 7 planned</p>'):]
    k = cat.find('<h3 class="dir-group"', cat.find('<h3 class="dir-group" id="live-2">Live</h3>') + 10)
    cat = cat[:k] + ('<a class="dir-row dir-live" href="counselling.html"><span class="dir-dot" style="background:%s"></span><span class="dir-text">'
                     '<span class="dir-title">Counselling in family medicine</span><span class="dir-sub">stages of change · 5A’s · FRAMES · MI · BATHE · bilingual</span></span><span class="dir-open">Open →</span></a>' % TONE) + cat[k:]
open(SITE + '/categories.html', 'w', encoding='utf-8').write(cat)

# search index
si = open(SITE + '/search-index.js', encoding='utf-8').read()
pre = 'window.FMG_SEARCH_INDEX = '
arr = json.loads(si[len(pre):].rstrip().rstrip(';'))
arr = [e for e in arr if e.get('guide') != 'counselling.html']
arr += json.load(open('/home/claude/merge/B/counselling-source/counselling_entries.json', encoding='utf-8'))
open(SITE + '/search-index.js', 'w', encoding='utf-8').write(pre + json.dumps(arr, ensure_ascii=False) + ';\n')
print('index entries', len(arr))
