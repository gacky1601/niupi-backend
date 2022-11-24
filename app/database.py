from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import config, Environment

SQLALCHMY_DATABASE_URL = config.POSTGRESS_ADDRESS

engine = create_engine(SQLALCHMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def initialize_db():
    if config.ENV == Environment.DEVELOPMENT:
        Base.metadata.drop_all(engine)

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    if config.ENV == Environment.DEVELOPMENT:
        # initialize role table
        from .api.user.models import Role

        roles = ["admin", "user"]
        for index, role in enumerate(roles):
            new_role = Role(id=index, role=role)
            db.add(new_role)

        db.commit()

        db.close()
