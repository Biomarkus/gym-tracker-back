from pydantic import BaseModel, field_validator, ConfigDict, Field
from src.repository.exercise import get_exercise_by_id
from src.repository.session import get_sessions_by_filters

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

class SessionExerciseCreationModel(SessionExerciseBasicModel):
    session_id: int  = Field(alias="sessionId")
    model_config = ConfigDict(populate_by_name=True)
    @field_validator('session_id')
    @classmethod
    def validate_session_id(cls, value: int) -> int:
        if not get_sessions_by_filters(session_filters={'session_id': value}).scalar():
            raise ValueError("Session id doesn't exist")
        return  value

class SessionExercisesCreationModel(BaseModel):
    session_exercises: list[SessionExerciseCreationModel]= Field(alias="sessionExercises")

    model_config = ConfigDict(populate_by_name=True)