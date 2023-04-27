'''deals with the CRUD functionality'''
from sqlalchemy.orm import Session
import models
# import schemas


def get_competitors(database: Session, skip: int = 0, limit: int = 100):
    ''' Get competitor list from the database '''
    return database.query(models.Competitor).offset(skip).limit(limit).all()
