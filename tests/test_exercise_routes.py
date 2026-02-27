# tests/test_exercise_routes.py
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app
from app.api.exercise_routes import get_exercise_service
from app.model.schemas.exercise_schema import ExerciseRead

# ===========================
# Mock service som hanterar alla scenarion
# ===========================
def mock_exercise_service():
    mock = MagicMock()

    # Mock för get_exercises_for_workout
    mock.get_exercises_for_workout.return_value = [
        ExerciseRead(id=1, name="Pec Dec", description=None, sets_count=0, sets=[]),
        ExerciseRead(id=2, name="Sidolyft", description=None, sets_count=0, sets=[]),
    ]

    # Mock för create_exercise
    def create_exercise_side_effect(db, workout_id, exercise):
        if workout_id == 999:
            # Simulerar "Workout Not Found"
            raise ValueError("Workout Not Found")
        return ExerciseRead(
            id=1, name=exercise.name, description=exercise.description, sets_count=0, sets=[]
        )

    mock.create_exercise.side_effect = create_exercise_side_effect

    return mock

# Override dependency
app.dependency_overrides[get_exercise_service] = mock_exercise_service

# Initiera klienten
client = TestClient(app)

# ===========================
# TESTS
# ===========================
def test_create_exercise_success():
    response = client.post(
        "/workout/1/exercise",
        json={"name": "Pec Dec"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Pec Dec"
    assert data["sets_count"] == 0

def test_create_exercise_not_found():
    response = client.post(
        "/workout/999/exercise",
        json={"name": "Pec Dec"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Workout Not Found"}

def test_get_exercises_success():
    response = client.get("/workout/1/exercise")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Pec Dec"
    assert data[1]["name"] == "Sidolyft"

