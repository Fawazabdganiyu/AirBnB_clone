"""
Module Name: tests/test_models/test_base_model.py
Description: This module tests the class `BaseModel` in the module.

"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A definition of `TestBaseModel` that inherites from `TestCase`
    """

    def test_instances(self):
        """Test that objects from the class are instances of the class
        """
        bm1 = BaseModel()
        bm2 = BaseModel()

        self.assertIsInstance(bm1, BaseModel)
        self.assertIsInstance(bm2, BaseModel)
        self.assertIsNot(bm1, bm2)

    def test_attributes(self):
        """Test that an instance has all the attributes in the constructor
        """
        bm = BaseModel()

        self.assertIsNotNone(bm.id)
        self.assertIsNotNone(bm.created_at)
        self.assertIsNotNone(bm.updated_at)

    def test_id_is_str(self):
        """Test that id type is `str`.
        """
        bm = BaseModel()

        self.assertIsInstance(bm.id, str)

    def test_unique_attributes(self):
        """Test that the instance ids are unique
        """
        bm1 = BaseModel()
        bm2 = BaseModel()

        self.assertNotEqual(bm1.id, bm2.id)
        self.assertNotEqual(bm1.created_at, bm2.created_at)
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

    def test_str(self):
        """Test the __str__ method
        """
        bm = BaseModel()

        expected = f"[BaseModel] ({bm.id}) {bm.__dict__}"

        self.assertEqual(str(bm), expected)

    def test_save_method(self):
        """Test that save actually update the updated time
        """
        bm = BaseModel()
        first_update = bm.updated_at

        bm.name = 'Test Model'

        bm.save()

        second_update = bm.updated_at

        self.assertNotEqual(first_update, second_update)

    def test_no_update_save(self):
        """Test that `updated_at` is constant when new attribute is added
        """
        bm = BaseModel()
        first_update = bm.updated_at

        bm.save()

        second_update = bm.updated_at
        self.assertNotEqual(first_update, second_update)

    def test_save_with_arg(self):
        """Test that TypeError is raised when `save` is called
        with any argument
        """
        bm = BaseModel()

        with self.assertRaises(TypeError):
            bm.save("update")

    def test_to_dict_dictionary(self):
        """Test that the method returns a dictionary
        """
        bm = BaseModel()

        self.assertIsInstance(bm.to_dict(), dict)

    def test_to_dict_attributes(self):
        """Test that the method return all the instance attribute
        together with a key `__class__`
        """
        bm = BaseModel()

        bm.name = "Test Model"
        bm.age = "infant"

        bm_dict = {'__class__': 'BaseModel', **bm.__dict__}
        bm_dict['created_at'] = bm_dict['created_at'].isoformat()
        bm_dict['updated_at'] = bm_dict['updated_at'].isoformat()

        expected_dict = bm.to_dict()

        self.assertEqual(bm_dict, expected_dict)

    def test_to_dict_with_an_arg(self):
        """Test that a TypeError is raised when an argument is passed to the
        method
        """
        bm = BaseModel()

        with self.assertRaises(TypeError):
            bm.to_dict("bm")

    def test_type_created_at(self):
        """Test that the type of `created_at` is `str` after applying the
        method `to_dict`.
        """
        bm = BaseModel()

        bm_dict = bm.to_dict()

        self.assertIsInstance(bm_dict['created_at'], str)

    def test_type_updated_at(self):
        """Test that the type of `updated_at` is `str` after applying the
        method `to_dict`.
        """
        bm = BaseModel()

        bm_dict = bm.to_dict()

        self.assertIsInstance(bm_dict['updated_at'], str)
        
