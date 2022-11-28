from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .service import create_user, get_user_by_email
from .schemas import UserCreate
from .dependencies import get_db
from .exceptions import EmailExists
from app.api.user.schemas import User

router = APIRouter()


@router.post("/signup", response_model=User)
def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)

    if db_user:
        raise EmailExists

    return create_user(db, user)
