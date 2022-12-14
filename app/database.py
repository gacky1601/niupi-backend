from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import config, Environment

SQLALCHMY_DATABASE_URL = config.POSTGRESS_ADDRESS

engine = create_engine(SQLALCHMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def initialize_database():
    if config.ENV == Environment.DEVELOPMENT:
        Base.metadata.drop_all(engine)

    Base.metadata.create_all(bind=engine)

    if config.ENV == Environment.DEVELOPMENT:
        database = SessionLocal()

        # initialize role table
        from .api.user.models import Role

        roles = ["admin", "user"]
        for index, role in enumerate(roles):
            new_role = Role(id=index, role=role)
            database.add(new_role)

        from .utils.districts import initialize_county_table, initialize_district_table

        initialize_county_table(database)
        initialize_district_table(database)

        database.commit()

        database.close()
