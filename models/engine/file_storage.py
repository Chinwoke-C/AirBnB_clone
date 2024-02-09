#!/usr/bin/python3

""" Defines the FileStorage class."""



import json
from os.path import exists
from models.base_model import BaseModel

class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects. 
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in dictionary the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj
    
    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        obj_dict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)
    
def reload(self):
    """Reload objects from the JSON file."""
    if exists(self.__file_path):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            print("Error: The JSON file does not exist.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON data from the file.")
    else:
        print("Warning: The JSON file does not exist. No action taken.")
