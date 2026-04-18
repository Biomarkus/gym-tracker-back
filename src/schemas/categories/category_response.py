from src.schemas.categories.category_create import CategoryCreationModel


class CategoryResponseModel(CategoryCreationModel):
    category_id: int