from typing import List
from fastapi import APIRouter

from .model import User, Tranactions, Query, Coin, Market, Record,Transaction
from ..src import data

router = APIRouter()

@router.get("/login/{name}", name="Verify User", response_model=User)
async def GetUsername(name:str):
    row = data.GetUsername(name)
    if row:
        return User(**row[0])
    else:
        value = User()
        return value
