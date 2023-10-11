"""
Module Name: models/engine/file_storage.py
Description: This module provides a `FileStorage` class
             that serializes instances to a JSON file and
             deserializes JSON file to instances.

"""
import json
from os import path


class FileStorage:
    """A definition of `FileStorage` class for serialization/deserialization.

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
        key = str(obj_class) + "." + obj.id

        FileStorage.__objects.update({key: obj})

    def save(self):
        """serializes `__objects` to the JSON file (path: `__file_path`)
        """
        filename = FileStorage.__file_path
        with open(filename, mode='w', encoding='utf-8') as f:
            # update with latest __dict__
            to_dict = {k: str(obj) for k, obj in FileStorage.__objects.items()}

            json.dump(to_dict, f)

    def reload(self):
        """deserializes the JSON file to `__objects`.
        """
        filename = FileStorage.__file_path
        if path.exists(filename):
            with open(filename, mode='r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
