#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up for each test method"""
        self.city = City()

    def test_instance_creation(self):
        """Test if an instance is created correctly"""
        self.assertIsInstance(self.city, City)

    def test_inheritance(self):
        """Test if City inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_state_id(self):
        """Test the default value of state_id"""
        self.assertEqual(self.city.state_id, "")

    def test_name(self):
        """Test the default value of name"""
        self.assertEqual(self.city.name, "")

    def test_str_method(self):
        """Test the string representation of the instance"""
        city_str = str(self.city)
        self.assertIn(f"[City] ({self.city.id})", city_str)

    def test_to_dict(self):
        """Test the to_dict method"""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["id"], self.city.id)
        self.assertEqual(city_dict["created_at"], self.city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], self.city.updated_at.isoformat())

    def test_save_method(self):
        """Test the save method updates updated_at"""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)


if __name__ == "__main__":
    unittest.main()
