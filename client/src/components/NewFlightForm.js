import { useOutletContext, useNavigate } from "react-router-dom";
import { useState } from "react";

function NewFlightForm(){

    const { addFlight } = useOutletContext()

    const navigate = useNavigate()

    const [formData, setFormData] = useState({
        airline: "",
        image: ""
    })

    function handleSubmit(event){
        event.preventDefault()

        fetch('/flights', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if(response.ok){
                response.json().then(newFlightData => {
                    addFlight(newFlightData)
                    navigate('/')
                })
            }
            else{
                response.json().then(errorObject => {
                    alert(`Error: ${errorObject.error}`)
                })
            }
        })
    }

    function updateFormData(event){
        setFormData({...formData, [event.target.name]: event.target.value})
    }

    return (
        <div>
            <h2>Add New Flight</h2>
            <form onSubmit={handleSubmit}>
                <label htmlFor="new-airline">Airline: </label>
                <input onChange={updateFormData} type="text" id="new-airline" name="airline" value={formData.airline}/>
                <br/><br/>
                <label htmlFor="new-image">Image: </label>
                <input onChange={updateFormData} type="text" id="new-image" name="image" value={formData.image}/>
                <br/><br/>
                <input type="submit" value="Add Flight"/>
            </form>
        </div>
    )
}

export default NewFlightForm;