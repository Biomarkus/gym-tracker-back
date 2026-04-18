from pydantic import BaseModel, field_validator, ValidationError
from src.repository.exercise import get_exercise_by_id

class SessionExerciseCreationModel(BaseModel):
    session_id: int
    exercise_id: int
    reps: int
    weight: int


    @field_validator('exercise_id')
    @classmethod
    def validate_exercise_id(cls, value: int):
        if not get_exercise_by_id(exercise_id=value):
            raise ValidationError("Exercise id doesn't exist")