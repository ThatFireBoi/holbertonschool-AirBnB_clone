#!/usr/bin/python3
"""This module defines a class to manage file storage for the HBnB clone"""


import json
from os import path
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User


class FileStorage:
    """This class manages storage of HBnB models in JSON format

    Attributes:
        __file_path (str): path to JSON file
        __objects (dict): dictionary of models currently in storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps)(new_dict)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists); otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                class_name = value['__class__']
                del value['__class__']
                self.new(eval(class_name)(**value))
