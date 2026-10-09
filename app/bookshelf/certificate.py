"""The printable PDF certificate for reaching a reading milestone."""

import io

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


def _draw_star(c, cx, cy, size, fill_color):
    """Draw a simple 5-point star centered at (cx, cy)."""
    import math
    points = []
    for i in range(10):
        angle = math.pi / 2 + i * math.pi / 5
        r = size if i % 2 == 0 else size * 0.4
        points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))

    c.setFillColor(fill_color)
    c.setStrokeColor(fill_color)
    path = c.beginPath()
    path.moveTo(*points[0])
    for x, y in points[1:]:
        path.lineTo(x, y)
    path.close()
    c.drawPath(path, fill=1, stroke=0)

def _draw_trophy(c, cx, cy, size, fill_color, outline_color=None):
    """Draw a simple trophy centered at (cx, cy). `size` controls overall scale."""
    from reportlab.lib.colors import HexColor

    outline_color = outline_color or fill_color
    c.setFillColor(fill_color)
    c.setStrokeColor(outline_color)

    cup_w = size * 1.1
    cup_h = size * 1.0
    stem_w = size * 0.22
    stem_h = size * 0.35
    base_w = size * 1.0
    base_h = size * 0.18

    # Cup body (rounded rect)
    c.roundRect(cx - cup_w / 2, cy, cup_w, cup_h, size * 0.25, fill=1, stroke=0)

    # Handles (two arcs, drawn as open bezier-ish curves via ellipse halves)
    handle_r = size * 0.32
    c.setLineWidth(size * 0.12)
    c.setStrokeColor(fill_color)
    c.ellipse(cx - cup_w / 2 - handle_r, cy + cup_h * 0.15,
              cx - cup_w / 2 + handle_r * 0.3, cy + cup_h * 0.75,
              fill=0, stroke=1)
    c.ellipse(cx + cup_w / 2 - handle_r * 0.3, cy + cup_h * 0.15,
              cx + cup_w / 2 + handle_r, cy + cup_h * 0.75,
              fill=0, stroke=1)

    # Stem
    c.setFillColor(fill_color)
    c.rect(cx - stem_w / 2, cy - stem_h, stem_w, stem_h, fill=1, stroke=0)

    # Base
    c.roundRect(cx - base_w / 2, cy - stem_h - base_h, base_w, base_h, size * 0.06, fill=1, stroke=0)



def make_certificate(name, milestone, today):
    """Returns (BytesIO of the PDF, download filename)."""
    name = name or "Reader"
    buffer = io.BytesIO()
    page_size = landscape(A4)
    c = canvas.Canvas(buffer, pagesize=page_size)
    width, height = page_size

    # Palette — bright and friendly
    gold = HexColor("#F5A623")
    teal = HexColor("#2FB6A9")
    coral = HexColor("#FF6F61")
    purple = HexColor("#8E6FD8")
    navy = HexColor("#2E3A59")
    star_colors = [gold, teal, coral, purple]

    # Background
    c.setFillColor(HexColor("#FFFBF2"))
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Decorative border (double rounded rect)
    margin = 24
    c.setStrokeColor(teal)
    c.setLineWidth(6)
    c.roundRect(margin, margin, width - 2 * margin, height - 2 * margin, 24, fill=0, stroke=1)
    c.setStrokeColor(gold)
    c.setLineWidth(2)
    c.roundRect(margin + 10, margin + 10, width - 2 * (margin + 10), height - 2 * (margin + 10), 18, fill=0, stroke=1)

    # Scattered stars along the top and bottom
    star_positions = [
        # 2 stars on the left side (vertically stacked, mid-height)
        (60, height / 2 - 70),
        (60, height / 2 + 70),

        # 2 stars on the right side (mirrored)
        (width - 60, height / 2 - 70),
        (width - 60, height / 2 + 70),

        # 4 stars along the bottom
        (85, height - 95),
        (width / 2 - 160, height - 55),
        (width / 2 + 160, height - 55),
        (width - 85, height - 95),

        # 4 stars along the top (mirrored y of bottom row)
        (85, 95),
        (width / 2 - 160, 55),
        (width / 2 + 160, 55),
        (width - 85, 95),
    ]
    for i, (sx, sy) in enumerate(star_positions):
        _draw_star(c, sx, sy, 14, star_colors[i % len(star_colors)])

    # Title
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 42)
    title = "Certificate of Achievement"
    c.drawCentredString(width / 2, height - 150, title)

    # Trophy above the title
    _draw_trophy(c, width / 2, height - 200, 22, gold)

    # Subtitle
    c.setFont("Helvetica", 22)
    c.setFillColor(navy)
    c.drawCentredString(width / 2, height - 250, "This is a certificate for")

    # Name
    c.setFont("Helvetica-Bold", 36)
    c.setFillColor(coral)
    c.drawCentredString(width / 2, height - 310, name)
    c.setLineWidth(1)
    c.setStrokeColor(navy)
    line_w = stringWidth(name, "Helvetica", 12) + 40
    c.line(width / 2 - line_w / 2, 80, width / 2 + line_w / 2, 80)

    # Achievement line
    c.setFont("Helvetica", 20)
    c.setFillColor(navy)
    achievement_text = f"For a wonderful love of reading and the curiosity to explore {milestone} book{'s' if milestone != 1 else ''}!"
    c.drawCentredString(width / 2, height - 355, achievement_text)

    # Encouraging line
    c.setFont("Helvetica-BoldOblique", 14)
    c.setFillColor(teal)

    lines = [
    "You've shown real dedication and a love of stories.",
    "Every book you read makes your imagination even bigger.",
    "We're so proud of you!",
    ]

    line_height = 22  # spacing between lines, in points — adjust to taste
    start_y = height - 410

    for i, line in enumerate(lines):
        c.drawCentredString(width / 2, start_y - (i * line_height), line)
    
    # Date, bottom center
    c.setFont("Helvetica", 12)
    c.setFillColor(navy)
    today_str = f"{today.day} {today.strftime('%B %Y')}"
    c.drawCentredString(width / 2, 90, today_str)
    c.setLineWidth(1)
    c.setStrokeColor(navy)
    line_w = stringWidth(today_str, "Helvetica", 12) + 40
    c.line(width / 2 - line_w / 2, 80, width / 2 + line_w / 2, 80)

    c.showPage()
    c.save()
    buffer.seek(0)

    safe = "".join(ch if ch.isalnum() else "_" for ch in name)
    return buffer, f"{safe}_certificate_{milestone}_books.pdf"
