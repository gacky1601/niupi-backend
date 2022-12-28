from sqlalchemy import Column, ForeignKey, Integer, String

from app.database import Base


class District(Base):
    __tablename__ = "district"

    id = Column(Integer, primary_key=True)
    county_id = Column(Integer, ForeignKey("county.id"))
    name = Column(String)
