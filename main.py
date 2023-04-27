from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def main_page():
    return "Main page"

@app.get("/competitors/", response_model=list[schemas.Competitor])
def list_competitors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    competitors = crud.get_competitors(db, skip=skip, limit=limit)
    return competitors


@app.get("/competitors2/", response_model=list[schemas.Competitor])
def list_competitors2(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    competitors = crud.get_competitors(db, skip=skip, limit=limit)
    print(competitors)
