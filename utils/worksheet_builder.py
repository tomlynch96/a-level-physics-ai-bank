import random
from copy import deepcopy

def build_question_instance(q):
    """Return a copy of the question with values filled in (if any)."""
    instance = deepcopy(q)
    instance["question_text"] = instance["question_template"]
    return instance

def get_linked_mcq(q):
    """Return the independently authored MCQ testing the same idea."""
    return {
        "text": q['mcq']['question'],
        "options": q['mcq']['options'],
        "correct": q['mcq']['correct'],
        "explanation": q['mcq'].get('explanation', '')
    }

