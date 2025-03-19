#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api

# Add your model imports
from models import Flight

# Views go here!

class AllFlights(Resource):
    def get(self):
        flights = Flight.query.all()
        response_body = [flight.to_dict(only=('id', 'airline', 'image')) for flight in flights]
        return make_response(response_body, 200)
    
    def post(self):
        try:
            new_flight = Flight(airline=request.json.get('airline'), image=request.json.get('image'))
            db.session.add(new_flight)
            db.session.commit()
            response_body = new_flight.to_dict(only=('id', 'airline', 'image'))
            return make_response(response_body, 201)
        except Exception as e:
            response_body = {
                "error": str(e)
            }
            return make_response(response_body, 422)

api.add_resource(AllFlights, '/flights')

class FlightByID(Resource):

    def get(self, id):
        flight = db.session.get(Flight, id)

        if flight:
            response_body = flight.to_dict(only=('id', 'airline', 'image'))
            return make_response(response_body, 200)

        else:
            response_body = {
                "error": "Flight Not Found!"
            }
            return make_response(response_body, 404)

    def patch(self, id):
        flight = db.session.get(Flight, id)

        if flight:
            try:
                for attr in request.json:
                    setattr(flight, attr, request.json[attr])
                db.session.commit()
                response_body = flight.to_dict(only=('id', 'airline', 'image'))
                return make_response(response_body, 200)
            except Exception as e:
                response_body = {
                    "error": str(e)
                }
                return make_response(response_body, 422)

        else:
            response_body = {
                "error": "Flight Not Found!"
            }
            return make_response(response_body, 404)

    def delete(self, id):
        flight = db.session.get(Flight, id)

        if flight:
            db.session.delete(flight)
            db.session.commit()
            return make_response({}, 204)

        else:
            response_body = {
                "error": "Flight Not Found!"
            }
            return make_response(response_body, 404)

api.add_resource(FlightByID, '/flights/<int:id>')

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)

