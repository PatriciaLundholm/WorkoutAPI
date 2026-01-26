from sqlalchemy.orm import Session
from app.model.db.exercise_model import Exercise
from app.model.db.set_model import Set
from app.model.schemas.exercise_schema import ExerciseCreate
from app.model.schemas.set_schema import SetCreate

class ExerciseService:

    def create_exercise(self, db: Session, workout_id: int, exercise: ExerciseCreate):
        new_exercise = Exercise(
            name=exercise.name,
            description=exercise.description,
            workout_id=workout_id
        )
        db.add(new_exercise)
        db.commit()
        db.refresh(new_exercise)
        return new_exercise

    def get_exercises_for_workout(self, db: Session, workout_id: int):
        return db.query(Exercise).filter(Exercise.workout_id == workout_id).all()

    def set_exercise(self, db: Session, exercise_id: int, set_data: SetCreate):
        exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
        if not exercise:
            raise ValueError("Exercise not found")
        new_set = Set(reps=set_data.reps, weight=set_data.weight, exercise_id=exercise_id)
        db.add(new_set)
        db.commit()
        db.refresh(new_set)
        return new_set

    def get_sets(self, db: Session):
        return db.query(Set).all()

