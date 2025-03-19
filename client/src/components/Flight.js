function Flight({flight}){
    return (
        <li className="flight">
            <h2>Flight # {flight.id}</h2>
            <h3>Airline: {flight.airline}</h3>
            <img src={flight.image} alt={flight.airline}/>
        </li>
    )
}

export default Flight;