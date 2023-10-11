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
        self.id = str(uuid.uuid4())  # Id is created for each instance
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for k, v in kwargs.items():
                if k in self.to_dict().keys() and k != '__class__':
                    if k == 'created_at':
                        self.created_at = datetime.fromisoformat(v)
                    elif k == 'updated_at':
                        self.updated_at = datetime.fromisoformat(v)
                    else:
                        setattr(self, k, v)

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
        dict_copy = self.__dict__.copy()  # Getting a copy of instance dict

        # Update created_at and updated_at attributes with isoformat time
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()

        # Add a new value, the class name
        dict_copy['__class__'] = f"{self.__class__.__name__}"

        return dict_copy
