import pdfplumber
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Simple stopwords list
stop_words = {
    "the", "a", "an", "is", "are", "was", "were",
    "and", "or", "to", "of", "in", "for", "on",
    "with", "at", "by", "from", "that", "this"
}

SKILLS = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pandas",
    "numpy",
    "flask",
    "streamlit",
    "nlp",
    "data analysis",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "mongodb",
    "c",
    "c++"
]

def extract_text(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def preprocess_text(text):
    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    words = text.split()

    words = [word for word in words if word not in stop_words]

    return " ".join(words)


def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))


def calculate_similarity(job_description, resume_text):
    documents = [job_description, resume_text]

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )

    return round(similarity[0][0] * 100, 2)


def get_candidate_name(text):
    lines = text.split("\n")

    for line in lines:
        if line.strip():
            return line.strip()

    return "Unknown Candidate"