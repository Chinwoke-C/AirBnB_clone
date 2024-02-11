#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city inheriting from the BaseModel class.

    """

    state_id = ""
    name = ""
