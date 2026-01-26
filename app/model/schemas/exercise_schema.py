from pydantic import BaseModel
from typing import List, Optional
from app.model.schemas.set_schema import SetRead

class ExerciseCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ExerciseRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    sets_count: int
    sets: List[SetRead] = []

    class Config:
        orm_mode = True


