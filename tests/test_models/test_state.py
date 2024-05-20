#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up for each test method"""
        self.state = State()

    def test_instance_creation(self):
        """Test if an instance is created correctly"""
        self.assertIsInstance(self.state, State)

    def test_inheritance(self):
        """Test if State inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_name(self):
        """Test the default value of name"""
        self.assertEqual(self.state.name, "")

    def test_str_method(self):
        """Test the string representation of the instance"""
        state_str = str(self.state)
        self.assertIn(f"[State] ({self.state.id})", state_str)

    def test_to_dict(self):
        """Test the to_dict method"""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["id"], self.state.id)
        self.assertEqual(state_dict["created_at"], self.state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"], self.state.updated_at.isoformat())

    def test_save_method(self):
        """Test the save method updates updated_at"""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)


if __name__ == "__main__":
    unittest.main()
