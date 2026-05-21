from datetime import datetime

from pydantic import field_serializer, ConfigDict
from pydantic.alias_generators import to_camel

from src.schemas.session_tags.session_tags_response import SessionTagResponseModel
from src.schemas.sessions.session_create import SessionCreationBasicModel
from src.schemas.validations import format_date_response
from src.schemas.session_exercises.session_ex_response import SessionExerciseResponseModel


class SessionResponseModel(SessionCreationBasicModel):
    session_id: int
    start_date: datetime
    end_date: datetime | None
    session_exercises: list[SessionExerciseResponseModel] = []
    session_tags: list[SessionTagResponseModel] = []

    model_config = ConfigDict(from_attributes=True, alias_generator=to_camel, populate_by_name=True)

    @field_serializer('start_date','end_date')
    def serialize_finish_time(self, value: datetime | None) -> str | None:
        return format_date_response(date_input=value)