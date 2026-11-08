"""Add the Peds ER parent leaflets to patients.html and the search index.

usage: python3 tools/add_peds_leaflets_site.py
Idempotent. Cards use the same markup as the existing leaflet cards; they go
after the home blood glucose card. Build the PDFs/cards first with
tools/public-education-source/build_peds_leaflets.py src
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(Path(__file__).resolve().parent / "public-education-source"))
from peds_leaflets import PEDS_LEAFLETS

def card(L):
    s = L["slug"]
    return f"""<article class="pt-card" id="leaflet-{s}" style="--c:{L['tone']}">
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
</article>"""

pg = ROOT / "patients.html"; t = pg.read_text(encoding="utf-8")
anchor = '<article class="pt-card" id="leaflet-home-blood-glucose"'
i = t.index(anchor); j = t.index("</article>", i) + len("</article>")
add = "".join("\n" + card(L) for L in PEDS_LEAFLETS if f'id="leaflet-{L["slug"]}"' not in t)
if add:
    t = t[:j] + add + t[j:]
    pg.write_text(t, encoding="utf-8")

si = ROOT / "search-index.js"; x = si.read_text(encoding="utf-8")
pre, arr, post = x[:x.index("[")], json.loads(x[x.index("["):x.rindex("]") + 1]), x[x.rindex("]") + 1:]
have = {(e["guide"], e["id"]) for e in arr}
for L in PEDS_LEAFLETS:
    key = ("patients.html", "leaflet-" + L["slug"])
    if key not in have:
        arr.append(dict(guide="patients.html", guideTitle="For patients & families", tag=L["tone"], id=key[1],
                        heading=L["title_en"] + " — patient leaflet", snippet=L["card_en"],
                        headingAr=L["title_ar"] + " — نشرة للمريض", snippetAr=L["card_ar"]))
si.write_text(pre + json.dumps(arr, ensure_ascii=False) + post, encoding="utf-8")
print("done")
