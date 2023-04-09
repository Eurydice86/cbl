'''Deals with database creation and ORM functions'''

from datetime import datetime
import uuid
from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import exists

SQLALCHEMY_DATABASE_URL = "sqlite:///database/test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=False) # set echo true for logging
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()
Base = declarative_base()


class Competitor(Base):
    '''class for the fighters table in the database'''
    __tablename__ = "competitors"
    competitor_uid = Column("competitor_uid", String, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    rating = Column("rating", Float)
    creation_timestamp = Column("creation_timestamp", DateTime(timezone=True), default=datetime.now)

    def __init__(self, first_name, last_name):
        self.competitor_uid = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.rating = 1000

    def __str__(self):
        return f"{self.competitor_uid}: {self.first_name} {self.last_name}, Rating: {self.rating}"


class Fight(Base):
    '''class for the fights table in the database'''
    __tablename__ = "fights"
    fight_uid = Column("fight_uid", String, primary_key=True)
    winner = Column("winner_uid", String)
    loser = Column("loser_uid", String)
    timestamp = Column("timestamp", DateTime(timezone=True), default=datetime.now)

    def __init__(self, winner, loser):
        self.fight_uid = str(uuid.uuid4())
        self.winner = winner
        self.loser = loser

    def __str__(self):
        return f"\n{self.fight_uid}\nWinner: {self.winner}, Loser: {self.loser}\n"


def create_competitor(competitor : Competitor):
    '''creates a Competitor entry and adds it to the database'''
    full_name : str = competitor.first_name + competitor.last_name
    check = session.query(exists().\
        where(Competitor.first_name + Competitor.last_name == full_name)).scalar()
    if check:
        print("The competitor already exists in the database")
        return
    else:
        session.add(competitor)
        session.commit()
        print("\nThe competitor")
        print(competitor)
        print("was added to the database.\n")
        return


def log_fight(fight : Fight):
    '''creates a Fight entry and adds it to the database'''
    session.add(fight)
    session.commit()
    return

def update_elo(uid : str, new_rating : float):
    '''updates the elo rating of a competitor given their uid and the new rating'''
    session.query(Competitor).filter(Competitor.competitor_uid == uid).\
        update({Competitor.rating : new_rating}, synchronize_session=False)
    session.commit()


def query_by_full_name(first_name, last_name):
    '''returns the competitor_uid from the full name'''
    result = session.query(Competitor).\
        filter(Competitor.first_name == first_name).\
        filter(Competitor.last_name == last_name)
    for row in result:
        return row.competitor_uid

def list_all_competitors():
    '''returns a list of all competitors'''
    competitors_dict = []
    result = session.query(Competitor).order_by(Competitor.last_name.asc())
    for row in result:
        entry = {"last_name" : row.last_name, "first_name" : row.first_name}
        competitors_dict.append(entry)
    return competitors_dict
