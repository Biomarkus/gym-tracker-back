from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from config.constants import SESSION_TABLE_NAME, EXERCISE_TABLE_NAME, SESSION_EXERCISE_TABLE_NAME
from factory import Base


class SessionExercise(Base):
    __tablename__ = SESSION_EXERCISE_TABLE_NAME
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    session_id = Column(ForeignKey(f"{SESSION_TABLE_NAME}.session_id"))
    exercise_id = Column(ForeignKey(f"{EXERCISE_TABLE_NAME}.exercise_id"))
    exercise = relationship("Exercise", lazy="select")

    reps = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)