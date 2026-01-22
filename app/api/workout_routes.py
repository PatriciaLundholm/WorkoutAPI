from fastapi import APIRouter
from app.model.schemas.workout_schema import WorkoutCreate
from app.service.workout_service import WorkoutService

router = APIRouter()
service = WorkoutService()

@router.post("/workout") #skapa pass
def create_workout(workout: WorkoutCreate):
    return service.create_workout(workout)

@router.get("/workout/{id}") #specifikt pass
def get_workout(id: int):
    return service.get_workout(id)

@router.get("/workouts") #alla pass
def get_workouts():
    return service.get_workouts()


