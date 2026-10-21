"""Apply the credit block, nav rows, homepage band and public search entries
to every page of a Family Medicine Guides site copy. Idempotent: safe to run
again, and safe to run on the author's full 17-page copy.

usage: python3 apply_updates.py SITE_DIR [--entries build/_out/public_entries.json]
Order for a full build:
  1. python3 apply_updates.py SITE          (credit + nav + homepage)
  2. python3 build_leaflets.py SITE         (PDFs + cards)
  3. python3 build_pages.py SITE            (about.html, patients.html)
  4. python3 apply_updates.py SITE --entries _out/public_entries.json   (search)
"""
import sys, os, re, json, pathlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import CREDIT_BLOCK

CHEV = ('<svg class="fmg-chev" width="8" height="14" viewBox="0 0 8 14" fill="none"><path d="M1 1l6 6-6 6" '
        'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def row(href, label, sub, dot):
    return (f'<a href="{href}" class="fmg-row"><span class="fmg-row-main"><span class="fmg-row-dot" style="background:{dot}"></span>'
            f'<span class="fmg-row-text"><span class="fmg-row-label">{label}</span><span class="fmg-row-sub">{sub}</span></span></span>{CHEV}</a>')


NAV_ROWS = ('\n<!-- FMG-NAV-PUBLIC:START -->\n'
            + row('patients.html', 'For patients &amp; families', 'Leaflets in Arabic &amp; English · للمرضى وأسرهم', '#2B6A8C') + '\n'
            + row('about.html', 'About this site', 'Medical editor · how content is reviewed', '#123C38')
            + '\n<!-- FMG-NAV-PUBLIC:END -->\n')

HOME_BAND = """<!-- FMG-PUBLIC:START -->
<style>
  .fmg-public{padding:6px 0 18px;}
  .fmg-public-card{display:flex;gap:18px;align-items:center;justify-content:space-between;flex-wrap:wrap;
    background:#EAF2F7;border:1.5px solid #BCD3E1;border-radius:18px;padding:20px 22px;text-decoration:none;color:#1B2A28;}
  .fmg-public-card:hover{border-color:#2B6A8C;}
  .fmg-public-text{min-width:0;flex:1 1 320px;}
  .fmg-public-eyebrow{font-family:'JetBrains Mono',monospace;font-size:0.7rem;letter-spacing:0.08em;text-transform:uppercase;color:#2B6A8C;margin:0 0 6px;}
  .fmg-public-h{font-family:'Fraunces',serif;font-weight:600;font-size:1.3rem;line-height:1.25;color:#123C38;margin:0 0 4px;}
  .fmg-public-ar{font-family:'IBM Plex Sans Arabic','Inter',sans-serif;font-weight:600;font-size:1.08rem;color:#123C38;margin:0 0 6px;text-align:left;}
  .fmg-public-p{font-size:0.88rem;line-height:1.55;color:#4B5D59;margin:0;}
  .fmg-public-go{flex-shrink:0;background:#2B6A8C;color:#fff;font-weight:600;font-size:0.86rem;border-radius:10px;padding:10px 16px;}
</style>
<section class="fmg-public" aria-label="For patients and families">
  <div class="wrap">
    <a class="fmg-public-card" href="patients.html">
      <span class="fmg-public-text">
        <span class="fmg-public-eyebrow" style="display:block">For patients &amp; families</span>
        <span class="fmg-public-h" style="display:block">Your health, explained clearly</span>
        <span class="fmg-public-ar" style="display:block" lang="ar" dir="rtl">صحتك… بكلمات واضحة</span>
        <span class="fmg-public-p" style="display:block">Leaflets and WhatsApp-size summary cards — iron deficiency and fasting Ramadan with diabetes — plus home blood pressure and blood sugar guides with record sheets to bring to every visit, and urgent help numbers.</span>
      </span>
      <span class="fmg-public-go">Open leaflets →</span>
    </a>
  </div>
</section>
<!-- FMG-PUBLIC:END -->
"""

QUICK_PILL = '<a href="patients.html" class="quick-pill" style="--pc:#2B6A8C"><span class="quick-dot"></span>For patients · للمرضى</a>'


def replace_or_insert(s, start, end, block, insert_at):
    if start in s:
        a = s.index(start); b = s.index(end, a) + len(end)
        return s[:a] + block.strip() + s[b:], 'updated'
    return insert_at(s, block), 'added'


def add_credit(s):
    def ins(s, block):
        i = s.rfind('</footer>')
        if i == -1:
            i = s.find('<!-- FMG-I18N-JS:START -->')
            if i == -1:
                i = s.rfind('</body>')
            return s[:i] + '<footer>' + block + '</footer>\n' + s[i:]
        return s[:i] + block + '\n' + s[i:]
    return replace_or_insert(s, '<!-- FMG-CREDIT:START -->', '<!-- FMG-CREDIT:END -->', CREDIT_BLOCK, ins)


def add_nav(s):
    if '<!-- FMG-NAV:START -->' not in s:
        return s, 'no nav'
    a = s.index('<!-- FMG-NAV:START -->'); b = s.index('<!-- FMG-NAV:END -->')
    nav = s[a:b]
    if 'FMG-NAV-PUBLIC:START' in nav:
        x = nav.index('<!-- FMG-NAV-PUBLIC:START -->'); y = nav.index('<!-- FMG-NAV-PUBLIC:END -->') + len('<!-- FMG-NAV-PUBLIC:END -->')
        nav = nav[:x] + NAV_ROWS.strip() + nav[y:]
        st = 'updated'
    else:
        m = re.search(r'data-panel="root"[^>]*>', nav)
        assert m, 'root panel not found'
        close = nav.index('</div>', m.end())
        nav = nav[:close] + NAV_ROWS + nav[close:]
        st = 'added'
    return s[:a] + nav + s[b:], st


WRAP_FIX = '<style>/* FMG-WRAP-FIX */ .wrap{width:100%;min-width:0;}</style>\n'


def add_wrapfix(s):
    if 'FMG-WRAP-FIX' in s:
        return s, 'present'
    i = s.index('</head>')
    return s[:i] + WRAP_FIX + s[i:], 'added'


def add_home(s):
    s, st1 = replace_or_insert(s, '<!-- FMG-PUBLIC:START -->', '<!-- FMG-PUBLIC:END -->', HOME_BAND,
                               lambda s, blk: s.replace('<section class="library">', blk + '\n<section class="library">', 1)
                               if '<section class="library">' in s else (_ for _ in ()).throw(AssertionError('library section not found')))
    st2 = 'present'
    if 'href="patients.html" class="quick-pill"' not in s:
        m = re.search(r'(<div class="quick-row">[\s\S]*?)(\n\s*</div>)', s)
        assert m, 'quick-row not found'
        s = s[:m.end(1)] + '\n      ' + QUICK_PILL + s[m.end(1):]
        st2 = 'added'
    return s, f'band {st1}, pill {st2}'


def update_search(site, entries_path):
    p = site / 'search-index.js'
    s = p.read_text(encoding='utf-8')
    a = s.index('['); b = s.rindex(']') + 1
    data = json.loads(s[a:b])
    new = json.loads(pathlib.Path(entries_path).read_text(encoding='utf-8'))
    keep = [e for e in data if e.get('guide') not in ('patients.html', 'about.html')]
    out = keep + new
    p.write_text(s[:a] + json.dumps(out, ensure_ascii=False) + s[b:], encoding='utf-8')
    return f'{len(data)} → {len(out)} entries ({len(new)} public)'


if __name__ == '__main__':
    site = pathlib.Path(sys.argv[1])
    if '--entries' in sys.argv:
        print('search-index.js:', update_search(site, sys.argv[sys.argv.index('--entries') + 1]))
        sys.exit()
    for f in sorted(site.glob('*.html')):
        s = f.read_text(encoding='utf-8')
        s, c = add_credit(s)
        s, n = add_nav(s)
        s, w = add_wrapfix(s)
        if f.name == 'asthma.html' and 'FMG-SEG-FIX' not in s and 'id="seg"' in s:
            s = s.replace('</head>', '<style>/* FMG-SEG-FIX */ #seg{max-width:100%;flex-wrap:wrap;}</style>\n</head>', 1)
        h = ''
        if f.name == 'index.html':
            s, h = add_home(s)
        f.write_text(s, encoding='utf-8')
        print(f'{f.name:22} credit {c:8} nav {n:8} wrapfix {w:8} {h}')
