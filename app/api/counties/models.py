from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class County(Base):
    __tablename__ = "county"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    districts = relationship("District")
