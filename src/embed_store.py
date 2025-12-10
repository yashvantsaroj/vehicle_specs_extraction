



import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os
import pickle

DB_PATH = "C:/Assignments_Predii/vehicle_specs_extraction/data/vector_db/faiss.index"
META_PATH = "C:/Assignments_Predii/vehicle_specs_extraction/data/vector_db/meta.pkl"

class VectorDB:
    def __init__(self, load_existing=False):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        if load_existing and os.path.exists(DB_PATH) and os.path.exists(META_PATH):
            self.index = faiss.read_index(DB_PATH)
            with open(META_PATH, "rb") as f:
                self.metadata = pickle.load(f)
        else:
            self.index = None
            self.metadata = []

    def add_documents(self, chunks):
        texts = [c["text"] for c in chunks]
        embeddings = self.model.encode(texts, convert_to_numpy=True)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

        self.metadata = chunks

        faiss.write_index(self.index, DB_PATH)
        with open(META_PATH, "wb") as f:
            pickle.dump(chunks, f)

    def search(self, query, top_k=5):
        q_emb = self.model.encode([query], convert_to_numpy=True)
        distances, ids = self.index.search(q_emb, top_k)

        results = []
        for i in ids[0]:
            if i < len(self.metadata):
                results.append(self.metadata[i])

        return results
