from sqlalchemy.orm import Session

from . import models
from . import schemas
import bcrypt


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    password = user.password.encode("utf-8")
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")

    db_user = models.User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        role_id=0,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
