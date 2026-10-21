import asyncio, sys, os
sys.path.insert(0, '/home/claude/build')
from pdf_content import QR, LF
from playwright.async_api import async_playwright

S = '/tmp/claude-0/-home-claude/fef16184-1949-5305-a6bc-c40986cadd89/scratchpad'
FF = S + '/ff'
OUT = '/home/claude/site/downloads'
os.makedirs(OUT, exist_ok=True)
TONE = '#9C4F2E'

BASE = '''
@import url("fonts.css");
@page{size:A4;margin:0;}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;}
body{font-family:%(font)s;color:#1B2A28;font-size:8.6pt;line-height:1.38;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.page{width:210mm;height:297mm;padding:10mm 11mm 9mm;position:relative;overflow:hidden;page-break-after:always;display:flex;flex-direction:column;}
.page:last-child{page-break-after:auto;}
.band{background:%(tone)s;color:#fff;border-radius:4mm;padding:5mm 6mm;margin-bottom:4mm;}
.kicker{font-size:7.5pt;letter-spacing:%(ls)s;text-transform:%(tt)s;opacity:.85;margin:0 0 1.5mm;}
h1{font-family:%(hfont)s;font-size:20pt;line-height:1.15;margin:0 0 1.5mm;font-weight:700;}
.sub{margin:0;font-size:9.5pt;opacity:.95;}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:3.2mm;flex:1;align-content:start;}
.card{border:0.3mm solid #D9CFC7;border-radius:3mm;padding:3.2mm 3.6mm;background:#fff;break-inside:avoid;}
.card.span{grid-column:1 / -1;}
.card.tint{background:#F8EFE9;border-color:#E8CDBE;}
.card.red{background:#FCEEEC;border-color:#E8B7AC;}
.card.red h2{color:#B0392C;}
.card.blue{background:#EEF2F6;border-color:#BECDDB;}
h2{font-family:%(hfont)s;font-size:10.5pt;margin:0 0 1.8mm;color:%(tone)s;font-weight:700;}
ul{margin:0;padding:0;padding-inline-start:4mm;}
li{margin:0 0 1mm;}
p{margin:0 0 1.2mm;}
table{border-collapse:collapse;width:100%%;}
th,td{border:0.25mm solid #E2D8D0;padding:1.1mm 1.6mm;text-align:start;vertical-align:top;}
th{background:#F3ECE6;font-weight:700;color:#123C38;}
td.k{font-weight:700;white-space:nowrap;color:#123C38;}
.note{font-size:7.6pt;color:#4B5D59;margin-top:1.6mm;}
.foot{font-size:6.6pt;color:#4B5D59;margin-top:2.5mm;border-top:0.3mm solid #D4DAD1;padding-top:1.6mm;}
.write{border-bottom:0.3mm dotted #9AA5A1;height:6.2mm;}
.diary td{height:7mm;}
.big{font-size:10pt;line-height:1.45;}
.trig td:first-child{width:18%%;}
'''

def css(lang):
    ar = lang == 'ar'
    return BASE % dict(
        font="'IBM Plex Sans Arabic','Inter',sans-serif" if ar else "'Inter',sans-serif",
        hfont="'IBM Plex Sans Arabic',sans-serif" if ar else "'Fraunces',serif",
        tone=TONE, ls='0' if ar else '.08em', tt='none' if ar else 'uppercase')

def ul(items): return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'
def kv(rows): return '<table>' + ''.join('<tr><td class="k">%s</td><td>%s</td></tr>' % tuple(r) for r in rows) + '</table>'
def tb(head, rows, cls=''):
    return '<table class="%s"><tr>%s</tr>%s</table>' % (cls, ''.join('<th>%s</th>' % h for h in head),
            ''.join('<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>' for r in rows))

LEAF = '''
body{font-size:11pt;line-height:1.5;}
h1{font-size:27pt;}
.sub.big{font-size:12pt;}
h2{font-size:14pt;margin-bottom:2.5mm;}
.big{font-size:11.5pt;line-height:1.6;}
th,td{padding:1.8mm 2.2mm;}
.grid{gap:3.8mm;}
.card{padding:4.5mm 5mm;}
li{margin-bottom:1.8mm;}
.write{height:7.5mm;}
.diary td{height:7.8mm;}
.foot{font-size:7.5pt;}
'''
def doc(lang, body, extra=''):
    d = 'rtl' if lang == 'ar' else 'ltr'
    return '<!DOCTYPE html><html lang="%s" dir="%s"><head><meta charset="utf-8"><style>%s%s</style></head><body>%s</body></html>' % (lang, d, css(lang), extra, body)

def quickref(L):
    g = lambda k: QR[k][L]
    p1 = '''<div class="page">
<div class="band"><p class="kicker">%s</p><h1>%s</h1><p class="sub">%s</p></div>
<div class="grid">
<div class="card tint span"><h2>%s</h2>%s</div>
<div class="card span"><h2>%s</h2>%s<p class="note">%s</p></div>
<div class="card"><h2>%s</h2>%s<p class="note">%s</p></div>
<div class="card"><h2>%s</h2>%s<p class="note">%s</p></div>
<div class="card red"><h2>%s</h2>%s</div>
<div class="card"><h2>%s</h2><p>%s</p></div>
</div>
<div class="foot">%s</div></div>''' % (
        g('kicker'), g('title'), g('sub'),
        g('choose_h'), ul(g('choose')),
        g('stages_h'), tb(g('stages_head'), g('stages')), g('stages_note'),
        g('fiveas_h'), kv(g('fiveas')), g('fiveas_note'),
        g('frames_h'), kv(g('frames')), g('frames_note'),
        g('refer_h'), ul(g('refer')),
        g('qual_h'), g('qual'),
        g('disclaimer'))
    p2 = '''<div class="page">
<div class="grid">
<div class="card span"><h2>%s</h2>%s</div>
<div class="card tint"><h2>%s</h2>%s</div>
<div class="card"><h2>%s</h2>%s<p class="note">%s</p></div>
<div class="card span"><h2>%s</h2>%s<div style="display:grid;grid-template-columns:1fr 1.9fr;gap:3mm;margin-top:2mm"><div><p><b>%s</b></p>%s<p class="note">%s</p></div><div>%s</div></div></div>
<div class="card blue span"><h2>%s</h2>%s</div>
</div>
<div class="foot">%s</div></div>''' % (
        g('mi_h'), ul(g('mi')),
        g('ruler_h'), ul(g('ruler')),
        g('bathe_h'), kv(g('bathe')), g('bathe_note'),
        g('tob_h'), ul(g('tob')), g('hsi_h'), tb(g('hsi_head'), g('hsi')), g('hsi_note'), tb(g('med_head'), g('med')),
        g('ev_h'), ul(g('ev')),
        g('foot'))
    return doc(L, p1 + p2)

def leaflet(L):
    g = lambda k: LF[k][L]
    fld = lambda x, n=1: '<div><p style="margin:2.2mm 0 0"><b>%s</b></p>%s</div>' % (x, '<div class="write"></div>' * n)
    pl = g('plan')
    plan = ('<div style="display:grid;grid-template-columns:1fr 1fr;gap:5mm">' + fld(pl[0]) + fld(pl[1]) + '</div>'
            + fld(pl[2], 2) + fld(pl[3]) + fld(pl[4]))
    diary = tb(g('diary_cols'), [[''] * 5 for _ in range(5)], 'diary')
    trig = tb(['', '', ''], [[('<b>%s</b>' % r[0]), r[1], r[2]] for r in g('trig')], 'trig').replace('<tr><th></th><th></th><th></th></tr>', '')
    p1 = '''<div class="page">
<div class="band"><p class="kicker">%s</p><h1>%s</h1><p class="sub big">%s</p></div>
<div class="grid">
<div class="card tint"><h2>%s</h2>%s</div>
<div class="card"><h2>%s</h2><p class="big">%s</p></div>
<div class="card span"><h2>%s</h2>%s</div>
</div></div>''' % (g('kicker'), g('title'), g('lead'),
        g('body_h'), kv(g('body')),
        g('wd_h'), g('wd'),
        g('trig_h'), trig)
    p2 = '''<div class="page">
<div class="grid">
<div class="card span"><h2>%s</h2>%s</div>
<div class="card tint span"><h2>%s</h2>%s</div>
<div class="card span"><h2>%s</h2>%s</div>
<div class="card blue span"><h2>%s</h2><p class="big">%s</p></div>
</div>
<div class="foot">%s</div></div>''' % (g('help_h'), ul(g('help')), g('plan_h'), plan, g('diary_h'), diary, g('slip_h'), g('slip'), g('foot'))
    return doc(L, p1 + p2, LEAF)

async def main():
    jobs = [('counselling-quick-reference-en', quickref('en')), ('counselling-quick-reference-ar', quickref('ar')),
            ('quit-smoking-leaflet-en', leaflet('en')), ('quit-smoking-leaflet-ar', leaflet('ar'))]
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html in jobs:
            path = FF + '/' + name + '.html'
            open(path, 'w', encoding='utf-8').write(html)
            pg = await b.new_page()
            await pg.goto('file://' + path)
            await pg.evaluate('document.fonts.ready')
            await pg.wait_for_timeout(300)
            # overflow check: content must fit inside each .page
            over = await pg.evaluate('''Array.from(document.querySelectorAll('.page')).map(p => p.scrollHeight - p.clientHeight)''')
            await pg.pdf(path=OUT + '/' + name + '.pdf', format='A4', print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
            print(name, 'overflow per page (px):', over)
            await pg.close()
        await b.close()
asyncio.run(main())
