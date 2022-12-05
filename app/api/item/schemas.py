from typing import Optional
from pydantic import BaseModel, UUID4, constr


class item(BaseModel):
    id: UUID4
    name: constr(min_length=1, strip_whitespace=True)
    description: Optional[constr(min_length=1, strip_whitespace=True)]
    price: int
    store_id: UUID4
    inventory: int
    photos: list[UUID4]

    class Config:
        orm_mode = True
