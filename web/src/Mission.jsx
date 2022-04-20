import React, {useState, useEffect} from 'react';
import {AppBar, Button, Toolbar,FormControl,InputLabel,
    Select,Typography, TextField, Paper, Container} from '@material-ui/core';
import {makeStyles} from '@material-ui/styles';
import {useNavigate} from 'react-router-dom';
import Header from "./components/Header";


const Mission =() =>{

    return (
        <>
            <Header/>
            <h1>Mission</h1>
        </>
    );
};

export default Mission;