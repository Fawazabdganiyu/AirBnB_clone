#!/usr/bin/python3
"""
Module Name: models/state.py
Description: This module provide class `State` that inherits from `BaseModel`.

"""
from models.base_model import BaseModel


class State(BaseModel):
    """A definition of class `State`

    Attributes:
        name (str): Name of a state

    """
    name = ""
