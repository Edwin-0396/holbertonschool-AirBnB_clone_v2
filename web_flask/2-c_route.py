#!/usr/bin/python3
"""This module starts a Flask web application and displays text starting with C
"""
from flask import Flask
from flask import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns the string Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Returns the string HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """Returns a string starting with C"""
    mod_text = escape(text)
    return 'C %s' % mod_text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
