from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base

class NetflixLibrary(Base):
    __tablename__ = 'netflix_library'

    movie_show_id = Column(Integer, primary_key=True)
    tmdb_id = Column(String)
    title = Column(String)
    type = Column(String)
    release_year = Column(Integer)
    runtime = Column(Integer)
    genres = Column(String)
    production_countries = Column(String)
    imdb_id = Column(String) 