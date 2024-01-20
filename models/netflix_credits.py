from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base


class NetflixCredits(Base):
    __tablename__ = 'netflix_credits'

    cast_id = Column(Integer, primary_key=True)
    tmdb_id = Column(String)
    actors = Column(String)
    directors = Column(String)