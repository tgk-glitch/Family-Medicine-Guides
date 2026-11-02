"""Build src/fever-rash.html (Eleventy page) + its search-index entries + images.

Usage: python3 tools/fever-rash-source/build_page.py IMG_DIR
  IMG_DIR holds the source .webp photos (measles.webp, ...).
Writes:  src/fever-rash.html, src/assets/fever-rash/*.webp,
         tools/fever-rash-source/fever_rash_entries.json
"""
import sys, re, json, html, shutil, os
from pathlib import Path
from collections import Counter

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SRC = ROOT / 'src'
sys.path.insert(0, str(HERE))
from content_fr1 import APPROACH, IPC
from content_fr2 import MEASLES, RUBELLA, MUMPS
from content_fr3 import VARICELLA, ROSEOLA, FIFTH
from content_fr4 import SCARLET, IMPETIGO, DONTMISS
from content_fr5 import SPECIAL, PREVENTION, SOURCES

IMG_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else None
SECTIONS = [APPROACH, IPC, MEASLES, RUBELLA, MUMPS, VARICELLA, ROSEOLA, FIFTH, SCARLET, IMPETIGO, DONTMISS, SPECIAL, PREVENTION]
CHIP = {'approach': ('Approach', 'المنهج'), 'precautions': ('Isolation & school', 'العزل والمدرسة'),
        'measles': ('Measles', 'الحصبة'), 'rubella': ('Rubella', 'الحصبة الألمانية'), 'mumps': ('Mumps', 'النكاف'),
        'varicella': ('Chickenpox & shingles', 'الجديري والحزام الناري'), 'roseola': ('Roseola', 'الوردية'),
        'fifth': ('Fifth disease', 'المرض الخامس'), 'scarlet': ('Scarlet fever', 'الحمّى القرمزية'),
        'impetigo': ('Impetigo', 'القوباء'), 'do-not-miss': ('Do not miss', 'لا يفوتك'),
        'special-populations': ('Pregnancy & at-risk', 'الحمل والفئات المعرّضة'), 'prevention': ('Prevention & KSA', 'الوقاية والسياق المحلي')}
P = 'fr'
TONE = '#9B3D5A'
GUIDE = 'fever-rash.html'
GUIDE_TITLE = 'Fever with Rash'
ASSET = 'assets/fever-rash/'

ICON = {'glance': '◍', 'features': '◐', 'dx': '⊕', 'ddx': '⇄', 'mx': '✚', 'special': '◈', 'comp': '△',
        'evidence': '⊕', 'fu': '↻', 'tell': '💬', 'local': '⌖', 'note': '◎', 'prev': '⊘', 'ipc': '⛨'}

RLM_FIX = re.compile(r'([A-Za-z0-9’\'%])\)')
def rtlfix(ar):
    return RLM_FIX.sub(lambda m: m.group(1) + ')&rlm;', ar).replace(')&rlm;&rlm;', ')&rlm;')

def bi_inline(en, ar):
    return '<span class="fmg-en">%s</span><span class="fmg-ar" lang="ar">%s</span>' % (en, rtlfix(ar))

def bi_block(en, ar):
    return '<div class="fmg-en">%s</div><div class="fmg-ar" lang="ar" dir="rtl">%s</div>' % (en, rtlfix(ar))

# ── figures ────────────────────────────────────────────────
CREDITS = json.load(open(HERE / 'credits.json', encoding='utf-8'))
AUTHOR = {'measles': 'CDC Public Health Image Library', 'koplik': 'CDC', 'rubella': 'CDC', 'mumps': 'CDC/NIP, Barbara Rice',
          'scarlet': 'Whispyhistory', 'strawberry': 'Whispyhistory', 'varicella': 'CDC Public Health Image Library',
          'zoster': 'NIAID', 'fifth': 'Andrew Kerr (derivative: Berita)', 'roseola': 'Emiliano Burzagli',
          'impetigo': 'CDC Public Health Image Library', 'hfmd': 'James Heilman, MD', 'ssss': 'OpenStax Microbiology',
          'kawasaki': 'Dong Soo Kim (derivative: Natr)', 'dengue': 'Ranjan Premaratna', 'mpox': 'CDC, Brian W.J. Mahy'}
FIG = {
 'measles': ('Red blotchy maculopapular measles rash on a child’s back', 'طفح الحصبة الأحمر البقعي اللطخي الحطاطي على ظهر طفل',
             'Measles: blotchy maculopapular rash becoming confluent', 'الحصبة: طفح بقعي لطخي حطاطي يصبح متكتّلًا'),
 'koplik': ('Koplik spots: small white spots on the inner cheek', 'بقع كوبليك: بقع بيضاء صغيرة على باطن الخد',
            'Koplik spots on the buccal mucosa, before the rash', 'بقع كوبليك على الغشاء المخاطي للخد، قبل الطفح'),
 'rubella': ('Fine pink rubella rash on a child’s back', 'طفح الحصبة الألمانية الوردي الناعم على ظهر طفل',
             'Rubella: discrete pink macules, less confluent than measles', 'الحصبة الألمانية: لطخات وردية متفرّقة، أقل تكتّلًا من الحصبة'),
 'mumps': ('Child with swelling of the parotid gland in front of the ear', 'طفل مع تورّم الغدة النكفية أمام الأذن',
           'Mumps: parotid swelling lifting the earlobe', 'النكاف: تورّم الغدة النكفية يرفع شحمة الأذن'),
 'scarlet': ('Fine red sandpaper-like rash of scarlet fever on the neck and chest', 'طفح الحمّى القرمزية الأحمر الناعم كورق الصنفرة على الرقبة والصدر',
             'Scarlet fever: fine “sandpaper” erythema of neck and trunk', 'الحمّى القرمزية: حُمامى ناعمة «كورق الصنفرة» على الرقبة والجذع'),
 'strawberry': ('White strawberry tongue and inflamed throat in strep pharyngitis', 'لسان الفراولة الأبيض مع التهاب الحلق في التهاب البلعوم العقدي',
                'White strawberry tongue and palatal petechiae (confirmed GAS)', 'لسان الفراولة الأبيض ونَمَشات الحنك (عدوى عقدية مؤكدة)'),
 'varicella': ('Chickenpox spots at different stages on a child’s skin', 'بقع الجديري في مراحل مختلفة على جلد طفل',
               'Chickenpox: papules, vesicles and crusts at the same time', 'الجديري: حطاطات وحويصلات وقشور في الوقت نفسه'),
 'zoster': ('Shingles: grouped blisters in a band on one side of the body', 'الحزام الناري: حويصلات متجمعة في شريط على جانب واحد من الجسم',
            'Shingles: grouped vesicles in one dermatome', 'الحزام الناري: حويصلات متجمعة في قطاع جلدي واحد'),
 'fifth': ('Toddler with bright red slapped-cheek rash of fifth disease', 'طفل صغير بطفح الخد المصفوع الأحمر الزاهي في المرض الخامس',
           'Fifth disease: “slapped cheek” erythema', 'المرض الخامس: حُمامى «الخد المصفوع»'),
 'roseola': ('Baby with pink rash of roseola on the trunk', 'رضيع بطفح الوردية الوردي على الجذع',
             'Roseola: rose-pink macules appearing as the fever breaks', 'الوردية: لطخات وردية تظهر مع انكسار الحمّى'),
 'impetigo': ('Bullous impetigo: ruptured blisters with thin crusts on the skin', 'القوباء الفقاعية: فقاعات منفجرة مع قشور رقيقة على الجلد',
              'Bullous impetigo: ruptured bullae with collarettes of scale', 'القوباء الفقاعية: فقاعات منفجرة مع أطواق من القشور'),
 'hfmd': ('Oval vesicles on the fingers and palm in hand, foot and mouth disease', 'حويصلات بيضاوية على الأصابع والكف في مرض اليد والقدم والفم',
          'Hand, foot and mouth disease: oval vesicles on the hands', 'مرض اليد والقدم والفم: حويصلات بيضاوية على اليدين'),
 'ssss': ('Infant with red peeling skin of staphylococcal scalded skin syndrome', 'رضيع بجلد أحمر متقشّر في متلازمة الجلد المسموط العنقودية',
          'SSSS: tender erythema with superficial peeling', 'متلازمة الجلد المسموط: حُمامى مؤلمة مع تقشّر سطحي'),
 'kawasaki': ('Kawasaki disease: red eyes without discharge, sparing the edge of the cornea', 'داء كاواساكي: احمرار العينين دون إفرازات مع سلامة حافة القرنية',
              'Kawasaki disease: bilateral non-exudative conjunctivitis with limbal sparing', 'داء كاواساكي: التهاب ملتحمة ثنائي دون نضحة مع سلامة الحافة'),
 'dengue': ('Dengue recovery rash with white islands in a sea of red', 'طفح النقاهة في حمّى الضنك مع جزر بيضاء في بحر أحمر',
            'Dengue: convalescent rash, “white islands in a sea of red”', 'حمّى الضنك: طفح النقاهة، «جزر بيضاء في بحر أحمر»'),
 'mpox': ('Mpox: firm, deep-seated pustules of the same stage on the skin', 'جدري القردة: بثور صلبة عميقة في المرحلة نفسها على الجلد',
          'Mpox: deep-seated lesions at the same stage (adult, 1997)', 'جدري القردة: آفات عميقة في المرحلة نفسها (بالغ، 1997)'),
}
SIZES = {}

def lic_html(k):
    c = CREDITS[k]
    lic = c['license']
    lic_link = '<a href="%s" rel="noopener">%s</a>' % (c['licenseUrl'], lic) if c.get('licenseUrl') else lic
    return '%s · %s · <a href="%s" rel="noopener">Wikimedia Commons</a>' % (html.escape(AUTHOR[k]), lic_link, c['page'])

def render_fig(k):
    alt_en, alt_ar, cap_en, cap_ar = FIG[k]
    w, h = SIZES.get(k, (600, 400))
    return ('<figure class="fr-fig"><img src="%s%s.webp" width="%d" height="%d" loading="lazy" decoding="async" alt="%s" data-alt-ar="%s">'
            '<figcaption>%s<span class="fr-credit">%s</span></figcaption></figure>'
            % (ASSET, k, w, h, html.escape(alt_en), html.escape(alt_ar), bi_inline(cap_en, cap_ar), lic_html(k)))

# ── tool: isolation / exclusion / contacts helper ──────────
TOOL = '''
<div class="fr-tool fmg-block" id="tool-contacts">
<div class="fr-tool-head"><span class="fr-tool-badge">%s</span><h4>%s</h4></div>
<p class="fr-tool-sub">%s</p>
<div class="fr-q"><label for="ctDx">%s</label><select id="ctDx"></select></div>
<div class="fr-result" id="ctResult" aria-live="polite"></div>
</div>''' % (
    bi_inline('Interactive', 'تفاعلي'), bi_inline('Isolation, exclusion & contacts helper', 'مساعد العزل والاستبعاد والمخالطين'),
    bi_inline('Pick the working diagnosis. The helper shows the precautions in clinic, how long the child stays home, who at home is at risk, and what the contacts need.',
              'اختر التشخيص المرجّح. يعرض المساعد احتياطات العيادة، ومدة بقاء الطفل في البيت، ومن في البيت معرَّض للخطر، وما يحتاجه المخالطون.'),
    bi_inline('Working diagnosis', 'التشخيص المرجّح'))

def render_block(b):
    k = b['kind']
    if k == 'tool':
        return TOOL
    title = bi_inline(b['t_en'], b['t_ar'])
    body = bi_block(b['en'], b['ar'])
    figs = ''
    if b.get('figs'):
        figs = '<div class="fr-figs fr-figs-%d">%s</div>' % (len(b['figs']), ''.join(render_fig(f) for f in b['figs']))
    if k in ('flag', 'trap', 'exam', 'note', 'local'):
        return ('<div class="%s-%s fmg-block" id="%s"><div class="%s-%s-label">%s</div>%s%s</div>'
                % (P, k, b['id'], P, k, title, figs, body))
    ic = ICON.get(k, '◍')
    return ('<div class="%s-block %s-block-%s fmg-block" id="%s"><h3><span class="%s-block-ic">%s</span>%s</h3>%s%s</div>'
            % (P, P, k, b['id'], P, ic, title, figs, body))

def render_section(s, n):
    out = ['<section class="%s-sec fmg-sec" id="%s">' % (P, s['id']),
           '<div class="%s-sec-head">' % P,
           '<p class="%s-secnum">%s</p>' % (P, bi_inline('Part %d' % n, 'الجزء %d' % n)),
           '<h2>%s</h2>' % bi_inline(s['h_en'], s['h_ar']),
           '<p class="%s-subtitle">%s</p></div>' % (P, bi_inline(s['sub_en'], s['sub_ar']))]
    for b in s['blocks']:
        out.append(render_block(b))
    out.append('</section>')
    return '\n'.join(out)

# ── search entries ─────────────────────────────────────────
def strip(h):
    t = re.sub(r'<[^>]+>', ' ', h)
    t = html.unescape(t).replace('‏', '')
    return re.sub(r'\s+', ' ', t).strip()

TOK = re.compile(r'[A-Za-z][A-Za-z\-’\']{2,}|[؀-ۿ]{3,}|\d+[A-Za-z%]*')
STOP = set('the and for with that this are you your was not but from have has can will what when who how they them their its into than then also any all one two more most each very just only such about which would could should there here been were our out use used may might like over under after before between does did per via'.split())

def tokens(t):
    out = []
    for w in TOK.findall(t):
        wl = w.lower().strip('’\'-')
        if len(wl) < 3 or wl in STOP:
            continue
        out.append(wl)
    return out

def snippet(t, n=180):
    t = strip(t)
    return t if len(t) <= n else t[:n].rsplit(' ', 1)[0] + ' …'

def build_entries():
    raw = []
    for s in SECTIONS:
        raw.append(dict(id=s['id'], heading=s['h_en'], headingAr=s['h_ar'], snippet=s['sub_en'], snippetAr=s['sub_ar'],
                        body=' '.join(strip(b['en']) for b in s['blocks']), bodyAr=' '.join(strip(b['ar']) for b in s['blocks'])))
        for b in s['blocks']:
            if b['kind'] == 'tool':
                raw.append(dict(id=b['id'], heading='Isolation, exclusion & contacts helper · ' + s['h_en'],
                                headingAr='مساعد العزل والاستبعاد والمخالطين · ' + s['h_ar'],
                                snippet='Pick a diagnosis: precautions in clinic, days off school, who at home is at risk and post-exposure prophylaxis.',
                                snippetAr='اختر التشخيص: احتياطات العيادة، وأيام الغياب عن المدرسة، ومن في البيت معرَّض للخطر، والوقاية بعد التعرّض.',
                                body='measles varicella chickenpox rubella mumps scarlet impetigo meningococcal mpox airborne droplet contact exclusion school nursery prophylaxis',
                                bodyAr='الحصبة الجديري الحصبة الألمانية النكاف القرمزية القوباء السحائية العزل المدرسة الوقاية'))
                continue
            t_en = re.sub(r'^[^\w“"]+', '', b['t_en']).strip()
            t_ar = re.sub(r'^[^\w؀-ۿ“«]+', '', b['t_ar']).strip()
            raw.append(dict(id=b['id'], heading=t_en + ' · ' + s['h_en'], headingAr=t_ar + ' · ' + s['h_ar'],
                            snippet=snippet(b['en']), snippetAr=snippet(b['ar']), body=strip(b['en']), bodyAr=strip(b['ar'])))
    df = Counter()
    for r in raw:
        for lang in ('body', 'bodyAr'):
            df.update(set(tokens(r[lang])))
    entries = []
    for r in raw:
        e = dict(guide=GUIDE, guideTitle=GUIDE_TITLE, tag=TONE, id=r['id'], heading=r['heading'], snippet=r['snippet'],
                 headingAr=r['headingAr'], snippetAr=r['snippetAr'])
        for src, hs, key in (('body', ('heading', 'snippet'), 'kw'), ('bodyAr', ('headingAr', 'snippetAr'), 'kwAr')):
            seen = set(tokens(r[hs[0]] + ' ' + r[hs[1]]))
            order = []
            for i, w in enumerate(tokens(r[src])):
                if w in seen:
                    continue
                seen.add(w)
                order.append((df[w], i, w))
            order.sort()
            kw, n = [], 0
            for _, _, w in order:
                if n + len(w) + 1 > 620:
                    continue
                kw.append(w); n += len(w) + 1
            if kw:
                e[key] = ' '.join(kw)
        entries.append(e)
    return entries

# ── page shell ─────────────────────────────────────────────
def read(p):
    return open(p, encoding='utf-8').read()

EXTRA_CSS = '''
  .fr-figs{display:grid;gap:12px;margin:12px 0 16px;}
  .fr-figs-2{grid-template-columns:1fr 1fr;}
  .fr-fig{margin:0;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;display:flex;flex-direction:column;}
  .fr-fig img{display:block;width:100%;height:auto;max-height:340px;object-fit:contain;background:#F0F1EE;}
  .fr-figs-2 .fr-fig img{height:220px;object-fit:cover;}
  .fr-fig figcaption{padding:9px 12px 10px;font-size:0.82rem;line-height:1.45;color:var(--ink);}
  .fr-credit{display:block;margin-top:4px;font-size:0.7rem;color:var(--ink-soft);direction:ltr;text-align:left;}
  .fr-credit a{color:var(--ink-soft);}
  .fr-src-h{font-family:'Fraunces',serif;font-size:1rem;color:var(--teal-deep);margin:18px 0 8px;}
  .fr-block-ipc h3 .fr-block-ic{background:#E8EEF5;color:#2E4F73;}
  .fr-block-comp h3 .fr-block-ic{background:#FBEEE4;color:#A8611C;}
  .fr-block-special h3 .fr-block-ic{background:#EFE6F2;color:#6B3F7A;}
  .fr-result dl{display:grid;grid-template-columns:max-content 1fr;gap:6px 14px;margin:0;}
  .fr-result dt{font-weight:700;color:var(--teal-deep);font-size:0.86rem;}
  .fr-result dd{margin:0;font-size:0.88rem;line-height:1.5;}
  .fr-pill{display:inline-block;font-size:0.72rem;font-weight:700;color:#fff;background:var(--tone);border-radius:100px;padding:2px 9px;margin-inline-end:4px;}
  .fr-pill.air{background:#2E4F73}.fr-pill.drop{background:#3E7A6A}.fr-pill.con{background:#A8611C}.fr-pill.std{background:#6B7A76}
  .fr-draft{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:0.68rem;letter-spacing:0.05em;color:#8A5A00;background:#FBF1DA;border:1px solid #E9D3A0;border-radius:100px;padding:4px 10px;margin:0 0 12px;}
  @media (max-width:640px){
    .fr-table-wrap.fmg-wide{overflow:visible;}
    .fr-table-wrap.fmg-wide table{min-width:0;border:none;}
    .fr-table-wrap.fmg-wide thead{display:none;}
    .fr-table-wrap.fmg-wide table,.fr-table-wrap.fmg-wide tbody,.fr-table-wrap.fmg-wide tr,.fr-table-wrap.fmg-wide td{display:block;width:auto;}
    .fr-table-wrap.fmg-wide tr{border:1px solid var(--line);border-radius:10px;margin:0 0 10px;background:#fff;overflow:hidden;}
    .fr-table-wrap.fmg-wide td{border:none;border-top:1px solid var(--line);padding:7px 12px;}
    .fr-table-wrap.fmg-wide td:first-child{border-top:none;background:var(--paper-2);font-weight:600;color:var(--teal-deep);}
    .fr-table-wrap.fmg-wide td:not(:first-child)::before{content:attr(data-label);display:block;font-size:0.7rem;font-weight:700;letter-spacing:0.02em;color:var(--ink-soft);margin-bottom:2px;}
    .fr-table-wrap.fmg-wide td:empty{display:none;}
  }
  @media (max-width:560px){
    .fr-figs-2{grid-template-columns:1fr;}
    .fr-figs-2 .fr-fig img{height:auto;max-height:300px;object-fit:contain;}
    .fr-result dl{grid-template-columns:1fr;}
    .fr-result dt{margin-top:6px;}
  }
'''

CSS = read(HERE / 'page.css').replace('%TONE%', TONE).replace('--tone-soft:#F8EFE9; --tone-line:#E8CDBE;', '--tone-soft:#F7ECF0; --tone-line:#E6C6D2;') + EXTRA_CSS
CSS = CSS.replace('.fr-chip:hover{background:#F1DFD3;}', '.fr-chip:hover{background:#F0DCE4;}')
I18N_CSS = read(HERE / 'i18n.css')
I18N_JS = read(HERE / 'i18n.js')
TOOL_JS = read(HERE / 'tool.js')

LEAFLETS = [
    ('downloads/leaflets/fever-rash-en.pdf', 'Parent leaflet (EN)', 'نشرة للأهل (إنجليزي)'),
    ('downloads/leaflets/fever-rash-ar.pdf', 'Parent leaflet (AR)', 'نشرة للأهل (عربي)'),
    ('downloads/leaflets/fever-rash-en-card.png', 'WhatsApp card (EN)', 'بطاقة واتساب (إنجليزي)'),
    ('downloads/leaflets/fever-rash-ar-card.png', 'WhatsApp card (AR)', 'بطاقة واتساب (عربي)'),
]

def downloads():
    items = [x for x in LEAFLETS if (SRC / x[0]).exists()]
    if not items:
        return ''
    links = ''.join('<a class="fr-dl" href="%s" download>%s</a>' % (h, bi_inline('⤓ ' + en, '⤓ ' + ar)) for h, en, ar in items)
    return '<div class="fr-downloads"><p class="fr-dl-label">%s</p><div class="fr-dl-row">%s</div></div>' % (
        bi_inline('For families — a two-page leaflet to print or send, and a one-screen card for WhatsApp',
                  'للأسر — نشرة من صفحتين للطباعة أو الإرسال، وبطاقة بحجم شاشة واحدة للواتساب'), links)

def page():
    chips = ''.join('<a class="%s-chip" href="#%s">%s</a>' % (P, s['id'], bi_inline(*CHIP[s['id']])) for s in SECTIONS)
    chips += '<a class="%s-chip" href="#sources">%s</a>' % (P, bi_inline('Sources', 'المراجع'))
    secs = '\n'.join(render_section(s, i + 1) for i, s in enumerate(SECTIONS))
    items = []
    for t, u in SOURCES:
        if not u and t.startswith('<b>'):
            items.append('</ol><h3 class="fr-src-h">%s</h3><ol class="fr-src">' % t)
        else:
            items.append('<li>%s</li>' % (t + (' <a href="%s" rel="noopener">link</a>' % u if u else '')))
    img_list = ''.join('<li>%s — %s</li>' % (FIG[k][2], lic_html(k)) for k in FIG)
    src = ('<ol class="fr-src">' + ''.join(items) + '</ol>').replace('<ol class="fr-src"></ol>', '')
    src += '<h3 class="fr-src-h">%s</h3><ul class="fr-src">%s</ul>' % (bi_inline('Photo credits', 'مصادر الصور'), img_list)
    sources = ('<section class="%s-sec fmg-sec" id="sources"><div class="%s-sec-head"><h2>%s</h2><p class="%s-subtitle">%s</p></div>%s</section>'
               % (P, P, bi_inline('Sources and further reading', 'المراجع والقراءة الإضافية'), P,
                  bi_inline('Where to look next — the global and Saudi references behind this page', 'أين تبحث بعد ذلك — المراجع العالمية والسعودية التي بُنيت عليها هذه الصفحة'), src))
    hero = '''<section class="fr-hero fmg-hero"><div class="wrap">
<div class="fmg-langswitch" role="group" aria-label="Language"><button type="button" data-fmg-lang="en">English</button><button type="button" data-fmg-lang="ar" lang="ar">العربية</button></div>
<p class="fr-eyebrow">%s</p>
<h1>%s</h1>
<p class="fr-draft">%s</p>
%s
%s
</div></section>''' % (
        bi_inline('Pediatrics · Dermatology · Infectious disease', 'طب الأطفال · الجلدية · الأمراض المعدية'),
        bi_inline('Fever with rash in children', 'الحمّى مع الطفح عند الأطفال'),
        bi_inline('DRAFT · AI-assisted · under clinical review', 'مسودة · بمساعدة الذكاء الاصطناعي · قيد المراجعة السريرية'),
        bi_block('<p>The common infectious rashes of childhood — <b>measles, rubella, mumps, chickenpox and shingles, roseola, fifth disease, scarlet fever and impetigo</b> — and the look-alikes you must not miss. For each: how to recognise it, how to confirm it, what to prescribe and what to do without a prescription, <b>which CDC precautions apply and why</b>, when the child can go back to school, and what it means for the <b>pregnant woman, the newborn, the immunocompromised and the unvaccinated</b> at home.</p><p>Each part follows the same skeleton: <b>at a glance → features → diagnosis → management → special populations → what to tell the family.</b></p>',
                 '<p>أشيع أمراض الطفح المعدية في الطفولة — <b>الحصبة، والحصبة الألمانية، والنكاف، والجديري والحزام الناري، والوردية، والمرض الخامس، والحمّى القرمزية، والقوباء</b> — والحالات المشابهة التي لا يجب أن تفوتك. لكلٍّ منها: كيف تتعرّف عليه، وكيف تؤكده، وماذا تصف وماذا تفعل دون وصفة، و<b>أي احتياطات CDC تنطبق ولماذا</b>، ومتى يعود الطفل إلى المدرسة، وماذا يعني ذلك <b>للحامل، وحديث الولادة، وضعيف المناعة، وغير المطعَّم</b> في البيت.</p><p>يتبع كل جزء الهيكل نفسه: <b>لمحة سريعة ← الصورة السريرية ← التشخيص ← العلاج ← الفئات الخاصة ← ماذا تقول للأسرة.</b></p>'),
        downloads())
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Fever with Rash in Children — Family Medicine Guides</title>
<meta content="Measles, rubella, mumps, chickenpox, roseola, fifth disease, scarlet fever, impetigo and the do-not-miss rashes: diagnosis, treatment, CDC isolation precautions, school exclusion, pregnancy and immunocompromised contacts — for Saudi primary care. English and Arabic." name="description"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&amp;family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@400;500&amp;family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<style>
%s
%s
</style>
</head>
<body>
{%% include "nav.html" %%}
%s
<nav class="fr-jump"><div class="fr-jump-inner fmg-jump-inner">%s</div></nav>
<section class="fr-list fmg-list"><div class="wrap">
%s
%s
</div></section>
<footer><div class="wrap">%s</div>{%% include "credit.html" %%}
</footer>
<script>
%s
</script>
%s
</body>
</html>
''' % (CSS, I18N_CSS, hero, chips, secs, sources,
       bi_block('<p>Built by a family physician for the family medicine community — free to use, share, and study from.</p><p>Developed from the CDC, AAP Red Book, WHO, NICE, UKHSA, IDSA and AHA guidance and the Saudi Ministry of Health sources listed above.</p><p class="mono">Educational summary for clinicians. AI-assisted draft under clinical review. Verify doses against the current SFDA formulary and local protocols, and check the current MOH schedule and notifiable-disease list. The Arabic text is a draft awaiting native clinical review.</p>',
                '<p>أعدّه طبيب أسرة لمجتمع طب الأسرة — للاستخدام والمشاركة والمذاكرة مجانًا.</p><p>بُني على إرشادات CDC والكتاب الأحمر للأكاديمية الأمريكية لطب الأطفال ومنظمة الصحة العالمية وNICE وUKHSA وجمعية الأمراض المعدية الأمريكية وجمعية القلب الأمريكية، ومصادر وزارة الصحة السعودية المذكورة أعلاه.</p><p class="mono">ملخص تعليمي للأطباء. مسودة بمساعدة الذكاء الاصطناعي قيد المراجعة السريرية. تحقّق من الجرعات وفق دليل الأدوية الحالي لدى هيئة الغذاء والدواء والبروتوكولات المحلية، وراجع جدول التطعيم الحالي وقائمة الأمراض الواجب الإبلاغ عنها لدى وزارة الصحة. النص العربي مسودة بانتظار مراجعة سريرية من متحدث أصلي.</p>'),
       TOOL_JS, I18N_JS)

if __name__ == '__main__':
    out = SRC / 'assets' / 'fever-rash'
    out.mkdir(parents=True, exist_ok=True)
    from PIL import Image
    for k in FIG:
        srcf = (IMG_DIR / (k + '.webp')) if IMG_DIR else (out / (k + '.webp'))
        if IMG_DIR:
            shutil.copyfile(srcf, out / (k + '.webp'))
        SIZES[k] = Image.open(out / (k + '.webp')).size
    page_html = page()
    assert '{{' not in page_html and page_html.count('{%') == 2, 'liquid tags in content'
    (SRC / GUIDE).write_text(page_html, encoding='utf-8')
    ents = build_entries()
    ids = re.findall(r'id="([^"]+)"', page_html)
    dup = [i for i, c in Counter(ids).items() if c > 1]
    assert not dup, dup
    for e in ents:
        assert ids.count(e['id']) == 1, e['id']
    json.dump(ents, open(HERE / 'fever_rash_entries.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('page', len(page_html) // 1024, 'KB; entries', len(ents))
