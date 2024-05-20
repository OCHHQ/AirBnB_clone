#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up for each test method"""
        self.user = User()

    def test_instance_creation(self):
        """Test if an instance is created correctly"""
        self.assertIsInstance(self.user, User)

    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_email(self):
        """Test the default value of email"""
        self.assertEqual(self.user.email, "")

    def test_password(self):
        """Test the default value of password"""
        self.assertEqual(self.user.password, "")

    def test_first_name(self):
        """Test the default value of first_name"""
        self.assertEqual(self.user.first_name, "")

    def test_last_name(self):
        """Test the default value of last_name"""
        self.assertEqual(self.user.last_name, "")

    def test_str_method(self):
        """Test the string representation of the instance"""
        user_str = str(self.user)
        self.assertIn(f"[User] ({self.user.id})", user_str)

    def test_to_dict(self):
        """Test the to_dict method"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["id"], self.user.id)
        self.assertEqual(user_dict["created_at"], self.user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], self.user.updated_at.isoformat())

    def test_save_method(self):
        """Test the save method updates updated_at"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)


if __name__ == "__main__":
    unittest.main()
