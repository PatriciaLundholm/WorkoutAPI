from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    workout_id = Column(Integer, ForeignKey("workouts.id"))

    workout = relationship(
        "Workout",
        back_populates="exercises"
    )

    sets = relationship(
        "Set",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )