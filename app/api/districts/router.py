from fastapi import APIRouter

from app.utils.address import districts

router = APIRouter()


@router.get("")
def read_districts():
    return districts
