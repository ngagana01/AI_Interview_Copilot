def analyze_voice(audio_bytes):

    length=len(audio_bytes)

    confidence=min(100,length/800)

    stress=max(0,100-confidence)

    return round(confidence,2), round(stress,2)
