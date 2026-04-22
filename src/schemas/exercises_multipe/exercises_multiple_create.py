from pydantic import BaseModel

from src.schemas.exercises.exercise_create import ExerciseCreationModel


class ExercisesCreationModel(BaseModel):
    exercises: list[ExerciseCreationModel]