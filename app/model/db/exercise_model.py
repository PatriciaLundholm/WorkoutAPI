from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Exercise(Base):
    __tablename__ = "exercise"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    workout_id = Column(Integer, ForeignKey("workout.id"))

    sets = relationship("Set", back_populates="exercise", cascade="all, delete-orphan")

