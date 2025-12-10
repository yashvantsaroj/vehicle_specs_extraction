

import fitz
import os

def load_pdf(pdf_path="data/service_manual.pdf"):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    doc = fitz.open(pdf_path)
    pages = []

    for i, page in enumerate(doc):
        text = page.get_text("text")
        pages.append({"page_number": i+1, "text": text})

    return pages
