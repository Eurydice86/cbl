''' Main functionality of the API '''
from fastapi import Depends, FastAPI#, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    '''Open the database'''
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

@app.get("/")
def main_page():
    '''Get the main page'''
    return "Main page"

@app.get("/competitors/", response_model=list[schemas.Competitor])
def list_competitors(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    '''Get a list of all competitors'''
    competitors = crud.get_competitors(database, skip=skip, limit=limit)
    return competitors
