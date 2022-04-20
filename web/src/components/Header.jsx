import React from 'react';
import {AppBar, Toolbar, Button, Typography} from '@material-ui/core';
import {useNavigate} from 'react-router';

const Header = () => {
    const navigate = useNavigate();

    return (
        <>
            <AppBar position='static' style={{marginBottom: '8px'}}>
                <Toolbar>
                    <Button
                        style={{fontSize: '20px', color: '#ffffff'}}
                        size='large'
                        onClick={() => {
                            navigate('/')
                        }}>
                        Joint Task Force Heavy
                    </Button>
                    <Button
                        style={{fontSize: '16px', color: '#ffffff'}}
                        variant='outlined'
                        size='small'
                        color='primary'
                        onClick={() => {
                            navigate('/roster')
                        }}>
                        Roster
                    </Button>
                    <Button
                        style={{fontSize: '16px', color: '#ffffff'}}
                        variant='outlined'
                        size='small'
                        color='primary'
                        onClick={() => {
                            navigate('/roster')
                        }}>
                        Roster
                    </Button>
                    <Button
                        style={{fontSize: '16px', color: '#ffffff'}}
                        variant='outlined'
                        size='small'
                        color='primary'
                        onClick={() => {
                            navigate('/roster')
                        }}>
                        Roster
                    </Button>
                </Toolbar>
            </AppBar>
        </>
    );
};
export default Header;