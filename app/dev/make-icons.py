"""Draws the app icon (original geometric mark: rounded plus with an amber centre)
and writes PNG sizes + SVG into app/static/icons/. Run: python3 app/dev/make-icons.py"""
from PIL import Image, ImageDraw
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "static" / "icons"
OUT.mkdir(parents=True, exist_ok=True)
DEEP, TEAL, CREAM, AMBER = (18, 60, 56), (31, 92, 85), (244, 246, 242), (201, 138, 44)
S = 2048  # draw large, then downsample

def vertical_gradient(size, top, bottom):
    g = Image.new("RGB", (1, size))
    for y in range(size):
        t = y / (size - 1)
        g.putpixel((0, y), tuple(round(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    return g.resize((size, size))

def mark(draw, cx, cy, scale):
    arm, length, r = 0.30 * scale, 1.0 * scale, 0.15 * scale
    draw.rounded_rectangle([cx - arm / 2, cy - length / 2, cx + arm / 2, cy + length / 2], radius=r, fill=CREAM)
    draw.rounded_rectangle([cx - length / 2, cy - arm / 2, cx + length / 2, cy + arm / 2], radius=r, fill=CREAM)
    d = 0.17 * scale
    draw.ellipse([cx - d / 2, cy - d / 2, cx + d / 2, cy + d / 2], fill=AMBER)

def icon(maskable=False):
    bg = vertical_gradient(S, TEAL, DEEP).convert("RGBA")
    if not maskable:  # rounded square with transparent corners
        m = Image.new("L", (S, S), 0)
        ImageDraw.Draw(m).rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.22), fill=255)
        bg.putalpha(m)
    mark(ImageDraw.Draw(bg), S / 2, S / 2, S * (0.46 if maskable else 0.58))
    return bg

std, msk = icon(), icon(maskable=True)
for size, name in [(512, "icon-512.png"), (192, "icon-192.png"), (32, "favicon-32.png")]:
    std.resize((size, size), Image.LANCZOS).save(OUT / name, optimize=True)
msk.resize((512, 512), Image.LANCZOS).save(OUT / "maskable-512.png", optimize=True)
# Apple ignores transparency: use the full-bleed version.
msk_apple = icon(maskable=True)
msk_apple.convert("RGB").resize((180, 180), Image.LANCZOS).save(OUT / "apple-touch-icon.png", optimize=True)

(OUT / "icon.svg").write_text("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1F5C55"/><stop offset="1" stop-color="#123C38"/></linearGradient></defs>
<rect width="100" height="100" rx="22" fill="url(#g)"/>
<rect x="41.3" y="21" width="17.4" height="58" rx="8.7" fill="#F4F6F2"/>
<rect x="21" y="41.3" width="58" height="17.4" rx="8.7" fill="#F4F6F2"/>
<circle cx="50" cy="50" r="4.9" fill="#C98A2C"/>
</svg>
""")
print("icons written to", OUT)
