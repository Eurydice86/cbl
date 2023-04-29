''' Pydantic schemas setup '''
from pydantic import BaseModel
import uuid


class CompetitorBase(BaseModel):
    ''' Model for the Competitor class '''
    first_name: str
    last_name: str

class CompetitorCreate(CompetitorBase):
    ''' Creation of the Competitor class '''


class Competitor(CompetitorBase):
    ''' Competitor class '''
    competitor_uid: uuid.UUID
    rating: float

    class Config:
        ''' configuration of the class '''
        orm_mode = True


class FightBase(BaseModel):
    ''' Model for the Fight class '''
    winner : str
    loser : str
    fight_uid : str

class FightCreate(FightBase):
    ''' Creation of the Fight class '''


class Fight(FightBase):
    ''' Fight class '''


    class Config:
        ''' configuration of the class '''
        orm_mode = True
