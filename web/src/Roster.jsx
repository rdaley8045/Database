import React, {useState, useEffect} from 'react';
import {
    AppBar, Button, Toolbar, FormControl, InputLabel,
    Select, Typography, TextField, Paper, Container
} from '@material-ui/core';
import {makeStyles} from '@material-ui/styles';
import {useNavigate} from 'react-router-dom';
import Header from "./components/Header";


const Roster = () => {

    const [roster, setRoster] = useState([])
    const [rank, setRank] = useState([])
    const [sqLog, setSqLog] = useState([])
    const [indLog, setIndLog] = useState([])

    const fetchRoster = () => {
        fetch('http://localhost:5000/individual/484th')
            .then(resp => resp.json())
            .then(response => {
                setRoster(response)
                console.log(response)
            })
    }

    const fetchRank = () => {
        fetch('http://127.0.0.1:5000/rank')
            .then(resp => resp.json())
            .then(response => {
                setRank(response)
                console.log(response)
            })
    }

    const fetchSqLog = () => {
        fetch('http://127.0.0.1:5000/squadronLogs/484th')
            .then(resp => resp.json())
            .then(response => {
                setSqLog(response)
                console.log(response)
            })
    }

    const fetchIndLog = () => {
        fetch('http://127.0.0.1:5000/squadronLogs/484th')
            .then(resp => resp.json())
            .then(response => {
                setSqLog(response)
                console.log(response)
        })
    }

    useEffect(() => {
        fetchRoster();
    }, []);

    useEffect(() => {
        fetchRank();
    }, []);

    useEffect(() => {
        fetchSqLog();
    }, []);

    return (
        <>
            <Header/>
            <h1>Roster</h1>
            <h3>Squadron Members</h3>
            <div>
                <table>
                    <thead>
                    <tr>
                        <th>Callsign</th>
                        <th>Commander</th>
                        <th>Executive</th>
                        <th>Position</th>
                    </tr>
                    </thead>
                    <tbody>
                    {
                        roster.map((item) => (
                            <tr key={item.callsign}>
                                <td>{item.callsign}</td>
                                <td>{item.commander}</td>
                                <td>{item.executive}</td>
                                <td>{item.position}</td>
                                <td/>
                            </tr>
                        ))
                    }
                    </tbody>
                </table>
            </div>


            <h3>Rank Structure</h3>
            <div>
                <table>
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Grade</th>
                    </tr>
                    </thead>
                    <tbody>
                    {
                        rank.map((item) => (
                            <tr key={item.id}>
                                <td>{item.id}</td>
                                <td>{item.position}</td>

                            </tr>
                        ))
                    }
                    </tbody>
                </table>
            </div>

            <h3>Squad Flight Logs</h3>
            <div>
                <table>
                    <thead>
                    <tr>
                        <th>Callsign</th>
                        <th>Name</th>
                        <th>Mission Name</th>
                        <th>Air-Air Kills</th>
                        <th>Air-Ground Kills</th>
                        <th>Take Off Date</th>
                        <th>Take Off Time</th>
                        <th>Landing Date</th>
                        <th>Landing Time</th>
                    </tr>
                    </thead>
                    <tbody>
                    {
                        sqLog.map((item) => (
                            <tr key={item.callsign}>
                                <td>{item.name}</td>
                                <td>{item.missionname}</td>
                                <td>{item.aakills}</td>
                                <td>{item.agkills}</td>
                                <td>{item.takeoffdate}</td>
                                <td>{item.takeofftime}</td>
                                <td>{item.landingdata}</td>
                                <td>{item.landingtime}</td>

                            </tr>
                        ))
                    }
                    </tbody>
                </table>
            </div>

            <h3>Individual Flight Logs</h3>
        </>
    );
};


export default Roster;
