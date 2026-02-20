st.divider()
st.header("AI Resume Evaluation")

file=st.file_uploader("Upload Resume",type=["pdf"])

if file:

    text=parse_resume(file)

    result=score_resume(text,role)

    st.success("AI Resume Analysis")
    st.write(result)
