from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app
from app.api.exercise_routes import get_exercise_service
from app.model.schemas.exercise_schema import ExerciseRead

# Mock service
def mock_exercise_service():
    mock = MagicMock()
    mock.get_exercises_for_workout.return_value = [
        ExerciseRead(id=1, name="Pec Dec", description="Maskin", sets=[]),
        ExerciseRead(id=2, name="Sidolyft", description="Hantlar", sets=[]),
    ]
    mock.create_exercise.return_value = ExerciseRead(
        id=1, name="Pec Dec", description=None, sets=[]
    )
    return mock

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
    assert "sets" in data  # nyckel finns
    assert data["sets"] == []  # tom lista

def test_create_exercise_not_found():
    mock_service = MagicMock()
    mock_service.create_exercise.side_effect = ValueError("Workout Not Found")
    app.dependency_overrides[get_exercise_service] = lambda: mock_service
    response = client.post(
        "/api/exercises/workout/999/exercise",
        json={"name": "Pec Dec"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Workout Not Found"}
    # återställ override
    app.dependency_overrides.clear()
    app.dependency_overrides[get_exercise_service] = mock_exercise_service

def test_get_exercises_success():
    response = client.get("/api/exercises/workout/1/exercise")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Pec Dec"
    assert data[0]["sets"] == []  # uppdaterat
    assert data[1]["name"] == "Sidolyft"
    assert data[1]["sets"] == []

