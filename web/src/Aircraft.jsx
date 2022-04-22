import React, {useState, useEffect} from 'react';
import {
    AppBar, Button, Toolbar, FormControl, InputLabel,
    Select, Typography, TextField, Paper, Container
} from '@material-ui/core';
import {makeStyles} from '@material-ui/styles';
import {useNavigate} from 'react-router-dom';
import Header from "./components/Header";


const Aircraft = () => {
    const [aircraft, setAircraft] = useState([])

    const fetchAircraft = () => {
        fetch('http://127.0.0.1:5000/aircraft')
            .then(resp => resp.json())
            .then(response => {
                setAircraft(response)
                console.log(response)
            })
    }

    useEffect(() => {
        fetchAircraft();
    }, []);

    return (
        <>
            <Header/>
            <h1>Aircraft</h1>
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
                        aircraft.map((item) => (
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

export default Aircraft;
