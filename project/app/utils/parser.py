import fitz  # PyMuPDF

def extract_text(pdf_file):
    try:
        # Open PDF from memory
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

        text = ""

        for page in doc:
            text += page.get_text()

        return text.strip()

    except Exception as e:
        return f"Error reading PDF: {str(e)}"