from sqlalchemy import Date, Boolean, Column, ForeignKey, Integer, String, DateTime, Enum, Float, dialects
from sqlalchemy.orm import relationship
from database import Base


class ImdbRating(Base):

    __tablename__ = 'fact_imdb_ratings'
    imdb_id = Column(String,primary_key=True)
   
    movie_id = Column(String, ForeignKey(
        'engagement.movie_id',ondelete='CASCADE'),nullable=True)
    revenue_id = Column(String, ForeignKey(
        'revenues.revenue_id',ondelete='CASCADE'),nullable=True)
    region_id = Column(String, ForeignKey(
        'regions.region_id',ondelete='CASCADE'),nullable=True)
    genre_id = Column(String, ForeignKey(
        'genres.genre_id',ondelete='CASCADE'),nullable=True)
    
    average_rating = Column(Float)

    revenues = relationship("Revenues", backref="fact_imdb_ratings")
    genres = relationship("Genres", backref="fact_imdb_ratings")
    engagement = relationship("Engagement", backref="fact_imdb_ratings")
    regions = relationship ("Regions", backref="fact_imdb_ratings")