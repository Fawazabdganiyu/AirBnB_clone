#!/usr/bin/python3
"""
Module Name: place
Description: defines a class `Place` that inherits from BaseModel class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place:
        Contains the infromation of a place
        Attributes:
            `name`(string): The name of the place
            `description`(string): Description of the place
            `city_id`(string): City of residence (city identification )
            `user_id`(string): The id of the user who request such place
            `number_rooms`(int): Number of rooms contained
            `number_bathrooms`(int): Number of bathrooms contained
            `max_guest`(int): Maximum number of guest
            `amenity_ids`(list): List of strings containing ids of amenities
            `price_by_night`(int): Price per night
            `latitude`(float): Latitude
            `longitude`(float): Longitude
    """
    # Place informations with their default values
    name = ""
    description = ""
    city_id = ""
    user_id = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = 0
    amenty_ids = []
    price_by_night = 0
    latitiude = 0.0
    longitude = 0.0
