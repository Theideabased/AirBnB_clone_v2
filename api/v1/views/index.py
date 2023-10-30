#!/usr/bin/python3
"""Flask Api"""
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

classes = {"amenity": Amenity, "city": City,
           "place": Place, "review": Review, "state": State, "user": User}


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def index():
    """returns a JSON: 'statu': 'OK'"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """retrieves the number of each objects by type"""
    static = {}
    for k, v in classes.items():
        static[k] = storage.count(v)
    return jsonify(static)
