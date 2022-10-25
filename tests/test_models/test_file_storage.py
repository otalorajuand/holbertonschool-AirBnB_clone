#!/usr/bin/python3
"""
Unittest for class FileStorage
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import os
import models


class TestFileStorage(unittest.TestCase):

    def test_file_path(self):

        file_1 = FileStorage()
        self.assertTrue(file_1._FileStorage__file_path == 'file.json')

    """
    def test_objs(self):

        b_1 = BaseModel()
        self.assertTrue(b_1 in models.storage.all())
    """
