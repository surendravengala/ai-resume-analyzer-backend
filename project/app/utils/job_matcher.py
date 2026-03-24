from .job_roles import JOB_ROLES
from .formatter import format_skills   # ✅ ADD THIS

def suggest_roles(resume_skills):
    results = []

    resume_set = set(resume_skills)

    for role, skills in JOB_ROLES.items():
        role_skills = set(skills)

        matched = resume_set & role_skills

        if len(role_skills) == 0:
            score = 0
        else:
            score = int((len(matched) / len(role_skills)) * 100)

        results.append({
            "role": role.title(),  # ✅ FIX ROLE FORMAT
            "match_score": score,
            "matched_skills": format_skills(list(matched))  # ✅ FIX SKILLS
        })

    results.sort(key=lambda x: x["match_score"], reverse=True)

    return results[:3]