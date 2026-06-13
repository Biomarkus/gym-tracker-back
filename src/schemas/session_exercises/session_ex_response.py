from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from src.schemas.exercises.exercise_response import ExerciseResponseModel
from src.schemas.session_exercises.session_ex_create import SessionExerciseBasicModel


class SessionExerciseResponseModel(SessionExerciseBasicModel):
    id: int
    exercise: ExerciseResponseModel

    model_config = ConfigDict(from_attributes=True, alias_generator=to_camel, populate_by_name=True)
