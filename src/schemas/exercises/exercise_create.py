from pydantic import BaseModel, field_validator, ValidationError
from src.repository.category import get_category_by_id


class ExerciseCreationModel(BaseModel):
    title: str
    icon_path: str
    category_id: int

    @field_validator('category_id')
    @classmethod
    def validate_category_id(cls, value: int):
        if not get_category_by_id(category_id=value).scalar():
            raise ValidationError("Category id doesn't exist")
        return value