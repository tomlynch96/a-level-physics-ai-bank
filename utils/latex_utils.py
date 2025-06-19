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
    for i, q in enumerate(questions):
        try:
            text = escape_latex(q["question_template"])  # updated from 'question_text'
        except KeyError:
            print(f"⚠️ Skipping question {i}: missing 'question_template'")
            continue

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
