from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .dependencies import get_db
from .service import get_districts

router = APIRouter()


@router.get("")
def read_districts(database: Session = Depends(get_db)):
    return get_districts(database)
