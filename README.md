
# 📘 Vehicle Specification Extraction System

*A Retrieval-Augmented Generation (RAG) Pipeline for Extracting Automotive Specifications from Service Manuals*
**Developed for: Predii India Private Limited Assignment**

---

# 📌 **1. Project Overview**

This project implements a **complete end-to-end pipeline** that extracts **vehicle specifications**—such as torque values, fluid capacities, and part numbers—from an automotive service manual in PDF format.

The system uses:

* **PDF Parsing**
* **Text Preprocessing**
* **Semantic Chunking**
* **Vector Embeddings**
* **FAISS Vector Search**
* **Retrieval-Augmented Generation (RAG) using an LLM**
* **Structured JSON Output**

This tool allows a user to input a query like:

> “Torque for brake caliper bolts”

and receive precise structured results such as:

```json
[
  {
    "component": "Brake Caliper Bolt",
    "spec_type": "Torque",
    "value": "35",
    "unit": "Nm",
    "page_number": 72
  }
]
```

This pipeline follows exactly the guidelines provided in the assignment.

---

# 📁 **2. Folder Structure**

```
vehicle-spec-extraction/
│
├─ data/
│   └─ service_manual.pdf
│
├─ src/
│   ├─ pdf_loader.py
│   ├─ preprocess.py
│   ├─ chunker.py
│   ├─ embed_store.py
│   ├─ retriever.py
│   ├─ llm_extractor.py
│   ├─ postprocess.py
│   └─ __init__.py
│
├─ outputs/
│   └─ specs.json
│
├─ notebooks/
│
├─ run_pipeline.py
├─ requirements.txt
└─ README.md
```

---

# ⚙️ **3. Features**

### ✔ PDF Parsing

Extracts raw text from automotive service manuals using **PyMuPDF**.

### ✔ Preprocessing

Cleans text, removes noise, normalizes spaces & hyphenated line breaks.

### ✔ Intelligent Chunking

Splits content into overlapping semantic chunks for improved retrieval.

### ✔ Embedding + Vector Store

Uses **Sentence Transformers** + **FAISS** for efficient similarity search.

### ✔ Retrieval-Augmented Generation (RAG)

Feeds relevant chunks to an LLM for correct, context-backed extraction.

### ✔ Structured Output

Outputs specifications in clean **JSON** format.

---

# 🚀 **4. How to Run the Project**

## **Step 1: Clone or Create Project Folder**

```bash
git clone <repo-url>
```

Or create your folder manually.

---

## **Step 2: Create and Activate Virtual Environment**

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## **Step 3: Install Requirements**

Inside your project folder:

```bash
pip install -r requirements.txt
```

---

## **Step 4: Add Your PDF**

Place the service manual inside:

```
data/service_manual.pdf
```

---

## **Step 5: Add Your OpenAI API Key**

Create `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## **Step 6: Run the Entire Pipeline**

```bash
python run_pipeline.py
```

This performs:

* PDF Extraction
* Chunking
* Embedding
* Vector Index Building
* Querying
* LLM Extraction

---

## **Step 7: View Final Output**

Output location:

```
outputs/specs.json
```

---

# 🧠 **5. System Architecture**

Below is the step-by-step pipeline followed:

```
            ┌────────────────────────────┐
            │     Service Manual PDF     │
            └─────────────┬──────────────┘
                          ▼
               ┌────────────────────┐
               │   PDF Extraction   │
               └────────────────────┘
                          ▼
               ┌────────────────────┐
               │    Preprocessing   │
               └────────────────────┘
                          ▼
               ┌────────────────────┐
               │      Chunking      │
               └────────────────────┘
                          ▼
               ┌────────────────────┐
               │    Embeddings      │
               └────────────────────┘
                          ▼
               ┌────────────────────┐
               │    FAISS Index     │
               └────────────────────┘
                          ▼
               ┌────────────────────┐
               │   Query Retrieval  │
               └────────────────────┘
                          ▼
               ┌────────────────────┐
               │  LLM Extraction    │
               └────────────────────┘
                          ▼
               ┌────────────────────┐
               │  JSON Output File  │
               └────────────────────┘
```

---

# 🔧 **6. Tools & Technologies Used**

| Component     | Technology                                      |
| ------------- | ----------------------------------------------- |
| PDF Parser    | PyMuPDF                                         |
| Text Cleaning | Python                                   |
| Embeddings    | SentenceTransformers (MiniLM-L6-v2)             |
| Vector Store  | FAISS CPU                                       |
| LLM           | gemini-2.5-flash                                |
| Output        | JSON                                            |

---

# 📝 **7. Design Decisions**

### ✔ Why PyMuPDF?

Fast, accurate text extraction that preserves formatting better than pdfminer.

### ✔ Why Sentence Transformers?

Very fast + high-quality semantic embeddings.

### ✔ Why FAISS?

Industry-standard for similarity search and vector retrieval.

### ✔ Why Chunk Overlap?

Avoids losing important contextual information.

### ✔ Why JSON Output?

Matches assignment requirement and ideal for API integration.

---

# 📈 **8. Ideas for Future Improvements**

These can be mentioned during your interview:

* Add **OCR** for image-based PDFs (Tesseract or EasyOCR)
* Add **Streamlit UI** for better user experience
* Implement **multi-query search** for complex cases
* Improve chunking using **heading-based section segmentation**
* Add unit normalization (Nm ↔ ft-lb)
* Add accuracy evaluation by manual ground truthing

---

# 🙋‍♂️ **9. Maintainer**

**Developer:** Yashvant Saroj
**Assignment:** Predii India Private Limited – LLM Specification Extraction Task
**Year:** 2025

---




