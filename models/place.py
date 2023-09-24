#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
import os
import models

# Get storage environment varible
storage_type = os.getenv('HBNB_TYPE_STORAGE')

place_amenity_table = Table("place_amenity", Base.metadata,
                            Column("place_id", String(60),
                                   Foreign_Key("places.id"), primary_key=True,
                                   nullable=False),
                            Column("amenity_id", String(60),
                                ForeignKey("amenities.id"),
                                primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if storage_type == 'db':
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete")
        amenities=relationship(
                "Amenity", secondary=place_amenity_table,
                back_populates="place_amenities",
                viewonly=False)
    else:
        @property
        def reviews(self):
            """Getter function for Review objects"""
            reviews = []
            for review in list(models.storage.all(Review).calues()):
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """Getter function for amenities"""
            amenities = []
            for amenity in list(models.storage,all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, value):
            """ setter function for amenities """
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
