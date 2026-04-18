from sqlalchemy.orm import Query

from factory import session
from models.session_exercise import SessionExercise
from src.repository.filter_querier import FilterQuerier


def get_session_exercises_by_filters(session_exercises_filters: dict | None = None) -> Query:
    return FilterQuerier(session, SessionExercise, session_exercises_filters).filter_by_properties()