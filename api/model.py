import datetime
from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy import Date, Time


class IndividualsInSquadron(BaseModel):
    callsign: str
    commander: bool
    executive: bool
    position: str

    class Config:
        orm_mode = True


class SquadronLogs(BaseModel):
    callsign: str
    name: str
    missionname: str
    aakills: int
    agkills: int
    takeoffdate: datetime.date
    takeofftime: datetime.time
    landingdata: datetime.date
    landingtime: datetime.time

    class Config:
        orm_mode = True


class IndividualLog(BaseModel):
    name: str
    missionname: str
    aakills: int
    agkills: int
    takeoffdate: datetime.date
    takeofftime: datetime.time
    landingdata: datetime.date
    landingtime: datetime.time

    class Config:
        orm_mode = True


class Callsign(BaseModel):
    callsign: str

    class Config:
        orm_mode = True


class Map(BaseModel):
    id: int = 0
    name: str = ''

    class Config:
        orm_mode = True


class Squad(BaseModel):
    id: int
    name: str
    aircraftid: int

    class Config:
        orm_mode = True


class AC(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Rank(BaseModel):
    id: int = 0
    position: str = ''

    class Config:
        orm_mode = True


class Miss(BaseModel):
    name: str
    description: str
    createddate: datetime.date
    mapid: int

    class Config:
        orm_mode = True
