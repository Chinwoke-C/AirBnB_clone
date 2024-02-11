#!/usr/bin/python3
""" Defines Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits BaseModel """
    place_id = ""
    user_id = ""
    text = ""
