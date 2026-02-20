import random

questions = {
    "Data Scientist": {
        "Easy": [
            "What is machine learning?",
            "What is overfitting?"
        ],
        "Medium": [
            "Explain bias vs variance tradeoff.",
            "How does cross validation work?"
        ],
        "Hard": [
            "Explain gradient descent mathematically.",
            "How would you deploy an ML model?"
        ]
    },

    "Web Developer": {
        "Easy": [
            "What is HTML?",
            "Difference between div and span?"
        ],
        "Medium": [
            "Explain REST API.",
            "What is event bubbling?"
        ],
        "Hard": [
            "How does virtual DOM work?",
            "Explain authentication flow in web apps."
        ]
    },

    "AI Engineer": {
        "Easy":["What is AI?"],
        "Medium":["Difference between AI and ML?"],
        "Hard":["Explain transformer architecture."]
    }
}

def generate_question(role,level):
    return random.choice(questions[role][level])
