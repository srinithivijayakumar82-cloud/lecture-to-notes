import json

from groq import Groq

API_KEY = "groq_api_key"
client = Groq(api_key=API_KEY)
MODEL_NAME = "llama-3.3-70b-versatile"

def generate_notes(transcript: str) -> dict:
    prompt = f"""You are a note-taking assistant for students.
Given the following lecture transcript, generate structured notes.

Return ONLY a valid JSON object with this structure:
{{
    "title": "main topic of the lecture",
    "summary": "2-3 sentence overview",
    "key_points": ["point 1", "point 2", "point 3"],
    "topics": [
        {{"topic": "topic name", "notes": ["note 1", "note 2"]}}
    ]
}}

Transcript:
\"\"\"
{transcript}
\"\"\"
"""
    
    response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": prompt}]
    )
    raw_text = response.choices[0].message.content.strip()
    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]
        raw_text = raw_text.strip()

    try:
        notes = json.loads(raw_text)
        return notes
    except json.JSONDecodeError:
        print("Could not parse JSON. Raw response was:")
        print(raw_text)
        return []
    