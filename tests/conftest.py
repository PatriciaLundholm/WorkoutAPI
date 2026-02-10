import pytest
from app.database import get_db
from app.model.db.workout_model import Workout

@pytest.fixture
def db_session():
    db = next(get_db())
    workout = Workout(id=1, name="Pec Dec")
    db.add(workout)
    db.commit()
    yield db
    db.rollback()