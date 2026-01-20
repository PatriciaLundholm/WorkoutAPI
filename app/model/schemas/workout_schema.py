from pydantic import BaseModel
from datetime import date
from typing import List


class WorkoutCreate(BaseModel): #används som en POST
    date: date
    exercises: List[str] #lista med övningsnamn som man själv anger


class WorkoutRead(BaseModel): #används som en GET
    id : int
    date: date
    exercises: List[str]

class Config:
    orm_mode = True #viktigt för SQL