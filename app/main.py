from fastapi import FastAPI
from app.api.workout_routes import router as workout_router
from app.api.exercise_routes import router as exercise_router

app = FastAPI()

app.include_router(workout_router, prefix="/api/workouts")
app.include_router(exercise_router, prefix="/api/exercises")


