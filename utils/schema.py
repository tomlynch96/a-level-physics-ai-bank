{
  "question_text": "...",
  "topic": "Kinetic Energy",
  "spec_links": {
    "OCR": "3.2.1",
    "AQA": "4.5.1"
  },
  "difficulty": "medium",
  "variables": {
    "m": {"range": [1, 10], "unit": "kg"},
    "v": {"range": [1, 20], "unit": "m/s"}
  },
  "latex_equation": "E_k = \\frac{1}{2}mv^2",
  "mcq": {
    "question": "...",
    "choices": ["...", "...", "...", "..."],
    "correct": "..."
  },
  "hint": "...",
  "explanation": "...",
  "id": "KE001"
}

def validate_question(q: dict) -> bool:
    required_fields = [
        "question_text", "topic", "difficulty", "spec_links", "variables",
        "latex_equation", "mcq", "hint", "explanation", "id"
    ]
    for field in required_fields:
        if field not in q:
            print(f"Missing: {field}")
            return False
    mcq_fields = ["question", "choices", "correct"]
    for field in mcq_fields:
        if field not in q["mcq"]:
            print(f"Missing MCQ field: {field}")
            return False
    return True
