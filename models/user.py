#!/usr/bin/python3
"""This module defines a class User"""


from models.base_model import BaseModel
from datetime import datetime


class User(BaseModel):
    """This class defines a User object"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """ constructor method """
        self.created_at = datetime.now()
