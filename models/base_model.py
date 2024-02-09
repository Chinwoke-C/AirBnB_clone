#!/usr/bin/python3

"""Defines the BaseModel class."""

from datetime import datetime
from uuid import uuid4
from models import storage

class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):

        """initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    
    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""

        return f"{self.__class__.__name__} {self.id} {self.__dict__}"
    
    def save(self):
        """Update updated_at with the current datetime."""

        self.updated_at = datetime.now()
        storage.save()

    
    def to_dict(self):
        """ Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.

        """
        r_dict = self.__dict__
        r_dict["__class__"] = self.__class__.__name__
        r_dict["created_at"] = self.created_at.isoformat()
        r_dict["updated_at"] = self.updated_at.isoformat()
        return r_dict
