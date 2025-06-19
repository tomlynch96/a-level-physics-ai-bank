import os
import subprocess
from io import BytesIO

def escape_latex(text):
    if not isinstance(text, str):
        return text
    replacements = {
        "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
        "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}",
        "^": r"\^{}", "\\": r"\textbackslash{}"
    }
    for original, escaped in replacements.items():
        text = text.replace(original, escaped)
    return text

def build_latex_content(questions):
    entries = []
    for q in questions:
        text = escape_latex(q["question_text"])
        hint = escape_latex(q.get("hint", ""))
        explanation = escape_latex(q.get("explanation", ""))
        eq = q.get("latex_eq", "")

        block = f"\\item {text}\n"
        if eq:
            block += f"\\[\n{eq}\n\\]\n"
        if hint:
            block += f"\\textbf{{Hint:}} {hint} \\\\\n"
        if explanation:
            block += f"\\textbf{{Explanation:}} {explanation}\n"

        entries.append(block)

    return "\n\n".join(entries)

def compile_pdf_from_latex(template_path, latex_content):
    with open(template_path, "r") as f:
        template = f.read()

    filled = template.replace("%__QUESTIONS__", latex_content)

    with open("worksheet.tex", "w") as f:
        f.write(filled)

    subprocess.run(["pdflatex", "-interaction=nonstopmode", "worksheet.tex"], check=True)

    with open("worksheet.pdf", "rb") as f:
        return BytesIO(f.read())
