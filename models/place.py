#!/usr/bin/python3
"""
Place module
Defines the Place class which inherits from BaseModel.
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """Defines attributes for Place"""
    city_id = ""        # it will be the City.id
    user_id = ""        # it will be the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []    # it will be a list of Amenity.id
