# AI Sentiment Analyzer

A production-ready AI app that analyzes text sentiment using HuggingFace transformers,
built with FastAPI and shipped with a full CI/CD pipeline.

![CI/CD](https://github.com/YOUR_USERNAME/sentiment-analyzer/actions/workflows/ci-cd.yml/badge.svg)
```

Replace `YOUR_USERNAME` with `manches3003` — this shows a live green/red badge on your repo showing if the pipeline is passing.

**2 — Add topics to your repo** so it shows up in searches. Go to your GitHub repo → click the gear icon next to "About" → add tags like:
```
fastapi  python  sentiment-analysis  docker  ci-cd  nlp  huggingface

## Live Demo
Send any text → get back POSITIVE or NEGATIVE with a confidence score.

## Tech Stack
- **FastAPI** — Python web framework
- **HuggingFace Transformers** — AI sentiment model
- **Docker** — containerization
- **GitHub Actions** — CI/CD pipeline

## CI/CD Pipeline
Every push to `main` automatically triggers:
```
Code Push → CI (lint + test) → Docker Build → Staging → Production
```

## Project Structure
```
sentiment-analyzer/
├── app/
│   ├── main.py        ← FastAPI endpoints
│   └── model.py       ← AI model logic
├── tests/
│   └── test_api.py    ← automated tests
├── Dockerfile         ← container setup
├── requirements.txt   ← dependencies
└── .github/
    └── workflows/
        └── ci-cd.yml  ← pipeline config
```

## Run Locally
```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
Open http://localhost:8000/docs

## Run with Docker
```bash
docker build -t sentiment-analyzer .
docker run -p 8000:8000 sentiment-analyzer
```

## API Usage
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this project!"}'
```

Response:
```json
{
  "text": "I love this project!",
  "label": "POSITIVE",
  "score": 0.9998
}
```

## Run Tests
```bash
pytest tests/ -v
```
