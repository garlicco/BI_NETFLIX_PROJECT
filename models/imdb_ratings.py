from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects, Float
from sqlalchemy.orm import relationship
from database import Base


class ImdbRating(Base):
    __tablename__ = 'imdb_ratings'

    imdb_id = Column(String, primary_key=True)
    average_rating = Column(Float)
    num_votes = Column(Integer)