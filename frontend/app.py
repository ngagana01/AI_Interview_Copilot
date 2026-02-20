import sys
import os
sys.path.append(os.path.abspath("../backend"))
from backend.ai_engine import interviewer_chat, score_resume
from resume import parse_resume
import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="AI Interview Copilot", layout="wide")

# ---------------- HEADER ----------------

st.title("🤖 AI Interview Copilot")
st.caption("Practice Interviews with Real AI Feedback")

st.divider()

# ---------------- ROLE SELECTOR ----------------

roles = ["Data Scientist","Web Developer","AI Engineer","ML Engineer","Full Stack Developer"]
role = st.selectbox("Select Job Role", roles)

# ---------------- DIFFICULTY SELECTOR ----------------

difficulty = st.selectbox("Select Difficulty", ["Easy","Medium","Hard"])

# ---------------- QUESTION BANK ----------------

questions = {
    "Data Scientist":[
        "Explain overfitting.",
        "What is bias vs variance?",
        "Explain p-value."
    ],
    "Web Developer":[
        "What is REST API?",
        "Explain event loop in JS.",
        "Difference between cookies and sessions?"
    ],
    "AI Engineer":[
        "What is backpropagation?",
        "Explain transformers.",
        "Difference between AI and ML?"
    ],
    "ML Engineer":[
        "Explain gradient descent.",
        "What is feature scaling?",
        "What is cross validation?"
    ],
    "Full Stack Developer":[
        "Explain MVC architecture.",
        "What is JWT?",
        "Difference between frontend and backend?"
    ]
}

# ---------------- GENERATE QUESTION ----------------

if "question" not in st.session_state:
    st.session_state.question = ""

if st.button("Generate Question"):

    q = random.choice(questions[role])
    st.session_state.question = q

if st.session_state.question:
    st.success(st.session_state.question)

# ---------------- ANSWER BOX ----------------

answer = st.text_area("Your Answer", height=150)

# ---------------- EVALUATION ----------------

def evaluate(ans):
    score = random.randint(4,10)
    return {
        "score":score,
        "strength":"Good explanation",
        "weakness":"Needs more technical depth",
        "tip":"Add real examples"
    }

if st.button("Submit Answer"):

    result = evaluate(answer)

    st.subheader("📊 Evaluation Result")

    st.metric("Score", f"{result['score']}/10")
    st.write("**Strength:**", result["strength"])
    st.write("**Weakness:**", result["weakness"])
    st.write("**Tip:**", result["tip"])

# ---------------- CHAT INTERVIEWER ----------------

st.divider()
st.header("🤖 AI Interviewer Chat")

if "chat" not in st.session_state:
    st.session_state.chat=[]

user_msg = st.text_input("Reply to interviewer")

if st.button("Send"):

    ai_reply = random.choice([
        "Interesting answer. Can you explain more?",
        "Why did you choose that approach?",
        "What would you improve?",
        "Can you give real-world example?"
    ])

    st.session_state.chat.append(("You",user_msg))
    st.session_state.chat.append(("AI",ai_reply))

for sender,msg in st.session_state.chat:
    if sender=="You":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

# ---------------- RESUME ANALYZER ----------------

st.divider()
st.header("📄 Resume Analyzer")

file = st.file_uploader("Upload Resume", type=["pdf","txt"])

if file:
    st.success("Resume uploaded successfully")

    suggested_roles = ["AI Engineer","ML Engineer","Data Scientist"]
    st.write("**Recommended Roles:**")

    for r in suggested_roles:
        st.button(r)

# ---------------- GRAPH ANALYTICS ----------------

st.divider()
st.header("📈 Performance Analytics")

data = pd.DataFrame({
    "Attempt":[1,2,3,4,5],
    "Score":[5,6,7,7,9]
})

st.line_chart(data.set_index("Attempt"))

confidence_data = pd.DataFrame({
    "Session":[1,2,3,4,5],
    "Confidence":[40,55,60,75,85]
})

st.bar_chart(confidence_data.set_index("Session"))

# ---------------- NEXT QUESTION ----------------

if st.button("Next Question"):
    st.session_state.question = random.choice(questions[role])
    st.rerun()
