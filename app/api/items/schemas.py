from typing import Optional

from pydantic import BaseModel, UUID4, constr


class Item(BaseModel):
    id: UUID4
    name: constr(min_length=1, strip_whitespace=True)
    description: Optional[constr(min_length=1, strip_whitespace=True)]
    price: int
    store_id: UUID4
    inventory: int
    photo_ids: list[UUID4]

    class Config:
        orm_mode = True


class ItemUpdate(BaseModel):
    name: constr(min_length=1, strip_whitespace=True)
    description: Optional[constr(min_length=1, strip_whitespace=True)]
    price: int
    inventory: int


class ItemCreate(BaseModel):
    store_id: UUID4
    name: constr(min_length=1, strip_whitespace=True)
    description: Optional[constr(min_length=1, strip_whitespace=True)]
    price: int
    inventory: int
    photo_ids: Optional[list[UUID4]]

    class Config:
        orm_mode = True
