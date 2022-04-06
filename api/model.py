from pydantic import BaseModel, validator
from typing import Optional
from datetime import date
from datetime import datetime


class Individual(BaseModel):
    callsign: str = ''
    squadronId: int = 0
    rankId: int = 0
    flightLead: bool = False
    commander: bool = False
    executive: bool = False
    admin: bool = False
    moderator: bool = False
    flightInstructor: bool = False

    class Config:
        rom_mode = True
