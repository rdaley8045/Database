CREATE TABLE aircraft
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE,
    image VARCHAR(1024)
);

CREATE TABLE squadron
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(150),
    aircraftId INT REFERENCES aircraft(id)
);

CREATE TABLE grade
(
    id SERIAL PRIMARY KEY,
    position VARCHAR(100) UNIQUE,
    image VARCHAR(1024),
    flightLead BOOLEAN,
    commander BOOLEAN,
    executive BOOLEAN,
    admin BOOLEAN,
    moderator BOOLEAN,
    flightInstructor BOOLEAN
);


CREATE TABLE rooster
(
    callsign VARCHAR(40) PRIMARY KEY,
    squadronId INT REFERENCES squadron(id),
    rankId INT REFERENCES grade(id)
);

CREATE TABLE login
(
    callsign VARCHAR(40)  PRIMARY KEY REFERENCES rooster(callsign),
    email    VARCHAR(200) UNIQUE,
    password VARCHAR(128)
);

CREATE TABLE map
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) UNIQUE
);


CREATE TABLE mission
(
    data DATE,
    name VARCHAR(200) PRIMARY KEY UNIQUE,
    createdTime DATE,
    mapId INT REFERENCES map(id),
    description TEXT
);

CREATE TABLE flightlog
(
    callsign VARCHAR(40) PRIMARY KEY REFERENCES rooster(callsign),
    aircraftId INT REFERENCES aircraft(id),
    takeoffTime DATE,
    landingTime DATE,
    aakills INT,
    agkills INT,
    mapId INT REFERENCES map(id)
);

