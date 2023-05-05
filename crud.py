''' deals with the CRUD functionality on the database (queries, insertions, etc) '''
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
    ''' Get a list of all the fights from the database '''
    return database.query(models.Fight).all()

def get_competitors_ranked(database: Session, limit: int = 10):
    ''' Get competitor list from the database and sort them by rating (descending)'''
    return database.query(
        models.Competitor
        ).order_by(
        models.Competitor.rating.desc(),
        models.Competitor.last_name.asc()
        ).limit(
        limit
        ).all()

def create_competitor(
        database: Session,
        competitor: schemas.CompetitorCreate,
        ):
    ''' Create a new competitor and add them to the database '''
    db_competitor=models.Competitor(
        first_name=competitor.first_name,
        last_name=competitor.last_name
        )

    database.add(db_competitor)
    database.commit()
    database.refresh(db_competitor)
    return db_competitor



def log_fight(
        database: Session,
        fight: schemas.FightCreate,
        ):
    ''' Create a new fight and add it to the database '''
    db_fight=models.Fight(
        winner_uid=fight.winner_uid,
        loser_uid=fight.loser_uid
        )

    database.add(db_fight)
    database.commit()
    database.refresh(db_fight)
    return db_fight










def main():
    ''' Use crud as main '''

if __name__ == "__main__":
    main()
