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

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)

