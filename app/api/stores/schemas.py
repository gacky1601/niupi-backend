from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr, constr

from app.utils.validator import cellphone_number_regex, telephone_number_regex


class Store(BaseModel):
    id: UUID4
    seller_id: UUID4
    name: Optional[constr(min_length=1, strip_whitespace=True)]
    address: Optional[constr(min_length=1, strip_whitespace=True)]
    email: Optional[EmailStr]
    cellphone_number: Optional[constr(min_length=1, strip_whitespace=True)]
    telephone_number: Optional[constr(min_length=1, strip_whitespace=True)]

    class Config:
        orm_mode = True


class StoreUpdate(BaseModel):
    name: Optional[constr(min_length=1, strip_whitespace=True)]
    address: Optional[constr(min_length=1, strip_whitespace=True)]
    email: Optional[EmailStr]

    cellphone_number: Optional[
        constr(
            min_length=1,
            strip_whitespace=True,
            regex=cellphone_number_regex
        )
    ]

    telephone_number: Optional[
        constr(
            min_length=1,
            strip_whitespace=True,
            regex=telephone_number_regex
        )
    ]


class SearchItem(BaseModel):
    item_id: UUID4
    store_id: UUID4
    name: constr(min_length=1, strip_whitespace=True)
    price: int
    inventory: int
    photos: Optional[UUID4]
