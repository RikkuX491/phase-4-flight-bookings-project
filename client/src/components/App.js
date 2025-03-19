import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";

import Header from "./Header";

function App() {

  const [flights, setFlights] = useState([])
  console.log(flights)

  useEffect(getFlights, [])

  function getFlights(){
    fetch("/flights")
    .then(response => response.json())
    .then(flightsData => setFlights(flightsData))
  }

  return (
    <div>
      <Header/>
    </div>
  );
}

export default App;
