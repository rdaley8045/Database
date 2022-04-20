import React, {useState, useEffect} from 'react';
import Header from "./components/Header";



const Home =() =>{


  return (
    <>
        <Header/>
        <h1>Welcome to Flight Comm</h1>
        <p>This is the project that Raymond Daley and Kevin Chamberlain
            has created for CSC 484 - Database Management. The project was created using
        pythons FastApi, a postgres database, and a react front end. All SQL statement are as followed:</p>
        <ol>
            <li>
                SELECT roster.callsign, roster.commander, roster.executive, grade.position
                FROM roster JOIN squadron ON squadron.id = roster.squadronid JOIN grade ON grade.id =
                roster.rankid WHERE squadron.name = %(name_1)s
            </li>
            <li>
                SELECT flightlog.callsign, aircraft.name, flightlog.missionname, flightlog.aakills, flightlog.agkills,
                flightlog.takeoffdate, flightlog.takeofftime, flightlog.landingdata, flightlog.landingtime
                FROM flightlog, aircraft JOIN squadron ON aircraft.id IS NOT NULL WHERE squadron.name = %(name_1)s AND
                aircraft.id = flightlog.aircraftid ORDER BY flightlog.takeoffdate, flightlog.takeofftime
            </li>
            <li>
                SELECT aircraft.name, flightlog.missionname, flightlog.aakills, flightlog.agkills, flightlog.takeoffdate,
                flightlog.takeofftime, flightlog.landingdata, flightlog.landingtime
                FROM flightlog JOIN aircraft ON aircraft.id = flightlog.aircraftid
                WHERE flightlog.callsign = %(callsign_1)s ORDER BY flightlog.takeoffdate, flightlog.takeofftime
            </li>
            <li>
                SELECT roster.callsign FROM roster JOIN squadron ON squadron.id = roster.squadronid
                WHERE squadron.name = %(name_1)s AND roster.flightlead = %(bool1)s AND roster.commander = %(bool2)s
                AND roster.executive = %(bool3)s AND roster.flightinstructor = %(bool4)s
            </li>
            <li>
                SELECT roster.callsign FROM roster WHERE roster.flightlead = %(bool1)s  AND roster.commander = %(bool2)s
                AND roster.executive = %(bool3)s  AND roster.flightinstructor = %(bool4)s
            </li>
            <li>
                 SELECT roster.callsign FROM roster WHERE roster.admin = %(bool1)s AND roster.moderator = %(bool2)s
            </li>
            <li>
                SELECT roster.callsign FROM roster JOIN squadron ON squadron.id = roster.squadronid
                WHERE squadron.name = %(name_1)s AND roster.admin = %(bool1)s AND roster.moderator = %(bool2)s
            </li>
            <li>
                INSERT INTO mission (name, createddate, mapid, description) VALUES (%(name)s, %(createddate)s,
                %(mapid)s, %(description)s)
            </li>
            <li>
                 SELECT map.id AS map_id, map.name AS map_name FROM map
            </li>
            <li>
                INSERT INTO flightlog (id, callsign, aircraftid, squadronid, takeoffdate, takeofftime, landingtime,
                landingdata, aakills, agkills, missionname) VALUES (%(id)s, %(callsign)s, %(aircraftid)s, %(squadronid)s,
                %(takeoffdate)s, %(takeofftime)s, %(landingtime)s, %(landingdata)s, %(aakills)s, %(agkills)s, %(missionname)s)
            </li>
            <li>
                SELECT squadron.id, squadron.name, squadron.aircraftid FROM squadron
            </li>
            <li>
                SELECT aircraft.id, aircraft.name FROM aircraft
            </li>
            <li>
                SELECT grade.id, grade.position FROM grade
            </li>
            <li>
                INSERT INTO map (id, name) VALUES (%(id)s, %(name)s)
            </li>
            <li>
                INSERT INTO aircraft (id, name) VALUES (%(id)s, %(name)s)
            </li>
            <li>
                INSERT INTO roster (callsign, squadronid, rankid, flightlead, commander, executive, admin, moderator,
                flightinstructor) VALUES (%(callsign)s, %(squadronid)s, %(rankid)s, %(flightlead)s, %(commander)s,
                %(executive)s, %(admin)s, %(moderator)s, %(flightinstructor)s)
            </li>
            <li>
                UPDATE roster SET rankid=%(rankid)s, admin=%(admin)s, flightinstructor=%(flightinstructor)s
                WHERE roster.callsign = %(roster_callsign)s
            </li>
            <li>
                 SELECT mission.name, mission.description, mission.createddate, mission.mapidFROM mission
            </li>

        </ol>
    </>
  );
};
export default Home;