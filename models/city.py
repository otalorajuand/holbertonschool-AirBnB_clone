#!/usr/bin/python3
"""this module contains the class City
that inherits from class BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """the class contains:
        Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string"""

    state_id = ""
    name = ""
