from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class County(Base):
    __tablename__ = "county"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    districts = relationship("District")


class District(Base):
    __tablename__ = "district"

    id = Column(Integer, primary_key=True)
    county_id = Column(Integer, ForeignKey("county.id"))
    name = Column(String)
