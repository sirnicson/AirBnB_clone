#!/usr/bin/python3
"""Unittests for BaseModel."""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance_creation(self):
        """Test BaseModel instance creation."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_unique_id(self):
        """Test unique IDs for different instances."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_save_method(self):
        """Test that save updates the updated_at attribute."""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        sleep(0.001)  # Introduce a slight delay to ensure a timestamp difference
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test to_dict method creates the correct dictionary."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_init_new_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_init_from_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(obj.id, new_obj.id)
        self.assertEqual(obj.created_at, new_obj.created_at)
        self.assertEqual(obj.updated_at, new_obj.updated_at)



if __name__ == "__main__":
    unittest.main()
