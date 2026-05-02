from pydantic import BaseModel, Field, field_validator


class SessionTagsCreationModel(BaseModel):
    tag_names: list[str] = Field(min_length=1)

    @field_validator("tag_names")
    @classmethod
    def normalize_tags(cls, tags: list[str]) -> list[str]:
        return [tag.strip().lower() for tag in tags if tag.strip()]