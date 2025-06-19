import streamlit as st
import json
import random
from utils.worksheet_builder import build_question_instance, get_linked_mcq
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from utils.latex_utils import build_pdf_reportlab

def generate_pdf(worksheet_text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 50
    for line in worksheet_text.split('\n'):
        c.drawString(40, y, line)
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50
    c.save()
    buffer.seek(0)
    return buffer


# Load question bank
with open("data/questions.json") as f:
    questions = json.load(f)

st.title("Physics Worksheet Generator")

# Select topic and worksheet difficulty
topics = sorted(set(q['topic'] for q in questions))
selected_topic = st.selectbox("Choose topic:", topics)
difficulty = st.selectbox("Overall worksheet difficulty:", ["Easy", "Medium", "Hard"])
worksheet_type = st.radio("Worksheet type:", ["Free Response", "MCQ Follow-up", "Both"])
num_questions = st.slider("Number of questions", 1, 10, 3)
title = st.text_input("Enter the worksheet title", value="A Level Physics Worksheet")

# Difficulty mix based on overall level
difficulty_mix = {
    "Easy": {"Easy": 0.75, "Medium": 0.25},
    "Medium": {"Easy": 0.25, "Medium": 0.5, "Hard": 0.25},
    "Hard": {"Medium": 0.25, "Hard": 0.75}
}

mix = difficulty_mix[difficulty]
by_difficulty = {d: [q for q in questions if q["topic"] == selected_topic and q["difficulty"] == d] for d in mix}
counts = {d: int(num_questions * mix[d]) for d in mix}

# Top-up to match total (due to rounding)
total = sum(counts.values())
remaining = num_questions - total
sorted_diffs = sorted(mix.items(), key=lambda x: x[1], reverse=True)  # prioritise largest proportion
for d, _ in sorted_diffs:
    if remaining == 0:
        break
    if len(by_difficulty[d]) > counts[d]:
        counts[d] += 1
        remaining -= 1

# Sample questions
final_sample = []
for d in counts:
    final_sample.extend(random.sample(by_difficulty[d], min(counts[d], len(by_difficulty[d]))))

random.shuffle(final_sample)

# Display questions
if not final_sample:
    st.warning("No questions available for this topic and difficulty.")
else:
    st.subheader("Generated Worksheet")
    worksheet_text = ""

    for i, q in enumerate(final_sample):
        instance = build_question_instance(q)

        if worksheet_type in ["Free Response", "Both"]:
            st.markdown(f"### Q{i+1}: Free Response")
            st.markdown(instance["question_text"])
            # latex_eq intentionally excluded here
            with st.expander("Hint"):
                st.markdown(instance["hint"])
            with st.expander("Explanation"):
                st.markdown(instance["explanation"])

            worksheet_text += f"Q{i+1}: {instance['question_text']}\n"
            worksheet_text += f"Hint: {instance['hint']}\n"
            worksheet_text += f"Explanation: {instance['explanation']}\n\n"

        if worksheet_type in ["MCQ Follow-up", "Both"]:
            mcq = get_linked_mcq(q)
            st.markdown(f"### Q{i+1}: Follow-up MCQ")
            st.markdown(mcq["text"])
            for j, opt in enumerate(mcq["options"]):
                st.markdown(f"{chr(65 + j)}. {opt}")
            with st.expander("Explanation"):
                st.markdown(mcq["explanation"])

            worksheet_text += f"Q{i+1} MCQ: {mcq['text']}\n"
            for j, opt in enumerate(mcq["options"]):
                worksheet_text += f"{chr(65 + j)}. {opt}\n"
            worksheet_text += f"Explanation: {mcq['explanation']}\n\n"

# generate pdf
if st.button("Generate PDF"):
    with st.spinner("Generating PDF..."):
        pdf_bytes = build_pdf_reportlab(final_sample, title=title)

    # download button here...
    st.download_button(
        label="Download PDF",
        data=pdf_bytes,
        file_name=filename,
        mime="application/pdf"
    
    )

