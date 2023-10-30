#!/usr/bin/python3
"""
Module base_model
Contains a Class that defines all common attributes or
methods for other classes
"""

from datetime import datetime
import uuid
import models


class BaseModel():
    ''' a base class for other classes '''

    def __init__(self, *args, **kwargs):
        '''
        initializes the values
        '''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        '''
        print in "[<class name>] (<self.id>) <self.__dict__>" format
        '''
        return ('[{}] ({}) {}'.format(
            self.__class__.__name__,
            self.id,
            self.__dict__))

    def save(self):
        '''
        updates the public instance attribute updated_at
        with the current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save(self)

    def to_dict(self):
        '''
        returns a dictionary containing all keysvalues
        of __dict__ of the instance
        '''
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
