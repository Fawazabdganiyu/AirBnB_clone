#!/usr/bin/python3
"""
Module name: b_model
Usage: This module is used to define a 'BaseModel' class as the parent
class of all other classes defined in the program
"""
import uuid
from datetime import datetime


class BaseModel:
    """ The parent class of all classes used in the program """
    def __init__(self, *args, **kwargs):
        """ The constructor
        Args:
            args: tuple containing ordered arguments
            kwargs: dictionary containing keyworded arguments

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

    def __str__(self):
        """ Returns an informal representation of instances """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Saves the time when this method is being called.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns the dictionary representation of an instance """
        dict_copy = self.__dict__.copy()  # Get a copy of instance dict

        # Update created_at and updated_at attributes with isoformat time
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()

        # Add a new value, the class name
        dict_copy['__class__'] = f"{self.__class__.__name__}"

        return dict_copy
