from sqlalchemy import Boolean, PrimaryKeyConstraint, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base


class Credits(Base):
    __tablename__ = 'credits'
    person_id = Column(String)
    tmdb_id = Column(String,ForeignKey('engagement.tmdb_id',ondelete='CASCADE'))
    name = Column(String)
    role = Column(String)

    __table_args__ = ( 
        PrimaryKeyConstraint('person_id', 'tmdb_id','role'), )
    engagement  = relationship("EngagementReport", backref="credits")