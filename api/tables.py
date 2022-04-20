from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time
from sqlalchemy.orm import relationship

from database import Base


class Map(Base):
    __tablename__ = "map"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Aircraft(Base):
    __tablename__ = "aircraft"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Squadron(Base):
    __tablename__ = "squadron"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    aircraftid = Column(Integer, ForeignKey('aircraft.id'))


class Grade(Base):
    __tablename__ = "grade"

    id = Column(Integer, primary_key=True, index=True)
    position = Column(String, index=True)


class Roster(Base):
    __tablename__ = "roster"

    callsign = Column(String, primary_key=True, index=True)
    squadronid = Column(Integer, ForeignKey('squadron.id'))
    rankid = Column(Integer, ForeignKey('grade.id'))
    flightlead = Column(Boolean, default=False)
    commander = Column(Boolean, default=False)
    executive = Column(Boolean, default=False)
    admin = Column(Boolean, default=False)
    moderator = Column(Boolean, default=False)
    flightinstructor = Column(Boolean, default=False)


class Mission(Base):
    __tablename__ = "mission"

    name = Column(String, primary_key=True, index=True)
    createddate = Column(Date)
    mapid = Column(Integer, ForeignKey('map.id'))
    description = Column(String)


class FlightLog(Base):
    __tablename__ = "flightlog"

    id = Column(Integer, primary_key=True, index=True)
    callsign = Column(String, ForeignKey('roster.callsign'))
    aircraftid = Column(Integer, ForeignKey(Aircraft.id))
    squadronid = Column(Integer, ForeignKey('squadron.id'))
    takeoffdate = Column(Date)
    takeofftime = Column(Time)
    landingtime = Column(Time)
    landingdata = Column(Date)
    aakills = Column(Integer)
    agkills = Column(Integer)
    missionname = Column(String, ForeignKey('mission.name'))
