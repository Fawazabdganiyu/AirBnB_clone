#!/usr/bin/python3
"""
Module Name: models/__init__.py
Description: This module uses `FileStorage` class to create a unique instance

"""
from models.engine import file_storage


# Create a FileStorage instance
storage = file_storage.FileStorage()
storage.reload()
