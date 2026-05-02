from pydantic import BaseModel, ConfigDict


class SessionTagResponseModel(BaseModel):
    tag_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)