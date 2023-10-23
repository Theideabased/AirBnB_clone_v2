#!/usr/bin/python3
"""Flask Application Module"""

from flask import Flask
from models import storage
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Displays list of all states present in DBStorage in an HTML page"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """Displays state of id passed and all it's cities in an HTML page"""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", states=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
