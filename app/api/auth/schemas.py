from pydantic import Field
from app.api.user.schemas import UserBase


class UserCreate(UserBase):
    password: str = Field(min_length=1)
