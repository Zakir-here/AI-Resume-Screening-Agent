
import os
import re
import fitz
import spacy
from docx import Document


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESUME_DIR = os.path.join(BASE_DIR, "data", "resumes")

SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".txt"]


# --------------------------------------------------
# LOAD SPACY MODEL
# --------------------------------------------------

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    nlp = None


# --------------------------------------------------
# TEXT EXTRACTION FUNCTIONS
# --------------------------------------------------

def extract_pdf_text(file_path):
    """Extract text from a PDF file."""
    text = ""

    try:
        document = fitz.open(file_path)

        for page in document:
            text += page.get_text()

        document.close()

    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")

    return text


def extract_docx_text(file_path):
    """Extract text from a DOCX file."""
    text = ""

    try:
        document = Document(file_path)

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

    except Exception as e:
        print(f"Error reading DOCX {file_path}: {e}")

    return text


def extract_txt_text(file_path):
    """Extract text from a TXT file."""
    text = ""

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            text = file.read()

    except Exception as e:
        print(f"Error reading TXT {file_path}: {e}")

    return text


def extract_text(file_path):
    """Extract text based on file extension."""

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    elif extension == ".docx":
        return extract_docx_text(file_path)

    elif extension == ".txt":
        return extract_txt_text(file_path)

    return ""


# --------------------------------------------------
# CLEAN TEXT
# --------------------------------------------------

def clean_text(text):
    """Clean unnecessary spaces and line breaks."""

    text = text.replace("\r", "\n")

    text = re.sub(r"[ \t]+", " ", text)

    text = re.sub(r"\n+", "\n", text)

    return text.strip()


# --------------------------------------------------
# NAME EXTRACTION
# --------------------------------------------------

def extract_name(text):
    """Extract candidate name without including 'Candidate ID'."""

    # First try a line beginning with Name:
    match = re.search(
        r"Name\s*:\s*(.+?)(?:\s+Candidate\s+ID\b|[\r\n]|$)",
        text,
        re.IGNORECASE
    )

    if match:
        name = match.group(1).strip()

        # Extra safety cleanup
        name = re.sub(
            r"\s+Candidate\s+ID.*$",
            "",
            name,
            flags=re.IGNORECASE
        )

        return name.strip()

    return "Unknown Candidate"


# --------------------------------------------------
# CANDIDATE ID EXTRACTION
# --------------------------------------------------

def extract_candidate_id(text, filename):
    """Extract candidate ID from resume text."""

    match = re.search(
        r"Candidate\s+ID\s*:\s*([A-Za-z0-9_-]+)",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    # Fallback to filename
    filename_without_extension = os.path.splitext(
        os.path.basename(filename)
    )[0]

    return filename_without_extension


# --------------------------------------------------
# EDUCATION EXTRACTION
# --------------------------------------------------

def extract_education(text):
    """Extract education information."""

    match = re.search(
        r"EDUCATION\s*(.*?)(?=\nEXPERIENCE|\nSKILLS|\nPROJECTS|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return " ".join(match.group(1).split())

    return "Not specified"


# --------------------------------------------------
# EXPERIENCE EXTRACTION
# --------------------------------------------------

def extract_experience(text):
    """Extract experience information."""

    match = re.search(
        r"EXPERIENCE\s*(.*?)(?=\nSKILLS|\nPROJECTS|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return " ".join(match.group(1).split())

    return "Not specified"


# --------------------------------------------------
# SKILLS EXTRACTION
# --------------------------------------------------

def extract_skills(text):
    """Extract skills from resume."""

    match = re.search(
        r"SKILLS\s*(.*?)(?=\nPROJECTS|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if not match:
        return []

    skills_text = " ".join(match.group(1).split())

    skills = [
        skill.strip()
        for skill in skills_text.split(",")
        if skill.strip()
    ]

    return skills


# --------------------------------------------------
# COMPLETE CANDIDATE INFORMATION
# --------------------------------------------------

def extract_candidate_info(text, filename=None):
    """Extract structured candidate information."""

    cleaned = clean_text(text)

    candidate = {
        "name": extract_name(cleaned),
        "candidate_id": extract_candidate_id(
            cleaned,
            filename if filename else "unknown"
        ),
        "education": extract_education(cleaned),
        "experience": extract_experience(cleaned),
        "skills": extract_skills(cleaned),
        "text": cleaned,
        "word_count": len(cleaned.split())
    }

    return candidate


# --------------------------------------------------
# FIND RESUMES
# --------------------------------------------------

def get_resume_files():
    """Find all supported resume files."""

    if not os.path.exists(RESUME_DIR):
        return []

    files = []

    for filename in os.listdir(RESUME_DIR):

        extension = os.path.splitext(filename)[1].lower()

        if extension in SUPPORTED_EXTENSIONS:
            files.append(
                os.path.join(RESUME_DIR, filename)
            )

    return sorted(files)


# --------------------------------------------------
# MAIN PARSER
# --------------------------------------------------

def parse_all_resumes():

    resume_files = get_resume_files()

    print()
    print("Resume Screening Agent")
    print("=" * 60)

    print(f"Found {len(resume_files)} resumes.")

    for file_path in resume_files:

        filename = os.path.basename(file_path)

        text = extract_text(file_path)

        candidate = extract_candidate_info(
            text,
            filename
        )

        print()
        print("-" * 60)

        print(f"Resume: {filename}")

        print(f"Name: {candidate['name']}")

        print(
            f"Candidate ID: "
            f"{candidate['candidate_id']}"
        )

        print(
            f"Education: "
            f"{candidate['education']}"
        )

        print(
            f"Experience: "
            f"{candidate['experience']}"
        )

        print("Skills:")

        if candidate["skills"]:
            print(", ".join(candidate["skills"]))
        else:
            print("None detected")

        print(
            f"Words extracted: "
            f"{candidate['word_count']}"
        )


# --------------------------------------------------
# RUN
# --------------------------------------------------

if __name__ == "__main__":

    parse_all_resumes()

