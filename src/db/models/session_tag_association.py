from sqlalchemy import Table, Column, Integer, ForeignKey

from config.constants import SESSION_TAG_ASSOCIATION_TABLE_NAME, SESSION_TABLE_NAME, SESSION_TAGS_TABLE_NAME
from factory import Base

session_tag_association = Table(
    SESSION_TAG_ASSOCIATION_TABLE_NAME,
    Base.metadata,
    Column("session_id", Integer, ForeignKey(f"{SESSION_TABLE_NAME}.session_id")),
    Column("tag_id", Integer, ForeignKey(f"{SESSION_TAGS_TABLE_NAME}.tag_id"))
)