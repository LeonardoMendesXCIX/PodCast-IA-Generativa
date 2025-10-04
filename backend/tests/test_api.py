import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "AI Podcast Generator API"}

def test_create_episode():
    response = client.post("/api/v1/episodes", json={"title": "Test", "prompt": "Test prompt"})
    assert response.status_code == 200
    # Add more assertions
