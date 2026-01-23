from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Set(Base):
    __tablename__ = "sets"

    id = Column(Integer, primary_key=True, index=True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)

    reps = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    exercise = relationship("Exercise", back_populates="sets")


