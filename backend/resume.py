import re

def parse_resume(file):
    text = file.read().decode("utf-8", errors="ignore")

    skills = []

    skill_keywords = [
        "python","machine learning","deep learning","nlp",
        "sql","javascript","react","node","flask",
        "django","tensorflow","pytorch","data analysis"
    ]

    for skill in skill_keywords:
        if skill.lower() in text.lower():
            skills.append(skill)

    score = min(len(skills)*10, 100)

    return {
        "skills": skills,
        "score": score,
        "strength": "Good technical background" if score>60 else "Needs improvement",
        "improve": "Add more quantified achievements"
    }
