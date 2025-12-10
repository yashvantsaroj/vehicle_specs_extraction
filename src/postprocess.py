



import json
import re
import os

OUTPUT_PATH = "Outputs/specs.json"

def validate_json(text):
    # Remove code fences or extra text
    text = text.replace("```json", "").replace("```", "").strip()

    # Fix missing commas
    text = re.sub(r'\n\s*}', '}', text)

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {
            "component": None,
            "spec_type": None,
            "value": None,
            "unit": None,
            "page_number": None
        }

def save_json(data):
    os.makedirs("Outputs", exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(data, f, indent=4)
