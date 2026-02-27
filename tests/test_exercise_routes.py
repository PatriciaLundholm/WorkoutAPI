# tests/test_exercise_routes.py
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app
from app.api.exercise_routes import get_exercise_service
from app.model.db.exercise_model import Exercise


def mock_exercise_service():
    mock = MagicMock()
    # Returnera två exercises när man hämtar exercises för ett pass
    mock.get_exercises_for_workout.return_value = [
        Exercise(id=1, name="Pec Dec", description="Maskin"),
        Exercise(id=2, name="Sidolyft", description="Hantlar"),
    ]
    # Returnera en exercise när man skapar en ny
    mock.create_exercise.return_value = Exercise(id=1, name="Pec Dec", description=None)
    return mock

# Override dependency
app.dependency_overrides[get_exercise_service] = mock_exercise_service

client = TestClient(app)

def test_create_exercise_success():
    response = client.post(
        "/api/exercises/workout/1/exercise",
        json={"name": "Pec Dec"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Pec Dec"
    assert data["id"] == 1

def test_create_exercise_not_found():
    # Mock som kastar ValueError
    mock_service = MagicMock()
    mock_service.create_exercise.side_effect = ValueError("Workout Not Found")
    app.dependency_overrides[get_exercise_service] = lambda: mock_service

    response = client.post(
        "/api/exercises/workout/999/exercise",
        json={"name": "Pec Dec"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Workout Not Found"}


    app.dependency_overrides[get_exercise_service] = mock_exercise_service

def test_get_exercises_success():
    response = client.get("/api/exercises/workout/1/exercise")
    assert response.status_code == 200
    data = response.json()
    
    assert len(data) == 2
    assert data[0]["name"] == "Pec Dec"
    assert data[1]["name"] == "Sidolyft"

