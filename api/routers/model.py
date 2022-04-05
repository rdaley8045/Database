from pydantic import BaseModel, validator
from typing import Optional
from datetime import date
from datetime import datetime

class User (BaseModel):
    id: int = 0
    username: str = ''
