from logging import exception

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.model.schemas.set_schema import SetCreate, SetRead
from app.service.set_service import SetService

router = APIRouter()
service = SetService()

@router.post("/exercise/{exercise_id}/sets", response_model=SetRead)
def add_set(exercise_id: int, set_data: SetCreate, db: Session = Depends(get_db)):
    try:
        return service.create_set(db, exercise_id, set_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))