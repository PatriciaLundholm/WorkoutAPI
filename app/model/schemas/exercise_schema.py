from pydantic import BaseModel
from typing import (List,Optional)


class ExerciseCreate(BaseModel): #skapa övning
    title: List[str]
    description: List[str]
    weight: Optional[float] = None
    reps: Optional[int] = None
    sets: Optional[int] = None


class ExerciseRead(BaseModel): #GET för att se övningen
    id: int
    name: str
    description: str
    weight: Optional[float] = None
    reps: Optional[int] = None
    sets: Optional[int] = None


class Config:
    orm_mode = True #så att SQLAlchemy objekt kan serialiseras