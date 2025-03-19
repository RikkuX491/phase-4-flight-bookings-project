import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";

function App() {

  const [flights, setFlights] = useState([])
  console.log(flights)

  useEffect(getFlights, [])

  function getFlights(){
    fetch("/flights")
    .then(response => response.json())
    .then(flightsData => setFlights(flightsData))
  }

  return <h1>Project Client</h1>;
}

export default App;
