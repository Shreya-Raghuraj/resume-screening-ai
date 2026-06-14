# Resume Screening AI

## Overview

Resume Screening AI is an AI-powered application that automates the process of screening resumes against a job description. The system extracts text from uploaded PDF resumes, identifies relevant skills, calculates similarity scores using TF-IDF and cosine similarity, and ranks candidates based on their relevance to the job requirements.

## Features

* Upload multiple resumes in PDF format
* Enter a custom job description
* Extract candidate skills automatically
* Perform text preprocessing
* Calculate resume-job description similarity scores
* Rank candidates based on match percentage
* Generate candidate summaries including skills and score
* Simple and interactive Streamlit interface

## Tech Stack

* Python 3
* Streamlit
* pdfplumber
* Scikit-learn

## Project Structure

```text
Resume-Screening-AI/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
└── sample_resumes/
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/resume-screening-ai.git
```

2. Navigate to the project folder

```bash
cd resume-screening-ai
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## Workflow

1. Enter a job description.
2. Upload one or more PDF resumes.
3. Click **Rank Candidates**.
4. View ranked candidates with:

   * Candidate Name
   * Match Score
   * Extracted Skills

## Example Output

* Rank 1: Highest matching candidate
* Rank 2: Second highest matching candidate
* Match scores displayed as percentages
* Extracted skills listed for each candidate

## Future Improvements

* Named Entity Recognition (NER) for better information extraction
* Education and experience extraction
* Sentence-BERT embeddings for improved matching accuracy
* Database integration
* Export results to CSV or PDF

## Author

Shreya Raghuraj
