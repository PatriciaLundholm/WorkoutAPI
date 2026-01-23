from app.model.db.exercise_model import Exercise
from sqlalchemy.orm import Session
from app.model.schemas.set_schema import SetCreate
from app.model.db.set_model import Set


class SetService:
    def create_set(self, db: Session, exercise_id: int, data: SetCreate):
        exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
        if not exercise:
            raise ValueError("Exercise not found")

        new_set = Set(
            exercise_id=exercise_id,
            reps=data.reps,
            weight=data.weight,
        )

        db.add(new_set)
        db.commit()
        db.refresh(new_set)
        return new_set
