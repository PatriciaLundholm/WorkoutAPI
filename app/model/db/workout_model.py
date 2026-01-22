from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Workout(Base):
    __tablename__ = "workout"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    exercises = relationship("Exercise", back_populates="workout")


