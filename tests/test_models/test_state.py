#!/usr/bin/python3
"""
Module Name: test_state
Description: Provides a test suite for the `State` class located inside
    the state module
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestStateClass(unittest.TestCase):
    """
    Test-suite for `State` class instances
    """
    def test_state_1(self):
        """
        Test if the State class exist
        """
        kaduna = None
        kaduna = State()
        self.assertIsNotNone(kaduna)

    def test_state_2(self):
        """
        Test State instances / objects
        """
        state1 = State()
        state2 = State()
        state3 = State()

        self.assertTrue(isinstance(state1, State))
        self.assertTrue(isinstance(state2, State))
        self.assertTrue(isinstance(state3, State))

    def test_state_inheritance(self):
        """
        Test that the State class inherited from the BaseModel class
        """
        state1 = State()
        state2 = State()
        state3 = State()

        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(issubclass(State, BaseModel))
