from typing import Optional

from pydantic import BaseModel, UUID4, constr


class OrderItem(BaseModel):
    name: constr(min_length=1, strip_whitespace=True)
    price: int
    photo_id: UUID4
    quantity: int


class Order(BaseModel):
    store_id: UUID4
    store_name: constr(min_length=1, strip_whitespace=True)
    items: list[OrderItem]
    recipient: constr(min_length=1, strip_whitespace=True)
    recipient_telephone_number: Optional[constr(min_length=1, strip_whitespace=True)]
    address: constr(min_length=1, strip_whitespace=True)
    sub_total: int
    shipping_fee: int
    total_amount: int

    class Config:
        orm_mode = True
