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
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets a new object 'obj' into the dictionary '__objects'
        """
        key = obj.__class__.__name__ + '.' + obj.id   # <CLASS_NAME>.ID

        # Set in the new object with key: 'key'
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes all the objects stored in '__objects' into a dict then to
        JSON string and finally saves them to JSON file specified as the class attribute:
        '__file_path'
        """
        # Get a copy of __objects
        objects_copy = FileStorage.__objects

        # Convert objects to their dict representation for saving
        for key_id, obj in objects_copy.items():
            objects_copy[key_id] = obj.to_dict()

        # Open file and store the JSON string representation into file
        with open(FileStorage.__file_path, 'w') as FILE:
            json.dump(objects_copy, FILE)

    def reload(self):
        """
        Deserializes the __file_path -> JSON file into '__objects' dictionary
        and back into objects again
        """
        from models.base_model import BaseModel

        try:
            with open(FileStorage.__file_path) as FILE:  # Defaults to read
                # It comes out as dict containing dict-representation of objects
                FileStorage.__objects = json.load(FILE)
        except Exception:
            pass
        finally:  # Therefore we convert them back into objects
            for key_id, obj_dict in FileStorage.__objects.items():
                FileStorage.__objects[key_id] = BaseModel(**obj_dict)
