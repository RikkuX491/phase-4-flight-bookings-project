from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

# Adding the validates import to use validations
from sqlalchemy.orm import validates

from config import db

# Models go here!
class Flight(db.Model, SerializerMixin):
    __tablename__ = 'flights'

    id = db.Column(db.Integer, primary_key=True)
    airline = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)

    @validates('airline', 'image')
    def validate_airline(self, column_name, value):
        if type(value) != str:
            raise TypeError(f"{column_name} must be a string!")
        elif len(value) < 5:
            raise ValueError(f"{column_name} must be at least 5 characters long!")
        else:
            return value
        
    def __repr__(self):
        return f"<Flight {self.id} - Airline: {self.airline}, Image: {self.image}>"