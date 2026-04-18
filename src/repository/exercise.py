from sqlalchemy.orm import Query

from factory import session
from src.db.models.exercise import Exercise
from src.repository.filter_querier import FilterQuerier


def get_exercise_by_id(exercise_id: int) -> Query:
    return session.query(Exercise).filter(Exercise.id == exercise_id)

def get_exercise_by_filters(exercises_filters: dict | None = None) -> Query:
    return FilterQuerier(session, Exercise, exercises_filters, 'title').filter_by_properties()

def create_new_exercise(exercise: Exercise) -> None:
    session.add(exercise)
    session.commit()