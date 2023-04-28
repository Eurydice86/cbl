''' deals with the CRUD functionality on the database (queries, insertions, etc) '''
from sqlalchemy.orm import Session
import models
import schemas
import uuid


def get_competitors(database: Session):
    ''' Get competitor list from the database '''
    return database.query(models.Competitor).all()

def get_competitor(uid, database: Session):
    ''' Get competitor list from the database '''
    return database.query(models.Competitor).where(models.Competitor.competitor_uid == uid).first()


def get_fights(database: Session):
    ''' Get competitor list from the database '''
    return database.query(models.Fight).all()

def get_competitors_ranked(database: Session, limit: int = 10):
    ''' Get competitor list from the database and sort them by rating (descending)'''
    return database.query(models.Competitor).order_by(models.Competitor.rating.desc()).limit(limit).all()


if __name__ == "__main__":
    from database import SessionLocal
    comp = get_competitor(uid="941c1c8a-8ab1-46e9-92ad-ea7081c1e252", database=SessionLocal())
    print(comp.competitor_uid, comp.first_name, comp.last_name, comp.rating)
