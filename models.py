'''deals with the database models'''

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, UUID
# from sqlalchemy.orm import relationship
from database import Base


class Competitor(Base):
    '''class for the fighters table in the database'''
    __tablename__ = "competitors"
    default_uid = uuid.uuid4

    competitor_uid = Column(UUID(as_uuid=True), primary_key=True, default=default_uid)
    first_name = Column(String)
    last_name = Column(String)
    rating = Column(Float, default=1000.0)
    creation_timestamp = Column(DateTime(timezone=True), default=datetime.now)


class Fight(Base):
    '''class for the fights table in the database'''
    __tablename__ = "fights"
    fight_uid = Column(String, primary_key=True)
    winner = Column(String, ForeignKey("competitors.competitor_uid"))
    loser = Column(String, ForeignKey("competitors.competitor_uid"))
    timestamp = Column(DateTime(timezone=True), default=datetime.now)
