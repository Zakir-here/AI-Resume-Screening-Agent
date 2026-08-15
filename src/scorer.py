
import os
import csv
from parser import extract_text, extract_candidate_info

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

RESUME_FOLDER = os.path.join(
    BASE_DIR,
    "data",
    "resumes"
)

JOB_DESCRIPTION_FILE = os.path.join(
    BASE_DIR,
    "data",
    "job_description.txt"
)

OUTPUT_FOLDER = os.path.join(
    BASE_DIR,
    "outputs"
)

OUTPUT_CSV = os.path.join(
    OUTPUT_FOLDER,
    "screening_results.csv"
)


# ============================================================
# REQUIRED SKILLS
# ============================================================

REQUIRED_SKILLS = [
    "Python",
    "Machine Learning",
    "Artificial Intelligence",
    "NLP",
    "SQL",
    "LLMs",
    "Generative AI",
    "Git",
    "GitHub",
    "Research",
    "API Integration",
    "Pandas",
    "Scikit-learn"
]


# ============================================================
# LOAD JOB DESCRIPTION
# ============================================================

def load_job_description():

    if not os.path.exists(JOB_DESCRIPTION_FILE):

        raise FileNotFoundError(
            f"Job description not found:\n{JOB_DESCRIPTION_FILE}"
        )

    with open(
        JOB_DESCRIPTION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


# ============================================================
# SKILL MATCHING
# ============================================================

def calculate_skill_match(candidate_skills):

    candidate_skills_lower = {
        skill.lower().strip()
        for skill in candidate_skills
    }

    matched_skills = []

    for required_skill in REQUIRED_SKILLS:

        if required_skill.lower() in candidate_skills_lower:

            matched_skills.append(required_skill)

    score = (
        len(matched_skills)
        / len(REQUIRED_SKILLS)
    ) * 100

    return score, matched_skills


# ============================================================
# EXPERIENCE SCORE
# ============================================================

def calculate_experience_score(experience):

    experience_lower = experience.lower()

    if "1.5 years" in experience_lower:
        return 100

    if "2 years" in experience_lower:
        return 100

    if "1 year" in experience_lower:
        return 90

    if "6-month" in experience_lower:
        return 75

    if "4 months" in experience_lower:
        return 65

    if "internship" in experience_lower:
        return 60

    if "fresher" in experience_lower:
        return 50

    return 30


# ============================================================
# EDUCATION SCORE
# ============================================================

def calculate_education_score(education):

    education_lower = education.lower()

    if "artificial intelligence" in education_lower:
        return 100

    if "data science" in education_lower:
        return 95

    if "computer science" in education_lower:
        return 95

    if "computer applications" in education_lower:
        return 90

    if "btech" in education_lower:
        return 90

    if "bca" in education_lower:
        return 90

    if "bsc" in education_lower:
        return 85

    return 50


# ============================================================
# NLP SIMILARITY
# ============================================================

def calculate_nlp_similarity(
    resume_text,
    job_description
):

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(
        documents
    )

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return similarity * 100


# ============================================================
# FINAL SCORE
# ============================================================

def calculate_final_score(
    skill_score,
    nlp_score,
    experience_score,
    education_score
):

    final_score = (
        skill_score * 0.40
        + nlp_score * 0.25
        + experience_score * 0.20
        + education_score * 0.15
    )

    return final_score


# ============================================================
# DECISION
# ============================================================

def get_decision(final_score):

    if final_score >= 75:
        return "Strong Match"

    elif final_score >= 60:
        return "Consider"

    elif final_score >= 45:
        return "Maybe"

    else:
        return "Reject"


# ============================================================
# SAVE RESULTS TO CSV
# ============================================================

def save_results_to_csv(results):

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    with open(
        OUTPUT_CSV,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Rank",
            "Name",
            "Candidate ID",
            "Final Score",
            "Skills Match",
            "NLP Similarity",
            "Experience",
            "Education",
            "Matched Skills",
            "Decision"
        ])

        for rank, result in enumerate(
            results,
            start=1
        ):

            writer.writerow([
                rank,
                result["name"],
                result["candidate_id"],
                f'{result["final_score"]:.2f}%',
                f'{result["skill_score"]:.2f}%',
                f'{result["nlp_score"]:.2f}%',
                f'{result["experience_score"]:.2f}%',
                f'{result["education_score"]:.2f}%',
                ", ".join(result["matched_skills"]),
                result["decision"]
            ])

    print()
    print("=" * 70)
    print("RESULT FILE CREATED")
    print("=" * 70)
    print(f"CSV file: {OUTPUT_CSV}")


# ============================================================
# SCREEN ALL RESUMES
# ============================================================

def screen_resumes():

    job_description = load_job_description()

    results = []

    if not os.path.exists(RESUME_FOLDER):

        print("Resume folder not found.")
        print(RESUME_FOLDER)
        return

    resume_files = sorted([
        file
        for file in os.listdir(RESUME_FOLDER)
        if file.lower().endswith(
            (".pdf", ".docx", ".txt")
        )
    ])

    print()
    print("RESUME SCREENING RESULTS")
    print("=" * 70)

    print()
    print(f"Found {len(resume_files)} resumes.")

    if len(resume_files) == 0:

        print("No resumes found.")
        return

    for filename in resume_files:

        file_path = os.path.join(
            RESUME_FOLDER,
            filename
        )

        try:

            resume_text = extract_text(
                file_path
            )

            candidate = extract_candidate_info(
                resume_text
            )

            skill_score, matched_skills = (
                calculate_skill_match(
                    candidate["skills"]
                )
            )

            nlp_score = calculate_nlp_similarity(
                resume_text,
                job_description
            )

            experience_score = (
                calculate_experience_score(
                    candidate["experience"]
                )
            )

            education_score = (
                calculate_education_score(
                    candidate["education"]
                )
            )

            final_score = calculate_final_score(
                skill_score,
                nlp_score,
                experience_score,
                education_score
            )

            decision = get_decision(
                final_score
            )

            results.append({

                "name": candidate["name"],

                "candidate_id":
                    candidate["candidate_id"],

                "skill_score":
                    skill_score,

                "nlp_score":
                    nlp_score,

                "experience_score":
                    experience_score,

                "education_score":
                    education_score,

                "final_score":
                    final_score,

                "matched_skills":
                    matched_skills,

                "decision":
                    decision
            })

        except Exception as error:

            print()
            print(
                f"Error processing {filename}:"
            )

            print(error)


    # ========================================================
    # SORT RESULTS
    # ========================================================

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )


    # ========================================================
    # DISPLAY RESULTS
    # ========================================================

    for rank, result in enumerate(
        results,
        start=1
    ):

        print()
        print(
            f"Rank {rank}: "
            f"{result['name']}"
        )

        print(
            f"Candidate ID: "
            f"{result['candidate_id']}"
        )

        print(
            f"Final Score: "
            f"{result['final_score']:.2f}%"
        )

        print(
            f"Skills Match: "
            f"{result['skill_score']:.2f}%"
        )

        print(
            f"NLP Similarity: "
            f"{result['nlp_score']:.2f}%"
        )

        print(
            f"Experience: "
            f"{result['experience_score']:.2f}%"
        )

        print(
            f"Education: "
            f"{result['education_score']:.2f}%"
        )

        print(
            "Matched Skills: "
            + ", ".join(
                result["matched_skills"]
            )
        )

        print(
            f"Decision: "
            f"{result['decision']}"
        )

        print("-" * 70)


    # ========================================================
    # SAVE CSV REPORT
    # ========================================================

    if results:

        save_results_to_csv(
            results
        )

    print()
    print("Screening completed successfully.")


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    screen_resumes()

