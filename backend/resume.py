import PyPDF2

def parse_resume(file):

    reader=PyPDF2.PdfReader(file)
    text=""

    for page in reader.pages:
        text+=page.extract_text()

    skills=[]
    keywords=["python","machine learning","ai","sql","react","data"]

    for k in keywords:
        if k in text.lower():
            skills.append(k)

    return {"skills":skills,"score":len(skills)*15}
