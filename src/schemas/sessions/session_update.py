from pydantic import ConfigDict, Field, BaseModel
from pydantic.alias_generators import to_camel

from src.schemas.session_exercises.session_ex_create import SessionExerciseBasicModel


class SessionUpdateModel(BaseModel):
    title: str | None = None
    end_date: str | None = Field(alias="endDate", default=None)
    session_exercises: list[SessionExerciseBasicModel] | None = None
    session_tag_ids: list[int] | None = None

    model_config = ConfigDict(from_attributes=True, alias_generator=to_camel, populate_by_name=True)