from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4
from .schemas import User, UserUpdate
from .service import get_user_by_id, delete_user_by_id, update_user
from .dependencies import get_db
from .exceptions import UserNotFound, DeleteNonExistingUser, UpdateNonExistingUser


router = APIRouter()


@router.get("/{user_id}", response_model=User)
def read_user(user_id: UUID4, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise UserNotFound

    return user


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: UUID4, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise DeleteNonExistingUser

    delete_user_by_id(db, user_id)


@router.patch("/{user_id}", response_model=User)
def update_user_(user_id: UUID4, payload: UserUpdate, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise UpdateNonExistingUser

    update = update_user(db, user_id, payload)

    return update
