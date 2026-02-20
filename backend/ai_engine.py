import os
import requests

API_KEY = st.secrets["API_KEY"]

def ask_ai(prompt):

    url="https://api.openai.com/v1/chat/completions"

    headers={
        "Authorization":f"Bearer {API_KEY}",
        "Content-Type":"application/json"
    }

    data={
        "model":"gpt-4o-mini",
        "messages":[{"role":"user","content":prompt}],
        "temperature":0.7
    }

    res=requests.post(url,headers=headers,json=data)
    return res.json()["choices"][0]["message"]["content"]


# ---------- AI INTERVIEWER ----------

def interviewer_chat(role,level,answer):

    prompt=f"""
    You are a professional interviewer.

    Candidate role: {role}
    Difficulty: {level}
    Candidate answer: {answer}

    Respond with:
    1. feedback
    2. follow up question
    3. rating /10
    """

    return ask_ai(prompt)


# ---------- AI RESUME SCORING ----------

def score_resume(text,role):

    prompt=f"""
    You are a recruiter.

    Job Role: {role}

    Resume:
    {text}

    Evaluate:
    - Resume Score /100
    - Strengths
    - Missing skills
    - Improvements
    """

    return ask_ai(prompt)
