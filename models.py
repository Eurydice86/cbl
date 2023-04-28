'''deals with the database models'''

# import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
from database import Base


class Competitor(Base):
    '''class for the fighters table in the database'''
    __tablename__ = "competitors"
    competitor_uid = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    rating = Column(Float)
    creation_timestamp = Column(DateTime(timezone=True), default=datetime.now)


class Fight(Base):
    '''class for the fights table in the database'''
    __tablename__ = "fights"
    fight_uid = Column(String, primary_key=True)
    winner = Column(String, ForeignKey("competitors.competitor_uid"))
    loser = Column(String, ForeignKey("competitors.competitor_uid"))
    timestamp = Column(DateTime(timezone=True), default=datetime.now)
