import re

from typing import Union
from pydantic import BaseModel, EmailStr, UUID4, Field, constr, validator
from fastapi import HTTPException, status


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
    email: EmailStr
    username: constr(min_length=1, strip_whitespace=True)
    address: Union[constr(min_length=1, strip_whitespace=True), None]
    cellphone_number: Union[constr(min_length=1, strip_whitespace=True), None]

    @validator('cellphone_number')
    def invaild_cellphonenumber(cls, value):
        InvalidCellphoneNumber = HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=[
                {
                    "loc": [
                        "body",
                        "cellphone_number"
                    ],
                    "msg": "value is not a valid cellphone number",
                    "type": "value_error.cellphone_number"
                }
            ]
        )
        cellphone_number_Regex = re.compile(r'09\d{8}')
        cellphone_number_check = cellphone_number_Regex.search(value)
        if cellphone_number_check is None:
            raise InvalidCellphoneNumber
        return value.title()
