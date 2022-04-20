import {HashRouter, Route, Routes} from 'react-router-dom';
import Home from "./Home";
import Mission from "./Mission";
import Roster from "./Roster";
import Aircraft from "./Aircraft";
import Squadron from "./Squadron";


const App = () => {


    return (
        <HashRouter>
            <Routes>
                <Route path="/" element ={<Home/>}/>
                <Route path="/roster" element= {<Roster/>}/>
                <Route path="/mission" element={<Mission/>}/>
                <Route path="/aircraft" element={<Aircraft/>}/>
                <Route path="/squadron" element={<Squadron/>}/>
            </Routes>
        </HashRouter>
    );
};

export default App;