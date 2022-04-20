import React, {useState, useEffect} from 'react';
import {AppBar, Button, Toolbar,FormControl,InputLabel,
    Select,Typography, TextField, Paper, Container} from '@material-ui/core';
import {makeStyles} from '@material-ui/styles';
import {useNavigate} from 'react-router-dom';
import Header from "./components/Header";



const Home =() =>{

    let squadron = ''

    useEffect(()=>{
        fetch('http://localhost:5000/squadrons/')
            .then(resp => resp.json())
            .then(response => {
                squadron = response.name;
            })
    })

  return (
    <>
        <Header/>
        <Toolbar>
            <FormControl variant = 'filled'>
                <InputLabel id='ver-lable'>Squadrons</InputLabel>
                <Select
                    labelId ="ver-lable"
                    id = "squadron"
                    value = {sqaudron}
                    onChange={squadronSelect}
                    ></Select>


            </FormControl>
        </Toolbar>
    </>
  );
};
export default Home;