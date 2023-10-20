#!/usr/bin/python3

"""a program that can print hello world on flask"""
from flask import Flask
from flask import render_template

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
def c_text(text):
    """ this will display HBNB """
    return(f"C {text}").replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ this will display what is given in the argument but 'is cool'\n
    by default """
    return(f"Python {text}").replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ this will display the number n is an integer \n
    if it is an integer"""
    if isinstance(n, int):
        return(f'{n} is a number')


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ a template with the number """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
