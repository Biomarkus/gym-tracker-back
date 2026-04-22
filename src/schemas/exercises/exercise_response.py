from pydantic import ConfigDict

from src.schemas.exercises.exercise_create import ExerciseCreationModel


class ExerciseResponseModel(ExerciseCreationModel):
    exercise_id: int

    model_config = ConfigDict(from_attributes=True)