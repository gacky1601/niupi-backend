from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4
from .schemas import User
from .service import get_user_by_id
from .dependencies import get_db
from .exceptions import UserNotFound

router = APIRouter()


@router.get("/{user_id}", response_model=User)
def read_user(user_id: UUID4, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise UserNotFound

    return user
