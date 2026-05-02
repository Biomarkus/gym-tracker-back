from sqlalchemy.orm import Query

from factory import session
from models.session_tag import SessionTag
from src.repository.filter_querier import FilterQuerier


def get_session_tags_by_filters(session_tags_filters: dict | None = None) -> Query:
    return FilterQuerier(session, SessionTag, session_tags_filters).filter_by_properties()

def create_new_tags(tags: list[SessionTag]) -> None:
    session.add_all(tags)
    session.commit()