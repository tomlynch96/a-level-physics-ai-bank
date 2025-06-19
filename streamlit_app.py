import streamlit as st
import json
import random
from utils.worksheet_builder import build_question_instance, get_linked_mcq

# Load question bank
with open("data/questions.json") as f:
    questions = json.load(f)

st.title("Physics Worksheet Generator")

# Select topic and difficulty
topics = sorted(set(q['topic'] for q in questions))
selected_topic = st.selectbox("Choose topic:", topics)

difficulty = st.selectbox("Choose difficulty:", ["Easy", "Medium", "Hard"])

worksheet_type = st.radio("Worksheet type:", ["Free Response", "MCQ Follow-up", "Both"])

num_questions = st.slider("Number of questions", 1, 5, 3)

# Filter question list
filtered = [q for q in questions if q['topic'] == selected_topic and q['difficulty'] == difficulty]

if len(filtered) == 0:
    st.warning("No questions available for this topic and difficulty.")
else:
    sample = random.sample(filtered, min(num_questions, len(filtered)))
    st.subheader("Generated Worksheet")

    worksheet_text = ""

    for i, q in enumerate(sample):
        instance = build_question_instance(q)

        if worksheet_type in ["Free Response", "Both"]:
            st.markdown(f"### Q{i+1}: Free Response")
            st.markdown(instance["question_text"])
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

    # Download as .txt for now
    st.download_button(
        label="Download Worksheet as Text",
        data=worksheet_text,
        file_name="worksheet.txt",
        mime="text/plain"
    )
