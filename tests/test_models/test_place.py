#!/usr/bin/python3
"""
Module Name: test_place
Description: Provides a test suite for the `Place` class located inside
    the `models.place` module
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """
    Test-suite for `Place` class instances
    """
    def test_place_1(self):
        """
        Test if the `Place` class exist
        """
        palladan = None
        palladan = Place()
        self.assertIsNotNone(palladan)

    def test_place_2(self):
        """
        Test `Place` instances / objects
        """
        lagos_street = Place()
        pz = Place()
        bassawa = Place()

        self.assertTrue(isinstance(lagos_street, Place))
        self.assertTrue(isinstance(pz, Place))
        self.assertTrue(isinstance(bassawa, Place))

    def test_place_inheritance(self):
        """
        Test that the `Place` class inherited from the BaseModel class
        """
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_attributes(self):
        """
        Test that the `Place` class has its attributes
        """
        place = Place()

        self.assertIn("name", dir(place))
        self.assertIn("city_id", dir(place))
        self.assertIn("user_id", dir(place))
        self.assertIn("description", dir(place))
        self.assertIn("number_rooms", dir(place))
        self.assertIn("number_bathrooms", dir(place))
        self.assertIn("max_guest", dir(place))
        self.assertIn("price_by_night", dir(place))
        self.assertIn("latitude", dir(place))
        self.assertIn("longitude", dir(place))
        self.assertIn("amenity_ids", dir(place))

    def test_place_attributes_str(self):
        """
        Test that the `Place` class has string attributes
        """
        place = Place()

        self.assertTrue(isinstance(place.name, str))
        self.assertTrue(isinstance(place.city_id, str))
        self.assertTrue(isinstance(place.user_id, str))
        self.assertTrue(isinstance(place.description, str))

    def test_place_attributes_int(self):
        """
        Test that the `Place` class has attributes of type integer
        """
        place = Place()

        self.assertTrue(isinstance(place.number_rooms, int))
        self.assertTrue(isinstance(place.number_bathrooms, int))
        self.assertTrue(isinstance(place.max_guest, int))
        self.assertTrue(isinstance(place.price_by_night, int))

    def test_place_attributes_float(self):
        """
        Test that the `Place` class has attributes of type float
        """
        place = Place()

        self.assertTrue(isinstance(place.latitude, float))
        self.assertTrue(isinstance(place.longitude, float))

    def test_place_attributes_list(self):
        """
        Test that the `Place` has attributes of type list
        """
        place = Place()

        self.assertTrue(isinstance(place.amenity_ids, list))

    def test_place_has_BaseModels_methods(self):
        """
        Test that `Place` has all BaseModel's method
        """
        place = Place()

        self.assertIn("created_at", dir(place))
        self.assertIn("updated_at", dir(place))
        self.assertIn("save", dir(place))
        self.assertIn("id", dir(place))
        self.assertIn("to_dict", dir(place))
