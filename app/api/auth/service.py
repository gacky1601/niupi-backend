import bcrypt
from sqlalchemy.orm import Session

from app.api.stores.models import Store
from .models import User
from . import schemas


def get_user_by_email(database: Session, email: str):
    statement = (
        f"""
        SELECT users.*, store.id AS store_id
        FROM users
        JOIN store
        ON users.id=store.user_id
        WHERE users.email='{email}'
        """
    )

    return database.execute(statement).first()


def create_user(db: Session, user: schemas.UserCreate):
    password = user.password.encode("utf-8")
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")

    new_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        role_id=0,
    )

    new_store = Store(
        seller_id=new_user.id
    )

    new_user.store = new_store

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
