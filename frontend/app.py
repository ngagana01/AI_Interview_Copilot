from ai_engine import interviewer_chat, score_resume
from resume import parse_resume
import streamlit as st
import sys
import pandas as pd
import random

sys.path.append("backend")

from similarity import similarity_score
from evaluator import evaluate_answer
from confidence import analyze_voice
from question_generator import generate_question

st.set_page_config(page_title="AI Interview Copilot",layout="wide")

st.markdown(
"""
<style>
.main {background-color:#0e1117;color:white;}
.stButton>button {border-radius:20px;height:3em;width:100%;}
</style>
""",unsafe_allow_html=True
)

st.title("AI Interview Copilot")

# ---------------- SIDEBAR ----------------

role=st.sidebar.selectbox("Select Role",
["Data Scientist","Web Developer","AI Engineer"])

difficulty=st.sidebar.selectbox("Difficulty",
["Easy","Medium","Hard"])

if "question" not in st.session_state:
    st.session_state.question=""

if st.sidebar.button("Generate Question"):
    st.session_state.question=generate_question(role,difficulty)

st.sidebar.write("Selected:",role,"-",difficulty)

# ---------------- QUESTION ----------------

st.subheader("Interview Question")
st.info(st.session_state.question if st.session_state.question else "Click generate")

answer=st.text_area("Your Answer")

# ---------------- EVALUATION ----------------

if st.button("Analyze Answer"):

    if answer:

        sim=similarity_score(st.session_state.question,answer)
        result=evaluate_answer(answer)

        st.success("Analysis Complete")

        col1,col2=st.columns(2)

        with col1:
            st.metric("Answer Rating",result["rating"])
            st.metric("Relevance Score",sim)

        with col2:
            st.write("Strengths")
            for s in result["strengths"]:
                st.success(s)

            st.write("Improvements")
            for i in result["improvements"]:
                st.warning(i)

        # graph
        chart=pd.DataFrame({
            "Metric":["Rating","Relevance"],
            "Score":[result["rating"]*10,sim]
        })

        st.bar_chart(chart.set_index("Metric"))

        st.subheader("Pro Tip")
        st.info("Structure answers using STAR method: Situation, Task, Action, Result.")

        st.subheader("Sample Strong Answer")
        st.write("A strong answer explains concept clearly, gives example, and justifies reasoning.")

    else:
        st.error("Enter answer first")

# ---------------- VOICE ANALYSIS ----------------

st.divider()
st.subheader("Voice Confidence Analysis")

audio=st.file_uploader("Upload Voice",type=["wav","mp3"])

if audio:
    data=audio.read()
    conf,stress=analyze_voice(data)

    st.metric("Confidence Level",conf)
    st.metric("Stress Level",stress)

    df=pd.DataFrame({
        "Metric":["Confidence","Stress"],
        "Value":[conf,stress]
    })

    st.line_chart(df.set_index("Metric"))
