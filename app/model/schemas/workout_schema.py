from pydantic import BaseModel
from datetime import date
from typing import List, Optional


from pydantic import BaseModel

class WorkoutCreate(BaseModel):
    name: str



class WorkoutRead(BaseModel): #används som en GET
    id : int
    date: date
    exercises: List[str]

class Config:
    orm_mode = True #viktigt för SQL