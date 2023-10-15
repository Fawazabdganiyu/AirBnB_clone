#!/usr/bin/python3
"""
Module Name: test_city
Description: Provides a test suite for the `City` class located inside
    the `models.city` module
"""
import unittest
from models.city import City
from models.base_model import BaseModel
from models.__init__ import storage


class TestCityClass(unittest.TestCase):
    """
    Test-suite for `City` class instances
    """
    def test_city_1(self):
        """
        Test if the City class exist
        """
        city = None
        city = City()
        self.assertIsNotNone(city)

    def test_city_2(self):
        """
        Test City instances / objects
        """
        city1 = City()
        city2 = City()
        city3 = City()

        self.assertTrue(isinstance(city1, City))
        self.assertTrue(isinstance(city2, City))
        self.assertTrue(isinstance(city3, City))

    def test_city_inheritance(self):
        """
        Test that the City class inherited from the BaseModel class
        """
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_attribute(self):
        """
        Test that the `city` class has its attributes
        """
        city = City()

        self.assertIn("name", dir(city))
        self.assertIn("state_id", dir(city))

    def test_city_attribute_type(self):
        """
        Test that `City` attributes are of right types
        """
        city = City()

        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)

    def test_city_has_BaseModels_methods(self):
        """
        Test that `City` has all BaseModel's method
        """
        city = City()

        self.assertIn("created_at", dir(city))
        self.assertIn("updated_at", dir(city))
        self.assertIn("save", dir(city))
        self.assertIn("id", dir(city))
        self.assertIn("to_dict", dir(city))
