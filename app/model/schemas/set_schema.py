
from pydantic import BaseModel

class SetCreate(BaseModel):
    reps: int
    weight: float

class SetRead(BaseModel):
    id: int
    reps: int
    weight: float

    class Config:
        orm_mode = True

