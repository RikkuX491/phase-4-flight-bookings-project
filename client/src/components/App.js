import React, { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";

import Header from "./Header";

function App() {

  const [flights, setFlights] = useState([])

  useEffect(getFlights, [])

  function getFlights(){
    fetch("/flights")
    .then(response => response.json())
    .then(flightsData => setFlights(flightsData))
  }

  return (
    <div className="app">
      <Header/>
      <Outlet context={
        {
          flights: flights
        }
      }/>
    </div>
  );
}

export default App;
