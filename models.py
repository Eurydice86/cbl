'''deals with the database models'''

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Competitor(Base):
    '''class for the fighters table in the database'''
    __tablename__ = "competitors"
    competitor_uid = Column("competitor_uid", String, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    rating = Column("rating", Float)
    creation_timestamp = Column("creation_timestamp", DateTime(timezone=True), default=datetime.now)

    fights = relationship("Fight", back_populates="competitor")


class Fight(Base):
    '''class for the fights table in the database'''
    __tablename__ = "fights"
    fight_uid = Column("fight_uid", String, primary_key=True)
    winner = Column("winner_uid", String, ForeignKey("competitors.competitor_uid"))
    loser = Column("loser_uid", String)
    timestamp = Column("timestamp", DateTime(timezone=True), default=datetime.now)

    competitor = relationship("Competitor", back_populates="fights")
