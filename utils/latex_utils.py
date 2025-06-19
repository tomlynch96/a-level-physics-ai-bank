from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch
from reportlab.lib.colors import black, HexColor
from io import BytesIO
import html

def build_pdf_reportlab(questions, title="A Level Physics Worksheet"):
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72,
    )

    # Base styles and custom styles
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        name='TitleStyle',
        parent=styles['Title'],
        fontSize=24,
        leading=28,
        alignment=TA_CENTER,
        spaceAfter=24,
    )

    section_style = ParagraphStyle(
        name='SectionStyle',
        parent=styles['Heading2'],
        fontSize=18,
        leading=22,
        spaceBefore=12,
        spaceAfter=12,
        alignment=TA_LEFT,
        textColor=HexColor("#003366"),
    )

    question_style = ParagraphStyle(
        name='QuestionStyle',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        leftIndent=12,
        spaceAfter=6,
    )

    hint_style = ParagraphStyle(
        name='HintStyle',
        parent=styles['Italic'],
        fontSize=11,
        leading=14,
        leftIndent=24,
        textColor=HexColor("#555555"),
        spaceAfter=6,
    )

    explanation_style = ParagraphStyle(
        name='ExplanationStyle',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        leftIndent=24,
        spaceAfter=12,
    )

    story = []

    # Title
    story.append(Paragraph(title, title_style))

    # Section heading
    story.append(Paragraph("Questions", section_style))

    for i, q in enumerate(questions, start=1):
        question_text = html.escape(q.get("question_template", ""))
        hint = html.escape(q.get("hint", ""))
        explanation = html.escape(q.get("explanation", ""))
        latex_eq = q.get("latex_eq", "")

        # Question text with number
        story.append(Paragraph(f"<b>Q{i}:</b> {question_text}", question_style))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()

