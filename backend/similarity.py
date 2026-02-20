from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity_score(q,a):
    vec=TfidfVectorizer()
    mat=vec.fit_transform([q,a])
    score=cosine_similarity(mat[0],mat[1])[0][0]
    return round(score*100,2)
