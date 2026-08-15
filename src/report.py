
import os
import csv
from datetime import datetime


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REPORT_DIR = os.path.join(BASE_DIR, "reports")

CSV_FILE = os.path.join(
    REPORT_DIR,
    "resume_screening_report.csv"
)

TXT_FILE = os.path.join(
    REPORT_DIR,
    "resume_screening_report.txt"
)


# --------------------------------------------------
# SAMPLE RESULTS
# --------------------------------------------------
# These are the results from your current scorer.py.
# Later, we can connect this automatically to scorer.py.

RESULTS = [
    {
        "rank": 1,
        "name": "Arjun Nair",
        "candidate_id": "candidate_07",
        "final_score": 75.53,
        "skills_match": 69.23,
        "nlp_similarity": 51.33,
        "experience": 100.00,
        "education": 100.00,
        "decision": "Strong Match",
        "matched_skills": [
            "Python",
            "Machine Learning",
            "Artificial Intelligence",
            "NLP",
            "SQL",
            "LLMs",
            "Generative AI",
            "Git",
            "Research"
        ]
    },
    {
        "rank": 2,
        "name": "Rohan Kumar",
        "candidate_id": "candidate_03",
        "final_score": 69.10,
        "skills_match": 76.92,
        "nlp_similarity": 47.34,
        "experience": 65.00,
        "education": 90.00,
        "decision": "Consider",
        "matched_skills": [
            "Python",
            "Machine Learning",
            "NLP",
            "SQL",
            "LLMs",
            "Generative AI",
            "Git",
            "GitHub",
            "Research",
            "API Integration"
        ]
    },
    {
        "rank": 3,
        "name": "Karan Joshi",
        "candidate_id": "candidate_09",
        "final_score": 59.52,
        "skills_match": 61.54,
        "nlp_similarity": 25.61,
        "experience": 75.00,
        "education": 90.00,
        "decision": "Maybe",
        "matched_skills": [
            "Python",
            "Machine Learning",
            "NLP",
            "SQL",
            "Git",
            "API Integration",
            "Pandas",
            "Scikit-learn"
        ]
    },
    {
        "rank": 4,
        "name": "Aarav Mehta",
        "candidate_id": "candidate_01",
        "final_score": 56.30,
        "skills_match": 61.54,
        "nlp_similarity": 32.73,
        "experience": 50.00,
        "education": 90.00,
        "decision": "Maybe",
        "matched_skills": [
            "Python",
            "Machine Learning",
            "NLP",
            "SQL",
            "Git",
            "GitHub",
            "Pandas",
            "Scikit-learn"
        ]
    },
    {
        "rank": 5,
        "name": "Diya Sharma",
        "candidate_id": "candidate_02",
        "final_score": 55.19,
        "skills_match": 38.46,
        "nlp_similarity": 30.21,
        "experience": 90.00,
        "education": 95.00,
        "decision": "Maybe",
        "matched_skills": [
            "Python",
            "SQL",
            "Git",
            "Pandas",
            "Scikit-learn"
        ]
    },
    {
        "rank": 6,
        "name": "Aditya Kulkarni",
        "candidate_id": "candidate_11",
        "final_score": 53.52,
        "skills_match": 53.85,
        "nlp_similarity": 30.95,
        "experience": 50.00,
        "education": 95.00,
        "decision": "Maybe",
        "matched_skills": [
            "Python",
            "Machine Learning",
            "NLP",
            "SQL",
            "LLMs",
            "Git",
            "Pandas"
        ]
    },
    {
        "rank": 7,
        "name": "Vikram Singh",
        "candidate_id": "candidate_05",
        "final_score": 48.98,
        "skills_match": 46.15,
        "nlp_similarity": 25.07,
        "experience": 50.00,
        "education": 95.00,
        "decision": "Maybe",
        "matched_skills": [
            "Python",
            "Machine Learning",
            "SQL",
            "Git",
            "Pandas",
            "Scikit-learn"
        ]
    },
    {
        "rank": 8,
        "name": "Ishita Rao",
        "candidate_id": "candidate_04",
        "final_score": 41.95,
        "skills_match": 15.38,
        "nlp_similarity": 17.20,
        "experience": 90.00,
        "education": 90.00,
        "decision": "Reject",
        "matched_skills": [
            "SQL",
            "Git"
        ]
    },
    {
        "rank": 9,
        "name": "Priya Verma",
        "candidate_id": "candidate_08",
        "final_score": 41.77,
        "skills_match": 30.77,
        "nlp_similarity": 23.87,
        "experience": 50.00,
        "education": 90.00,
        "decision": "Reject",
        "matched_skills": [
            "Python",
            "SQL",
            "Git",
            "Pandas"
        ]
    },
    {
        "rank": 10,
        "name": "Neha Patel",
        "candidate_id": "candidate_06",
        "final_score": 38.73,
        "skills_match": 23.08,
        "nlp_similarity": 24.00,
        "experience": 50.00,
        "education": 90.00,
        "decision": "Reject",
        "matched_skills": [
            "Python",
            "SQL",
            "Git"
        ]
    },
    {
        "rank": 11,
        "name": "Sneha Iyer",
        "candidate_id": "candidate_10",
        "final_score": 30.26,
        "skills_match": 0.00,
        "nlp_similarity": 11.06,
        "experience": 100.00,
        "education": 50.00,
        "decision": "Reject",
        "matched_skills": []
    },
    {
        "rank": 12,
        "name": "Meera Thomas",
        "candidate_id": "candidate_12",
        "final_score": 22.89,
        "skills_match": 0.00,
        "nlp_similarity": 21.55,
        "experience": 50.00,
        "education": 50.00,
        "decision": "Reject",
        "matched_skills": []
    }
]


# --------------------------------------------------
# CREATE REPORT DIRECTORY
# --------------------------------------------------

def create_report_directory():
    os.makedirs(REPORT_DIR, exist_ok=True)


# --------------------------------------------------
# GENERATE CSV REPORT
# --------------------------------------------------

def generate_csv_report():

    headers = [
        "Rank",
        "Name",
        "Candidate ID",
        "Final Score",
        "Skills Match",
        "NLP Similarity",
        "Experience",
        "Education",
        "Decision",
        "Matched Skills"
    ]

    with open(
        CSV_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(headers)

        for candidate in RESULTS:

            writer.writerow([
                candidate["rank"],
                candidate["name"],
                candidate["candidate_id"],
                f'{candidate["final_score"]:.2f}%',
                f'{candidate["skills_match"]:.2f}%',
                f'{candidate["nlp_similarity"]:.2f}%',
                f'{candidate["experience"]:.2f}%',
                f'{candidate["education"]:.2f}%',
                candidate["decision"],
                ", ".join(candidate["matched_skills"])
            ])


# --------------------------------------------------
# GENERATE TEXT REPORT
# --------------------------------------------------

def generate_text_report():

    with open(
        TXT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("=" * 70 + "\n")
        file.write("RESUME SCREENING REPORT\n")
        file.write("=" * 70 + "\n\n")

        file.write(
            "Generated: "
            + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            + "\n\n"
        )

        file.write(
            f"Total Resumes Screened: {len(RESULTS)}\n\n"
        )

        file.write("-" * 70 + "\n\n")

        for candidate in RESULTS:

            file.write(
                f'Rank {candidate["rank"]}: '
                f'{candidate["name"]}\n'
            )

            file.write(
                f'Candidate ID: '
                f'{candidate["candidate_id"]}\n'
            )

            file.write(
                f'Final Score: '
                f'{candidate["final_score"]:.2f}%\n'
            )

            file.write(
                f'Skills Match: '
                f'{candidate["skills_match"]:.2f}%\n'
            )

            file.write(
                f'NLP Similarity: '
                f'{candidate["nlp_similarity"]:.2f}%\n'
            )

            file.write(
                f'Experience: '
                f'{candidate["experience"]:.2f}%\n'
            )

            file.write(
                f'Education: '
                f'{candidate["education"]:.2f}%\n'
            )

            file.write(
                f'Decision: '
                f'{candidate["decision"]}\n'
            )

            matched = candidate["matched_skills"]

            if matched:
                file.write(
                    "Matched Skills: "
                    + ", ".join(matched)
                    + "\n"
                )
            else:
                file.write(
                    "Matched Skills: None\n"
                )

            file.write("\n")
            file.write("-" * 70 + "\n\n")


# --------------------------------------------------
# DISPLAY SUMMARY
# --------------------------------------------------

def display_summary():

    strong_matches = sum(
        1 for candidate in RESULTS
        if candidate["decision"] == "Strong Match"
    )

    consider = sum(
        1 for candidate in RESULTS
        if candidate["decision"] == "Consider"
    )

    maybe = sum(
        1 for candidate in RESULTS
        if candidate["decision"] == "Maybe"
    )

    rejected = sum(
        1 for candidate in RESULTS
        if candidate["decision"] == "Reject"
    )

    print()
    print("=" * 70)
    print("REPORT GENERATED SUCCESSFULLY")
    print("=" * 70)

    print()
    print(f"Total Resumes: {len(RESULTS)}")
    print(f"Strong Matches: {strong_matches}")
    print(f"Consider: {consider}")
    print(f"Maybe: {maybe}")
    print(f"Rejected: {rejected}")

    print()
    print("Files created:")
    print(f"CSV Report: {CSV_FILE}")
    print(f"Text Report: {TXT_FILE}")

    print()
    print("Top Candidate:")
    print(
        f'{RESULTS[0]["name"]} '
        f'({RESULTS[0]["final_score"]:.2f}%)'
    )

    print("=" * 70)


# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main():

    create_report_directory()

    generate_csv_report()

    generate_text_report()

    display_summary()


if __name__ == "__main__":
    main()
