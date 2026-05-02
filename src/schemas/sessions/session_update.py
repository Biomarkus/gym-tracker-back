from src.schemas.session_exercises.session_ex_create import SessionExerciseBasicModel
from src.schemas.sessions.session_create import SessionCreationBasicModel


class SessionUpdateModel(SessionCreationBasicModel):
    session_exercises: list[SessionExerciseBasicModel] | None = None
    session_tag_ids: list[int] | None = None