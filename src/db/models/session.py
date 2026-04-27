from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from config.constants import SESSION_TABLE_NAME, MAX_TEXT_LENGTH
from factory import Base
from models.session_tag_association import session_tag_association


class Session(Base):
    __tablename__ = SESSION_TABLE_NAME
    __table_args__ = {'extend_existing': True}

    session_id = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(MAX_TEXT_LENGTH), nullable=False)
    start_date: datetime = Column(DateTime, nullable=False, default=datetime.now())
    end_date: datetime = Column(DateTime, nullable=True)
    session_exercises: list = relationship(
        "SessionExercise", cascade="all, delete-orphan"
    )

    session_tags = relationship(
        "SessionTag",
        secondary=session_tag_association,
        back_populates="sessions"
    )