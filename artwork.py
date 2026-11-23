"""Offline design source for the World Briefing page of Monday 23 November 2026.

Run ``python3 artwork.py`` to draw ``entry.png`` (1024 by 1024) beside this file.
Only Pillow and the DejaVu fonts in ``/usr/share/fonts/truetype/dejavu/`` are used.
"""

from __future__ import annotations

from functools import cache
from typing import TypedDict

from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_BOLD = FONT_DIR + "DejaVuSerif-Bold.ttf"
SERIF = FONT_DIR + "DejaVuSerif.ttf"
SANS_BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"
SANS_COND = FONT_DIR + "DejaVuSansCondensed.ttf"

PAGE = 1024
MARGIN = 40
MASTHEAD_H = 190
CONTENT_W = PAGE - 2 * MARGIN

PAPER = "#f1ece0"
CARD_FILL = "#fbf9f1"
CARD_EDGE = "#ddd6c4"
RULE = "#cbc4b1"
INK = "#1b1d22"
INK_SOFT = "#33363d"
MASTHEAD = "#16181d"
MASTHEAD_TEXT = "#fbf8ee"
MASTHEAD_DIM = "#cdc7b6"
MASTHEAD_LINE = "#4a4d54"

CARD_W = 460
CARD_H = 218
CARD_GAP = 22
CARD_TOP = 244
CARD_EDGE_W = 7
CARD_PAD = 16
ICON = 50


class Story(TypedDict):
    """One card of the front page."""

    tag: str
    title: tuple[str, str]
    fact: str
    icon: str
    color: str


STORIES: list[Story] = [
    {
        "tag": "UKRAINE / THE GUARDIAN",
        "title": ("Kyiv region strikes", "killed at least 14"),
        "fact": "At least 14 killed in strikes on Kyiv region",
        "icon": "building",
        "color": "#a8322c",
    },
    {
        "tag": "LIBYA / ARAB NEWS",
        "title": ("Russian corvette", "sunk off Libya"),
        "fact": "Seven naval drones sank corvette Merkury",
        "icon": "ship",
        "color": "#23507f",
    },
    {
        "tag": "VANUATU / USGS",
        "title": ("Magnitude 6.5", "under Vanuatu"),
        "fact": "Magnitude 6.5 at 598 km deep; alert green",
        "icon": "quake",
        "color": "#1b1d22",
    },
    {
        "tag": "ASIA / AL JAZEERA",
        "title": ("Asian markets", "open sharply lower"),
        "fact": "Kospi down 3.2%; Hang Seng 0.6% lower",
        "icon": "chart",
        "color": "#2f6b4f",
    },
    {
        "tag": "GAZA / THE GUARDIAN",
        "title": ("Gaza water and", "soil contaminated"),
        "fact": "61m tonnes of debris; water and soil toxic",
        "icon": "drop",
        "color": "#65662e",
    },
    {
        "tag": "PARIS / EURONEWS",
        "title": ("Champs-Élysées", "lights switched on"),
        "fact": "400 trees, two million LEDs, 200 exhibitors",
        "icon": "lights",
        "color": "#a8801f",
    },
]


@cache
def load_font(path: str, size: int) -> ImageFont.FreeTypeFont:
    """Load and cache a TrueType font at one pixel size."""
    return ImageFont.truetype(path, size)


def tracked_width(text: str, font: ImageFont.FreeTypeFont, tracking: float) -> float:
    """Width of ``text`` drawn with ``tracking`` extra pixels between glyphs."""
    if not text:
        return 0.0
    return sum(font.getlength(ch) for ch in text) + tracking * (len(text) - 1)


def fit_size(
    texts: list[str],
    path: str,
    max_width: float,
    max_size: int,
    min_size: int,
    tracking: float = 0.0,
) -> int:
    """Largest shared font size at which every string fits ``max_width``.

    Raises:
        ValueError: when even ``min_size`` cannot fit one of the strings.
    """
    for size in range(max_size, min_size - 1, -1):
        font = load_font(path, size)
        if all(tracked_width(t, font, tracking) <= max_width for t in texts):
            return size
    raise ValueError(f"no size at or above {min_size} fits: {texts!r}")


def draw_tracked(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: str,
    tracking: float,
) -> float:
    """Draw ``text`` with letter spacing, top-left anchored, and return its width."""
    x, y = xy
    start = x
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill, anchor="lt")
        x += font.getlength(ch) + tracking
    return x - tracking - start


def draw_globe(draw: ImageDraw.ImageDraw, cx: float, cy: float, r: float, colour: str) -> None:
    """Draw a flat wireframe globe centred on ``cx, cy``."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=colour, width=3)
    draw.line([cx, cy - r, cx, cy + r], fill=colour, width=2)
    for k in (0.45, 0.8):
        draw.ellipse([cx - r * k, cy - r, cx + r * k, cy + r], outline=colour, width=2)
    for dy in (-0.55 * r, 0.0, 0.55 * r):
        half = (r * r - dy * dy) ** 0.5
        draw.line([cx - half, cy + dy, cx + half, cy + dy], fill=colour, width=2)


def icon_building(draw: ImageDraw.ImageDraw, x: float, y: float, s: float, colour: str) -> None:
    """A damaged apartment block with a burst of debris."""
    left, right, base = x + 0.08 * s, x + 0.66 * s, y + 0.94 * s
    draw.line([left, y + 0.50 * s, left, base], fill=colour, width=3)
    draw.line([right, y + 0.42 * s, right, base], fill=colour, width=3)
    draw.line([left, base, right, base], fill=colour, width=3)
    draw.line(
        [
            left,
            y + 0.50 * s,
            x + 0.24 * s,
            y + 0.53 * s,
            x + 0.34 * s,
            y + 0.40 * s,
            x + 0.45 * s,
            y + 0.47 * s,
            x + 0.55 * s,
            y + 0.33 * s,
            right,
            y + 0.42 * s,
        ],
        fill=colour,
        width=3,
        joint="curve",
    )
    for row in (0.60, 0.76):
        for col in (0.18, 0.36, 0.54):
            draw.rectangle(
                [x + col * s, y + row * s, x + (col + 0.09) * s, y + (row + 0.09) * s],
                outline=colour,
                width=2,
            )
    bx, by = x + 0.76 * s, y + 0.28 * s
    for dx, dy in ((0.20, -0.16), (0.22, 0.06), (0.10, -0.26)):
        draw.line([bx, by, bx + dx * s, by + dy * s], fill=colour, width=3)
    draw.rectangle([x + 0.90 * s, y + 0.10 * s, x + 0.97 * s, y + 0.17 * s], fill=colour)


def icon_ship(draw: ImageDraw.ImageDraw, x: float, y: float, s: float, colour: str) -> None:
    """A listing warship with smoke and a small drone overhead."""
    draw.polygon(
        [
            (x + 0.06 * s, y + 0.62 * s),
            (x + 0.86 * s, y + 0.62 * s),
            (x + 0.74 * s, y + 0.80 * s),
            (x + 0.18 * s, y + 0.80 * s),
        ],
        outline=colour,
        width=3,
    )
    draw.rectangle([x + 0.40 * s, y + 0.48 * s, x + 0.58 * s, y + 0.62 * s], outline=colour, width=3)
    draw.line([x + 0.49 * s, y + 0.48 * s, x + 0.49 * s, y + 0.30 * s], fill=colour, width=3)
    draw.line([x + 0.30 * s, y + 0.30 * s, x + 0.60 * s, y + 0.30 * s], fill=colour, width=2)
    draw.line([x + 0.02 * s, y + 0.90 * s, x + 0.92 * s, y + 0.90 * s], fill=colour, width=2)
    for cx, cy, r in ((0.40, 0.22, 0.055), (0.31, 0.13, 0.045), (0.23, 0.07, 0.035)):
        draw.ellipse(
            [x + (cx - r) * s, y + (cy - r) * s, x + (cx + r) * s, y + (cy + r) * s],
            outline=colour,
            width=2,
        )
    draw.line([x + 0.68 * s, y + 0.16 * s, x + 0.92 * s, y + 0.16 * s], fill=colour, width=3)
    draw.line([x + 0.80 * s, y + 0.16 * s, x + 0.80 * s, y + 0.24 * s], fill=colour, width=2)


def icon_quake(draw: ImageDraw.ImageDraw, x: float, y: float, s: float, colour: str) -> None:
    """Concentric seismic rings over a small island."""
    cx, cy = x + 0.50 * s, y + 0.86 * s
    draw.chord([x + 0.30 * s, y + 0.78 * s, x + 0.70 * s, y + 0.98 * s], 200, 340, fill=colour)
    for r in (0.20, 0.34, 0.48):
        draw.arc(
            [cx - r * s, cy - r * s, cx + r * s, cy + r * s],
            205,
            335,
            fill=colour,
            width=3,
        )
    draw.line([x + 0.50 * s, y + 0.70 * s, x + 0.50 * s, y + 0.80 * s], fill=colour, width=3)


def icon_chart(draw: ImageDraw.ImageDraw, x: float, y: float, s: float, colour: str) -> None:
    """A falling line chart with an arrow head."""
    draw.line([x + 0.10 * s, y + 0.10 * s, x + 0.10 * s, y + 0.88 * s], fill=colour, width=3)
    draw.line([x + 0.10 * s, y + 0.88 * s, x + 0.92 * s, y + 0.88 * s], fill=colour, width=3)
    points = [
        (x + 0.18 * s, y + 0.26 * s),
        (x + 0.34 * s, y + 0.46 * s),
        (x + 0.48 * s, y + 0.36 * s),
        (x + 0.64 * s, y + 0.62 * s),
        (x + 0.86 * s, y + 0.76 * s),
    ]
    draw.line(points, fill=colour, width=3, joint="curve")
    draw.line([points[-1], (x + 0.72 * s, y + 0.76 * s)], fill=colour, width=3)
    draw.line([points[-1], (x + 0.86 * s, y + 0.62 * s)], fill=colour, width=3)


def icon_drop(draw: ImageDraw.ImageDraw, x: float, y: float, s: float, colour: str) -> None:
    """A cracked water drop over rubble."""
    draw.ellipse([x + 0.30 * s, y + 0.36 * s, x + 0.70 * s, y + 0.76 * s], outline=colour, width=3)
    draw.polygon(
        [(x + 0.50 * s, y + 0.08 * s), (x + 0.34 * s, y + 0.46 * s), (x + 0.66 * s, y + 0.46 * s)],
        outline=colour,
        width=3,
    )
    draw.line(
        [
            x + 0.62 * s,
            y + 0.20 * s,
            x + 0.46 * s,
            y + 0.44 * s,
            x + 0.58 * s,
            y + 0.54 * s,
            x + 0.42 * s,
            y + 0.72 * s,
        ],
        fill=colour,
        width=2,
    )
    for bx, bw, by in ((0.10, 0.16, 0.84), (0.34, 0.13, 0.90), (0.58, 0.18, 0.83), (0.80, 0.12, 0.91)):
        draw.rectangle(
            [x + bx * s, y + by * s, x + (bx + bw) * s, y + min(0.98, by + 0.10) * s],
            outline=colour,
            width=2,
        )


def icon_lights(draw: ImageDraw.ImageDraw, x: float, y: float, s: float, colour: str) -> None:
    """A string of festoon lights between two poles."""
    left, right = x + 0.10 * s, x + 0.90 * s
    top, bottom = y + 0.20 * s, y + 0.92 * s
    draw.line([left, top, left, bottom], fill=colour, width=3)
    draw.line([right, top, right, bottom], fill=colour, width=3)

    def sag(t: float) -> float:
        """Vertical offset of the wire at fraction ``t`` between the poles."""
        return top + 0.46 * s * 4 * t * (1 - t)

    points = [(left + (right - left) * step / 24, sag(step / 24)) for step in range(25)]
    draw.line(points, fill=colour, width=2)
    for step in (3, 8, 13, 18, 22):
        bx = left + (right - left) * step / 24
        by = sag(step / 24)
        draw.ellipse([bx - 0.05 * s, by + 0.01 * s, bx + 0.05 * s, by + 0.11 * s], fill=colour)


ICONS = {
    "building": icon_building,
    "ship": icon_ship,
    "quake": icon_quake,
    "chart": icon_chart,
    "drop": icon_drop,
    "lights": icon_lights,
}


def draw_masthead(draw: ImageDraw.ImageDraw) -> None:
    """Draw the dark band with the globe, the words and the day."""
    draw.rectangle([0, 0, PAGE - 1, MASTHEAD_H - 1], fill=MASTHEAD)
    draw_globe(draw, 92, 94, 42, MASTHEAD_TEXT)
    draw_tracked(draw, (166, 30), "WORLD / BRIEFING", load_font(SANS_BOLD, 22), MASTHEAD_DIM, 2.0)
    draw.rectangle([166, 64, 396, 66], fill="#a8322c")
    draw.text((166, 74), "MONDAY", font=load_font(SERIF_BOLD, 52), fill=MASTHEAD_TEXT, anchor="lt")
    draw.text(
        (166, 136), "23 NOVEMBER 2026", font=load_font(SERIF, 33), fill="#e6e1d2", anchor="lt"
    )
    draw.line([MARGIN, MASTHEAD_H + 2, PAGE - MARGIN, MASTHEAD_H + 2], fill=INK, width=2)


def draw_kicker(draw: ImageDraw.ImageDraw) -> None:
    """Draw the kicker line and the six palette marks."""
    draw_tracked(
        draw, (MARGIN, 206), "THE WORLD IN SIX STORIES", load_font(SANS_BOLD, 18), INK, 2.0
    )
    x = PAGE - MARGIN
    for story in reversed(STORIES):
        draw.rectangle([x - 14, 206, x, 220], fill=story["color"])
        x -= 22


def draw_card(
    draw: ImageDraw.ImageDraw,
    story: Story,
    x0: float,
    y0: float,
    tag_size: int,
    head_size: int,
    fact_size: int,
) -> None:
    """Draw one story card at ``x0, y0``."""
    accent = story["color"]
    draw.rectangle([x0, y0, x0 + CARD_W - 1, y0 + CARD_H - 1], fill=CARD_FILL, outline=CARD_EDGE, width=1)
    draw.rectangle([x0, y0, x0 + CARD_EDGE_W - 1, y0 + CARD_H - 1], fill=accent)

    left = x0 + CARD_EDGE_W + CARD_PAD
    right = x0 + CARD_W - CARD_PAD

    draw_tracked(draw, (left, y0 + 18), story["tag"], load_font(SANS_BOLD, tag_size), accent, 1.4)
    draw.line([left, y0 + 49, right, y0 + 49], fill=RULE, width=1)

    head_font = load_font(SERIF_BOLD, head_size)
    line_gap = round(head_size * 1.14)
    icon_x = right - ICON
    ICONS[story["icon"]](draw, icon_x, y0 + 58, ICON, accent)
    for index, line in enumerate(story["title"]):
        draw.text(
            (left, y0 + 58 + index * line_gap),
            line,
            font=head_font,
            fill=INK,
            anchor="lt",
        )

    draw.line([left, y0 + 152, right, y0 + 152], fill=RULE, width=1)
    draw.text(
        (left, y0 + 163),
        story["fact"],
        font=load_font(SANS_COND, fact_size),
        fill=INK_SOFT,
        anchor="lt",
    )


def draw_footer(draw: ImageDraw.ImageDraw) -> None:
    """Draw the footer rule, the day line and the closing rule."""
    draw.line([MARGIN, 952, PAGE - MARGIN, 952], fill=RULE, width=1)
    draw_tracked(
        draw, (MARGIN, 962), "MONDAY 23 NOVEMBER 2026", load_font(SANS_BOLD, 18), INK, 2.0
    )
    label = "SIX STORIES"
    font = load_font(SANS_BOLD, 18)
    width = tracked_width(label, font, 2.0)
    draw_tracked(draw, (PAGE - MARGIN - width, 962), label, font, INK_SOFT, 2.0)
    draw.line([MARGIN, 998, PAGE - MARGIN, 998], fill=INK, width=3)


def build(path: str) -> tuple[int, int, int]:
    """Draw the whole page into ``path`` and return the three shared font sizes."""
    image = Image.new("RGB", (PAGE, PAGE), PAPER)
    draw = ImageDraw.Draw(image)

    tags = [s["tag"] for s in STORIES]
    facts = [s["fact"] for s in STORIES]
    heads = [line for s in STORIES for line in s["title"]]

    content_w = CARD_W - CARD_EDGE_W - 2 * CARD_PAD
    tag_size = fit_size(tags, SANS_BOLD, content_w, 20, 16, tracking=1.4)
    head_size = fit_size(heads, SERIF_BOLD, content_w - ICON - 14, 38, 26)
    fact_size = fit_size(facts, SANS_COND, content_w, 21, 18)

    draw_masthead(draw)
    draw_kicker(draw)

    for index, story in enumerate(STORIES):
        column = index % 2
        row = index // 2
        x0 = MARGIN + column * (CARD_W + CARD_GAP)
        y0 = CARD_TOP + row * (CARD_H + CARD_GAP)
        draw_card(draw, story, x0, y0, tag_size, head_size, fact_size)

    draw_footer(draw)
    image.save(path, format="PNG")
    return tag_size, head_size, fact_size


def main() -> None:
    """Write ``entry.png`` beside this file."""
    import os

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    tag_size, head_size, fact_size = build(path)
    print(f"wrote {path} (tag {tag_size}px, headline {head_size}px, fact {fact_size}px)")


if __name__ == "__main__":
    main()
