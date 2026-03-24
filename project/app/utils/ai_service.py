import os
import re

from .skills import SKILLS_DB

def extract_skills(text, skills_db):
    text = text.lower()
    found_skills = []

    for skill in skills_db:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


def analyze_with_ai(resume_text, job_desc):
    resume_skills = extract_skills(resume_text, SKILLS_DB)
    job_skills = extract_skills(job_desc, SKILLS_DB)

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills
    }

