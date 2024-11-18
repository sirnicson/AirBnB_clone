import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    
    def test_instance_creation(self):
        """Test if an instance of BaseModel is created correctly."""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertTrue(hasattr(bm, 'id'))
        self.assertTrue(hasattr(bm, 'created_at'))
        self.assertTrue(hasattr(bm, 'updated_at'))
    
    def test_id_is_unique(self):
        """Test that each instance of BaseModel gets a unique id."""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
    
    def test_str_method(self):
        """Test the __str__ method."""
        bm = BaseModel()
        expected = f"[BaseModel] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected)

    def test_save_method(self):
        """Test that the save method updates the updated_at attribute."""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(bm.updated_at, old_updated_at)
        self.assertTrue(isinstance(bm.updated_at, datetime))
    
    def test_to_dict_method(self):
        """Test the to_dict method."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(bm_dict["id"], bm.id)
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())
    
    def test_to_dict_values(self):
        """Test that to_dict() returns the correct dictionary values."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        
        # Check if all instance variables are correctly converted to dict
        for key, value in bm.__dict__.items():
            if key != "_sa_instance_state":  # Ignore SQLAlchemy internal state if present
                self.assertEqual(bm_dict[key], value)
    
if __name__ == "__main__":
    unittest.main()
