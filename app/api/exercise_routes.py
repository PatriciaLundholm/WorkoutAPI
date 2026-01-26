
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.model.schemas.exercise_schema import ExerciseCreate, ExerciseRead
from app.model.schemas.set_schema import SetCreate
from app.service.exercise_service import ExerciseService

router = APIRouter()
service = ExerciseService()


@router.post("/workout/{workout_id}/exercise", response_model=ExerciseRead)
def create_exercise(
    workout_id: int,
    exercise: ExerciseCreate,
    db: Session = Depends(get_db)
):

    try:
        return service.create_exercise(db, workout_id, exercise)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/workout/{workout_id}/exercise", response_model=List[ExerciseRead])
def get_exercises(workout_id: int, db: Session = Depends(get_db)):

    exercises = service.get_exercises_for_workout(db, workout_id)
    return exercises


# Logga set i en övning
@router.post("/exercise/{exercise_id}/sets")
def set_exercise(
    exercise_id: int,
    set_data: SetCreate,
    db: Session = Depends(get_db)
):
    return service.set_exercise(db, exercise_id, set_data)

# Hämta alla sets (för grafer)
@router.get("/sets")
def get_sets(db: Session = Depends(get_db)):
    return service.get_sets(db)
