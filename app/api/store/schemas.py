import re

from typing import Union
from pydantic import BaseModel, EmailStr, UUID4, constr, validator
from fastapi import HTTPException, status


class Store(BaseModel):
    id: UUID4
    user_id: UUID4
    name: Union[constr(min_length=1, strip_whitespace=True), None]
    address: Union[constr(min_length=1, strip_whitespace=True), None]
    email: Union[EmailStr, None]
    cellphone_number: Union[constr(min_length=1, strip_whitespace=True), None]
    telephone_number: Union[constr(min_length=1, strip_whitespace=True), None]

    class Config:
        orm_mode = True


class StoreInitialize(BaseModel):
    name: constr(min_length=1, strip_whitespace=True)
    address: Union[constr(min_length=1, strip_whitespace=True), None]
    email: Union[EmailStr, None]
    cellphone_number: Union[constr(min_length=1, strip_whitespace=True), None]
    telephone_number: Union[constr(min_length=1, strip_whitespace=True), None]

    @validator('cellphone_number')
    def invaild_cellphone_number(cls, value):
        cellphone_number_Regex = re.compile(r'09\d{8}')
        cellphone_number_check = cellphone_number_Regex.search(value)
        if cellphone_number_check is None:
            raise HTTPException(
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
        return value.title()

    @validator('telephone_number')
    def invaild_telephone_number(cls, value):
        telephone_number_Regex = re.compile(r'((02|03|04|05|06|07|08)\d{8})')
        telephone_number_check = telephone_number_Regex.search(value)
        if telephone_number_check is None:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=[{
                    "loc": [
                        "body",
                        "telephone_number"
                    ],
                    "msg": "value is not a valid telephone number",
                    "type": "value_error.telephone_number"
                }]
            )
        return value.title()
