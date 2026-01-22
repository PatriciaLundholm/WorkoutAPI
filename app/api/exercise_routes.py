from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.schemas.exercise_schema import ExerciseCreate
from app.service.exercise_service import ExerciseService

router = APIRouter()
service = ExerciseService()

# Skapa övning i ett pass
@router.post("/workout/{workout_id}/exercise")
def create_exercise(
    workout_id: int,
    exercise: ExerciseCreate,
    db: Session = Depends(get_db)
):
    return service.create_exercise(db, workout_id, exercise)

# Lista övningar i ett pass
@router.get("/workout/{workout_id}/exercise")
def get_exercises(workout_id: int, db: Session = Depends(get_db)):
    return service.get_exercise_for_workout(db, workout_id)

# Logga set i en övning
@router.post("/exercise/{exercise_id}/sets")
def set_exercise(
    exercise_id: int,
    set_data: dict,  # här kan du skapa ett SetSchema om du vill
    db: Session = Depends(get_db)
):
    return service.set_exercise(db, exercise_id, set_data)

# Hämta alla sets (för grafer)
@router.get("/sets")
def get_sets(db: Session = Depends(get_db)):
    return service.get_sets(db)
