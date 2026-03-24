import re


def detect_section(text, section_keywords):
    lines = text.split("\n")

    for line in lines:
        line_clean = line.strip().lower()

        for keyword in section_keywords:
            # Match headings only
            if line_clean == keyword or line_clean.startswith(keyword):
                return True

    return False

def analyze_resume_structure(text):
    text_lower = text.lower()

    # -----------------------------
    # 📞 CONTACT INFO DETECTION
    # -----------------------------
    phone_pattern = r'\b\d{10}\b'
    email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
    linkedin_pattern = r'linkedin\.com'

    phone_found = bool(re.search(phone_pattern, text))
    email_found = bool(re.search(email_pattern, text))
    linkedin_found = bool(re.search(linkedin_pattern, text_lower))

    # -----------------------------
    # 📄 SECTION DETECTION
    # -----------------------------
    sections = {
    "skills": detect_section(text, ["skills", "technical skills"]),
    "education": detect_section(text, ["education", "academic"]),
    "experience": detect_section(text, [
        "experience",
        "work experience",
        "professional experience",
        "employment history"
    ]),
    "projects": detect_section(text, ["projects", "project"])
}

    # -----------------------------
    # ❌ MISSING ITEMS
    # -----------------------------
    missing_items = []

    if not phone_found:
        missing_items.append("Phone number not found")

    if not email_found:
        missing_items.append("Email not found")

    if not linkedin_found:
        missing_items.append("LinkedIn profile not found")

    for section, exists in sections.items():
        if not exists:
            missing_items.append(f"{section.capitalize()} section is missing")

    return {
        "contact_info": {
            "phone": phone_found,
            "email": email_found,
            "linkedin": linkedin_found
        },
        "sections": sections,
        "missing_items": missing_items
    }