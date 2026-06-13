from sqlalchemy.orm import Query
from factory import session
from src.db.models.session import Session
from src.repository.filter_querier import FilterQuerier


def get_sessions_by_filters(session_filters: dict) -> Query:
    return FilterQuerier(session, Session, session_filters, 'title').filter_by_properties()