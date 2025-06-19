def escape_latex(text):
    """
    Escapes LaTeX special characters in a text string.
    """
    if not isinstance(text, str):
        return text  # Ignore non-strings (e.g. None)

    replacements = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\^{}",
        "\\": r"\textbackslash{}",
    }

    for original, escaped in replacements.items():
        text = text.replace(original, escaped)

    return text
