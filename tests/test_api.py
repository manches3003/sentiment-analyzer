from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

# --- Health & root checks ---

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# --- Sentiment endpoint ---
# We mock the model so tests run fast without downloading AI weights

def test_analyze_positive():
    mock_result = {"text": "I love this!", "label": "POSITIVE", "score": 0.9998}
    with patch("app.main.analyze", return_value=mock_result):
        response = client.post("/analyze", json={"text": "I love this!"})
    assert response.status_code == 200
    data = response.json()
    assert data["label"] == "POSITIVE"
    assert data["score"] > 0.9

def test_analyze_negative():
    mock_result = {"text": "This is terrible.", "label": "NEGATIVE", "score": 0.9985}
    with patch("app.main.analyze", return_value=mock_result):
        response = client.post("/analyze", json={"text": "This is terrible."})
    assert response.status_code == 200
    data = response.json()
    assert data["label"] == "NEGATIVE"

def test_empty_text_returns_400():
    response = client.post("/analyze", json={"text": "   "})
    assert response.status_code == 400

def test_missing_text_field():
    response = client.post("/analyze", json={})
    assert response.status_code == 422  # FastAPI validation error