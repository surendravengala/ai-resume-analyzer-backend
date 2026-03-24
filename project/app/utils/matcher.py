from .job_matcher import suggest_roles
from .text_improver import improve_text
from .formatter import format_skills
from .resume_analyzer import analyze_resume_structure
from .ats_tips import generate_ats_tips


def calculate_match(ai_data, resume_text):
    # Normalize skills
    resume_skills = set(skill.lower() for skill in ai_data.get("resume_skills", []))
    job_skills = set(skill.lower() for skill in ai_data.get("job_skills", []))
    resume_analysis = analyze_resume_structure(resume_text)
    

    # Matching logic
    matched = sorted(list(resume_skills & job_skills))
    missing = sorted(list(job_skills - resume_skills))
    ats_tips = generate_ats_tips(job_skills, matched, missing)
    # Score calculation
    if len(job_skills) == 0:
        score = 0
    else:
        score = int((len(matched) / len(job_skills)) * 100)

    # Match level
    if score >= 75:
        level = "Strong Match"
    elif score >= 50:
        level = "Moderate Match"
    else:
        level = "Low Match"

    # Better suggestions
    if missing:
        formatted_missing = format_skills(missing)
        combined_skills = ", ".join(formatted_missing)

        suggestions = [
            f"Consider adding {combined_skills} through projects, certifications, or hands-on experience"
        ]
    else:
        suggestions = []

    # Additional features
   
    if score == 0:
        role_suggestions = [
            {
                "role": "No suitable role match",
                "match_score": 0,
                "message": "Your resume currently does not match this job description. Improve your resume by adding relevant skills and projects."
            }
    ]
    else:
        role_suggestions = suggest_roles(list(resume_skills))



    grammar_suggestions = improve_text(
        resume_text,
        score,
        missing,
        resume_analysis
)

    return {
        "match_score": score,
        "match_level": level,

        "resume_skills": format_skills(list(resume_skills)),
        "job_skills": format_skills(list(job_skills)),

        "matched_skills": format_skills(matched),
        "missing_skills": format_skills(missing),
        "ats_tips": ats_tips,
        "suggestions": suggestions,
        "recommended_roles": role_suggestions,
        "resume_feedback": grammar_suggestions,
        "resume_analysis": resume_analysis,
    }