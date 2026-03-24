DISPLAY_NAMES = {
    "aws": "AWS",
    "sql": "SQL",
    "mysql": "MySQL",
    "sqlite": "SQLite",
    "javascript": "JavaScript",
    "html": "HTML",
    "css": "CSS",
    "github": "GitHub",
    "next.js": "Next.js"
}

def format_skills(skills):
    formatted = []
    for skill in skills:
        if skill in DISPLAY_NAMES:
            formatted.append(DISPLAY_NAMES[skill])
        else:
            formatted.append(skill.capitalize())
    return formatted