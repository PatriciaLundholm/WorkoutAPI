# tests/test_exercise_routes.py
import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient

from app.main import app  # se till att detta är din FastAPI-app
from app.model.schemas.exercise_schema import ExerciseCreate, ExerciseRead

def test_root_exists():
    response = client.get("/")
    print(response.status_code)
    print(response.text[:200])

    response = client.get("/docs")
    print("Swagger status:", response.status_code)

client = TestClient(app)

# --------------------------
# Fixtures / Mocks
# --------------------------

@pytest.fixture
def mock_service():
    service = MagicMock()
    app.dependency_overrides = {}  # rensa eventuella overrides
    app.dependency_overrides[get_exercise_service] = lambda: service
    return service

# --------------------------
# Tests
# --------------------------

def get_exercise_service():
    """Dummy function för FastAPI Depends override"""
    # Returneras av pytest fixture istället
    pass

def test_create_exercise_success(mock_service):
    mock_exercise = {
        "id": 1,
        "name": "Pec Dec",
        "description": None,
        "sets": []
    }
    mock_service.create_exercise.return_value = mock_exercise

    response = client.post(
        "/workout/1/exercise",
        json={"name": "Pec Dec"}
    )

    assert response.status_code == 200
    assert response.json() == mock_exercise
    mock_service.create_exercise.assert_called_once()


def test_create_exercise_not_found(mock_service):
    mock_service.create_exercise.side_effect = ValueError("Workout Not Found")

    response = client.post(
        "/workout/999/exercise",
        json={"name": "Pec Dec"}
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Workout Not Found"}


def test_get_exercises_success(mock_service):
    mock_service.get_exercises_for_workout.return_value = [
        {"id": 1, "name": "Pec Dec", "description": None, "sets": []},
        {"id": 2, "name": "Bench Press", "description": None, "sets": []},
    ]

    response = client.get("/workout/1/exercise")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Pec Dec"
    assert data[1]["name"] == "Bench Press"

