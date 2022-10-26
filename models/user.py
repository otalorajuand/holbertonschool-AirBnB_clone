#!/usr/bin/python3
"""this module contains the User
that inherits from class BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """this class defines the User

    Public class attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
