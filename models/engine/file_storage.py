#!/usr/bin/python3
"""
Module name: 'file_storage'
Description: This module defines a class 'FileStorage' which is a child-class
             of the 'BaseModel class'.
             It is used in handling the process of saving objects to 
             a file DataBase(JSON) file
             and retrieving of objects from that file for processing.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage:
        This class is used for processing 'BaseModule' objects/instances by:
        * Serializing BaseModel instances into JSON string representation
        * Storing this representation into a file Data Base (JSON file)
        * Retrieving such object via deserializing for processing when needed

    It contains class attributes such as:
        __file_path: path to a JSON file (DBS)
        __objects: dictionary containing objects with key as <class_name>.id

    It also contains processor methods. Such as:
        all(self): returns the dictionary '__objects'
        new(self, obj): sets a new object into the '__objects' dictionary
            with key as '<obj class_name>.id'
        save(self): serializes all the objects stored in '__objects' into
            a JSON string and saves them in the FILE specified by __file_path
        reload(self): deserializes all objects stored in JSON file into
            objects and saves them in '__objects' dictionary for processing
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary: '__objects' class attribute
        """
        return self.__objects

    def new(self, obj):
        """
        Sets a new object 'obj' into the dictionary '__objects'
        """
        key = obj.__class__.__name__ + '.' + obj.id   # <CLASS_NAME>.ID

        # Set in the new object with key: 'key'
        __objects[key] = obj

    def save(self):
        """
        Serializes all the objects stored in '__objects' into a JSON string
        and saves them to JSON file specified as the class attribute:
        '__file_path'
        """
        # Get a copy of __objects
        objects_copy = FileStorage.__objects

        # Change each object in __objects into it's dictionary representation
        for key, obj in objects_copy.items():
            obj_dict = obj.to_dict()
            objects_copy[key] = obj_dict

        # Open file and store the JSON string representation into file
        with open((FileStorage.__file_path, 'w')) as FILE:
            json.dump(FILE, objects_copy)

    def reload(self):
        """
        Deserializes the __file_path -> JSON file into '__objects' dictionary
        """
        if self.__file_path:
            with open(self.__file_path) as FILE:  # Defaults to read
                self.__objects = json.load(FILE)
