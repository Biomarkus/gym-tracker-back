from pydantic import ConfigDict

from src.schemas.categories.category_create import CategoryCreationModel


class CategoryResponseModel(CategoryCreationModel):
    category_id: int

    model_config = ConfigDict(from_attributes=True)