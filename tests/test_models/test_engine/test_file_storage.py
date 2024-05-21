#!/usr/bin/python3
"""
Unittest for FileStorage class
"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up for each test method"""
        self.storage = FileStorage()
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Clean up after each test method"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        """Test all method returns a dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        """Test new method adds an object to __objects"""
        model = BaseModel()
        key = f"BaseModel.{model.id}"
        self.storage.new(model)
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        """Test save method creates a file"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_deserializes_objects(self):
        """Test reload method deserializes objects from file"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{model.id}"
        self.assertIn(key, self.storage.all())

if __name__ == "__main__":
    unittest.main()
