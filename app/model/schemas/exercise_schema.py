
from pydantic import BaseModel
from typing import List, Optional
from app.model.db.set_model import Set

class SetRead(BaseModel):
    id: int
    reps: int
    weight: float

    class Config:
        orm_mode = True

class ExerciseCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ExerciseRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    sets: List[SetRead] = []

    class Config:
        orm_mode = True

