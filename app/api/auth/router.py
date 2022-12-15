import bcrypt
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .dependencies import get_db
from .exceptions import EmailExists, InvalidEmailOrPassword
from .schemas import LoginResponse, User, UserCreate, UserLogin
from .service import create_user, get_user_by_email

router = APIRouter()


@router.post("/signup", response_model=User)
def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)

    if db_user:
        raise EmailExists

    return create_user(db, user)


@router.get('/login', response_model=LoginResponse)
def sing_in(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)

    if db_user is None:
        raise InvalidEmailOrPassword

    password = user.password.encode('utf-8')
    correct_hashed_password = db_user.hashed_password.encode('utf-8')
    if not bcrypt.checkpw(password, correct_hashed_password):
        raise InvalidEmailOrPassword

    return db_user
