#!/usr/bin/python3
"""This module defines a class Place"""


from models.base_model import BaseModel


class Place(BaseModel):
    """This class defines a Place object

    Attributes:
        city_id (str): The city id
        user_id (str): The user id
        name (str): The name of the place
        description (str): The description of the place
        number_rooms (int): The number of rooms in the place
        number_bathrooms (int): The number of bathrooms in the place
        max_guest (int): The maximum number of guests the place can hold
        price_by_night (int): The price by night for the place
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_ids (list): A list of Amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
