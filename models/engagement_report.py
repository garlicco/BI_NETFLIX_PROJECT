from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base

class NetflixEngagement(Base):
    __tablename__ = 'netflix_engagement'

    engagement_id = Column(Integer, primary_key=True)
    title = Column(String)
    hours_viewed = Column(Integer)
    global_availability = Column(String)

    # Foreign keys to dimension tables
    movie_show_id = Column(Integer, ForeignKey('netflix_library.movie_show_id'))
    cast_id = Column(Integer, ForeignKey('netflix_credits.cast_id'))
    revenue_id = Column(Integer, ForeignKey('movies_revenues.revenue_id'))
    imdb_id = Column(String, ForeignKey('imdb_ratings.imdb_id'))
