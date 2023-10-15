#!/usr/bin/python3
"""
Module Name: test_review
Description: Provides a test suite for the `Review` class located inside
    the `models.review` module
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReviewClass(unittest.TestCase):
    """
    Test-suite for `Place` class instances
    """
    def test_review_1(self):
        """
        Test if the `Review` class exist
        """
        good_review = None
        good_review = Review()
        self.assertIsNotNone(good_review)

    def test_review_2(self):
        """
        Test `Review` instances / objects
        """
        good_review = Review()
        bad_review = Review()
        mid_review = Review()

        self.assertTrue(isinstance(good_review, Review))
        self.assertTrue(isinstance(bad_review, Review))
        self.assertTrue(isinstance(mid_review, Review))

    def test_review_inheritance(self):
        """
        Test that the `Review` class inherited from the BaseModel class
        """
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_attributes(self):
        """
        Test that the `Review` class has its attributes
        """
        review = Review()

        self.assertIn("text", dir(review))
        self.assertIn("place_id", dir(review))
        self.assertIn("user_id", dir(review))

    def test_review_attributes_str(self):
        """
        Test that the `Review` class has string attributes
        """
        review = Review()

        self.assertTrue(isinstance(review.text, str))
        self.assertTrue(isinstance(review.place_id, str))
        self.assertTrue(isinstance(review.user_id, str))

    def test_review_has_BaseModels_methods(self):
        """
        Test that class `Review` has all BaseModel's method
        """
        review = Review()

        self.assertIn("created_at", dir(review))
        self.assertIn("updated_at", dir(review))
        self.assertIn("save", dir(review))
        self.assertIn("id", dir(review))
        self.assertIn("to_dict", dir(review))
