from pydantic import BaseModel, field_validator, ConfigDict, Field
from src.repository.exercise import get_exercise_by_id

class SessionExerciseBasicModel(BaseModel):
    exercise_id: int = Field(alias="exerciseId")
    reps: int
    weight: float

    @field_validator('exercise_id')
    @classmethod
    def validate_exercise_id(cls, value: int) -> int:
        if not get_exercise_by_id(exercise_id=value).scalar():
            raise ValueError("Exercise id doesn't exist")
        return  value

class SessionExercisesCreationModel(BaseModel):
    session_exercises: list[SessionExerciseBasicModel]= Field(alias="sessionExercises")

    model_config = ConfigDict(populate_by_name=True)