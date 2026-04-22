from pydantic import ConfigDict

from src.schemas.session_exercises.session_ex_create import SessionExerciseCreationModel


class SessionExerciseResponseModel(SessionExerciseCreationModel):
    id: int

    model_config = ConfigDict(from_attributes=True)