from pydantic import BaseModel


class CompetitorBase(BaseModel):
    first_name : str
    last_name : str
    rating : float


class CompetitorCreate(CompetitorBase):
    pass


class Competitor(CompetitorBase):
    competitor_uid : str
    rating : int

    class Config:
        orm_mode = True


class FightBase(BaseModel):
    winner : str
    loser : str


class FightCreate(FightBase):
    pass


class Fight(FightBase):
    fight_uid : str

    class Config:
        orm_mode = True