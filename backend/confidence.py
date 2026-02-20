import numpy as np

def analyze_confidence(audio_bytes):
    size=len(audio_bytes)

    score=min(100,max(20,size/1000))

    if score>75: label="Very Confident"
    elif score>55: label="Moderately Confident"
    elif score>35: label="Nervous"
    else: label="Low Confidence"

    return {"score":round(score,2),"label":label}
