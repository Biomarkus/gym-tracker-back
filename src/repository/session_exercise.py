from sqlalchemy.orm import Query

from factory import session
from src.db.models.session_exercise import SessionExercise
from src.repository.filter_querier import FilterQuerier


def get_session_exercises_by_filters(session_exercises_filters: dict | None = None) -> Query:
    return FilterQuerier(session, SessionExercise, session_exercises_filters).filter_by_properties()

def delete_session_exercises(session_exercise_id: int) -> None:
    FilterQuerier(session, SessionExercise, {'id': session_exercise_id}).filter_by_properties().delete()
    session.commit()

def create_session_exercise(session_exercise: SessionExercise) -> None:
    session.add(session_exercise)
    session.commit()

def create_session_exercises(session_exercises: list[SessionExercise]) -> None:
    session.add_all(session_exercises)
    session.commit()
