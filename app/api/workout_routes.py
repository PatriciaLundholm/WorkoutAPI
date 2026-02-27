from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.model.schemas.workout_schema import WorkoutCreate, WorkoutRead
from app.service.workout_service import WorkoutService

router = APIRouter()

def get_workout_service():
    return WorkoutService()

@router.post("/", response_model=WorkoutRead)
def create_workout(
    workout: WorkoutCreate,
    service: WorkoutService = Depends(get_workout_service),
    db: Session = Depends(get_db),
):
    return service.create_workout(db, workout)

@router.get("/", response_model=List[WorkoutRead])
def get_workouts(
    service: WorkoutService = Depends(get_workout_service),
    db: Session = Depends(get_db),
):
    return service.get_workouts(db)

@router.get("/{id}", response_model=WorkoutRead)
def get_workout(
    id: int,
    service: WorkoutService = Depends(get_workout_service),
    db: Session = Depends(get_db),
):
    return service.get_workout(db, id)