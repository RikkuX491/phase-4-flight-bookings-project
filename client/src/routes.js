import App from "./components/App";
import ErrorPage from "./components/ErrorPage";
import FlightList from "./components/FlightList";

const routes = [
    {
        path: "/",
        element: <App/>,
        errorElement: <ErrorPage/>,
        children: [
            {
                path: "/",
                element: <FlightList/>
            }
        ]
    }
]

export default routes;