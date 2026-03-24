def improve_text(resume_text, match_score, missing_skills, resume_analysis):
    feedback = []

    # -----------------------------
    # 🎯 MATCH SCORE BASED
    # -----------------------------
    if match_score == 0:
        feedback.append(
            "Your resume does not align with the job description. You need to significantly improve your skill set to match industry requirements."
        )
    elif match_score < 50:
        feedback.append(
            "Your resume partially matches the job requirements, but there is significant room for improvement."
        )
    else:
        feedback.append(
            "Your resume shows a good match with the job description, but can still be optimized further."
        )

    # -----------------------------
    # 🧠 MISSING SKILLS
    # -----------------------------
    if missing_skills:
        skills_text = ", ".join([skill.capitalize() for skill in missing_skills[:5]])
        feedback.append(
            f"You are missing important skills such as {skills_text}. Adding these will improve your chances of selection."
        )

    # -----------------------------
    # 📄 MISSING SECTIONS
    # -----------------------------
    missing_items = resume_analysis.get("missing_items", [])

    for item in missing_items:
        feedback.append(item)

    # -----------------------------
    # 💡 GENERAL IMPROVEMENT
    # -----------------------------
    feedback.append(
        "Include measurable achievements and project impact (e.g., performance improvements, user growth) to strengthen your resume."
    )

    return feedback