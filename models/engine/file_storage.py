#!/usr/bin/python3
"""Class that serializes instances to a JSON file
    and deserializes JSON file to instances:"""

import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity


class FileStorage:
    """Class that serializes instances to a JSON file
    and deserializes JSON file to instances.

    Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary that will store all objects by
        <class name>.id.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: object to set in __objects.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: val.to_dict() for key, val in
                       FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised).
        """
        from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = {k: BaseModel(
                    **v) for k, v in json.load(f).items()}
