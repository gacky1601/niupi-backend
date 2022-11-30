from typing import Union
from pydantic import BaseModel, EmailStr, UUID4, constr, validator
from .exceptions import InvalidCellphoneNumber, InvalidTelephoneNumber


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
    def invaild_cellphonenumber(cls, v):
        if ' ' in v:
            raise InvalidCellphoneNumber
        if len(v) != 10:
            raise InvalidCellphoneNumber
        return v.title()

    @validator('telephone_number')
    def invaild_telephonenumber(cls, v):
        if ' ' in v:
            raise InvalidTelephoneNumber
        if len(v) != 10:
            raise InvalidTelephoneNumber
        return v.title()
