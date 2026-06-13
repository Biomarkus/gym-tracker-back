from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from src.schemas.exercises.exercise_create import ExerciseCreationModel


class ExerciseResponseModel(ExerciseCreationModel):
    exercise_id: int

    model_config = ConfigDict(from_attributes=True, alias_generator=to_camel, populate_by_name=True)