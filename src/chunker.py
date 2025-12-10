


def create_chunks(pages, chunk_size=800):
    chunks = []

    for p in pages:
        words = p["text"].split()
        for i in range(0, len(words), chunk_size):
            chunk_text = " ".join(words[i:i + chunk_size])
            chunks.append({
                "page_number": p["page_number"],
                "text": chunk_text
            })

    return chunks
