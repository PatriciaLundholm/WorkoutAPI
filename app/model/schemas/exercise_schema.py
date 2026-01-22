from typing import Optional

from pydantic import BaseModel

class ExerciseCreate(BaseModel):
    name: str
    reps: int
    weight: float


class ExerciseRead(BaseModel):  # GET för att se övningen
    id: int
    name: str
    description: str
    weight: Optional[float] = None
    reps: Optional[int] = None
    sets: Optional[int] = None

    class Config:
        orm_mode = True
