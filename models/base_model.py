#!/usr/bin/python3
"""
Module Name: models/base_model.py
Description: This module defines a `BaseModel` class

"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """ The parent class of all classes used in the program """
    def __init__(self, *args, **kwargs):
        """ The constructor

        Args:
            *args (tuple): Variable number of ordered arguments
            **kwargs (dictionary): keyworded arguments

        It assigns this parameters to attributes

        Returns:
            None
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        v = datetime.fromisoformat(v)
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns an informal representation of instances """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates objects and the public instance attribute `updated_at`
        with the current datetime of updation.
        """
        self.updated_at = datetime.now()
        models.storage.save()  # Save the updated objects

    def to_dict(self):
        """ Returns the dictionary representation of an instance """
        dict_copy = self.__dict__.copy()  # Get a copy of instance dict

        # Update created_at and updated_at attributes with isoformat time
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()

        # Add a new value, the class name
        dict_copy['__class__'] = f"{self.__class__.__name__}"

        return dict_copy
