from sqlalchemy.orm import Session

from .models import County


def get_county_ids(database: Session):
    return database.query(County).all()
