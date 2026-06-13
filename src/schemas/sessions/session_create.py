from datetime import datetime

from pydantic import BaseModel


class SessionCreationBasicModel(BaseModel):
    title: str