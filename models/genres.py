from sqlalchemy import Boolean, PrimaryKeyConstraint, Column,  ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base


class Genres(Base):
    __tablename__ = 'genres'

    genre_id = Column(String, ForeignKey('engagement.movie_id',ondelete='CASCADE'),primary_key=True )
    genres = Column(String)
    
    engagement = relationship ("EngagementReport", backref="genres")
