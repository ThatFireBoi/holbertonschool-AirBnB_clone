#!/usr/bin/python3


"""This is the base model class for AirBnB"""

from uuid import uuid4  # for uuid
from datetime import datetime  # for datetime
from models import storage  # for storage
import uuid  # for uuid
import json
import sys
import os.path


class BaseModel():
    """ A base class for other classes"""

    def __init__(self, *args, **kwargs):
        """ Initializes the attributes"""
        if kwargs:
            dtf = "%Y-%m-%dT%H:%M:%S.%f"
            k_dict = kwargs.copy()
            del k_dict['__class__']
            for key in k_dict:
                if ("created_at" == key or "update_at == key"):
                    k_dict[key] = datetime.strptime(k_dict[key], dtf)
            self.__dict__ = k_dict
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Print in "[<class name>], (<self.id>) <self.__dict__>" format """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute updated_at with the current
        datetime """
        self.updated_at = datetime.now()
        storage.save()  # save to file

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the
        instance """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
