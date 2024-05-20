#!/usr/bin/python3

# Unittest for BaseModel class

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up for each test method"""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if an instance is created correctly"""
        self.assertIsInstance(self.model, BaseModel)

    def test_id_is_unique(self):
        """Test if id is unique"""
        another_model = BaseModel()
        self.assertNotEqual(self.model.id, another_model.id)

    def test_id_is_string(self):
        """Test if id is a string"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """Test if created_at is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test if updated_at is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """Test the string representation of the instance"""
        model_str = str(self.model)
        self.assertIn(f"[BaseModel] ({self.model.id})", model_str)

    def test_save_method(self):
        """Test the save method updates updated_at"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(
            model_dict["created_at"],
            self.model.created_at.isoformat()
        )
        self.assertEqual(
            model_dict["updated_at"],
            self.model.updated_at.isoformat()
        )

    def test_kwargs(self):
        """Test instantiation with kwargs"""
        model_dict = self.model.to_dict()
        model_dict.pop('__class__', None)  # Remove the __class__ key
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)


if __name__ == "__main__":
    unittest.main()
