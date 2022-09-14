#!/usr/bin/python3
"""This module starts a Flask web application and displays filters with states
cities, and amenities
"""
from flask import Flask
from flask import escape
from flask import render_template
from models import storage
from models import State
from models import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def display_filters():
    """displays states, cities, and amenities under filters"""
    state_dict = storage.all(State)
    amenity_dict = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', state_dict=state_dict,
                           amenity_dict=amenity_dict)


@app.teardown_appcontext
def teardown_db(self):
    """removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)