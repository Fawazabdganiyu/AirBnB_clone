#!/usr/bin/python3
"""
Module Name: tests/test_console.py
Description: This module test the interpreter functionallity.
"""
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import unittest


class TestConsole(unittest.TestCase):
    """
    Test console
    """
    def test_help(self):
        """
        Test that help is working
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
