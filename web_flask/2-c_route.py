#!/usr/bin/python3

"""a program that can print hello world on flask"""
from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def home():
    """ this will display hello HBNB! """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ this will display HBNB """
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """ this will display HBNB """
    return(f"C {text}").replace("_", " ")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)