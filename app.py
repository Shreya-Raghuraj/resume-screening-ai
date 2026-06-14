import streamlit as st

from utils import (
    extract_text,
    preprocess_text,
    extract_skills,
    calculate_similarity,
    get_candidate_name
)

st.set_page_config(page_title="Resume Screening AI")

st.title("📄 Resume Screening AI")

job_description = st.text_area(
    "Enter Job Description"
)

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Rank Candidates"):

    if not job_description:
        st.warning("Please enter a job description.")
        st.stop()

    if not uploaded_files:
        st.warning("Please upload at least one resume.")
        st.stop()

    results = []

    for file in uploaded_files:

        resume_text = extract_text(file)

        processed_resume = preprocess_text(resume_text)

        processed_jd = preprocess_text(job_description)

        skills = extract_skills(resume_text)

        score = calculate_similarity(
            processed_jd,
            processed_resume
        )

        candidate = {
            "name": get_candidate_name(resume_text),
            "skills": skills,
            "score": score
        }

        results.append(candidate)

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    st.subheader("Candidate Rankings")

    for rank, candidate in enumerate(results, start=1):

        st.markdown(f"### Rank {rank}")

        st.write(
            f"**Name:** {candidate['name']}"
        )

        st.write(
            f"**Match Score:** {candidate['score']}%"
        )

        st.write(
            f"**Skills:** {', '.join(candidate['skills'])}"
        )

        st.markdown("---")