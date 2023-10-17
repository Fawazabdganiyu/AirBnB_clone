#!/usr/bin/python3
"""
Module Name: tests/test_console.py
Description: This module test the interpreter functionallity.
"""
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import cmd
import unittest


class TestConsole(unittest.TestCase):
    """
    Test console
    """
    def test_subclass(self):
        """
        Test that `HBNBCommand` inherited from `cmd` module.
        """
        self.assertTrue(issubclass(HBNBCommand, cmd.Cmd))

    def test_isistance(self):
        """
        Test that `HBNBCommand` is instance of `cmd`.
        """
        self.assertNotIsInstance(HBNBCommand, cmd.Cmd)

    def test_quit(self):
        """
        Test quit command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_quit_help(self):
        """
        Test quit help doc
        """
        output = ("Quit command to exit the program")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")

        self.assertEqual(output, f.getvalue().strip())

    def test_EOF_help(self):
        """
        Test that EOF doc is displayed
        """
        output = ("Exit the program on receiving EOF signal")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")

        self.assertEqual(output, f.getvalue().strip())

    def test_EOF(self):
        """
        Test that EOF returns True for quiting.
        """
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_promt(self):
        """
        Test that the expexted prompt is displayed
        """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_help(self):
        """
        Test that help is working
        """
        output = ("Documented commands (type help <topic>):\n"
                  "========================================\n"
                  "EOF  all  count  create  destroy  help  quit  show  update")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")

        self.assertEqual(f.getvalue().strip(), output)

    def test_empty_line(self):
        """
        Test that nothing is executed with empty line + `ENTER`.
        """
        output = ""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
        self.assertEqual(output, f.getvalue().strip())
