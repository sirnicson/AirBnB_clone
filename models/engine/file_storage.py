#!/usr/bin/python3
import json

class FileStorage:
    """Handles serialization and deserialization of BaseModel instances."""
    
    __file_path = 'storage/file.json'
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
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                try:
                    objects_dict = json.load(f)
                    for key, value in objects_dict.items():
                        class_name = value["__class__"]
                        class_ = globals()[class_name]  # Get class by name
                        self.__objects[key] = class_(**value)
                except json.JSONDecodeError:
                    self.__objects = {}
        except FileNotFoundError:
            self.__objects = {}
