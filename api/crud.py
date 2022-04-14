from sqlalchemy.orm import Session
from tables import Roster, Squadron, Grade, FlightLog, Mission, Map, Aircraft


def getIndividualsInSquadron(db: Session, squadronName: str):
    return db.query(Roster.callsign, Roster.commander, Roster.executive, Grade.position).join(Squadron, Grade). \
        filter(Squadron.name == squadronName).all()


def getSqudronLogs(db: Session, squadronName: str):
    return db.query(FlightLog.callsign, Aircraft.name, FlightLog.missionname, FlightLog.aakills,
                    FlightLog.agkills, FlightLog.takeoffdate, FlightLog.takeofftime,
                    FlightLog.landingdata, FlightLog.landingtime).join(Squadron, Aircraft.id != None). \
        filter(Squadron.name == squadronName, Aircraft.id == FlightLog.aircraftid).order_by(
        (FlightLog.takeoffdate), (FlightLog.takeofftime)).all()


def getIndividualLogs(db: Session, callsign: str):
    return db.query(Aircraft.name, FlightLog.missionname, FlightLog.aakills, FlightLog.agkills, FlightLog.takeoffdate,
                    FlightLog.takeofftime, FlightLog.landingdata, FlightLog.landingtime).join(Aircraft). \
        filter(FlightLog.callsign == callsign).order_by((FlightLog.takeoffdate), (FlightLog.takeofftime)).all()


def getIndividualDutiesPerSquadron(db, squadron, flightlead, commander, exo, instructor):
    return db.query(Roster.callsign).join(Squadron).filter(Squadron.name == squadron, Roster.flightlead == flightlead,
                                                           Roster.commander == commander, Roster.executive == exo,
                                                           Roster.flightinstructor == instructor).all()


def getIndividualsSelectDuty(db, flightlead, commander, exo, instructor):
    return db.query(Roster.callsign).filter(Roster.flightlead == flightlead, Roster.commander == commander,
                                            Roster.executive == exo, Roster.flightinstructor == instructor).all()


def getIndividualSelectPermissions(db, admin, moderator):
    return db.query(Roster.callsign).filter(Roster.admin == admin, Roster.moderator == moderator).all()


def getIndividualsSelectPermissionsPerSquadron(squadron, admin, moderator, db):
    return db.query(Roster.callsign).join(Squadron).filter(Squadron.name == squadron, Roster.admin == admin,
                                                           Roster.moderator == moderator).all()


def createMission(name, createDate, mapId, description, db):
    stmt = Mission(name=name, createdate=createDate, mapid=mapId, description=description)
    db.add(stmt)
    return db.commit()


def getMaps(db):
    return db.query(Map.id, Map.name)


def addFlightLog(id, callsign, acId, sqId, offDate, offTime, landDate, landTime, aa, ag, mission, db):
    stmt = FlightLog(id=id, callsign=callsign, aircraftid=acId, squadronid=sqId, takeoffdate=offDate,
                     takeofftime=offTime, landingtime=landTime, landingdata=landDate, aakills=aa,
                     agkills=ag, missionname=mission)
    db.add(stmt)
    return db.commit()


def getSquadrons(db):
    return db.query(Squadron.id, Squadron.name, Squadron.aircraftid).all()


def getAircraft(db):
    return db.query(Aircraft.id, Aircraft.name).all()


def addMap(id, name, db):
    stmt = Map(id=id, name=name)
    db.add(stmt)
    return db.commit()


def addPlayer(callsign, sqID, rank, flight, comm, exo, admin, mod, instructor, db):
    stmt = Roster(callsign=callsign, squadronid=sqID, rankid=rank, flightlead=flight, commander=comm,
                  executive=exo, admin=admin, moderator=mod, flightinstructor=instructor)
    db.add(stmt)
    return db.commit()


def getRank(db):
    return db.query(Grade.id, Grade.position, Grade.description).all()


def addAircraft(id, name, db):
    stmt = Aircraft(id=id, name=name)
    db.add(stmt)
    return db.commit()


def removePlayer(callsign, db):
    db.query(Roster).filter(Roster.callsign == callsign).delete()
    return db.commit()


def updatePlayer(callsign, sqID, rank, flight, comm, exo, admin, mod, instructor, db):
    player = db.query(Roster).filter(Roster.callsign == callsign).one()
    player.squadronid = sqID
    player.rankid = rank
    player.flightlead = flight
    player.commander = comm
    player.executive = exo
    player.admin = admin
    player.moderator = mod
    player.flightinstructor = instructor

    return db.commit()


def getMissions(db):
    return db.query(Mission.name, Mission.description, Mission.createddate, Mission.mapId).all()
