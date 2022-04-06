from pydantic import BaseModel, validator
from typing import Optional
from datetime import date
from datetime import datetime


class Individual(BaseModel):
    callsign: str = ''
