#!/usr/bin/python3
"""
BaseModel class to be inherited by other models.
"""


class BaseModel:
    def __init__(self, id=None):
        """
        Initializes a new BaseModel instance with an optional ID.
        """
        self.id = id
