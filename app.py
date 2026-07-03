from notes_gen import generate_notes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
class TranscriptRequest(BaseModel):
    transcript: str

@app.post("/generate_notes_endpoint")
def generate_notes_endpoint(request: TranscriptRequest):
    return generate_notes(request.transcript)