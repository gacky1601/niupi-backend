from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import config

SQLALCHMY_DATABASE_URL = config.POSTGRESS_ADDRESS

engine = create_engine(SQLALCHMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def initialize_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    from .api.user.models import Role

    # initialize role table
    roles = ["admin", "user"]
    for index, role in enumerate(roles):
        new_role = Role(id=index, role=role)
        db.add(new_role)

    db.commit()

    db.close()