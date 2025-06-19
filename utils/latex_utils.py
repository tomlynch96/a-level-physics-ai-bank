from pylatex import Document, Section, Enumerate, NoEscape, Math, Command
from pylatex.utils import escape_latex as pylatex_escape
from io import BytesIO

def escape_latex(text):
    """
    Basic LaTeX escape for PyLaTeX compatibility.
    """
    if not isinstance(text, str):
        return text
    # You can use pylatex.utils.escape_latex or keep your own
    return pylatex_escape(text)

# def build_pdf(questions):
#     geometry_options = {"margin": "1in"}
#     doc = Document(geometry_options=geometry_options)
#     doc.preamble.append(Command('title', 'Physics Worksheet'))
#     doc.preamble.append(Command('date', NoEscape(r'\today')))
#     doc.append(NoEscape(r'\maketitle'))

#     with doc.create(Section('Questions')):
#         with doc.create(Enumerate()) as enum:
#             for q in questions:
#                 text = escape_latex(q.get("question_template", ""))
#                 hint = escape_latex(q.get("hint", ""))
#                 explanation = escape_latex(q.get("explanation", ""))
#                 latex_eq = q.get("latex_eq", "")

#                 enum.add_item(text)

#                 if latex_eq:
#                     enum.append(Math(data=[NoEscape(latex_eq)]))

#                 if hint:
#                     enum.append(NoEscape(r'\textbf{Hint:} ' + hint + r'\\'))

#                 if explanation:
#                     enum.append(NoEscape(r'\textbf{Explanation:} ' + explanation))

#     # Create PDF in-memory
#     pdf_bytes = BytesIO()
#     doc.generate_pdf(pdf_bytes, clean_tex=True)
#     pdf_bytes.seek(0)
#     return pdf_bytes

import tempfile
from pylatex import Document, Section, Enumerate, NoEscape, Math, Command
from pylatex.utils import escape_latex as pylatex_escape

def escape_latex(text):
    if not isinstance(text, str):
        return text
    return pylatex_escape(text)

# def build_pdf(questions):
#     geometry_options = {"margin": "1in"}
#     doc = Document(geometry_options=geometry_options)
#     doc.preamble.append(Command('title', 'Physics Worksheet'))
#     doc.preamble.append(Command('date', NoEscape(r'\today')))
#     doc.append(NoEscape(r'\maketitle'))

#     with doc.create(Section('Questions')):
#         with doc.create(Enumerate()) as enum:
#             for q in questions:
#                 text = escape_latex(q.get("question_template", ""))
#                 hint = escape_latex(q.get("hint", ""))
#                 explanation = escape_latex(q.get("explanation", ""))
#                 latex_eq = q.get("latex_eq", "")

#                 enum.add_item(text)

#                 if latex_eq:
#                     enum.append(Math(data=[NoEscape(latex_eq)]))

#                 if hint:
#                     enum.append(NoEscape(r'\textbf{Hint:} ' + hint + r'\\'))

#                 if explanation:
#                     enum.append(NoEscape(r'\textbf{Explanation:} ' + explanation))

#     # Use tempfile to write and read pdf
#     with tempfile.TemporaryDirectory() as tempdir:
#         filepath = f"{tempdir}/worksheet.pdf"
#         doc.generate_pdf(filepath[:-4], clean_tex=True)  # generate_pdf needs filename without extension

#         with open(filepath, "rb") as f:
#             pdf_bytes = f.read()

#     return pdf_bytes
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch
from io import BytesIO
import html

def build_pdf_reportlab(questions):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph("Physics Worksheet", styles['Title']))
    story.append(Spacer(1, 12))

    # Add questions
    for i, q in enumerate(questions, start=1):
        # Escape HTML special chars
        question_text = html.escape(q.get("question_template", ""))
        hint = html.escape(q.get("hint", ""))
        explanation = html.escape(q.get("explanation", ""))

        story.append(Paragraph(f"<b>Q{i}:</b> {question_text}", styles['Normal']))
        story.append(Spacer(1, 6))

        if hint:
            story.append(Paragraph(f"<b>Hint:</b> {hint}", styles['Italic']))
            story.append(Spacer(1, 6))
        if explanation:
            story.append(Paragraph(f"<b>Explanation:</b> {explanation}", styles['Normal']))
            story.append(Spacer(1, 12))

        if i % 5 == 0:
            story.append(PageBreak())

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()
