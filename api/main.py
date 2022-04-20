from datetime import date, time
from typing import List

from fastapi import Depends, FastAPI, Request, Response
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import crud
import tables
from api.model import IndividualsInSquadron, SquadronLogs, IndividualLog, Callsign, Map, Squad, AC, Rank, Miss
from database import SessionLocal, engine

tables.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    'http://localhost:3000',
    'http://127.0.0.1:5000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/individual/{squadron}", name="Get Individual in Squadron", response_model=List[IndividualsInSquadron])
def GetIndividualInSquadron(squadron: str, db: Session = Depends(get_db)):
    return crud.getIndividualsInSquadron(db, squadron)


@app.get("/squadronLogs/{squadron}", name="Get Flight Logs for an entire squadron",response_model=List[SquadronLogs])
def GetSquadronLogs(squadron: str, db: Session = Depends(get_db)):
    return crud.getSqudronLogs(db, squadron)


@app.get("/individualLogs/{callsign}", name="Get Flight Logs for individual pilots", response_model=List[IndividualLog])
def GetIndividualLogs(callsign: str, db: Session = Depends(get_db)):
    return crud.getIndividualLogs(db, callsign)


# Individuals with select duty per squadron
@app.get("/individualsDutiesPerSquadron/{squadron}/{flightlead}/{commander}/{exo}/{instructor}",
         name="Get individuals with a select duty per Squadron", response_model=List[Callsign])
def GetIndividualDutiesPerSquadron(squadron: str, flightlead: bool, commander: bool, exo: bool,
                                   instructor: bool, db: Session = Depends(get_db)):
    return crud.getIndividualDutiesPerSquadron(db, squadron, flightlead, commander, exo, instructor)


# Indviduals with select duty all
@app.get("/individualsSelectDuty/{flightlead}/{commander}/{exo}/{instructor}",
         name="Get individuals with a select duty", response_model= List[Callsign])
def GetIndividualsSelectDuty(flightlead: bool, commader: bool, exo: bool, instructor: bool, db: Session = Depends(
    get_db)):
    return crud.getIndividualsSelectDuty(db, flightlead, commader, exo, instructor)


# Individuals with select permissions
@app.get("/individualSelectPermissions/{admin}/{moderator}", name="Get Individual with permissions",
         response_model=List[Callsign])
def GetIndividualSelectPermissions(admin: bool, moderator: bool, db: Session = Depends(get_db)):
    return crud.getIndividualSelectPermissions(db, admin, moderator)


# Individuals with select permissions per squadron
@app.get("/individualSelectPermissionsPerSquadron/{squadron}/{admin}/{moderator}",
         name="Get Individuals a select squadron with a set permissions", response_model=List[Callsign])
def GetIndividaulsSelectPermissionsPerSquadron(squadron: str, admin: bool, moderator: bool,
                                               db: Session = Depends(get_db)):
    return crud.getIndividualsSelectPermissionsPerSquadron(squadron, admin, moderator, db)


# enter new mission
@app.post("/mission/{name}/{createDate}/{mapId}/{description}", name="Enter in new mission")
def CreateMission(name: str, createDate: date, mapId: int, description: str, db: Session = Depends(get_db)):
    crud.createMission(name, createDate, mapId, description, db)


# get list of maps
@app.get("/maps", name="Get list of Maps with ID", response_model=List[Map])
def Maps(db: Session = Depends(get_db)):
    return crud.getMaps(db)


# enter new flight log
@app.post("/addFlightLog/{id}/{callsign}/{acId}/{sqId}/{offDate}/{offTime}/{landDate}/{landTime}/{aa}/{ag}/{mission}", )
def AddFlightLog(id: int, callsign: str, acId: int, sqId: int, offDate: date, offTime: time, landDate: date,
                 landTime: time,
                 aa: int, ag: int, mission: str, db: Session = Depends(get_db)):
    return crud.addFlightLog(id, callsign, acId, sqId, offDate, offTime, landDate, landTime, aa, ag, mission, db)


@app.get("/squadrons", name='Get list of Squadrons', response_model=List[Squad])
def Squadrons(db: Session = Depends(get_db)):
    return crud.getSquadrons(db)


@app.get("/aircraft", name='Get list of Aircraft', response_model=List[AC])
def Aircraft(db: Session = Depends(get_db)):
    return crud.getAircraft(db)


@app.get("/rank", name="Get list of Rank", response_model=List[Rank])
def Rank(db: Session = Depends(get_db)):
    return crud.getRank(db)


# Enter new map
@app.put("/addMap/{name}", name="Add new map")
def AddMap(name: str, db: Session = Depends(get_db)):
    crud.addMap(name, db)


@app.put("/addAircraft/{name}", name="Add new Aircraft")
def AddAircraft(name: str, db: Session = Depends(get_db)):
    crud.addAircraft(name, db)


# enter in new individual
@app.put("/addPlayer/{callsign}/{sqID}/{rank}/{flight}/{comm}/{exo}/{admin}/{mod}/{instructor}",
         name="Add new player")
def AddPlayer(callsign: str, sqID: int, rank: int, flight: bool, comm: bool, exo: bool, admin: bool, mod: bool,
              instructor: bool,
              db: Session = Depends(get_db)):
    crud.addPlayer(callsign, sqID, rank, flight, comm, exo, admin, mod, instructor, db)


# update Roster with new squadron assignments.
@app.delete("/removePlayer/{callsign}", name="Remove player")
def RemovePlayer(callsign: str, db: Session = Depends(get_db)):
    crud.removePlayer(callsign, db)


@app.put("/updatePlayer/{callsign}/{sqID}/{rank}/{flight}/{comm}/{exo}/{admin}/{mod}/{instructor}",
         name="Update player")
def UpdatePlayer(callsign: str, sqID: int, rank: int, flight: bool, comm: bool, exo: bool, admin: bool, mod: bool,
                 instructor: bool,
                 db: Session = Depends(get_db)):
    crud.updatePlayer(callsign, sqID, rank, flight, comm, exo, admin, mod, instructor, db)


@app.get("/getMission/", name="Get Missions",response_model=List[Miss])
def GetMissions(db: Session = Depends(get_db)):
    return crud.getMissions(db)
