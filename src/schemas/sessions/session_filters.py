from pydantic import BaseModel


class SessionFiltersModel(BaseModel):
    title: str | None = None
    start_date: str | None = None

    class Config:
        extra = "forbid"