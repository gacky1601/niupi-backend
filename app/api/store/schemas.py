from typing import Union
from pydantic import BaseModel, EmailStr, UUID4, Field, constr


class Store(BaseModel):
    id: UUID4
    user_id: UUID4
    name: Union[constr(min_length=1, strip_whitespace=True), None]
    address: Union[constr(min_length=1, strip_whitespace=True), None]
    email: Union[constr(min_length=1, strip_whitespace=True), None]
    cellphone_number: Union[constr(min_length=1, strip_whitespace=True), None]
    telephone_number: Union[constr(min_length=1, strip_whitespace=True), None]

    class Config:
        orm_mode = True
