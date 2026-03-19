from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import analyze

app = FastAPI(
    title="AI Sentiment Analyzer",
    description="Analyze sentiment of any text using AI",
    version="1.0.0"
)

class TextInput(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    text: str
    label: str      # POSITIVE or NEGATIVE
    score: float    # confidence 0.0 - 1.0

@app.get("/")

def root():
    return {"message": "Sentiment Analyzer API is running!"}

@app.get("/health")
def health():
    """Health check — used by staging & production to verify app is alive."""
    return {"status": "ok"}

@app.post("/analyze", response_model=SentimentResponse)
def analyze_sentiment(body: TextInput):
    """Analyze the sentiment of a piece of text."""
    if not body.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    result = analyze(body.text)
    return result