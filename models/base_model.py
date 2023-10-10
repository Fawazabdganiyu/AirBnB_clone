#!/usr/bin/python3
"""
This module defines a `BaseModel` class

"""
import uuid
from datetime import datetime


class BaseModel:
    """A definition of a class `BaseModel` with all common attributes/methods
    for other classes.

    Attributes:
        id (str): An uuid assigned identification when an instance is created.
        created_at (str): datetime - assign with the current datetime when
            an instance is created.
        updated_at (str): datetime - assign with the current datetime when
            an instance is created and it will be updated every time
            an object is changed.
    """

    def __init__(self, *args, **kwargs):
        """Constructor

        Args:
            args (iter): A tuple of attribute for an instance.
            kwargs (iter): A keyword arguments for an instance.

        """
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at':
                        v = datetime.fromisoformat(v)
                    if k == 'updated_at':
                        v = datetime.fromisoformat(v)
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Informal string representation

        Returns:
            A string representation of an instance

        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute `updated_at` with the
        current datetime.

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the __dict__
        of the instance.

        """
        dict_cpy = self.__dict__.copy()

        created_time = self.__dict__["created_at"]
        updated_time = self.__dict__["updated_at"]

        dict_cpy["created_at"] = created_time.isoformat()
        dict_cpy["updated_at"] = updated_time.isoformat()

        for_json = {"__class__": 'BaseModel', **dict_cpy}

        return for_json
