#!/usr/bin/python3
"""
This module contains the class BaseModel
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """defines all common attributes/methods for other classes

    Attributes:
        id (str): unique id for each instance.
        created_at (datetime): current datetime when an instance is created
        updated_at (datetime): current datetime when an instance is created
        and it will be updated every time you change your object
    """

    def __init__(self, *args, **kwargs):

        if not kwargs == {}: 
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

            self.created_at = datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime"""
        storage.new(self)
        storage.save()

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""

        res = self.__dict__
        res['__class__'] = self.__class__.__name__
        res['created_at'] = res['created_at'].isoformat()
        res['updated_at'] = res['updated_at'].isoformat()

        return res
