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

api.add_resource(AllFlights, '/flights')

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)

