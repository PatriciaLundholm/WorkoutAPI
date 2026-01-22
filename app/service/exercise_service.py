from sqlalchemy.orm import Session
from typing import List

from app.model.schemas.exercise_schema import ExerciseCreate
from app.model.db.exercise_model import Exercise
from app.model.db.workout_model import Workout


class ExerciseService:

    def create_exercise(
        self,
        db: Session,
        workout_id: int,
        exercise: ExerciseCreate
    ) -> Exercise:

        # Kontrollera att workout finns
        workout = (
            db.query(Workout)
            .filter(Workout.id == workout_id)
            .first()
        )

        if not workout:
            raise ValueError("Workout not found")

        db_exercise = Exercise(
            name=exercise.title,
            reps=exercise.reps,
            weight=exercise.weight,
            workout_id=workout_id
        )

        db.add(db_exercise)
        db.commit()
        db.refresh(db_exercise)

        return db_exercise

    def get_exercises_for_workout(
        self,
        db: Session,
        workout_id: int
    ) -> List[Exercise]:

        return (
            db.query(Exercise)
            .filter(Exercise.workout_id == workout_id)
            .all()
        )
