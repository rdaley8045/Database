import React, {useState, useEffect} from 'react';
import {
    AppBar, Button, Toolbar, FormControl, InputLabel,
    Select, Typography, TextField, Paper, Container
} from '@material-ui/core';
import {makeStyles} from '@material-ui/styles';
import {useNavigate} from 'react-router-dom';
import Header from "./components/Header";


const Squadron = () => {

    return (

        <>
            <Header/>
            <h1>Squadron</h1>
        </>
    );
};

export default Squadron;