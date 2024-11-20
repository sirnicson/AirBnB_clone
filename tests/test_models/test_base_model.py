#!/usr/bin/python3
"""Unittests for BaseModel."""
import unittest
from datetime import datetime
import uuid
from time import sleep
from unittest.mock import patch

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.storage_manager import StorageManager


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up for each test case."""
        self.storage = StorageManager()  # Using StorageManager
        self.obj = BaseModel()  # Create a new BaseModel instance for testing

    def test_instance_creation(self):
        """Test BaseModel instance creation."""
        self.assertIsInstance(self.obj, BaseModel)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_unique_id(self):
        """Test unique IDs for different instances."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_save_method(self):
        """Test that save updates the updated_at attribute."""
        old_updated_at = self.obj.updated_at
        sleep(0.001)  # Introduce a slight delay to ensure a timestamp difference
        self.obj.save() # Save the object to update the timestamp
        self.assertNotEqual(old_updated_at, self.obj.updated_at)
        self.assertGreater(self.obj.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test to_dict method creates the correct dictionary."""
        obj_dict = self.obj.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], self.obj.id)
        self.assertEqual(obj_dict["created_at"], self.obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], self.obj.updated_at.isoformat())
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_init_new_instance(self):
        """Test initialization of a new BaseModel instance."""
        self.assertIsInstance(self.obj, BaseModel)
        self.assertIsNotNone(self.obj.id)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_init_from_dict(self):
        """Test initialization from a dictionary."""
        obj_dict = self.obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(self.obj.id, new_obj.id)
        self.assertEqual(self.obj.created_at, new_obj.created_at)
        self.assertEqual(self.obj.updated_at, new_obj.updated_at)


    @patch.object(StorageManager, 'save')  # Mock save at the StorageManager level
    @patch.object(FileStorage, 'reload')  # Mock reload to avoid file system interaction
    def test_reload_method(self, mock_reload, mock_save):
        """Test the reload method of StorageManager."""
        mock_reload.return_value = None  # Avoid actual file reading
        mock_save.return_value = None    # Avoid actual file writing

        self.storage.new(self.obj)  # Add object to storage
        self.storage.save()         # Simulate saving process
        self.storage.reload()       # Simulate reload process

        all_objects = self.storage.all()  # Retrieve all objects
        key = f"BaseModel.{self.obj.id}"
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key].id, self.obj.id)


    @patch.object(FileStorage, 'all')
    @patch.object(FileStorage, 'new')
    def test_reload_method_isolated(self, mock_new, mock_all):
        """Test reload behavior in isolation."""
        mock_all.return_value = {f"BaseModel.{self.obj.id}": self.obj}
        mock_new.return_value = None

        self.storage.new(self.obj)  # Add object
        self.storage.reload()       # Mock reload behavior

        all_objects = self.storage.all()
        key = f"BaseModel.{self.obj.id}"
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key].id, self.obj.id)


    def test_reload_empty_file(self):
        """Test FileStorage reload with an empty or missing file."""
        with open('storage/file.json', 'w') as f:
            f.write("")  # Write an empty file

        self.storage.reload()  # Reload should handle this gracefully
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {})




if __name__ == "__main__":
    unittest.main()
