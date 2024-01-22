from sqlalchemy import PrimaryKeyConstraint,ForeignKeyConstraint, Boolean, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base
class Engagement(Base):
    __tablename__ = 'engagement'

    movie_id = Column(String, primary_key=True, unique=True)
    tmdb_id = Column(String, unique=True)
    title = Column(String)
    hours_viewed = Column(Integer)
    global_availability = Column(String)
    release_year=Column(Integer)
    type=Column(String)
    age_certification =Column(String)