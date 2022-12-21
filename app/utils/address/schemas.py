from typing import Optional

from pydantic import BaseModel, constr


class Address(BaseModel):
    county: Optional[constr(min_length=1, strip_whitespace=True)]
    district: Optional[constr(min_length=1, strip_whitespace=True)]
    detail: Optional[constr(min_length=1, strip_whitespace=True)]
