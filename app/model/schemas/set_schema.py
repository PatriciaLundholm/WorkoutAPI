from pydantic import BaseModel
from datetime import datetime

class SetCreate(BaseModel):
    reps: int
    weight: float

class SetRead(BaseModel):
    id: int
    reps:int
    weight: float
    created_at: datetime

    class Config:
        from_attributes = True
