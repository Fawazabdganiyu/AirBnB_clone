#!/usr/bin/python3
"""
Module Name: test_user
Description: Provides a test suite for the `User` class located inside
    the `models.user` module
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models.__init__ import storage


class TestUserClass(unittest.TestCase):
    """
    Test-suite for `User` class instances
    """
    def setUp(self):
        """
        Create a User object at every test case
        """
        self.user = None
        self.user = User()

    def test_user_1(self):
        """
        Test if the `User` class exist
        """
        self.assertIsNotNone(self.user)

    def test_user_2(self):
        """
        Test `User` instances / objects
        """
        user1 = User()
        user2 = User()
        user3 = User()
        self.assertIsInstance(user1, User)
        self.assertIsInstance(user2, User)
        self.assertIsInstance(user3, User)

    def test_user_inheritance(self):
        """
        Test that the `User` class inherited from the `BaseModel` class
        """
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_attribute_first_name_exist(self):
        """
        Test that the `User` class attributes ``first_name`` exists
        """
        self.assertIn("first_name", dir(self.user))

    def test_user_attribute_last_name_exist(self):
        """
        Test that the `User` class attribute ``last_name`` exists
        """
        self.assertIn("last_name", dir(self.user))

    def test_user_attribute_email_exist(self):
        """
        Test that the `User` class attribute ``email`` exists
        """
        self.assertIn("email", dir(self.user))

    def test_user_attribute_password_exist(self):
        """
        Test that the `User` class attribute password exists
        """
        self.assertIn("password", dir(self.user))

    def test_user_attribute_email_type(self):
        """
        Test that `User` attribute ``email`` is of type string
        """
        self.assertIsInstance(self.user.email, str)

    def test_user_attribute_password_type(self):
        """
        Test that `User` attribute ``password`` is of type string
        """
        self.assertIsInstance(self.user.password, str)

    def test_user_has_BaseModels_methods(self):
        """
        Test that `User` has all BaseModel's method
        """
        self.assertIn("created_at", dir(self.user))
        self.assertIn("updated_at", dir(self.user))
        self.assertIn("save", dir(self.user))
        self.assertIn("id", dir(self.user))
        self.assertIn("to_dict", dir(self.user))

    def test_user_to_dict_method(self):
        """
        Test `User`'s ``to_dict`` method to see if it aligns to
        user information
        """
        user_dict = self.user.to_dict()
        self.assertEqual("User", user_dict["__class__"])

    def test_user_id(self):
        """
        Test that `User` id
        """
        user_dict = self.user.to_dict()
        id_ = self.user.id

        self.assertIn(id_, user_dict.values())

    def test_user_key(self):
        """
        Test that `User` key is "User.<id>" in all objects dictionary
        """
        all_objs = storage.all()
        user_dict = self.user.to_dict()

        id_ = user_dict["id"]
        key = f"User.{id_}"

        self.assertIn(key, all_objs.keys())

    def tearDown(self):
        """
        Deletes the `User` object created at each tests
        """
        del self.user
