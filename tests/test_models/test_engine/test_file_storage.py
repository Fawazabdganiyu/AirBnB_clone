#!/usr/bin/python3
"""
Module Name: test_file_storage
Description: Contains test suite for the file_storage module

"""
import unittest
import json
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    TestFileStorage:
        Test suite class used to test all the functionalities of
        `FileStorage` class
    """
    def setUp(self):
        self.fs = FileStorage()

    def test_is_instance(self):
        """
        Test if an object is an instance of FileStorage
        """
        self.assertIsInstance(self.fs, FileStorage)

    def test_class_attributes(self):
        """
        Test that its class attributes are private
        """
        self.assertTrue(hasattr(self.fs, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.fs, "_FileStorage__objects"))

        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_method_all(self):
        """
        Testcase for the `all` method for its functionality
        """
        dict_retval = self.fs.all()
        self.assertIsInstance(dict_retval, dict)

        # Test that the objects stored in the __objects dict are not dict
        for obj in dict_retval.values():
            self.assertNotIsInstance(obj, dict)

    def test_all_no_arg(self):
        """
        Test that method `all()` takes no argument
        """
        with self.assertRaises(TypeError):
            self.fs.all('User')

    def test_method_new(self):
        """
        Testcase for the `new` method for its functionality
        """
        new_obj = BaseModel()
        new_obj_key = f"{new_obj.__class__.__name__}.{new_obj.id}"

        self.fs.new(new_obj)
        all_objs = self.fs.all()

        self.assertIn(new_obj_key, all_objs.keys())
        self.assertEqual(new_obj, all_objs[new_obj_key])

    def test_new_one_arg(self):
        """
        Test that method `new()` takes one argument
        """
        with self.assertRaises(TypeError):
            self.fs.new()

        with self.assertRaises(TypeError):
            obj1 = BaseModel()
            obj2 = BaseModel()
            self.fs.new(obj1, obj2)

    def test_method_save(self):
        """
        Testcase for the `save` method, testing its functionalities
        """
        # Create a user instance
        bm = BaseModel()

        created = bm.created_at

        bm.name = "John Smith"
        bm.age = 98
        # Save this user along with its time of updation
        bm.save()

        # Get and compare its updation time with its creation time
        updated = bm.updated_at
        self.assertNotEqual(created, updated)

    def test_storage_save(self):
        """
        Test that storage save(self) is called in BaseModel
        """
        bm = BaseModel()
        bm.name = "Test Model"
        bm_key = f'BaseModel.{bm.id}'
        storage.new(bm)
        storage.save()
        # Get from JSON file
        with open("file.json", mode="r", encoding="utf-8") as f:
            all_objs = json.load(f)

        self.assertIn(bm_key, all_objs)
        # Test that the same time of update is save and accessed
        bm_dict = all_objs[bm_key]
        self.assertEqual(bm.name, bm_dict['name'])

        # Confirm that the content saved to `file.json` is retrived as a dict
        self.assertIsInstance(all_objs, dict)

    def test_save_no_arg(self):
        """
        Test that the `save()` method takes no argument
        """
        bm1 = BaseModel()
        bm2 = BaseModel()

        with self.assertRaises(TypeError):
            self.fs.save(bm1)

        with self.assertRaises(TypeError):
            self.fs.save(bm1, bm2)

    def test_method_reload(self):
        """
        Testcase for the `reload` method, testing its functionalities
        """
        before_reload = self.fs.all()

        bm = BaseModel()
        bm.save()  # Save the new object in json file

        self.fs.reload()
        after_reload = self.fs.all()

        self.assertNotEqual(before_reload, after_reload)

    def test_reload_no_arg(self):
        """
        Test that the `reload()` method takes no argument
        """
        with self.assertRaises(TypeError):
            self.fs.reload('User')

        with self.assertRaises(TypeError):
            self.fs.reload('User', 'City')

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
        del self.fs
