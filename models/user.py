#!/usr/bin/python3
"""this module contains the User
that inherits from class BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """this class contains the next public attributes
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
        """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
