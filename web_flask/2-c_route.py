#!/usr/bin/python3
"""
Starts a flask server
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Text """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ More Text """
    return ("Hello HBNB!")


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """ More Text """
    return ("C {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
