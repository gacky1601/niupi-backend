from pydantic import BaseModel, EmailStr, Field, UUID4

from app.api.user.schemas import UserBase, User


class UserCreate(UserBase):
    password: str = Field(min_length=1)


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1)


class LoginResponse(User):
    store_id: UUID4
