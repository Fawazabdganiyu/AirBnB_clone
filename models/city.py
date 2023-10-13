#!/usr/bin/python3
"""
Module Name: models/city.py
Description: This module provides class `City` that inherits from `BaseModel`.

"""
from models.base_model import BaseModel


class City(BaseModel):
    """A definition of class `City` that give information about a city.

    Attributes:
        state_id (str): The id of the state where the city is located.
                        This will be the id of the `State` class => `State.id`
        name (str): The name of the city.

    """
    state_id = ""
    name = ""
