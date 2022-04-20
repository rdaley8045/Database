import React, {useState, useEffect} from 'react';
import {AppBar, Button, Toolbar,FormControl,InputLabel,
    Select,Typography, TextField, Paper, Container} from '@material-ui/core';
import {makeStyles} from '@material-ui/styles';
import {useNavigate} from 'react-router-dom';
import Header from "./components/Header";



const Home =() =>{

    let squadron = []

    useEffect(()=>{
        fetch('http://localhost:5000/individual/484th')
            .then(resp => resp.json())
            .then(response => {
                console.log(response)
            })
    })

  return (
    <>
        <Header/>



            <p>This is a test</p>
    </>
  );
};
export default Home;