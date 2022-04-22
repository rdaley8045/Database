import React, {useState, useEffect} from 'react';
import Header from "./components/Header";

function trueFalse(value){
    if (value){
        return "True"
    }else{
        return "False"
    }
}

const Squadron = () => {

    const [squadron, setSquadron] = useState([])

    const fetchSquadron = () => {
        fetch('http://localhost:5000/squadrons')
            .then(resp => resp.json())
            .then(response => {
                setSquadron(response)
            })
    }


    useEffect(() => {
        fetchSquadron();
    }, []);


    return (

        <>
            <Header/>
            <h1>Squadron</h1>
            <div>
                <table>
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Aircraft ID</th>
                    </tr>
                    </thead>
                    <tbody>
                    {
                        squadron.map((item) => (
                            <tr key={item.id}>
                                <td>{item.id}</td>
                                <td>{item.name}</td>
                                <td>{item.aircraftid}</td>
                            </tr>
                        ))
                    }
                    </tbody>
                </table>
            </div>

            <h3> Select Duties</h3>
            <form>

            </form>
            <h3>Individual Permissions</h3>
        </>
    );
};

export default Squadron;