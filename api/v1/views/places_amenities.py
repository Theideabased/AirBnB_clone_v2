#!/usr/bin/python3
"""view for the link between Place objects and Amenity objects that
handles all default RESTFul API actions"""
from flask import jsonify, abort, request, make_response
from models.amenity import Amenity
from models.place import Place
from api.v1.views import app_views
from models import storage
import os


@app_views.route('places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def return_amnity(place_id):
    """Retrieves the list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    li = []
    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        for amenity in place.amenities:
            li.append(amenity.to_dict())
    else:
        for amenity_id in place.amenity_ids:
            li.append(storage.get(Amenity, amenity_id).to_dict())
    return jsonify(li)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_amenity(place_id, amenity_id):
    """Deletes a Amenity object to a Place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        if amenity not in place.amenities:
            abort(404)
        place.amenities.delete(amenity)
    else:
        if amenity_id not in place.amenity_ids:
            abort(404)
        place.amenity_ids.remove(amenity_id)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'],
                 strict_slashes=False)
def create_object(place_id, amenity_id):
    """Link a Amenity object to a Plac"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        if amenity in place.amenities:
            return make_response(jsonify(amenity.to_dict()), 200)
        else:
            place.amenities.append(amenity)
    else:
        if amenity_id in place.amenity_ids:
            return make_response(jsonify(amenity.to_dict()), 200)
        else:
            place.amenity_ids.append(amenity_id)
    storage.save()
    return make_response(jsonify(amenity.to_dict()), 201)
