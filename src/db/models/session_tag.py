from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.constants import SESSION_TAGS_TABLE_NAME, EXERCISE_TABLE_NAME, SESSION_EXERCISE_TABLE_NAME, MAX_TEXT_LENGTH
from factory import Base
from models.session_tag_association import session_tag_association


class SessionTag(Base):
    __tablename__ = SESSION_TAGS_TABLE_NAME

    tag_id = Column(Integer, primary_key=True)
    name = Column(String(MAX_TEXT_LENGTH), unique=True, nullable=False)

    sessions = relationship(
        "Session",
        secondary=session_tag_association,
        back_populates="session_tags"
    )