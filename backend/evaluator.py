def evaluate_answer(answer):

    words=len(answer.split())
    score=0
    feedback=[]
    strengths=[]
    improvements=[]

    if words>30:
        score+=30
        strengths.append("Answer length is detailed")
    else:
        improvements.append("Add more explanation")

    if "example" in answer.lower():
        score+=25
        strengths.append("Used example")
    else:
        improvements.append("Include real example")

    if "because" in answer.lower():
        score+=25
        strengths.append("Provided reasoning")
    else:
        improvements.append("Explain reasoning")

    score+=20

    rating=round(score/10,1)

    return {
        "rating":rating,
        "strengths":strengths,
        "improvements":improvements
    }
