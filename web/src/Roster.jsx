import React, {useState, useEffect} from 'react';
import {
    AppBar, Button, Toolbar, FormControl, InputLabel,
    Select, Typography, TextField, Paper, Container
} from '@material-ui/core';
import {makeStyles} from '@material-ui/styles';
import {useNavigate} from 'react-router-dom';
import Header from "./components/Header";


const Roster = () => {

    return (
        <>
            <Header/>
            <h1>Roster</h1>

            <h3>Squadron Members</h3>

            <h3>Rank Structure</h3>

            <h3>Squad Flight Logs</h3>

            <h3>Individual Flight Logs</h3>
        </>
    );
};

export default Roster;