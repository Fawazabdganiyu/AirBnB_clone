#!/usr/bin/python3
"""
Module Name: models/engine/file_storage.py
Description: This module provides a `FileStorage` class
             that serializes instances to a JSON file and
             deserializes JSON file to instances.

             This module defines a class 'FileStorage' which is a child-class
             of the 'BaseModel class'.
             It is used in handling the process of saving objects to
             a file DataBase(JSON) file
             and retrieving of objects from that file for processing.
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.review import Review
from models.state import State
from os import path


class FileStorage:
    """A definition of `FileStorage` class for serialization/deserialization.

    This class is used for processing 'BaseModule' objects/instances by:
        * Serializing BaseModel instances into JSON string representation
        * Storing this representation into a file Data Base (JSON file)
        * Retrieving such object via deserializing for processing when needed

    Attributes:
        file_path (string): A private class attribute that specify the path
                            to the JSON file (ex: file.json).
        objects (dict): A private class attribute that stores  all objects by
                        <class name>.id (ex: to store a BaseModel object
                        id=12121212, the key will be BaseModel.12121212).

        It also contains processor methods. Such as:
        all(self): returns the dictionary '__objects'
        new(self, obj): sets a new object into the '__objects' dictionary
                        with key as '<obj class_name>.id'
        save(self): serializes all the objects stored in '__objects' into
                    a JSON string and saves them in the file specified
                    by __file_path
        reload(self): deserializes all objects stored in JSON file into
                      objects and saves them in '__objects' dictionary
                      for processing

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary: '__objects' class attribute
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id   # <obj class name>.id

        # Set in the new object with key: 'key'
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes `__objects` to the JSON file (path: `__file_path`)

        Serializes all the objects stored in '__objects' into a dict then to
        JSON string and finally saves them to JSON file specified as
        the class attribute:
        '__file_path'
        """
        filename = FileStorage.__file_path

        # Get a copy of __objects
        objs_copy = FileStorage.__objects

        # Change each object in __objects into it's dictionary representation
        obj_dict = {k: obj.to_dict() for k, obj in objs_copy.items()}

        # Open file and store the JSON string representation into file
        with open(filename, mode='w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the __file_path -> JSON file into '__objects' dictionary
        and back into objects again.

        Read and deserialise the file content with the format,
        ({ <class name>.id: { Attr: value, ... }, ...})
        Then this is used to re-create each instance found in this file

        """
        filename = FileStorage.__file_path
        # Make sure the file exist
        if not path.exists(filename):
            return
        # Get the file content
        with open(filename, mode='r', encoding='utf-8') as f:
            obj_dict = json.load(f)

        # Make a dict to store <obj class name>.id=obj ==> key=value
        objs_dict = {}
        for k, v in obj_dict.items():
            # Get the class name
            class_name = v['__class__']
            # Re-create an object with keyword arguments using the appropriate
            # class name from the global scope.
            obj = globals()[class_name](**v)  # obj = __class__(**v)
            # Update `objs_dict` to hold `<obj class name>.id=obj` pair
            objs_dict[k] = obj

        # Make the objs available to the `FileStorage` class
        FileStorage.__objects = objs_dict
