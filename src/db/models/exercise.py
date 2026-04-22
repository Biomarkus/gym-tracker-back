from sqlalchemy import Column, Integer, String, ForeignKey

from config.constants import EXERCISE_TABLE_NAME, CATEGORY_TABLE_NAME , MAX_TEXT_LENGTH
from factory import Base


class Exercise(Base):
    __tablename__ = EXERCISE_TABLE_NAME
    __table_args__ = {'extend_existing': True}

    exercise_id = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(MAX_TEXT_LENGTH), nullable=False)
    icon_path: str = Column(String(MAX_TEXT_LENGTH), nullable=False)
    category_id: int = Column(Integer, ForeignKey(f"{CATEGORY_TABLE_NAME}.category_id"), nullable=False)