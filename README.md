# Resume Screening Agent

## Overview

The Resume Screening Agent is an AI-assisted resume screening system that automatically analyzes multiple candidate resumes and ranks them according to their suitability for a given job description.

The system extracts candidate information from PDF, DOCX, and TXT resumes, identifies relevant skills, calculates NLP-based similarity with the job description, evaluates education and experience, and produces a final candidate score.

The goal is to reduce manual resume screening effort and provide recruiters with a consistent, explainable candidate ranking.

---

## Key Features

* Supports PDF, DOCX, and TXT resumes
* Automatic resume text extraction
* Candidate name and ID extraction
* Education and experience extraction
* Required skill matching
* TF-IDF and cosine similarity based NLP analysis
* Weighted candidate scoring
* Automatic candidate ranking
* Candidate decision classification
* CSV result generation
* Excel report generation
* Summary dashboard in Excel

---

## Project Workflow

```text
Job Description
       |
       v
Resume Files
       |
       v
Resume Parser
       |
       v
Candidate Information Extraction
       |
       +------------------+
       |                  |
       v                  v
Skill Matching       NLP Similarity
       |                  |
       +--------+---------+
                |
                v
        Experience Score
                |
                v
         Education Score
                |
                v
          Final Score
                |
                v
       Candidate Ranking
                |
                v
       Screening Decision
                |
        +-------+-------+
        |               |
        v               v
       CSV           Excel Report
```

---

## Project Structure

```text
Resume-Screening-Agent/
│
├── data/
│   ├── resumes/
│   │   ├── candidate_01.pdf
│   │   ├── candidate_02.pdf
│   │   ├── candidate_03.pdf
│   │   ├── candidate_04.pdf
│   │   ├── candidate_05.docx
│   │   ├── candidate_06.docx
│   │   ├── candidate_07.docx
│   │   ├── candidate_08.docx
│   │   ├── candidate_09.txt
│   │   ├── candidate_10.txt
│   │   ├── candidate_11.txt
│   │   └── candidate_12.txt
│   │
│   └── job_description.txt
│
├── src/
│   ├── parser.py
│   ├── scorer.py
│   └── report_generator.py
│
├── outputs/
│   ├── screening_results.csv
│   └── screening_report.xlsx
│
├── reports/
│
├── requirements.txt
├── README.md
├── SCORING_METHOD.md
└── TRADOFFS.md
```

---

## Technologies Used

### Programming Language

* Python

### NLP and Machine Learning

* spaCy
* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity

### Resume Processing

* PyMuPDF / fitz for PDF files
* python-docx for DOCX files
* Standard Python file handling for TXT files

### Data Processing

* Pandas
* NumPy

### Reporting

* CSV
* OpenPyXL
* Microsoft Excel

---

## Resume Parsing

The parser processes resumes from:

```text
data/resumes/
```

Supported formats:

```text
.pdf
.docx
.txt
```

The parser extracts:

* Candidate name
* Candidate ID
* Education
* Experience
* Skills
* Resume text

Example:

```text
Name: Arjun Nair
Candidate ID: candidate_07
Education: MSc Artificial Intelligence, 2025
Experience: 1.5 years AI research assistant
Skills: Python, Machine Learning, NLP, LLMs, Generative AI, SQL, Research
```

---

## Candidate Scoring

Each candidate receives a final score based on four major components:

| Component      | Weight |
| -------------- | -----: |
| Skills Match   |    40% |
| NLP Similarity |    25% |
| Experience     |    20% |
| Education      |    15% |

The final score is calculated using:

```text
Final Score =
(Skills × 0.40)
+ (NLP Similarity × 0.25)
+ (Experience × 0.20)
+ (Education × 0.15)
```

The candidates are then sorted from highest to lowest final score.

---

## Decision System

Candidates are classified using their final score:

|  Final Score | Decision     |
| -----------: | ------------ |
| 75% or above | Strong Match |
| 60% – 74.99% | Consider     |
| 45% – 59.99% | Maybe        |
|    Below 45% | Reject       |

These decisions are intended as screening recommendations and should not replace human recruitment decisions.

---

## Current Screening Results

The current test dataset contains 12 candidate resumes.

The highest-ranked candidate is:

```text
Candidate: Arjun Nair
Candidate ID: candidate_07
Final Score: 75.53%
Decision: Strong Match
```

The second-ranked candidate is:

```text
Candidate: Rohan Kumar
Candidate ID: candidate_03
Final Score: 69.10%
Decision: Consider
```

The third-ranked candidate is:

```text
Candidate: Karan Joshi
Candidate ID: candidate_09
Final Score: 59.52%
Decision: Maybe
```

---

## Output Files

### CSV Report

The screening system generates:

```text
outputs/screening_results.csv
```

The CSV contains:

* Rank
* Candidate name
* Candidate ID
* Final score
* Skills match
* NLP similarity
* Experience score
* Education score
* Matched skills
* Decision

### Excel Report

The system also generates:

```text
outputs/screening_report.xlsx
```

The Excel workbook contains:

* Screening Results sheet
* Summary sheet
* Candidate rankings
* Scores
* Matched skills
* Screening decisions

---

## How to Run the Project

### 1. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Run the resume parser

```powershell
python ".\src\parser.py"
```

### 3. Run the scoring system

```powershell
python ".\src\scorer.py"
```

### 4. Generate the Excel report

```powershell
python ".\src\report_generator.py"
```

After successful execution, the following files will be available:

```text
outputs/screening_results.csv
outputs/screening_report.xlsx
```

---

## Example Output

```text
RESUME SCREENING RESULTS

Rank 1: Arjun Nair
Candidate ID: candidate_07
Final Score: 75.53%
Skills Match: 69.23%
NLP Similarity: 51.33%
Experience: 100.00%
Education: 100.00%
Decision: Strong Match
```

---

## Advantages

* Automates initial resume screening
* Reduces repetitive manual work
* Provides consistent scoring
* Combines keyword-based and NLP-based analysis
* Produces ranked candidates
* Provides transparent scoring components
* Supports multiple resume formats
* Generates recruiter-friendly reports

---

## Limitations

The system is an automated screening assistant and has several limitations.

* Resume wording can affect NLP similarity.
* Skill matching depends on the configured required skills.
* Experience scoring uses predefined rules.
* Education scoring uses predefined categories.
* The system may not understand every equivalent skill or job title.
* A high score does not guarantee actual job performance.
* Human review is recommended before making hiring decisions.

---

## Future Enhancements

Possible future improvements include:

* Web-based recruiter dashboard
* Upload resumes through a browser
* Automatic job description extraction
* Advanced semantic embeddings
* Large Language Model based resume analysis
* Skill synonym detection
* Automatic skill-gap analysis
* Interview question generation
* Candidate comparison dashboard
* Email notifications
* Database integration
* Authentication and recruiter accounts
* Deployment as a cloud application

---

## Conclusion

The Resume Screening Agent demonstrates how Python, NLP, machine learning techniques, and automated reporting can be combined to create a practical recruitment-support system.

The system processes resumes, evaluates candidates against a job description, calculates multiple scoring factors, ranks candidates, and produces structured CSV and Excel reports.

It is designed as a decision-support tool that helps recruiters prioritize candidates while keeping the final hiring decision under human supervision.
