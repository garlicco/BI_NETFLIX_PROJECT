from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects, Float
from sqlalchemy.orm import relationship
from database import Base

class MoviesRevenues(Base):
    __tablename__ = 'movies_revenues'

    revenue_id = Column(Integer, primary_key=True)
    budget = Column(Float)
    imdb_id = Column(String)  # Foreign key to ImdbRating
    revenue = Column(Float)
    profit = Column(Float)