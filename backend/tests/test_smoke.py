"""
Smoke tests for HealBotPro backend.
Run with: pytest backend/tests/ -v

Requires GROQ_API_KEY and other env vars to be set.
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from fastapi.testclient import TestClient

# Minimal stub so firebase_admin doesn't fail without credentials
import unittest.mock as mock
with mock.patch("firebase_admin.initialize_app"), \
     mock.patch("firebase_admin.get_app", side_effect=ValueError):
    from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json().get("status") == "ok"


def test_debug_pdf_endpoint():
    response = client.get("/debug/pdf")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data


def test_intake_turn_missing_body():
    response = client.post("/intake/turn", json={})
    assert response.status_code == 422  # Validation error


def test_consult_missing_body():
    response = client.post("/consult", json={})
    assert response.status_code == 422
