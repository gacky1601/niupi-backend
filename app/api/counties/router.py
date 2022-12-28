from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .dependencies import get_db
from .service import get_county_ids

router = APIRouter()


@router.get("")
def read_counties(database: Session = Depends(get_db)):
    return get_county_ids(database)
