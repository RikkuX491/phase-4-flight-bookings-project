import React, { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";

import Header from "./Header";
import NavBar from "./NavBar";

function App() {

  const [flights, setFlights] = useState([])

  useEffect(getFlights, [])

  function getFlights(){
    fetch("/flights")
    .then(response => response.json())
    .then(flightsData => setFlights(flightsData))
  }

  function addFlight(newFlight){
    setFlights([...flights, newFlight])
  }

  return (
    <div className="app">
      <NavBar/>
      <Header/>
      <Outlet context={
        {
          flights: flights,
          addFlight: addFlight
        }
      }/>
    </div>
  );
}

export default App;
