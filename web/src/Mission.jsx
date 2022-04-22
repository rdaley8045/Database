import React, {useState, useEffect} from 'react';
import {AppBar, Button, Toolbar,FormControl,InputLabel,
    Select,Typography, TextField, Paper, Container} from '@material-ui/core';
import {makeStyles} from '@material-ui/styles';
import {useNavigate} from 'react-router-dom';
import Header from "./components/Header";



const Mission =() =>{

    const [missions, setMission] = useState([])
    const [maps, setMap] = useState([])

    const fetchMission = () => {
        fetch('http://127.0.0.1:5000/getMission/')
            .then(resp => resp.json())
            .then(response => {
                setMission(response)
                console.log(response)
            })
    }

    const fetchMap = () => {
        fetch('http://127.0.0.1:5000/maps')
            .then(resp => resp.json())
            .then(response => {
                setMap(response)
                console.log(response)
            })
    }

    useEffect(() => {
        fetchMission();
    }, []);

    useEffect(() => {
        fetchMap();
    }, []);

    return (
        <>
            <Header/>
            <h1>Mission</h1>
            <h3>Missions</h3>
            <div>
                <table>
                    <thead>
                    <tr>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Created Date</th>
                        <th>Map ID</th>
                    </tr>
                    </thead>
                    <tbody>
                    {
                        missions.map((item) => (
                            <tr key={item.name}>
                                <td>{item.name}</td>
                                <td>{item.description}</td>
                                <td>{item.createddate}</td>
                                <td>{item.mapiid}</td>
                                <td/>
                            </tr>
                        ))
                    }
                    </tbody>
                </table>
            </div>
            <h3>Maps </h3>
            <div>
                <table>
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                    </tr>
                    </thead>
                    <tbody>
                    {
                        maps.map((item) => (
                            <tr key={item.id}>
                                <td>{item.id}</td>
                                <td>{item.name}</td>
                                <td/>
                            </tr>
                        ))
                    }
                    </tbody>
                </table>
            </div>
        </>
    );
};

export default Mission;
