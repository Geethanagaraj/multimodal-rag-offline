import PyPDF2

def extract_text_from_pdf(file_path):
    pages_data = []

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page_number, page in enumerate(reader.pages):
            text = page.extract_text()

            if text:
                pages_data.append({
                    "page": page_number + 1,
                    "text": text
                })

    return pages_data