from typing import Union
from pydantic import BaseModel, EmailStr, UUID4, constr, validator
from .exceptions import InvalidCellphoneNumber, InvalidTelephoneNumber
import re


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


class update_Store(BaseModel):
    name: constr(min_length=1, strip_whitespace=True)
    address: Union[constr(min_length=1, strip_whitespace=True), None]
    email: Union[EmailStr, None]
    cellphone_number: Union[constr(min_length=1, strip_whitespace=True), None]
    telephone_number: Union[constr(min_length=1, strip_whitespace=True), None]

    @validator('cellphone_number')
    def invaild_cellphonenumber(cls, value):
        cellphone_number_Regex = re.compile(r'09\d{8}')
        cellphone_number_check = cellphone_number_Regex.search(value)
        if cellphone_number_check is None:
            raise InvalidCellphoneNumber
        return value.title()

    @validator('telephone_number')
    def invaild_telephonenumber(cls, value):
        telephone_number_Regex = re.compile(r'((02|03|04|05|06|07|08)\d{8})')
        telephone_number_check = telephone_number_Regex.search(value)
        if telephone_number_check is None:
            raise InvalidTelephoneNumber
        return value.title()
