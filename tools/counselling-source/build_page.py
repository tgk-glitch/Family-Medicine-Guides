"""Assemble counselling.html + its search-index entries.

Usage: python3 build_page.py <repo_dir>
"""
import sys, re, json, html
from collections import Counter

sys.path.insert(0, '/home/claude/build')
from content_cs1 import FOUNDATIONS, STAGES
from content_cs2 import FIVE_AS, FRAMES
from content_cs3 import MI, BATHE
from content_cs4 import SMOKING, SOURCES

REPO = sys.argv[1]
SECTIONS = [FOUNDATIONS, STAGES, FIVE_AS, FRAMES, MI, BATHE, SMOKING]
P = 'cs'
TONE = '#9C4F2E'
GUIDE = 'counselling.html'
GUIDE_TITLE = 'Counselling'

ICON = {'glance': '◍', 'features': '◐', 'dx': '⊕', 'ddx': '⇄', 'mx': '✚', 'special': '◈',
        'evidence': '⊕', 'fu': '↻', 'tell': '💬', 'local': '⌖', 'note': '◎', 'prev': '⊘'}
CALLOUT = {'flag': 'flag', 'trap': 'trap', 'local': 'local', 'exam': 'exam', 'note': 'note'}

RLM_FIX = re.compile(r'([A-Za-z0-9’\'%])\)')
def rtlfix(ar):
    return RLM_FIX.sub(lambda m: m.group(1) + ')&rlm;', ar)

def bi_inline(en, ar):
    ar = rtlfix(ar)
    return '<span class="fmg-en">%s</span><span class="fmg-ar" lang="ar">%s</span>' % (en, ar)

def bi_block(en, ar):
    ar = rtlfix(ar)
    return '<div class="fmg-en">%s</div><div class="fmg-ar" lang="ar" dir="rtl">%s</div>' % (en, ar)

# ── tools markup ────────────────────────────────────────────
TOOLS = {
'tool-chooser': '''
<div class="cs-tool fmg-block" id="tool-chooser">
<div class="cs-tool-head"><span class="cs-tool-badge">%s</span><h4>%s</h4></div>
<p class="cs-tool-sub">%s</p>
<div class="cs-q"><label for="chProblem">%s</label><select id="chProblem"></select></div>
<div class="cs-q"><label for="chStage">%s</label><select id="chStage"></select></div>
<div class="cs-result" id="chResult" aria-live="polite"></div>
</div>''' % (
    bi_inline('Interactive', 'تفاعلي'), bi_inline('Strategy chooser', 'أداة اختيار الاستراتيجية'),
    bi_inline('Pick the problem and where the patient is now. The tool names the stage, the strategy to lead with, and a first line to say.',
              'اختر نوع المشكلة وأين يقف المريض الآن. تحدد الأداة المرحلة، والاستراتيجية التي تبدأ بها، وأول عبارة تقولها.'),
    bi_inline('1. What kind of problem is it?', '1. ما نوع المشكلة؟'),
    bi_inline('2. Which best describes the patient right now?', '2. أيّ وصف ينطبق على المريض الآن؟')),
'tool-ruler': '''
<div class="cs-tool fmg-block" id="tool-ruler">
<div class="cs-tool-head"><span class="cs-tool-badge">%s</span><h4>%s</h4></div>
<p class="cs-tool-sub">%s</p>
<div class="cs-q"><label for="rulImp">%s <b id="rulImpV">5</b></label><input type="range" id="rulImp" min="0" max="10" step="1" value="5"></div>
<div class="cs-q"><label for="rulConf">%s <b id="rulConfV">5</b></label><input type="range" id="rulConf" min="0" max="10" step="1" value="5"></div>
<div class="cs-result" id="rulResult" aria-live="polite"></div>
</div>''' % (
    bi_inline('Interactive', 'تفاعلي'), bi_inline('Readiness ruler', 'مسطرة الاستعداد'),
    bi_inline('Ask the patient: “On a scale of 0 to 10, how important is this change to you?” and “How confident are you that you could do it?” Enter their answers.',
              'اسأل المريض: «من 0 إلى 10، ما مدى أهمية هذا التغيير بالنسبة لك؟» و«ما مدى ثقتك بأنك تستطيع القيام به؟» ثم أدخل إجابتيه.'),
    bi_inline('Importance:', 'الأهمية:'), bi_inline('Confidence:', 'الثقة:')),
'tool-hsi': '''
<div class="cs-tool fmg-block" id="tool-hsi">
<div class="cs-tool-head"><span class="cs-tool-badge">%s</span><h4>%s</h4></div>
<p class="cs-tool-sub">%s</p>
<div class="cs-q"><label for="hsiT">%s</label><select id="hsiT"></select></div>
<div class="cs-q"><label for="hsiC">%s</label><select id="hsiC"></select></div>
<div class="cs-result" id="hsiResult" aria-live="polite"></div>
</div>''' % (
    bi_inline('Interactive', 'تفاعلي'), bi_inline('Heaviness of Smoking Index (HSI)', 'مؤشر شدة التدخين (HSI)'),
    bi_inline('Two questions from the Fagerström test. Score 0–6. Validated for cigarettes — not for shisha, medwakh or e-cigarettes.',
              'سؤالان من اختبار فاغرستروم. الدرجة من 0 إلى 6. مُتحقَّق منه للسجائر — لا للشيشة أو المدواخ أو السجائر الإلكترونية.'),
    bi_inline('Time to first cigarette after waking', 'الوقت حتى أول سيجارة بعد الاستيقاظ'),
    bi_inline('Cigarettes per day', 'عدد السجائر في اليوم')),
}

# ── render ─────────────────────────────────────────────────
def render_block(b):
    k = b['kind']
    if k == 'tool':
        return TOOLS[b['id']]
    title = bi_inline(b['t_en'], b['t_ar'])
    body = bi_block(b['en'], b['ar'])
    if k in ('flag', 'trap', 'exam', 'note') or (k == 'local'):
        lab = 'local' if k == 'local' else k
        return ('<div class="%s-%s fmg-block" id="%s"><div class="%s-%s-label">%s</div>%s</div>'
                % (P, lab, b['id'], P, lab, title, body))
    ic = ICON.get(k, '◍')
    return ('<div class="%s-block %s-block-%s fmg-block" id="%s"><h3><span class="%s-block-ic">%s</span>%s</h3>%s</div>'
            % (P, P, k, b['id'], P, ic, title, body))

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

# ── text utilities for search ───────────────────────────────
def strip(h):
    t = re.sub(r'<[^>]+>', ' ', h)
    t = html.unescape(t)
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
        sec_text_en = ' '.join(strip(b['en']) for b in s['blocks'])
        sec_text_ar = ' '.join(strip(b['ar']) for b in s['blocks'])
        raw.append(dict(id=s['id'], heading=s['h_en'], headingAr=s['h_ar'],
                        snippet=s['sub_en'], snippetAr=s['sub_ar'], body=sec_text_en, bodyAr=sec_text_ar))
        for b in s['blocks']:
            if b['kind'] == 'tool':
                tool_text = {'tool-chooser': ('Strategy chooser — stage of change and which counselling strategy to lead with', 'أداة اختيار الاستراتيجية — مرحلة التغيير وأي استراتيجية إرشاد تبدأ بها'),
                             'tool-ruler': ('Readiness ruler — importance and confidence 0–10, motivational interviewing follow-up questions', 'مسطرة الاستعداد — الأهمية والثقة من 0 إلى 10 وأسئلة المتابعة في المقابلة التحفيزية'),
                             'tool-hsi': ('Heaviness of Smoking Index — nicotine dependence score and NRT patch strength', 'مؤشر شدة التدخين — درجة الاعتماد على النيكوتين وقوة لصقة بدائل النيكوتين')}[b['id']]
                raw.append(dict(id=b['id'], heading=b['t_en'] + ' · ' + s['h_en'], headingAr=b['t_ar'] + ' · ' + s['h_ar'],
                                snippet=tool_text[0], snippetAr=tool_text[1], body='', bodyAr=''))
                continue
            t_en = re.sub(r'^[^\w“"]+', '', b['t_en']).strip()
            t_ar = re.sub(r'^[^\w؀-ۿ“«]+', '', b['t_ar']).strip()
            raw.append(dict(id=b['id'], heading=t_en + ' · ' + s['h_en'], headingAr=t_ar + ' · ' + s['h_ar'],
                            snippet=snippet(b['en']), snippetAr=snippet(b['ar']), body=strip(b['en']), bodyAr=strip(b['ar'])))
    # rarest-first keyword budget (mirrors enrich_index.py behaviour for this page's entries)
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

def nav_block():
    s = read(REPO + '/index.html')
    a = s.find('<!-- FMG-NAV:START -->'); b = s.find('<!-- FMG-NAV:END -->') + len('<!-- FMG-NAV:END -->')
    return s[a:b]

CSS = read('/home/claude/build/page.css').replace('%TONE%', TONE)
I18N_CSS = read('/home/claude/build/i18n.css')
I18N_JS = read('/home/claude/build/i18n.js')
TOOLS_JS = read('/home/claude/build/tools.js')

def downloads():
    items = [
        ('downloads/counselling-quick-reference-en.pdf', 'Quick reference (EN)', 'المرجع السريع (إنجليزي)'),
        ('downloads/counselling-quick-reference-ar.pdf', 'Quick reference (AR)', 'المرجع السريع (عربي)'),
        ('downloads/quit-smoking-leaflet-en.pdf', 'Patient leaflet (EN)', 'نشرة المريض (إنجليزي)'),
        ('downloads/quit-smoking-leaflet-ar.pdf', 'Patient leaflet (AR)', 'نشرة المريض (عربي)'),
    ]
    links = ''.join('<a class="cs-dl" href="%s" download>%s</a>' % (h, bi_inline('⤓ ' + en, '⤓ ' + ar)) for h, en, ar in items)
    return '<div class="cs-downloads"><p class="cs-dl-label">%s</p><div class="cs-dl-row">%s</div></div>' % (
        bi_inline('Printable — two-page clinician quick reference and a patient leaflet to hand over', 'للطباعة — مرجع سريع للطبيب من صفحتين ونشرة لتسليمها للمريض'), links)

def page():
    chips = ''.join('<a class="%s-chip" href="#%s">%s</a>' % (P, s['id'], bi_inline(s['h_en'] if s['id'] != 'smoking' else 'Tobacco cessation',
                     s['h_ar'] if s['id'] != 'smoking' else 'الإقلاع عن التبغ')) for s in SECTIONS)
    chips += '<a class="%s-chip" href="#sources">%s</a>' % (P, bi_inline('Sources', 'المراجع'))
    secs = '\n'.join(render_section(s, i + 1) for i, s in enumerate(SECTIONS))
    src = '<ol class="cs-src">' + ''.join('<li>%s</li>' % (t + (' <a href="%s" rel="noopener">link</a>' % u if u else '')) for t, u in SOURCES) + '</ol>'
    sources = ('<section class="%s-sec fmg-sec" id="sources"><div class="%s-sec-head"><h2>%s</h2><p class="%s-subtitle">%s</p></div>%s</section>'
               % (P, P, bi_inline('Sources', 'المراجع'), P,
                  bi_inline('Primary literature and guidelines behind this page', 'الأدبيات الأولية والإرشادات التي بُنيت عليها هذه الصفحة'), src))
    hero = '''<section class="cs-hero fmg-hero"><div class="wrap">
<div class="fmg-langswitch" role="group" aria-label="Language"><button type="button" data-fmg-lang="en">English</button><button type="button" data-fmg-lang="ar" lang="ar">العربية</button></div>
<p class="cs-eyebrow">%s</p>
<h1>%s</h1>
%s
%s
</div></section>''' % (
        bi_inline('Counselling · primary care', 'الإرشاد · الرعاية الأولية'),
        bi_inline('Counselling is a clinical skill — and it fits in ten minutes', 'الإرشاد مهارة سريرية — وتتسع لها عشر دقائق'),
        bi_block('<p>Family physicians counsel all day: on smoking, weight, adherence, grief, stress. This guide sets out the five evidence-based strategies built for primary care — <b>stages of change, the Five A’s, FRAMES, motivational interviewing and BATHE</b> — what each assumes, when it fits, and what the evidence actually shows. The last part applies all of them to the conversation with the highest yield in Saudi practice: <b>stopping tobacco</b>.</p><p>Each part follows the same skeleton: <b>at a glance → how it works → evidence → traps → what to say → local context.</b></p>',
                 '<p>يُرشد طبيب الأسرة مرضاه طوال اليوم: في التدخين والوزن والالتزام بالعلاج والحزن والضغوط. يعرض هذا الدليل الاستراتيجيات الخمس المبنية على الدليل والمصممة للرعاية الأولية — <b>مراحل التغيير، والخطوات الخمس، وFRAMES، والمقابلة التحفيزية، وBATHE</b> — وما يفترضه كلٌّ منها، ومتى يناسب، وما يقوله الدليل فعلًا. ويطبّقها الجزء الأخير جميعًا على الحوار الأعلى مردودًا في الممارسة السعودية: <b>الإقلاع عن التبغ</b>.</p><p>يتبع كل جزء الهيكل نفسه: <b>لمحة سريعة ← كيف يعمل ← الدليل ← الأخطاء ← ماذا تقول ← السياق المحلي.</b></p>'),
        downloads())
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Counselling — Family Medicine Guides</title>
<meta content="Counselling in family medicine: stages of change, the Five A's, FRAMES, motivational interviewing and BATHE — with a strategy chooser, readiness ruler and tobacco-cessation guide for Saudi practice. English and Arabic." name="description"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&amp;family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@400;500&amp;family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<style>
%s
%s
</style>
</head>
<body>
%s
%s
<nav class="cs-jump"><div class="cs-jump-inner fmg-jump-inner">%s</div></nav>
<section class="cs-list fmg-list"><div class="wrap">
%s
%s
</div></section>
<footer><div class="wrap">%s</div></footer>
<script>
%s
</script>
%s
</body>
</html>
''' % (CSS, I18N_CSS, nav_block(), hero, chips, secs, sources,
       bi_block('<p>Built by a family physician for the family medicine community — free to use, share, and study from.</p><p>Developed from the AAFP review by Searight (2018) and the guidelines listed above.</p><p class="mono">Educational summary for clinicians. Verify medicine doses and service details against current local guidance and the SFDA formulary. The Arabic text is a draft awaiting native clinical review.</p>',
                '<p>أعدّه طبيب أسرة لمجتمع طب الأسرة — للاستخدام والمشاركة والمذاكرة مجانًا.</p><p>بُني على مراجعة Searight في AAFP (2018) والإرشادات المذكورة أعلاه.</p><p class="mono">ملخص تعليمي للأطباء. تحقّق من جرعات الأدوية وتفاصيل الخدمات وفق الإرشادات المحلية الحالية ودليل الأدوية لدى هيئة الغذاء والدواء. النص العربي مسودة بانتظار مراجعة سريرية من متحدث أصلي.</p>'),
       TOOLS_JS, I18N_JS)

if __name__ == '__main__':
    open(REPO + '/counselling.html', 'w', encoding='utf-8').write(page())
    ents = build_entries()
    json.dump(ents, open('/home/claude/build/counselling_entries.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('entries', len(ents))
