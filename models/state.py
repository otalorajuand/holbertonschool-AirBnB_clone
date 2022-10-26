#!/usr/bin/python3
"""this module contains the class State
that inherits from class BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """The class defines State

    Public class attributes:
        name (str): The name of the state.
    """

    name = ""
