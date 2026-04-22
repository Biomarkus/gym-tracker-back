from datetime import datetime

from pydantic import field_serializer, ConfigDict

from src.schemas.sessions.session_create import SessionCreationBasicModel
from src.schemas.validations import format_date_response
from src.schemas.session_exercises.session_ex_response import SessionExerciseResponseModel


class SessionResponseModel(SessionCreationBasicModel):
    session_id: int
    start_date: datetime
    end_date: datetime | None
    session_exercises: list[SessionExerciseResponseModel] = []

    model_config = ConfigDict(from_attributes=True)

    @field_serializer('start_date','end_date')
    def serialize_finish_time(self, value: datetime | None) -> str | None:
        return format_date_response(date_input=value)