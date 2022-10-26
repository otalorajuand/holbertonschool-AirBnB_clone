#!/usr/bin/python3
"""
this module contains the class Amenity
that inherits from class BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The class defines the Amenity 

        Public class attributes:
            name (str) - The name of the amenity
    """

    name = ""
