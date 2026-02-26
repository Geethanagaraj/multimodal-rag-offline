from ingestion.pdf_loader import extract_text_from_pdf

file_path = "sample.pdf"   # we will add this file next

text = extract_text_from_pdf(file_path)

print(text)