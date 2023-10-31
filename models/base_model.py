#!/bin/usr/python3
"""This module defines a class BaseModel"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """This class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """This method initializes a BaseModel instance
        Args:
            *args: unused
            **kwargs: key/value pairs used to create instance
        attributes:
            id: unique id for each instance
            created_at: creation date
            updated_at: date of last update
            storage: instance of FileStorage class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
            self.id = kwargs["id"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """This method returns a string representation of a BaseModel
        instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """This method updates the public instance attribute updated_at
        with the current datetime when the object is saved"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This method returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
