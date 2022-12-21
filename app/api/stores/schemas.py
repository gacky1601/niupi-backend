from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr, constr

from app.utils.validator import cellphone_number_regex, telephone_number_regex


class Address(BaseModel):
    county: Optional[constr(min_length=1, strip_whitespace=True)]
    district: Optional[constr(min_length=1, strip_whitespace=True)]
    detail: Optional[constr(min_length=1, strip_whitespace=True)]


class Store(BaseModel):
    id: UUID4
    seller_id: UUID4
    name: Optional[constr(min_length=1, strip_whitespace=True)]
    address: Address
    email: Optional[EmailStr]
    cellphone_number: Optional[constr(min_length=1, strip_whitespace=True)]
    telephone_number: Optional[constr(min_length=1, strip_whitespace=True)]

    class Config:
        orm_mode = True


class StoreUpdate(BaseModel):
    name: Optional[constr(min_length=1, strip_whitespace=True)]
    county_id: Optional[int]
    district_id: Optional[int]
    detail_address: Optional[constr(min_length=1, strip_whitespace=True)]
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
    photo: Optional[UUID4]
