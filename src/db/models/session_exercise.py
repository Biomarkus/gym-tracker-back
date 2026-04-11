from sqlalchemy import Column, Integer, ForeignKey

from config.constants import SESSION_TABLE_NAME, EXERCISE_TABLE_NAME
from factory import Base


class SessionExercise(Base):
    __tablename__ = "session_exercise"

    id = Column(Integer, primary_key=True)
    session_id = Column(ForeignKey(f"{SESSION_TABLE_NAME}.session_id"))
    exercise_id = Column(ForeignKey(f"{EXERCISE_TABLE_NAME}.exercise_id"))

    reps = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)