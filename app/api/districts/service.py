from sqlalchemy.orm import Session

from .models import District


def get_districts(database: Session):
    return database.query(District).all()
