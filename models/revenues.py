from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects, Float
from sqlalchemy.orm import relationship
from database import Base

class Revenues(Base):
    __tablename__ = 'revenues'

    revenue_id = Column(String, primary_key=True)
    budget = Column(Float)
    revenue = Column(Float)
    profit = Column(Float)
