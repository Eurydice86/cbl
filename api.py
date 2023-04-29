''' Main functionality of the API '''
from fastapi import Depends, FastAPI#, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    '''Open the database'''
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


@app.post("/competitors", response_model=schemas.Competitor)
def create_competitor(
    competitor: schemas.CompetitorCreate,
    database: Session = Depends(get_db)
    ):
    ''' Create a new competitor and add them to the database '''
    return crud.create_competitor(
        database=database,
        competitor=competitor
        )




@app.get("/competitors", response_model=list[schemas.Competitor])
def list_competitors(database: Session = Depends(get_db)):
    '''Get a list of all competitors'''
    competitors = crud.get_competitors(database)
    return competitors

@app.get("/competitors/{uid}", response_model=schemas.Competitor)
def show_competitor_details(uid: str, database: Session = Depends(get_db)):
    '''Get a list of the competitor with given uid'''
    competitor = crud.get_competitor(uid, database)
    return competitor

@app.get("/ranking/{top_n}", response_model=list[schemas.Competitor])
def show_top_n_competitors(top_n: int,
                       database: Session = Depends(get_db)):
    '''Get a descending sorted list of the top 10 competitors by rating'''
    competitors = crud.get_competitors_ranked(database, limit=top_n)
    return competitors


@app.get("/fights/", response_model=list[schemas.Fight])
def list_fights(database: Session = Depends(get_db)):
    '''Get a list of all fights'''
    fights = crud.get_fights(database)
    return fights

