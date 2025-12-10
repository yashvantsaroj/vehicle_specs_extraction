


import re

def preprocess_pages(pages):
    cleaned = []
    for p in pages:
        text = re.sub(r"\s+", " ", p["text"]).strip()
        cleaned.append({"page_number": p["page_number"], "text": text})
    return cleaned
