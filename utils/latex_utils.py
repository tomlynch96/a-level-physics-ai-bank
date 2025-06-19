# from pylatex import Document, Section, Enumerate, NoEscape, Math, Command
# from pylatex.utils import escape_latex as pylatex_escape
# from io import BytesIO

# def escape_latex(text):
#     """
#     Basic LaTeX escape for PyLaTeX compatibility.
#     """
#     if not isinstance(text, str):
#         return text
#     # You can use pylatex.utils.escape_latex or keep your own
#     return pylatex_escape(text)

# # def build_pdf(questions):
# #     geometry_options = {"margin": "1in"}
# #     doc = Document(geometry_options=geometry_options)
# #     doc.preamble.append(Command('title', 'Physics Worksheet'))
# #     doc.preamble.append(Command('date', NoEscape(r'\today')))
# #     doc.append(NoEscape(r'\maketitle'))

# #     with doc.create(Section('Questions')):
# #         with doc.create(Enumerate()) as enum:
# #             for q in questions:
# #                 text = escape_latex(q.get("question_template", ""))
# #                 hint = escape_latex(q.get("hint", ""))
# #                 explanation = escape_latex(q.get("explanation", ""))
# #                 latex_eq = q.get("latex_eq", "")

# #                 enum.add_item(text)

# #                 if latex_eq:
# #                     enum.append(Math(data=[NoEscape(latex_eq)]))

# #                 if hint:
# #                     enum.append(NoEscape(r'\textbf{Hint:} ' + hint + r'\\'))

# #                 if explanation:
# #                     enum.append(NoEscape(r'\textbf{Explanation:} ' + explanation))

# #     # Create PDF in-memory
# #     pdf_bytes = BytesIO()
# #     doc.generate_pdf(pdf_bytes, clean_tex=True)
# #     pdf_bytes.seek(0)
# #     return pdf_bytes

# import tempfile
# from pylatex import Document, Section, Enumerate, NoEscape, Math, Command
# from pylatex.utils import escape_latex as pylatex_escape

# def escape_latex(text):
#     if not isinstance(text, str):
#         return text
#     return pylatex_escape(text)

# # def build_pdf(questions):
# #     geometry_options = {"margin": "1in"}
# #     doc = Document(geometry_options=geometry_options)
# #     doc.preamble.append(Command('title', 'Physics Worksheet'))
# #     doc.preamble.append(Command('date', NoEscape(r'\today')))
# #     doc.append(NoEscape(r'\maketitle'))

# #     with doc.create(Section('Questions')):
# #         with doc.create(Enumerate()) as enum:
# #             for q in questions:
# #                 text = escape_latex(q.get("question_template", ""))
# #                 hint = escape_latex(q.get("hint", ""))
# #                 explanation = escape_latex(q.get("explanation", ""))
# #                 latex_eq = q.get("latex_eq", "")

# #                 enum.add_item(text)

# #                 if latex_eq:
# #                     enum.append(Math(data=[NoEscape(latex_eq)]))

# #                 if hint:
# #                     enum.append(NoEscape(r'\textbf{Hint:} ' + hint + r'\\'))

# #                 if explanation:
# #                     enum.append(NoEscape(r'\textbf{Explanation:} ' + explanation))

# #     # Use tempfile to write and read pdf
# #     with tempfile.TemporaryDirectory() as tempdir:
# #         filepath = f"{tempdir}/worksheet.pdf"
# #         doc.generate_pdf(filepath[:-4], clean_tex=True)  # generate_pdf needs filename without extension

# #         with open(filepath, "rb") as f:
# #             pdf_bytes = f.read()

# #     return pdf_bytes
# # from reportlab.lib.pagesizes import letter
# # from reportlab.pdfgen import canvas
# # from reportlab.lib.styles import getSampleStyleSheet
# # from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
# # from reportlab.lib.units import inch
# # from io import BytesIO
# # import html

# # def build_pdf_reportlab(questions):
# #     buffer = BytesIO()
# #     doc = SimpleDocTemplate(buffer, pagesize=letter,
# #                             rightMargin=72, leftMargin=72,
# #                             topMargin=72, bottomMargin=18)
# #     styles = getSampleStyleSheet()
# #     story = []

# #     # Title
# #     story.append(Paragraph("Physics Worksheet", styles['Title']))
# #     story.append(Spacer(1, 12))

# #     # Add questions
# #     for i, q in enumerate(questions, start=1):
# #         # Escape HTML special chars
# #         question_text = html.escape(q.get("question_template", ""))
# #         hint = html.escape(q.get("hint", ""))
# #         explanation = html.escape(q.get("explanation", ""))

# #         story.append(Paragraph(f"<b>Q{i}:</b> {question_text}", styles['Normal']))
# #         story.append(Spacer(1, 6))

# #         if hint:
# #             story.append(Paragraph(f"<b>Hint:</b> {hint}", styles['Italic']))
# #             story.append(Spacer(1, 6))
# #         if explanation:
# #             story.append(Paragraph(f"<b>Explanation:</b> {explanation}", styles['Normal']))
# #             story.append(Spacer(1, 12))

# #         if i % 5 == 0:
# #             story.append(PageBreak())

# #     doc.build(story)
# #     buffer.seek(0)
# #     return buffer.getvalue()

# # from reportlab.lib.pagesizes import letter
# # from reportlab.pdfgen import canvas
# # from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
# # from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Frame, PageTemplate
# # from reportlab.lib.units import inch
# # from reportlab.lib.enums import TA_CENTER, TA_LEFT
# # from io import BytesIO
# # import html

# # def header_footer(canvas, doc):
# #     canvas.saveState()
# #     width, height = letter
# #     canvas.setFont('Helvetica-Bold', 12)
# #     canvas.drawString(inch, height - 0.75 * inch, "A Level Physics")
# #     canvas.drawRightString(width - inch, height - 0.75 * inch, "Physics Worksheet")
# #     canvas.setFont('Helvetica', 10)
# #     canvas.drawRightString(width - inch, 0.75 * inch, f"Page {doc.page}")
# #     canvas.restoreState()

# # def build_pdf_reportlab(questions):
# #     buffer = BytesIO()
# #     doc = SimpleDocTemplate(buffer, pagesize=letter,
# #                             rightMargin=72, leftMargin=72,
# #                             topMargin=72, bottomMargin=72)

# #     styles = getSampleStyleSheet()
# #     # Customize styles to mimic LaTeX formatting
# #     title_style = ParagraphStyle(
# #         'titleStyle',
# #         parent=styles['Title'],
# #         alignment=TA_CENTER,
# #         spaceAfter=24
# #     )
# #     section_style = ParagraphStyle(
# #         'sectionStyle',
# #         parent=styles['Heading2'],
# #         spaceBefore=12,
# #         spaceAfter=12,
# #         alignment=TA_LEFT
# #     )
# #     question_style = ParagraphStyle(
# #         'questionStyle',
# #         parent=styles['Normal'],
# #         spaceAfter=6,
# #         leftIndent=12
# #     )
# #     hint_style = ParagraphStyle(
# #         'hintStyle',
# #         parent=styles['Italic'],
# #         spaceAfter=6,
# #         leftIndent=24
# #     )
# #     explanation_style = ParagraphStyle(
# #         'explanationStyle',
# #         parent=styles['Normal'],
# #         spaceAfter=12,
# #         leftIndent=24
# #     )

# #     story = []

# #     story.append(Paragraph("Physics Worksheet", title_style))
# #     story.append(Paragraph("Questions", section_style))

# #     for i, q in enumerate(questions, start=1):
# #         question_text = html.escape(q.get("question_template", ""))
# #         hint = html.escape(q.get("hint", ""))
# #         explanation = html.escape(q.get("explanation", ""))
# #         latex_eq = q.get("latex_eq", "")

# #         # Add question number and text
# #         story.append(Paragraph(f"<b>Q{i}:</b> {question_text}", question_style))

# #         # Add equation as plain text (or add images if you want to support math)
# #         if latex_eq:
# #             story.append(Paragraph(f"Equation: {latex_eq}", question_style))

# #         # Add hint and explanation indented
# #         if hint:
# #             story.append(Paragraph(f"Hint: {hint}", hint_style))
# #         if explanation:
# #             story.append(Paragraph(f"Explanation: {explanation}", explanation_style))

# #         if i % 5 == 0:
# #             story.append(PageBreak())

# #     doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
# #     buffer.seek(0)
# #     return buffer.getvalue()

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch
from reportlab.lib.colors import black, HexColor
from io import BytesIO
import html

def build_pdf_reportlab(questions):
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
    story.append(Paragraph("A Level Physics Worksheet", title_style))

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

