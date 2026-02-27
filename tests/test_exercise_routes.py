
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app
from app.api.exercise_routes import get_exercise_service
from app.model.schemas.exercise_schema import ExerciseRead

def fixed_mock_service():
    mock = MagicMock()
    # get_exercises_for_workout returnerar två exercises
    mock.get_exercises_for_workout.return_value = [
        ExerciseRead(id=1, name="Pec Dec", description=None, sets_count=0, sets=[]),
        ExerciseRead(id=2, name="Sidolyft", description=None, sets_count=0, sets=[]),
    ]
    # create_exercise returnerar en exercise
    mock.create_exercise.side_effect = lambda db, workout_id, ex: (
        ExerciseRead(id=1, name=ex.name, description=ex.description, sets_count=0, sets=[])
        if workout_id != 999
        else (_ for _ in ()).throw(ValueError("Workout Not Found"))
    )
    return mock

app.dependency_overrides[get_exercise_service] = fixed_mock_service
client = TestClient(app)

def test_create_exercise_success():
    response = client.post("/api/exercises/workout/1/exercise", json={"name": "Pec Dec"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Pec Dec"
    assert data["id"] == 1

def test_create_exercise_not_found():
    response = client.post("/api/exercises/workout/999/exercise", json={"name": "Pec Dec"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Workout Not Found"}

def test_get_exercises_success():
    response = client.get("/api/exercises/workout/1/exercise")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Pec Dec"
    assert data[1]["name"] == "Sidolyft"

