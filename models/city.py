#!/usr/bin/python3
"""This module defines a class City"""


from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a City object

    Attributes:
        state_id (str): The state id
        name (str): The name of the city
    """

    state_id = ""
    name = ""
