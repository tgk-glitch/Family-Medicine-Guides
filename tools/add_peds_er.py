"""Add the Pediatric ER Doses tool (peds-er.html) to the Eleventy site.

Usage: python3 tools/add_peds_er.py SOURCE_TOOL_HTML
Idempotent: re-running replaces the page and skips links/entries already present.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "src"
src = Path(sys.argv[1]).read_text(encoding="utf-8")

# ---------- 1. page ----------
PARENTS = """
    <p class="fmg-en">Hand these out at discharge, printed or as a WhatsApp card. Go through the dose with the carer using their own bottle and syringe, write the mL on the plan, and ask them to show you the dose (teach-back).</p>
    <p class="fmg-ar" lang="ar">أعطِها للأهل عند الخروج، مطبوعة أو بطاقة واتساب. راجع الجرعة مع مقدّم الرعاية باستخدام عبوته ومحقنته، واكتب الكمية بالمليلتر في الخطة، واطلب منه أن يريك كيف يسحب الجرعة.</p>
    <ul class="tight">
      <li><a href="patients.html#leaflet-fever-medicine-child"><span class="fmg-en">Fever and pain medicine for your child</span><span class="fmg-ar" lang="ar">خافض الحرارة والمسكّن لطفلك</span></a> · <a href="downloads/leaflets/fever-medicine-child-en.pdf">EN PDF</a> · <a href="downloads/leaflets/fever-medicine-child-ar.pdf">AR PDF</a></li>
      <li><a href="patients.html#leaflet-spacer-nebulizer"><span class="fmg-en">Using a spacer or a nebulizer at home</span><span class="fmg-ar" lang="ar">استخدام البخاخ مع الحجرة أو جهاز البخار في المنزل</span></a> · <a href="downloads/leaflets/spacer-nebulizer-en.pdf">EN PDF</a> · <a href="downloads/leaflets/spacer-nebulizer-ar.pdf">AR PDF</a></li>
    </ul>"""
css = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
body = src.split("</style>", 1)[1]
script = re.search(r"<script>(.*?)</script>", body, re.S).group(1)
markup = body.split("<script>", 1)[0]

# site palette + fonts, light only (matches the rest of the site)
css = re.sub(r":root\{.*?\n\}", """:root{
  --bg:#F4F6F2; --card:#FFFFFF; --ink:#1B2A28; --mute:#4B5D59; --line:#D4DAD1;
  --accent:#1F5C55; --accent-soft:#E3EEEA;
  --fix:#B0392C; --fix-soft:#F8E6E3; --upd:#8A5A00; --upd-soft:#FBF1DA; --ok:#2C7A4B; --ok-soft:#E3F2E8;
  --f-disp:'Fraunces',Georgia,serif;
  --f-body:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  --f-mono:'JetBrains Mono',ui-monospace,Menlo,Consolas,monospace;
}""", css, count=1, flags=re.S)
css = re.sub(r"@media \(prefers-color-scheme:dark\)\{.*?\}\}\n", "", css, flags=re.S)
css = re.sub(r':root\[data-theme="dark"\]\{.*?\}\n', "", css, flags=re.S)
css = re.sub(r"body::before\{.*?\}\n", "", css)
css = css.replace("body{background:var(--bg);color:var(--ink);font:15px/1.5 var(--f-body);-webkit-tap-highlight-color:transparent}",
                  "body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 var(--f-body);-webkit-font-smoothing:antialiased;-webkit-tap-highlight-color:transparent}")
# scope element rules so the shared nav is untouched
for sel in ["h1,h2,h3{", "h1{", "h2{", "h3{", "p{", "input,select{", "input:focus-visible", "table{", "th,td{", "th{"]:
    css = css.replace("\n" + sel, "\n#pe " + sel.replace(",", ",#pe "), 1)
css = css.replace("small,.mute{", "#pe small,.mute{")
css = css.replace("h1{font-size:1.75rem;font-weight:700}", "h1{font-size:clamp(1.9rem,4.5vw,2.6rem);font-weight:600;letter-spacing:-0.015em;color:#123C38}")
css = css.replace("h2{font-size:1.35rem;font-weight:700;", "h2{font-size:1.35rem;font-weight:600;color:#123C38;")
# Fraunces is a text serif: lighter tab labels, no uppercase on group rows
css = css.replace("nav.tabs button{flex:0 0 auto;font:600 .9rem var(--f-disp);letter-spacing:.02em;",
                  "nav.tabs button{flex:0 0 auto;font:600 .88rem var(--f-body);")
css = css.replace(".sev{font:700 .85rem var(--f-disp);", ".sev{font:700 .8rem var(--f-body);")
css = css.replace(".grp td{background:var(--accent-soft);font:700 .8rem var(--f-disp);", ".grp td{background:var(--accent-soft);font:700 .76rem var(--f-body);")
# weight bar sits under the 64px shared nav bar
css = css.replace(".bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;", ".bar{position:sticky;top:64px;z-index:80;")
css = css.replace("header.top{padding-block:20px 8px}", "header.top{padding-block:36px 12px}")
css += "\n@media (max-width:560px){#drugTable,#resusTable,#sedTable,#seizTable{min-width:0!important}#drugTable thead,#resusTable thead,#sedTable thead,#seizTable thead{display:none}#drugTable tr,#resusTable tr,#sedTable tr,#seizTable tr{display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:10px;border-bottom:1px solid var(--line);padding:8px 10px}#drugTable td,#resusTable td,#sedTable td,#seizTable td{border:none;padding:0}#drugTable td:nth-child(2),#resusTable td:nth-child(2),#sedTable td:nth-child(2){grid-column:1/-1;grid-row:2;font-size:.8rem;color:var(--mute)}#drugTable td:nth-child(3),#resusTable td:nth-child(3),#sedTable td:nth-child(3){grid-column:2;grid-row:1;text-align:right}#drugTable td:nth-child(4),#resusTable td:nth-child(4),#sedTable td:nth-child(4){grid-column:1/-1;grid-row:3;font-size:.84rem;margin-top:2px}#drugTable tr.grp{display:block;background:var(--accent-soft)}#seizTable td:nth-child(1){grid-column:1/-1;font-size:.75rem;color:var(--accent)}#seizTable td:nth-child(1):empty{display:none}#seizTable td:nth-child(3){grid-column:1;font-size:.8rem;color:var(--mute)}#seizTable td:nth-child(4){grid-column:2;grid-row:span 2;text-align:right;align-self:center}}\n.panel{scroll-margin-top:240px}\n@media (max-width:560px){#pe .bar .wrap{gap:8px 10px;padding-block:8px}#estBtn{font-size:.8rem;padding:7px 9px}.wt-hint:not(.on){display:none}#wt{width:5.5rem}#age{width:4.5rem!important}}\n[hidden]{display:none!important}\n#pe footer.pe-src{padding-block:8px 24px}\n"

# markup tweaks
markup = markup.replace('<div class="wrap">\n  <nav class="tabs"', '<div class="wrap">\n  <nav class="tabs"', 1)
# drop the artifact's own credit line and footer heading (the shared FMG-CREDIT block replaces it)
markup = re.sub(r'\s*<div class="credit">.*?</div>', "", markup, count=1, flags=re.S)
markup = markup.replace("<footer>", '<footer class="pe-src">', 1)
markup = re.sub(r"<title>.*?</title>\s*", "", markup)
markup = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\s*', "", markup)
markup = re.sub(r"<link [^>]*>\s*", "", markup)
markup = markup.replace("DRAFT · AI-assisted · awaiting review against your hospital formulary (Lexicomp/UpToDate) before clinical use",
                        "DRAFT · under review · confirm every dose against your hospital formulary before use")
markup = markup.replace("مسودة · بمساعدة الذكاء الاصطناعي · بانتظار المراجعة مقابل دليل الأدوية في مستشفاك قبل الاستخدام السريري",
                        "مسودة · قيد المراجعة · تحقّق من كل جرعة مقابل دليل الأدوية في مستشفاك قبل الاستخدام")
# parent leaflets: real links on the site
markup = re.sub(r'(<div class="pearl" id="parentsBox">.*?</b>).*?(\n  </div>)', lambda m: m.group(1) + PARENTS + m.group(2), markup, count=1, flags=re.S)
markup = markup.replace("Your quick note, checked against current guidelines and turned into a calculator.",
                        "Common pediatric ER and urgent-care doses, checked against current guidelines and turned into a calculator.")
markup = markup.replace('<span class="fmg-en">Your note, line by line</span><span class="fmg-ar" lang="ar">ملاحظتك سطرًا بسطر</span>',
                        '<span class="fmg-en">What changed from the common quick-note doses</span><span class="fmg-ar" lang="ar">ما الذي تغيّر في جرعات الملاحظات الشائعة</span>')
markup = markup.replace('الأحمر: قد يسبب خطأً في الجرعة كما كُتب.', 'الأحمر: اختصار شائع يسبب أخطاء في الجرعات.')
markup = markup.replace("Red = could cause a dosing error as written.", "Red = a common shorthand that causes dosing errors.")
markup = markup.replace("<th>Your note</th>", "<th>Common note</th>")

markup = markup.replace('<h1><span class="fmg-en">Peds ER Doses</span>', '<h1><span class="fmg-en">Pediatric ER Doses</span>')
markup = markup.replace(">Estimate weight from age<", ">Estimate from age<")
script = script.replace("$('#wtHint').textContent='Estimated by APLS '", "$('#wtHint').classList.add('on');$('#wtHint').textContent='Estimated by APLS '")
script = script.replace("$('#wtHint').textContent='Over 12 years", "$('#wtHint').classList.add('on');$('#wtHint').textContent='Over 12 years")
script = script.replace("if(s==='#wt')$('#wtHint').textContent=", "if(s==='#wt'){$('#wtHint').classList.remove('on')}if(s==='#wt')$('#wtHint').textContent=")
# hash links: accept #fluids and #p-fluids
script = script.replace("const h=(location.hash||'').slice(1);",
                        "const h=(location.hash||'').slice(1).replace(/^p-/,'');")
script = script.replace("try{localStorage.setItem('pedsTab',id)}catch(e){}",
                        "try{localStorage.setItem('pedsTab',id)}catch(e){}\n  try{history.replaceState(null,'','#'+id)}catch(e){}")
script += "\nwindow.addEventListener('hashchange',function(){var t=(location.hash||'').slice(1).replace(/^p-/,'');var b=document.querySelector('nav.tabs button[data-tab=\"'+t+'\"]');if(b)b.click();});\n"

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Pediatric ER Doses — Family Medicine Guides</title>
<meta content="Weight-based pediatric ER and urgent-care doses, fluids, KCl and transfusion calculators, PRAM, Westley, CDS and PECARN scores, and when to admit or refer." name="description"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&amp;family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@400;500&amp;family=IBM+Plex+Sans+Arabic:wght@400;600&amp;display=swap" rel="stylesheet"/>
<style>
/* Pediatric ER Doses (prefix-free, scoped to #pe) */
{css.strip()}
</style>
</head>
<body>
{{% include "nav.html" %}}
<div id="pe">
{markup.strip()}
</div>
<footer>
{{% include "credit.html" %}}
</footer>
<script>
{{% raw %}}{script.strip()}{{% endraw %}}
</script>
</body>
</html>
"""
# American spelling to match the rest of the site
for a, b in [("Paediatric", "Pediatric"), ("paediatric", "pediatric"), ("aemia", "emia"), ("aematoma", "ematoma"),
             ("Haem", "Hem"), ("haem", "hem"), ("oedema", "edema"), ("Oedema", "Edema"), ("aemic", "emic"),
             ("nebulised", "nebulized"), ("nebulisation", "nebulization"), ("generalises", "generalizes"),
             ("atomiser", "atomizer"), ("nebuliser", "nebulizer"), ("Hypoglycaemia", "Hypoglycemia"),
             ("hypoglycaemia", "hypoglycemia"), ("ketoacidosis", "ketoacidosis"), ("anaemia", "anemia")]:
    page = page.replace(a, b)
# keep literature titles intact
page = page.replace("Lancet Hematol", "Lancet Haematol")
(ROOT / "peds-er.html").write_text(page, encoding="utf-8")

# ---------- 2. nav, homepage, directory ----------
CHEV = '<svg class="fmg-chev" width="8" height="14" viewBox="0 0 8 14" fill="none"><path d="M1 1l6 6-6 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def nav_row(color):
    return (f'<a href="peds-er.html" class="fmg-row"><span class="fmg-row-main"><span class="fmg-row-dot" style="background:{color}"></span>'
            '<span class="fmg-row-text"><span class="fmg-row-label">Pediatric ER Doses</span><span class="fmg-row-sub">weight-based doses · nebulizers · scores</span></span></span>'
            + CHEV + '</a>\n')

nav = ROOT / "_includes/nav.html"; t = nav.read_text(encoding="utf-8")
if "peds-er.html" not in t:
    t = t.replace('<div class="fmg-panel" data-panel="cat-urgent">', '<div class="fmg-panel" data-panel="cat-urgent">', 1)
    i = t.index('data-panel="cat-urgent"'); j = t.index('<div class="fmg-menu-section-label">Live protocols</div>\n', i) + len('<div class="fmg-menu-section-label">Live protocols</div>\n')
    t = t[:j] + nav_row("#B0392C") + t[j:]
    i = t.index('data-panel="cat-peds"'); j = t.index('</button>\n', i) + len('</button>\n')
    t = t[:j] + '<div class="fmg-menu-section-label">Emergency dosing</div>\n' + nav_row("#C98A2C") + t[j:]
    t = t.replace('Urgent Care &amp; Emergencies</span><span class="fmg-row-sub">15 live · 5 planned', 'Urgent Care &amp; Emergencies</span><span class="fmg-row-sub">16 live · 5 planned')
    t = t.replace('Pediatrics</span><span class="fmg-row-sub">3 live · 11 planned', 'Pediatrics</span><span class="fmg-row-sub">4 live · 11 planned')
    nav.write_text(t, encoding="utf-8")

idx = ROOT / "index.html"; t = idx.read_text(encoding="utf-8")
if "pediatric er doses" not in t:
    t = t.replace('data-tags="urgent care &amp; emergencies ', 'data-tags="urgent care &amp; emergencies pediatric er doses weight-based calculator fluids kcl prbc infusion ', 1)
    t = t.replace('data-tags="pediatrics ', 'data-tags="pediatrics pediatric er doses weight-based calculator pram westley croup dehydration pecarn febrile infant ', 1)
    t = t.replace('<span class="cat-count">15 live · 5 planned</span>', '<span class="cat-count">16 live · 5 planned</span>', 1)
    t = t.replace('<span class="cat-count">3 live · 11 planned</span>', '<span class="cat-count">4 live · 11 planned</span>', 1)
    t = t.replace('<a href="asthma.html" class="quick-pill" style="--pc:#C98A2C"><span class="quick-dot"></span>Pediatric Asthma</a>',
                  '<a href="asthma.html" class="quick-pill" style="--pc:#C98A2C"><span class="quick-dot"></span>Pediatric Asthma</a>\n      <a href="peds-er.html" class="quick-pill" style="--pc:#B0392C"><span class="quick-dot"></span>Pediatric ER Doses</a>', 1)
    idx.write_text(t, encoding="utf-8")

cat = ROOT / "categories.html"; t = cat.read_text(encoding="utf-8")
if "peds-er.html" not in t:
    def dir_row(color, sub):
        return (f'<a class="dir-row dir-live" href="peds-er.html"><span class="dir-dot" style="background:{color}"></span><span class="dir-text">'
                f'<span class="dir-title">Pediatric ER Doses</span><span class="dir-sub">{sub}</span></span><span class="dir-open">Open →</span></a>')
    t = t.replace('<h3 class="dir-group" id="live-protocols">Live protocols</h3>',
                  '<h3 class="dir-group" id="live-protocols">Live protocols</h3>' + dir_row("#B0392C", "weight-based doses, fluids, infusions, nebulizers, scores"), 1)
    t = t.replace('<h3 class="dir-group" id="respiratory">Respiratory</h3>',
                  '<h3 class="dir-group" id="emergency-dosing">Emergency dosing</h3>' + dir_row("#C98A2C", "calculator · PRAM · Westley · CDS · PECARN · admit/refer")
                  + '<h3 class="dir-group" id="respiratory">Respiratory</h3>', 1)
    t = t.replace('<p class="dir-count">15 live · 5 planned</p>', '<p class="dir-count">16 live · 5 planned</p>', 1)
    t = t.replace('<p class="dir-count">3 live · 11 planned</p>', '<p class="dir-count">4 live · 11 planned</p>', 1)
    cat.write_text(t, encoding="utf-8")

# ---------- 3. search index (all peds-er entries rebuilt each run) ----------
si = ROOT / "search-index.js"; t = si.read_text(encoding="utf-8")
pre, arr, post = t[:t.index("[")], json.loads(t[t.index("["):t.rindex("]") + 1]), t[t.rindex("]") + 1:]
G = dict(guide="peds-er.html", guideTitle="Pediatric ER Doses", tag="#C98A2C")
E = [
 ("p-review", "What changed from common quick-note doses", "ما الذي تغيّر في جرعات الملاحظات الشائعة", "PRBC 10–15 mL/kg not mg/kg; morphine 0.05–0.1 mg/kg; granisetron IV 10–40 mcg/kg; salbutamol 2.5 mg under 20 kg; prednisolone once daily; GINA 2026 oxygen targets; elemental iron 3 mg/kg/day.", "dose errors corrections morphine granisetron prbc gina 2026"),
 ("p-fluids", "Pediatric fluids, KCl and transfusion calculator", "حاسبة السوائل والبوتاسيوم ونقل الدم للأطفال", "Holliday–Segar 4-2-1 maintenance, 2/3 maintenance, shock/DKA/cardiac boluses, KCl mEq/kg/day check, PRBC volume from Hb, albumin, hypoglycemia D10.", "maintenance bolus potassium kcl blood transfusion albumin dextrose"),
 ("p-drugs", "Pediatric ER drug doses by weight and age", "جرعات أدوية الطوارئ للأطفال حسب الوزن والعمر", "Paracetamol, ibuprofen, salbutamol, ipratropium, prednisolone, dexamethasone, magnesium, ondansetron, granisetron, ceftriaxone, amoxicillin, furosemide, iron — capped at maximum doses, age limits flagged.", "acetaminophen paracetamol ibuprofen steroids antiemetic antibiotics age months"),
 ("p-nebs", "Nebulizer doses in mL: child and adult", "جرعات جهاز البخار بالمليلتر للطفل والبالغ", "Salbutamol, ipratropium, budesonide, normal saline 0.9%, hypertonic saline 3% and 7%, epinephrine (croup, angioedema), racemic epinephrine, isotonic magnesium, dornase alfa: mL per session, fill volume, mixing, oxygen vs air, infection control.", "nebuliser neb volume ml hypertonic saline budesonide pulmicort atrovent ventolin combivent adrenaline croup cystic fibrosis"),
 ("p-resus", "Pediatric resuscitation and vasoactive infusions", "إنعاش الأطفال وتسريب الأدوية الرافعة للضغط", "Epinephrine arrest and IM anaphylaxis, defibrillation joules, amiodarone, adenosine, atropine, naloxone, 3% saline, ETT size by age, hypotension threshold; epinephrine, norepinephrine and milrinone infusion rates.", "pals epinephrine adrenaline noradrenaline milrinone inotrope cardiac arrest ett"),
 ("p-sed", "Pediatric status epilepticus, sedation and analgesia", "الحالة الصرعية والتهدئة وتسكين الألم عند الأطفال", "Midazolam, lorazepam, levetiracetam, fosphenytoin, valproate timeline; fentanyl IN/IV, morphine, ketamine sedation and analgesia doses.", "seizure benzodiazepine ketamine fentanyl morphine midazolam procedural sedation"),
 ("p-scores", "Pediatric scores: PRAM, Westley, CDS, PECARN", "مقاييس الأطفال: PRAM وWestley والجفاف وPECARN", "Asthma PRAM, croup Westley, Clinical Dehydration Scale with ORT volumes, PECARN head CT rule, AAP 2021 febrile infant 8–60 days.", "asthma croup dehydration head injury febrile infant score calculator"),
 ("p-dispo", "Pediatric ER: when to admit, call PICU or refer", "طوارئ الأطفال: متى ننوّم أو نستدعي العناية المركزة أو نحوّل", "Disposition criteria for asthma, croup, bronchiolitis, gastroenteritis, DKA, febrile infant, seizure, head injury, anaphylaxis and sickle cell; parent leaflets.", "admission discharge referral picu transfer disposition leaflet"),
]
arr = [e for e in arr if e.get("guide") != "peds-er.html"] + [dict(G, id=i, heading=h, snippet=sn, headingAr=ha, kw=k) for i, h, ha, sn, k in E]
si.write_text(pre + json.dumps(arr, ensure_ascii=False) + post, encoding="utf-8")
# subtitles on an already-wired site
for f, a, b in [("_includes/nav.html", "weight-based calculator · scores · disposition", "weight-based doses · nebulizers · scores"),
                ("categories.html", "weight-based doses, fluids, infusions, scores<", "weight-based doses, fluids, infusions, nebulizers, scores<")]:
    q = ROOT / f; x = q.read_text(encoding="utf-8")
    if a in x: q.write_text(x.replace(a, b), encoding="utf-8")
idx = ROOT / "index.html"; x = idx.read_text(encoding="utf-8")
if "nebulizer" not in x:
    x = x.replace("pediatric er doses weight-based calculator fluids kcl prbc infusion ", "pediatric er doses weight-based calculator fluids kcl prbc infusion nebulizer budesonide hypertonic saline ", 1)
    idx.write_text(x, encoding="utf-8")
print("done")
