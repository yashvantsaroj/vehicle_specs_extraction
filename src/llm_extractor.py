


import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

# Using the correct working model
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash",
    generation_config={
        "temperature": 0,
        "max_output_tokens": 1024
    }
)

def extract_specs(query, retrieved_chunks):
    # Build context from chunks
    context = "\n".join(
        f"[Page {c['page_number']}] {c['text']}" for c in retrieved_chunks
    )[:8000]

    prompt = f"""
You are an automotive technical specification extraction engine.

Your job is to extract **one single most relevant vehicle specification** from the PDF text.

Requirements:
- ONLY use text from the provided context.
- Never guess or hallucinate missing values.
- Extract only one specification related to the query.
- If multiple matches exist, pick the best one.
- If nothing is found, return all null values.

Return JSON in this exact structure:

{{
    "component": "<name of the component>",
    "spec_type": "<Torque/Dimension/Pressure/etc>",
    "value": "<numeric or '-' if missing>",
    "unit": "<Nm/mm/kg/L/bar/etc>",
    "page_number": <page>
}}

User Query:
{query}

Context:
{context}

Return JSON only. No explanation. No backticks.
"""

    try:
        response = model.generate_content(prompt)
        cleaned = response.text.strip()
        return cleaned

    except Exception as e:
        print("Gemini Error:", e)
        return """{
            "component": null,
            "spec_type": null,
            "value": null,
            "unit": null,
            "page_number": null
        }"""
