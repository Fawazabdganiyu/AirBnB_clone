#!/usr/bin/python3
"""
Module Name: models/amenity.py
Description: This module provide class `Amenity` that inherits from `BaseModel`.

"""
from models.base_model import BaseModel


class State(BaseModel):
    """A definition of class `Amenity` that name the amenity available
    in a place.

    Attributes:
        name (str): The name of a place amenity.

    """
    name = ""
