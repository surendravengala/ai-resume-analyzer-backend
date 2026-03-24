def generate_ats_tips(job_skills, matched_skills, missing_skills):
    tips = []

    # Tip 1: Missing keywords
    if missing_skills:
        skills_text = ", ".join([skill.capitalize() for skill in missing_skills])
        tips.append(
            f"Include keywords like {skills_text} in your resume to improve ATS matching."
        )

    # Tip 2: Matched skills optimization
    if matched_skills:
        matched_text = ", ".join([skill.capitalize() for skill in matched_skills])
        tips.append(
            f"Highlight your experience with {matched_text} using strong project descriptions."
        )

    # Tip 3: General alignment
    if job_skills:
        tips.append(
            "Ensure your resume aligns closely with the job description by using similar terminology and role-specific keywords."
        )

    # Tip 4: Projects suggestion
    if missing_skills:
        tips.append(
            "Add projects demonstrating the missing skills to strengthen your profile."
        )

    return tips