import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import {ThemeProvider, createTheme, StyledEngineProvider} from '@material-ui/core/styles';

const THEME = createTheme({
    palette: {
        type: 'light',
        contrastThreshold: 3,
        tonalOffset: 0.2,
        primary: {
            main: '#d79146'
        },
        secondary:{
            main: '#607d8b'
        },
        text:{
          primary: "rgba(0,0,0,0.87)",
          secondary: "rgba(0,0,0,0.54)",
          disabled: "rgba(0,0,0,0.38)",
          hint: "rgba(0,0,0,0.38)"
        }
    },
    typography:{
        useNextVariants: true,
        h1:{
            fontWeight: 500,
            fontSize: '2.125 rem'
        },
        h2:{
            fontWeight: 500,
            fontSize: '1.375 rem'
        },
        h3:{
            fontWeight: 500,
            fontSize: '1.243 rem'
        },
        subtitle1:{
            fontStyle: 'italic',
            fontSize: '0.875 rem',
            lineHeight: 1
        },
        h6:{
            textDecoration: 'underline'
        }
    }
});

ReactDOM.render(
    <React.StrictMode>
        <StyledEngineProvider injectFirst>
            <ThemeProvider theme = {THEME}>
                <App/>
            </ThemeProvider>
        </StyledEngineProvider>
    </React.StrictMode>,
    document.getElementById('root')
);