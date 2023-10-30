import uuid
from datetime import datetime
from models import storage  # Import the storage instance
""" This module defines a BaseModel class"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Initialize a new BaseModel.
        Args:
                  *args (any): Unused.
                  **kwargs (dict): Key/value pairs of attributes.
        Attributes:
        id (str): The BaseModel id.
        created_at (datetime): The datetime at creation.
        updated_at (datetime): The datetime of last update."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)  # Call new method of the storage instance

    def save(self):
        """ Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()  # Call save method of the storage instance

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
