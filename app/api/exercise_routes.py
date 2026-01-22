from fastapi import APIRouter
from app.model.schemas.exercise_schema import ExerciseCreate
from app.service.exercise_service import ExerciseService

router = APIRouter()
service = ExerciseService()

@router.post("/workout/{id}/exercise") #skapa övning till pass
def create_exercise(id: int):
    return service.create_exercise(id)

@router.get("/workout/{id}/exercise") #lista övningar i pass
def get_exercise(id: int):
    return service.get_exercise(id)

@router.post("/exercise/{id}/sets") #logga set i övning
def set_exercise(id: int):
    return service.set_exercise(id)

@router.get("/sets") #hämta set, för grafer
def get_sets():
    return service.get_sets()