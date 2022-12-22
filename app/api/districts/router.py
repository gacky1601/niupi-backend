from fastapi import APIRouter

from app.utils.districts import districts

router = APIRouter()


@router.get("")
def read_districts():
    return districts
