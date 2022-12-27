from typing import Optional

from pydantic import BaseModel, UUID4, constr


class OrderItem(BaseModel):
    name: constr(min_length=1, strip_whitespace=True)
    price: int
    photo_id: UUID4
    quantity: int


class Orders(BaseModel):
    store_id: UUID4
    store_name: constr(min_length=1, strip_whitespace=True)
    items: list[OrderItem]
    recipient: constr
    recipient_telephone_number: constr
    address: constr
    sub_total: int
    shipping_fee: int
    total_amount: int

    class Config:
        orm_mode = True
