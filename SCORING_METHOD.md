# Resume Screening Agent — Scoring Method

## 1. Purpose

The scoring system evaluates each candidate resume against the configured job description and produces a final suitability score.

The system combines four factors:

1. Skills Match
2. NLP Similarity
3. Experience
4. Education

The purpose of using multiple factors is to avoid relying only on keyword matching.

---

## 2. Overall Scoring Formula

The final score is calculated as:

```text
Final Score =
(Skills Match × 0.40)
+ (NLP Similarity × 0.25)
+ (Experience × 0.20)
+ (Education × 0.15)
```

Therefore, the total weight is:

```text
40% + 25% + 20% + 15% = 100%
```

---

## 3. Skills Match — 40%

Skills are compared against the predefined required skills.

The current required skills are:

```text
Python
Machine Learning
Artificial Intelligence
NLP
SQL
LLMs
Generative AI
Git
GitHub
Research
API Integration
Pandas
Scikit-learn
```

There are 13 required skills.

The skill score is calculated as:

```text
Skills Match =
(Number of matched skills / Total required skills) × 100
```

### Example

If a candidate matches 9 out of 13 required skills:

```text
9 / 13 × 100 = 69.23%
```

Therefore:

```text
Skills Match = 69.23%
```

Skills matching is the highest-weighted component because technical skills are highly relevant to the target AI-oriented role.

---

## 4. NLP Similarity — 25%

The system uses TF-IDF vectorization and cosine similarity to compare the resume text with the job description.

### TF-IDF

TF-IDF stands for:

```text
Term Frequency — Inverse Document Frequency
```

It converts text into numerical vectors based on the importance of words within the documents.

Common English stop words are removed during vectorization.

### Cosine Similarity

Cosine similarity measures how similar the resume and job description vectors are.

The result ranges from:

```text
0 to 1
```

The system converts this value to a percentage:

```text
NLP Similarity = Cosine Similarity × 100
```

### Example

If cosine similarity is:

```text
0.5133
```

the NLP similarity becomes:

```text
51.33%
```

This component helps identify candidates whose overall resume content is relevant to the job description, even beyond the explicitly matched skills.

---

## 5. Experience Score — 20%

Experience is evaluated using predefined rules based on the extracted experience description.

Current scoring rules include:

| Experience         | Score |
| ------------------ | ----: |
| 1.5 years          |  100% |
| 2 years            |  100% |
| 1 year             |   90% |
| 6-month internship |   75% |
| 4 months           |   65% |
| Internship         |   60% |
| Fresher            |   50% |
| Other/Unknown      |   30% |

The experience score is intentionally rule-based so that the scoring process remains predictable and explainable.

---

## 6. Education Score — 15%

Education is evaluated according to relevance to the target AI/data-oriented role.

Current rules include:

| Education               | Score |
| ----------------------- | ----: |
| Artificial Intelligence |  100% |
| Data Science            |   95% |
| Computer Science        |   95% |
| Computer Applications   |   90% |
| BTech                   |   90% |
| BCA                     |   90% |
| BSc                     |   85% |
| Other                   |   50% |

The system gives higher scores to degrees that are more directly related to artificial intelligence, computer science, data science, and software development.

---

## 7. Candidate Decision Rules

After calculating the final score, the system assigns a screening decision.

|   Final Score | Decision     |
| ------------: | ------------ |
| 75% or higher | Strong Match |
|  60% – 74.99% | Consider     |
|  45% – 59.99% | Maybe        |
|     Below 45% | Reject       |

These thresholds are configurable and can be modified according to the recruitment requirement.

---

## 8. Example Calculation

Consider a candidate with:

```text
Skills Match = 69.23%
NLP Similarity = 51.33%
Experience = 100%
Education = 100%
```

The final score is:

```text
(69.23 × 0.40)
+ (51.33 × 0.25)
+ (100 × 0.20)
+ (100 × 0.15)
```

Therefore:

```text
27.692
+ 12.8325
+ 20
+ 15
= 75.5245
```

Rounded to two decimal places:

```text
Final Score = 75.53%
```

Since the score is greater than or equal to 75%:

```text
Decision = Strong Match
```

---

## 9. Ranking

After all candidates are scored, the system sorts candidates in descending order of final score.

The candidate with the highest final score receives:

```text
Rank 1
```

The next highest receives:

```text
Rank 2
```

and so on.

This allows recruiters to quickly prioritize candidates.

---

## 10. Why Multiple Scoring Factors Are Used

A resume may contain many keywords without actually being a strong candidate.

For example:

* A candidate may have many technical skills but little experience.
* A candidate may have relevant experience but fewer listed skills.
* A candidate may have strong education but limited practical experience.
* A resume may use different wording from the job description.

Combining multiple scoring factors provides a more balanced screening approach.

---

## 11. Explainability

The system does not provide only a single unexplained score.

For every candidate, it provides:

```text
Final Score
Skills Match
NLP Similarity
Experience
Education
Matched Skills
Decision
```

This allows a recruiter to understand why a candidate received a particular ranking.

---

## 12. Current Example

The current screening dataset produced the following top candidates:

| Rank | Candidate   | Final Score | Decision     |
| ---: | ----------- | ----------: | ------------ |
|    1 | Arjun Nair  |      75.53% | Strong Match |
|    2 | Rohan Kumar |      69.10% | Consider     |
|    3 | Karan Joshi |      59.52% | Maybe        |
|    4 | Aarav Mehta |      56.30% | Maybe        |
|    5 | Diya Sharma |      55.19% | Maybe        |

These results demonstrate how candidates are ranked using the combined scoring model.

---

## 13. Important Considerations

The scoring system is designed as a recruitment-support mechanism rather than a replacement for human judgment.

The score can be affected by:

* Resume formatting
* Resume wording
* Missing skills
* Different terminology for similar skills
* Limited experience descriptions
* Education terminology
* Job description quality

Recruiters should review shortlisted candidates before making final hiring decisions.

---

## 14. Future Improvements

The scoring model can be improved by adding:

* Semantic embeddings
* Skill synonym detection
* LLM-based resume analysis
* Job title similarity
* Industry-specific experience scoring
* Project relevance scoring
* Certifications
* Soft skills
* Seniority detection
* Named entity recognition
* Configurable scoring weights
* Recruiter-defined scoring thresholds

---

## 15. Summary

The current scoring architecture combines:

```text
40% Skills
25% NLP Similarity
20% Experience
15% Education
```

This creates a transparent and reproducible candidate ranking system.

The approach provides a practical balance between explicit technical skill matching and broader resume-to-job-description similarity while retaining simple, explainable rules for experience and education.
