#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity_table

class Amenity(BaseModel, Base):
    """ Amenity class definition with many to many 
    relationship with the class Place"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity_table)
