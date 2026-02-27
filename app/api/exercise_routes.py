from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.model.schemas.exercise_schema import ExerciseCreate, ExerciseRead
from app.model.schemas.set_schema import SetCreate, SetRead
from app.service.exercise_service import ExerciseService

router = APIRouter()
service = ExerciseService()

def get_exercise_service():
    return ExerciseService()

@router.post("/workout/{workout_id}/exercise", response_model=ExerciseRead)
def create_exercise(
    workout_id: int,
    exercise: ExerciseCreate,
    db: Session = Depends(get_db),
):
    return service.create_exercise(db, workout_id, exercise)


@router.get("/workout/{workout_id}/exercise", response_model=List[ExerciseRead])
def get_exercises(workout_id: int, db: Session = Depends(get_db)):
    return service.get_exercises_for_workout(db, workout_id)


@router.post("/exercise/{exercise_id}/sets", response_model=SetRead)
def add_set(
    exercise_id: int,
    set_data: SetCreate,
    db: Session = Depends(get_db),
):
    try:
        return service.set_exercise(db, exercise_id, set_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))