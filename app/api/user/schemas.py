from typing import Union
from pydantic import BaseModel, EmailStr, UUID4, Field, constr


class UserBase(BaseModel):
    email: EmailStr
    username: constr(min_length=1, strip_whitespace=True)


class User(UserBase):
    id: UUID4
    address: Union[constr(min_length=1, strip_whitespace=True), None]
    cellphone_number: Union[constr(min_length=1, strip_whitespace=True), None]
    role_id: int = Field(ge=0, le=1)

    class Config:
        orm_mode = True
