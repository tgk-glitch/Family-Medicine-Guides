"""Render the fever-and-rash parent leaflet (EN/AR PDF + WhatsApp card) with the
shared leaflet engine, and list it on patients.html.

usage: FMG_FONTS=/path/to/fonts python3 tools/fever-rash-source/build_leaflet.py [--final]
Writes src/downloads/leaflets/fever-rash-{en,ar}.pdf and -card.png.
Only this leaflet is rendered; the other leaflets are left untouched.
"""
import sys, tempfile, shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "tools/public-education-source"))
sys.path.insert(0, str(HERE))
import build_leaflets as B
from leaflet_fr import FEVER_RASH

B.LEAFLETS = [FEVER_RASH]
B.REVIEWED = {"en": "November 2026", "ar": "نوفمبر 2026"}
B.NEXT_REVIEW = {"en": "November 2027, or sooner if guidance changes",
                 "ar": "نوفمبر 2027، أو قبل ذلك إذا تغيّرت التوصيات"}

final = "--final" in sys.argv
with tempfile.TemporaryDirectory() as tmp:
    for r in B.build(tmp, final):
        print(r)
    dst = ROOT / "src/downloads/leaflets"
    for f in (Path(tmp) / "downloads/leaflets").glob("fever-rash-*"):
        shutil.copyfile(f, dst / f.name)
        print("wrote", f.name)

# ---------- list on patients.html ----------
MARK = "leaflet-fever-rash"
pp = ROOT / "src/patients.html"
t = pp.read_text(encoding="utf-8")
if MARK not in t:
    L = FEVER_RASH
    s = L["slug"]
    card = f'''<article class="pt-card" id="{MARK}" style="--c:{L['tone']}">
<div class="pt-card-top"><span class="fmg-en pt-topic">{L['topic_en']}</span><span class="fmg-ar pt-topic" lang="ar">{L['topic_ar']}</span><span class="fmg-en pt-status">Draft — under clinical review</span><span class="fmg-ar pt-status" lang="ar">مسودة — قيد المراجعة السريرية</span></div>
<h3 class="fmg-en">{L['title_en']}</h3><h3 class="fmg-ar" lang="ar">{L['title_ar']}</h3>
<p class="fmg-en">{L['card_en']}</p><p class="fmg-ar" lang="ar">{L['card_ar']}</p>
<div class="pt-dl">
<a class="pt-btn pt-btn-main" href="downloads/leaflets/{s}-en.pdf" download><span class="fmg-en">Leaflet · English (PDF)</span><span class="fmg-ar" lang="ar">النشرة · الإنجليزية (PDF&rlm;)</span></a>
<a class="pt-btn pt-btn-main" href="downloads/leaflets/{s}-ar.pdf" download><span class="fmg-en">Leaflet · Arabic (PDF)</span><span class="fmg-ar" lang="ar">النشرة · العربية (PDF&rlm;)</span></a>
<a class="pt-btn" href="downloads/leaflets/{s}-en-card.png" download><span class="fmg-en">Summary card · English</span><span class="fmg-ar" lang="ar">بطاقة ملخّص · الإنجليزية</span></a>
<a class="pt-btn" href="downloads/leaflets/{s}-ar-card.png" download><span class="fmg-en">Summary card · Arabic</span><span class="fmg-ar" lang="ar">بطاقة ملخّص · العربية</span></a>
</div>
<a class="pt-guide" href="{L['guide']}"><span class="fmg-en">Clinician guide for this topic →</span><span class="fmg-ar" lang="ar">دليل الطبيب لهذا الموضوع ←</span></a>
</article>'''
    anchor = '<article class="pt-card" id="leaflet-quit-smoking"'
    assert t.count(anchor) == 1
    t = t.replace(anchor, card + anchor)
    pp.write_text(t, encoding="utf-8")
    print("patients.html: card added")
