from pydantic import BaseModel


class CategoryCreationModel(BaseModel):
    name: str