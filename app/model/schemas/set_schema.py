from pydantic import BaseModel


class SetCreate(BaseModel):
    reps: int
    weight: float


class SetRead(BaseModel):
    id: int
    reps: int
    weight: float

    model_config = {
        "from_attributes": True
    }