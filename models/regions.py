from sqlalchemy import Boolean, PrimaryKeyConstraint, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base


class Regions(Base):
    __tablename__ = 'regions'

    region_id = Column(String, primary_key=True)
    regions = Column(String)
