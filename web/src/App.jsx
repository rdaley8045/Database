import {HashRouter, Route, Routes} from 'react-router-dom';
import Home from "./Home";


const App = () => {


    return (
        <HashRouter>
            <Routes>
                <Route path="/" element ={<Home/>}/>
            </Routes>
        </HashRouter>
    );
};

export default App;