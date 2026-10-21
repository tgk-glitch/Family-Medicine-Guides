"""Build the bilingual About page and the public-education hub.

usage: python3 build_pages.py SITE_DIR
Reads the shared nav from SITE_DIR/index.html (run apply_updates.py first so
the nav already carries the new rows), writes SITE_DIR/about.html and
SITE_DIR/patients.html, and build/_out/public_entries.json for search.
"""
import sys, os, json, pathlib
sys.path.insert(0, os.path.dirname(__file__))
from shared import (bi, page, nav_from, CREDIT_BLOCK, LANG_SWITCH, rtlfix,
                    EDITOR_EN, EDITOR_AR, ROLE_EN, ROLE_AR)
from leaflet_content import LEAFLETS

SITE = pathlib.Path(sys.argv[1])
NAV = nav_from((SITE / 'index.html').read_text(encoding='utf-8'))
ENTRIES = []


def sec(p, sid, h_en, h_ar, sub_en, sub_ar, inner, guide, title, tag):
    ENTRIES.append(dict(guide=guide, guideTitle=title, tag=tag, id=sid, heading=h_en, snippet=sub_en,
                        headingAr=h_ar, snippetAr=sub_ar))
    return (f'<section class="{p}-sec fmg-sec" id="{sid}"><div class="{p}-sec-head">'
            f'{bi(h_en, h_ar, "h2")}{bi(sub_en, sub_ar, "p", p + "-sub fmg-sub")}</div>{inner}</section>')


def block(p, kind, label_en, label_ar, inner_en, inner_ar, bid=''):
    i = f' id="{bid}"' if bid else ''
    return (f'<div class="{p}-block {p}-{kind} fmg-block"{i}>'
            f'{bi(label_en, label_ar, "p", p + "-block-label")}'
            f'<div class="fmg-en">{inner_en}</div><div class="fmg-ar" lang="ar">{rtlfix(inner_ar)}</div></div>')


def ul(items):
    return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'


def jump(p, items):
    chips = ''.join(f'<a class="{p}-chip" href="#{i}">{bi(en, ar)}</a>' for i, en, ar in items)
    return f'<nav class="{p}-jump fmg-jump" aria-label="On this page"><div class="{p}-jump-inner fmg-jump-inner">{chips}</div></nav>'


def footer(src_en, src_ar):
    return (f'<footer><div class="wrap">{bi(src_en, src_ar, "p", "mono")}</div>{CREDIT_BLOCK}</footer>')


# ====================================================================== ABOUT
def about():
    p, tone, soft, line = 'ab', '#123C38', '#E8EFEC', '#BFD3CC'
    g, t, tag = 'about.html', 'About this site', '#123C38'
    hero = f"""<header class="{p}-hero fmg-hero"><div class="wrap">
{LANG_SWITCH}
{bi('About this site', 'عن الموقع', 'p', p + '-eyebrow fmg-eyebrow')}
{bi('A free family medicine reference for Saudi primary care', 'مرجع مجاني في طب الأسرة للرعاية الأولية في المملكة', 'h1')}
{bi('Field guides, point-of-care tools and patient leaflets — in English and Arabic — for family physicians, trainees, and the families they care for.',
    'أدلة ميدانية، وأدوات تُستخدم عند المريض، ونشرات توعوية، بالعربية والإنجليزية، لأطباء الأسرة والمتدربين والأسر التي يرعونها.', 'p')}
</div></header>"""
    j = jump(p, [('editor', 'Medical editor', 'المحرر الطبي'), ('how-we-work', 'How content is made', 'إعداد المحتوى'), ('acknowledgements', 'Acknowledgements', 'شكر وتقدير'),
                 ('audiences', 'Who it is for', 'لمن الموقع'), ('independence', 'Independence', 'الاستقلالية'),
                 ('disclaimer', 'Disclaimer', 'إخلاء المسؤولية'), ('feedback', 'Feedback', 'الملاحظات')])

    editor_card = f"""<div class="{p}-person">
<span class="{p}-mark" aria-hidden="true">AA</span>
<div class="{p}-person-body">
{bi(ROLE_EN.replace('&', '&amp;'), ROLE_AR, 'p', p + '-role')}
{bi(EDITOR_EN, EDITOR_AR, 'p', p + '-name')}
{bi('Family Medicine', 'طب الأسرة', 'p', p + '-spec')}
</div></div>"""
    s1 = sec(p, 'editor', 'Founder & medical editor', 'المؤسس والمحرر الطبي',
             'Who created the site and supervises its content', 'من أنشأ الموقع ويشرف على محتواه',
             editor_card +
             bi(f'This site was created by <b>{EDITOR_EN}</b>, who supervises all of its clinical content. '
                'He chooses the topics, sets the standards each page must meet, and checks each page and leaflet '
                'against the original guidelines.',
                f'أنشأ هذا الموقعَ <b>{EDITOR_AR}</b>، ويشرف على كامل محتواه الطبي؛ فهو يختار الموضوعات، '
                'ويضع المعايير التي يجب أن تستوفيها كل صفحة، ويتحقق من كل صفحة ونشرة مقارنةً بالإرشادات الأصلية.', 'p') +
             bi('The content is also being reviewed, in English and Arabic, with colleagues in family medicine before the site is shared widely.',
                'ويجري أيضًا مراجعة المحتوى، بالعربية والإنجليزية، مع زملاء في طب الأسرة قبل نشر الموقع على نطاق واسع.', 'p'),
             g, t, tag)

    how_en = ul([
        '<b>Saudi guidance first.</b> Pages start from Saudi sources where they exist — the Ministry of Health, the Saudi Commission for Health Specialties, the Saudi Food and Drug Authority, and national societies such as the Saudi Thoracic Society (SINA) — and then the international guidelines family physicians use (for example WHO, NICE, GINA, ADA, ACC/AHA, ESC and USPSTF).',
        '<b>Latest guidance, checked at the time of writing.</b> Every page is checked for guideline updates when it is written, and its sources are listed on the page.',
        '<b>AI-assisted drafting, human review.</b> AI tools help compile, summarise and filter the source material and write the first draft of each page and leaflet. Every item is then checked one by one against the original guidelines by the medical editor and reviewed with colleagues in family medicine.',
        '<b>Sources are credited.</b> Pages credit the guidelines, papers and teaching material they draw on (see Acknowledgements).',
        '<b>Reviewed and dated.</b> Each leaflet carries a "last updated" and a "next review" date. Content is reviewed at least once a year, or sooner when a major guideline changes.',
        '<b>Drafts are labelled.</b> Anything not yet through clinical review says so clearly.',
        '<b>Arabic and English, reviewed together.</b> Both languages are reviewed side by side by family physicians who are native Arabic speakers, using standard clinical terminology and plain Modern Standard Arabic.',
    ])
    how_ar = ul([
        '<b>المصادر السعودية أولًا.</b> تبدأ الصفحات من المصادر السعودية متى وُجدت، مثل وزارة الصحة، والهيئة السعودية للتخصصات الصحية، والهيئة العامة للغذاء والدواء، والجمعيات الوطنية كالجمعية السعودية لأمراض الصدر (المبادرة السعودية للربو)، ثم الإرشادات الدولية التي يستخدمها أطباء الأسرة (مثل منظمة الصحة العالمية وNICE وGINA وADA وACC/AHA وESC وUSPSTF).',
        '<b>أحدث التوصيات وقت الكتابة.</b> تُراجَع كل صفحة بحثًا عن تحديثات الإرشادات عند كتابتها، وتُذكر مصادرها في الصفحة نفسها.',
        '<b>صياغة بمساعدة الذكاء الاصطناعي، ومراجعة بشرية.</b> تساعد أدوات الذكاء الاصطناعي في جمع المادة العلمية وتلخيصها وتصفيتها، وفي كتابة المسودة الأولى لكل صفحة ونشرة. ثم يتحقق المحرر الطبي من كل بند على حدة مقارنةً بالإرشادات الأصلية، ويراجعه مع زملاء في طب الأسرة.',
        '<b>نسبة المصادر.</b> تنسب الصفحات المعلومات إلى الإرشادات والأبحاث والمواد التعليمية التي تعتمد عليها (انظر «شكر وتقدير»).',
        '<b>مراجعة مؤرَّخة.</b> تحمل كل نشرة تاريخ «آخر تحديث» وتاريخ «المراجعة القادمة». ويُراجَع المحتوى مرة في السنة على الأقل، أو قبل ذلك عند صدور تحديث مهم في الإرشادات.',
        '<b>المسودات موسومة.</b> كل ما لم يكتمل تدقيقه السريري يُذكر ذلك عليه بوضوح.',
        '<b>العربية والإنجليزية معًا.</b> يراجع النسختين جنبًا إلى جنب أطباءُ أسرة لغتهم الأم العربية، باستخدام المصطلحات السريرية المعتمدة ولغة فصحى مبسّطة.',
    ])
    s2 = sec(p, 'how-we-work', 'How content is prepared and reviewed', 'كيف يُعَدّ المحتوى ويُراجَع',
             'The standards every page and leaflet follows', 'المعايير التي تلتزم بها كل صفحة ونشرة',
             block(p, 'glance', 'Work in progress', 'عمل قيد التطوير',
                   '<p>This site is <b>not a final source of information</b>. Pages and leaflets are added in stages and are being reviewed one by one. Until an item has been reviewed, it is marked as a draft.</p>',
                   '<p>هذا الموقع <b>ليس مصدرًا نهائيًا للمعلومات</b>. تُضاف الصفحات والنشرات على مراحل، وتجري مراجعتها واحدةً واحدة، وكل ما لم تكتمل مراجعته يُوسم بأنه مسودة.</p>', bid='work-in-progress')
             + f'<div class="fmg-en">{how_en}</div><div class="fmg-ar" lang="ar">{rtlfix(how_ar)}</div>', g, t, tag)

    s_ack = sec(p, 'acknowledgements', 'Acknowledgements', 'شكر وتقدير',
                'Teaching material that helped shape this site', 'مواد تعليمية أسهمت في بناء الموقع',
                bi('The study notes of the <i>Mastering Family Medicine</i> course (1st edition) by <b>Dr. Bandar Bardisi</b> are one of the '
                   'references used to plan and check the topics covered on this site. We are grateful for this teaching material.',
                   'تُعدّ مذكرات دورة <i>Mastering Family Medicine</i> (الطبعة الأولى) للدكتور <b>بندر برديسي</b> من المراجع المستخدمة في تخطيط '
                   'موضوعات هذا الموقع ومراجعتها، ونشكره على هذه المادة التعليمية.', 'p')
                + bi('Content on this site is rebuilt from current primary guidelines, so any errors are ours. This acknowledgement does not '
                     'mean that Dr. Bardisi has reviewed or endorsed the site.',
                     'ويُعاد بناء محتوى الموقع من أحدث الإرشادات الأصلية، فأي خطأ فيه يقع علينا. ولا يعني هذا الشكر أن الدكتور برديسي راجع الموقع أو أقرّه.', 'p')
                + bi('Patient materials from the Saudi Thoracic Society are linked, not copied, so they keep their own attribution.',
                     'تُربط مواد الجمعية السعودية لأمراض الصدر للمرضى ولا تُنسخ، لتبقى منسوبة إلى أصحابها.', 'p'),
                g, t, tag)

    s3 = sec(p, 'audiences', 'Who it is for', 'لمن هذا الموقع؟',
             'Two audiences, two kinds of content', 'جمهوران ونوعان من المحتوى',
             f"""<div class="{p}-two">
<a class="{p}-tile" href="index.html">{bi('For clinicians', 'للأطباء', 'p', p + '-tile-h')}
{bi('Field guides, urgent care protocols, calculators and OSCE stations for family physicians and residents.', 'أدلة ميدانية، وبروتوكولات الرعاية العاجلة، وحاسبات، ومحطات اختبار سريري لأطباء الأسرة والمتدربين.', 'p')}</a>
<a class="{p}-tile" href="patients.html">{bi('For patients &amp; families', 'للمرضى وأسرهم', 'p', p + '-tile-h')}
{bi('Short, plain-language leaflets in Arabic and English to read at home, print, or share.', 'نشرات قصيرة بلغة بسيطة بالعربية والإنجليزية للقراءة في المنزل أو الطباعة أو المشاركة.', 'p')}</a>
</div>""", g, t, tag)

    s4 = sec(p, 'independence', 'Independence', 'الاستقلالية',
             'Free to use, with no advertising', 'مجاني ودون إعلانات',
             bi('The site is free to use and share. It carries no advertising and has no sponsorship or funding from '
                'pharmaceutical or device companies. Medicines are named by their generic names.',
                'الموقع مجاني للاستخدام والمشاركة، ولا يتضمن إعلانات، ولا يتلقى رعاية أو تمويلًا من شركات الأدوية أو الأجهزة الطبية. '
                'وتُذكر الأدوية بأسمائها العلمية.', 'p'), g, t, tag)

    s5 = sec(p, 'disclaimer', 'Important', 'تنبيه مهم',
             'What this site is — and is not', 'ما هذا الموقع، وما ليس هو',
             block(p, 'flag', 'Medical disclaimer', 'إخلاء المسؤولية الطبية',
                   ul(['This site is a <b>work in progress</b> and is not a final source of information.',
                       'This is an educational reference. It does not replace an individual clinical assessment, local protocols, or the full guidelines it summarises.',
                       'Clinicians should check doses, thresholds and drug availability against current Saudi product information before prescribing.',
                       'Patients and families should not start, stop or change any treatment based on this site alone — talk to your own doctor.',
                       'In an emergency, call <b>997</b> (or <b>911</b> where the unified number operates). For health advice, call the Ministry of Health on <b>937</b>.']),
                   ul(['هذا الموقع <b>عمل قيد التطوير</b>، وليس مصدرًا نهائيًا للمعلومات.',
                       'هذا مرجع تعليمي، ولا يغني عن التقييم السريري الفردي، ولا عن البروتوكولات المحلية، ولا عن الإرشادات الكاملة التي يلخّصها.',
                       'على الأطباء التحقق من الجرعات والقيم المرجعية وتوفّر الأدوية وفق معلومات المنتجات المعتمدة في المملكة قبل وصفها.',
                       'على المرضى وأسرهم عدم البدء بأي علاج أو إيقافه أو تغييره اعتمادًا على هذا الموقع وحده؛ تحدّث مع طبيبك.',
                       'في الحالات الطارئة اتصل بـ <b>997</b> (أو <b>911</b> حيث يعمل الرقم الموحد). وللاستشارات الصحية اتصل بوزارة الصحة على <b>937</b>.'])),
             g, t, tag)

    s6 = sec(p, 'feedback', 'Feedback and corrections', 'الملاحظات والتصحيحات',
             'A dedicated channel will open after peer review', 'ستُتاح قناة مخصّصة بعد مراجعة الزملاء',
             bi('The site is in an early stage, and its content is being reviewed with colleagues in family medicine. A dedicated channel for '
                'feedback, corrections and questions will open once that review is complete.',
                'الموقع في مرحلة مبكرة، ويجري مراجعة محتواه مع الزملاء في طب الأسرة. وستُتاح قناة مخصّصة للملاحظات والتصحيحات والأسئلة '
                'بعد اكتمال هذه المراجعة.', 'p'), g, t, tag)

    css = f"""
.{p}-person{{display:flex;gap:16px;align-items:center;background:var(--tone-soft);border:1.5px solid var(--tone-line);border-radius:14px;padding:16px 18px;margin:0 0 16px;}}
.{p}-mark{{width:54px;height:54px;border-radius:50%;background:var(--teal-deep);color:#F4F6F2;display:flex;align-items:center;justify-content:center;
  font-family:'Fraunces',serif;font-weight:600;font-size:1.15rem;flex-shrink:0;}}
.{p}-person-body{{min-width:0;}}
.{p}-person-body p{{margin:0;}}
.{p}-role{{font-family:'JetBrains Mono',monospace;font-size:0.7rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--ink-soft);}}
html[lang|="ar"] .{p}-role{{font-family:inherit;letter-spacing:0;text-transform:none;font-size:0.8rem;}}
.{p}-name{{font-family:'Fraunces',serif;font-weight:600;font-size:1.25rem;color:var(--teal-deep);line-height:1.3;}}
.{p}-spec{{font-size:0.88rem;color:var(--ink-soft);}}
.{p}-two{{display:grid;grid-template-columns:1fr 1fr;gap:14px;}}
.{p}-tile{{display:block;text-decoration:none;color:var(--ink);background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:16px 18px;}}
.{p}-tile:hover{{border-color:var(--tone);}}
.{p}-tile p{{font-size:0.88rem;color:var(--ink-soft);margin:0;}}
.{p}-tile .{p}-tile-h{{font-family:'Fraunces',serif;font-weight:600;font-size:1.05rem;color:var(--teal-deep);margin:0 0 6px;}}
@media (max-width:560px){{.{p}-two{{grid-template-columns:1fr;}}}}
"""
    body = (hero + j + f'<main class="wrap"><div class="{p}-list fmg-list">{s1}{s2}{s_ack}{s3}{s4}{s5}{s6}</div></main>'
            + footer('Last updated October 2026.', 'آخر تحديث: أكتوبر 2026.'))
    return page(title='About · Family Medicine Guides', p=p, tone=tone, tone_soft=soft, tone_line=line,
                description='About Family Medicine Guides — created and medically supervised by Dr. Albaraa Albawab. How content is prepared, sourced and reviewed.',
                nav=NAV, body=body, extra_css=css)


# ====================================================================== PATIENTS HUB
def existing(*names):
    for n in names:
        if (SITE / n.split('#')[0]).exists():
            return n
    return None


def patients():
    p, tone, soft, line = 'pt', '#2B6A8C', '#EAF2F7', '#BCD3E1'
    g, t, tag = 'patients.html', 'For patients & families', '#2B6A8C'
    hero = f"""<header class="{p}-hero fmg-hero"><div class="wrap">
{LANG_SWITCH}
{bi('For patients &amp; families', 'للمرضى وأسرهم', 'p', p + '-eyebrow fmg-eyebrow')}
{bi('Your health, explained clearly', 'صحتك… بكلمات واضحة', 'h1')}
{bi('Short leaflets in Arabic and English, written in plain language and checked against current guidelines. Read them at home, print them, or share them with your family.',
    'نشرات قصيرة بالعربية والإنجليزية، بلغة بسيطة، ومراجَعة وفق أحدث الإرشادات. اقرأها في المنزل، أو اطبعها، أو شاركها مع أسرتك.', 'p')}
</div></header>"""
    j = jump(p, [('urgent-help', 'Urgent help', 'مساعدة عاجلة'), ('leaflets', 'Leaflets', 'النشرات'),
                 ('trusted-sources', 'Trusted sources', 'مصادر موثوقة'), ('your-visit', 'Your visit', 'زيارتك للطبيب'),
                 ('for-clinicians', 'For clinicians', 'للأطباء')])

    nums = f"""<div class="{p}-nums">
<div class="{p}-num"><b>997</b>{bi('Ambulance — Saudi Red Crescent', 'الإسعاف — هيئة الهلال الأحمر')}</div>
<div class="{p}-num"><b>911</b>{bi('Unified emergency number, where it operates', 'الرقم الموحد للطوارئ، حيث يعمل')}</div>
<div class="{p}-num"><b>937</b>{bi('Health advice, Ministry of Health — 24 hours', 'الاستشارات الصحية، وزارة الصحة — على مدار الساعة')}</div>
<div class="{p}-num"><b>920033360</b>{bi('Mental health counselling (NCMH)', 'الاستشارات النفسية (المركز الوطني لتعزيز الصحة النفسية)')}</div>
</div>"""
    s1 = sec(p, 'urgent-help', 'Urgent help', 'مساعدة عاجلة',
             'Call first — read later', 'اتصل أولًا، واقرأ لاحقًا',
             nums + block(p, 'flag', 'Call 997 or go to the emergency department now for:', 'اتصل بـ 997 أو اذهب إلى الطوارئ فورًا في الحالات التالية:',
                          ul(['Chest pain or pressure, especially with sweating or shortness of breath.',
                              'Signs of stroke: a drooping face, a weak arm or leg, or trouble speaking — even if they go away.',
                              'Severe difficulty breathing, or lips turning blue.',
                              'Fainting, a seizure, heavy bleeding, or a severe allergic reaction.',
                              'Thoughts of ending your life or harming yourself.']),
                          ul(['ألم أو ضغط في الصدر، خاصةً مع التعرّق أو ضيق النفس.',
                              'علامات الجلطة الدماغية: ميلان في الوجه، أو ضعف في الذراع أو الساق، أو صعوبة في الكلام، حتى لو اختفت.',
                              'صعوبة شديدة في التنفس، أو ازرقاق الشفتين.',
                              'الإغماء، أو التشنّج، أو النزف الشديد، أو الحساسية الشديدة.',
                              'أفكار بإنهاء حياتك أو إيذاء نفسك.']), bid='urgent-help-red-flags'),
             g, t, tag)

    cards = []
    for L in LEAFLETS:
        s = L['slug']
        guide = existing(*{'iron-deficiency': ['hematology.html', L['guide']],
                           'ramadan-diabetes': ['ramadan.html', 'endocrine.html', L['guide']],
                           'home-blood-pressure': ['cardiovascular.html', L['guide']],
                           'home-blood-glucose': ['endocrine.html', L['guide']]}.get(s, [L['guide']])) or L['guide']
        rec = ''
        if L.get('record'):
            rec = (f'<a class="{p}-btn" href="downloads/leaflets/{s}-en-record.pdf" download>{bi("Record sheets only · English", "صفحات السجل فقط · الإنجليزية")}</a>'
                   f'<a class="{p}-btn" href="downloads/leaflets/{s}-ar-record.pdf" download>{bi("Record sheets only · Arabic", "صفحات السجل فقط · العربية")}</a>')
        ENTRIES.append(dict(guide=g, guideTitle=t, tag=L['tone'], id='leaflet-' + s,
                            heading=L['title_en'] + ' — patient leaflet', snippet=L['card_en'],
                            headingAr=L['title_ar'] + ' — نشرة للمريض', snippetAr=L['card_ar']))
        cards.append(f"""<article class="{p}-card" id="leaflet-{s}" style="--c:{L['tone']}">
<div class="{p}-card-top">{bi(L['topic_en'], L['topic_ar'], 'span', p + '-topic')}{bi('Draft — under clinical review', 'مسودة — قيد المراجعة السريرية', 'span', p + '-status')}</div>
{bi(L['title_en'], L['title_ar'], 'h3')}
{bi(L['card_en'], L['card_ar'], 'p')}
<div class="{p}-dl">
<a class="{p}-btn {p}-btn-main" href="downloads/leaflets/{s}-en.pdf" download>{bi('Leaflet · English (PDF)', 'النشرة · الإنجليزية (PDF)')}</a>
<a class="{p}-btn {p}-btn-main" href="downloads/leaflets/{s}-ar.pdf" download>{bi('Leaflet · Arabic (PDF)', 'النشرة · العربية (PDF)')}</a>
<a class="{p}-btn" href="downloads/leaflets/{s}-en-card.png" download>{bi('Summary card · English', 'بطاقة ملخّص · الإنجليزية')}</a>
<a class="{p}-btn" href="downloads/leaflets/{s}-ar-card.png" download>{bi('Summary card · Arabic', 'بطاقة ملخّص · العربية')}</a>
{rec}</div>
<a class="{p}-guide" href="{guide}">{bi('Clinician guide for this topic →', 'دليل الطبيب لهذا الموضوع ←')}</a>
</article>""")
    if existing('downloads/quit-smoking-leaflet-en.pdf') and existing('downloads/quit-smoking-leaflet-ar.pdf'):
        ENTRIES.append(dict(guide=g, guideTitle=t, tag='#9C4F2E', id='leaflet-quit-smoking',
                            heading='Quitting smoking — patient leaflet', snippet='Your quit plan, triggers, medicines and support from MOH cessation clinics.',
                            headingAr='الإقلاع عن التدخين — نشرة للمريض', snippetAr='خطة الإقلاع، والمحفّزات، والأدوية، والدعم من عيادات الإقلاع.'))
        cs = existing('counselling.html#smoking', 'counselling.html') or 'categories.html#cat-resp'
        cards.append(f"""<article class="{p}-card" id="leaflet-quit-smoking" style="--c:#9C4F2E">
<div class="{p}-card-top">{bi('Smoking', 'التدخين', 'span', p + '-topic')}{bi('Draft — under clinical review', 'مسودة — قيد المراجعة السريرية', 'span', p + '-status')}</div>
{bi('Quitting smoking', 'الإقلاع عن التدخين', 'h3')}
{bi('Your quit plan, triggers, medicines that improve your chances, and support from MOH cessation clinics.', 'خطة الإقلاع، والمحفّزات، والأدوية التي ترفع فرص النجاح، والدعم من عيادات الإقلاع في وزارة الصحة.', 'p')}
<div class="{p}-dl">
<a class="{p}-btn {p}-btn-main" href="downloads/quit-smoking-leaflet-en.pdf" download>{bi('Leaflet · English (PDF)', 'النشرة · الإنجليزية (PDF)')}</a>
<a class="{p}-btn {p}-btn-main" href="downloads/quit-smoking-leaflet-ar.pdf" download>{bi('Leaflet · Arabic (PDF)', 'النشرة · العربية (PDF)')}</a>
</div>
<a class="{p}-guide" href="{cs}">{bi('Clinician guide for this topic →', 'دليل الطبيب لهذا الموضوع ←')}</a>
</article>""")

    official = f"""<div class="{p}-card {p}-card-ext" id="leaflet-asthma-sts" style="--c:#2C7A6B">
<div class="{p}-card-top">{bi('Asthma', 'الربو', 'span', p + '-topic')}{bi('Official Saudi material', 'مادة سعودية رسمية', 'span', p + '-status ' + p + '-status-ok')}</div>
{bi('Asthma: action plan and control test', 'الربو: خطة العمل واختبار التحكم', 'h3')}
{bi('Published by the Saudi Thoracic Society (SINA). We link to the official versions instead of writing our own, so you always get the current one.',
    'من إصدار الجمعية السعودية لأمراض الصدر (المبادرة السعودية للربو). نضع رابط النسخ الرسمية بدل كتابة نسخة خاصة بنا، لتحصل دائمًا على أحدثها.', 'p')}
<div class="{p}-dl">
<a class="{p}-btn {p}-btn-main" href="https://saudithoracicsociety.org/wp-content/uploads/2019/11/Action_Plan_for_Asthma_Patients-Arabic.pdf" rel="noopener" target="_blank">{bi('Asthma action plan (Arabic)', 'خطة عمل الربو (بالعربية)')}</a>
<a class="{p}-btn" href="https://saudithoracicsociety.org/wp-content/uploads/2019/11/Asthma-Control-Test-Arabic.pdf" rel="noopener" target="_blank">{bi('Asthma Control Test (Arabic)', 'اختبار التحكم في الربو (بالعربية)')}</a>
<a class="{p}-btn" href="https://saudithoracicsociety.org/wp-content/uploads/2019/11/Asthma-Control-Test-English.pdf" rel="noopener" target="_blank">{bi('Asthma Control Test (English)', 'اختبار التحكم في الربو (بالإنجليزية)')}</a>
</div>
<a class="{p}-guide" href="adult-asthma.html">{bi('Clinician guide for this topic →', 'دليل الطبيب لهذا الموضوع ←')}</a>
</div>"""
    ENTRIES.append(dict(guide=g, guideTitle=t, tag='#2C7A6B', id='leaflet-asthma-sts',
                        heading='Asthma action plan and control test — official Saudi material',
                        snippet='Saudi Thoracic Society (SINA) patient materials in Arabic and English.',
                        headingAr='الربو: خطة العمل واختبار التحكم — مادة سعودية رسمية',
                        snippetAr='مواد الجمعية السعودية لأمراض الصدر للمرضى بالعربية والإنجليزية.'))
    s2 = sec(p, 'leaflets', 'Leaflets', 'النشرات التوعوية',
             'Each with a WhatsApp-size summary card. Monitoring guides include record sheets to fill in and bring to every visit.', 'لكل نشرة بطاقة ملخّص بحجم مناسب للواتساب، ولأدلة القياس المنزلي صفحات سجل تُملأ وتُحضر في كل زيارة.',
             block(p, 'note', 'About the drafts', 'عن المسودات',
                   '<p>Leaflets marked <b>draft</b> were written with AI assistance, checked by the medical editor, and are still being reviewed with colleagues. Please use them alongside advice from your own doctor.</p>',
                   '<p>النشرات الموسومة بـ<b>مسودة</b> صيغت بمساعدة الذكاء الاصطناعي وراجعها المحرر الطبي، وما زالت قيد المراجعة مع الزملاء، فاستخدمها مع نصيحة طبيبك.</p>')
             + f'<div class="{p}-cards">{"".join(cards)}{official}</div>', g, t, tag)

    s3 = sec(p, 'trusted-sources', 'Trusted Saudi sources', 'مصادر سعودية موثوقة',
             'Where to look next', 'إلى أين تتجه بعد ذلك',
             f'<div class="fmg-en">' + ul([
                 '<b>Ministry of Health awareness platform</b> — health topics and seasonal guidance, including Ramadan and Hajj. <a href="https://www.moh.gov.sa/en/awarenessplateform/SeasonalAndFestivalHealth/Pages/Ramadan-Health.aspx" rel="noopener" target="_blank">Ramadan health (MOH)</a>',
                 '<b>Sehhaty app</b> — book appointments, see your results, and join virtual clinics, including the quit-smoking clinic.',
                 '<b>937</b> — Ministry of Health advice line, 24 hours a day.',
                 '<b>Saudi Thoracic Society</b> — official asthma materials for patients. <a href="https://saudithoracicsociety.org/sina/" rel="noopener" target="_blank">SINA patient tools</a>',
             ]) + '</div><div class="fmg-ar" lang="ar">' + rtlfix(ul([
                 '<b>منصة التوعية في وزارة الصحة</b>: موضوعات صحية وإرشادات موسمية، منها رمضان والحج. <a href="https://www.moh.gov.sa/en/awarenessplateform/SeasonalAndFestivalHealth/Pages/Ramadan-Health.aspx" rel="noopener" target="_blank">الصحة في رمضان (وزارة الصحة)</a>',
                 '<b>تطبيق صحتي</b>: لحجز المواعيد، والاطلاع على النتائج، والعيادات الافتراضية، ومنها عيادة الإقلاع عن التدخين.',
                 '<b>937</b>: خط الاستشارات في وزارة الصحة على مدار الساعة.',
                 '<b>الجمعية السعودية لأمراض الصدر</b>: مواد الربو الرسمية للمرضى. <a href="https://saudithoracicsociety.org/sina/" rel="noopener" target="_blank">أدوات المبادرة السعودية للربو</a>',
             ])) + '</div>', g, t, tag)

    s4 = sec(p, 'your-visit', 'Getting the most from your visit', 'كيف تستفيد من زيارتك للطبيب',
             'Small things that make a big difference', 'أمور بسيطة تصنع فرقًا كبيرًا',
             f'<div class="fmg-en">' + ul([
                 'Bring all your medicines, or photos of their boxes.',
                 'Write down your top 2–3 questions before you go.',
                 'Ask three questions: <b>What is my main problem? What do I need to do? Why is it important?</b>',
                 'Say it back in your own words to check you have understood — your doctor will welcome it.',
                 'Bring a family member if you like, and tell the clinic which language you prefer.',
             ]) + '</div><div class="fmg-ar" lang="ar">' + rtlfix(ul([
                 'أحضر كل أدويتك، أو صورًا لعلبها.',
                 'اكتب أهم سؤالين أو ثلاثة قبل موعدك.',
                 'اسأل ثلاثة أسئلة: <b>ما مشكلتي الأساسية؟ ماذا عليّ أن أفعل؟ ولماذا هذا مهم؟</b>',
                 'أعد ما فهمته بكلماتك لتتأكد من فهمك؛ سيرحّب طبيبك بذلك.',
                 'أحضر أحد أفراد أسرتك إن رغبت، وأخبر العيادة باللغة التي تفضّلها.',
             ])) + '</div>', g, t, tag)

    clin_en = ul([
        '<b>Go through the five key messages together</b>, then fill in the "My plan" box with the patient — the actual tablet, dose and next test.',
        '<b>Use teach-back:</b> "So I know I explained it well, how will you take your tablets tomorrow?" Correct, then ask again.',
        '<b>Match the language</b> to the person who will use the leaflet. Many households need both versions. For carers who read neither, use a professional interpreter, not a child.',
        '<b>Involve family</b> with the patient\'s agreement — decisions are often shared at home.',
        '<b>Choose the format:</b> print A4 double-sided for older adults; send the PDF or summary card by WhatsApp after the visit for younger patients and carers; read the key box aloud when literacy is limited.',
        '<b>Time it:</b> give the Ramadan leaflet 6–8 weeks before Ramadan, at the pre-Ramadan risk visit.',
        '<b>Monitoring records:</b> write the target, arm or meter, and medicines on the record before the patient leaves. At the next visit, review the record during clerking, fill the "For the clinic" box (home BP average of days 2–7; glucose lows and fasting average), document it in the file, and hand over fresh record sheets.',
    ])
    clin_ar = ul([
        '<b>راجع النقاط الخمس مع المريض</b>، ثم املأ معه خانة «خطتي»: اسم الدواء، والجرعة، وموعد التحليل القادم.',
        '<b>استخدم طريقة «أعد ما فهمت»:</b> «لأتأكد أنني شرحت جيدًا، كيف ستأخذ حبوبك غدًا؟» صحّح ثم اسأل مجددًا.',
        '<b>اختر لغة الشخص الذي سيستخدم النشرة.</b> كثير من الأسر تحتاج إلى النسختين. وإذا كان المرافق لا يقرأ أيًّا منهما، فاستعن بمترجم متخصص لا بطفل.',
        '<b>أشرك الأسرة</b> بموافقة المريض؛ فالقرارات كثيرًا ما تُتخذ في البيت بشكل مشترك.',
        '<b>اختر الشكل المناسب:</b> نسخة مطبوعة على وجهين لكبار السن، وإرسال الملف أو بطاقة الملخّص عبر الواتساب بعد الزيارة للشباب والمرافقين، وقراءة النقاط الأساسية بصوت عالٍ عند محدودية القراءة.',
        '<b>اختر التوقيت:</b> قدّم نشرة رمضان قبل رمضان بـ 6 إلى 8 أسابيع، في زيارة تقييم المخاطر.',
        '<b>سجلات القياس المنزلي:</b> اكتب الهدف والذراع أو الجهاز والأدوية في السجل قبل أن يغادر المريض. وفي الزيارة التالية راجع السجل أثناء أخذ التاريخ المرضي، واملأ خانة «للعيادة» (متوسط ضغط الأيام 2 إلى 7؛ ومرات الهبوط ومتوسط السكر الصائم)، ودوّنه في الملف، وسلّمه صفحات سجل جديدة.',
    ])
    std_en = ul([
        'Two A4 pages at most, opening with five key messages.',
        'Plain language: short sentences, everyday words, about a school grade 6 reading level in English; simple Modern Standard Arabic.',
        'Western digits in both languages, so numbers match the patient\'s meter or cuff.',
        'A red "get help" box, a fill-in plan, sources, a last-updated date and a next-review date.',
        'No website address printed, so leaflets stay valid if the address changes.',
        'Where an official Saudi leaflet already exists, we link to it instead of writing our own.',
    ])
    std_ar = ul([
        'صفحتا A4 كحد أقصى، تبدأ بخمس نقاط أساسية.',
        'لغة بسيطة: جمل قصيرة وكلمات يومية، بمستوى قراءة الصف السادس تقريبًا بالإنجليزية، وعربية فصحى مبسّطة.',
        'أرقام لاتينية في النسختين لتطابق ما يظهر على جهاز السكر أو الضغط.',
        'خانة حمراء «اطلب المساعدة»، وخطة للتعبئة، والمصادر، وتاريخ آخر تحديث، وتاريخ المراجعة القادمة.',
        'لا يُطبع عنوان الموقع على النشرات حتى تبقى صالحة إذا تغيّر العنوان.',
        'إذا وُجدت نشرة سعودية رسمية للموضوع، نضع رابطها بدل كتابة نشرة خاصة بنا.',
    ])
    s5 = sec(p, 'for-clinicians', 'For clinicians: delivering a leaflet well', 'للأطباء: كيف تقدّم النشرة بفاعلية',
             'A leaflet works best as part of the conversation, not instead of it', 'تنجح النشرة حين تكون جزءًا من الحوار، لا بديلًا عنه',
             f'<div class="fmg-en">{clin_en}</div><div class="fmg-ar" lang="ar">{rtlfix(clin_ar)}</div>'
             + block(p, 'glance', 'How our leaflets are written', 'معايير كتابة نشراتنا', std_en, std_ar, bid='leaflet-standard'),
             g, t, tag)

    css = f"""
.{p}-nums{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin:0 0 6px;}}
.{p}-num{{background:#fff;border:1.5px solid #E8B7AC;border-radius:12px;padding:11px 14px;font-size:0.85rem;color:#7A2A20;line-height:1.45;}}
.{p}-num b{{display:block;font-family:'JetBrains Mono',monospace;font-size:1.25rem;color:var(--red);direction:ltr;}}
html[dir="rtl"] .{p}-num b{{text-align:right;unicode-bidi:plaintext;}}
.{p}-cards{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;}}
.{p}-card{{border:1px solid var(--line);border-top:5px solid var(--c);border-radius:14px;padding:16px 16px 14px;background:#fff;display:flex;flex-direction:column;min-width:0;scroll-margin-top:150px;}}
.{p}-card-top{{display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;margin-bottom:8px;}}
.{p}-topic{{font-family:'JetBrains Mono',monospace;font-size:0.66rem;letter-spacing:0.07em;text-transform:uppercase;color:var(--c);font-weight:500;}}
html[lang|="ar"] .{p}-topic{{font-family:inherit;letter-spacing:0;text-transform:none;font-size:0.8rem;font-weight:600;}}
.{p}-status{{font-size:0.68rem;font-weight:700;background:#FBE7B5;color:#6B4A12;padding:3px 9px;border-radius:100px;white-space:nowrap;}}
.{p}-status-ok{{background:#E3F0EA;color:#1F5C55;}}
.{p}-card h3{{font-family:'Fraunces',serif;font-weight:600;font-size:1.15rem;color:var(--teal-deep);margin:0 0 6px;line-height:1.3;}}
.{p}-card p{{font-size:0.87rem;color:var(--ink-soft);margin:0 0 12px;}}
.{p}-dl{{display:grid;grid-template-columns:1fr 1fr;gap:7px;margin-top:auto;}}
.{p}-btn{{text-align:center;display:flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:600;text-decoration:none;color:var(--c);border:1.5px solid var(--c);border-radius:9px;padding:8px 11px;line-height:1.3;}}
.{p}-btn-main{{background:var(--c);color:#fff;}}
.{p}-guide{{font-size:0.8rem;font-weight:600;margin-top:12px;text-decoration:none;color:var(--ink-soft);}}
.{p}-guide:hover{{color:var(--c);}}
@media (max-width:640px){{.{p}-cards{{grid-template-columns:1fr;}}}}
@media (max-width:420px){{.{p}-nums{{grid-template-columns:1fr;}}}}
"""
    body = (hero + j + f'<main class="wrap"><div class="{p}-list fmg-list">{s1}{s2}{s3}{s4}{s5}</div></main>'
            + footer('Emergency numbers as published by the Saudi Red Crescent Authority and the Ministry of Health. Leaflet sources are listed on each leaflet.',
                     'أرقام الطوارئ وفق ما تنشره هيئة الهلال الأحمر السعودي ووزارة الصحة. وتُذكر مصادر كل نشرة عليها.'))
    return page(title='For patients & families · Family Medicine Guides', p=p, tone=tone, tone_soft=soft, tone_line=line,
                description='Plain-language patient leaflets in Arabic and English — iron deficiency, Ramadan and diabetes, home blood pressure — plus urgent help numbers in Saudi Arabia.',
                nav=NAV, body=body, extra_css=css)


if __name__ == '__main__':
    (SITE / 'about.html').write_text(about(), encoding='utf-8')
    (SITE / 'patients.html').write_text(patients(), encoding='utf-8')
    out = pathlib.Path(os.path.dirname(os.path.abspath(__file__))) / '_out'
    out.mkdir(exist_ok=True)
    (out / 'public_entries.json').write_text(json.dumps(ENTRIES, ensure_ascii=False, indent=1), encoding='utf-8')
    print('about.html, patients.html written;', len(ENTRIES), 'search entries')
