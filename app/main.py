from fastapi import FastAPI
from app.api.workout_routes import router as workout_router
from app.api.exercise_routes import router as exercise_router
from app.database import Base, engine
from app.database import init_db
from app.model.db.workout_model import Workout
from app.model.db.exercise_model import Exercise

app = FastAPI(
    title="Workout API",
    description="API för träningspass och övningar",
    version="0.1.0"
)

# Skapa tabeller
Base.metadata.create_all(bind=engine)

# Registrera routers
app.include_router(workout_router, prefix="/api/workouts")
app.include_router(exercise_router, prefix="/api/exercises")

init_db()