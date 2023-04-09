'''deals with the CRUD functionality'''
from sqlalchemy.orm import Session
import models, schemas

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Competitor).offset(skip).limit(limit).all()
