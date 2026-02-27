from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Set(Base):
    __tablename__ = "sets"

    id = Column(Integer, primary_key=True, index=True)
    weight = Column(Float, nullable=False)
    reps = Column(Integer, nullable=False)

    exercise_id = Column(Integer, ForeignKey("exercises.id"))

    exercise = relationship(
        "Exercise",
        back_populates="sets"
    )
