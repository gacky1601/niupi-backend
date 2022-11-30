from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4
from .schemas import User
from .service import get_user_by_id, delete_user_by_id, update_user_by_id
from .dependencies import get_db
from . import exceptions
import re

router = APIRouter()


@router.get("/{user_id}", response_model=User)
def read_user(user_id: UUID4, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise exceptions.UserNotFound

    return user


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: UUID4, db: Session = Depends(get_db)):
    if get_user_by_id(db, user_id) is None:
        raise exceptions.DeleteNonExistingUser

    delete_user_by_id(db, user_id)


@router.patch("/{user_id}", response_model=User)
def update_user(user_id: UUID4, update_data: User, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise exceptions.UpdateNonExistingUser

    update_user = update_user_by_id(db, user_id, update_data)

    cellphone_number_Regex = re.compile(r'09\d{8}')
    cellphone_number_check = cellphone_number_Regex.search(str(update_data.cellphone_number))
    if update_data.cellphone_number is None:
        return update_user
    elif cellphone_number_check is None:
        raise exceptions.InvalidCellphoneNumber
    else:
        return update_user
