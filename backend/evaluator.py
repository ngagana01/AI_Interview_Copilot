def evaluate_answer(answer):

    feedback=[]

    if len(answer.split())<20:
        feedback.append("Answer is too short")
    else:
        feedback.append("Good answer length")

    if "example" not in answer.lower():
        feedback.append("Add example for stronger impact")

    if "i " not in answer.lower():
        feedback.append("Use personal experience statements")

    return feedback
