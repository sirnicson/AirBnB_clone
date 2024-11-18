#!/usr/bin/python3
"""The BaseModel class nBnB"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """Initialize a new BaseModel Instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the 'update_at' attribute to the current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all instance attributes"""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
