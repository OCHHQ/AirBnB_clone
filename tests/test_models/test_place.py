#!/usr/bin/python3
"""
Unittest for Place class
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up for each test method"""
        self.place = Place()

    def test_instance_creation(self):
        """Test if an instance is created correctly"""
        self.assertIsInstance(self.place, Place)

    def test_inheritance(self):
        """Test if Place inherits from BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_city_id(self):
        """Test the default value of city_id"""
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """Test the default value of user_id"""
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """Test the default value of name"""
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """Test the default value of description"""
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """Test the default value of number_rooms"""
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """Test the default value of number_bathrooms"""
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """Test the default value of max_guest"""
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """Test the default value of price_by_night"""
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """Test the default value of latitude"""
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """Test the default value of longitude"""
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """Test the default value of amenity_ids"""
        self.assertEqual(self.place.amenity_ids, [])

    def test_str_method(self):
        """Test the string representation of the instance"""
        place_str = str(self.place)
        self.assertIn(f"[Place] ({self.place.id})", place_str)

    def test_to_dict(self):
        """Test the to_dict method"""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["id"], self.place.id)
        self.assertEqual(place_dict["created_at"], self.place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"], self.place.updated_at.isoformat())

    def test_save_method(self):
        """Test the save method updates updated_at"""
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)


if __name__ == "__main__":
    unittest.main()
