from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Exercise(Base):
    __tablename__ = 'exercise'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    workout_id = Column(Integer, ForeignKey('workout.id'))
    workout = relationship("Workout", back_populates="exercises")
