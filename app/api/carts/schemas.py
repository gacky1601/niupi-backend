from typing import Optional
import datetime

from fastapi import HTTPException, status
from pydantic import BaseModel, UUID4, constr


class CartItem(BaseModel):
    name: Optional[constr(min_length=1, strip_whitespace=True)]
    price: int
    photo_id: list[UUID4]
    updated_at: datetime.datetime = None
    quantity: int


class CartStore(BaseModel):
    id: UUID4
    name: Optional[constr(min_length=1, strip_whitespace=True)]
    items: list[CartItem]


class Cart(BaseModel):
    cart_id: UUID4
    stores: list[CartStore]

    class Config:
        orm_mode = True
