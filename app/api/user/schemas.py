import re
from typing import Optional

from pydantic import BaseModel, EmailStr, UUID4, Field, constr
from fastapi import HTTPException, status

from app.utils import validator


class UserBase(BaseModel):
    email: EmailStr
    username: constr(min_length=1, strip_whitespace=True)


class User(UserBase):
    id: UUID4
    address: Optional[constr(min_length=1, strip_whitespace=True)]
    cellphone_number: Optional[constr(min_length=1, strip_whitespace=True)]
    role_id: int = Field(ge=0, le=1)

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    username: Optional[constr(min_length=1, strip_whitespace=True)]
    address: Optional[constr(min_length=1, strip_whitespace=True)]
    cellphone_number: Optional[
        constr(
            min_length=1,
            strip_whitespace=True,
            regex=validator.cellphone_number_regex
        )
    ]
