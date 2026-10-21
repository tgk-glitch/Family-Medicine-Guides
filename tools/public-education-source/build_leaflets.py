"""Render the pilot patient leaflets to A4 PDFs (2 pages) and WhatsApp-size
PNG summary cards, English and Arabic.

usage: python3 build_leaflets.py OUT_DIR [--final]
  OUT_DIR/downloads/leaflets/<slug>-<lang>.pdf
  OUT_DIR/downloads/leaflets/<slug>-<lang>-card.png
Without --final each leaflet carries a DRAFT stamp.
No website URL is printed on leaflets (the domain may change).
"""
import sys, os, pathlib, html as H
from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(__file__))
from leaflet_content import LEAFLETS, REVIEWED, NEXT_REVIEW
from shared import EDITOR_EN, EDITOR_AR, ROLE_EN, ROLE_AR, SPECIALTY_EN, SPECIALTY_AR, rtlfix

# Fontsource packages unpacked here (npm pack @fontsource/inter @fontsource/fraunces @fontsource/ibm-plex-sans-arabic)
FONTS = pathlib.Path(os.environ.get('FMG_FONTS', '/home/claude/fonts'))


def ff(family, path, weight):
    return (f"@font-face{{font-family:'{family}';src:url('file://{FONTS / path}') format('woff2');"
            f"font-weight:{weight};font-style:normal;}}")


FONT_CSS = "\n".join([
    ff('Inter', 'fontsource-inter-5.3.0/files/inter-latin-400-normal.woff2', 400),
    ff('Inter', 'fontsource-inter-5.3.0/files/inter-latin-600-normal.woff2', 600),
    ff('Inter', 'fontsource-inter-5.3.0/files/inter-latin-700-normal.woff2', 700),
    ff('Fraunces', 'fontsource-fraunces-5.3.0/files/fraunces-latin-600-normal.woff2', 600),
    ff('Fraunces', 'fontsource-fraunces-5.3.0/files/fraunces-latin-700-normal.woff2', 700),
] + [ff('Plex Arabic', f'fontsource-ibm-plex-sans-arabic-5.3.0/files/ibm-plex-sans-arabic-arabic-{w}-normal.woff2', w)
     for w in (400, 500, 600, 700)]
  + [ff('Plex Arabic', f'fontsource-ibm-plex-sans-arabic-5.3.0/files/ibm-plex-sans-arabic-latin-{w}-normal.woff2', w)
     for w in (400, 700)])

T = {
    'en': dict(label="Patient information", brand="Family Medicine Guides",
               draft="Draft — pending clinical review",
               prepared=f"Prepared and medically supervised by {EDITOR_EN}, {SPECIALTY_EN}",
               role=f"{ROLE_EN}, Family Medicine Guides",
               updated="Last updated", nextr="Next review", sources="Sources",
               disc="This leaflet gives general information. It does not replace advice from your own doctor, "
                    "who knows your health. Bring it to your next visit and ask about anything that is unclear.",
               ai_draft="Written with AI assistance, checked by the medical editor, and still under review with colleagues.",
               ai_final="Written with AI assistance and reviewed by family physicians.",
               page="Page", of="of", emergency="Emergency: 997", advice="Health advice (MOH): 937",
               card_cta="Ask your doctor for the full leaflet.",
               bring="Bring this record, your device and your medicines to every visit.",
               now="Now", today="Today", visit="Next visit", eg="e.g."),
    'ar': dict(label="معلومات للمريض", brand="أدلة طب الأسرة",
               draft="مسودة — قيد المراجعة السريرية",
               prepared=f"إعداد وإشراف طبي: {EDITOR_AR}، {SPECIALTY_AR}",
               role=f"{ROLE_AR}، أدلة طب الأسرة",
               updated="آخر تحديث", nextr="المراجعة القادمة", sources="المصادر",
               disc="تقدّم هذه النشرة معلومات عامة، ولا تغني عن نصيحة طبيبك الذي يعرف حالتك. "
                    "أحضرها معك في زيارتك القادمة واسأل عن أي شيء غير واضح.",
               ai_draft="صيغت بمساعدة الذكاء الاصطناعي، وراجعها المحرر الطبي، وما زالت قيد المراجعة مع الزملاء.",
               ai_final="صيغت بمساعدة الذكاء الاصطناعي، وراجعها أطباء أسرة.",
               page="صفحة", of="من", emergency="الطوارئ: 997", advice="الاستشارات الصحية (وزارة الصحة): 937",
               card_cta="اطلب النشرة الكاملة من طبيبك.",
               bring="أحضر هذا السجل وجهازك وأدويتك في كل زيارة.",
               now="فورًا", today="اليوم", visit="الزيارة القادمة", eg="مثال"),
}


def css(tone, soft, lang):
    ar = lang == 'ar'
    body_font = "'Plex Arabic', 'Inter', sans-serif" if ar else "'Inter', sans-serif"
    head_font = "'Plex Arabic', serif" if ar else "'Fraunces', Georgia, serif"
    return FONT_CSS + f"""
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: {body_font}; color: #1B2A28; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.page {{ width: 210mm; height: 297mm; padding: 11mm 14mm 10mm; position: relative; overflow: hidden;
        display: flex; flex-direction: column; page-break-after: always; break-after: page; }}
.page:last-child {{ page-break-after: auto; break-after: auto; }}
.content {{ flex: 1; min-height: 0; }}
.band {{ background: {tone}; color: #fff; border-radius: 4mm; padding: 5mm 6.5mm 5.5mm; margin-bottom: 4mm; }}
.band-top {{ display: flex; justify-content: space-between; align-items: center; gap: 4mm; margin-bottom: 3mm; }}
.label {{ font-size: {'9.5pt' if ar else '8pt'}; font-weight: 700; letter-spacing: {'0' if ar else '0.12em'};
          text-transform: {'none' if ar else 'uppercase'}; opacity: 0.92; }}
.draft {{ background: #FBE7B5; color: #6B4A12; font-size: {'9pt' if ar else '7.5pt'}; font-weight: 700;
          padding: 1.2mm 3mm; border-radius: 10mm; white-space: nowrap; }}
h1 {{ font-family: {head_font}; font-weight: {700 if ar else 600}; font-size: {'23pt' if ar else '22pt'};
      line-height: {1.3 if ar else 1.12}; margin: 0 0 2mm; letter-spacing: {'0' if ar else '-0.01em'}; }}
.sub {{ font-size: {'12.5pt' if ar else '11.5pt'}; line-height: 1.45; margin: 0; opacity: 0.95; }}
h2 {{ font-family: {head_font}; font-weight: {700 if ar else 600}; color: {tone};
      font-size: {'13.5pt' if ar else '13pt'}; margin: 3.4mm 0 1.2mm; line-height: 1.28; }}
p, li, td, th {{ font-size: {'11.2pt' if ar else '10.6pt'}; line-height: {1.56 if ar else 1.42}; }}
p {{ margin: 0 0 2mm; }}
ul {{ margin: 0 0 2mm; padding-{'right' if ar else 'left'}: 6mm; padding-{'left' if ar else 'right'}: 0; }}
li {{ margin-bottom: 0.8mm; }}
ul.two {{ columns: 2; column-gap: 8mm; }}
ul.two li {{ break-inside: avoid; }}
b {{ font-weight: 700; }}
.box {{ border-radius: 3mm; padding: 3mm 4.6mm 2.8mm; margin: 2.6mm 0; }}
.box-title {{ font-weight: 700; font-size: {'12pt' if ar else '11.5pt'}; margin: 0 0 1.6mm; }}
.box ul {{ margin-bottom: 0; }}
.key {{ background: {soft}; border: 0.5mm solid {tone}; }}
.key .box-title {{ color: {tone}; }}
.key li {{ font-size: {'11.6pt' if ar else '11pt'}; }}
.help {{ background: #FCEEEC; border: 0.5mm solid #B0392C; }}
.help .box-title {{ color: #9A2C21; }}
.help li {{ color: #5E1F17; }}
.tip {{ background: #FBF4E6; border: 0.4mm solid #D9BE85; }}
.tip .box-title {{ color: #7A5222; }}
table {{ width: 100%; border-collapse: collapse; margin: 1.5mm 0 2.5mm; table-layout: fixed; }}
th {{ background: {soft}; color: {tone}; font-weight: 700; text-align: {'right' if ar else 'left'};
      padding: 1.4mm 2.4mm; border: 0.3mm solid #C9D1C6; }}
td {{ padding: 1.4mm 2.4mm; border: 0.3mm solid #C9D1C6; vertical-align: top; text-align: {'right' if ar else 'left'}; }}
.plan {{ border: 0.4mm dashed {tone}; }}
.plan .box-title {{ color: {tone}; }}
.fill {{ display: flex; align-items: flex-end; gap: 3mm; margin: 2.4mm 0 0; }}
.fill span {{ font-size: {'11pt' if ar else '10.5pt'}; white-space: nowrap; color: #4B5D59; }}
.fill i {{ flex: 1; border-bottom: 0.3mm solid #8A968F; height: 5mm; }}
.log td {{ height: 7.4mm; }}
.log td:first-child {{ width: 13%; font-weight: 600; color: #4B5D59; }}
.foot {{ border-top: 0.3mm solid #C9D1C6; padding-top: 2.6mm; margin-top: 3mm; font-size: {'8.6pt' if ar else '8pt'};
         line-height: 1.5; color: #4B5D59; }}
.foot p {{ font-size: inherit; line-height: inherit; margin: 0 0 1mm; }}
.foot .who {{ display: flex; gap: 3mm; align-items: center; margin-bottom: 1.6mm; }}
.mark {{ width: 8.5mm; height: 8.5mm; border-radius: 50%; background: #123C38; color: #F4F6F2; flex-shrink: 0;
         display: flex; align-items: center; justify-content: center; font-family: 'Fraunces', serif; font-weight: 600; font-size: 8.5pt; }}
.who b {{ color: #123C38; font-size: {'9.6pt' if ar else '9pt'}; }}
.srcs {{ margin: 0; padding-{'right' if ar else 'left'}: 4.5mm; }}
.srcs li {{ font-size: 7.6pt; line-height: 1.4; margin: 0 0 0.5mm; direction: ltr; text-align: left; }}
.numbers {{ display: flex; justify-content: space-between; gap: 4mm; font-weight: 600; color: #123C38; }}
.pageno {{ white-space: nowrap; }}
.strip {{ background: {tone}; color: #fff; border-radius: 3mm; padding: 3mm 5mm; margin: 0 0 3mm;
          display: flex; justify-content: space-between; align-items: center; gap: 4mm; }}
.strip h2 {{ color: #fff; margin: 0; font-size: {'15pt' if ar else '14.5pt'}; }}
.strip .label {{ white-space: nowrap; }}
.fields {{ display: grid; grid-template-columns: 1fr 1fr; column-gap: 7mm; margin: 0 0 2mm; }}
.fields .fill {{ margin-top: 2mm; }}
.fields .wide {{ grid-column: 1 / -1; }}
.hint {{ font-size: {'9.8pt' if ar else '9.4pt'}; color: #4B5D59; margin: 1mm 0 1.5mm; }}
.gtitle {{ font-weight: 700; color: {tone}; font-size: {'11.6pt' if ar else '11pt'}; margin: 2.6mm 0 0; }}
table.grid {{ margin: 1.2mm 0 2mm; }}
table.grid th {{ font-size: {'9pt' if ar else '8.4pt'}; line-height: 1.25; padding: 1.4mm 1.4mm; text-align: center; vertical-align: middle; }}
table.grid td {{ padding: 0 1.4mm; font-size: {'9pt' if ar else '8.6pt'}; vertical-align: middle; text-align: center; }}
table.grid td.lab {{ font-weight: 600; color: #4B5D59; }}
table.grid tr.eg td {{ color: #7A8783; font-style: {'normal' if ar else 'italic'}; background: #F6F8F5; }}
.clinic {{ border: 0.45mm solid #123C38; background: #F1F4F2; }}
.clinic .box-title {{ color: #123C38; }}
.clinic .fields {{ grid-template-columns: 1fr 1fr 1fr; column-gap: 5mm; margin: 0; }}
.clinic .fill span {{ font-size: {'9.8pt' if ar else '9.2pt'}; white-space: normal; }}
.tier {{ border-radius: 2.6mm; padding: 2.4mm 4mm 2.2mm; margin: 0 0 1.8mm; border-{'right' if ar else 'left'}: 2.2mm solid var(--c);
         background: var(--bg); }}
.tier-h {{ display: flex; gap: 3mm; align-items: baseline; margin: 0 0 1mm; }}
.tier-tag {{ background: var(--c); color: #fff; font-weight: 700; font-size: {'9pt' if ar else '8pt'}; padding: 0.6mm 2.4mm;
             border-radius: 8mm; white-space: nowrap; letter-spacing: {'0' if ar else '0.04em'}; text-transform: {'none' if ar else 'uppercase'}; }}
.tier-t {{ font-weight: 700; color: var(--c); font-size: {'11.2pt' if ar else '10.8pt'}; }}
.tier ul {{ margin: 0; }}
.tier li {{ margin-bottom: 0.4mm; }}
.lines i {{ display: block; border-bottom: 0.3mm solid #8A968F; height: 8mm; }}
"""


def esc_ar(s, lang):
    return rtlfix(s) if lang == 'ar' else s


TIER = {'now': ('#B0392C', '#FCEEEC'), 'today': ('#B5721E', '#FBF3E6'), 'visit': ('#1F5C55', '#EAF2EF')}


def fill(lbl, cls=''):
    c = f' class="fill {cls}"' if cls else ' class="fill"'
    return f'<div{c}><span>{lbl}:</span><i></i></div>'


def render_blocks(blocks, lang, tone):
    """Returns (pages, record_start) — record_start is the index of the first
    record page (blocks after ('break', 'record')), or None."""
    pages, cur, record_start = [], [], None
    t = T[lang]
    for b in blocks:
        if b[0] == 'break':
            pages.append(cur); cur = []
            if len(b) > 1 and b[1] == 'record' and record_start is None:
                record_start = len(pages)
            continue
        bt = b[0]
        f = lambda s: esc_ar(s, lang)
        if bt == 'key':
            cur.append(f'<div class="box key"><p class="box-title">{f(b[1])}</p><ul>'
                       + ''.join(f'<li>{f(i)}</li>' for i in b[2]) + '</ul></div>')
        elif bt in ('help', 'tip'):
            cur.append(f'<div class="box {bt}"><p class="box-title">{f(b[1])}</p><ul>'
                       + ''.join(f'<li>{f(i)}</li>' for i in b[2]) + '</ul></div>')
        elif bt == 'h':
            cur.append(f'<h2>{f(b[1])}</h2>')
        elif bt == 'p':
            cur.append(f'<p>{f(b[1])}</p>')
        elif bt == 'ul2':
            cur.append('<ul class="two">' + ''.join(f'<li>{f(i)}</li>' for i in b[1]) + '</ul>')
        elif bt == 'ul':
            cur.append('<ul>' + ''.join(f'<li>{f(i)}</li>' for i in b[1]) + '</ul>')
        elif bt == 'table':
            head = ''.join(f'<th>{f(c)}</th>' for c in b[1])
            rows = ''.join('<tr>' + ''.join(f'<td>{f(c)}</td>' for c in r) + '</tr>' for r in b[2])
            cols = ''.join(f'<col style="width:{w}%">' for w in b[3]) if len(b) > 3 else ''
            cur.append(f'<table><colgroup>{cols}</colgroup><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>')
        elif bt == 'plan':
            fills = ''.join(f'<div class="fill"><span>{f(lbl)}:</span><i></i></div>' for lbl, _ in b[2])
            cur.append(f'<div class="box plan"><p class="box-title">{f(b[1])}</p>{fills}</div>')
        elif bt == 'log':
            head = ''.join(f'<th>{f(c)}</th>' for c in b[2])
            rows = ''.join('<tr><td>' + str(i + 1) + '</td>' + '<td></td>' * (len(b[2]) - 1) + '</tr>' for i in range(b[3]))
            cur.append(f'<div class="box plan"><p class="box-title">{f(b[1])}</p>'
                       f'<table class="log"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>')
        elif bt == 'strip':
            cur.append(f'<div class="strip"><h2>{f(b[1])}</h2><span class="label">{f(b[2])}</span></div>')
        elif bt == 'fields':
            cur.append('<div class="fields">' + ''.join(fill(f(x[0]), 'wide' if len(x) > 1 and x[1] == 'wide' else '') for x in b[1]) + '</div>')
        elif bt == 'hint':
            cur.append(f'<p class="hint">{f(b[1])}</p>')
        elif bt == 'grid':
            # ('grid', title, header, rows, opts) rows: int or list of row labels
            title, header, rows, o = b[1], b[2], b[3], (b[4] if len(b) > 4 else {})
            widths = o.get('widths')
            cols = ''.join(f'<col style="width:{w}%">' for w in widths) if widths else ''
            head = ''.join(f'<th>{f(c)}</th>' for c in header)
            labels = rows if isinstance(rows, list) else [''] * rows
            h = o.get('h', 8)
            body = ''
            if o.get('eg'):
                body += '<tr class="eg">' + ''.join(f'<td style="height:{h}mm">{f(c)}</td>' for c in o['eg']) + '</tr>'
            for lab in labels:
                body += (f'<tr><td class="lab" style="height:{h}mm">{f(str(lab))}</td>' + '<td></td>' * (len(header) - 1) + '</tr>')
            tt = f'<p class="gtitle">{f(title)}</p>' if title else ''
            cur.append(f'{tt}<table class="grid"><colgroup>{cols}</colgroup><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>')
        elif bt == 'clinic':
            cur.append(f'<div class="box clinic"><p class="box-title">{f(b[1])}</p><div class="fields">'
                       + ''.join(fill(f(x)) for x in b[2]) + '</div></div>')
        elif bt == 'tiers':
            out = ''
            for kind, title, items in b[1]:
                c, bg = TIER[kind]
                out += (f'<div class="tier" style="--c:{c};--bg:{bg}"><div class="tier-h"><span class="tier-tag">{t[kind]}</span>'
                        f'<span class="tier-t">{f(title)}</span></div><ul>' + ''.join(f'<li>{f(i)}</li>' for i in items) + '</ul></div>')
            cur.append(out)
        elif bt == 'lines':
            cur.append(f'<p class="gtitle">{f(b[1])}</p><div class="lines">' + '<i></i>' * b[2] + '</div>')
        else:
            raise ValueError(bt)
    pages.append(cur)
    return pages, record_start


def leaflet_html(L, lang, draft=True, only_record=False):
    t = T[lang]
    tone, soft = L['tone'], L['tone_soft']
    title, sub = L['title_' + lang], L['sub_' + lang]
    pages, rs = render_blocks(L[lang], lang, tone)
    full_at = (rs - 1) if rs else len(pages) - 1
    idx = list(range(len(pages)))
    if only_record:
        idx = list(range(rs, len(pages)))
    n = len(idx)
    out = []
    stamp = f'<span class="draft">{t["draft"]}</span>' if draft else ''
    for k, i in enumerate(idx):
        content = pages[i]
        head = ''
        if i == 0:
            head = (f'<div class="band"><div class="band-top"><span class="label">{t["label"]} · {t["brand"]}</span>{stamp}</div>'
                    f'<h1>{title}</h1><p class="sub">{esc_ar(sub, lang)}</p></div>')
        pn = f'<span class="pageno">{t["page"]} {k + 1} {t["of"]} {n}</span>'
        if i == full_at and not only_record:
            srcs = ''.join(f'<li>{H.escape(s)}</li>' for s in L['sources'])
            foot = (f'<div class="foot">'
                    f'<div class="who"><span class="mark">AA</span><div><b>{t["prepared"]}</b><br>{t["role"]}</div></div>'
                    f'<p>{t["disc"]} {t["ai_draft"] if draft else t["ai_final"]}</p>'
                    f'<p><b>{t["updated"]}:</b> {REVIEWED[lang]} · <b>{t["nextr"]}:</b> {NEXT_REVIEW[lang]}</p>'
                    f'<p><b>{t["sources"]}:</b></p><ol class="srcs">{srcs}</ol>'
                    f'<div class="numbers"><span>{t["emergency"]} · {t["advice"]}</span>{pn}</div></div>')
        elif rs is not None and i >= rs:
            foot = (f'<div class="foot"><div class="numbers"><span>{t["bring"]} · {t["emergency"]}</span>{pn}</div>'
                    f'<div class="numbers" style="font-weight:400;margin-top:0.6mm"><span>{t["prepared"]}</span>{stamp}</div></div>')
        else:
            foot = (f'<div class="foot"><div class="numbers"><span>{t["prepared"]}</span>{pn}</div></div>')
        out.append(f'<section class="page">{head}<div class="content">{"".join(content)}</div>{foot}</section>')
    d = 'rtl' if lang == 'ar' else 'ltr'
    return (f'<!DOCTYPE html><html lang="{lang}" dir="{d}"><head><meta charset="utf-8">'
            f'<title>{title}</title><style>{css(tone, soft, lang)}</style></head><body>{"".join(out)}</body></html>')


def card_html(L, lang):
    t = T[lang]
    tone, soft = L['tone'], L['tone_soft']
    ar = lang == 'ar'
    key = next(b for b in L[lang] if b[0] == 'key')
    f = lambda s: esc_ar(s, lang)
    items = ''.join(f'<li><span class="n">{i + 1}</span><span>{f(x)}</span></li>' for i, x in enumerate(key[2]))
    bf = "'Plex Arabic','Inter',sans-serif" if ar else "'Inter',sans-serif"
    hf = "'Plex Arabic',serif" if ar else "'Fraunces',serif"
    return f"""<!DOCTYPE html><html lang="{lang}" dir="{'rtl' if ar else 'ltr'}"><head><meta charset="utf-8"><style>
{FONT_CSS}
*{{box-sizing:border-box}} html,body{{margin:0}}
body{{width:1080px;height:1350px;background:{soft};font-family:{bf};color:#1B2A28;display:flex;flex-direction:column;padding:64px 70px 56px}}
.top{{background:{tone};color:#fff;border-radius:34px;padding:46px 52px 48px}}
.lab{{font-size:{'27px' if ar else '22px'};font-weight:700;letter-spacing:{'0' if ar else '.14em'};text-transform:{'none' if ar else 'uppercase'};opacity:.9;margin:0 0 18px}}
h1{{font-family:{hf};font-weight:{700 if ar else 600};font-size:{'62px' if ar else '60px'};line-height:{1.3 if ar else 1.08};margin:0}}
ul{{list-style:none;margin:44px 0 0;padding:0;flex:1}}
li{{display:flex;gap:24px;align-items:flex-start;font-size:{'33px' if ar else '32px'};line-height:{1.55 if ar else 1.38};margin:0 0 26px}}
.n{{flex-shrink:0;width:54px;height:54px;border-radius:50%;background:{tone};color:#fff;font:700 28px 'Inter',sans-serif;display:flex;align-items:center;justify-content:center;margin-top:{'6px' if ar else '2px'}}}
b{{font-weight:700}}
.help{{background:#fff;border:4px solid #B0392C;border-radius:24px;padding:22px 30px;font-size:{'29px' if ar else '28px'};line-height:1.45;color:#7A2A20;font-weight:600}}
.foot{{display:flex;justify-content:space-between;align-items:center;gap:20px;margin-top:30px;font-size:{'24px' if ar else '22px'};color:#4B5D59}}
.who{{display:flex;align-items:center;gap:16px}}
.mark{{width:52px;height:52px;border-radius:50%;background:#123C38;color:#F4F6F2;display:flex;align-items:center;justify-content:center;font:600 21px 'Fraunces',serif;flex-shrink:0}}
.draft{{background:#FBE7B5;color:#6B4A12;font-weight:700;padding:6px 16px;border-radius:40px;white-space:nowrap}}
</style></head><body>
<div class="top"><p class="lab">{t['label']} · {t['brand']}</p><h1>{L['title_' + lang]}</h1></div>
<ul>{items}</ul>
<div class="help">{t['emergency']} · {t['card_cta']}</div>
<div class="foot"><div class="who"><span class="mark">AA</span><span>{t['prepared']}</span></div>__DRAFT__</div>
</body></html>"""


def build(out_dir, final=False):
    out = pathlib.Path(out_dir) / 'downloads' / 'leaflets'
    out.mkdir(parents=True, exist_ok=True)
    tmp = pathlib.Path(os.path.dirname(os.path.abspath(__file__))) / '_render'; tmp.mkdir(exist_ok=True)
    report = []
    with sync_playwright() as p:
        br = p.chromium.launch()
        for L in LEAFLETS:
            for lang in ('en', 'ar'):
                src = tmp / f"{L['slug']}-{lang}.html"
                src.write_text(leaflet_html(L, lang, draft=not final), encoding='utf-8')
                pg = br.new_page()
                pg.goto(src.as_uri()); pg.wait_for_load_state('networkidle')
                pg.evaluate('document.fonts.ready')
                over = pg.evaluate("""[...document.querySelectorAll('.page')].map(p=>{
                    const c=p.querySelector('.content'); return Math.round(c.scrollHeight - c.clientHeight);})""")
                pdf = out / f"{L['slug']}-{lang}.pdf"
                pg.pdf(path=str(pdf), format='A4', print_background=True, prefer_css_page_size=True)
                pg.close()
                if any(b[0] == 'break' and len(b) > 1 and b[1] == 'record' for b in L[lang]):
                    rsrc = tmp / f"{L['slug']}-{lang}-record.html"
                    rsrc.write_text(leaflet_html(L, lang, draft=not final, only_record=True), encoding='utf-8')
                    rp = br.new_page(); rp.goto(rsrc.as_uri()); rp.wait_for_load_state('networkidle'); rp.evaluate('document.fonts.ready')
                    rp.pdf(path=str(out / f"{L['slug']}-{lang}-record.pdf"), format='A4', print_background=True, prefer_css_page_size=True)
                    rp.close()
                ch = card_html(L, lang).replace('__DRAFT__', '' if final else f'<span class="draft">{T[lang]["draft"]}</span>')
                csrc = tmp / f"{L['slug']}-{lang}-card.html"; csrc.write_text(ch, encoding='utf-8')
                cp = br.new_page(viewport={'width': 1080, 'height': 1350})
                cp.goto(csrc.as_uri()); cp.evaluate('document.fonts.ready')
                cover = cp.evaluate("document.body.scrollHeight - 1350")
                cp.screenshot(path=str(out / f"{L['slug']}-{lang}-card.png"))
                cp.close()
                report.append((L['slug'], lang, over, cover))
        br.close()
    return report


if __name__ == '__main__':
    final = '--final' in sys.argv
    for r in build(sys.argv[1], final):
        print('%-22s %s  page overflow(px)=%s  card overflow(px)=%s' % r)
