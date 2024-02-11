#!/usr/bin/python3

"""Defines a FileStorage class"""



import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents an abstracted storage engine"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects
    
    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

    
    def save(self):
        """ serializes objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fname:
            new_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(new_dict, fname)


# I used this to handle error IGNORE!!!!
            
# def reload(self):
#     """Reload objects from the JSON file."""
#     if exists(self.__file_path):
#         try:
#             with open(self.__file_path, "r") as file:
#                 self.__objects = json.load(file)
#         except FileNotFoundError:
#             print("Error: The JSON file does not exist.")
#         except json.JSONDecodeError as e:
#             print(f"Error: Failed to decode JSON data from the file: {e}")
#     else:
#         print("Warning: The JSON file does not exist. No action taken.")


    def reload(self):
        """Reload objects from the JSON file."""
        if exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                    self.__objects = json.load(file)
        else:
            print("Error: The JSON file does not exist.")

