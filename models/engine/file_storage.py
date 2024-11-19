#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """Handles serialization and deserialization of BaseModel instances."""
    
    __file_path = 'file.json'
    __objects = {}
    
    def all(self):
        """Returns the dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to __objects dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass  # Ignore if the file doesn't exist

