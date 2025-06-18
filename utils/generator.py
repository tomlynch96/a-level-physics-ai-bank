import uuid

def generate_sample_question():
    return {
        "question_text": "Calculate the kinetic energy of a 4kg object moving at 3m/s.",
        "topic": "Kinetic Energy",
        "spec_links": {
            "OCR": "3.2.1",
            "AQA": "4.5.1"
        },
        "difficulty": "easy",
        "variables": {
            "m": {"range": [1, 10], "unit": "kg"},
            "v": {"range": [1, 20], "unit": "m/s"}
        },
        "latex_equation": "E_k = \\frac{1}{2}mv^2",
        "mcq": {
            "question": "Which factor affects kinetic energy most?",
            "choices": ["Mass", "Velocity", "Time", "Force"],
            "correct": "Velocity"
        },
        "hint": "Use the kinetic energy equation.",
        "explanation": "KE is proportional to the square of velocity.",
        "id": f"KE_{uuid.uuid4().hex[:6]}"
    }
