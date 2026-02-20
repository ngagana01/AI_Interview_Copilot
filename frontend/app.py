import streamlit as st
import sys
import random
import pandas as pd

sys.path.append("backend")

from similarity import similarity_score
from evaluator import evaluate_answer
from confidence import analyze_confidence
from emotion import detect_emotion
from resume import parse_resume

st.set_page_config(page_title="AI Interview Copilot",layout="wide")

# ---------------- LOGIN SYSTEM ----------------

if "user" not in st.session_state:
    st.session_state.user=None

def login():
    st.title("Login")

    username=st.text_input("Username")
    password=st.text_input("Password",type="password")

    if st.button("Login"):
        if username and password:
            st.session_state.user=username
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Enter credentials")

if not st.session_state.user:
    login()
    st.stop()

# ---------------- SIDEBAR ----------------

st.sidebar.title("Candidate Panel")

job_role=st.sidebar.selectbox(
    "Select Job Role",
    ["Data Scientist","Web Developer","AI Engineer","ML Engineer","Full Stack Developer"]
)

round_type=st.sidebar.selectbox(
    "Interview Round",
    ["HR Round","Technical Round","Coding Round","Aptitude Round"]
)

st.sidebar.write("Logged in as:",st.session_state.user)

# ---------------- MAIN TITLE ----------------

st.title("AI Interview Copilot Dashboard")

tab1,tab2,tab3,tab4=st.tabs(["Answer Evaluation","Voice Confidence","Resume Analysis","Performance Dashboard"])

# ---------------- TAB 1 ----------------

with tab1:

    st.subheader("Interview Practice")

    q=st.text_area("Interview Question")
    a=st.text_area("Your Answer")

    if st.button("Evaluate Answer"):

        score=similarity_score(q,a)
        feedback=evaluate_answer(a)

        st.success("Evaluation Complete")

        st.write("Similarity Score:",score,"%")
        st.progress(score/100)

        st.subheader("Feedback")
        for f in feedback:
            st.write("-",f)

        # Save performance
        st.session_state["score"]=score


# ---------------- TAB 2 ----------------

with tab2:

    audio=st.file_uploader("Upload Voice",type=["wav","mp3"])

    if audio:

        data=audio.read()

        conf=analyze_confidence(data)
        emo=detect_emotion(data)

        st.write("Confidence Score:",conf["score"])
        st.write("Confidence Level:",conf["label"])
        st.write("Emotion:",emo)

        st.session_state["confidence"]=conf["score"]


# ---------------- TAB 3 ----------------

with tab3:

    file=st.file_uploader("Upload Resume PDF",type=["pdf"])

    if file:

        result=parse_resume(file)

        st.write("Skills Detected:",result["skills"])
        st.write("Resume Score:",result["score"])

        st.session_state["resume"]=result["score"]


# ---------------- TAB 4 DASHBOARD ----------------

with tab4:

    st.subheader("Performance Analytics")

    score=st.session_state.get("score",random.randint(50,90))
    conf=st.session_state.get("confidence",random.randint(50,90))
    resume=st.session_state.get("resume",random.randint(50,90))

    data=pd.DataFrame({
        "Metric":["Answer Score","Confidence","Resume"],
        "Value":[score,conf,resume]
    })

    st.bar_chart(data.set_index("Metric"))

    st.write("Selected Role:",job_role)
    st.write("Interview Type:",round_type)

    avg=(score+conf+resume)/3

    st.metric("Overall Performance",round(avg,2))

    if avg>80:
        st.success("Excellent Interview Readiness")
    elif avg>60:
        st.info("Good, but needs improvement")
    else:
        st.warning("Needs Practice")
