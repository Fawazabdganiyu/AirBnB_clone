"""
Module Name: models/engine/file_storage.py
Description: This module provides a `FileStorage` class
             that serializes instances to a JSON file and
             deserializes JSON file to instances.

"""
import json
from models.base_model import BaseModel
from models.user import User
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

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in `__objects` the `obj` with key `<obj class name>.id`
        """
        obj_class = obj.__class__.__name__
        key = str(obj_class) + "." + obj.id  # <obj class name>.id

        FileStorage.__objects.update({key: obj})

    def save(self):
        """serializes `__objects` to the JSON file (path: `__file_path`)
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
        """deserializes the JSON file to `__objects`.
        """
        filename = FileStorage.__file_path
        # Make sure the file exist
        if not path.exists(filename):
            return
        # Read and deserialise the file content
        # ({ <obj class name>.id: { Attribute1: value1, ... } })
        # for each BaseModel instance stored.
        with open(filename, mode='r', encoding='utf-8') as f:
            obj_dict = json.load(f)

        # Make a dict to store <obj class name>.id=obj ==> key=value
        objs_dict = {}
        for k, v in obj_dict.items():
            # Recreate the BaseModel instances from
            # the saved dict values as `obj`
            class_name = v['__class__']

            # Get the value of the expected class name from the global scope
            obj = globals()[class_name](**v)  # obj = __class__(**v)
            # Update `objs_dict` to hold `<obj class name>.id=obj` pair
            objs_dict[k] = obj

        # Assign the dict of recreated instances
        # to the private class instance `objects`.
        FileStorage.__objects = objs_dict
