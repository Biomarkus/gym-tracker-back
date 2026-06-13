from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from src.schemas.exercises.exercise_response import ExerciseResponseModel
from src.schemas.session_exercises.session_ex_create import SessionExerciseCreationModel


class SessionExerciseResponseModel(SessionExerciseCreationModel):
    id: int
    exercise: ExerciseResponseModel

    model_config = ConfigDict(from_attributes=True, alias_generator=to_camel, populate_by_name=True)
