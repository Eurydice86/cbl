''' deals with the CRUD functionality on the database (queries, insertions, etc) '''
import uuid
from sqlalchemy.orm import Session
import models
import schemas


def get_competitors(database: Session):
    ''' Get competitor list from the database '''
    return database.query(
        models.Competitor
        ).all()

def get_competitor(uid, database: Session):
    ''' Get competitor list from the database '''
    return database.query(
        models.Competitor
        ).where(
        models.Competitor.competitor_uid == uid
        ).first()


def get_fights(database: Session):
    ''' Get competitor list from the database '''
    return database.query(models.Fight).all()

def get_competitors_ranked(database: Session, limit: int = 10):
    ''' Get competitor list from the database and sort them by rating (descending)'''
    return database.query(
        models.Competitor
        ).order_by(
        models.Competitor.rating.desc()
        ).limit(
        limit
        ).all()

def create_competitor(database: Session, competitor: schemas.CompetitorCreate, first_name: str, last_name: str):
    ''' Create a new competitor and add them to the database '''
    uid = str(uuid.uuid4())
    db_competitor = models.Competitor(
        first_name=first_name,
        last_name=last_name,
        competitor_uid= uid,
        rating= 1000.0)
    database.add(db_competitor)
    database.commit()
    database.refresh(db_competitor)
    return db_competitor












def main():
    print("main starts")
    from database import SessionLocal
    #comp = get_competitor(uid="941c1c8a-8ab1-46e9-92ad-ea7081c1e252", database=SessionLocal())

    #comp = create_competitor(database=SessionLocal(), first_name="John", last_name="Doe")
    #print(comp.competitor_uid, comp.first_name, comp.last_name, comp.rating)


if __name__ == "__main__":
    main()