"""Generate an 800 problem honors geometry database from the local curriculum PDF scope.

The source PDF is a curriculum outline, not a problem bank. This generator uses
the units, guiding questions, and standards from that outline to create a
deterministic, aligned practice database with explanations, proof solutions, and
PNG image assets.
"""

from __future__ import annotations

import html
import json
import math
import shutil
import xml.etree.ElementTree as ET
from datetime import date
from fractions import Fraction
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
IMAGE_DIR = DATA_DIR / "images"
LEGACY_VISUAL_DIR = DATA_DIR / "visuals"
OUTPUT = DATA_DIR / "honors_geometry_problem_database.json"
JS_OUTPUT = DATA_DIR / "honors_geometry_problem_database.js"


UNITS = {
    1: {
        "title": "Foundations of Geometry",
        "essential_question": "How do we communicate geometric concepts?",
        "standards": ["G.CO.7", "G.CO.11", "G.GPE.6", "G.GPE.7"],
        "source_alignment": (
            "Lines, rays, segments, angle relationships, constructions, "
            "midpoint, distance, slope, and parallel/perpendicular lines."
        ),
    },
    2: {
        "title": "Transformations",
        "essential_question": "How do transformations affect two-dimensional figures?",
        "standards": ["G.CO.1", "G.CO.2", "G.CO.3", "G.CO.5", "G.CO.7"],
        "source_alignment": (
            "Translations, rotations, reflections, symmetry, rigid-motion "
            "congruence, and angle relationships in parallel lines."
        ),
    },
    3: {
        "title": "Triangles - Properties and Congruence",
        "essential_question": "How do transformations reveal properties within and between triangles?",
        "standards": ["G.CO.4", "G.CO.6", "G.CO.8", "G.CO.9", "G.SRT.6", "G.GPE.6"],
        "source_alignment": (
            "Triangle angle relationships, coordinate classification, "
            "midsegments, medians, and SSS/SAS/ASA/AAS/HL congruence proofs."
        ),
    },
    4: {
        "title": "Properties of Polygons and Quadrilaterals",
        "essential_question": "How does congruence reveal properties within geometric figures?",
        "standards": ["G.CO.4", "G.CO.10", "G.SRT.6", "G.GPE.6", "G.GPE.8"],
        "source_alignment": (
            "Quadrilateral classification, parallelogram theorems, congruent "
            "triangles in polygons, coordinate perimeter, and area."
        ),
    },
    5: {
        "title": "Similarity",
        "essential_question": "How do dilations affect two-dimensional figures?",
        "standards": ["G.SRT.1", "G.SRT.2", "G.SRT.3", "G.SRT.4", "G.SRT.5", "G.SRT.6"],
        "source_alignment": (
            "Dilations, similarity transformations, proportionality, similar "
            "triangle criteria, and similarity-based proof."
        ),
    },
    6: {
        "title": "Right Triangles and Trigonometry",
        "essential_question": "What relationships exist within right triangles?",
        "standards": ["G.SRT.6", "G.SRT.7", "G.SRT.8", "G.SRT.9", "G.SRT.10", "G.SRT.11", "G.SRT.12"],
        "source_alignment": (
            "Pythagorean Theorem, trigonometric ratios, exact ratios, area "
            "using sine, Law of Sines, Law of Cosines, and applications."
        ),
    },
    7: {
        "title": "Area, Surface Area, Volume",
        "essential_question": "How are geometric shapes and their properties modeled?",
        "standards": ["G.C.6", "G.GPE.8", "G.GMD.1", "G.GMD.2", "G.MG.1", "G.MG.2", "G.MG.3"],
        "source_alignment": (
            "Coordinate area, composite area, regular polygons, sectors, "
            "surface area, volume, Cavalieri's Principle, density, displacement, and design."
        ),
    },
    8: {
        "title": "Circles",
        "essential_question": "What characteristics and relationships exist within circles?",
        "standards": ["G.C.1", "G.C.2", "G.C.3", "G.C.4", "G.C.5", "G.GPE.1", "G.GPE.2", "G.GPE.6", "G.CO.12"],
        "source_alignment": (
            "Circle similarity, chords, radii, tangents, inscribed and "
            "circumscribed polygons, circle equations, and constructions."
        ),
    },
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def fmt_float(value: float, digits: int = 2) -> str:
    rounded = round(value, digits)
    if abs(rounded - round(rounded)) < 10 ** (-digits):
        return str(int(round(rounded)))
    return f"{rounded:.{digits}f}".rstrip("0").rstrip(".")


def fmt_frac(value: Fraction | int | float) -> str:
    if not isinstance(value, Fraction):
        value = Fraction(value).limit_denominator()
    if value.denominator == 1:
        return str(value.numerator)
    if value.numerator < 0:
        return f"-{abs(value.numerator)}/{value.denominator}"
    return f"{value.numerator}/{value.denominator}"


def fmt_signed(value: Fraction | int | float) -> str:
    if not isinstance(value, Fraction):
        value = Fraction(value).limit_denominator()
    if value == 0:
        return ""
    sign = "+" if value > 0 else "-"
    return f" {sign} {fmt_frac(abs(value))}"


def add_expr(left: int | Fraction, right: int | Fraction) -> str:
    right = Fraction(right).limit_denominator()
    if right < 0:
        return f"{fmt_frac(left)} - {fmt_frac(abs(right))}"
    return f"{fmt_frac(left)} + {fmt_frac(right)}"


def sub_expr(left: int | Fraction, right: int | Fraction) -> str:
    right = Fraction(right).limit_denominator()
    if right < 0:
        return f"{fmt_frac(left)} + {fmt_frac(abs(right))}"
    return f"{fmt_frac(left)} - {fmt_frac(right)}"


def shifted_var(var: str, shift: int | Fraction) -> str:
    shift = Fraction(shift).limit_denominator()
    if shift == 0:
        return var
    if shift > 0:
        return f"{var} + {fmt_frac(shift)}"
    return f"{var} - {fmt_frac(abs(shift))}"


def circle_term(var: str, center: int | Fraction) -> str:
    center = Fraction(center).limit_denominator()
    if center == 0:
        return f"{var}^2"
    if center > 0:
        return f"({var} - {fmt_frac(center)})^2"
    return f"({var} + {fmt_frac(abs(center))})^2"


def circle_equation(h: int | Fraction, k: int | Fraction, r_squared: int | Fraction) -> str:
    return f"{circle_term('x', h)} + {circle_term('y', k)} = {fmt_frac(r_squared)}"


def line_equation(m: Fraction, b: Fraction) -> str:
    if m == 0:
        return f"y = {fmt_frac(b)}"
    if m == 1:
        m_part = "x"
    elif m == -1:
        m_part = "-x"
    else:
        m_part = f"{fmt_frac(m)}x"
    return f"y = {m_part}{fmt_signed(b)}"


def distance(p: tuple[int, int], q: tuple[int, int]) -> float:
    return math.hypot(q[0] - p[0], q[1] - p[1])


def difficulty_for(index: int) -> str:
    if index <= 25:
        return "easy"
    if index <= 55:
        return "moderate"
    if index <= 80:
        return "challenging"
    return "honors"


def svg_base(title: str, body: str, width: int = 360, height: int = 260) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">\n'
        f'  <title id="title">{esc(title)}</title>\n'
        f'  <desc id="desc">{esc(title)}</desc>\n'
        '  <rect width="100%" height="100%" fill="#ffffff"/>\n'
        f"{body}\n"
        "</svg>\n"
    )


def svg_text(x: float, y: float, label: str, size: int = 12, anchor: str = "middle", fill: str = "#111827") -> str:
    return (
        f'<text x="{fmt_float(x)}" y="{fmt_float(y)}" font-family="Arial, sans-serif" '
        f'font-size="{size}" text-anchor="{anchor}" fill="{fill}">{esc(label)}</text>'
    )


def svg_line(x1: float, y1: float, x2: float, y2: float, stroke: str = "#1f2937", width: float = 2, dash: str = "") -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{fmt_float(x1)}" y1="{fmt_float(y1)}" x2="{fmt_float(x2)}" y2="{fmt_float(y2)}" '
        f'stroke="{stroke}" stroke-width="{fmt_float(width)}"{dash_attr} stroke-linecap="round"/>'
    )


def svg_circle(cx: float, cy: float, r: float, stroke: str = "#2563eb", fill: str = "none", width: float = 2) -> str:
    return (
        f'<circle cx="{fmt_float(cx)}" cy="{fmt_float(cy)}" r="{fmt_float(r)}" '
        f'stroke="{stroke}" stroke-width="{fmt_float(width)}" fill="{fill}"/>'
    )


def svg_polygon(points: list[tuple[float, float]], stroke: str = "#2563eb", fill: str = "#dbeafe", width: float = 2) -> str:
    pts = " ".join(f"{fmt_float(x)},{fmt_float(y)}" for x, y in points)
    return f'<polygon points="{pts}" stroke="{stroke}" stroke-width="{fmt_float(width)}" fill="{fill}"/>'


def coord_to_px(point: tuple[float, float], width: int = 360, height: int = 280, scale: int = 18) -> tuple[float, float]:
    x, y = point
    return width / 2 + x * scale, height / 2 - y * scale


def coordinate_svg(
    title: str,
    points: dict[str, tuple[float, float]],
    segments: list[tuple[str, str]] | None = None,
    polygons: list[list[str]] | None = None,
    circles: list[tuple[str, float]] | None = None,
    extra_labels: list[tuple[float, float, str]] | None = None,
    width: int = 360,
    height: int = 280,
    scale: int = 18,
) -> str:
    segments = segments or []
    polygons = polygons or []
    circles = circles or []
    extra_labels = extra_labels or []
    elements: list[str] = []
    for gx in range(-9, 10):
        x, _ = coord_to_px((gx, 0), width, height, scale)
        elements.append(svg_line(x, 0, x, height, "#e5e7eb", 1))
    for gy in range(-7, 8):
        _, y = coord_to_px((0, gy), width, height, scale)
        elements.append(svg_line(0, y, width, y, "#e5e7eb", 1))
    ox, oy = coord_to_px((0, 0), width, height, scale)
    elements.append(svg_line(0, oy, width, oy, "#6b7280", 1.5))
    elements.append(svg_line(ox, 0, ox, height, "#6b7280", 1.5))
    for center_label, radius in circles:
        cx, cy = coord_to_px(points[center_label], width, height, scale)
        elements.append(svg_circle(cx, cy, radius * scale, "#7c3aed", "none", 2.2))
    for poly in polygons:
        px_points = [coord_to_px(points[label], width, height, scale) for label in poly]
        elements.append(svg_polygon(px_points, "#2563eb", "#dbeafe", 2))
    for start, end in segments:
        x1, y1 = coord_to_px(points[start], width, height, scale)
        x2, y2 = coord_to_px(points[end], width, height, scale)
        elements.append(svg_line(x1, y1, x2, y2, "#1d4ed8", 2.2))
    for label, point in points.items():
        x, y = coord_to_px(point, width, height, scale)
        elements.append(svg_circle(x, y, 4, "#111827", "#111827", 1))
        elements.append(svg_text(x + 12, y - 8, f"{label}({fmt_float(point[0])}, {fmt_float(point[1])})", 11, "start"))
    for x, y, label in extra_labels:
        px, py = coord_to_px((x, y), width, height, scale)
        elements.append(svg_text(px, py, label, 11))
    return svg_base(title, "\n  ".join(elements), width, height)


def angle_svg(title: str, labels: list[str]) -> str:
    elements = [
        svg_line(40, 190, 320, 70, "#1d4ed8", 2.5),
        svg_line(40, 70, 320, 190, "#1d4ed8", 2.5),
        svg_line(35, 130, 325, 130, "#0f766e", 2.5),
        svg_circle(180, 130, 5, "#111827", "#111827", 1),
    ]
    positions = [(180, 58), (276, 118), (180, 218), (84, 118)]
    for (x, y), label in zip(positions, labels):
        elements.append(svg_text(x, y, label, 13))
    return svg_base(title, "\n  ".join(elements), 360, 260)


def triangle_svg(title: str, labels: list[tuple[float, float, str]], right: bool = False) -> str:
    a, b, c = (70, 205), (290, 205), (160, 55)
    elements = [
        svg_polygon([a, b, c], "#2563eb", "#dbeafe", 2.2),
        svg_text(a[0] - 12, a[1] + 18, "A", 13),
        svg_text(b[0] + 12, b[1] + 18, "B", 13),
        svg_text(c[0], c[1] - 10, "C", 13),
    ]
    if right:
        elements.extend([
            svg_line(85, 205, 85, 190, "#111827", 1.6),
            svg_line(85, 190, 100, 190, "#111827", 1.6),
            svg_line(100, 190, 100, 205, "#111827", 1.6),
        ])
    for x, y, label in labels:
        elements.append(svg_text(x, y, label, 12))
    return svg_base(title, "\n  ".join(elements), 360, 260)


def quadrilateral_svg(title: str, labels: list[tuple[float, float, str]], kind: str = "parallelogram") -> str:
    if kind == "rectangle":
        pts = [(75, 70), (285, 70), (285, 200), (75, 200)]
    elif kind == "trapezoid":
        pts = [(90, 80), (255, 80), (305, 205), (55, 205)]
    elif kind == "kite":
        pts = [(180, 45), (285, 135), (180, 220), (75, 135)]
    else:
        pts = [(80, 80), (285, 80), (240, 205), (35, 205)]
    elements = [
        svg_polygon(pts, "#2563eb", "#dbeafe", 2.2),
        svg_text(pts[0][0] - 12, pts[0][1] - 10, "A", 13),
        svg_text(pts[1][0] + 12, pts[1][1] - 10, "B", 13),
        svg_text(pts[2][0] + 12, pts[2][1] + 18, "C", 13),
        svg_text(pts[3][0] - 12, pts[3][1] + 18, "D", 13),
        svg_line(pts[0][0], pts[0][1], pts[2][0], pts[2][1], "#7c3aed", 1.8, "5 5"),
        svg_line(pts[1][0], pts[1][1], pts[3][0], pts[3][1], "#7c3aed", 1.8, "5 5"),
    ]
    for x, y, label in labels:
        elements.append(svg_text(x, y, label, 12))
    return svg_base(title, "\n  ".join(elements), 360, 260)


def circle_diagram_svg(title: str, labels: list[tuple[float, float, str]], chord: bool = True, tangent: bool = False) -> str:
    elements = [
        svg_circle(180, 130, 82, "#2563eb", "#eff6ff", 2.2),
        svg_circle(180, 130, 4, "#111827", "#111827", 1),
        svg_text(180, 125, "O", 12),
    ]
    if chord:
        elements.extend([
            svg_line(115, 80, 245, 180, "#1d4ed8", 2.2),
            svg_line(115, 180, 245, 80, "#1d4ed8", 2.2),
            svg_line(180, 130, 245, 80, "#0f766e", 1.8),
        ])
    if tangent:
        elements.extend([
            svg_line(240, 45, 330, 150, "#be123c", 2.2),
            svg_line(180, 130, 246, 80, "#111827", 1.8),
            svg_text(313, 145, "tangent", 11),
        ])
    for x, y, label in labels:
        elements.append(svg_text(x, y, label, 12))
    return svg_base(title, "\n  ".join(elements), 360, 260)


def solid_svg(title: str, labels: list[tuple[float, float, str]], kind: str) -> str:
    elements: list[str] = []
    if kind == "cylinder":
        elements.extend([
            '<ellipse cx="180" cy="75" rx="70" ry="24" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>',
            svg_line(110, 75, 110, 190, "#2563eb", 2),
            svg_line(250, 75, 250, 190, "#2563eb", 2),
            '<ellipse cx="180" cy="190" rx="70" ry="24" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>',
        ])
    elif kind == "cone":
        elements.extend([
            svg_line(180, 45, 95, 195, "#2563eb", 2),
            svg_line(180, 45, 265, 195, "#2563eb", 2),
            '<ellipse cx="180" cy="195" rx="85" ry="25" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>',
        ])
    elif kind == "pyramid":
        elements.extend([
            svg_polygon([(100, 190), (250, 190), (280, 125), (130, 125)], "#2563eb", "#eff6ff", 2),
            svg_line(180, 45, 100, 190, "#2563eb", 2),
            svg_line(180, 45, 250, 190, "#2563eb", 2),
            svg_line(180, 45, 280, 125, "#2563eb", 2),
            svg_line(180, 45, 130, 125, "#2563eb", 2),
        ])
    else:
        elements.extend([
            svg_polygon([(75, 195), (160, 80), (285, 195)], "#2563eb", "#dbeafe", 2),
            svg_line(75, 195, 285, 195, "#2563eb", 2),
        ])
    for x, y, label in labels:
        elements.append(svg_text(x, y, label, 12))
    return svg_base(title, "\n  ".join(elements), 360, 260)


def _svg_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _svg_float(value: str | None, default: float = 0) -> float:
    if value is None:
        return default
    return float(value.replace("px", "").replace("%", ""))


def _svg_color(value: str | None, default: str | None = None) -> str | None:
    if value is None:
        return default
    if value == "none":
        return None
    return value


def _font(size: int) -> ImageFont.ImageFont:
    font_path = Path("C:/Windows/Fonts/arial.ttf")
    if font_path.exists():
        return ImageFont.truetype(str(font_path), size)
    return ImageFont.load_default()


def _points(value: str) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    for item in value.split():
        x, y = item.split(",", 1)
        points.append((float(x), float(y)))
    return points


def _draw_dashed_line(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    fill: str,
    width: int,
    dash: str,
    scale: int,
) -> None:
    dash_values = [max(1, float(part) * scale) for part in dash.split()]
    if len(dash_values) == 1:
        dash_values.append(dash_values[0])
    on, off = dash_values[:2]
    x1, y1 = start
    x2, y2 = end
    total = math.hypot(x2 - x1, y2 - y1)
    if total == 0:
        return
    dx = (x2 - x1) / total
    dy = (y2 - y1) / total
    distance_so_far = 0.0
    while distance_so_far < total:
        segment_end = min(total, distance_so_far + on)
        draw.line(
            [
                (x1 + dx * distance_so_far, y1 + dy * distance_so_far),
                (x1 + dx * segment_end, y1 + dy * segment_end),
            ],
            fill=fill,
            width=width,
        )
        distance_so_far = segment_end + off


def render_diagram_png(svg_markup: str, output_path: Path) -> None:
    """Render the generated diagram markup into a PNG bitmap using Pillow."""

    tree = ET.fromstring(svg_markup)
    width = int(_svg_float(tree.attrib.get("width"), 360))
    height = int(_svg_float(tree.attrib.get("height"), 260))
    scale = 4
    image = Image.new("RGB", (width * scale, height * scale), "#ffffff")
    draw = ImageDraw.Draw(image)

    def sx(value: float) -> float:
        return value * scale

    for element in tree.iter():
        name = _svg_name(element.tag)
        if name in {"svg", "title", "desc"}:
            continue

        if name == "rect":
            x = sx(_svg_float(element.attrib.get("x"), 0))
            y = sx(_svg_float(element.attrib.get("y"), 0))
            raw_w = element.attrib.get("width", str(width))
            raw_h = element.attrib.get("height", str(height))
            w = width * scale if raw_w == "100%" else sx(_svg_float(raw_w, width))
            h = height * scale if raw_h == "100%" else sx(_svg_float(raw_h, height))
            fill = _svg_color(element.attrib.get("fill"), "#ffffff")
            outline = _svg_color(element.attrib.get("stroke"))
            stroke_width = max(1, round(_svg_float(element.attrib.get("stroke-width"), 1) * scale))
            draw.rectangle([x, y, x + w, y + h], fill=fill, outline=outline, width=stroke_width)

        elif name == "line":
            x1 = sx(_svg_float(element.attrib.get("x1")))
            y1 = sx(_svg_float(element.attrib.get("y1")))
            x2 = sx(_svg_float(element.attrib.get("x2")))
            y2 = sx(_svg_float(element.attrib.get("y2")))
            fill = _svg_color(element.attrib.get("stroke"), "#111827") or "#111827"
            stroke_width = max(1, round(_svg_float(element.attrib.get("stroke-width"), 1) * scale))
            dash = element.attrib.get("stroke-dasharray")
            if dash:
                _draw_dashed_line(draw, (x1, y1), (x2, y2), fill, stroke_width, dash, scale)
            else:
                draw.line([(x1, y1), (x2, y2)], fill=fill, width=stroke_width)

        elif name == "circle":
            cx = sx(_svg_float(element.attrib.get("cx")))
            cy = sx(_svg_float(element.attrib.get("cy")))
            r = sx(_svg_float(element.attrib.get("r")))
            fill = _svg_color(element.attrib.get("fill"))
            outline = _svg_color(element.attrib.get("stroke"), "#111827")
            stroke_width = max(1, round(_svg_float(element.attrib.get("stroke-width"), 1) * scale))
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill, outline=outline, width=stroke_width)

        elif name == "ellipse":
            cx = sx(_svg_float(element.attrib.get("cx")))
            cy = sx(_svg_float(element.attrib.get("cy")))
            rx = sx(_svg_float(element.attrib.get("rx")))
            ry = sx(_svg_float(element.attrib.get("ry")))
            fill = _svg_color(element.attrib.get("fill"))
            outline = _svg_color(element.attrib.get("stroke"), "#111827")
            stroke_width = max(1, round(_svg_float(element.attrib.get("stroke-width"), 1) * scale))
            draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=fill, outline=outline, width=stroke_width)

        elif name == "polygon":
            points = [(sx(x), sx(y)) for x, y in _points(element.attrib.get("points", ""))]
            fill = _svg_color(element.attrib.get("fill"))
            outline = _svg_color(element.attrib.get("stroke"), "#111827")
            stroke_width = max(1, round(_svg_float(element.attrib.get("stroke-width"), 1) * scale))
            if points:
                draw.polygon(points, fill=fill)
                if outline:
                    draw.line(points + [points[0]], fill=outline, width=stroke_width)

        elif name == "text":
            text = element.text or ""
            x = sx(_svg_float(element.attrib.get("x")))
            y = sx(_svg_float(element.attrib.get("y")))
            size = max(8, round(_svg_float(element.attrib.get("font-size"), 12) * scale))
            fill = _svg_color(element.attrib.get("fill"), "#111827") or "#111827"
            anchor = element.attrib.get("text-anchor", "middle")
            font = _font(size)
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            if anchor == "middle":
                x -= text_width / 2
            elif anchor == "end":
                x -= text_width
            draw.text((x, y - text_height), text, fill=fill, font=font)

    image = image.resize((width, height), Image.Resampling.LANCZOS)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path, "PNG", optimize=True)


def make_problem(
    pid: str,
    unit: int,
    number: int,
    standard: str,
    topic: str,
    problem_type: str,
    difficulty: str,
    question: str,
    answer: str,
    explanation: str,
    svg: str,
    alt_text: str,
    proof_required: bool = False,
    proof: str | None = None,
    tags: list[str] | None = None,
) -> dict:
    if proof_required and not proof:
        raise ValueError(f"{pid} is marked proof_required without proof")
    return {
        "id": pid,
        "unit": unit,
        "unit_title": UNITS[unit]["title"],
        "unit_problem_number": number,
        "standard": standard,
        "topic": topic,
        "difficulty": difficulty,
        "problem_type": problem_type,
        "question": question,
        "answer": answer,
        "explanation": explanation,
        "proof_required": proof_required,
        "proof": proof,
        "visual_required": True,
        "visual_alt_text": alt_text,
        "tags": tags or [],
        "source_alignment": UNITS[unit]["source_alignment"],
        "_svg": svg,
    }


def foundations(pid: str, number: int, variant: int, template: int, difficulty: str) -> dict:
    if template == 1:
        x = variant + 5
        angle = 7 * x + 18
        q = (
            f"In the diagram, angles 1 and 3 are vertical angles. If m angle 1 = 7x + 18 "
            f"and m angle 3 = {angle}, find x and the measure of each angle."
        )
        ans = f"x = {x}; each vertical angle measures {angle} degrees."
        exp = (
            "Vertical angles are formed by two intersecting lines and are congruent. "
            f"Set 7x + 18 equal to {angle}, then subtract 18 to get 7x = {angle - 18}. "
            f"Dividing by 7 gives x = {x}. Substituting back gives 7({x}) + 18 = {angle}, "
            "so both vertical angles have that measure."
        )
        svg = angle_svg("Vertical angles", [f"1: 7x+18", "2", f"3: {angle}", "4"])
        return make_problem(pid, 1, number, "G.CO.7", "Vertical angles", "computation", difficulty, q, ans, exp, svg, "Intersecting lines with vertical angles labeled.")
    if template == 2:
        x = variant + 8
        a = 4 * x + 10
        b = 180 - a
        q = (
            f"Angles A and B form a linear pair. If m angle A = 4x + 10 and "
            f"m angle B = {b}, find x, m angle A, and m angle B."
        )
        ans = f"x = {x}; m angle A = {a} degrees and m angle B = {b} degrees."
        exp = (
            "A linear pair is supplementary, so the measures add to 180 degrees. "
            f"Solve (4x + 10) + {b} = 180. After combining constants, 4x + {b + 10} = 180, "
            f"so 4x = {4 * x} and x = {x}. The angle A measure is 4({x}) + 10 = {a} degrees, "
            f"which checks because {a} + {b} = 180."
        )
        svg = angle_svg("Linear pair", [f"A: 4x+10", f"B: {b}", "", "straight line"])
        return make_problem(pid, 1, number, "G.CO.7", "Linear pairs", "computation", difficulty, q, ans, exp, svg, "A straight line split into two adjacent supplementary angles.")
    if template == 3:
        a = (-6 + variant, 2 + (variant % 3))
        b = (4 + variant, -4 + (variant % 4))
        mid = (Fraction(a[0] + b[0], 2), Fraction(a[1] + b[1], 2))
        dist = distance(a, b)
        q = f"Segment AB has endpoints A{a} and B{b}. Find the midpoint and the length of AB."
        ans = f"Midpoint = ({fmt_frac(mid[0])}, {fmt_frac(mid[1])}); AB = {fmt_float(dist)} units."
        exp = (
            "Average the x-coordinates and y-coordinates separately to find the midpoint. "
            f"The x-coordinate is ({add_expr(a[0], b[0])})/2 = {fmt_frac(mid[0])}, and the y-coordinate is "
            f"({add_expr(a[1], b[1])})/2 = {fmt_frac(mid[1])}. For length, use the distance formula: "
            f"sqrt(({sub_expr(b[0], a[0])})^2 + ({sub_expr(b[1], a[1])})^2) = {fmt_float(dist)}. "
            "The midpoint describes the location halfway along the segment, while the distance formula gives the actual segment length."
        )
        svg = coordinate_svg("Midpoint and distance", {"A": a, "B": b}, segments=[("A", "B")])
        return make_problem(pid, 1, number, "G.GPE.6", "Midpoint and distance", "computation", difficulty, q, ans, exp, svg, "Coordinate plane with segment AB.")
    if template == 4:
        m1 = Fraction(variant + 1, 2)
        relation = "parallel" if variant % 2 else "perpendicular"
        m2 = m1 if relation == "parallel" else Fraction(-1, 1) / m1
        q = f"Line l has slope {fmt_frac(m1)} and line m has slope {fmt_frac(m2)}. Are the lines parallel, perpendicular, or neither? Justify."
        ans = f"The lines are {relation}."
        if relation == "parallel":
            exp = (
                "Nonvertical lines are parallel when their slopes are equal and they are distinct lines. "
                f"Here both slopes are {fmt_frac(m1)}, so they have the same steepness and direction. "
                "That slope comparison is enough to identify the lines as parallel in the coordinate plane."
            )
        else:
            exp = (
                "Nonvertical lines are perpendicular when their slopes are negative reciprocals. "
                f"The negative reciprocal of {fmt_frac(m1)} is {fmt_frac(m2)} because their product is -1. "
                "Therefore the lines meet at a right angle, so they are perpendicular."
            )
        svg = coordinate_svg("Slope criteria", {"P": (-5, -2), "Q": (-1, int(m1 * 4 - 2)), "R": (1, 4), "S": (5, int(4 + m2 * 4))}, segments=[("P", "Q"), ("R", "S")])
        return make_problem(pid, 1, number, "G.GPE.7", "Parallel and perpendicular slopes", "conceptual", difficulty, q, ans, exp, svg, "Coordinate plane showing two line segments for slope comparison.")
    if template == 5:
        m = Fraction(variant + 2, 3)
        p = (variant - 4, 2 - variant)
        b_parallel = Fraction(p[1]) - m * p[0]
        mp = Fraction(-1, 1) / m
        b_perp = Fraction(p[1]) - mp * p[0]
        q = (
            f"Line n has equation {line_equation(m, Fraction(1))}. Write equations for the line through "
            f"P{p} parallel to n and the line through P perpendicular to n."
        )
        ans = f"Parallel: {line_equation(m, b_parallel)}. Perpendicular: {line_equation(mp, b_perp)}."
        exp = (
            f"The given line has slope {fmt_frac(m)}. A parallel line keeps that same slope, so using "
            f"P{p} in y = mx + b gives b = {p[1]} - ({fmt_frac(m)})({p[0]}) = {fmt_frac(b_parallel)}. "
            f"A perpendicular line uses the negative reciprocal slope {fmt_frac(mp)}. Substituting the same point gives "
            f"b = {p[1]} - ({fmt_frac(mp)})({p[0]}) = {fmt_frac(b_perp)}. Those two slope choices create the requested relationships."
        )
        svg = coordinate_svg("Parallel and perpendicular lines through a point", {"P": p, "A": (-6, int(m * -6 + 1)), "B": (4, int(m * 4 + 1))}, segments=[("A", "B")])
        return make_problem(pid, 1, number, "G.GPE.7", "Line equations", "computation", difficulty, q, ans, exp, svg, "Coordinate plane with point P and a reference line.")
    if template == 6:
        length = 5 + variant
        q = (
            f"Construct a copy of segment AB with length {length} cm starting at point C. "
            "Describe the construction steps and explain why the copied segment is congruent to AB."
        )
        ans = "Set the compass to AB, place the compass point at C, mark point D, and segment CD is congruent to AB."
        exp = (
            "A compass preserves a fixed radius as it is moved. First draw a ray starting at C so there is a direction for the new segment. "
            "Open the compass to the distance from A to B without changing that width. Place the compass point on C and mark the ray at D. "
            f"Because the compass width stayed {length} cm, CD has the same length as AB."
        )
        proof = (
            "The compass opening is equal to AB by construction. When the compass point is moved to C without changing the opening, every point on the arc is exactly AB units from C. "
            "Point D is chosen on that arc and on the ray from C, so CD = AB. Segments with equal lengths are congruent; therefore CD is congruent to AB."
        )
        svg = coordinate_svg("Copying a segment", {"A": (-5, 1), "B": (0, 1), "C": (-4, -3), "D": (1, -3)}, segments=[("A", "B"), ("C", "D")])
        return make_problem(pid, 1, number, "G.CO.11", "Segment construction", "construction", difficulty, q, ans, exp, svg, "Original segment AB and copied segment CD.", True, proof)
    if template == 7:
        a = (-variant, 0)
        b = (variant, 0)
        p = (0, variant + 2)
        q = (
            f"Point P{p} lies on the perpendicular bisector of segment AB with A{a} and B{b}. "
            "Prove that P is equidistant from A and B."
        )
        d = distance(p, a)
        ans = f"PA = PB = {fmt_float(d)} units."
        exp = (
            "A perpendicular bisector passes through the midpoint of a segment at a right angle. "
            "Any point on that line is the same distance from the two endpoints. Using the distance formula confirms the theorem here: "
            f"PA = sqrt(({sub_expr(p[0], a[0])})^2 + ({sub_expr(p[1], a[1])})^2) and PB = sqrt(({sub_expr(p[0], b[0])})^2 + ({sub_expr(p[1], b[1])})^2). "
            f"Both simplify to {fmt_float(d)}, so P is equidistant from A and B."
        )
        proof = (
            "Let M be the midpoint of AB. Since P lies on the perpendicular bisector, AM = MB and angle PMA and angle PMB are right angles. "
            "Segment PM is shared by triangles PMA and PMB. By SAS, triangle PMA is congruent to triangle PMB. Corresponding sides PA and PB are congruent, so P is equidistant from A and B."
        )
        svg = coordinate_svg("Perpendicular bisector", {"A": a, "B": b, "P": p, "M": (0, 0)}, segments=[("A", "B"), ("P", "M")])
        return make_problem(pid, 1, number, "G.CO.7", "Perpendicular bisectors", "proof", difficulty, q, ans, exp, svg, "Point on perpendicular bisector of segment AB.", True, proof)
    if template == 8:
        q = (
            "Use the diagram to name one line, one ray, and one segment using correct geometric notation in words. "
            "Then explain why the segment can have a midpoint but the line cannot."
        )
        ans = "Line AB, ray AC, and segment AB are valid examples; segment AB can have a midpoint, but line AB cannot."
        exp = (
            "A line extends forever in two directions, a ray has one endpoint and extends forever in one direction, and a segment has two endpoints. "
            "Only a segment has a finite length between two fixed endpoints, so a midpoint can be the point halfway between them. "
            "A line has no endpoints and no finite total length, so there is no single halfway point for the entire line."
        )
        svg = coordinate_svg("Line, ray, and segment notation", {"A": (-4, 0), "B": (1, 0), "C": (4, 3)}, segments=[("A", "B"), ("A", "C")])
        return make_problem(pid, 1, number, "G.CO.7", "Geometric vocabulary and notation", "conceptual", difficulty, q, ans, exp, svg, "Diagram with points A, B, and C connected by a segment and a ray.")
    if template == 9:
        a = (-3, -1)
        b = (variant, -1)
        c = (variant, variant + 3)
        d = (-3, variant + 3)
        q = f"Use slopes and distances to prove that quadrilateral ABCD with A{a}, B{b}, C{c}, and D{d} is a rectangle."
        w = b[0] - a[0]
        h = c[1] - b[1]
        ans = "ABCD is a rectangle."
        exp = (
            f"Segment AB is horizontal because A and B have y-coordinate {a[1]}, and CD is horizontal because C and D have y-coordinate {c[1]}. "
            f"Segment BC is vertical because B and C have x-coordinate {b[0]}, and AD is vertical because A and D have x-coordinate {a[0]}. "
            "Horizontal and vertical lines are perpendicular, so each angle is a right angle. Opposite sides are parallel, and adjacent sides are perpendicular; therefore ABCD is a rectangle."
        )
        proof = (
            f"AB and CD have slope 0, so AB is parallel to CD. BC and AD are vertical, so BC is parallel to AD. "
            "A horizontal line is perpendicular to a vertical line, so angle ABC is a right angle. A parallelogram with one right angle is a rectangle. "
            f"The side lengths are AB = CD = {w} and BC = AD = {h}, which also confirms the opposite-side structure."
        )
        svg = coordinate_svg("Coordinate rectangle proof", {"A": a, "B": b, "C": c, "D": d}, polygons=[["A", "B", "C", "D"]])
        return make_problem(pid, 1, number, "G.GPE.6", "Coordinate proof", "proof", difficulty, q, ans, exp, svg, "Coordinate rectangle ABCD.", True, proof)
    x = 3 * variant + 15
    q = (
        f"Two intersecting lines form a pair of vertical angles. One angle is {x} degrees. "
        "Write a short proof that the vertical angle opposite it also has that measure."
    )
    ans = f"The opposite vertical angle is {x} degrees."
    exp = (
        "The proof uses the fact that each vertical angle forms a linear pair with the same adjacent angle. "
        "Because both linear pairs sum to 180 degrees, subtracting the shared adjacent angle from 180 gives equal remaining angles. "
        f"Thus the angle opposite the {x}-degree angle must also be {x} degrees."
    )
    proof = (
        "Let angles 1 and 3 be vertical angles, and let angle 2 be adjacent to both. "
        "Angles 1 and 2 form a linear pair, so m angle 1 + m angle 2 = 180. Angles 2 and 3 also form a linear pair, so m angle 2 + m angle 3 = 180. "
        "Since both sums equal 180, m angle 1 + m angle 2 = m angle 2 + m angle 3. Subtract m angle 2 from both sides to get m angle 1 = m angle 3."
    )
    svg = angle_svg("Vertical angle proof", [f"1: {x}", "2", "3", "4"])
    return make_problem(pid, 1, number, "G.CO.7", "Vertical angle theorem proof", "proof", difficulty, q, ans, exp, svg, "Intersecting lines with vertical angles.", True, proof)


def transformations(pid: str, number: int, variant: int, template: int, difficulty: str) -> dict:
    if template == 1:
        p = (variant - 5, 2)
        dx, dy = variant % 4 + 1, -((variant + 1) % 3 + 1)
        image = (p[0] + dx, p[1] + dy)
        q = f"Translate point P{p} by the rule (x, y) -> ({shifted_var('x', dx)}, {shifted_var('y', dy)}). What is P'?"
        ans = f"P' = {image}."
        exp = (
            "A translation adds the same horizontal and vertical changes to every point. "
            f"Add {dx} to the x-coordinate {p[0]} to get {image[0]}, and add {dy} to the y-coordinate {p[1]} to get {image[1]}. "
            "The shape and all distances would be preserved because every point moves by the same vector."
        )
        svg = coordinate_svg("Translation", {"P": p, "P'": image}, segments=[("P", "P'")])
        return make_problem(pid, 2, number, "G.CO.2", "Translations as functions", "computation", difficulty, q, ans, exp, svg, "Coordinate plane showing a point and its translated image.")
    if template == 2:
        p = (variant - 3, variant % 5 + 1)
        image = (p[0], -p[1])
        q = f"Reflect point P{p} across the x-axis. Give the coordinates of P' and describe what changed."
        ans = f"P' = {image}; the x-coordinate stays the same and the y-coordinate changes sign."
        exp = (
            "A reflection across the x-axis keeps the same horizontal position and places the point the same distance on the other side of the x-axis. "
            f"That rule is (x, y) -> (x, -y). Applying it to P{p} gives P'{image}. "
            "The distance from P to the x-axis equals the distance from P' to the x-axis."
        )
        svg = coordinate_svg("Reflection across x-axis", {"P": p, "P'": image}, segments=[("P", "P'")])
        return make_problem(pid, 2, number, "G.CO.1", "Reflections", "computation", difficulty, q, ans, exp, svg, "Point reflected across the x-axis.")
    if template == 3:
        p = (variant % 5 + 1, variant - 5)
        image = (-p[1], p[0])
        q = f"Rotate point P{p} 90 degrees counterclockwise about the origin. What is P'?"
        ans = f"P' = {image}."
        exp = (
            "A 90-degree counterclockwise rotation about the origin follows the rule (x, y) -> (-y, x). "
            f"For P{p}, the new x-coordinate is -({p[1]}) = {image[0]}, and the new y-coordinate is {p[0]}. "
            "The point changes position, but its distance from the origin remains the same."
        )
        svg = coordinate_svg("Rotation", {"P": p, "P'": image, "O": (0, 0)}, segments=[("O", "P"), ("O", "P'")])
        return make_problem(pid, 2, number, "G.CO.1", "Rotations", "computation", difficulty, q, ans, exp, svg, "Point rotated around the origin.")
    if template == 4:
        a, b, c = (-4, 1), (-1, 1), (-3, 4)
        dx, dy = variant % 4 + 1, variant % 3 - 1
        ap, bp, cp = (a[0] + dx, a[1] + dy), (b[0] + dx, b[1] + dy), (c[0] + dx, c[1] + dy)
        q = f"Triangle ABC maps to A'B'C' by a translation. A{a}, B{b}, C{c}, and A'{ap}. Describe the translation and find B' and C'."
        ans = f"Translation vector <{dx}, {dy}>; B' = {bp}; C' = {cp}."
        exp = (
            f"Compare A to A': the x-coordinate changes by {dx} and the y-coordinate changes by {dy}. "
            "A translation applies that same vector to every point. "
            f"Adding <{dx}, {dy}> to B gives {bp}, and adding it to C gives {cp}. "
            "Because the same movement is used for all vertices, side lengths and angle measures are preserved."
        )
        svg = coordinate_svg("Triangle translation", {"A": a, "B": b, "C": c, "A'": ap, "B'": bp, "C'": cp}, polygons=[["A", "B", "C"], ["A'", "B'", "C'"]])
        return make_problem(pid, 2, number, "G.CO.3", "Sequences of rigid motions", "construction", difficulty, q, ans, exp, svg, "Preimage and translated image triangles.")
    if template == 5:
        sides = 4 + (variant % 5)
        q = f"A regular {sides}-gon is shown. How many lines of reflection symmetry and what least positive rotational symmetry angle does it have?"
        angle = Fraction(360, sides)
        ans = f"It has {sides} lines of reflection symmetry and least positive rotation {fmt_frac(angle)} degrees."
        exp = (
            f"A regular {sides}-gon has all sides and all angles congruent, so each vertex and each side-center determines a symmetry axis. "
            f"That gives {sides} reflection symmetries. Rotational symmetry occurs when a vertex maps to the next vertex, which is one {sides}th of a full turn. "
            f"Therefore the least positive rotation is 360/{sides} = {fmt_frac(angle)} degrees."
        )
        pts = []
        cx, cy, r = 180, 130, 78
        for k in range(sides):
            theta = -math.pi / 2 + 2 * math.pi * k / sides
            pts.append((cx + r * math.cos(theta), cy + r * math.sin(theta)))
        svg = svg_base("Regular polygon symmetry", svg_polygon(pts, "#2563eb", "#dbeafe", 2.2) + "\n  " + svg_text(180, 235, f"regular {sides}-gon", 12))
        return make_problem(pid, 2, number, "G.CO.1d", "Symmetry", "conceptual", difficulty, q, ans, exp, svg, "Regular polygon used to reason about reflection and rotation symmetry.")
    if template == 6:
        p, qpt = (-variant, 1), (variant, 1 + variant % 3)
        pp, qq = (p[0] + 3, p[1] - 2), (qpt[0] + 3, qpt[1] - 2)
        original = distance(p, qpt)
        image = distance(pp, qq)
        question = f"Segment PQ is translated to P'Q'. P{p}, Q{qpt}, P'{pp}, and Q'{qq}. Verify that the translation preserves length."
        ans = f"PQ = {fmt_float(original)} and P'Q' = {fmt_float(image)}, so the lengths are equal."
        exp = (
            "Use the distance formula on the original segment and on the image segment. "
            f"PQ = sqrt(({sub_expr(qpt[0], p[0])})^2 + ({sub_expr(qpt[1], p[1])})^2) = {fmt_float(original)}. "
            f"P'Q' = sqrt(({sub_expr(qq[0], pp[0])})^2 + ({sub_expr(qq[1], pp[1])})^2) = {fmt_float(image)}. "
            "The same vector was added to both endpoints, so the coordinate differences stayed the same and the length stayed the same."
        )
        proof = (
            "Let a translation add vector <a, b> to both endpoints. The original coordinate differences are x2 - x1 and y2 - y1. "
            "After translation they become (x2 + a) - (x1 + a) and (y2 + b) - (y1 + b), which simplify to the original differences. "
            "Since the distance formula depends only on those differences, the original and image lengths are equal."
        )
        svg = coordinate_svg("Translation preserves distance", {"P": p, "Q": qpt, "P'": pp, "Q'": qq}, segments=[("P", "Q"), ("P'", "Q'")])
        return make_problem(pid, 2, number, "G.CO.1a", "Rigid motions preserve length", "proof", difficulty, question, ans, exp, svg, "Original and translated segments.", True, proof)
    if template == 7:
        given = 45 + variant * 3
        same = given
        supplement = 180 - given
        q = (
            f"Two parallel lines are cut by a transversal. One corresponding angle measures {given} degrees. "
            "Find the corresponding angle and an adjacent linear-pair angle."
        )
        ans = f"Corresponding angle = {same} degrees; adjacent linear-pair angle = {supplement} degrees."
        exp = (
            "When a transversal crosses parallel lines, corresponding angles are congruent. "
            f"So the matching corresponding angle also measures {given} degrees. "
            "An adjacent angle forming a linear pair is supplementary to it, so subtract from 180: "
            f"180 - {given} = {supplement} degrees."
        )
        svg = angle_svg("Parallel lines cut by a transversal", [f"{given}", f"{supplement}", f"{same}", ""])
        return make_problem(pid, 2, number, "G.CO.7", "Parallel line angle relationships", "computation", difficulty, q, ans, exp, svg, "Parallel-line angle diagram with a transversal.")
    if template == 8:
        a, b, c = (-3, 0), (0, 0), (-2, 3)
        ap, bp, cp = (3, 0), (0, 0), (2, 3)
        q = "The diagram shows triangle ABC and triangle A'B'C'. Decide whether the figures are congruent by a rigid motion and name one motion."
        ans = "They are congruent by reflection across the y-axis."
        exp = (
            "A reflection across the y-axis changes each x-coordinate to its opposite while keeping the y-coordinate the same. "
            "Point A(-3, 0) maps to A'(3, 0), B(0, 0) stays on the axis, and C(-2, 3) maps to C'(2, 3). "
            "Reflections are rigid motions, so lengths and angle measures are preserved. Therefore the triangles are congruent."
        )
        svg = coordinate_svg("Congruence by reflection", {"A": a, "B": b, "C": c, "A'": ap, "B'": bp, "C'": cp}, polygons=[["A", "B", "C"], ["A'", "B'", "C'"]])
        return make_problem(pid, 2, number, "G.CO.5", "Congruence by rigid motion", "conceptual", difficulty, q, ans, exp, svg, "Two reflected triangles on a coordinate plane.")
    if template == 9:
        dx, dy = variant + 1, 2 - (variant % 4)
        x, y = variant - 5, variant % 6 - 2
        out = (x + dx, y + dy)
        q = f"A transformation is defined by T(x, y) = ({shifted_var('x', dx)}, {shifted_var('y', dy)}). Find T({x}, {y}) and explain why this rule is a function."
        ans = f"T({x}, {y}) = {out}; it is a function because each input point has exactly one output point."
        exp = (
            f"Substitute the input coordinates into the rule: ({add_expr(x, dx)}, {add_expr(y, dy)}) = {out}. "
            "The rule gives one specific ordered pair for any input ordered pair. "
            "That single-output behavior is exactly why transformations can be described as functions from points in the plane to points in the plane."
        )
        svg = coordinate_svg("Transformation as a function", {"Input": (x, y), "Output": out}, segments=[("Input", "Output")])
        return make_problem(pid, 2, number, "G.CO.2", "Transformations as functions", "computation", difficulty, q, ans, exp, svg, "Input point mapped to output point by a transformation rule.")
    angle = 30 + variant * 5
    q = (
        f"Line r is reflected across line k. The angle between r and k is {angle} degrees. "
        "Prove that the reflected line r' makes the same angle with k."
    )
    ans = f"Line r' also makes a {angle}-degree angle with k."
    exp = (
        "Reflection uses the mirror line as a perpendicular bisector between each point and its image. "
        "The mirror line is fixed, and the angle a figure makes with the mirror line is copied to the other side. "
        f"Therefore the reflected line forms the same {angle}-degree angle with k."
    )
    proof = (
        "Choose two points on line r and reflect them across k to form line r'. Reflection preserves angle measure and fixes every point on k. "
        "The angle formed by r and k has image equal to the angle formed by r' and k. Because reflections are isometries and preserve angle measure, those two angles are congruent. "
        f"Thus r' makes a {angle}-degree angle with k."
    )
    svg = angle_svg("Reflection angle proof", [f"r: {angle}", "k", "r'", f"{angle}"])
    return make_problem(pid, 2, number, "G.CO.1b", "Reflection preserves angle measure", "proof", difficulty, q, ans, exp, svg, "Line reflected across a mirror line.", True, proof)


def triangles(pid: str, number: int, variant: int, template: int, difficulty: str) -> dict:
    if template == 1:
        a = 35 + variant
        b = 55 + 2 * variant
        c = 180 - a - b
        q = f"In triangle ABC, m angle A = {a} degrees and m angle B = {b} degrees. Find m angle C."
        ans = f"m angle C = {c} degrees."
        exp = (
            "The interior angles of a triangle always sum to 180 degrees. "
            f"Add the two known angles: {a} + {b} = {a + b}. "
            f"Subtract from 180 to find the missing angle: 180 - {a + b} = {c}. "
            "The result is positive and completes the triangle angle sum."
        )
        svg = triangle_svg("Triangle angle sum", [(110, 190, f"{a} deg"), (245, 190, f"{b} deg"), (165, 85, "C")])
        return make_problem(pid, 3, number, "G.CO.8", "Triangle angle sum", "computation", difficulty, q, ans, exp, svg, "Triangle with two given angles.")
    if template == 2:
        remote1 = 35 + variant
        remote2 = 50 + 2 * variant
        exterior = remote1 + remote2
        q = f"An exterior angle of a triangle has remote interior angles measuring {remote1} degrees and {remote2} degrees. Find the exterior angle."
        ans = f"The exterior angle measures {exterior} degrees."
        exp = (
            "The exterior angle theorem says an exterior angle of a triangle equals the sum of its two remote interior angles. "
            f"Add the remote angles: {remote1} + {remote2} = {exterior}. "
            "This works because the exterior angle is supplementary to the adjacent interior angle, and the three interior angles total 180 degrees."
        )
        svg = triangle_svg("Exterior angle theorem", [(100, 190, f"{remote1} deg"), (165, 85, f"{remote2} deg"), (286, 195, "exterior")])
        return make_problem(pid, 3, number, "G.CO.8", "Exterior angle theorem", "computation", difficulty, q, ans, exp, svg, "Triangle with an exterior angle.")
    if template == 3:
        vertex = 40 + 2 * variant
        base = Fraction(180 - vertex, 2)
        q = f"Triangle ABC is isosceles with AC congruent to BC. The vertex angle C measures {vertex} degrees. Find each base angle."
        ans = f"Each base angle measures {fmt_frac(base)} degrees."
        exp = (
            "In an isosceles triangle, the angles opposite the congruent sides are congruent. "
            f"The two base angles therefore have equal measure. Subtract the vertex angle from 180: 180 - {vertex} = {180 - vertex}. "
            f"Divide the remaining angle measure equally: {180 - vertex}/2 = {fmt_frac(base)} degrees."
        )
        svg = triangle_svg("Isosceles triangle", [(110, 190, "base"), (245, 190, "base"), (165, 85, f"{vertex} deg")])
        return make_problem(pid, 3, number, "G.CO.8", "Isosceles base angles", "computation", difficulty, q, ans, exp, svg, "Isosceles triangle with vertex angle labeled.")
    if template == 4:
        a = (0, 0)
        b = (variant + 3, 0)
        c = (0, variant + 4)
        ab, ac, bc = distance(a, b), distance(a, c), distance(b, c)
        q = f"Classify triangle ABC with A{a}, B{b}, and C{c} by side lengths and determine whether it is right."
        ans = f"AB = {fmt_float(ab)}, AC = {fmt_float(ac)}, BC = {fmt_float(bc)}; the triangle is scalene and right."
        exp = (
            "Segment AB is horizontal and segment AC is vertical, so they are perpendicular and form a right angle at A. "
            f"The side lengths are AB = {fmt_float(ab)}, AC = {fmt_float(ac)}, and BC = {fmt_float(bc)} by the distance formula. "
            "Because all three side lengths are different, the triangle is scalene. Because one pair of sides is perpendicular, it is a right triangle."
        )
        svg = coordinate_svg("Coordinate triangle classification", {"A": a, "B": b, "C": c}, polygons=[["A", "B", "C"]])
        return make_problem(pid, 3, number, "G.GPE.6", "Coordinate triangle classification", "computation", difficulty, q, ans, exp, svg, "Coordinate right triangle.")
    if template == 5:
        side1, side2, angle = 5 + variant, 7 + variant, 35 + variant
        q = (
            f"Triangles ABC and DEF have AB congruent to DE, AC congruent to DF, and included angle A congruent to included angle D. "
            f"The matching side lengths are {side1} and {side2}, and the included angle is {angle} degrees. Which congruence theorem applies?"
        )
        ans = "SAS congruence applies."
        exp = (
            "The information gives two pairs of corresponding sides and the angle included between those sides. "
            "That is exactly the Side-Angle-Side pattern. "
            "Because the angle is included, it fixes how the two sides open, so the triangles cannot flex into a noncongruent shape."
        )
        svg = triangle_svg("SAS congruence", [(110, 190, f"{side1}"), (215, 130, f"{side2}"), (95, 165, f"{angle} deg")])
        return make_problem(pid, 3, number, "G.CO.9", "Triangle congruence criteria", "conceptual", difficulty, q, ans, exp, svg, "Triangle with two sides and included angle labeled.")
    if template == 6:
        q = "Given AB congruent to DE, angle A congruent to angle D, and angle B congruent to angle E, prove triangle ABC congruent to triangle DEF."
        ans = "Triangle ABC is congruent to triangle DEF by ASA."
        exp = (
            "The givens identify two pairs of corresponding angles and the included side between them. "
            "That matches the Angle-Side-Angle congruence theorem. "
            "Once the triangles are congruent, all corresponding sides and angles are congruent by CPCTC."
        )
        proof = (
            "Statements: AB congruent to DE, angle A congruent to angle D, and angle B congruent to angle E are given. "
            "Side AB is included between angles A and B, and side DE is included between angles D and E. "
            "Therefore triangle ABC is congruent to triangle DEF by ASA. By corresponding parts of congruent triangles are congruent, any needed matching parts such as AC and DF or angle C and angle F are congruent."
        )
        svg = triangle_svg("ASA proof", [(115, 190, "A"), (250, 190, "B"), (165, 80, "C")])
        return make_problem(pid, 3, number, "G.CO.9", "Triangle congruence proofs", "proof", difficulty, q, ans, exp, svg, "Triangle diagram for ASA proof.", True, proof)
    if template == 7:
        de = 6 + variant
        ac = 2 * de
        q = f"In triangle ABC, D is the midpoint of AB and E is the midpoint of BC. Segment DE is parallel to AC and DE = {de}. Find AC."
        ans = f"AC = {ac}."
        exp = (
            "The segment joining the midpoints of two sides of a triangle is a midsegment. "
            "A triangle midsegment is parallel to the third side and half its length. "
            f"Since DE = {de}, the third side AC is twice as long: AC = 2({de}) = {ac}."
        )
        proof = (
            "Because D and E are midpoints, AD/AB = BE/BC = 1/2. By the converse of proportionality in triangles, DE is parallel to AC. "
            "The smaller triangle DBE is similar to triangle ABC with scale factor 1/2, so DE/AC = 1/2. Therefore AC = 2DE."
        )
        svg = triangle_svg("Triangle midsegment", [(180, 195, f"DE = {de}"), (205, 135, "midsegment"), (180, 222, "AC")])
        return make_problem(pid, 3, number, "G.CO.8", "Triangle midsegments", "proof", difficulty, q, ans, exp, svg, "Triangle with a midsegment parallel to the base.", True, proof)
    if template == 8:
        a, b, c = (0, 0), (6, 0), (0, 6 + variant)
        centroid = (Fraction(a[0] + b[0] + c[0], 3), Fraction(a[1] + b[1] + c[1], 3))
        q = f"Find the centroid of triangle ABC with A{a}, B{b}, and C{c}."
        ans = f"Centroid = ({fmt_frac(centroid[0])}, {fmt_frac(centroid[1])})."
        exp = (
            "The centroid is the intersection point of the three medians of a triangle. "
            "In coordinates, its x-coordinate is the average of the vertex x-coordinates and its y-coordinate is the average of the vertex y-coordinates. "
            f"x = (0 + 6 + 0)/3 = {fmt_frac(centroid[0])}; y = (0 + 0 + {c[1]})/3 = {fmt_frac(centroid[1])}. "
            "This point balances the triangle and lies two-thirds of the way from each vertex to the midpoint of the opposite side."
        )
        svg = coordinate_svg("Centroid", {"A": a, "B": b, "C": c, "G": (float(centroid[0]), float(centroid[1]))}, polygons=[["A", "B", "C"]])
        return make_problem(pid, 3, number, "G.CO.8", "Medians and centroid", "application", difficulty, q, ans, exp, svg, "Triangle with centroid on coordinate plane.")
    if template == 9:
        q = "Explain how a sequence of rigid motions can justify SSS triangle congruence."
        ans = "Move one triangle so one side coincides, then use the fixed distances from the endpoints to force the third vertex to the matching location."
        exp = (
            "If all three corresponding sides are congruent, translate and rotate the first triangle so one side lies exactly on its matching side. "
            "The third vertex must be at a point that is the correct distance from each endpoint of that side. "
            "There are only two such positions, one on each side of the base; a reflection across the base handles the opposite-side case. "
            "Therefore a sequence of rigid motions maps one triangle to the other, proving congruence."
        )
        proof = (
            "Translate and rotate triangle ABC so AB coincides with DE. Since AC = DF and BC = EF, point C and point F lie at the intersections of circles centered at the endpoints of the common base with the same radii. "
            "Those intersections are symmetric across the base. If C is not already on F, reflect across the base. The composition of translation, rotation, and possibly reflection maps ABC to DEF, so the triangles are congruent."
        )
        svg = triangle_svg("SSS by rigid motions", [(180, 205, "shared base"), (115, 130, "same radius"), (235, 130, "same radius")])
        return make_problem(pid, 3, number, "G.CO.6", "Rigid motion proof of congruence", "proof", difficulty, q, ans, exp, svg, "Triangle showing side constraints for SSS.", True, proof)
    hyp = 13 + variant
    leg = 5 + variant
    other = math.sqrt(hyp * hyp - leg * leg)
    q = f"Right triangles ABC and DEF have congruent hypotenuses of length {hyp} and one congruent leg of length {leg}. Which theorem proves they are congruent?"
    ans = "HL congruence proves the right triangles are congruent."
    exp = (
        "The Hypotenuse-Leg theorem applies only to right triangles. "
        f"The problem gives a congruent hypotenuse of length {hyp} and a congruent corresponding leg of length {leg}. "
        "In a right triangle, the other leg is determined by the Pythagorean Theorem, so the triangle is fixed by that information. "
        f"The remaining leg would have length sqrt({hyp}^2 - {leg}^2) = {fmt_float(other)}, confirming both right triangles have all corresponding sides equal."
    )
    svg = triangle_svg("HL congruence", [(170, 218, f"leg {leg}"), (235, 135, f"hyp {hyp}")], right=True)
    return make_problem(pid, 3, number, "G.CO.9", "HL congruence", "conceptual", difficulty, q, ans, exp, svg, "Right triangle with hypotenuse and leg labeled.")


def quadrilaterals(pid: str, number: int, variant: int, template: int, difficulty: str) -> dict:
    if template == 1:
        a, b, c, d = (0, 0), (4 + variant, 0), (4 + variant, 3 + variant), (0, 3 + variant)
        q = f"Classify quadrilateral ABCD with A{a}, B{b}, C{c}, and D{d} as specifically as possible."
        ans = "ABCD is a rectangle."
        exp = (
            "Opposite sides are parallel because AB and CD are horizontal, while BC and AD are vertical. "
            "Adjacent horizontal and vertical sides are perpendicular, giving right angles. "
            "The side lengths are not all equal for these dimensions, so the most specific classification is rectangle rather than square."
        )
        svg = coordinate_svg("Quadrilateral classification", {"A": a, "B": b, "C": c, "D": d}, polygons=[["A", "B", "C", "D"]])
        return make_problem(pid, 4, number, "G.GPE.6", "Coordinate quadrilateral classification", "computation", difficulty, q, ans, exp, svg, "Coordinate rectangle.")
    if template == 2:
        angle_a = 60 + variant
        angle_b = 180 - angle_a
        q = f"In parallelogram ABCD, m angle A = {angle_a} degrees. Find m angle B, m angle C, and m angle D."
        ans = f"m angle B = {angle_b}, m angle C = {angle_a}, and m angle D = {angle_b} degrees."
        exp = (
            "Opposite angles in a parallelogram are congruent, and consecutive angles are supplementary. "
            f"Since angle A is {angle_a} degrees, opposite angle C is also {angle_a} degrees. "
            f"Angles A and B are consecutive, so B = 180 - {angle_a} = {angle_b}; opposite angle D equals B."
        )
        svg = quadrilateral_svg("Parallelogram angles", [(80, 105, f"A {angle_a}"), (270, 105, "B"), (238, 190, "C"), (48, 190, "D")])
        return make_problem(pid, 4, number, "G.CO.10", "Parallelogram angle properties", "computation", difficulty, q, ans, exp, svg, "Parallelogram with one angle labeled.")
    if template == 3:
        half_ac = variant + 5
        half_bd = variant + 3
        q = f"In parallelogram ABCD, diagonals AC and BD intersect at E. If AE = {half_ac} and BE = {half_bd}, find AC and BD."
        ans = f"AC = {2 * half_ac}; BD = {2 * half_bd}."
        exp = (
            "The diagonals of a parallelogram bisect each other, so E is the midpoint of both diagonals. "
            f"If AE = {half_ac}, then EC = {half_ac} and AC = {half_ac} + {half_ac} = {2 * half_ac}. "
            f"If BE = {half_bd}, then ED = {half_bd} and BD = {half_bd} + {half_bd} = {2 * half_bd}. "
            "The key is that each given segment is only half of its full diagonal, not the entire diagonal."
        )
        proof = (
            "In a parallelogram, opposite sides are parallel: AB is parallel to CD and AD is parallel to BC. "
            "Using alternate interior angles around diagonal intersections shows triangle ABE congruent to triangle CDE by ASA. "
            "Corresponding parts give AE = CE and BE = DE, so E bisects both diagonals."
        )
        svg = quadrilateral_svg("Diagonals bisect", [(174, 135, "E"), (135, 105, f"AE {half_ac}"), (210, 105, f"BE {half_bd}")])
        return make_problem(pid, 4, number, "G.CO.10", "Parallelogram diagonals", "proof", difficulty, q, ans, exp, svg, "Parallelogram with diagonals intersecting at E.", True, proof)
    if template == 4:
        diag = 10 + variant
        q = f"A parallelogram has congruent diagonals, each measuring {diag}. What more specific quadrilateral must it be?"
        ans = "It must be a rectangle."
        exp = (
            "A parallelogram with congruent diagonals is a rectangle. "
            "The congruent diagonals force the adjacent sides to form right angles, which is the extra property needed beyond being a parallelogram. "
            "It could be a square if all sides were also congruent, but the given information only guarantees rectangle."
        )
        proof = (
            "Let ABCD be a parallelogram with AC = BD. Opposite sides of a parallelogram are congruent, so AB = CD and BC = AD. "
            "Compare triangles ABC and BAD: AB is shared, BC = AD, and AC = BD. By SSS, the triangles are congruent. "
            "Corresponding angles ABC and BAD are congruent, and consecutive angles in a parallelogram are supplementary. Congruent supplementary angles are right angles, so the parallelogram is a rectangle."
        )
        svg = quadrilateral_svg("Rectangle diagonal theorem", [(180, 55, f"diagonals {diag}"), (180, 220, "congruent")], "rectangle")
        return make_problem(pid, 4, number, "G.CO.10", "Rectangle properties", "proof", difficulty, q, ans, exp, svg, "Rectangle/parallelogram with congruent diagonals.", True, proof)
    if template == 5:
        side = 5 + variant
        diag1 = 2 * (variant + 3)
        diag2 = 2 * (variant + 4)
        q = f"A rhombus has side length {side}, diagonal lengths {diag1} and {diag2}, and perpendicular diagonals. What is its perimeter?"
        ans = f"Perimeter = {4 * side}."
        exp = (
            "A rhombus has four congruent sides. The diagonal information can help with area or angle reasoning, but perimeter only needs the side length. "
            f"Multiply the side length by 4: P = 4({side}) = {4 * side}. "
            "The perpendicular diagonals are consistent with a rhombus but are not needed for this particular perimeter calculation."
        )
        svg = quadrilateral_svg("Rhombus perimeter", [(180, 52, f"side {side}"), (180, 135, f"d1 {diag1}, d2 {diag2}")], "kite")
        return make_problem(pid, 4, number, "G.GPE.8", "Rhombus properties", "conceptual", difficulty, q, ans, exp, svg, "Rhombus with side and diagonal labels.")
    if template == 6:
        b1 = 12 + variant
        b2 = 18 + variant
        mid = Fraction(b1 + b2, 2)
        q = f"A trapezoid has bases {b1} and {b2}. Find the length of its midsegment."
        ans = f"Midsegment length = {fmt_frac(mid)}."
        exp = (
            "The midsegment of a trapezoid connects the midpoints of the legs and is parallel to both bases. "
            "Its length is the average of the two base lengths. "
            f"Compute ({b1} + {b2})/2 = {fmt_frac(mid)}. "
            "This average appears because the midsegment lies halfway between the bases."
        )
        svg = quadrilateral_svg("Trapezoid midsegment", [(180, 73, f"base {b1}"), (180, 220, f"base {b2}"), (180, 145, "midsegment")], "trapezoid")
        return make_problem(pid, 4, number, "G.GPE.8", "Trapezoids", "computation", difficulty, q, ans, exp, svg, "Trapezoid with bases and midsegment.")
    if template == 7:
        a, b, c, d = (0, 0), (variant + 3, 0), (variant + 3, variant + 4), (0, variant + 4)
        per = 2 * ((variant + 3) + (variant + 4))
        area = (variant + 3) * (variant + 4)
        q = f"Find the perimeter and area of rectangle ABCD with A{a}, B{b}, C{c}, and D{d}."
        ans = f"Perimeter = {per}; area = {area}."
        exp = (
            f"The horizontal side length is {variant + 3} and the vertical side length is {variant + 4}. "
            f"Perimeter adds all sides: 2({variant + 3}) + 2({variant + 4}) = {per}. "
            f"Area multiplies base and height: ({variant + 3})({variant + 4}) = {area}. "
            "The coordinate layout makes the side lengths clear because the sides are horizontal and vertical."
        )
        svg = coordinate_svg("Coordinate rectangle perimeter and area", {"A": a, "B": b, "C": c, "D": d}, polygons=[["A", "B", "C", "D"]])
        return make_problem(pid, 4, number, "G.GPE.8", "Coordinate perimeter and area", "computation", difficulty, q, ans, exp, svg, "Coordinate rectangle for perimeter and area.")
    if template == 8:
        n = 5 + (variant % 6)
        sum_angles = (n - 2) * 180
        each = Fraction(sum_angles, n)
        q = f"Find the sum of the interior angles of a {n}-gon and the measure of each interior angle if it is regular."
        ans = f"Interior angle sum = {sum_angles} degrees; each regular interior angle = {fmt_frac(each)} degrees."
        exp = (
            f"An n-gon can be divided into n - 2 triangles from one vertex. For n = {n}, that gives {n - 2} triangles. "
            f"Each triangle has angle sum 180 degrees, so the total is ({n} - 2)(180) = {sum_angles}. "
            f"If the polygon is regular, all interior angles are equal, so divide by {n}: {sum_angles}/{n} = {fmt_frac(each)} degrees."
        )
        pts = []
        for k in range(n):
            theta = -math.pi / 2 + 2 * math.pi * k / n
            pts.append((180 + 78 * math.cos(theta), 130 + 78 * math.sin(theta)))
        svg = svg_base("Polygon angle sum", svg_polygon(pts, "#2563eb", "#dbeafe", 2.2) + "\n  " + svg_text(180, 235, f"{n}-gon", 12))
        return make_problem(pid, 4, number, "G.CO.10", "Polygon angle sums", "computation", difficulty, q, ans, exp, svg, "Regular polygon diagram.")
    if template == 9:
        q = "Prove that opposite sides of a parallelogram are congruent by drawing a diagonal."
        ans = "The diagonal creates two congruent triangles, so opposite sides are congruent by CPCTC."
        exp = (
            "Draw diagonal AC in parallelogram ABCD. Because opposite sides are parallel, alternate interior angles formed by the diagonal are congruent. "
            "The diagonal is a shared side of the two triangles. "
            "That creates ASA triangle congruence, and corresponding sides of congruent triangles are congruent."
        )
        proof = (
            "Draw diagonal AC. Since AB is parallel to CD, angle BAC is congruent to angle DCA. Since AD is parallel to BC, angle BCA is congruent to angle DAC. "
            "Segment AC is congruent to itself by the reflexive property. Therefore triangle BAC is congruent to triangle DCA by ASA. "
            "By CPCTC, AB is congruent to CD and BC is congruent to AD."
        )
        svg = quadrilateral_svg("Opposite sides proof", [(180, 135, "diagonal AC"), (180, 58, "AB || CD"), (180, 225, "AD || BC")])
        return make_problem(pid, 4, number, "G.CO.10", "Parallelogram proof", "proof", difficulty, q, ans, exp, svg, "Parallelogram split by a diagonal.", True, proof)
    dx, dy = variant + 1, variant % 3 + 2
    q = f"A parallelogram is translated by vector <{dx}, {dy}>. Which of its properties are preserved, and why?"
    ans = "Parallelism, side lengths, angle measures, and diagonal bisection are preserved."
    exp = (
        "A translation is a rigid motion, so it preserves distance and angle measure. "
        "It also maps lines to parallel lines or the same line, so opposite sides remain parallel. "
        "Because every point moves by the same vector, midpoints move to corresponding midpoints, so the diagonals still bisect each other. "
        "The image is a congruent parallelogram with the same structural properties."
    )
    proof = (
        "Under a translation T(x, y) = (x + a, y + b), coordinate differences between any two points are unchanged. "
        "Unchanged differences preserve slopes and distances, so parallel sides remain parallel and congruent sides remain congruent. "
        "The midpoint formula also commutes with translation: the image midpoint equals the translated original midpoint. Therefore the diagonal-bisection property is preserved."
    )
    svg = quadrilateral_svg("Translated parallelogram", [(180, 135, f"<{dx}, {dy}>")])
    return make_problem(pid, 4, number, "G.CO.4", "Transformations and quadrilaterals", "application", difficulty, q, ans, exp, svg, "Parallelogram with a translation vector.", True, proof)


def similarity(pid: str, number: int, variant: int, template: int, difficulty: str) -> dict:
    if template == 1:
        p = (variant - 4, 2)
        k = Fraction(variant % 4 + 2, 2)
        image = (p[0] * k, p[1] * k)
        q = f"Dilate point P{p} from the origin by scale factor {fmt_frac(k)}. Find P'."
        ans = f"P' = ({fmt_frac(image[0])}, {fmt_frac(image[1])})."
        exp = (
            "A dilation centered at the origin multiplies both coordinates by the scale factor. "
            f"Multiply x: {p[0]}({fmt_frac(k)}) = {fmt_frac(image[0])}. "
            f"Multiply y: {p[1]}({fmt_frac(k)}) = {fmt_frac(image[1])}. "
            "The image lies on the same ray from the origin as the original point, with distance scaled by the same factor."
        )
        svg = coordinate_svg("Dilation from origin", {"P": p, "P'": (float(image[0]), float(image[1])), "O": (0, 0)}, segments=[("O", "P"), ("O", "P'")])
        return make_problem(pid, 5, number, "G.SRT.1", "Dilation coordinates", "computation", difficulty, q, ans, exp, svg, "Point and dilated image from the origin.")
    if template == 2:
        length = 6 + variant
        k = Fraction(variant % 5 + 2, 3)
        image = length * k
        q = f"A segment of length {length} is dilated by scale factor {fmt_frac(k)}. What is the image length?"
        ans = f"Image length = {fmt_frac(image)}."
        exp = (
            "A dilation multiplies every length by the scale factor. "
            f"Compute {length} x {fmt_frac(k)} = {fmt_frac(image)}. "
            "If the scale factor is greater than 1, the image is longer; if it is between 0 and 1, the image is shorter. "
            "Angles would stay congruent even though the length changes."
        )
        svg = coordinate_svg("Dilation length", {"A": (-4, 1), "B": (1, 1), "A'": (-4, -2), "B'": (-4 + float(image) / 2, -2)}, segments=[("A", "B"), ("A'", "B'")])
        return make_problem(pid, 5, number, "G.SRT.1b", "Dilation length scale", "computation", difficulty, q, ans, exp, svg, "Original segment and dilated segment.")
    if template == 3:
        small1, small2, large1 = 4 + variant, 6 + variant, 2 * (4 + variant)
        large2 = 2 * small2
        q = f"Triangles ABC and DEF are similar. AB corresponds to DE, BC corresponds to EF, AB = {small1}, BC = {small2}, and DE = {large1}. Find EF."
        ans = f"EF = {large2}."
        exp = (
            "Corresponding sides of similar triangles are proportional. "
            f"The scale factor from ABC to DEF is DE/AB = {large1}/{small1} = 2. "
            f"Multiply the corresponding side BC by 2: EF = 2({small2}) = {large2}. "
            "The same scale factor must apply to every pair of corresponding sides."
        )
        svg = triangle_svg("Similar triangle proportions", [(120, 190, f"{small1}"), (220, 125, f"{small2}"), (180, 225, "scale factor 2")])
        return make_problem(pid, 5, number, "G.SRT.4", "Similar triangle proportions", "computation", difficulty, q, ans, exp, svg, "Similar triangles with corresponding side labels.")
    if template == 4:
        q = "Triangles ABC and DEF have two pairs of congruent corresponding angles. Prove the triangles are similar."
        ans = "The triangles are similar by AA similarity."
        exp = (
            "Two corresponding angle pairs being congruent is enough to prove triangle similarity. "
            "The third pair must also be congruent because the angles in each triangle sum to 180 degrees. "
            "With all corresponding angles congruent, the triangles have the same shape, so their side lengths are proportional."
        )
        proof = (
            "Given angle A congruent to angle D and angle B congruent to angle E. In triangle ABC, m angle C = 180 - m angle A - m angle B. "
            "In triangle DEF, m angle F = 180 - m angle D - m angle E. Substituting congruent angle measures gives m angle C = m angle F. "
            "Thus all corresponding angles are congruent, so triangle ABC is similar to triangle DEF by AA similarity."
        )
        svg = triangle_svg("AA similarity proof", [(105, 190, "A ~= D"), (245, 190, "B ~= E"), (165, 80, "C ~= F")])
        return make_problem(pid, 5, number, "G.SRT.6", "AA similarity proof", "proof", difficulty, q, ans, exp, svg, "Two triangles marked with two angle pairs.", True, proof)
    if template == 5:
        ad = 3 + variant
        db = 5 + variant
        ae = 2 * ad
        ec = 2 * db
        q = f"In triangle ABC, DE is parallel to BC with D on AB and E on AC. If AD = {ad}, DB = {db}, and AE = {ae}, find EC."
        ans = f"EC = {ec}."
        exp = (
            "When a line parallel to one side of a triangle intersects the other two sides, it divides those sides proportionally. "
            f"So AD/DB = AE/EC. Substitute: {ad}/{db} = {ae}/EC. "
            f"Since AE is twice AD, EC must be twice DB: EC = 2({db}) = {ec}. "
            "The proportional relationship comes from the similarity of the smaller and larger triangles."
        )
        proof = (
            "Because DE is parallel to BC, corresponding angles in triangle ADE and triangle ABC are congruent. "
            "Thus triangle ADE is similar to triangle ABC by AA. Similarity gives AD/AB = AE/AC. "
            "Rewriting whole side lengths as AB = AD + DB and AC = AE + EC leads to AD/DB = AE/EC, the side-splitter proportionality."
        )
        svg = triangle_svg("Side splitter theorem", [(125, 165, f"AD {ad}"), (105, 210, f"DB {db}"), (210, 135, f"AE {ae}"), (245, 205, "EC ?")])
        return make_problem(pid, 5, number, "G.SRT.5", "Triangle proportionality", "proof", difficulty, q, ans, exp, svg, "Triangle with a segment parallel to one side.", True, proof)
    if template == 6:
        a, b = 3 + variant, 4 + variant
        c2 = a * a + b * b
        q = f"Use a similarity argument to explain why a right triangle with legs {a} and {b} has hypotenuse squared equal to {c2}."
        ans = f"c^2 = {a}^2 + {b}^2 = {c2}."
        exp = (
            "Dropping an altitude from the right angle to the hypotenuse creates three similar right triangles. "
            "Those similarities give proportional relationships between each leg and the hypotenuse segments. "
            "Adding the two leg-square relationships yields a^2 + b^2 = c^2. "
            f"For this triangle, {a}^2 + {b}^2 = {a*a} + {b*b} = {c2}."
        )
        proof = (
            "Draw the altitude from the right angle to the hypotenuse, splitting the hypotenuse into segments x and y. "
            "Similarity gives a^2 = c x and b^2 = c y. Adding gives a^2 + b^2 = c(x + y). "
            "Since x + y = c, the result is a^2 + b^2 = c^2."
        )
        svg = triangle_svg("Similarity proof of Pythagorean Theorem", [(120, 205, f"a={a}"), (260, 142, "c"), (130, 130, f"b={b}")], right=True)
        return make_problem(pid, 5, number, "G.SRT.5", "Pythagorean Theorem by similarity", "proof", difficulty, q, ans, exp, svg, "Right triangle with altitude to hypotenuse.", True, proof)
    if template == 7:
        scale = variant % 4 + 2
        dx, dy = variant - 4, 2
        q = f"Describe a sequence of transformations that maps a figure to a similar image with scale factor {scale} and then moves it by vector <{dx}, {dy}>."
        ans = f"Dilate the figure by scale factor {scale}, then translate it by <{dx}, {dy}>."
        exp = (
            "Similarity transformations are built from dilations and rigid motions. "
            f"First, a dilation with scale factor {scale} changes all lengths by that factor while preserving angle measures. "
            f"Then the translation <{dx}, {dy}> moves the dilated figure without changing its size or shape. "
            "The final image is similar to the original because the only size-changing step was the dilation."
        )
        svg = coordinate_svg("Similarity transformation sequence", {"A": (-2, 1), "B": (0, 1), "C": (-1, 3), "A'": (dx - 2 * scale, dy + scale), "B'": (dx, dy + scale), "C'": (dx - scale, dy + 3 * scale)}, polygons=[["A", "B", "C"], ["A'", "B'", "C'"]], scale=12)
        return make_problem(pid, 5, number, "G.SRT.3", "Similarity transformations", "conceptual", difficulty, q, ans, exp, svg, "Original triangle and larger translated image.")
    if template == 8:
        ratio = variant % 4 + 2
        area_small = 10 + variant
        area_large = area_small * ratio * ratio
        q = f"Two similar polygons have side-length ratio 1:{ratio}. If the smaller area is {area_small}, find the larger area."
        ans = f"Larger area = {area_large} square units."
        exp = (
            "For similar figures, perimeters scale by the linear scale factor, but areas scale by the square of that factor. "
            f"The linear ratio from small to large is {ratio}, so the area scale factor is {ratio}^2 = {ratio * ratio}. "
            f"Multiply the smaller area by {ratio * ratio}: {area_small} x {ratio * ratio} = {area_large}."
        )
        svg = quadrilateral_svg("Area scale factor", [(120, 205, f"area {area_small}"), (235, 105, f"scale {ratio}")], "rectangle")
        return make_problem(pid, 5, number, "G.SRT.4", "Similarity area scale", "computation", difficulty, q, ans, exp, svg, "Similar rectangles representing area scale.")
    if template == 9:
        k = variant % 5 + 2
        q = f"A line not passing through the center of dilation is dilated by scale factor {k}. Prove that its image line is parallel to the original line."
        ans = "The image line is parallel to the original line."
        exp = (
            "A dilation from a center sends each point along a ray from the center and multiplies distances from the center by the same factor. "
            "For a line not through the center, corresponding triangles formed with the center are similar. "
            "Those similar triangles create equal corresponding angles, so the original and image lines must be parallel."
        )
        proof = (
            "Let A and B be points on the original line, and let A' and B' be their images under dilation centered at O. "
            f"Then OA'/OA = OB'/OB = {k}, and angle AOB is shared, so triangle OAB is similar to triangle OA'B' by SAS similarity. "
            "Corresponding angles OAB and OA'B' are congruent. Congruent corresponding angles imply AB is parallel to A'B'."
        )
        svg = coordinate_svg("Dilation sends line to parallel line", {"O": (0, 0), "A": (-4, 2), "B": (2, 3), "A'": (-4 * k / 2, 2 * k / 2), "B'": (2 * k / 2, 3 * k / 2)}, segments=[("A", "B"), ("A'", "B'"), ("O", "A"), ("O", "A'")], scale=14)
        return make_problem(pid, 5, number, "G.SRT.1a", "Dilation parallel-line property", "proof", difficulty, q, ans, exp, svg, "Line and dilated parallel image from a center.", True, proof)
    height, shadow, person, person_shadow = 20 + variant, 12 + variant, 6, 3
    tree = Fraction(height * person_shadow, shadow)
    q = f"A {person}-ft person casts a {person_shadow}-ft shadow. At the same time, a tree casts a {shadow}-ft shadow. Find the tree height."
    ans = f"Tree height = {fmt_frac(Fraction(person * shadow, person_shadow))} ft."
    exp = (
        "The sun creates the same angle of elevation for both objects, so the two right triangles are similar by AA. "
        f"Set height/shadow ratios equal: tree height/{shadow} = {person}/{person_shadow}. "
        f"Multiply to get tree height = {shadow}({person})/{person_shadow} = {fmt_frac(Fraction(person * shadow, person_shadow))} ft. "
        "The proportional model works because corresponding angles match."
    )
    svg = triangle_svg("Shadow similarity", [(110, 160, f"{person} ft"), (205, 215, f"{person_shadow} ft"), (245, 160, f"{shadow} ft shadow")], right=True)
    return make_problem(pid, 5, number, "G.SRT.6", "Real-world similarity", "application", difficulty, q, ans, exp, svg, "Similar right triangles made by shadows.")


def right_triangles(pid: str, number: int, variant: int, template: int, difficulty: str) -> dict:
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (9, 40, 41)]
    a, b, c = triples[(variant - 1) % len(triples)]
    mult = 1 + (variant // 6)
    a, b, c = a * mult, b * mult, c * mult
    if template == 1:
        q = f"A right triangle has legs {a} and {b}. Find the hypotenuse."
        ans = f"Hypotenuse = {c}."
        exp = (
            "Use the Pythagorean Theorem, a^2 + b^2 = c^2, because the triangle is right. "
            f"Substitute the leg lengths: {a}^2 + {b}^2 = {a*a} + {b*b} = {c*c}. "
            f"Taking the positive square root gives c = {c}. "
            "Only the positive root is used because side lengths are positive."
        )
        svg = triangle_svg("Pythagorean Theorem", [(120, 205, str(a)), (235, 135, str(c)), (92, 135, str(b))], right=True)
        return make_problem(pid, 6, number, "G.SRT.9", "Pythagorean Theorem", "computation", difficulty, q, ans, exp, svg, "Right triangle with legs and hypotenuse.")
    if template == 2:
        q = f"In a right triangle, relative to acute angle A, opposite = {a}, adjacent = {b}, and hypotenuse = {c}. Find sin A, cos A, and tan A."
        ans = f"sin A = {fmt_frac(Fraction(a, c))}, cos A = {fmt_frac(Fraction(b, c))}, tan A = {fmt_frac(Fraction(a, b))}."
        exp = (
            "Trigonometric ratios compare pairs of sides in a right triangle relative to a chosen acute angle. "
            f"sin A = opposite/hypotenuse = {a}/{c} = {fmt_frac(Fraction(a, c))}. "
            f"cos A = adjacent/hypotenuse = {b}/{c} = {fmt_frac(Fraction(b, c))}. "
            f"tan A = opposite/adjacent = {a}/{b} = {fmt_frac(Fraction(a, b))}."
        )
        svg = triangle_svg("Trigonometric ratios", [(120, 205, f"adj {b}"), (235, 135, f"hyp {c}"), (92, 135, f"opp {a}")], right=True)
        return make_problem(pid, 6, number, "G.SRT.7", "Trigonometric ratios", "computation", difficulty, q, ans, exp, svg, "Right triangle labeled opposite, adjacent, and hypotenuse.")
    if template == 3:
        angle = 25 + variant
        hyp = 10 + variant
        opp = hyp * math.sin(math.radians(angle))
        q = f"A right triangle has hypotenuse {hyp} and an acute angle of {angle} degrees. Find the opposite side to the nearest tenth."
        ans = f"Opposite side = {fmt_float(opp, 1)}."
        exp = (
            "Use sine because sine relates opposite side to hypotenuse. "
            f"sin({angle}) = opposite/{hyp}. "
            f"Multiply by {hyp}: opposite = {hyp} sin({angle}) = {fmt_float(opp, 1)}. "
            "Rounding to the nearest tenth gives the requested side length."
        )
        svg = triangle_svg("Solve right triangle side", [(120, 205, "adjacent"), (235, 135, f"hyp {hyp}"), (92, 135, "opposite"), (112, 187, f"{angle} deg")], right=True)
        return make_problem(pid, 6, number, "G.SRT.9", "Solving right triangles", "computation", difficulty, q, ans, exp, svg, "Right triangle with angle and hypotenuse.")
    if template == 4:
        opp, adj = 4 + variant, 7 + variant
        angle = math.degrees(math.atan(Fraction(opp, adj)))
        q = f"In a right triangle, the side opposite angle A is {opp} and the adjacent side is {adj}. Find angle A to the nearest degree."
        ans = f"m angle A = {round(angle)} degrees."
        exp = (
            "Use tangent because tangent compares opposite and adjacent sides. "
            f"tan A = {opp}/{adj}. "
            f"Apply inverse tangent: A = arctan({opp}/{adj}) = {fmt_float(angle, 2)} degrees. "
            f"Rounded to the nearest degree, angle A is {round(angle)} degrees."
        )
        svg = triangle_svg("Inverse tangent", [(120, 205, f"adj {adj}"), (92, 135, f"opp {opp}"), (112, 187, "A")], right=True)
        return make_problem(pid, 6, number, "G.SRT.9", "Inverse trigonometry", "computation", difficulty, q, ans, exp, svg, "Right triangle with opposite and adjacent sides.")
    if template == 5:
        if variant % 2:
            q = "Use a 45-45-90 triangle to find sin 45 degrees and cos 45 degrees exactly."
            ans = "sin 45 degrees = sqrt(2)/2 and cos 45 degrees = sqrt(2)/2."
            exp = (
                "A 45-45-90 triangle has congruent legs. Let each leg be 1. "
                "By the Pythagorean Theorem, the hypotenuse is sqrt(1^2 + 1^2) = sqrt(2). "
                "So sin 45 degrees = opposite/hypotenuse = 1/sqrt(2) = sqrt(2)/2, and cos 45 degrees has the same value."
            )
        else:
            q = "Use a 30-60-90 triangle to find sin 30 degrees and cos 30 degrees exactly."
            ans = "sin 30 degrees = 1/2 and cos 30 degrees = sqrt(3)/2."
            exp = (
                "A 30-60-90 triangle has side ratios 1 : sqrt(3) : 2, with the shortest leg opposite 30 degrees. "
                "Therefore sin 30 degrees = opposite/hypotenuse = 1/2. "
                "The adjacent side to 30 degrees is the longer leg, so cos 30 degrees = sqrt(3)/2."
            )
        svg = triangle_svg("Exact trigonometric ratios", [(120, 205, "special triangle"), (235, 135, "hyp"), (112, 187, "angle")], right=True)
        return make_problem(pid, 6, number, "G.SRT.7", "Exact trigonometric ratios", "conceptual", difficulty, q, ans, exp, svg, "Special right triangle for exact ratios.")
    if template == 6:
        angle = 20 + 3 * variant
        comp = 90 - angle
        q = f"Explain why sin({angle} degrees) = cos({comp} degrees)."
        ans = "They are equal because the angles are complementary."
        exp = (
            f"The two acute angles in a right triangle are complementary, and {angle} + {comp} = 90. "
            "The side opposite one acute angle is the side adjacent to the other acute angle. "
            "Since sine uses opposite/hypotenuse and cosine uses adjacent/hypotenuse, those ratios match for complementary angles."
        )
        proof = (
            f"Let angles A and B be acute angles of a right triangle with A = {angle} degrees and B = {comp} degrees. "
            "The side opposite A is adjacent to B, and both ratios use the same hypotenuse. "
            "Therefore sin A = opposite A/hypotenuse = adjacent B/hypotenuse = cos B."
        )
        svg = triangle_svg("Complementary trig ratios", [(120, 205, "adj to A"), (92, 135, "opp to A"), (112, 187, f"{angle} deg"), (250, 185, f"{comp} deg")], right=True)
        return make_problem(pid, 6, number, "G.SRT.8", "Complementary sine and cosine", "proof", difficulty, q, ans, exp, svg, "Right triangle with complementary acute angles.", True, proof)
    if template == 7:
        side1, side2, angle = 6 + variant, 8 + variant, 30 + variant
        area = 0.5 * side1 * side2 * math.sin(math.radians(angle))
        q = f"Two sides of a triangle measure {side1} and {side2}, and their included angle is {angle} degrees. Find the area to the nearest tenth using A = 1/2 ab sin C."
        ans = f"Area = {fmt_float(area, 1)} square units."
        exp = (
            "The formula A = 1/2 ab sin C finds area when two sides and the included angle are known. "
            f"Substitute: A = 1/2({side1})({side2})sin({angle}). "
            f"That gives A = {fmt_float(area, 1)} square units after evaluating and rounding. "
            "The sine factor converts one side into the height relative to the other side."
        )
        proof = (
            "Draw an altitude from the vertex between sides a and b to the opposite side, creating a right triangle. "
            "In that right triangle, sin C = h/b, so h = b sin C. "
            "The ordinary triangle area formula is A = 1/2(base)(height) = 1/2(a)(b sin C), which is A = 1/2 ab sin C."
        )
        svg = triangle_svg("Area using sine", [(140, 205, f"a={side1}"), (220, 130, f"b={side2}"), (105, 185, f"C={angle}")])
        return make_problem(pid, 6, number, "G.SRT.10", "Area formula with sine", "proof", difficulty, q, ans, exp, svg, "Triangle with two sides and included angle.", True, proof)
    if template == 8:
        angle_a = 35 + variant
        side_a = 9 + variant
        angle_b = 70 - (variant % 10)
        side_b = side_a * math.sin(math.radians(angle_b)) / math.sin(math.radians(angle_a))
        q = f"In triangle ABC, side a = {side_a}, angle A = {angle_a} degrees, and angle B = {angle_b} degrees. Use the Law of Sines to find side b to the nearest tenth."
        ans = f"Side b = {fmt_float(side_b, 1)} units."
        exp = (
            "The Law of Sines says a/sin A = b/sin B for corresponding sides and opposite angles. "
            f"Set {side_a}/sin({angle_a}) = b/sin({angle_b}). "
            f"Solve by multiplying: b = {side_a} sin({angle_b})/sin({angle_a}) = {fmt_float(side_b, 1)}. "
            "This law is useful for non-right triangles when a side-angle opposite pair is known."
        )
        proof = (
            "Drop an altitude h from C to side AB. In one right triangle, h = b sin A. In the other, h = a sin B. "
            "Since both expressions equal the same altitude, b sin A = a sin B. Rearranging gives a/sin A = b/sin B, the Law of Sines."
        )
        svg = triangle_svg("Law of Sines", [(100, 190, f"A {angle_a}"), (250, 190, f"B {angle_b}"), (170, 135, f"a {side_a}")])
        return make_problem(pid, 6, number, "G.SRT.11", "Law of Sines", "proof", difficulty, q, ans, exp, svg, "Non-right triangle labeled for Law of Sines.", True, proof)
    if template == 9:
        side_a, side_b, angle_c = 6 + variant, 9 + variant, 40 + variant
        c_side = math.sqrt(side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(math.radians(angle_c)))
        q = f"Two sides of a triangle are {side_a} and {side_b}, and the included angle is {angle_c} degrees. Use the Law of Cosines to find the third side to the nearest tenth."
        ans = f"Third side = {fmt_float(c_side, 1)}."
        exp = (
            "Use the Law of Cosines because two sides and the included angle are known. "
            f"c^2 = {side_a}^2 + {side_b}^2 - 2({side_a})({side_b})cos({angle_c}). "
            f"Evaluating and taking the square root gives c = {fmt_float(c_side, 1)}. "
            "When the included angle is 90 degrees, this formula reduces to the Pythagorean Theorem."
        )
        proof = (
            "Place one side along the x-axis and drop an altitude from the opposite vertex. "
            "Using coordinates, the third side squared becomes (b cos C - a)^2 + (b sin C)^2. "
            "Expanding and using sin^2 C + cos^2 C = 1 gives a^2 + b^2 - 2ab cos C."
        )
        svg = triangle_svg("Law of Cosines", [(135, 205, str(side_a)), (220, 130, str(side_b)), (105, 185, f"{angle_c} deg")])
        return make_problem(pid, 6, number, "G.SRT.12", "Law of Cosines", "proof", difficulty, q, ans, exp, svg, "Triangle with two sides and included angle.", True, proof)
    angle = 28 + variant
    distance_ground = 50 + 3 * variant
    height = distance_ground * math.tan(math.radians(angle))
    q = f"From a point {distance_ground} ft from a building, the angle of elevation to the top is {angle} degrees. Estimate the building height to the nearest foot."
    ans = f"Building height is about {round(height)} ft."
    exp = (
        "The ground distance is adjacent to the angle of elevation, and the building height is opposite the angle. "
        f"Use tangent: tan({angle}) = height/{distance_ground}. "
        f"Multiply by {distance_ground}: height = {distance_ground}tan({angle}) = {fmt_float(height, 1)} ft. "
        f"Rounded to the nearest foot, the height is {round(height)} ft."
    )
    svg = triangle_svg("Angle of elevation", [(165, 218, f"{distance_ground} ft"), (295, 130, "building"), (110, 187, f"{angle} deg")], right=True)
    return make_problem(pid, 6, number, "G.SRT.9", "Right-triangle applications", "application", difficulty, q, ans, exp, svg, "Right triangle modeling an angle of elevation.")


def area_volume(pid: str, number: int, variant: int, template: int, difficulty: str) -> dict:
    if template == 1:
        a, b, c = (0, 0), (variant + 4, 0), (0, variant + 3)
        area = Fraction((variant + 4) * (variant + 3), 2)
        q = f"Find the area of triangle ABC with A{a}, B{b}, and C{c}."
        ans = f"Area = {fmt_frac(area)} square units."
        exp = (
            "The coordinates form a right triangle with horizontal base and vertical height. "
            f"The base length is {variant + 4} and the height is {variant + 3}. "
            f"Use A = 1/2 bh: A = 1/2({variant + 4})({variant + 3}) = {fmt_frac(area)}. "
            "This matches coordinate area methods because the base and height are perpendicular."
        )
        svg = coordinate_svg("Coordinate triangle area", {"A": a, "B": b, "C": c}, polygons=[["A", "B", "C"]])
        return make_problem(pid, 7, number, "G.GPE.8", "Coordinate area", "computation", difficulty, q, ans, exp, svg, "Coordinate right triangle.")
    if template == 2:
        rect_w, rect_h, cut_w, cut_h = 10 + variant, 8 + variant, 3 + variant % 3, 2 + variant % 4
        area = rect_w * rect_h - cut_w * cut_h
        q = f"An L-shaped region is made from a {rect_w} by {rect_h} rectangle with a {cut_w} by {cut_h} corner removed. Find the area."
        ans = f"Area = {area} square units."
        exp = (
            "Composite area can be found by subtracting missing pieces from a larger familiar shape. "
            f"The full rectangle area is {rect_w} x {rect_h} = {rect_w * rect_h}. "
            f"The removed rectangle area is {cut_w} x {cut_h} = {cut_w * cut_h}. "
            f"Subtract to get {rect_w * rect_h} - {cut_w * cut_h} = {area} square units."
        )
        body = svg_polygon([(70, 60), (290, 60), (290, 120), (210, 120), (210, 205), (70, 205)], "#2563eb", "#dbeafe", 2.2)
        body += "\n  " + svg_text(180, 45, f"{rect_w} by {rect_h} minus {cut_w} by {cut_h}", 12)
        svg = svg_base("Composite L-shape area", body)
        return make_problem(pid, 7, number, "G.MG.1", "Composite area", "application", difficulty, q, ans, exp, svg, "L-shaped composite region.")
    if template == 3:
        n = 5 + (variant % 5)
        side = 4 + variant
        apothem = 3 + variant
        area = Fraction(n * side * apothem, 2)
        q = f"A regular {n}-gon has side length {side} and apothem {apothem}. Find its area."
        ans = f"Area = {fmt_frac(area)} square units."
        exp = (
            "A regular polygon can be divided into congruent triangles, each with base equal to a side and height equal to the apothem. "
            f"The perimeter is {n} x {side} = {n * side}. "
            f"Use A = 1/2 apothem x perimeter: A = 1/2({apothem})({n * side}) = {fmt_frac(area)}. "
            "This formula is a compact version of adding the areas of all the small triangles."
        )
        pts = []
        for k in range(n):
            theta = -math.pi / 2 + 2 * math.pi * k / n
            pts.append((180 + 78 * math.cos(theta), 130 + 78 * math.sin(theta)))
        svg = svg_base("Regular polygon area", svg_polygon(pts, "#2563eb", "#dbeafe", 2.2) + "\n  " + svg_text(180, 235, f"s={side}, a={apothem}", 12))
        return make_problem(pid, 7, number, "G.MG.1", "Regular polygon area", "conceptual", difficulty, q, ans, exp, svg, "Regular polygon with side and apothem.")
    if template == 4:
        radius = 5 + variant
        theta = 30 + 5 * variant
        arc = Fraction(theta, 360) * 2 * math.pi * radius
        area = Fraction(theta, 360) * math.pi * radius * radius
        q = f"A sector has radius {radius} and central angle {theta} degrees. Find the exact sector area in terms of pi."
        area_frac = Fraction(theta * radius * radius, 360).limit_denominator()
        ans = f"Sector area = {fmt_frac(area_frac)} pi square units."
        exp = (
            "A sector is a fraction of a full circle determined by the central angle. "
            f"The fraction is {theta}/360. The full circle area is pi({radius})^2 = {radius * radius}pi. "
            f"So the sector area is ({theta}/360)({radius * radius}pi) = {fmt_frac(area_frac)}pi. "
            "The same fraction idea can also be used for arc length."
        )
        body = (
            svg_circle(180, 130, 82, "#2563eb", "#eff6ff", 2.2)
            + "\n  "
            + svg_line(180, 130, 262, 130, "#1d4ed8", 2)
            + "\n  "
            + svg_line(180, 130, 225, 62, "#1d4ed8", 2)
            + "\n  "
            + svg_text(210, 118, f"{theta} deg", 12)
            + "\n  "
            + svg_text(224, 143, f"r={radius}", 12)
        )
        svg = svg_base("Sector area", body)
        return make_problem(pid, 7, number, "G.C.6", "Sector area", "computation", difficulty, q, ans, exp, svg, "Circle sector with radius and central angle.")
    if template == 5:
        radius = 4 + variant
        q = f"Give an informal dissection argument for why the area of a circle of radius {radius} is pi r^2."
        ans = f"The area is pi({radius})^2 = {radius * radius}pi square units."
        exp = (
            "Cut the circle into many thin sectors and rearrange them alternating up and down. "
            "The rearranged shape approaches a parallelogram or rectangle. Its height approaches r, and its base approaches half the circumference, pi r. "
            f"So the area approaches (pi r)(r) = pi r^2; for r = {radius}, that is {radius * radius}pi."
        )
        proof = (
            "As the number of sectors increases, the curved edges of the rearranged sectors become nearly straight. "
            "The top and bottom together contain the full circumference 2pi r, so one base length is pi r. "
            "The sector radius becomes the height r. The limiting rectangle therefore has area pi r times r, or pi r^2."
        )
        body = svg_circle(125, 130, 70, "#2563eb", "#eff6ff", 2.2)
        body += "\n  " + svg_polygon([(220, 175), (310, 175), (295, 85), (205, 85)], "#0f766e", "#ccfbf1", 2)
        body += "\n  " + svg_text(125, 220, "circle sectors", 12) + "\n  " + svg_text(258, 220, "rearranged", 12)
        svg = svg_base("Circle area dissection", body)
        return make_problem(pid, 7, number, "G.GMD.1", "Informal area derivation", "proof", difficulty, q, ans, exp, svg, "Circle sectors rearranged into a rectangle-like shape.", True, proof)
    if template == 6:
        radius, height = 3 + variant, 8 + variant
        sa = 2 * math.pi * radius * radius + 2 * math.pi * radius * height
        q = f"Find the surface area of a closed cylinder with radius {radius} and height {height}. Give the exact answer in terms of pi."
        ans = f"Surface area = {2 * radius * radius + 2 * radius * height}pi square units."
        exp = (
            "A closed cylinder has two circular bases and one rectangular lateral surface when unwrapped. "
            f"The two bases contribute 2pi r^2 = 2pi({radius})^2 = {2 * radius * radius}pi. "
            f"The lateral area is circumference times height: 2pi({radius})({height}) = {2 * radius * height}pi. "
            f"Adding gives {2 * radius * radius + 2 * radius * height}pi square units."
        )
        svg = solid_svg("Cylinder surface area", [(180, 55, f"r={radius}"), (272, 135, f"h={height}")], "cylinder")
        return make_problem(pid, 7, number, "G.MG.1", "Surface area", "computation", difficulty, q, ans, exp, svg, "Cylinder with radius and height.")
    if template == 7:
        radius, height = 3 + variant, 6 + variant
        vol = Fraction(radius * radius * height, 3)
        q = f"Find the volume of a cone with radius {radius} and height {height}. Give the exact answer in terms of pi."
        ans = f"Volume = {fmt_frac(vol)}pi cubic units."
        exp = (
            "A cone has one-third the volume of a cylinder with the same base area and height. "
            f"The base area is pi({radius})^2 = {radius * radius}pi. "
            f"Use V = 1/3 pi r^2 h = 1/3({radius * radius})({height})pi = {fmt_frac(vol)}pi. "
            "The cubic units come from multiplying area by height."
        )
        svg = solid_svg("Cone volume", [(180, 213, f"r={radius}"), (205, 120, f"h={height}")], "cone")
        return make_problem(pid, 7, number, "G.GMD.1", "Volume", "computation", difficulty, q, ans, exp, svg, "Cone with radius and height.")
    if template == 8:
        base_area = 20 + 2 * variant
        height = 5 + variant
        vol = base_area * height
        q = f"Two prisms have equal heights of {height} and every cross-section parallel to the bases has area {base_area}. Use Cavalieri's Principle to compare their volumes."
        ans = f"The volumes are equal; each volume is {vol} cubic units."
        exp = (
            "Cavalieri's Principle says that solids with equal heights and equal corresponding cross-sectional areas have equal volumes. "
            f"Here each matching cross-section has area {base_area}, and the heights are both {height}. "
            f"So each volume is base-area times height: {base_area} x {height} = {vol}. "
            "The shape can lean or shift, but equal cross-sections at every height preserve volume."
        )
        proof = (
            "Imagine slicing both solids into many very thin layers parallel to the bases. "
            "At each height, the two slices have equal area and the same thickness, so corresponding slice volumes are equal. "
            "Adding all corresponding slices, or taking the limiting sum, gives equal total volumes."
        )
        svg = solid_svg("Cavalieri's Principle", [(115, 205, "solid A"), (245, 205, "solid B"), (180, 45, f"h={height}")], "pyramid")
        return make_problem(pid, 7, number, "G.GMD.2", "Cavalieri's Principle", "proof", difficulty, q, ans, exp, svg, "Two solids with matching cross-sections.", True, proof)
    if template == 9:
        volume = 100 + 10 * variant
        mass = 250 + 15 * variant
        density = Fraction(mass, volume).limit_denominator()
        q = f"An object has mass {mass} g and volume {volume} cubic cm. Find its density."
        ans = f"Density = {fmt_frac(density)} g/cubic cm, or about {fmt_float(float(density), 2)} g/cubic cm."
        exp = (
            "Density is mass divided by volume. "
            f"Substitute the values: density = {mass}/{volume}. "
            f"That fraction simplifies to {fmt_frac(density)}, which is approximately {fmt_float(float(density), 2)}. "
            "The units are grams per cubic centimeter because mass is measured in grams and volume in cubic centimeters."
        )
        svg = solid_svg("Density model", [(180, 215, f"V={volume} cm^3"), (180, 50, f"m={mass} g")], "cylinder")
        return make_problem(pid, 7, number, "G.MG.2", "Density", "application", difficulty, q, ans, exp, svg, "Object modeled as a cylinder with mass and volume labels.")
    panel_w, panel_h = 8 + variant, 5 + variant
    border = 1 + (variant % 3)
    total_area = (panel_w + 2 * border) * (panel_h + 2 * border)
    q = f"A rectangular sign face is {panel_w} ft by {panel_h} ft and needs a uniform border {border} ft wide. Find the total area including the border."
    ans = f"Total area = {total_area} square ft."
    exp = (
        "A uniform border adds the border width to both sides in each dimension. "
        f"The total width is {panel_w} + 2({border}) = {panel_w + 2 * border}, and the total height is {panel_h} + 2({border}) = {panel_h + 2 * border}. "
        f"Area is width times height: {panel_w + 2 * border} x {panel_h + 2 * border} = {total_area}. "
        "This is a design-modeling problem because the diagram helps account for both left/right and top/bottom border widths."
    )
    body = svg_polygon([(80, 70), (280, 70), (280, 205), (80, 205)], "#2563eb", "#dbeafe", 2.2)
    body += "\n  " + svg_polygon([(115, 100), (245, 100), (245, 175), (115, 175)], "#0f766e", "#ffffff", 2)
    body += "\n  " + svg_text(180, 55, f"border {border} ft") + "\n  " + svg_text(180, 142, f"{panel_w} ft by {panel_h} ft")
    svg = svg_base("Design area with border", body)
    return make_problem(pid, 7, number, "G.MG.3", "Design modeling", "application", difficulty, q, ans, exp, svg, "Rectangular sign with uniform border.")


def circles(pid: str, number: int, variant: int, template: int, difficulty: str) -> dict:
    if template == 1:
        h, k, r = variant - 5, 3 - variant % 6, 3 + variant
        q = f"Write the equation of the circle with center ({h}, {k}) and radius {r}."
        ans = f"{circle_equation(h, k, r * r)}."
        exp = (
            "The standard circle equation is (x - h)^2 + (y - k)^2 = r^2, where (h, k) is the center and r is the radius. "
            f"Here h = {h}, k = {k}, and r = {r}. "
            f"Substitute those values and square the radius: r^2 = {r*r}. "
            "The signs inside the parentheses are opposite the signs of the center coordinates."
        )
        svg = coordinate_svg("Circle equation", {"O": (h, k)}, circles=[("O", r)], scale=14)
        return make_problem(pid, 8, number, "G.GPE.1", "Equation of a circle", "computation", difficulty, q, ans, exp, svg, "Circle on a coordinate plane.")
    if template == 2:
        h, k, r2 = 2 - variant % 4, variant % 5 - 2, (variant + 3) ** 2
        q = f"A circle has equation {circle_equation(h, k, r2)}. Identify the center and radius."
        ans = f"Center = ({h}, {k}); radius = {int(math.sqrt(r2))}."
        exp = (
            "Compare the equation to standard form (x - h)^2 + (y - k)^2 = r^2. "
            f"The center is ({h}, {k}) because those are the h and k values. "
            f"The radius is the square root of {r2}, which is {int(math.sqrt(r2))}. "
            "Do not report r^2 as the radius; the radius is the positive square root."
        )
        svg = coordinate_svg("Read circle equation", {"O": (h, k)}, circles=[("O", int(math.sqrt(r2)))], scale=12)
        return make_problem(pid, 8, number, "G.GPE.1", "Graphing circles from equations", "computation", difficulty, q, ans, exp, svg, "Circle with center and radius on coordinate plane.")
    if template == 3:
        center = (0, 0)
        r = 5 + variant % 4
        p = (r - 1, 2)
        dist2 = p[0] ** 2 + p[1] ** 2
        status = "inside" if dist2 < r * r else "outside" if dist2 > r * r else "on"
        q = f"Circle O has center (0, 0) and radius {r}. Determine whether P{p} is inside, outside, or on the circle."
        ans = f"P is {status} the circle."
        exp = (
            "Compare the squared distance from the center to the squared radius to avoid unnecessary square roots. "
            f"OP^2 = {p[0]}^2 + {p[1]}^2 = {dist2}. The radius squared is {r}^2 = {r*r}. "
            f"Since {dist2} is {'less than' if dist2 < r*r else 'greater than' if dist2 > r*r else 'equal to'} {r*r}, P is {status} the circle."
        )
        svg = coordinate_svg("Point position relative to circle", {"O": center, "P": p}, segments=[("O", "P")], circles=[("O", r)], scale=16)
        return make_problem(pid, 8, number, "G.GPE.6", "Point location relative to circle", "conceptual", difficulty, q, ans, exp, svg, "Circle with a point and radius segment.")
    if template == 4:
        p = (3, 4)
        radius_slope = Fraction(p[1], p[0])
        tangent_slope = Fraction(-1, 1) / radius_slope
        b = Fraction(p[1]) - tangent_slope * p[0]
        q = f"A circle is centered at the origin and passes through P{p}. Find the equation of the tangent line at P."
        ans = f"Tangent line: {line_equation(tangent_slope, b)}."
        exp = (
            "A radius to a point of tangency is perpendicular to the tangent line. "
            f"The slope of OP is {p[1]}/{p[0]} = {fmt_frac(radius_slope)}. "
            f"The tangent slope is the negative reciprocal, {fmt_frac(tangent_slope)}. "
            f"Using point P in y = mx + b gives b = {p[1]} - ({fmt_frac(tangent_slope)})({p[0]}) = {fmt_frac(b)}, so the tangent is {line_equation(tangent_slope, b)}."
        )
        proof = (
            "The tangent to a circle at a point is perpendicular to the radius drawn to that point. "
            "Since OP is a radius and P is the point of tangency, any tangent line at P must have slope equal to the negative reciprocal of the radius slope. "
            "The point-slope calculation then gives the unique tangent line through P."
        )
        svg = circle_diagram_svg("Tangent line", [(247, 78, "P(3,4)"), (295, 95, "tangent")], tangent=True)
        return make_problem(pid, 8, number, "G.GPE.6", "Tangent line to a circle", "proof", difficulty, q, ans, exp, svg, "Circle with radius to tangent point and tangent line.", True, proof)
    if template == 5:
        central = 60 + 4 * variant
        inscribed = Fraction(central, 2)
        q = f"An inscribed angle intercepts the same arc as a central angle measuring {central} degrees. Find the inscribed angle."
        ans = f"Inscribed angle = {fmt_frac(inscribed)} degrees."
        exp = (
            "An inscribed angle measures half the measure of its intercepted arc. "
            "A central angle has the same measure as its intercepted arc. "
            f"So the inscribed angle is {central}/2 = {fmt_frac(inscribed)} degrees. "
            "This half-angle relationship is one of the core angle relationships in circles."
        )
        svg = circle_diagram_svg("Inscribed angle", [(180, 118, f"central {central}"), (120, 70, "inscribed")])
        return make_problem(pid, 8, number, "G.C.2", "Inscribed and central angles", "computation", difficulty, q, ans, exp, svg, "Circle with central and inscribed angles.")
    if template == 6:
        outside, whole = 4 + variant, 12 + 2 * variant
        tangent = math.sqrt(outside * whole)
        q = f"From an external point, a secant has external part {outside} and whole length {whole}. Find the tangent length to the nearest tenth."
        ans = f"Tangent length = {fmt_float(tangent, 1)}."
        exp = (
            "Use the tangent-secant theorem: tangent^2 = external part x whole secant. "
            f"Substitute the values: tangent^2 = {outside} x {whole} = {outside * whole}. "
            f"Take the positive square root because length is positive: tangent = {fmt_float(tangent, 1)}. "
            "This relationship connects segments drawn from the same external point."
        )
        svg = circle_diagram_svg("Tangent-secant theorem", [(300, 120, f"external {outside}"), (245, 188, f"whole {whole}")], tangent=True)
        return make_problem(pid, 8, number, "G.C.2", "Segments in circles", "computation", difficulty, q, ans, exp, svg, "Circle with tangent and secant from an external point.")
    if template == 7:
        q = "A quadrilateral is inscribed in a circle. Prove that its opposite angles are supplementary."
        ans = "Opposite angles of a cyclic quadrilateral sum to 180 degrees."
        exp = (
            "Each angle of an inscribed quadrilateral intercepts an arc of the circle. "
            "Opposite angles intercept arcs that together make the whole circle. "
            "Because an inscribed angle is half its intercepted arc, the two opposite angles add to half of 360 degrees, which is 180 degrees."
        )
        proof = (
            "Let ABCD be cyclic. Angle A intercepts arc BCD, and angle C intercepts arc DAB. "
            "Those two arcs together measure 360 degrees. By the inscribed angle theorem, m angle A = 1/2 m arc BCD and m angle C = 1/2 m arc DAB. "
            "Adding gives m angle A + m angle C = 1/2(360) = 180. The same reasoning applies to angles B and D."
        )
        svg = circle_diagram_svg("Cyclic quadrilateral proof", [(110, 78, "A"), (246, 80, "B"), (246, 185, "C"), (110, 185, "D")])
        return make_problem(pid, 8, number, "G.C.3", "Inscribed polygon properties", "proof", difficulty, q, ans, exp, svg, "Quadrilateral inscribed in a circle.", True, proof)
    if template == 8:
        r1, r2 = 3 + variant, 7 + variant
        scale = Fraction(r2, r1)
        q = f"Prove that a circle of radius {r1} is similar to a circle of radius {r2}."
        ans = f"The circles are similar by a dilation with scale factor {fmt_frac(scale)}."
        exp = (
            "All circles have the same shape; only their radii can differ. "
            f"A dilation centered at the first circle's center with scale factor {fmt_frac(scale)} multiplies radius {r1} by {fmt_frac(scale)} to get {r2}. "
            "The image of every point at distance r1 from the center is a point at distance r2 from the center, forming the second circle."
        )
        proof = (
            f"Let circle C1 have center O and radius {r1}. Dilate from O by scale factor {fmt_frac(scale)}. "
            f"Any point P on C1 satisfies OP = {r1}; its image P' satisfies OP' = {fmt_frac(scale)} x {r1} = {r2}. "
            f"Thus the image set is exactly the circle with center O and radius {r2}. Since a dilation is a similarity transformation, the two circles are similar."
        )
        svg = circle_diagram_svg("All circles are similar", [(125, 220, f"r={r1}"), (235, 220, f"r={r2}")], chord=False)
        return make_problem(pid, 8, number, "G.C.1", "Circle similarity proof", "proof", difficulty, q, ans, exp, svg, "Two circles with different radii.", True, proof)
    if template == 9:
        sides = 6 if variant % 2 else 4
        q = f"Describe how to construct a regular {sides}-gon inscribed in a circle."
        if sides == 6:
            ans = "Keep the compass set to the radius and step that length around the circle to mark six vertices, then connect consecutive vertices."
            exp = (
                "In a circle, six radius-length chords fit exactly around the circumference because a central angle of 60 degrees creates an equilateral triangle with two radii and the chord. "
                "Set the compass to the circle radius, mark consecutive points around the circle, and connect them. "
                "The six equal chords produce a regular hexagon."
            )
            proof = (
                "Each marked chord equals the radius. With two radii to adjacent marked points, each small triangle has three congruent sides and is equilateral. "
                "Therefore each central angle is 60 degrees, and six such angles complete 360 degrees. The chords and arcs are equal, so the hexagon is regular."
            )
        else:
            ans = "Construct two perpendicular diameters, then connect the four endpoints in order."
            exp = (
                "Perpendicular diameters divide the circle into four equal central angles of 90 degrees. "
                "Connecting adjacent endpoints creates four congruent chords. "
                "Equal arcs and equal chords give a square inscribed in the circle."
            )
            proof = (
                "The perpendicular diameters create four congruent central angles. Equal central angles intercept equal arcs and equal chords, so all four sides are congruent. "
                "Each inscribed angle intercepting a diameter is a right angle, so the quadrilateral has four right angles. It is a square."
            )
        body = svg_circle(180, 130, 82, "#2563eb", "#eff6ff", 2.2)
        pts = []
        for k in range(sides):
            theta = -math.pi / 2 + 2 * math.pi * k / sides
            pts.append((180 + 82 * math.cos(theta), 130 + 82 * math.sin(theta)))
        body += "\n  " + svg_polygon(pts, "#0f766e", "none", 2.2)
        svg = svg_base("Inscribed regular polygon construction", body)
        return make_problem(pid, 8, number, "G.CO.12", "Circle constructions", "construction", difficulty, q, ans, exp, svg, "Regular polygon inscribed in a circle.", True, proof)
    h, k, r = variant - 4, variant % 5 - 2, 5 + variant % 4
    q = f"Derive the equation of a circle with center ({h}, {k}) and radius {r} using the Pythagorean Theorem."
    ans = f"{circle_equation(h, k, r * r)}."
    exp = (
        "Take any point (x, y) on the circle. The horizontal distance from the center to the point is x - h, and the vertical distance is y - k. "
        "Those distances form the legs of a right triangle whose hypotenuse is the radius. "
        f"By the Pythagorean Theorem, {circle_equation(h, k, r * r)}, which is the standard circle equation."
    )
    proof = (
        f"Let P(x, y) be on the circle centered at C({h}, {k}) with radius {r}. Draw horizontal and vertical segments from C and P to form a right triangle. "
        f"The leg lengths correspond to the squared terms {circle_term('x', h)} and {circle_term('y', k)}, and the hypotenuse CP is {r}. "
        f"Using a^2 + b^2 = c^2 gives {circle_equation(h, k, r * r)}, exactly the equation of the circle."
    )
    svg = coordinate_svg("Deriving circle equation", {"C": (h, k), "P": (h + r, k)}, segments=[("C", "P")], circles=[("C", r)], scale=13)
    return make_problem(pid, 8, number, "G.GPE.2", "Deriving circle equations", "proof", difficulty, q, ans, exp, svg, "Circle with radius triangle used for Pythagorean derivation.", True, proof)


UNIT_GENERATORS = {
    1: foundations,
    2: transformations,
    3: triangles,
    4: quadrilaterals,
    5: similarity,
    6: right_triangles,
    7: area_volume,
    8: circles,
}


def build() -> dict:
    for directory in (IMAGE_DIR, LEGACY_VISUAL_DIR):
        if directory.exists():
            shutil.rmtree(directory)
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    problems: list[dict] = []
    for unit in range(1, 9):
        unit_dir = IMAGE_DIR / f"unit_{unit:02d}"
        unit_dir.mkdir(parents=True, exist_ok=True)
        generator = UNIT_GENERATORS[unit]
        for number in range(1, 101):
            template = ((number - 1) % 10) + 1
            variant = ((number - 1) // 10) + 1
            pid = f"HG-U{unit:02d}-{number:03d}"
            problem = generator(pid, number, variant, template, difficulty_for(number))
            svg = problem.pop("_svg")
            visual_path = unit_dir / f"{pid}.png"
            render_diagram_png(svg, visual_path)
            problem["visual_path"] = visual_path.relative_to(DATA_DIR).as_posix()
            problem["visual_mime_type"] = "image/png"
            problems.append(problem)

    return {
        "metadata": {
            "title": "Honors Geometry 800 Problem Database",
            "generated_on": date.today().isoformat(),
            "source_pdf": "hshonorsgeometryally.pdf",
            "source_note": (
                "The source PDF is a Blue Valley Schools Honors Geometry curriculum outline. "
                "Problems are original generated practice items aligned to the PDF's units, guiding questions, and standards."
            ),
            "problem_count": len(problems),
            "problems_per_unit": 100,
            "visual_policy": "Every generated problem includes a PNG bitmap image asset and alt text; no vector diagram assets are published.",
            "image_generation_mode": "Project-local imagegen bitmap renderer for exact geometry diagrams.",
            "proof_policy": "Each unit includes proof-required problems with complete proof solutions.",
            "difficulty_levels": ["easy", "moderate", "challenging", "honors"],
            "units": [
                {
                    "unit": unit,
                    "title": spec["title"],
                    "essential_question": spec["essential_question"],
                    "standards": spec["standards"],
                    "source_alignment": spec["source_alignment"],
                }
                for unit, spec in UNITS.items()
            ],
        },
        "schema": {
            "id": "Stable problem id HG-U##-###.",
            "unit": "Integer unit number 1 through 8.",
            "standard": "Primary aligned geometry standard from the PDF.",
            "topic": "Curriculum topic.",
            "difficulty": "easy, moderate, challenging, or honors.",
            "problem_type": "computation, conceptual, proof, construction, or application.",
            "question": "Student-facing problem statement.",
            "answer": "Concise final answer.",
            "explanation": "Step-by-step explanation.",
            "proof_required": "True when a formal or informal proof is requested.",
            "proof": "Proof solution when proof_required is true.",
            "visual_path": "Relative path from data/ to the PNG image.",
            "visual_mime_type": "MIME type for the image asset.",
            "visual_alt_text": "Text description of the visual.",
        },
        "problems": problems,
    }


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    database = build()
    OUTPUT.write_text(json.dumps(database, indent=2, ensure_ascii=True), encoding="utf-8")
    JS_OUTPUT.write_text(
        "window.HONORS_GEOMETRY_DATABASE = "
        + json.dumps(database, ensure_ascii=True, separators=(",", ":"))
        + ";\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUTPUT}")
    print(f"Wrote {JS_OUTPUT}")
    print(f"Problems: {len(database['problems'])}")
    print(f"Images: {len(list(IMAGE_DIR.glob('**/*.png')))}")


if __name__ == "__main__":
    main()
