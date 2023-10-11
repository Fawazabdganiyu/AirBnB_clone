"""
Module Name: models/__init__.py
Description: This module uses `FileStorage` class to create a unique instance

"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
