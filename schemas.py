''' Pydantic schemas setup '''
from pydantic import BaseModel


class CompetitorBase(BaseModel):
    ''' Model for the Competitor class '''
    first_name : str
    last_name : str
    rating : float


class CompetitorCreate(CompetitorBase):
    ''' Creation of the Competitor class '''


class Competitor(CompetitorBase):
    ''' Competitor class '''
    competitor_uid : str
    rating : int

    class Config:
        ''' configuration of the class '''
        orm_mode = True


class FightBase(BaseModel):
    ''' Model for the Fight class '''
    winner : str
    loser : str


class FightCreate(FightBase):
    ''' Creation of the Fight class '''


class Fight(FightBase):
    ''' Fight class '''
    fight_uid : str

    class Config:
        ''' configuration of the class '''
        orm_mode = True
