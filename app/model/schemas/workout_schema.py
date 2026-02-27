from pydantic import BaseModel
from typing import List
from app.model.schemas.exercise_schema import ExerciseRead


class WorkoutCreate(BaseModel):
    name: str


class WorkoutRead(BaseModel):
    id: int
    name: str
    exercises: List[ExerciseRead] = []

    model_config = {
        "from_attributes": True
    }