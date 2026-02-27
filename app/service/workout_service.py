from sqlalchemy.orm import Session
from typing import List

from app.model.db.workout_model import Workout
from app.model.schemas.workout_schema import WorkoutCreate


class WorkoutService:

    def create_workout(self, db: Session, workout: WorkoutCreate) -> Workout:
        db_workout = Workout(name=workout.name)

        db.add(db_workout)
        db.commit()
        db.refresh(db_workout)

        return db_workout

    def get_workouts(self, db: Session) -> List[Workout]:
        return db.query(Workout).order_by(Workout.id.desc()).all()

    def get_workout(self, db: Session, id: int) -> Workout:
        workout = db.query(Workout).filter(Workout.id == id).first()
        if not workout:
            raise ValueError("Workout not found")
        return workout

