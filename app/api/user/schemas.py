import re
from typing import Union, Optional
from pydantic import BaseModel, EmailStr, UUID4, Field, constr
from sqlalchemy import CheckConstraint

from fastapi import HTTPException, status
from app.utils import validator


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


class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    username: Optional[constr(min_length=1, strip_whitespace=True)]
    address: Optional[constr(min_length=1, strip_whitespace=True)]
    cellphone_number: Optional[
        constr(min_length=1,
               strip_whitespace=True,
               regex=validator.cellphone_number_regex)
    ]
    __table_args__ = (CheckConstraint(
        "REGEXP_LIKE(email,'^[a-zA-Z0-9]+@+[a-zA-Z0-9-]+.+([a-zA-Z]{2,4})$')",
        name='emailcheck'))
    __table_args__ = (CheckConstraint(
        "REGEXP_LIKE(cellphone_number,'^09+([0-9]{8})$')",
        name='cellphone_numbercheck'))
