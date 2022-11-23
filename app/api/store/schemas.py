from typing import Union
from pydantic import BaseModel, EmailStr, UUID4, Field, constr


class StoreBase(BaseModel):
    email: EmailStr
    storename: constr(min_length=1, strip_whitespace=True)


class Store(StoreBase):
    id: UUID4
    address: Union[constr(min_length=1, strip_whitespace=True), None]
    cellphone_number: Union[constr(min_length=1, strip_whitespace=True), None]
    

    class Config:
        orm_mode = True
