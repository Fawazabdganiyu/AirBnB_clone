#!/usr/bin/python3
"""
Module Name: test_amenity
Description: Provides a test suite for the `Amenity` class located inside
    the `models.amenity` module
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.__init__ import storage


class TestAmenityClass(unittest.TestCase):
    """
    Test-suite for `Amenity` class instances
    """
    def test_amenity_1(self):
        """
        Test if the `Amenity` class exist
        """
        electricity = None
        electricity = Amenity()
        self.assertIsNotNone(electricity)

    def test_amenity_2(self):
        """
        Test `Amenity` instances / objects
        """
        water = Amenity()
        electricity = Amenity()
        wifi = Amenity()

        self.assertTrue(isinstance(water, Amenity))
        self.assertTrue(isinstance(electricity, Amenity))
        self.assertTrue(isinstance(wifi, Amenity))

    def test_amenity_inheritance(self):
        """
        Test that the `Amenity` class inherited from the BaseModel class
        """
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_attribute(self):
        """
        Test that the `Amenity` class has its attributes
        """
        internet = Amenity()

        self.assertIn("name", dir(internet))

    def test_amenity_attributes_type(self):
        """
        Test that the `amenity` attributes is of the right type
        """
        amenity = Amenity()

        self.assertTrue(isinstance(amenity.name, str))

    def test_amenity_has_BaseModels_methods(self):
        """
        Test that `Amenity` has all BaseModel's method
        """
        amenity = Amenity()

        self.assertIn("created_at", dir(amenity))
        self.assertIn("updated_at", dir(amenity))
        self.assertIn("save", dir(amenity))
        self.assertIn("id", dir(amenity))
        self.assertIn("to_dict", dir(amenity))
