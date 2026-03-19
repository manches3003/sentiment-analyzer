from transformers import pipeline

# Load model once at startup (not on every request)
_sentiment_pipeline = None

def get_pipeline():
    global _sentiment_pipeline
    if _sentiment_pipeline is None:
        _sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
    return _sentiment_pipeline

def analyze(text: str) -> dict:
    """
    Analyze sentiment of a given text.
    Returns label (POSITIVE/NEGATIVE) and confidence score.
    """
    pipe = get_pipeline()
    result = pipe(text[:512])[0]  # limit to 512 chars
    return {
        "text": text,
        "label": result["label"],
        "score": round(result["score"], 4)
    }