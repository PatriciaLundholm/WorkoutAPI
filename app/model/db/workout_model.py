from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.orm import relationship
from app.database import Base

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Relation till exercises
    exercises = relationship("Exercise", back_populates="workout", cascade="all, delete-orphan")



