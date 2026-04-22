from pydantic import BaseModel

from src.schemas.exercises.exercise_response import ExerciseResponseModel


class ExercisesResponseModel(BaseModel):
    exercises: list[ExerciseResponseModel]