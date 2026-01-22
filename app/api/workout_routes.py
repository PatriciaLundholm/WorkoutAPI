from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.schemas.workout_schema import WorkoutCreate
from app.service.workout_service import WorkoutService

router = APIRouter()
service = WorkoutService()

@router.post("/") #skapa pass
def create_workout(workout: WorkoutCreate, db: Session = Depends(get_db)):
    return service.create_workout(db, workout)

@router.get("/{id}") #specifikt pass
def get_workout(id: int, db: Session = Depends(get_db)):
    return service.get_workout(db,id)

@router.get("/") #alla pass
def get_workouts(db: Session = Depends(get_db)):
    return service.get_workouts(db)


