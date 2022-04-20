import React, {useState, useEffect} from 'react';
import Header from "./components/Header";


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
                                <td/>
                            </tr>
                        ))
                    }
                    </tbody>
                </table>
            </div>

            <h3> Select Duties</h3>
            <h3>Squad Duties</h3>
            <h3> Individual Permissions</h3>
            <h3>Squadron Permissions</h3>
        </>
    );
};

export default Squadron;