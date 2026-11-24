"""Render the 24 Nov 2026 v2 newspaper front page from stories.json.

- Fills template.html with data from stories.json (code-drawn layout).
- Screenshots at exactly 1024x1024 with Playwright Chromium (headless shell).
- Converts to JPEG (quality 88), checks <= 1 MiB and <= 1024x1024.
- Renders twice and compares SHA-256 to verify byte-identical determinism.
- Writes a 300px-wide preview for the small-size readability check.
- Checks the page does not overflow the 1024x1024 frame.

Run: ~/workspace/makefun-news-image/.venv-render/bin/python render.py
Outputs: render.html, render.png, news-20261124.jpg, preview-300.png
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

ICONS = {
    "burst": '<svg viewBox="0 0 24 24" fill="none" stroke="#16233f" stroke-width="1.7" stroke-linecap="round"><circle cx="12" cy="12" r="2.2"/><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M18.4 5.6l-2.8 2.8M8.4 15.6l-2.8 2.8"/></svg>',
    "satellite": '<svg viewBox="0 0 24 24" fill="none" stroke="#16233f" stroke-width="1.7" stroke-linecap="round"><rect x="10" y="10" width="5" height="5"/><path d="M10 12.5H4M20 12.5h-5M12.5 10V4M12.5 20v-5M4 9.5v6M20 9.5v6"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="#16233f" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 15.5h6"/></svg>',
    "scales": '<svg viewBox="0 0 24 24" fill="none" stroke="#16233f" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v16M8 20h8M12 6L7 8M12 6l5 2M7 8l-2.5 5h5L7 8zM17 8l-2.5 5h5L17 8z"/></svg>',
    "chip": '<svg viewBox="0 0 24 24" fill="none" stroke="#16233f" stroke-width="1.7" stroke-linecap="round"><rect x="7" y="7" width="10" height="10"/><rect x="10.2" y="10.2" width="3.6" height="3.6"/><path d="M9.5 7V3.5M14.5 7V3.5M9.5 20.5V17M14.5 20.5V17M7 9.5H3.5M7 14.5H3.5M20.5 9.5H17M20.5 14.5H17"/></svg>',
    "waves": '<svg viewBox="0 0 24 24" fill="none" stroke="#16233f" stroke-width="1.7" stroke-linecap="round"><path d="M3 8c2-2 4-2 6 0s4 2 6 0 4-2 6 0M3 13c2-2 4-2 6 0s4 2 6 0 4-2 6 0M3 18c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/></svg>',
    "plane": '<svg viewBox="0 0 24 24" fill="none" stroke="#16233f" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l18-7-7 18-2.5-7.5z"/><path d="M12 18.5L21 4"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="#16233f" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
    "columns": '<svg viewBox="0 0 24 24" fill="none" stroke="#16233f" stroke-width="1.7" stroke-linecap="round"><path d="M4 5h16M6 5v11M10 5v11M14 5v11M18 5v11M3 19h18M3 16h18"/></svg>',
}

# Coarse land mask as rectangles (row_start, row_end, col_start, col_end)
# on a 64 cols (lon -180..180) x 32 rows (lat 90..-90) grid.
LAND_RECTS = [
    (2, 4, 1, 6), (2, 6, 7, 21), (6, 8, 5, 20), (9, 11, 3, 7), (1, 4, 23, 26),
    (11, 13, 18, 24), (14, 17, 19, 25), (18, 20, 20, 24), (21, 22, 21, 23),
    (3, 5, 33, 37), (5, 6, 30, 31), (5, 8, 31, 39), (8, 9, 30, 32),
    (7, 9, 29, 41), (10, 13, 30, 41), (14, 16, 32, 40), (17, 19, 34, 38),
    (2, 5, 39, 62), (6, 10, 48, 56), (8, 10, 38, 44), (10, 13, 44, 48),
    (11, 13, 50, 55), (6, 8, 58, 60), (13, 14, 50, 58),
    (15, 17, 52, 59), (18, 19, 53, 57), (18, 20, 60, 61),
]

# (lat, lon) of the 13 main stories, for map pins.
PINS = {
    1: (40.7, -74.0), 2: (31.5, 34.45), 3: (47.85, 35.12), 4: (50.85, 4.35),
    5: (55.75, 37.6), 6: (38.0, -78.5), 7: (37.57, 126.98), 8: (25.03, 121.56),
    9: (27.85, 87.9), 10: (37.57, 126.98), 11: (52.6, 1.3), 12: (52.52, 13.4),
    13: (38.9, -77.04),
}
# nudge (dx, dy) in px for pins that would overlap a neighbour.
NUDGE = {1: (-8, -9), 10: (15, 11), 13: (-13, 8), 11: (-7, 0)}


def build_map_svg() -> str:
    w, h = 340, 170
    land = [[False] * 64 for _ in range(32)]
    for r0, r1, c0, c1 in LAND_RECTS:
        for r in range(r0, r1 + 1):
            for c in range(c0, c1 + 1):
                land[r][c] = True
    dots = []
    for r in range(32):
        for c in range(64):
            if land[r][c]:
                cx = (c + 0.5) * w / 64
                cy = (r + 0.5) * h / 32
                dots.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="1.9" fill="#8a7d5f"/>')
    pins = []
    for n, (lat, lon) in PINS.items():
        x = (lon + 180) / 360 * w
        y = (90 - lat) / 180 * h
        dx, dy = NUDGE.get(n, (0, 0))
        px, py = x + dx, y + dy
        if (dx, dy) != (0, 0):
            pins.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{px:.1f}" y2="{py:.1f}" stroke="#a93226" stroke-width="1"/>')
        pins.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="7.5" fill="#a93226"/>')
        pins.append(f'<text x="{px:.1f}" y="{py + 3:.1f}" font-size="9" font-weight="bold" fill="#f6f1e5" text-anchor="middle" font-family="Noto Sans, sans-serif">{n}</text>')
    return ('<svg width="340" height="170" viewBox="0 0 340 170">'
            + "".join(dots) + "".join(pins) + "</svg>")


def build_html(data: dict) -> str:
    tpl = (HERE / "template.html").read_text(encoding="utf-8")
    lead = data["lead"]
    timeline = "".join(
        f'<div class="tl-item"><b>{t}</b>{txt}</div>' for t, txt in data["timeline"]
    )
    numbers = "".join(
        f'<div class="num-item"><b>{v}</b><span>{txt}</span></div>' for v, txt in data["numbers"]
    )
    main = "".join(
        f'<div class="story"><div class="s-num">{s["n"]}</div>'
        f'<div class="s-icon">{ICONS[s["icon"]]}</div>'
        f'<div class="s-body"><div class="s-tag">{s["place"]} · {s["field"]} &nbsp;<span class="src">{s["tag"]} · {s["source"]}</span></div>'
        f'<div class="s-title">{s["title"]}</div>'
        f'<div class="s-sum">{s["summary"]}</div></div></div>'
        for s in data["main"]
    )
    also = data["also"]
    cols = [also[:8], also[8:]]
    also_html = "".join(
        "<div>" + "".join(
            f'<div class="a-item"><span class="a-num">{a["n"]}</span> <b>{a["place"]} —</b> {a["text"]} '
            f'<span class="a-src">({a["tag"]} · {a["source"]})</span></div>'
            for a in col
        ) + "</div>"
        for col in cols
    )
    out = tpl
    for key, val in {
        "%%MASTHEAD%%": data["masthead"],
        "%%SPEC%%": data["spec"],
        "%%DATE_LONG%%": data["date_long"],
        "%%LEAD_FIELD%%": lead["field"],
        "%%LEAD_PLACE%%": lead["place"],
        "%%LEAD_TAG%%": lead["tag"],
        "%%LEAD_SOURCE%%": lead["source"],
        "%%LEAD_CLAIM%%": lead["claim"],
        "%%LEAD_TITLE%%": lead["title"],
        "%%LEAD_SUMMARY%%": lead["summary"],
        "%%TIMELINE%%": timeline,
        "%%NUMBERS%%": numbers,
        "%%MAIN%%": main,
        "%%ALSO%%": also_html,
        "%%MAP%%": build_map_svg(),
        "%%REGIONS%%": data["regions"],
        "%%DATECHECK%%": data["datecheck"],
        "%%NOTYET%%": data["notyet"],
        "%%LEGEND%%": data["legend"],
        "%%FOOTNOTE%%": data["footnote"],
    }.items():
        out = out.replace(key, val)
    assert "%%" not in out, "unfilled template token remains"
    return out


def screenshot(html: str, png_path: Path) -> dict:
    sys.path.insert(0, str(Path.home() / "workspace/makefun-news-image/.venv-render/lib/python3.13/site-packages"))
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1024, "height": 1024}, device_scale_factor=1)
        pg.set_content(html, wait_until="load")
        pg.wait_for_timeout(400)
        metrics = pg.evaluate(
            "() => ({scrollW: document.documentElement.scrollWidth, "
            "scrollH: document.documentElement.scrollHeight, "
            "bodyH: document.body.scrollHeight})"
        )
        pg.screenshot(path=str(png_path))
        b.close()
    return metrics


def to_jpeg(png_path: Path, jpg_path: Path, quality: int = 88) -> tuple[int, int, int]:
    from PIL import Image
    im = Image.open(png_path).convert("RGB")
    im.save(jpg_path, "JPEG", quality=quality)
    return im.size[0], im.size[1], jpg_path.stat().st_size


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    data = json.loads((HERE / "stories.json").read_text(encoding="utf-8"))
    html = build_html(data)
    (HERE / "render.html").write_text(html, encoding="utf-8")
    hashes = []
    for i in (1, 2):
        png = HERE / f"render-{i}.png"
        metrics = screenshot(html, png)
        w, h, size = to_jpeg(png, HERE / "news-20261124.jpg")
        hashes.append(sha256(HERE / "news-20261124.jpg"))
        print(f"run {i}: png={png.name} metrics={metrics} jpeg={w}x{h} {size} bytes sha={hashes[-1][:16]}")
    from PIL import Image
    im = Image.open(HERE / "news-20261124.jpg")
    im.resize((300, 300)).save(HERE / "preview-300.png")
    print(f"deterministic: {hashes[0] == hashes[1]}")
    print(f"size_ok_1MiB: {size <= 1024 * 1024} ({size} bytes)")
    print(f"overflow: scrollH={metrics['scrollH']} (frame 1024)")


if __name__ == "__main__":
    main()
