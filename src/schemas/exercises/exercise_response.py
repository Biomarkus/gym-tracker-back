from src.schemas.exercises.exercise_create import ExerciseCreationModel


class ExerciseResponseModel(ExerciseCreationModel):
    exercise_id: int