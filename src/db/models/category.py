from sqlalchemy import Column, Integer, String

from config.constants import CATEGORY_TABLE_NAME, MAX_TEXT_LENGTH
from factory import Base


class Category(Base):
    __tablename__ = CATEGORY_TABLE_NAME

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(MAX_TEXT_LENGTH), nullable=False)