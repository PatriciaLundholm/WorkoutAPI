from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

#Denna klass motsvarar JPA entities

class Workout(Base):
    __tablename__ = 'workout'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    exercises = relationship("Exercise", back_populates="workout")

