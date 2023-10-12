#!/usr/bin/python3
"""
Module Name: models/user.py
Description: This module provides a class `User` that inherits from
             `BaseModel`.

"""


class User(BaseModel):
    """A definition of class `user`.

    Attributes:
        email (string): user email
        password (string): user password
        first_name (string): user first name
        last_name (string): user last name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
