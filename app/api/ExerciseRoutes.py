from fastapi import FastAPI, APIRouter

from app.api.WorkoutRoutes import service

app = FastAPI()
router = APIRouter()

@router.post("workout/{id}/exercise") #skapa övning till pass
def create_exercise():
    return service.create_exercise()

@router.get("/workout/{id}/exercise") #lista övningar i pass
def get_exercise():
    return service.get_exercise()

@router.post("exercise/{id}/sets") #logga set i övning
def set_exercise():
    return service.set_exercise()

@router.get("/sets") #hämta set, för grafer
def get_sets():
    return service.get_sets()