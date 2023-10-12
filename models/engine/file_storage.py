"""
Module Name: models/engine/file_storage.py
Description: This module provides a `FileStorage` class
             that serializes instances to a JSON file and
             deserializes JSON file to instances.

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
        """Deserializes the JSON file to `__objects`.

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
