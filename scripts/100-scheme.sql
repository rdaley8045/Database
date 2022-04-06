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
    description TEXT,
    image VARCHAR(1024)
);


CREATE TABLE rooster
(
    callsign VARCHAR(40) PRIMARY KEY,
    squadronId INT REFERENCES squadron(id),
    rankId INT REFERENCES grade(id),
    flightLead BOOLEAN,
    commander BOOLEAN,
    executive BOOLEAN,
    admin BOOLEAN,
    moderator BOOLEAN,
    flightInstructor BOOLEAN
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
    takeoffDate DATE,
    takeoffTime TIME,
    landingTime TIME,
    landingData DATE,
    aakills INT,
    agkills INT,
    mapId INT REFERENCES map(id)
);

INSERT INTO aircraft (id,name) VALUES (1,'A-10CII');
INSERT INTO aircraft (id,name) VALUES (2,'F/A-18');

INSERT INTO squadron (id, name, aircraftId) VALUES (1, '484th', 1);

INSERT INTO grade (id, position) VALUES (1, 'R');
INSERT INTO grade (id, position) VALUES (2, 'A-1');
INSERT INTO grade (id, position) VALUES (3, 'A-2');
INSERT INTO grade (id, position) VALUES (4, 'A-3');
INSERT INTO grade (id, position) VALUES (5, 'A-4');
INSERT INTO grade (id, position) VALUES (6, 'A-5');
INSERT INTO grade (id, position) VALUES (7, 'O-1');
INSERT INTO grade (id, position) VALUES (8, 'O-2');
INSERT INTO grade (id, position) VALUES (9, 'O-3');
INSERT INTO grade (id, position) VALUES (10, 'O-4');
INSERT INTO grade (id, position) VALUES (11, 'O-5');
INSERT INTO grade (id, position) VALUES (12, 'O-6');
INSERT INTO grade (id, position) VALUES (13, 'O-7');
INSERT INTO grade (id, position) VALUES (14, 'O-8');
INSERT INTO grade (id, position) VALUES (15, 'O-9');

INSERT INTO rooster VALUES ('Teapot', 1, 9,TRUE,TRUE,FALSE,FALSE,TRUE,FALSE);
INSERT INTO rooster VALUES ('Wezal', 1, 10,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE);

INSERT INTO login VALUES ('Teapot', 'teapot@gmail.com', 'password');
INSERT INTO login VALUES ('Wezal', 'wezal@gmail.com', 'password');

