from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import model
import tables
import crud
from database import SessionLocal, engine

tables.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    'http://localhost:3000'
]

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db

@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users

@app.get("/individual/{squadron}", name="Get Individual in Squadron",)
async def GetIndividualInSquadron(squadron: str, db: Session = Depends(get_db)):
    squadronRoster = crud.getIndividualsInSquadron(db, squadron)
    return squadronRoster

    # cur = prom.cursor()
    # query = "SELECT callsign FROM roster WHERE squadronID = (SELECT id FROM squadron WHERE name='" + squadron + "')"
    # print(query)
    # # cur.execute(query)
    # # response = cur.fetchall()
    # # print(response)
    # with engine.connect() as connection:
    #     result = connection.execute(query)
    #
    # print(result)
    # value = []
    # for resp in response:
    #     value.append(Individual(**resp))
    # return value
