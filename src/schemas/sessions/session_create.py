from datetime import datetime

from pydantic import BaseModel, field_validator
from src.schemas.validations import validate_date


class SessionCreationBasicModel(BaseModel):
    title: str