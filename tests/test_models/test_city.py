#!/usr/bin/python3
"""
Module Name: test_city
Description: Provides a test suite for the `City` class located inside
    the `models.place` module
"""
import unittest
from models.city import City
from models.base_model import BaseModel
from models import storage


class TestCityClass(unittest.TestCase):
    """
    Test-suite for `City` class instances
    """
    def test_city_1(self):
        """
        Test if the `City` class exist
        """
        self.assertTrue(issubclass(City, object))

    def test_city_2(self):
        """
        Test `City` instances / objects
        """
        city1 = City()
        city2 = City()
        city3 = City()

        self.assertIsInstance(city1, City)
        self.assertIsInstance(city2, City)
        self.assertIsInstance(city3, City)

    def test_city_inheritance(self):
        """
        Test that the `City` class inherited from the `BaseModel` class
        """
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_attributes(self):
        """
        Test that the `City` class attributes exist
        """
        city = City()

        self.assertIn("name", dir(city))
        self.assertIn("state_id", dir(city))

    def test_city_attribute_name_type(self):
        """
        Test that the `City` attribute ``name`` is of type string
        """
        city = City()
        self.assertIsInstance(city.name, str)

    def test_city_attribute_state_id_type(self):
        """
        Test that the `City` attribute ``state_id`` is of string type
        """
        city = City()
        self.assertIsInstance(city.state_id, str)

    def test_city_to_dict(self):
        """
        Test that the `City` to_dict() method aligns with City
        """
        city = City()
        city_dict = city.to_dict()
        self.assertEqual("City", city_dict["__class__"])

    def test_city_id(self):
        """
        Test that `City` has its id string
        """
        city = City()
        city_dict = city.to_dict()

        id_ = city.id

        self.assertIsInstance(city.id, str)
        self.assertTrue(id_ == city_dict["id"])

    def test_city_key(self):
        """
        Test that `City` key is "User.<id>" in all objects dictionary
        """
        city = City()
        id_ = city.id
        key = f"City.{id_}"

        all_objs = storage.all()
        self.assertIn(key, all_objs.keys())

    def test_city_has_BaseModels_methods(self):
        """
        Test that `City` class has all BaseModel's method
        """
        city = City()

        self.assertIn("created_at", dir(city))
        self.assertIn("updated_at", dir(city))
        self.assertIn("save", dir(city))
        self.assertIn("id", dir(city))
        self.assertIn("to_dict", dir(city))
