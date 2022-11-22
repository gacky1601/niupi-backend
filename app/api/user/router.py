from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4
from .schemas import User
from .service import get_user_by_id
from .service import delete_user_by_id
from .dependencies import get_db
from .exceptions import UserNotFound
from .exceptions import UserNotExist

router = APIRouter()


@router.get("/{user_id}", response_model=User)
def read_user(user_id: UUID4, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise UserNotFound

    return user


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: UUID4, db: Session = Depends(get_db)):
    if get_user_by_id(db, user_id) is None:
        raise UserNotExist

    delete_user_by_id(db, user_id)
