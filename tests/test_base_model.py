import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel"""

    def test_instance_creation(self):
        """Test the creation of a new BaseModel instance"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)  # Check that it's an instance of BaseModel
        self.assertIsInstance(bm.id, str)  # id should be a string
        self.assertIsInstance(bm.created_at, datetime)  # created_at should be a datetime object
        self.assertIsInstance(bm.updated_at, datetime)  # updated_at should be a datetime object

    def test_str_method(self):
        """Test the string representation of the BaseModel instance"""
        bm = BaseModel()
        # Check that the __str__ method returns the correct format
        expected_str = f"[{bm.__class__.__name__}] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected_str)

    def test_save_method(self):
        """Test the save method that updates updated_at"""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()  # Call save to update updated_at
        self.assertNotEqual(bm.updated_at, old_updated_at)  # updated_at should be updated

    def test_to_dict_method(self):
        """Test the to_dict method"""
        bm = BaseModel()
        bm_dict = bm.to_dict()

        # Check if to_dict includes all keys and correct values
        self.assertIn("id", bm_dict)
        self.assertIn("created_at", bm_dict)
        self.assertIn("updated_at", bm_dict)
        self.assertIn("__class__", bm_dict)  # Should include the class name
        self.assertEqual(bm_dict["__class__"], "BaseModel")  # The class name should be 'BaseModel'
        
        # Check if created_at and updated_at are in ISO format
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
