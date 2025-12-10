


from src.pdf_loader import load_pdf
from src.preprocess import preprocess_pages
from src.chunker import create_chunks
from src.embed_store import VectorDB
from src.retriever import retrieve
from src.llm_extractor import extract_specs
from src.postprocess import validate_json, save_json


def build_vdb():
    print("--- LOADING PDF ---")
    pages = load_pdf()

    print("\n--- PREPROCESSING ---")
    cleaned = preprocess_pages(pages)

    print("\n--- CHUNKING ---")
    chunks = create_chunks(cleaned)
    print("Total Chunks:", len(chunks))

    print("\n--- CREATING VECTOR DB ---")
    vdb = VectorDB()
    vdb.add_documents(chunks)
    print("Vector DB created successfully!\n")


def ask(query):
    print("\n--- LOADING VECTOR DB ---")
    vdb = VectorDB(load_existing=True)

    print("\n--- RETRIEVING CHUNKS ---")
    results = retrieve(query, vdb)
    print("Retrieved:", len(results))

    # Print preview
    for r in results:
        print(f"[Page {r['page_number']}] {r['text'][:250]}...\n")

    print("\n--- RUNNING LLM EXTRACTION ---")
    raw = extract_specs(query, results)

    print("\nRaw LLM Output:\n", raw)

    parsed = validate_json(raw)

    print("\n--- POSTPROCESS ---")
    save_json(parsed)
    print("Saved to Outputs/specs.json")


if __name__ == "__main__":
    build_vdb()

    while True:
        query = input("\nEnter your specification query (or type 'exit' to quit): ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        ask(query)
    # ask("Torque for parking brake cable bracket bolt (RH)")


# QUERIES WHICH CAN BE ASKED 
# Torque value for parking brake cable bracket bolt (RH)
# Torque for front brake caliper mounting bolts
# Torque for suspension lower arm bolts
# Torque specification for hub nut (front wheel)
# *Torque for rear stabilizer bar bracket bolts
