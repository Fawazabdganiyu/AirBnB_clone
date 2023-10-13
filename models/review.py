#!/usr/bin/python3
"""
Module Name: models/review.py
Description: This module provides a class `Review`
             that is inherited from `BaseModel`
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A definition of class `Review` that shows a review about a place
    and the owner.

    Attributes:
        place_id (string): An `id` of a `Place` instance.
        user_id (str): An `id` of a `User` instance.
        text (str): The content of the review.

    """
    place_id = ""
    user_id = ""
    text = ""
