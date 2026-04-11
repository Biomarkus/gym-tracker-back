from pydantic import BaseModel, field_validator
from src.repository.exercise import get_exercise_by_id

class SessionExerciseCreationModel(BaseModel):
    session_id: int
    exercise_id: int
    reps: int
    weight: int


    @field_validator('exercise_id')
    def validate_session_id(self, value: int):
        if not get_exercise_by_id(exercise_id=value):
            raise ValidationError("Exercise id doesn't exist")