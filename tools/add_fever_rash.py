"""Wire the Fever with Rash guide (fever-rash.html) into the site.

Run after tools/fever-rash-source/build_page.py has written src/fever-rash.html.
Adds: menu rows (Live guides, Pediatrics, Dermatology, Infectious Disease),
homepage pill + card counts/tags, directory rows/counts, and search-index entries.
Idempotent: everything is skipped if already present (marker FMG-FEVER-RASH).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "src"
HERE = Path(__file__).resolve().parent / "fever-rash-source"
TONE = "#9B3D5A"
MARK = "FMG-FEVER-RASH"
CHEV = ('<svg class="fmg-chev" width="8" height="14" viewBox="0 0 8 14" fill="none"><path d="M1 1l6 6-6 6" '
        'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def once(s, old, new, what):
    n = s.count(old)
    assert n == 1, f"{what}: found {n}"
    return s.replace(old, new)


def nav_row(href, label, sub, color):
    return (f'<a href="{href}" class="fmg-row"><span class="fmg-row-main"><span class="fmg-row-dot" style="background:{color}"></span>'
            f'<span class="fmg-row-text"><span class="fmg-row-label">{label}</span><span class="fmg-row-sub">{sub}</span></span></span>{CHEV}</a>\n')


def dir_row(href, title, sub, color):
    return (f'<a class="dir-row dir-live" href="{href}"><span class="dir-dot" style="background:{color}"></span><span class="dir-text">'
            f'<span class="dir-title">{title}</span><span class="dir-sub">{sub}</span></span><span class="dir-open">Open →</span></a>')


def panel_span(t, name):
    i = t.index(f'data-panel="{name}"')
    j = t.index('<div class="fmg-panel"', i + 10)
    return i, j


# ---------- 1. shared menu ----------
nav_p = ROOT / "_includes/nav.html"
t = nav_p.read_text(encoding="utf-8")
if MARK not in t:
    # Live guides: after Counselling
    i, j = panel_span(t, "live")
    k = t.index('<a href="osce.html" class="fmg-row">', i)
    assert k < j
    t = t[:k] + f"<!-- {MARK} -->" + nav_row("fever-rash.html", "Fever with Rash (children)", "measles → impetigo · CDC precautions · bilingual", TONE) + t[k:]
    # Pediatrics: after "Fever in the infant ≤90 days"
    i, j = panel_span(t, "cat-peds")
    k = t.index('href="urgent-care.html#febrile-infant"', i)
    k = t.index("</a>", k) + len("</a>\n")
    assert k < j
    t = t[:k] + nav_row("fever-rash.html", "Fever with rash", "measles · chickenpox · scarlet fever · impetigo · Kawasaki", "#C98A2C") + t[k:]
    t = once(t, 'Pediatrics</span><span class="fmg-row-sub">4 live · 11 planned', 'Pediatrics</span><span class="fmg-row-sub">5 live · 11 planned', "peds count")
    # Dermatology: new group before Cross-cutting tools
    i, j = panel_span(t, "cat-derm")
    lab = '<div class="fmg-menu-section-label">Cross-cutting tools</div>'
    k = t.index(lab, i)
    assert k < j
    t = t[:k] + '<div class="fmg-menu-section-label">Skin infections in children</div>\n' + nav_row("fever-rash.html", "Infectious rashes &amp; impetigo", "varicella · HFMD · SSSS · photos", "#B08A2C") + t[k:]
    t = once(t, 'Dermatology</span><span class="fmg-row-sub">8 live · 7 planned', 'Dermatology</span><span class="fmg-row-sub">9 live · 7 planned', "derm count")
    # Infectious disease: Live group before Planned
    i, j = panel_span(t, "cat-infx")
    lab = '<div class="fmg-menu-section-label">Planned</div>'
    k = t.index(lab, i)
    assert k < j
    t = t[:k] + '<div class="fmg-menu-section-label">Live</div>\n' + nav_row("fever-rash.html", "Fever with rash in children", "isolation · school exclusion · PEP · pregnancy", "#7A3E3E") + t[k:]
    t = once(t, 'Infectious Disease</span><span class="fmg-row-sub">6 planned', 'Infectious Disease</span><span class="fmg-row-sub">1 live · 6 planned', "infx count")
    nav_p.write_text(t, encoding="utf-8")

# ---------- 2. homepage ----------
idx_p = ROOT / "index.html"
t = idx_p.read_text(encoding="utf-8")
if MARK not in t:
    pill = '<a href="peds-er.html" class="quick-pill" style="--pc:#B0392C"><span class="quick-dot"></span>Pediatric ER Doses</a>'
    t = once(t, pill, pill + f'\n      <!-- {MARK} --><a href="fever-rash.html" class="quick-pill" style="--pc:{TONE}"><span class="quick-dot"></span>Fever with Rash</a>', "pill")
    t = once(t, 'data-tags="pediatrics ', 'data-tags="pediatrics fever with rash measles rubella mumps chickenpox varicella roseola fifth disease slapped cheek scarlet fever impetigo kawasaki hand foot mouth ', "peds tags")
    t = once(t, 'data-tags="dermatology ', 'data-tags="dermatology childhood rashes impetigo chickenpox shingles hand foot mouth ssss scalded skin viral exanthem ', "derm tags")
    t = once(t, 'data-tags="infectious disease ', 'data-tags="infectious disease fever with rash measles isolation precautions airborne droplet school exclusion post-exposure prophylaxis meningococcal mpox ', "infx tags")
    # counts on the three cards (each card: <a ... data-tags=...> ... <span class="cat-count">)
    for href, old, new in [("categories.html#cat-peds", "4 live · 11 planned", "5 live · 11 planned"),
                           ("categories.html#cat-derm", "8 live · 7 planned", "9 live · 7 planned"),
                           ("categories.html#cat-infx", "6 planned", "1 live · 6 planned")]:
        a = t.index(f'<a href="{href}" class="cat-card"')
        b = t.index("</a>", a)
        card = t[a:b]
        card2 = once(card, f'<span class="cat-count">{old}</span>', f'<span class="cat-count">{new}</span>', href)
        t = t[:a] + card2 + t[b:]
    idx_p.write_text(t, encoding="utf-8")

# ---------- 3. directory ----------
cat_p = ROOT / "categories.html"
t = cat_p.read_text(encoding="utf-8")
if MARK not in t:
    def section(t, cid):
        a = t.index(f'id="{cid}"')
        b = t.index("</section>", a)
        return a, b
    a, b = section(t, "cat-peds")
    sec = t[a:b]
    k = sec.index('href="urgent-care.html#febrile-infant"')
    k = sec.index("</a>", k) + len("</a>")
    sec = sec[:k] + f"<!-- {MARK} -->" + dir_row("fever-rash.html", "Fever with rash", "measles · chickenpox · scarlet fever · impetigo · Kawasaki · CDC precautions", "#C98A2C") + sec[k:]
    sec = once(sec, '<p class="dir-count">4 live · 11 planned</p>', '<p class="dir-count">5 live · 11 planned</p>', "dir peds")
    t = t[:a] + sec + t[b:]
    a, b = section(t, "cat-derm")
    sec = t[a:b]
    g = '<h3 class="dir-group" id="cross-cutting-tools">Cross-cutting tools</h3>'
    sec = once(sec, g, '<h3 class="dir-group" id="skin-infections-children">Skin infections in children</h3>'
               + dir_row("fever-rash.html#impetigo", "Infectious rashes &amp; impetigo", "varicella · HFMD · SSSS · with photos", "#B08A2C") + g, "dir derm")
    sec = once(sec, '<p class="dir-count">8 live · 7 planned</p>', '<p class="dir-count">9 live · 7 planned</p>', "dir derm count")
    t = t[:a] + sec + t[b:]
    a, b = section(t, "cat-infx")
    sec = t[a:b]
    g = '<h3 class="dir-group" id="planned-12">Planned</h3>'
    sec = once(sec, g, '<h3 class="dir-group" id="live-infx">Live</h3>'
               + dir_row("fever-rash.html", "Fever with rash in children", "isolation precautions · school exclusion · post-exposure prophylaxis · pregnancy", "#7A3E3E") + g, "dir infx")
    sec = once(sec, '<p class="dir-count">0 live · 6 planned</p>', '<p class="dir-count">1 live · 6 planned</p>', "dir infx count")
    t = t[:a] + sec + t[b:]
    cat_p.write_text(t, encoding="utf-8")

# ---------- 4. search index ----------
si = ROOT / "search-index.js"
t = si.read_text(encoding="utf-8")
if '"guide": "fever-rash.html"' not in t:
    ents = json.load(open(HERE / "fever_rash_entries.json", encoding="utf-8"))
    add = ", ".join(json.dumps(e, ensure_ascii=False) for e in ents)
    t = t.rstrip()
    assert t.endswith("];"), t[-40:]
    t = t[:-2].rstrip() + ", " + add + "];\n"
    si.write_text(t, encoding="utf-8")
print("fever-rash wired")
