#!/usr/bin/python3
"""
Module Name: test_file_storage
Description: Contains test suite for the file_storage module

"""
import unittest
import json
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    TestFileStorage:
        Test suite class used to test all the functionalities of
        `FileStorage` class
    """
    def setUp(self):
        self.storage_obj = FileStorage()

    def test_is_instance(self):
        """
        Test if an object is an instance of FileStorage
        """
        self.assertIsInstance(self.storage_obj, FileStorage)

    @unittest.expectedFailure
    def test_class_attributes(self):
        """
        Test that its class attributes are private
        """
        self.assertTrue(hasattr(self.storage_obj, "__file_path"))
        self.assertTrue(hasattr(self.storage_obj, "__objects"))

    def test_method_all(self):
        """
        Testcase for the `all` method for its functionality
        """
        dict_retval = self.storage_obj.all()
        self.assertIsInstance(dict_retval, dict)

        # Test that the objects stored in the __objects dict are not dict
        for obj in dict_retval.values():
            self.assertNotIsInstance(obj, dict)

    def test_all_no_arg(self):
        """
        Test that method `all()` takes no argument
        """
        with self.assertRaises(TypeError):
            self.storage_obj.all('User')

    def test_method_new(self):
        """
        Testcase for the `new` method for its functionality
        """
        new_obj = BaseModel()
        new_obj_key = f"{new_obj.__class__.__name__}.{new_obj.id}"

        self.storage_obj.new(new_obj)
        all_objs = self.storage_obj.all()

        self.assertIn(new_obj_key, all_objs.keys())
        self.assertEqual(new_obj, all_objs[new_obj_key])

    def test_new_one_arg(self):
        """
        Test that method `new()` takes one argument
        """
        with self.assertRaises(TypeError):
            self.storage_obj.new()

        with self.assertRaises(TypeError):
            obj1 = BaseModel()
            obj2 = User()
            self.storage_obj.new(obj1, obj2)

    def test_method_save(self):
        """
        Testcase for the `save` method, testing its functionalities
        """
        # Create a user instance
        user_obj = User()
        created_at = user_obj.created_at

        # Save this user along with its time of updation
        user_obj.save()

        # Get and compare its updation time with its creation time
        updated_at = user_obj.updated_at
        self.assertNotEqual(created_at, updated_at)

        # Get from JSON file
        all_objs = {}
        try:
            with open("file.json", mode="r", encoding="utf-8") as FILE:
                all_objs_str = FILE.read()
                all_objs = json.load(FILE)
        except json.decoder.JSONDecodeError:
            pass

        # Confirm that the content save to FILE is a JSON string
        self.assertIsInstance(all_objs_str, str)

        # Confirm that the content saved to FILE is a dict
        self.assertIsInstance(all_objs, dict)

    def test_save_no_arg(self):
        """
        Test that the `save()` method takes no argument
        """
        john = User()
        eric = User()

        with self.assertRaises(TypeError):
            self.storage_obj.save(john)

        with self.assertRaises(TypeError):
            self.storage_obj.save(john, eric)

    def test_method_reload(self):
        """
        Testcase for the `reload` method, testing its functionalities
        """
        before_reload = self.storage_obj.all()

        new_obj = User()
        self.storage_obj.save()  # Save the new object in json file

        self.storage_obj.reload()
        after_reload = self.storage_obj.all()

        self.assertNotEqual(before_reload, after_reload)

    def test_reload_no_arg(self):
        """
        Test that the `reload()` method takes no argument
        """
        with self.assertRaises(TypeError):
            self.storage_obj.reload('User')

        with self.assertRaises(TypeError):
            self.storage_obj.reload('User', 'City')

    def test_storage_variable(self):
        """
        Testcase to check if the FileStorage linker-variable exist
        """
        self.assertIsNotNone(storage)

    def test_storage_is_FileStorage_instance(self):
        """
        Tests to make sure `storage` variable is an instance of FileStorage
        """
        self.assertIsInstance(storage, FileStorage)

    def test_storage_has_FileStorage_methods(self):
        """
        Test to check that `storage` variable has all FileStorage methods
        """
        self.assertIn('all', dir(storage))
        self.assertIn('new', dir(storage))
        self.assertIn('save', dir(storage))
        self.assertIn('reload', dir(storage))

    def tearDown(self):
        del self.storage_obj
