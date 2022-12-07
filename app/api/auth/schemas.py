from pydantic import Field, BaseModel, EmailStr
from app.api.user.schemas import UserBase


class UserCreate(UserBase):
    password: str = Field(min_length=1)


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1)
