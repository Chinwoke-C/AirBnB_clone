#!/usr/bin/python3

""" """



import json
from os.path import exists
from models.base_model import BaseModel


class FileStorage:
    """ """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ """
        return self.__objects
    
    def new(self, obj):
        """ """
        class_name = obj.__class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

    
    def save(self):
        """ """
        obj_dict = {}
        for key, values in self.__objects.items():
            # I dont know whats causing the error on this line
            # I've tried everything
            obj_dict[key] = values.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)


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

