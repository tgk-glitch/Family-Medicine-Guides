"""Shared building blocks for Family Medicine Guides pages and leaflets.

Blocks are delimited with marker comments so they can be found, replaced
or skipped idempotently by apply_updates.py on any copy of the site.
"""
import re, html

EDITOR_EN = "Dr. Albaraa Albawab"
EDITOR_AR = "د. البراء البواب"
ROLE_EN = "Founder & Medical Editor"
ROLE_AR = "المؤسس والمحرر الطبي"
SPECIALTY_EN = "Family Medicine"
SPECIALTY_AR = "طب الأسرة"

GOOGLE_FONTS = ('<link href="https://fonts.googleapis.com" rel="preconnect"/>\n'
                '<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>\n'
                '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700'
                '&amp;family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@400;500'
                '&amp;family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>')


def esc(s):
    return html.escape(s, quote=False)


_RTL_BRACKET = re.compile(r'([A-Za-z0-9%°/.\-–]+)\)')


def rtlfix(s):
    """Arabic text ending in Latin/digits before ')' puts the bracket on the
    wrong side under bidi; a right-to-left mark after the run fixes it."""
    return _RTL_BRACKET.sub(lambda m: m.group(1) + '&rlm;)', s)


def bi(en, ar, tag='span', cls='', attrs=''):
    """Bilingual pair. Only use on elements whose default display is right
    (span, p, ul, ol, h*, plain div) — the i18n layer reverts display."""
    c = (' ' + cls) if cls else ''
    a = (' ' + attrs) if attrs else ''
    return (f'<{tag} class="fmg-en{c}"{a}>{en}</{tag}>'
            f'<{tag} class="fmg-ar{c}" lang="ar"{a}>{rtlfix(ar)}</{tag}>')


# ---------------------------------------------------------------- i18n layer
I18N_HEAD_JS = """<script>
(function(){try{var m=location.search.match(/[?&]lang=(ar|en)/);var l=m?m[1]:localStorage.getItem('fmgLang');
if(l==='ar'){var h=document.documentElement;h.lang='ar';h.dir='rtl';}}catch(e){}})();
</script>"""

I18N_CSS = """/* FMG-I18N:START */
.fmg-ar{display:none!important;}
html[lang|="ar"] .fmg-en{display:none!important;}
html[lang|="ar"] .fmg-ar{display:revert!important;}
html[lang|="ar"] body{font-family:'IBM Plex Sans Arabic','Inter',-apple-system,sans-serif;}
html[lang|="ar"] h1,html[lang|="ar"] h2,html[lang|="ar"] h3,html[lang|="ar"] h4{
  font-family:'IBM Plex Sans Arabic','Fraunces',Georgia,serif;letter-spacing:0;}
html[lang|="ar"] em,html[lang|="ar"] i,html[lang|="ar"] .fmg-sub{font-style:normal;}
html[lang|="ar"] li,html[lang|="ar"] p,html[lang|="ar"] td{line-height:1.8;}
html[dir="rtl"] ul,html[dir="rtl"] ol{padding-left:0;padding-right:22px;}
html[dir="rtl"] th,html[dir="rtl"] td{text-align:right;}
html[dir="rtl"] .fmg-sec::before{left:auto;right:0;}
html[lang|="ar"] .fmg-eyebrow{letter-spacing:0;text-transform:none;font-family:'IBM Plex Sans Arabic','Inter',sans-serif;font-weight:600;font-size:0.85rem;}
html[lang|="ar"] h1{line-height:1.38;}
html[lang|="ar"] h2,html[lang|="ar"] h3{line-height:1.45;}
.fmg-langswitch{display:inline-flex;max-width:100%;flex-wrap:wrap;border:1px solid var(--line,#D4DAD1);
  border-radius:100px;background:#fff;padding:3px;gap:2px;margin:0 0 18px;}
.fmg-langswitch button{border:none;background:none;border-radius:100px;padding:7px 15px;cursor:pointer;
  font:600 0.8rem 'Inter','IBM Plex Sans Arabic',sans-serif;color:var(--ink-soft,#4B5D59);}
.fmg-langswitch button[aria-pressed="true"]{background:var(--teal-deep,#123C38);color:#fff;}
.fmg-langswitch button:focus-visible{outline:2px solid var(--tone,#1F5C55);outline-offset:2px;}
/* FMG-I18N:END */"""

I18N_JS = """<!-- FMG-I18N-JS:START -->
<script>
(function(){
  window.fmgLangHooks = window.fmgLangHooks || [];
  function save(l){try{localStorage.setItem('fmgLang',l);}catch(e){}}
  function load(){try{return localStorage.getItem('fmgLang');}catch(e){return null;}}
  window.fmgIsArabic = function(){return (document.documentElement.lang||'').indexOf('ar')===0;};
  window.fmgSetLang = function(l, persist){
    l = (l==='ar') ? 'ar' : 'en';
    var h=document.documentElement; h.lang=l; h.dir=(l==='ar')?'rtl':'ltr';
    if(persist!==false) save(l);
    var b=document.querySelectorAll('[data-fmg-lang]');
    for(var i=0;i<b.length;i++) b[i].setAttribute('aria-pressed', b[i].getAttribute('data-fmg-lang')===l?'true':'false');
    for(var j=0;j<window.fmgLangHooks.length;j++){try{window.fmgLangHooks[j](l);}catch(e){}}
  };
  var m=location.search.match(/[?&]lang=(ar|en)/);
  window.fmgSetLang(m?m[1]:(load()||'en'), !!m);
  document.addEventListener('click', function(e){
    var t=e.target; while(t && t!==document && !(t.getAttribute && t.getAttribute('data-fmg-lang'))) t=t.parentNode;
    if(t && t!==document) window.fmgSetLang(t.getAttribute('data-fmg-lang'));
  });
})();
</script>
<!-- FMG-I18N-JS:END -->"""

LANG_SWITCH = ('<div class="fmg-langswitch" role="group" aria-label="Language / اللغة">'
               '<button type="button" data-fmg-lang="en" aria-pressed="true">English</button>'
               '<button type="button" data-fmg-lang="ar" aria-pressed="false" lang="ar">العربية</button></div>')

# ---------------------------------------------------------------- credit block
CREDIT_BLOCK = f"""<!-- FMG-CREDIT:START -->
<style>
  .fmg-credit{{max-width:900px;margin:26px auto 0;padding:18px 24px 0;border-top:1px solid #D4DAD1;
    font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;box-sizing:border-box;text-align:left;font-style:normal;}}
  .fmg-credit *{{box-sizing:border-box;}}
  .fmg-credit-ar{{text-align:right;}}
  .fmg-credit-in{{display:flex;gap:14px;align-items:flex-start;}}
  .fmg-credit-mark{{width:40px;height:40px;border-radius:50%;background:#123C38;color:#F4F6F2;flex-shrink:0;
    display:flex;align-items:center;justify-content:center;font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:0.92rem;}}
  .fmg-credit-body{{min-width:0;flex:1;}}
  .fmg-credit p{{margin:0;}}
  .fmg-credit-role{{font-family:'JetBrains Mono',monospace;font-size:0.66rem;letter-spacing:0.08em;
    text-transform:uppercase;color:#4B5D59;margin-bottom:3px !important;}}
  .fmg-credit-name{{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:1rem;line-height:1.35;color:#123C38;margin-bottom:5px !important;}}
  .fmg-credit-note{{font-size:0.8rem;line-height:1.6;color:#4B5D59;}}
  .fmg-credit-note b{{color:#123C38;}}
  .fmg-credit a{{color:#1F5C55;font-weight:600;}}
  .fmg-credit .fmg-credit-ar{{display:none;}}
  html[lang|="ar"] .fmg-credit .fmg-credit-en{{display:none;}}
  html[lang|="ar"] .fmg-credit .fmg-credit-ar{{display:block;}}
  .fmg-credit-ar,.fmg-credit-ar .fmg-credit-name{{font-family:'IBM Plex Sans Arabic','Inter',sans-serif;}}
  .fmg-credit-ar .fmg-credit-role{{letter-spacing:0;text-transform:none;font-family:'IBM Plex Sans Arabic',sans-serif;font-size:0.74rem;}}
  .fmg-credit-ar .fmg-credit-note{{line-height:1.8;}}
</style>
<div class="fmg-credit">
  <div class="fmg-credit-in">
    <span class="fmg-credit-mark" aria-hidden="true">AA</span>
    <div class="fmg-credit-body fmg-credit-en" lang="en" dir="ltr">
      <p class="fmg-credit-role">{ROLE_EN.replace('&', '&amp;')}</p>
      <p class="fmg-credit-name">Created and medically supervised by {EDITOR_EN}</p>
      <p class="fmg-credit-note">{SPECIALTY_EN} · <b>Work in progress</b> — drafted with AI assistance and under review by the editor and colleagues. An educational reference, not a final source; it does not replace a clinical assessment. <a href="about.html">About this site &amp; how content is reviewed</a></p>
    </div>
    <div class="fmg-credit-body fmg-credit-ar" lang="ar" dir="rtl">
      <p class="fmg-credit-role">{ROLE_AR}</p>
      <p class="fmg-credit-name">إعداد وإشراف طبي: {EDITOR_AR}</p>
      <p class="fmg-credit-note">{SPECIALTY_AR} · <b>عمل قيد التطوير</b>: صيغت المسودات بمساعدة الذكاء الاصطناعي، وتخضع للمراجعة من المحرر والزملاء. مرجع تعليمي وليس مصدرًا نهائيًا، ولا يغني عن التقييم السريري. <a href="about.html?lang=ar">عن الموقع وآلية مراجعة المحتوى</a></p>
    </div>
  </div>
</div>
<!-- FMG-CREDIT:END -->"""


# ---------------------------------------------------------------- page CSS
def page_css(p, tone, tone_soft, tone_line):
    """House design system (from the mental-health guide), re-toned.
    Every structural element also carries a generic fmg-* class for RTL."""
    return f"""
html{{-webkit-text-size-adjust:100%;text-size-adjust:100%;}}
button,a{{-webkit-tap-highlight-color:transparent;}}
img{{max-width:100%;height:auto;}}
:root{{--paper:#F4F6F2;--paper-2:#EBEEE7;--ink:#1B2A28;--ink-soft:#4B5D59;--line:#D4DAD1;
  --teal:#1F5C55;--teal-deep:#123C38;--red:#B0392C;--card:#FFFFFF;
  --tone:{tone};--tone-soft:{tone_soft};--tone-line:{tone_line};}}
*{{box-sizing:border-box;}}
html{{scroll-behavior:smooth;}}
h2,h3{{scroll-margin-top:170px;}}
.{p}-sec,.fmg-block{{scroll-margin-top:150px;}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;}}
.wrap{{max-width:900px;margin:0 auto;padding:0 24px;width:100%;min-width:0;}} /* FMG-WRAP-FIX */
.{p}-hero{{padding:38px 0 18px;}}
.{p}-eyebrow{{font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--tone);margin:0 0 14px;}}
.{p}-hero h1{{font-family:'Fraunces',serif;font-weight:600;font-size:clamp(1.9rem,4.6vw,2.8rem);line-height:1.12;letter-spacing:-0.015em;margin:0 0 14px;color:var(--teal-deep);}}
.{p}-hero p{{font-size:1.02rem;line-height:1.62;color:var(--ink-soft);max-width:660px;margin:0 0 12px;}}
.{p}-jump{{position:sticky;top:64px;z-index:80;background:rgba(244,246,242,0.96);background:color-mix(in srgb,var(--paper) 96%,transparent);
  -webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);padding:12px 0;
  -webkit-transform:translateZ(0);transform:translateZ(0);will-change:transform;}}
.{p}-jump-inner{{max-width:900px;margin:0 auto;padding:0 24px;display:flex;gap:8px;overflow-x:auto;scrollbar-width:thin;}}
.{p}-chip{{flex-shrink:0;font-weight:600;font-size:0.77rem;color:var(--tone);background:var(--tone-soft);border:1px solid var(--tone-line);
  padding:7px 13px;border-radius:100px;text-decoration:none;white-space:nowrap;}}
.{p}-list{{padding:26px 0 40px;display:flex;flex-direction:column;gap:28px;}}
.{p}-sec{{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:26px 26px 30px;position:relative;overflow:hidden;}}
.{p}-sec::before{{content:'';position:absolute;top:0;left:0;width:6px;height:100%;background:var(--tone);}}
.{p}-sec-head{{margin-bottom:16px;}}
.{p}-sec h2{{font-family:'Fraunces',serif;font-weight:600;font-size:1.5rem;margin:0 0 4px;color:var(--teal-deep);line-height:1.25;}}
.{p}-sub{{font-size:0.9rem;color:var(--ink-soft);font-style:italic;margin:0;}}
.{p}-sec h3{{font-family:'Fraunces',serif;font-size:1.06rem;font-weight:600;margin:20px 0 8px;color:var(--teal-deep);}}
ul{{margin:0;padding-left:20px;}}
li{{font-size:0.93rem;line-height:1.6;color:var(--ink);margin-bottom:7px;}}
li:last-child{{margin-bottom:0;}}
p{{margin:0 0 10px;font-size:0.94rem;line-height:1.62;}}
a{{color:var(--tone);}}
.{p}-block{{border-radius:12px;padding:16px 18px;margin:16px 0;}}
.{p}-block-label{{font-weight:700;font-size:0.92rem;margin-bottom:8px;}}
.{p}-glance{{background:var(--tone-soft);border:1.5px solid var(--tone-line);}}
.{p}-glance .{p}-block-label{{color:var(--tone);}}
.{p}-flag{{background:#FCEEEC;border:1.5px solid #E8B7AC;}}
.{p}-flag .{p}-block-label{{color:var(--red);}}
.{p}-flag li,.{p}-flag p{{color:#7A2A20;}}
.{p}-local{{background:#FBF4E6;border:1.5px solid #E3CE9E;}}
.{p}-local .{p}-block-label{{color:#8A5C2C;}}
.{p}-local li,.{p}-local p{{color:#6B4A22;}}
.{p}-note{{background:var(--paper-2);}}
.{p}-note li,.{p}-note p{{font-size:0.87rem;color:var(--ink-soft);}}
.{p}-table{{overflow-x:auto;margin:10px 0;}}
table{{border-collapse:collapse;width:100%;font-size:0.86rem;}}
th{{background:var(--paper-2);color:var(--teal-deep);font-weight:700;text-align:left;padding:9px 11px;border:1px solid var(--line);}}
td{{padding:9px 11px;border:1px solid var(--line);vertical-align:top;color:var(--ink);}}
footer{{border-top:1px solid var(--line);padding:30px 0 48px;margin-top:20px;}}
footer p{{font-size:0.85rem;color:var(--ink-soft);line-height:1.6;margin:0 0 6px;}}
footer .mono{{font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:var(--ink-soft);}}
@media (max-width:560px){{
  .wrap{{padding:0 16px;}}
  .{p}-jump-inner{{padding:0 16px;}}
  .{p}-sec{{padding:22px 18px 24px;border-radius:14px;}}
  .{p}-sec h2{{font-size:1.3rem;}}
  .fmg-credit{{padding-left:16px;padding-right:16px;}}
}}
"""


def nav_from(site_index_html):
    s = site_index_html
    a = s.index('<!-- FMG-NAV:START -->')
    b = s.index('<!-- FMG-NAV:END -->') + len('<!-- FMG-NAV:END -->')
    return s[a:b]


def page(*, title, description, p, tone, tone_soft, tone_line, nav, body, extra_css='', extra_js=''):
    return f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{description}"/>
{I18N_HEAD_JS}
{GOOGLE_FONTS}
<style>
{page_css(p, tone, tone_soft, tone_line)}
{extra_css}
{I18N_CSS}
</style>
</head>
<body>
{nav}
{body}
{extra_js}
{I18N_JS}
</body>
</html>
"""
