from app.model.schemas.workout_schema import WorkoutCreate
from sqlalchemy.orm import Session
from typing import List

from app.model.db.workout_model import Workout
from app.model.db.exercise_model import Exercise
from app.model.schemas.workout_schema import WorkoutCreate

class WorkoutService:

    def create_workout(self, db: Session, workout: WorkoutCreate) -> Workout:
        #kolla om workout redan finns
        existing = db.query(Workout).filter(Workout.date == workout.date).first()
        if existing:
            raise ValueError("Workout already exists for this date")

        #skapa en workout
        db_workout = Workout(date=workout.date)

        #lägg till exercise/exercises
        for name in workout.exercises:
            exercise = Exercise(name=name)
            db_workout.exercises.append(exercise)

        #spara i db
        db.add(db_workout)
        db.commit()
        db.refresh(db_workout)
        return db_workout


