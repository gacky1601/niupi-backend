from typing import Union
from pydantic import BaseModel, UUID4, constr


class Item(BaseModel):
    id: UUID4
    name: constr(min_length=1, strip_whitespace=True)
    description: str
    price: int
    store_id: UUID4
    inventory: int

    class Config:
        orm_mode = True
